# EVEZ Cognition API

**AI Agent Forensics as a Service.** Detect hallucinations, safety risks, and inconsistencies in LLM outputs.

## What It Detects

| Category | Signals |
|----------|---------|
| **Hallucination** | Vague quantifiers, hedging language, unsupported claims, confident falsehoods, fabricated entities |
| **Safety** | PII (SSN-like), API keys, email addresses, IP addresses |
| **Consistency** | Contradiction markers, temporal conflicts |
| **Quality** | Lexical diversity, repetition ratio, sentence structure |

## Verdicts

`CLEAN` → `SUSPICIOUS` → `HIGH_RISK` → `CRITICAL`

## Quick Start

```bash
# Analyze an agent output
curl -X POST http://localhost:8080/analyze \
  -H "Content-Type: application/json" \
  -d '{"output": "Studies show that approximately 95% of experts say this is definitely true.", "agent_id": "my-agent-v1"}'

# Response:
# {"verdict": "SUSPICIOUS", "risk_score": 45.2, "hallucination": {"score": 1.2, "flags": [...]}, ...}
```

### Docker

```bash
docker build -t evez-cognition-api .
docker run -p 8080:8080 evez-cognition-api
```

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/health` | Service health |
| POST | `/analyze` | Analyze single output |
| POST | `/batch` | Analyze multiple outputs |
| GET | `/model-info` | Detection model details |
| POST | `/infer` | Groq LLM inference (if GROQ_API_KEY set) |

## Architecture

- **Pure Python** — no ML model required, regex + heuristic forensics engine
- **FastAPI** — async, auto-generated OpenAPI docs at `/docs`
- **Docker** — multi-stage, non-root, health check
- **Optional Groq** — add `GROQ_API_KEY` for LLM-assisted inference

## License

MIT
