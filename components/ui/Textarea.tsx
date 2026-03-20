import { cn } from "@/lib/utils";

interface TextareaProps
  extends React.TextareaHTMLAttributes<HTMLTextAreaElement> {
  label?: string;
  hint?: string;
  error?: string;
  charCount?: { current: number; max: number };
}

export function Textarea({
  label,
  hint,
  error,
  charCount,
  className,
  id,
  ...props
}: TextareaProps) {
  return (
    <div className="flex flex-col gap-1.5">
      {label && (
        <div className="flex items-center justify-between">
          <label
            htmlFor={id}
            className="text-sm font-medium"
            style={{ color: "var(--text-primary)" }}
          >
            {label}
          </label>
          {charCount && (
            <span className="text-xs" style={{ color: "var(--text-muted)" }}>
              {charCount.current}/{charCount.max}
            </span>
          )}
        </div>
      )}
      <textarea
        id={id}
        className={cn(
          "w-full rounded-lg border px-4 py-2.5 text-sm transition-colors resize-none",
          "placeholder:text-slate-600",
          "focus:outline-none focus:ring-2 focus:ring-blue-500/50 focus:border-blue-500/50",
          error ? "border-red-500/50" : "",
          className
        )}
        style={{
          backgroundColor: "var(--bg-elevated)",
          borderColor: error ? undefined : "var(--border-subtle)",
          color: "var(--text-primary)",
        }}
        rows={3}
        {...props}
      />
      {hint && !error && (
        <p className="text-xs" style={{ color: "var(--text-muted)" }}>
          {hint}
        </p>
      )}
      {error && <p className="text-xs text-red-400">{error}</p>}
    </div>
  );
}
