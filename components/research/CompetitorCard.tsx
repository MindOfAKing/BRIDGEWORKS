import { ExternalLink } from "lucide-react";
import type { Competitor } from "@/lib/types";
import { Card } from "@/components/ui/Card";
import { Badge } from "@/components/ui/Badge";

interface CompetitorCardProps {
  competitor: Competitor;
}

export function CompetitorCard({ competitor }: CompetitorCardProps) {
  return (
    <Card hover className="flex flex-col gap-4">
      {/* Header */}
      <div className="flex items-start justify-between gap-2">
        <div>
          <h3 className="font-semibold text-base" style={{ color: "var(--text-primary)" }}>
            {competitor.name}
          </h3>
          {competitor.website && (
            <a
              href={`https://${competitor.website}`}
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-1 text-xs hover:text-blue-400 transition-colors mt-0.5"
              style={{ color: "var(--text-muted)" }}
            >
              {competitor.website}
              <ExternalLink className="h-3 w-3" />
            </a>
          )}
        </div>
        {competitor.pricePoint && (
          <Badge variant="muted" className="shrink-0">
            {competitor.pricePoint}
          </Badge>
        )}
      </div>

      {/* Description */}
      <p className="text-sm leading-relaxed" style={{ color: "var(--text-secondary)" }}>
        {competitor.description}
      </p>

      {/* Target audience */}
      {competitor.targetAudience && (
        <div>
          <Badge variant="blue">{competitor.targetAudience}</Badge>
        </div>
      )}

      {/* Strengths & Weaknesses */}
      <div className="grid grid-cols-2 gap-3 pt-2 border-t" style={{ borderColor: "var(--border-subtle)" }}>
        <div>
          <p className="text-xs font-semibold mb-2" style={{ color: "var(--success)" }}>
            Strengths
          </p>
          <ul className="space-y-1">
            {competitor.strengths.map((s, i) => (
              <li key={i} className="flex items-start gap-1.5 text-xs" style={{ color: "var(--text-secondary)" }}>
                <span className="mt-1 h-1.5 w-1.5 rounded-full shrink-0" style={{ backgroundColor: "var(--success)" }} />
                {s}
              </li>
            ))}
          </ul>
        </div>
        <div>
          <p className="text-xs font-semibold mb-2" style={{ color: "var(--warning)" }}>
            Weaknesses
          </p>
          <ul className="space-y-1">
            {competitor.weaknesses.map((w, i) => (
              <li key={i} className="flex items-start gap-1.5 text-xs" style={{ color: "var(--text-secondary)" }}>
                <span className="mt-1 h-1.5 w-1.5 rounded-full shrink-0" style={{ backgroundColor: "var(--warning)" }} />
                {w}
              </li>
            ))}
          </ul>
        </div>
      </div>
    </Card>
  );
}
