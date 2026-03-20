# BRIDGEWORKS

## Project Overview

BRIDGEWORKS is a project hosted at [MindOfAKing/BRIDGEWORKS](http://local_proxy@127.0.0.1:35397/git/MindOfAKing/BRIDGEWORKS). This file provides guidance for Claude Code when working in this repository.

## Git Workflow

### Branch Naming

- Feature branches: `claude/<description>-<session-id>`
- Never push directly to `main` or `master`

### Pushing Changes

```bash
git push -u origin <branch-name>
```

### Commit Messages

Write concise, descriptive commit messages in the imperative mood:
- "Add authentication module"
- "Fix null pointer in data parser"
- "Update CI pipeline to use Node 20"

## Development Setup

> Update this section once the project tech stack is established.

```bash
# Clone the repository
git clone <repo-url>
cd BRIDGEWORKS
```

## Common Commands

> Populate this section with build, test, and run commands as the project grows.

| Command | Description |
|---------|-------------|
| TBD     | Build the project |
| TBD     | Run tests |
| TBD     | Start development server |

## Testing

> Add test instructions here once a testing framework is configured.

Always run tests before committing:
```bash
# TBD: add test command
```

## Code Conventions

- Keep changes minimal and focused on the task at hand
- Avoid over-engineering or adding features not explicitly requested
- Validate user input at system boundaries; trust internal code
- Do not introduce security vulnerabilities (SQL injection, XSS, command injection, etc.)

## Project Structure

> Update this section as the project structure takes shape.

```
BRIDGEWORKS/
├── CLAUDE.md       # This file
└── ...
```
