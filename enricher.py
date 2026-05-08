import os, requests

CLEARBIT_KEY = os.environ.get("CLEARBIT_API_KEY", "")

def enrich_lead(lead: dict) -> dict:
    """Enrich a lead with company and person data from Clearbit."""
    email = lead.get("email", "")
    if not email or not CLEARBIT_KEY:
        return lead

    try:
        resp = requests.get(
            f"https://person.clearbit.com/v2/combined/find?email={email}",
            auth=(CLEARBIT_KEY, ""),
            timeout=10
        )
        if resp.status_code == 200:
            data = resp.json()
            lead["company_name"] = data.get("company", {}).get("name", lead.get("company_name"))
            lead["industry"] = data.get("company", {}).get("category", {}).get("industry")
            lead["employee_count"] = data.get("company", {}).get("metrics", {}).get("employees")
            lead["linkedin_url"] = data.get("person", {}).get("linkedin", {}).get("handle")
    except Exception as e:
        print(f"  Enrichment failed for {email}: {e}")

    return lead
