"""Transparent, non-diagnostic astronaut health trend assessment.

Thresholds in this prototype are demonstration heuristics, NOT flight-medicine limits.
The preferred signal is deviation from each crew member's own rolling baseline.
"""
from __future__ import annotations

METRICS = {
    "heart_rate": {"label": "Resting heart rate", "unit": "bpm", "baseline_delta": 15},
    "systolic": {"label": "Systolic blood pressure", "unit": "mmHg", "baseline_delta": 20},
    "diastolic": {"label": "Diastolic blood pressure", "unit": "mmHg", "baseline_delta": 12},
    "temperature": {"label": "Body temperature", "unit": "°C", "baseline_delta": 0.8},
    "glucose": {"label": "Blood glucose", "unit": "mg/dL", "baseline_delta": 35},
    "sleep_hours": {"label": "Sleep duration", "unit": "h", "baseline_delta": 2},
    "spo2": {"label": "SpO₂", "unit": "%", "baseline_delta": 3},
    "respiration": {"label": "Respiratory rate", "unit": "breaths/min", "baseline_delta": 5},
}


def assess_measurement(row: dict, baseline: dict | None = None) -> dict:
    """Return explainable flags based on baseline drift and conservative demo rules."""
    baseline = baseline or {}
    flags: list[dict] = []
    score = 0
    hard_flags = [
        ("heart_rate", lambda x: x < 40 or x > 140, "Heart rate outside demo safety envelope"),
        ("spo2", lambda x: x < 90, "Low SpO₂ in demo rules"),
        ("temperature", lambda x: x < 35.0 or x > 39.0, "Temperature outside demo safety envelope"),
        ("systolic", lambda x: x < 80 or x > 180, "Systolic pressure outside demo safety envelope"),
        ("glucose", lambda x: x < 54 or x > 250, "Glucose outside demo safety envelope"),
    ]
    for key, predicate, message in hard_flags:
        value = row.get(key)
        if value is not None and predicate(float(value)):
            flags.append({"metric": key, "level": "critical", "message": message, "source": "prototype guardrail"})
            score += 3
    for key, spec in METRICS.items():
        value, base = row.get(key), baseline.get(key)
        if value is None or base is None:
            continue
        delta = abs(float(value) - float(base))
        if delta >= spec["baseline_delta"]:
            flags.append({
                "metric": key, "level": "warning",
                "message": f"{spec['label']} changed by {delta:.1f} {spec['unit']} from personal baseline",
                "source": "personal baseline trend"
            })
            score += 1
    critical = any(f["level"] == "critical" for f in flags)
    level = "CRITICAL" if critical else ("WARNING" if score >= 2 else "NOMINAL")
    if not flags:
        flags.append({"metric": "overall", "level": "nominal", "message": "No configured demo rule or baseline drift was detected.", "source": "prototype analysis"})
    return {"risk_score": score, "risk_level": level, "flags": flags,
            "summary": "; ".join(f["message"] for f in flags)}


def calculate_baselines(history, astronaut: str, window: int = 24) -> dict:
    """Calculate per-person rolling means from prior records, excluding latest row."""
    person_rows = history[history["astronaut"] == astronaut].tail(window + 1)
    if len(person_rows) < 2:
        return {}
    prior = person_rows.iloc[:-1]
    return {key: float(prior[key].mean()) for key in METRICS
            if key in prior and prior[key].notna().any()}


def analyze_dataframe(frame):
    if frame.empty:
        return frame.copy()
    analyzed = frame.copy()
    results = [assess_measurement(row) for row in analyzed.to_dict(orient="records")]
    analyzed["risk_level"] = [r["risk_level"] for r in results]
    analyzed["risk_score"] = [r["risk_score"] for r in results]
    analyzed["reasons"] = [r["summary"] for r in results]
    return analyzed
