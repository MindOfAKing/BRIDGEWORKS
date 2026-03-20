import { Target } from "lucide-react";
import type { PositioningRecommendation } from "@/lib/types";
import { Card } from "@/components/ui/Card";
import { Badge } from "@/components/ui/Badge";

interface PositioningSectionProps {
  recommendations: PositioningRecommendation[];
}

export function PositioningSection({ recommendations }: PositioningSectionProps) {
  return (
    <section>
      <h2 className="text-xl font-semibold mb-4" style={{ color: "var(--text-primary)" }}>
        Positioning Recommendations
      </h2>
      <div className="space-y-4">
        {recommendations.map((rec, i) => (
          <Card key={i} hover>
            <div className="flex gap-4">
              <div
                className="flex h-8 w-8 shrink-0 items-center justify-center rounded-full text-sm font-bold"
                style={{
                  backgroundColor: "rgba(59, 130, 246, 0.1)",
                  color: "var(--accent-blue)",
                  border: "1px solid rgba(59, 130, 246, 0.2)",
                }}
              >
                {i + 1}
              </div>
              <div className="space-y-2 flex-1">
                <div className="flex items-start justify-between gap-2 flex-wrap">
                  <h3 className="font-semibold text-sm" style={{ color: "var(--text-primary)" }}>
                    {rec.angle}
                  </h3>
                  <Badge variant="cyan">
                    <Target className="h-2.5 w-2.5 mr-1" />
                    {rec.targetSegment}
                  </Badge>
                </div>
                <p className="text-sm" style={{ color: "var(--text-secondary)" }}>
                  {rec.rationale}
                </p>
              </div>
            </div>
          </Card>
        ))}
      </div>
    </section>
  );
}
