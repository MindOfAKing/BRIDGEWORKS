import { Zap } from "lucide-react";

export function Header() {
  return (
    <header
      className="sticky top-0 z-10 border-b backdrop-blur-sm"
      style={{
        backgroundColor: "rgba(10, 15, 30, 0.8)",
        borderColor: "var(--border-subtle)",
      }}
    >
      <div className="mx-auto max-w-6xl px-4 sm:px-6 py-4 flex items-center gap-2">
        <div
          className="flex h-7 w-7 items-center justify-center rounded-md"
          style={{ backgroundColor: "var(--accent-blue)" }}
        >
          <Zap className="h-4 w-4 text-white" />
        </div>
        <span className="font-bold text-lg tracking-tight" style={{ color: "var(--text-primary)" }}>
          BRIDGE<span style={{ color: "var(--accent-blue)" }}>WORKS</span>
        </span>
        <span
          className="ml-2 rounded-full border px-2 py-0.5 text-xs font-medium"
          style={{
            borderColor: "var(--border-subtle)",
            color: "var(--text-muted)",
            backgroundColor: "var(--bg-elevated)",
          }}
        >
          Beta
        </span>
      </div>
    </header>
  );
}
