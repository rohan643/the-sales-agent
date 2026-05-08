import os, yaml, time
from enricher import enrich_lead
from outreach import send_email, send_sms
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

with open("config/icp.yaml") as f:
    ICP = yaml.safe_load(f)

with open("config/sequences.yaml") as f:
    SEQUENCES = yaml.safe_load(f)


def score_lead(lead: dict) -> dict:
    prompt = f"""
    Score this lead against the ICP below. Return JSON with keys:
    score (0-100), reason (1 sentence), angle (best outreach angle), priority (HIGH/MED/LOW).

    ICP: {ICP}
    Lead: {lead}
    """
    resp = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"}
    )
    return resp.choices[0].message.content


def run_pipeline(leads: list[dict]):
    for lead in leads:
        print(f"Processing: {lead.get('name', 'Unknown')}")
        enriched = enrich_lead(lead)
        scored = score_lead(enriched)
        sequence = "outreach" if scored["score"] >= 70 else "nurture"
        print(f"  Score: {scored['score']} → {sequence} sequence")
        time.sleep(0.5)


if __name__ == "__main__":
    import json
    with open("leads.json") as f:
        leads = json.load(f)
    run_pipeline(leads)
