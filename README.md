# ASTROMED — Astronaut Health Self-Monitoring

**NASA Space Apps Challenge 2026 · Health Monitoring Software**

ASTROMED is an explainable crew-health dashboard prototype for long-duration space missions. It brings physiological and behavioral check-ins into one interface, compares readings with a crew member's recent personal baseline, and explains why a change is flagged.

> **Prototype notice:** all dashboard telemetry is synthetic demonstration data or manually entered demo values. ASTROMED does not ingest live NASA astronaut telemetry, connect to medical sensors, diagnose conditions, or replace a flight surgeon.

## Features

- Crew overview with heart rate, blood pressure, temperature, SpO₂, respiration, glucose, sleep, mood and optional radiation context.
- Trend visualizations and personal-baseline comparisons.
- Explainable attention flags that identify the metric and reason.
- Crew check-in workflow.
- Science & Sources section linking the NASA Human Research Program and Canadian Space Agency resources.
- Transparent demo medical-kit prioritization heuristic (not a care protocol).

## Requirements

- Python 3.10 or newer
- Windows, macOS or Linux
- Internet connection for the initial Python dependency installation

## Install and run

### Windows 10/11

1. Install Python from [python.org](https://www.python.org/downloads/). During installation, enable **Add Python to PATH**.
2. Download this repository using **Code → Download ZIP**, then extract it.
3. Open the extracted project folder.
4. In File Explorer, click the folder address bar, type `cmd`, and press Enter. This opens Command Prompt (CMD) directly in the project folder.
5. In the CMD window, run these commands:

```cmd
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python main.py
```


You can also double-click `start.bat` from File Explorer; it installs the requirements and starts the app.

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python main.py
```

Then open **http://127.0.0.1:8050** in your browser. Stop the server with `Ctrl+C`.

## Tests

```bash
python -m unittest discover -s tests -v
```

## NASA and partner-agency resources

These sources provide scientific and mission-risk context; they are **not** live data feeds used by this prototype.

| Agency | Resource | Role in ASTROMED |
|---|---|---|
| NASA HRP | [5 Hazards of Human Spaceflight](https://www.nasa.gov/hrp/hazards/) | Mission hazard framework |
| NASA HRP | [Risks of Human Spaceflight](https://www.nasa.gov/hrp/risks/) | Health-risk context |
| NASA HRP | [Ongoing HRP Research in Space](https://www.nasa.gov/hrp/ongoing-hrp-research/) | Research context and future evidence integration |
| Canadian Space Agency | [Monitoring Radiation for Astronaut Health](https://www.asc-csa.gc.ca/eng/news/articles/2026/2026-02-26-monitoring-radiation-astronaut-health.asp) | Radiation-monitoring context |
| Canadian Space Agency | [Why Do We Conduct Science Experiments in Space?](https://www.asc-csa.gc.ca/eng/iss/science/why-do-we-conduct-science-experiments-in-space.asp) | Space-research context |

Potential future research portals (not currently ingested): [NASA Open Science Data Repository](https://osdr.nasa.gov/) and [NASA Life Sciences Data Portal](https://nlsp.nasa.gov/). Any future dataset integration must cite the exact study, variables, units, access conditions and preprocessing.

## Assessment logic and safety

The prototype uses transparent demonstration heuristics and deviations from personal rolling baselines. These are **not clinically validated thresholds or NASA flight-medicine limits**. The dashboard is not a medical device and must not be used for diagnosis or treatment. Operational thresholds, escalation pathways and countermeasures require approval by qualified flight surgeons and mission medical authorities.

## Technology

Python · Dash · Plotly · Pandas · NumPy · HTML/CSS

## AI disclosure

No AI model is embedded in the application. ChatGPT (OpenAI) was used as an AI-assisted development and writing tool to help revise code, organize documentation and draft presentation materials. It does not process astronaut medical records or make health decisions.

## Project materials

- [Project Story & Judging Q&A (English and Ukrainian)](PROJECT_STORY_AND_JUDGING_QA.md)
- [7-slide demo presentation](ASTROMED_SpaceApps_Demo_7slides.pptx)
- [Project brief and source documentation](README.md)

## Space Apps Project Page — short description

ASTROMED is an explainable crew-health dashboard for long-duration space missions. It brings together key physiological and behavioral indicators, compares readings with each crew member's personal trend baseline, and explains when a change deserves attention. NASA Human Research Program and Canadian Space Agency resources inform the health-risk framework. Demonstration readings are synthetic or user-entered; no live NASA telemetry, medical sensor integration or clinical validation is claimed.

## Team

- Nazarii Shchur
- Vlad Moskaliuk
- Viktoria Moisiievych
- Tatkov Maksym

Update team roles and contact details before final submission if needed.
