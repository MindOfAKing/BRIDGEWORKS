import { NextRequest, NextResponse } from "next/server";
import { z } from "zod";
import { anthropic, DEFAULT_MODEL } from "@/lib/anthropic";
import { buildSystemPrompt, buildUserPrompt } from "@/lib/prompts";
import { safeParseReport } from "@/lib/parsers";

const AnalyzeSchema = z.object({
  market: z
    .string()
    .min(2, "Market/niche must be at least 2 characters")
    .max(200, "Market/niche must be 200 characters or less"),
  context: z.string().max(500, "Context must be 500 characters or less").optional(),
});

export async function POST(request: NextRequest) {
  let body: unknown;
  try {
    body = await request.json();
  } catch {
    return NextResponse.json({ error: "Invalid JSON body" }, { status: 400 });
  }

  const parsed = AnalyzeSchema.safeParse(body);
  if (!parsed.success) {
    return NextResponse.json(
      { error: parsed.error.issues[0].message },
      { status: 400 }
    );
  }

  const { market, context } = parsed.data;

  try {
    const message = await anthropic.messages.create({
      model: DEFAULT_MODEL,
      max_tokens: 4096,
      system: buildSystemPrompt(),
      messages: [{ role: "user", content: buildUserPrompt(market, context) }],
    });

    const textContent = message.content.find((c) => c.type === "text");
    if (!textContent || textContent.type !== "text") {
      return NextResponse.json(
        { error: "No text response from AI" },
        { status: 500 }
      );
    }

    const report = safeParseReport(textContent.text);
    return NextResponse.json({ report });
  } catch (err) {
    const message = err instanceof Error ? err.message : "Unknown error";
    console.error("Analyze error:", message);
    return NextResponse.json(
      { error: `Analysis failed: ${message}` },
      { status: 500 }
    );
  }
}
