# CEEFM Remotion Video Render Notes

## Status

Codex installed Remotion and built the video project from Claude Code's script deliverable:

`C:\Users\ELITEX21012G2\Projects\bridgeworks-workspace\clients\ceefm\deliverables\VIDEO-SCRIPT-GOOGLE-ADS-EN-HU.md`

TypeScript check passes:

```powershell
npx.cmd tsc --noEmit
```

Rendering is blocked inside the Codex sandbox by:

```txt
Error: spawn EPERM
```

This happens when Remotion tries to launch Chrome Headless Shell. The Chrome binary has already been downloaded under `node_modules\.remotion`, so the next render from a normal developer shell should not need a large browser download again.

## Render All Files

From this folder:

```powershell
cd C:\Users\ELITEX21012G2\Projects\bridgeworks-workspace\clients\ceefm\brand-visuals\remotion-video
npm.cmd run render
```

## Render In Smaller Batches

```powershell
npm.cmd run render:15s:en
npm.cmd run render:15s:hu
npm.cmd run render:30s:en
npm.cmd run render:30s:hu
```

## Expected Outputs

Files will be written to:

`C:\Users\ELITEX21012G2\Projects\bridgeworks-workspace\clients\ceefm\brand-visuals\remotion-video\out`

- `ceefm-ad-15s-16x9-EN.mp4`
- `ceefm-ad-15s-16x9-HU.mp4`
- `ceefm-ad-15s-1x1-EN.mp4`
- `ceefm-ad-15s-1x1-HU.mp4`
- `ceefm-ad-15s-9x16-EN.mp4`
- `ceefm-ad-15s-9x16-HU.mp4`
- `ceefm-ad-30s-16x9-EN.mp4`
- `ceefm-ad-30s-16x9-HU.mp4`
- `ceefm-ad-30s-1x1-EN.mp4`
- `ceefm-ad-30s-1x1-HU.mp4`
- `ceefm-ad-30s-9x16-EN.mp4`
- `ceefm-ad-30s-9x16-HU.mp4`

## Notes

- No voiceover is included.
- No music bed is included yet. Add licensed instrumental music later if required.
- Design follows Claude's dark green, gold, ivory script direction.
- Logo source is copied to `public/ceefm-logo.png`.
