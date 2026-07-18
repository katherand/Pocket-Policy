# Pocket Policy
**Democratizing access to state policy, one search at a time.**

## The Vision
Policy documents are often hidden behind complex, inaccessible portals, PDFs, and broken links. **Pocket Policy** transforms these static barriers into a lightweight, searchable, and offline-capable interface. 

The goal is to move from "document-first" (where you have to hunt for a packet) to "information-first" (where the rule finds you).

## How It Works
Pocket Policy is built on a two-part automated pipeline:
1. **The Scraper (`scrapyr.py`):** An automated harvest engine that deep-crawls official portals. It extracts raw policy text, strips out administrative noise, and maps deep paragraph-level data into a structured `policies.json`.
2. **The Generator (`creator.py`):** An automated build engine that consumes the JSON data and bakes it into a single, high-performance web application (`index.html` + `data.js`).

## The "State Quirk" Factor
Every state department (SCDHHS, DHEC, DSS, etc.) hosts their policy data differently. Some use HTML, others rely solely on Word docs or PDFs. 
* **Modularity:** This repository is built to be modular. If you are adapting this for a different state, you only need to tweak the `scrapyr.py` harvester to point to the new index URL and adjust the file parsers.
* **Collaboration:** We welcome forks and pull requests that add support for new states, better parsing logic for complex PDFs, or UI/UX improvements.

## Why it Matters
Access to official rules shouldn't require a master's degree in navigation. Whether it's a citizen verifying eligibility or a caseworker finding a specific regulation, this tool provides instant, reliable access to the text that matters most.

---

## 📱 Device-Specific Navigation Guides
Because Pocket Policy handles the hard work of matching text locally, it copies the exact sentence to your clipboard the moment you tap a card. Once the official document opens, use these steps to paste and find it:

### 🍏 iOS / iPhone Safari
1. Tap the card to copy the text and open the document.
2. In the bottom address bar, tap the **Puzzle Piece** icon.
3. Tap the **Find on Page** icon (a document with a magnifying glass) and paste your text.

### 🤖 Android Chrome
1. Tap the card to copy the text and open the document.
2. Tap the **Three Dots (...)** menu in the top right corner.
3. Select **Find in page** and paste your text.

### 🖥️ Desktop / Laptop / Tablet (Mac, Windows, Linux)
1. Click the card to copy the text and open the document.
2. Press **`Cmd + F`** (Mac) or **`Ctrl + F`** (Windows/Linux).
3. Paste the text into the search bar that pops up.