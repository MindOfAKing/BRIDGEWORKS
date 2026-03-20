# BRIDGEWORKS

## Project Overview

BRIDGEWORKS is an AI-powered competitive intelligence platform for entrepreneurs and startups. The core feature is a **Market Research tool**: users input a niche or market and receive a structured competitive analysis report — covering key players, market gaps, and positioning recommendations — powered by Claude.

## Tech Stack

- **Framework**: Next.js (App Router) + TypeScript
- **Styling**: Tailwind CSS (dark navy theme)
- **AI**: Anthropic Claude API (`@anthropic-ai/sdk`)
- **Validation**: Zod
- **Icons**: lucide-react
- **Deploy**: Vercel

## Development Setup

```bash
# Install dependencies
npm install

# Create environment file
cp .env.example .env.local
# Add your ANTHROPIC_API_KEY to .env.local

# Start dev server
npm run dev
```

App runs at `http://localhost:3000`.

## Common Commands

| Command | Description |
|---------|-------------|
| `npm run dev` | Start development server |
| `npm run build` | Production build |
| `npm start` | Run production build locally |

## Project Structure

```
BRIDGEWORKS/
├── app/
│   ├── api/analyze/route.ts   # POST /api/analyze — calls Claude, returns report
│   ├── layout.tsx
│   ├── page.tsx               # Main page (home)
│   └── globals.css
├── components/
│   ├── ui/                    # Button, Card, Badge, Input, Textarea
│   ├── layout/                # Header
│   ├── research/              # ResearchForm, ReportViewer, section cards
│   └── marketing/             # HeroSection
├── lib/
│   ├── types.ts               # CompetitiveReport and related interfaces
│   ├── anthropic.ts           # Singleton Anthropic client
│   ├── prompts.ts             # System + user prompt builders
│   ├── parsers.ts             # safeParseReport() — JSON safety layer
│   └── utils.ts               # cn() helper
├── .env.example               # Required env vars (safe to commit)
└── CLAUDE.md                  # This file
```

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `ANTHROPIC_API_KEY` | Yes | Get from console.anthropic.com |
| `ANTHROPIC_MODEL` | No | Default: `claude-sonnet-4-6` |

## Key Architectural Notes

- **API route** (`app/api/analyze/route.ts`): validates input with Zod, calls Claude, parses JSON response
- **Prompt engineering** (`lib/prompts.ts`): Claude is instructed to return raw JSON only (no markdown fences), with a defined schema
- **Parser safety** (`lib/parsers.ts`): `safeParseReport()` strips any accidental code fences and validates required fields before returning typed data
- **No auth/database**: Phase 1 is stateless — reports live in React state only

## Git Workflow

### Branch Naming
- Feature branches: `claude/<description>-<session-id>`
- Never push directly to `main` or `master`

### Pushing Changes
```bash
git push -u origin <branch-name>
```

### Commit Messages
Imperative mood, concise:
- "Add streaming to analyze route"
- "Fix competitor card layout on mobile"

## Code Conventions

- Keep changes minimal and focused on the task
- Avoid over-engineering or adding features not explicitly requested
- Validate user input at system boundaries (API routes); trust internal code
- Do not introduce security vulnerabilities (injection, XSS, etc.)
