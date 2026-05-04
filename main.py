"""
EVEZ Cognition API — Distributed inference + agent mesh
"""
from fastapi import FastAPI
import os, time, json
try:
    from groq import AsyncGroq
    groq = AsyncGroq(api_key=os.getenv("GROQ_API_KEY"))
except ImportError:
    groq = None

app = FastAPI(title="EVEZ Cognition API", version="2.0.0")

@app.get("/health")
def health():
    return {"status": "ok", "groq": groq is not None, "ts": int(time.time())}

@app.post("/infer")
async def infer(payload: dict):
    if not groq:
        return {"error": "GROQ_API_KEY not configured"}
    msgs = [{"role": "user", "content": payload.get("prompt", "")}]
    if payload.get("system"): msgs.insert(0, {"role": "system", "content": payload["system"]})
    resp = await groq.chat.completions.create(
        model=payload.get("model", "llama-3.3-70b-versatile"),
        messages=msgs, max_tokens=2048
    )
    return {"response": resp.choices[0].message.content, "model": resp.model,
            "tokens": resp.usage.total_tokens if resp.usage else None}
