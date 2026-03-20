export interface Competitor {
  name: string;
  description: string;
  strengths: string[];
  weaknesses: string[];
  pricePoint?: string | null;
  targetAudience?: string | null;
  website?: string | null;
}

export interface MarketGap {
  title: string;
  description: string;
  opportunity: string;
}

export interface PositioningRecommendation {
  angle: string;
  rationale: string;
  targetSegment: string;
}

export interface CompetitiveReport {
  executiveSummary: string;
  marketOverview: string;
  competitors: Competitor[];
  marketGaps: MarketGap[];
  positioningRecommendations: PositioningRecommendation[];
}

export interface AnalyzeRequest {
  market: string;
  context?: string;
}

export interface AnalyzeResponse {
  report: CompetitiveReport;
}
