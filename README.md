```
 _____ _            ____        _             _                    _
|_   _| |__   ___  / ___|  __ _| | ___  ___  / \   __ _  ___ _ __ | |_
  | | | '_ \ / _ \ \___ \ / _` | |/ _ \/ __| / _ \ / _` |/ _ \ '_ \| __|
  | | | | | |  __/  ___) | (_| | |  __/\__ \/ ___ \ (_| |  __/ | | | |_
  |_| |_| |_|\___| |____/ \__,_|_|\___||___/_/   \_\__, |\___|_| |_|\__|
                                                    |___/
```

> Automated CRM & multi-channel outreach — every lead captured, nurtured, and followed up. Zero manual work.

---

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white)
![n8n](https://img.shields.io/badge/n8n-workflow-EA4B71?style=flat-square&logo=n8n)
![Airtable](https://img.shields.io/badge/Airtable-CRM-18BFFF?style=flat-square&logo=airtable)
![Twilio](https://img.shields.io/badge/Twilio-SMS-F22F46?style=flat-square&logo=twilio)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT4o-412991?style=flat-square&logo=openai)

---

## The Problem

Businesses lose leads not because they're bad leads — but because nobody followed up in time. Someone fills out a form Monday. By Thursday they've signed with a competitor.

This system fixes that permanently.

---

## How It Works

```
Lead enters (form / ad / DM / referral)
    │
    ▼
Enrichment  ──►  Airtable CRM
    │
    ▼
GPT-4o scores ICP fit (0–100)
    │
    ├── Score ≥ 70  →  Outreach Sequence (email / SMS / LinkedIn)
    └── Score < 70  →  Nurture Sequence (long-term drip)
                │
                ▼
         Reply classified by AI
                │
    ├── Interested   →  Book via Cal.com
    ├── Not now      →  Snooze 45 days
    └── Unsubscribe  →  DNC list
```

---

## File Structure

```
the-sales-agent/
├── main.py                   # Orchestrator
├── enricher.py               # Lead enrichment (Clearbit + LinkedIn)
├── outreach.py               # Email / SMS dispatcher
├── workflow/
│   └── sales-agent.json      # n8n workflow export
├── config/
│   ├── icp.yaml              # ICP definition
│   └── sequences.yaml        # Outreach sequence timing
└── requirements.txt
```

---

## Outreach Sequence

| Touch | Day | Channel | Message Type |
|-------|-----|---------|-------------|
| 1 | 0 | Email | AI-personalized intro |
| 2 | 2 | Email | Value + case study |
| 3 | 5 | Email | Different angle |
| 4 | 10 | SMS | Short re-ping |
| 5 | 21 | Email | Long-term re-engage |

---

## Setup

```bash
git clone https://github.com/rohan643/the-sales-agent
cd the-sales-agent
pip install -r requirements.txt
cp config/icp.yaml.example config/icp.yaml
# Fill in API keys in .env
python main.py
```

Required: `OPENAI_API_KEY`, `AIRTABLE_API_KEY`, `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`

---

*Built by [@rohan643](https://github.com/rohan643)*
