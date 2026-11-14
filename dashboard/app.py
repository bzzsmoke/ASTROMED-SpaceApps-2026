"""ASTROMED | Astronaut Health Self-Monitoring prototype."""
from dash import Dash, dcc, html, Input, Output, State
import plotly.graph_objects as go
from monitoring.sensors import generate_history, ASTRONAUTS
from models.health_model import assess_measurement, calculate_baselines, METRICS
from models.resource_optimizer import allocate_medical_kits

HISTORY = generate_history(hours=24)
app = Dash(__name__, title="ASTROMED | Crew Health Monitor")
app.config.suppress_callback_exceptions = True

def metric_card(label, value, unit):
    return html.Div([html.Small(label), html.H2(f"{value} {unit}")], className="metric")

def layout_overview(person):
    current = HISTORY[HISTORY.astronaut == person].iloc[-1].to_dict()
    baseline = calculate_baselines(HISTORY, person)
    assessment = assess_measurement(current, baseline)
    cards = [
        ("Heart rate", current["heart_rate"], "bpm"),
        ("Blood pressure", f'{current["systolic"]}/{current["diastolic"]}', "mmHg"),
        ("SpO₂", current["spo2"], "%"),
        ("Temperature", current["temperature"], "°C"),
        ("Glucose", current["glucose"], "mg/dL"),
        ("Sleep", current["sleep_hours"], "h"),
        ("Respiration", current["respiration"], "/min"),
        ("Radiation (demo)", current["radiation_mSv"], "mSv"),
    ]
    subset = HISTORY[HISTORY.astronaut == person].sort_values("timestamp")
    fig = go.Figure()
    for key, label in [("heart_rate","Heart rate (bpm)"),("spo2","SpO₂ (%)"),("temperature","Temperature (°C)")]:
        fig.add_trace(go.Scatter(x=subset.timestamp, y=subset[key], mode="lines", name=label))
    fig.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", height=360)
    flags = [html.Li(f'{f["level"].upper()}: {f["message"]}') for f in assessment["flags"]]
    return html.Div([
        html.Div([metric_card(*c) for c in cards], className="metrics"),
        html.Div([html.H3("24-hour health trends"), dcc.Graph(figure=fig)], className="panel"),
        html.Div([html.H3(f'Assessment: {assessment["risk_level"]}'), html.Ul(flags),
                  html.P("Prototype heuristics only — not clinically validated.")], className="panel")
    ])

app.layout = html.Div([
    html.Header([html.H1("✦ ASTROMED"), html.P("CREW HEALTH SELF-MONITORING · SIMULATED MISSION FEED")]),
    html.Div([html.Label("Crew member"), dcc.Dropdown(id="crew", options=[{"label":p,"value":p} for p in ASTRONAUTS], value=ASTRONAUTS[0], clearable=False)], className="panel"),
    dcc.Tabs(id="tabs", value="overview", children=[
        dcc.Tab(label="Mission overview", value="overview"),
        dcc.Tab(label="Crew check-in", value="checkin"),
        dcc.Tab(label="Science & sources", value="science")]),
    html.Div(id="page"),
    html.Footer("SYNTHETIC DEMO DATA · NOT A MEDICAL DEVICE · NOT FOR DIAGNOSIS OR TREATMENT")
], className="shell")

@app.callback(Output("page","children"), Input("tabs","value"), Input("crew","value"))
def render(tab, person):
    if tab == "overview":
        return layout_overview(person)
    if tab == "checkin":
        return html.Div([html.H2("Personal health check-in"),
            dcc.Input(id="hr", type="number", value=72, placeholder="Heart rate (bpm)"),
            dcc.Input(id="spo2", type="number", value=98, placeholder="SpO₂ (%)"),
            dcc.Input(id="temp", type="number", value=36.7, placeholder="Temperature °C"),
            dcc.Input(id="glucose", type="number", value=95, placeholder="Glucose mg/dL"),
            html.Button("Assess demo check-in", id="submit"),
            html.Div(id="check-result")], className="panel")
    resources = [
        ("NASA — 5 Hazards of Human Spaceflight","https://www.nasa.gov/hrp/hazards/"),
        ("NASA — Risks of Human Spaceflight","https://www.nasa.gov/hrp/risks/"),
        ("NASA — Ongoing HRP Research in Space","https://www.nasa.gov/hrp/ongoing-hrp-research/"),
        ("CSA — Monitoring Radiation for Astronaut Health","https://www.asc-csa.gc.ca/eng/news/articles/2026/2026-02-26-monitoring-radiation-astronaut-health.asp"),
        ("CSA — Why Do We Conduct Science Experiments in Space?","https://www.asc-csa.gc.ca/eng/iss/science/why-do-we-conduct-science-experiments-in-space.asp")]
    return html.Div([html.H2("Science & Sources"), html.P("These resources inform context; they are not live telemetry feeds."),
        html.Ul([html.Li(html.A(name, href=url, target="_blank")) for name,url in resources]),
        html.P("All plotted values in this prototype are synthetic demonstration data.")], className="panel")

@app.callback(Output("check-result","children"), Input("submit","n_clicks"),
              State("hr","value"), State("spo2","value"), State("temp","value"), State("glucose","value"),
              prevent_initial_call=True)
def assess_checkin(n, hr, spo2, temp, glucose):
    result = assess_measurement({"heart_rate":hr,"spo2":spo2,"temperature":temp,"glucose":glucose})
    return html.Div([html.H3(result["risk_level"]), html.P(result["summary"])])

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=8050)
