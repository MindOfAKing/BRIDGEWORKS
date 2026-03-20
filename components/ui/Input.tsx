import { cn } from "@/lib/utils";

interface InputProps extends React.InputHTMLAttributes<HTMLInputElement> {
  label?: string;
  hint?: string;
  error?: string;
  charCount?: { current: number; max: number };
}

export function Input({
  label,
  hint,
  error,
  charCount,
  className,
  id,
  ...props
}: InputProps) {
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
      <input
        id={id}
        className={cn(
          "w-full rounded-lg border px-4 py-2.5 text-sm transition-colors",
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
