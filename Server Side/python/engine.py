import os
import re

import numpy as np

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from sentence_transformers import SentenceTransformer

from intents_new import intents
from command_registry import COMMAND_REGISTRY

os.environ["HF_HUB_OFFLINE"] = "1"
# ---------------------------------------------------------
# Offline model configuration
# ---------------------------------------------------------




# ---------------------------------------------------------
# Load model
# ---------------------------------------------------------

model = SentenceTransformer(
    "intfloat/multilingual-e5-small"
)


# ---------------------------------------------------------
# Build intent embeddings
# ---------------------------------------------------------

examples = []
labels = []

for intent, exs in intents.items():
    examples += exs
    labels += [intent] * len(exs)


emb = model.encode(
    ["passage: " + e for e in examples],
    normalize_embeddings=True
)


app = FastAPI()


class PredictRequest(BaseModel):
    input: str


class PredictResponse(BaseModel):
    output: str
    error: str = ""


# ---------------------------------------------------------
# Intent classification
# ---------------------------------------------------------

def classify(query, threshold=0.75):
    q = model.encode(
        ["query: " + query],
        normalize_embeddings=True
    )[0]

    sims = emb @ q
    i = np.argmax(sims)
    score = float(sims[i])

    if score >= threshold:
        return (
            labels[i],
            score
        )

    return (
        "unknown",
        score
    )


# Slot extraction
# ---------------------------------------------------------

_PATTERN = re.compile(
    r'"([^"]*)"'
)


def extract_quoted_name(text):
    return [
        item.strip()
        for group in _PATTERN.findall(text)
        for item in group.split(",")
    ]


def extract_slots(intent, text):
    slots = {}
    entry = COMMAND_REGISTRY.get(
        intent,
        {}
    )

    required = entry.get(
        "requires_slots",
        []
    )

    if required:
        names = extract_quoted_name(
            text
        )

        if len(names) == len(required):
            for slot_key, value in zip(
                required,
                names
            ):
                if value:
                    slots[slot_key] = value
    return slots


# ---------------------------------------------------------
# Build command
# ---------------------------------------------------------

def build_command(intent, slots):
    entry = COMMAND_REGISTRY.get(
        intent
    )

    if not entry:
        return (
            None,
            "No known command for this intent"
        )

    missing = [
        s
        for s in entry.get(
            "requires_slots",
            []
        )
        if not slots.get(s)
    ]

    if missing:
        return (
            None,
            f"Missing info: {', '.join(missing)}"
        )

    return (
        entry["template"].format(**slots),
        ""
    )


# ---------------------------------------------------------
# Run inference
# ---------------------------------------------------------

def run(text):
    intent, confidence = classify(
        text
    )

    if intent == "unknown":
        return {
            "output": "",
            "error": (
                "Couldn't confidently classify. "
                f"confidence={confidence:.2f}"
            )
        }

    slots = extract_slots(
        intent,
        text
    )

    cmd, error = build_command(
        intent,
        slots
    )

    if cmd is None:
        return {
            "output": "",
            "error": error
        }

    return {
        "output": cmd,
        "error": ""
    }


@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    user_input = request.input.strip()
    if not user_input:
        raise HTTPException(status_code=400, detail="Missing input")

    try:
        result = run(user_input)
        return PredictResponse(**result)
    except Exception as exc:
        return PredictResponse(output="", error=str(exc))


@app.get("/healthz")
def healthz():
    return {"status": "ok"}