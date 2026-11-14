# ASTROMED — Space Apps Challenge 2026
## Presentation (7 slides)

---

## Slide 1 — ASTROMED
**Health, understood. Even beyond Earth.**

An explainable crew-health self-monitoring dashboard for long-duration space missions.

**The promise:** Collect → Compare → Explain → Act.

Personal trends, clear alerts and mission-health context — in one crew-facing tool.

**Team:** Nazarii Shchur · Vlad Moskaliuk · Viktoria Moisiievych · Tatkov Maksym

---

## Slide 2 — The challenge
**Long missions make health self-awareness mission-critical.**

Astronauts face five interconnected hazards, while distance from Earth limits immediate support.

**Spaceflight hazards**
- Radiation
- Isolation & confinement
- Distance from Earth
- Altered gravity
- Hostile / closed environments

**Health consequences**
- Cardiovascular changes
- Bone and muscle loss
- Immune changes
- Sleep and behavioral health
- Nutrition and metabolic risks

**The gap:** Crew members need a clear way to collect indicators, notice meaningful changes and decide when to follow mission medical procedures — without relying on a black-box diagnosis.

---

## Slide 3 — Our solution
**ASTROMED turns check-ins into understandable health trends.**

A crew-facing interface designed for quick self-assessment and transparent decision support.

1. **Collect:** Heart rate, blood pressure, temperature, SpO₂, respiration, glucose, sleep, mood and radiation dose.
2. **Compare:** Per-person rolling baseline, trend charts, deviation flags and time-series context.
3. **Explain:** Every alert names the metric and the reason. No opaque AI diagnosis.
4. **Act:** Re-check a measurement, log context and follow approved mission medical procedures.

---

## Slide 4 — Prototype
**A working dashboard — not just a concept.**

The current build runs locally as a responsive Dash web app.

**Mission overview**
- Crew selector
- Eight indicator cards
- 24-hour cardiovascular, oxygenation and temperature trends
- Explainable attention queue
- Mission hazard context and demo kit-priority view

**Crew check-in + science**
- Interactive entry form for 10 health/context indicators
- Session-only check-in record
- Dedicated evidence tab with all five challenge resources
- Plain-language methodology and safety boundaries

---

## Slide 5 — NASA & partner resources
**Five challenge resources shape the science layer.**

The resources are research and guidance pages — not a unified live astronaut telemetry dataset.

**NASA Human Research Program**
- 5 Hazards of Human Spaceflight
- Risks of Human Spaceflight
- Ongoing HRP Research in Space

Used for hazard framing, risk-to-indicator context and research direction.

**Canadian Space Agency · Partner**
- Monitoring Radiation for Astronaut Health
- Why Do We Conduct Science Experiments in Space?

Used for radiation-monitoring context and the role of space-based research.

Additional research pathways: NASA OSDR · NASA Life Sciences Data Portal. Exact study datasets are future integrations, not claimed as ingested.

---

## Slide 6 — Scientific integrity
**We show what is real, simulated and still to validate.**

Trust is part of the product — especially when health information is involved.

**Current prototype**
- Synthetic demo telemetry
- User-entered demo check-ins
- Personal baseline comparison
- Explainable heuristic flags

**Not claimed**
- No real astronaut records
- No sensor hardware integration
- No clinically validated thresholds
- No AI diagnostic model

**Safety boundary:** Not a medical device. No diagnosis or treatment. Operational thresholds and actions require flight-surgeon approval and mission protocols.

---

## Slide 7 — Impact & next steps
**A practical step toward crew autonomy on deep-space missions.**

ASTROMED makes complex health signals easier to notice, understand and discuss.

**Immediate value**
- One view of physical and behavioral indicators
- Individual trend awareness
- Clear, explainable attention flags

**Next development**
- Integrate cited OSDR / NLSP study datasets
- Validate workflows with medical experts
- Offline-first storage and sensor interfaces

**Long-term vision**
- Support crew autonomy
- Improve human-health research translation
- Adapt to spacecraft, lunar and Mars habitats

*ASTROMED · Python / Dash / Plotly / Pandas · Demo data clearly labelled · Not for clinical use*
