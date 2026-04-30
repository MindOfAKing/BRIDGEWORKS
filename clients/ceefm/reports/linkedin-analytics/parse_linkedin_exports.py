from __future__ import annotations

from pathlib import Path
import json
import struct


END = 0xFFFFFFFE
FREE = 0xFFFFFFFF


def read_workbook_stream(path: Path) -> bytes:
    data = path.read_bytes()
    if data[:8] != b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1":
        raise ValueError(f"{path.name} is not a legacy Excel OLE file")

    sector_size = 1 << struct.unpack_from("<H", data, 30)[0]
    first_dir = struct.unpack_from("<I", data, 48)[0]
    difat = list(struct.unpack_from("<109I", data, 76))

    def sector(sec_id: int) -> bytes:
        start = (sec_id + 1) * sector_size
        return data[start : start + sector_size]

    fat: list[int] = []
    for sec_id in difat:
        if sec_id in (FREE, END):
            continue
        fat.extend(struct.unpack("<" + "I" * (sector_size // 4), sector(sec_id)))

    def read_chain(start: int, size: int | None = None) -> bytes:
        out = bytearray()
        sec_id = start
        seen: set[int] = set()
        while sec_id not in (FREE, END) and sec_id < len(fat) and sec_id not in seen:
            seen.add(sec_id)
            out.extend(sector(sec_id))
            sec_id = fat[sec_id]
        return bytes(out if size is None else out[:size])

    directory = read_chain(first_dir)
    for offset in range(0, len(directory), 128):
        entry = directory[offset : offset + 128]
        if len(entry) < 128:
            break
        name_len = struct.unpack_from("<H", entry, 64)[0]
        if name_len < 2:
            continue
        name = entry[: name_len - 2].decode("utf-16le", "ignore")
        entry_type = entry[66]
        start = struct.unpack_from("<I", entry, 116)[0]
        size = struct.unpack_from("<Q", entry, 120)[0]
        if entry_type == 2 and name in {"Workbook", "Book"}:
            return read_chain(start, size)

    raise ValueError(f"No Workbook stream found in {path.name}")


def biff_records(workbook: bytes):
    pos = 0
    while pos + 4 <= len(workbook):
        rec_type, length = struct.unpack_from("<HH", workbook, pos)
        rec_offset = pos
        pos += 4
        payload = workbook[pos : pos + length]
        pos += length
        yield rec_offset, rec_type, payload


def parse_biff_string(data: bytes, pos: int) -> tuple[str, int]:
    cch = struct.unpack_from("<H", data, pos)[0]
    pos += 2
    options = data[pos]
    pos += 1
    has_rich_text = options & 0x08
    has_ext = options & 0x04
    is_unicode = options & 0x01
    rich_runs = 0
    ext_len = 0
    if has_rich_text:
        rich_runs = struct.unpack_from("<H", data, pos)[0]
        pos += 2
    if has_ext:
        ext_len = struct.unpack_from("<I", data, pos)[0]
        pos += 4
    byte_len = cch * (2 if is_unicode else 1)
    raw = data[pos : pos + byte_len]
    pos += byte_len
    text = raw.decode("utf-16le" if is_unicode else "latin1", "ignore")
    pos += 4 * rich_runs
    pos += ext_len
    return text, pos


def parse_sst(records: list[tuple[int, int, bytes]]) -> list[str]:
    for index, (_, rec_type, payload) in enumerate(records):
        if rec_type != 0x00FC:
            continue
        chunks = bytearray(payload)
        cursor = index + 1
        while cursor < len(records) and records[cursor][1] == 0x003C:
            chunks.extend(records[cursor][2])
            cursor += 1

        data = bytes(chunks)
        if len(data) < 8:
            return []
        _total, unique = struct.unpack_from("<II", data, 0)
        strings: list[str] = []
        pos = 8
        for _ in range(unique):
            if pos + 3 > len(data):
                break
            try:
                text, pos = parse_biff_string(data, pos)
            except Exception:
                break
            strings.append(text)
        return strings
    return []


def rk_value(raw: int) -> float:
    divide_by_100 = raw & 1
    is_integer = raw & 2
    if is_integer:
        value = raw >> 2
        if value & 0x20000000:
            value -= 0x40000000
        number = float(value)
    else:
        packed = (raw & 0xFFFFFFFC) << 32
        number = struct.unpack("<d", struct.pack("<Q", packed))[0]
    return number / 100 if divide_by_100 else number


def parse_sheets(path: Path) -> dict[str, list[list[object]]]:
    workbook = read_workbook_stream(path)
    records = list(biff_records(workbook))
    shared_strings = parse_sst(records)

    bounds: list[tuple[str, int]] = []
    for offset, rec_type, payload in records:
        if rec_type != 0x0085 or len(payload) < 8:
            continue
        sheet_offset = struct.unpack_from("<I", payload, 0)[0]
        name_len = payload[6]
        options = payload[7]
        raw = payload[8 : 8 + name_len * (2 if options & 1 else 1)]
        name = raw.decode("utf-16le" if options & 1 else "latin1", "ignore")
        bounds.append((name, sheet_offset))

    sheets: dict[str, list[list[object]]] = {}
    for sheet_index, (name, start_offset) in enumerate(bounds):
        end_offset = bounds[sheet_index + 1][1] if sheet_index + 1 < len(bounds) else len(workbook)
        cells: dict[tuple[int, int], object] = {}
        max_row = 0
        max_col = 0
        for offset, rec_type, payload in records:
            if offset < start_offset or offset >= end_offset:
                continue
            value = None
            row = col = None
            if rec_type == 0x00FD and len(payload) >= 10:
                row, col, _xf, sst_index = struct.unpack_from("<HHHI", payload, 0)
                value = shared_strings[sst_index] if sst_index < len(shared_strings) else ""
            elif rec_type == 0x0203 and len(payload) >= 14:
                row, col, _xf = struct.unpack_from("<HHH", payload, 0)
                value = struct.unpack_from("<d", payload, 6)[0]
            elif rec_type == 0x027E and len(payload) >= 10:
                row, col, _xf = struct.unpack_from("<HHH", payload, 0)
                value = rk_value(struct.unpack_from("<I", payload, 6)[0])
            elif rec_type == 0x0204 and len(payload) >= 8:
                row, col, _xf, text_len = struct.unpack_from("<HHHH", payload, 0)
                value = payload[8 : 8 + text_len].decode("latin1", "ignore")
            elif rec_type == 0x00BD and len(payload) >= 6:
                row, first_col = struct.unpack_from("<HH", payload, 0)
                last_col = struct.unpack_from("<H", payload, len(payload) - 2)[0]
                pos = 4
                for col in range(first_col, last_col + 1):
                    if pos + 6 > len(payload) - 2:
                        break
                    raw = struct.unpack_from("<I", payload, pos + 2)[0]
                    cells[(row, col)] = rk_value(raw)
                    max_row = max(max_row, row)
                    max_col = max(max_col, col)
                    pos += 6
                continue

            if row is not None and col is not None:
                cells[(row, col)] = value
                max_row = max(max_row, row)
                max_col = max(max_col, col)

        rows = []
        for row in range(max_row + 1):
            rows.append([cells.get((row, col), "") for col in range(max_col + 1)])
        sheets[name] = rows

    return sheets


def main() -> None:
    root = Path(__file__).resolve().parent
    base = root / "2026-04"
    out = {}
    for path in sorted(base.glob("*.xls")):
        out[path.name] = parse_sheets(path)
    (root / "parsed-linkedin-exports.json").write_text(
        json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    for filename, sheets in out.items():
        print(f"\n{filename}")
        for sheet_name, rows in sheets.items():
            print(f"  {sheet_name}: {len(rows)} rows")
            for row in rows[:10]:
                print("   ", row)


if __name__ == "__main__":
    main()
