import type { CompetitiveReport } from "./types";

export function safeParseReport(raw: string): CompetitiveReport {
  const cleaned = raw
    .replace(/^```json\s*/i, "")
    .replace(/^```\s*/i, "")
    .replace(/```\s*$/i, "")
    .trim();

  const parsed = JSON.parse(cleaned);

  if (!Array.isArray(parsed.competitors))
    throw new Error("Missing competitors array");
  if (!Array.isArray(parsed.marketGaps))
    throw new Error("Missing marketGaps array");
  if (!Array.isArray(parsed.positioningRecommendations))
    throw new Error("Missing positioningRecommendations array");
  if (typeof parsed.executiveSummary !== "string")
    throw new Error("Missing executiveSummary");
  if (typeof parsed.marketOverview !== "string")
    throw new Error("Missing marketOverview");

  return parsed as CompetitiveReport;
}
