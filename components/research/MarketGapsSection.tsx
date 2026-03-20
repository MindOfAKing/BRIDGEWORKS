import { Lightbulb } from "lucide-react";
import type { MarketGap } from "@/lib/types";
import { Card } from "@/components/ui/Card";

interface MarketGapsSectionProps {
  gaps: MarketGap[];
}

export function MarketGapsSection({ gaps }: MarketGapsSectionProps) {
  return (
    <section>
      <h2 className="text-xl font-semibold mb-4" style={{ color: "var(--text-primary)" }}>
        Market Gaps & Opportunities
      </h2>
      <div className="grid gap-4 md:grid-cols-2">
        {gaps.map((gap, i) => (
          <Card key={i} hover>
            <div className="space-y-3">
              <h3 className="font-semibold text-sm" style={{ color: "var(--text-primary)" }}>
                {gap.title}
              </h3>
              <p className="text-sm" style={{ color: "var(--text-secondary)" }}>
                {gap.description}
              </p>
              <div
                className="rounded-lg p-3 border flex gap-2"
                style={{
                  backgroundColor: "rgba(6, 182, 212, 0.05)",
                  borderColor: "rgba(6, 182, 212, 0.2)",
                }}
              >
                <Lightbulb
                  className="h-4 w-4 shrink-0 mt-0.5"
                  style={{ color: "var(--accent-cyan)" }}
                />
                <p className="text-xs leading-relaxed" style={{ color: "var(--accent-cyan)" }}>
                  {gap.opportunity}
                </p>
              </div>
            </div>
          </Card>
        ))}
      </div>
    </section>
  );
}
