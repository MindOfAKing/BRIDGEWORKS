"use client";

import { useState } from "react";
import { Copy, Check } from "lucide-react";
import type { CompetitiveReport } from "@/lib/types";
import { Card } from "@/components/ui/Card";
import { Button } from "@/components/ui/Button";
import { CompetitorCard } from "./CompetitorCard";
import { MarketGapsSection } from "./MarketGapsSection";
import { PositioningSection } from "./PositioningSection";

interface ReportViewerProps {
  report: CompetitiveReport;
  market: string;
}

export function ReportViewer({ report, market }: ReportViewerProps) {
  const [copied, setCopied] = useState(false);

  function handleCopy() {
    const text = formatReportAsText(report, market);
    navigator.clipboard.writeText(text).then(() => {
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    });
  }

  return (
    <div className="space-y-8 animate-fade-in">
      {/* Report header */}
      <div className="flex items-start justify-between gap-4 flex-wrap">
        <div>
          <p className="text-xs font-semibold uppercase tracking-widest mb-1" style={{ color: "var(--accent-blue)" }}>
            Competitive Intelligence Report
          </p>
          <h2 className="text-2xl font-bold" style={{ color: "var(--text-primary)" }}>
            {market}
          </h2>
        </div>
        <Button variant="secondary" onClick={handleCopy} className="shrink-0">
          {copied ? (
            <>
              <Check className="h-4 w-4" />
              Copied
            </>
          ) : (
            <>
              <Copy className="h-4 w-4" />
              Copy Report
            </>
          )}
        </Button>
      </div>

      {/* Executive Summary */}
      <Card>
        <h2 className="text-lg font-semibold mb-3" style={{ color: "var(--text-primary)" }}>
          Executive Summary
        </h2>
        <p className="text-sm leading-relaxed" style={{ color: "var(--text-secondary)" }}>
          {report.executiveSummary}
        </p>
        <div
          className="mt-4 pt-4 border-t"
          style={{ borderColor: "var(--border-subtle)" }}
        >
          <p className="text-sm leading-relaxed" style={{ color: "var(--text-secondary)" }}>
            {report.marketOverview}
          </p>
        </div>
      </Card>

      {/* Competitors */}
      <section>
        <h2 className="text-xl font-semibold mb-4" style={{ color: "var(--text-primary)" }}>
          Competitor Landscape
          <span
            className="ml-2 text-sm font-normal"
            style={{ color: "var(--text-muted)" }}
          >
            {report.competitors.length} players
          </span>
        </h2>
        <div className="grid gap-4 md:grid-cols-2">
          {report.competitors.map((c, i) => (
            <CompetitorCard key={i} competitor={c} />
          ))}
        </div>
      </section>

      {/* Market Gaps */}
      <MarketGapsSection gaps={report.marketGaps} />

      {/* Positioning */}
      <PositioningSection recommendations={report.positioningRecommendations} />
    </div>
  );
}

function formatReportAsText(report: CompetitiveReport, market: string): string {
  const lines: string[] = [
    `BRIDGEWORKS — Competitive Intelligence Report`,
    `Market: ${market}`,
    ``,
    `EXECUTIVE SUMMARY`,
    report.executiveSummary,
    ``,
    report.marketOverview,
    ``,
    `COMPETITORS`,
    ...report.competitors.map(
      (c) =>
        `• ${c.name}${c.pricePoint ? ` (${c.pricePoint})` : ""}\n  ${c.description}\n  Strengths: ${c.strengths.join(", ")}\n  Weaknesses: ${c.weaknesses.join(", ")}`
    ),
    ``,
    `MARKET GAPS`,
    ...report.marketGaps.map((g) => `• ${g.title}: ${g.description}\n  Opportunity: ${g.opportunity}`),
    ``,
    `POSITIONING RECOMMENDATIONS`,
    ...report.positioningRecommendations.map(
      (r, i) => `${i + 1}. ${r.angle} (Target: ${r.targetSegment})\n   ${r.rationale}`
    ),
  ];
  return lines.join("\n");
}
