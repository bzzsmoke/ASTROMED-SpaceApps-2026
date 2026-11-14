"""Transparent priority queue for demo medical-kit allocation (not a care protocol)."""
def allocate_medical_kits(astronaut_risks: dict, available_kits: int) -> dict:
    if available_kits < 0:
        raise ValueError("Available kits cannot be negative.")
    ranked = sorted(astronaut_risks.items(), key=lambda item: item[1], reverse=True)
    selected = [name for name, score in ranked if score > 0][:available_kits]
    return {
        "assigned": selected,
        "not_assigned": [name for name, score in ranked if score > 0 and name not in selected],
        "ranking": ranked,
        "kits_used": len(selected),
        "kits_available": available_kits,
        "note": "Demo prioritization only. A flight surgeon / mission protocol must determine actual care and resource allocation.",
    }
