import { TrendingUp, Users, Map } from "lucide-react";

const features = [
  { icon: TrendingUp, label: "Competitor Analysis" },
  { icon: Map, label: "Market Gap Detection" },
  { icon: Users, label: "Positioning Strategy" },
];

export function HeroSection() {
  return (
    <div className="text-center space-y-6 pt-16 pb-10">
      <div
        className="inline-flex items-center gap-2 rounded-full border px-3 py-1 text-xs font-medium"
        style={{
          borderColor: "rgba(59,130,246,0.3)",
          backgroundColor: "rgba(59,130,246,0.05)",
          color: "var(--accent-blue)",
        }}
      >
        <span className="h-1.5 w-1.5 rounded-full bg-blue-500 animate-pulse" />
        AI-Powered Competitive Intelligence
      </div>

      <h1
        className="text-4xl sm:text-5xl font-bold tracking-tight leading-tight"
        style={{ color: "var(--text-primary)" }}
      >
        Know Your Competition.
        <br />
        <span style={{ color: "var(--accent-blue)" }}>Find Your Edge.</span>
      </h1>

      <p
        className="mx-auto max-w-xl text-base sm:text-lg"
        style={{ color: "var(--text-secondary)" }}
      >
        Enter any market or niche and get a full competitive intelligence report
        — competitors, gaps, and positioning recommendations — in seconds.
      </p>

      <div className="flex items-center justify-center gap-6 flex-wrap">
        {features.map(({ icon: Icon, label }) => (
          <div
            key={label}
            className="flex items-center gap-2 text-sm"
            style={{ color: "var(--text-muted)" }}
          >
            <Icon className="h-4 w-4" style={{ color: "var(--accent-cyan)" }} />
            {label}
          </div>
        ))}
      </div>
    </div>
  );
}
