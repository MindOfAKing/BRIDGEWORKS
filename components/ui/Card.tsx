import { cn } from "@/lib/utils";

interface CardProps {
  children: React.ReactNode;
  className?: string;
  hover?: boolean;
}

export function Card({ children, className, hover = false }: CardProps) {
  return (
    <div
      className={cn(
        "rounded-xl p-6",
        "border",
        hover && "transition-all duration-200 hover:border-blue-500/50 hover:shadow-[0_0_0_1px_rgba(59,130,246,0.2)]",
        className
      )}
      style={{
        backgroundColor: "var(--bg-surface)",
        borderColor: "var(--border-subtle)",
      }}
    >
      {children}
    </div>
  );
}
