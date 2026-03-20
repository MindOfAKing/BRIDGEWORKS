"use client";

import { useState } from "react";
import type { CompetitiveReport } from "@/lib/types";
import { Header } from "@/components/layout/Header";
import { HeroSection } from "@/components/marketing/HeroSection";
import { ResearchForm } from "@/components/research/ResearchForm";
import { ReportViewer } from "@/components/research/ReportViewer";
import { ReportSkeleton } from "@/components/research/ReportSkeleton";
import { Card } from "@/components/ui/Card";

export default function Home() {
  const [report, setReport] = useState<CompetitiveReport | null>(null);
  const [market, setMarket] = useState("");
  const [loading, setLoading] = useState(false);

  function handleReport(r: CompetitiveReport, m: string) {
    setReport(r);
    setMarket(m);
    setLoading(false);
  }

  function handleLoading(l: boolean) {
    setLoading(l);
    if (l) setReport(null);
  }

  return (
    <div className="min-h-screen" style={{ backgroundColor: "var(--bg-base)" }}>
      <Header />

      <main className="mx-auto max-w-6xl px-4 sm:px-6 pb-24">
        <HeroSection />

        {/* Input form */}
        <Card className="mb-10">
          <ResearchForm onReport={handleReport} onLoading={handleLoading} />
        </Card>

        {/* Results area */}
        {loading && <ReportSkeleton />}
        {report && !loading && (
          <ReportViewer report={report} market={market} />
        )}

        {/* Empty state */}
        {!loading && !report && (
          <div className="text-center py-16 space-y-3">
            <div
              className="mx-auto h-16 w-16 rounded-2xl flex items-center justify-center text-3xl"
              style={{ backgroundColor: "var(--bg-surface)", border: "1px solid var(--border-subtle)" }}
            >
              🔍
            </div>
            <p className="font-medium" style={{ color: "var(--text-primary)" }}>
              Ready to analyze
            </p>
            <p className="text-sm" style={{ color: "var(--text-muted)" }}>
              Enter a market or niche above to generate your competitive intelligence report
            </p>
          </div>
        )}
      </main>
    </div>
  );
}
