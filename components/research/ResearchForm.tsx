"use client";

import { useState } from "react";
import { Search } from "lucide-react";
import type { CompetitiveReport } from "@/lib/types";
import { Input } from "@/components/ui/Input";
import { Textarea } from "@/components/ui/Textarea";
import { Button } from "@/components/ui/Button";

interface ResearchFormProps {
  onReport: (report: CompetitiveReport, market: string) => void;
  onLoading: (loading: boolean) => void;
}

const MAX_MARKET = 200;
const MAX_CONTEXT = 500;

export function ResearchForm({ onReport, onLoading }: ResearchFormProps) {
  const [market, setMarket] = useState("");
  const [context, setContext] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    if (!market.trim()) return;

    setIsLoading(true);
    setError(null);
    onLoading(true);

    try {
      const res = await fetch("/api/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ market: market.trim(), context: context.trim() || undefined }),
      });

      const data = await res.json();

      if (!res.ok) {
        throw new Error(data.error ?? "Analysis failed");
      }

      onReport(data.report, market.trim());
    } catch (err) {
      const msg = err instanceof Error ? err.message : "Something went wrong";
      setError(msg);
      onLoading(false);
    } finally {
      setIsLoading(false);
    }
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <Input
        id="market"
        label="Market / Niche / Company"
        placeholder="e.g. project management software for remote teams"
        value={market}
        onChange={(e) => setMarket(e.target.value.slice(0, MAX_MARKET))}
        charCount={{ current: market.length, max: MAX_MARKET }}
        hint="Describe the market, niche, or a specific competitor you want analyzed"
        disabled={isLoading}
        required
      />
      <Textarea
        id="context"
        label={
          <span>
            Additional Context{" "}
            <span style={{ color: "var(--text-muted)" }}>(optional)</span>
          </span> as unknown as string
        }
        placeholder="e.g. targeting B2B SMBs with under 50 employees, bootstrapped, pricing under $30/mo"
        value={context}
        onChange={(e) => setContext(e.target.value.slice(0, MAX_CONTEXT))}
        charCount={{ current: context.length, max: MAX_CONTEXT }}
        disabled={isLoading}
      />
      {error && (
        <div
          className="rounded-lg border p-3 text-sm text-red-400"
          style={{ borderColor: "rgba(239,68,68,0.3)", backgroundColor: "rgba(239,68,68,0.05)" }}
        >
          {error}
        </div>
      )}
      <Button type="submit" loading={isLoading} disabled={!market.trim()} className="w-full sm:w-auto">
        <Search className="h-4 w-4" />
        {isLoading ? "Analyzing..." : "Analyze Market"}
      </Button>
    </form>
  );
}
