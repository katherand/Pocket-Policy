# Pocket Policy - Dev Log #001
**Date:** 2026-07-25  
**Focus:** Offline-first healthcare navigation engine & MPPM policy indexing  

---

### 💡 Field Context & Problem Solved
Healthcare navigators including family members and social workers sift through hundreds of pages of complex state regulations, income deduction rules, and asset limits while helping a client apply for benefits. 

Pocket Policy eliminates that friction by acting as a fast, zero-overhead offline lookup tool:
1. **No tracking / no accounts:** Designed for client privacy and fast searching in the field or anywhere.
2. **Immediate access:** Pinpoints official state Medicaid Policy and Procedures Manual (MPPM) rules—like allowable income deductions, essential expense exclusions, the application process itself, and county eligibility processing office locations—in seconds.
3. **Context & Audit Trail:** Features context expansion (previous/next paragraph loading) and direct links to full source documents to verify current policy during client reviews by utilizing the copy button to paste into the find feature of the source document to locate the exact policy.
4. **State-agnostic design:** A navigator in any state can update or swap the policy JSON schema to make the tool immediately accurate for their state's policy manual.

---

### 🛠️ What Was Built / Updated
* **Decoupled Engine from Policy Data:** Separated the core lookup interface (UI) from state-specific healthcare policy rules. The interface now ingests JSON policy schemas not fragile easily broken hardcoded logic.
* **Offline-First Indexing:** Implemented local-first data persistence so that community health workers (CHWs) can execute instant lookups without going through a cellular or internet connection.
* **Automated MPPM Policy Extraction:** Built a Python pipeline (`scrapyr.py`) that fetches, filters, and parses Medicaid Policy and Procedures Manual (`.docx` & HTML) files directly from state portals (e.g., SCDHHS) into `policies.json`.
* **Resilient Hybrid Location Ingestion:** Combined automated web parsing with LLM-assisted text normalization to clean up inconsistent state directory formatting (e.g., missing bullet markers on the SCDHHS *Where to Go For Help* page) into structured local eligibility records in `data.js`.

---

### 🎯 Next Up & Lessons Learned
* **DOM Instability in State Portals:** Inconsistent DOM formatting on state site directories reinforces why the client-side app should rely on clean static fallbacks (`data.js`) rather than live web fetching—though this may not be true for all state data.
* **Managing Monthly Policy Drift:** Aligning automated re-scraping routines (`scrapyr.py`) around regular state release cycles (such as monthly updates on the 1st) to ensure offline indexes remain current via a GitHub Actions cron workflow (`.github/workflows/monthly-scraper.yml`).
* **Publishing `policy-template.json` as a Fallback Method:** Created a clean, annotated template in the root repository so contributors in other states can easily plug in their own local office listings and state policy manuals.

To adapt Pocket Policy for another state:
* **Option A (Automated):** Run `scrapyr.py` with your state's Medicaid policy manual URL to auto-generate `policies.json`.
* **Option B (Manual / Fallback):** If your state's site breaks scrapers, populate `policy-template.json` manually (or via LLM extraction) and rename it to `policies.json`.
* **Multi-State Portal & Domain Roadmap:** Structuring the repository (`data/{state}-policies.json`) so contributors in other states can Fork and PR their state's dataset. This will power a simple state selection dropdown on `forgecommonsproject.org`, allowing the public, family members, and navigators to access offline policy lookups nationwide from a single, quiet web portal.