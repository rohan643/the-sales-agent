<div align="center">

# 🤖 The Sales Agent

**Automated CRM & multi-channel outreach — captures leads, nurtures them, closes the loop. Zero manual follow-up.**

[![n8n](https://img.shields.io/badge/n8n-Core-EA4B71?style=for-the-badge&logo=n8n&logoColor=white)](https://n8n.io)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com)
[![Airtable](https://img.shields.io/badge/Airtable-CRM-18BFFF?style=for-the-badge&logo=airtable&logoColor=white)](https://airtable.com)
[![Twilio](https://img.shields.io/badge/Twilio-SMS-F22F46?style=for-the-badge&logo=twilio&logoColor=white)](https://twilio.com)

</div>

---

## The Problem

Most businesses lose leads not because they're bad leads — but because nobody followed up fast enough, or the 4th touchpoint never happened because a human forgot. Opportunities slip through the cracks constantly.

The Sales Agent fixes that. Every lead is captured, centralized, and followed up with automatically — via whichever channel they're most likely to respond on.

---

## What It Does

```
New Lead Enters (form, ad, referral, DM, cold outreach reply)
         │
         ▼
┌─────────────────────────────┐
│  Lead Capture & Enrichment  │  ← Pulls company info, LinkedIn data,
│                             │    enriches contact record automatically
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│  Centralized CRM Entry      │  ← One place for every prospect,
│  (Airtable)                 │    no matter where they came from
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│  AI Qualification Score     │  ← GPT-4o scores the lead 0–100
│                             │    and assigns the right follow-up sequence
└──────────────┬──────────────┘
               │
        ┌──────┴──────┐
        │             │
        ▼             ▼
  High Score       Low Score
  (≥ 70)           (< 70)
   Outreach         Nurture
   Sequence         Sequence
        │             │
        └──────┬──────┘
               ▼
┌─────────────────────────────┐
│  Personalized Outreach      │  ← Email, SMS, or LinkedIn DM
│  (AI-written per lead)      │    based on lead's preferred channel
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│  Reply Handling             │  ← Classifies reply intent,
│                             │    books meeting or re-routes
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│  CRM Auto-Update            │  ← Stage, notes, next action —
│                             │    all updated with zero manual input
└─────────────────────────────┘
```

---

## Outreach Channels

| Channel | Use Case | Tooling |
|---|---|---|
| **Email** | Primary outreach, follow-up sequences | Gmail / SMTP |
| **SMS** | High-urgency follow-up, re-engagement | Twilio |
| **LinkedIn DM** | B2B prospects with LinkedIn presence | Phantombuster |
| **Instagram DM** | Consumer-facing or creator outreach | ManyChat |

The system automatically selects the best channel based on the lead source and profile data.

---

## Outreach Sequence Structure

```
Day 0:   First touch — personalized intro (AI-written based on lead data)
Day 2:   Follow-up — adds value (relevant case study or insight)
Day 5:   Third touch — different angle, lighter ask
Day 10:  Last touch — "closing the loop" message
Day 21:  Re-engagement — if no reply, new angle + fresh opener
Day 60:  Long-term nurture — monthly value email until they reply or unsubscribe
```

Every message is unique. GPT-4o generates each one from the lead's data, so nothing sounds templated.

---

## AI Personalization Sample

```
Input:   Lead is a roofing contractor, found via Instagram ad, 
         no follow-up system currently, based in Houston TX

Output (Email):
─────────────────────────────────────────────────────────
Subject: following up on the ad

Hey Mike,

Most contractors I talk to in Houston are amazing at the work — 
it's the follow-up where jobs get lost. Someone fills out a form 
on Monday and by Thursday they've already hired someone else.

Put together a quick 3-minute walkthrough of what I built for 
a similar contractor last quarter — went from losing ~40% of 
inbound leads to closing almost all of them in the first week.

Worth a look?

Rohan
─────────────────────────────────────────────────────────
```

---

## CRM Schema (Airtable)

```
Contacts table:
├── Name, Email, Phone
├── Company, Industry, Location
├── Lead Source (ad, referral, DM, etc.)
├── Channel (email, SMS, LinkedIn)
├── ICP Score (0–100, AI-generated)
├── Stage (New → Contacted → Replied → Meeting → Closed)
├── Follow-up Sequence (which sequence they're in)
├── Last Contacted (auto-updated)
├── Next Action (auto-set based on stage)
├── Notes (auto-populated from call transcripts)
└── Owner (assigned rep or "Automated")
```

---

## Setup

### Required Accounts
- n8n (self-hosted or cloud)
- Airtable
- OpenAI API
- Twilio (for SMS)
- Gmail or SMTP provider
- Phantombuster (optional, for LinkedIn)

### Environment Variables
```env
OPENAI_API_KEY=sk-...
AIRTABLE_API_KEY=...
AIRTABLE_BASE_ID=...
TWILIO_ACCOUNT_SID=...
TWILIO_AUTH_TOKEN=...
TWILIO_FROM_NUMBER=+1...
GMAIL_CLIENT_ID=...
GMAIL_CLIENT_SECRET=...
```

### Import & Configure
1. Import `the-sales-agent.json` into n8n
2. Add all credentials
3. Set your ICP scoring prompt in `config/icp-prompt.txt`
4. Set your outreach sequences in `config/sequences.yaml`
5. Activate — every new Airtable record triggers the pipeline

---

## Results

```
Before: Leads captured manually, follow-up inconsistent, opportunities lost
After:  Every lead captured, followed up 6x across 60 days, zero slipping through

Engagement lift:   +280% more touchpoints per lead
Time saved:        ~8 hours/week of manual follow-up eliminated
Reply rate:        Varies by industry (avg 22–34% across clients)
```

---

<div align="center">

**Built by [Rohan Mukherjee](https://github.com/rohan643)**

</div>
