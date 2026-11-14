"""Synthetic crew telemetry for the demonstrator. No real astronaut records."""
from datetime import datetime, timedelta
import random
import pandas as pd

ASTRONAUTS = ["Commander", "Flight Engineer", "Mission Specialist"]


def generate_history(hours: int = 24, seed: int = 7) -> pd.DataFrame:
    rng = random.Random(seed)
    now = datetime.now().replace(second=0, microsecond=0)
    rows = []
    for idx, person in enumerate(ASTRONAUTS):
        for step in range(hours * 4 + 1):
            ts = now - timedelta(minutes=15 * (hours * 4 - step))
            row = {
                "timestamp": ts, "astronaut": person,
                "heart_rate": round(rng.gauss(68 + idx * 3, 4), 1),
                "systolic": round(rng.gauss(116, 6), 1),
                "diastolic": round(rng.gauss(74, 5), 1),
                "temperature": round(rng.gauss(36.7, .15), 2),
                "spo2": round(min(100, rng.gauss(98, .5)), 1),
                "respiration": round(rng.gauss(14, 1.2), 1),
                "glucose": round(rng.gauss(95, 8), 1),
                "sleep_hours": round(max(0, rng.gauss(7.2, .6)), 1),
                "mood": rng.choice(["Good", "Good", "Okay", "Low"]),
                "radiation_mSv": round(max(0, rng.gauss(.012, .003)), 4),
                "data_origin": "SYNTHETIC DEMO DATA",
            }
            if idx == 1 and 45 <= step <= 49:
                row["heart_rate"] += 28
                row["spo2"] -= 6
            if idx == 2 and 70 <= step <= 74:
                row["sleep_hours"] = 3.2
                row["mood"] = "Low"
            rows.append(row)
    return pd.DataFrame(rows)
