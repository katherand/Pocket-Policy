import json
import re
import io
import requests
from bs4 import BeautifulSoup
import urllib3
from urllib.parse import urljoin
from docx import Document

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

INDEX_URL = "https://www1.scdhhs.gov/mppm/"
COUNTY_DIRECTORY_URL = "https://www.scdhhs.gov/members/where-go-help"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}

def clean_text(raw_string):
    if not raw_string:
        return ""
    clean = raw_string.replace("\n", " ").replace("\r", " ").replace("\t", " ")
    clean = re.sub(r'\s+', ' ', clean)
    return clean.strip()

def extract_text_from_docx(file_bytes):
    paragraphs = []
    try:
        doc_file = io.BytesIO(file_bytes)
        doc = Document(doc_file)
        for p in doc.paragraphs:
            text = clean_text(p.text)
            if len(text) > 30:
                paragraphs.append(text)
    except Exception as e:
        print(f"⚠️ Could not parse Word text blocks: {e}")
    return paragraphs

def harvest_live_counties():
    """Intelligently sweeps multi-line landmark layout groups block-by-block."""
    print("📍 Dynamically harvesting structural multi-line County Office Matrix...")
    county_records = []
    
    try:
        res = requests.get(COUNTY_DIRECTORY_URL, headers=headers, verify=False, timeout=15)
        soup = BeautifulSoup(res.text, "html.parser")
        
        # We sweep through all layout container blocks sequentially
        all_elements = soup.find_all(['p', 'div', 'td', 'h3', 'h4', 'strong'])
        
        current_county = None
        address_accumulator = []
        
        for el in all_elements:
            text = clean_text(el.text)
            if not text:
                continue
                
            # Step A: Catch the Bold Heading/Standalone line naming the county
            # e.g., "Abbeville County" or "Aiken County"
            if re.search(r'^[A-Za-z\s]+\s+County$', text, re.IGNORECASE):
                # If we were tracking a previous county, save its built address first
                if current_county and address_accumulator:
                    full_addr = ", ".join(address_accumulator).replace(" (Map)", "").replace("(Map)", "").strip()
                    county_records.append({
                        "id": f"county_{current_county.lower().replace(' ', '_')}",
                        "source": "COUNTY DIRECTORY",
                        "county": current_county,
                        "address": re.sub(r'\s+', ' ', full_addr)
                    })
                
                # Start fresh tracking the new county name
                current_county = text.replace("County", "").strip()
                address_accumulator = []
                continue
            
            # Step B: If we are actively tracking a county, grab the building names & streets
            if current_county:
                # Add the string fragment to our address pool for this county
                address_accumulator.append(text)
                
                # Step C: The "(Map)" text marks the absolute end of this county's visual container
                if "(map)" in text.lower():
                    full_addr = ", ".join(address_accumulator).replace(" (Map)", "").replace("(Map)", "").strip()
                    c_id = f"county_{current_county.lower().replace(' ', '_')}"
                    
                    if not any(c['id'] == c_id for c in county_records):
                        county_records.append({
                            "id": c_id,
                            "source": "COUNTY DIRECTORY",
                            "county": current_county,
                            "address": re.sub(r'\s+', ' ', full_addr)
                        })
                    
                    # Reset tracker fields so we don't accidentally leak text into the next county
                    current_county = None
                    address_accumulator = []
                    
    except Exception as e:
        print(f"⚠️ Dynamic multi-line structural parser error: {e}")
        
    print(f"✅ Extracted {len(county_records)} live county office complexes directly from layout stream.")
    return county_records

def harvest_deep_policy():
    print("📡 Pocket Policy Automation Engine connecting to manual database...")
    policy_records = harvest_live_counties()
    global_counter = len(policy_records)

    try:
        response = requests.get(INDEX_URL, headers=headers, verify=False, timeout=15)
        soup = BeautifulSoup(response.text, "html.parser")
    except Exception as e:
        print(f"❌ Initial Connection failed: {e}")
        return

    all_links = soup.find_all("a")
    print(f"Found {len(all_links)} directory links. Filtering public text maps...")

    for link in all_links:
        href = link.get("href")
        title = clean_text(link.text)
        
        if not href:
            continue
            
        internal_keywords = ['curam', 'cgis', 'login', 'portal', 'internal', 'procedural', 'eems', 'miap', 'notice']
        if any(keyword in title.lower() or keyword in href.lower() for keyword in internal_keywords):
            continue

        absolute_url = urljoin(INDEX_URL, href)
        source_name = "GENERAL POLICY"
        chapter_match = re.search(r'(chapter|section|mppm)\s*\d+', title.lower())
        if chapter_match:
            source_name = chapter_match.group(0).upper()

        if any(ext in href.lower() for ext in ['.html', '.htm']):
            try:
                page_res = requests.get(absolute_url, headers=headers, verify=False, timeout=10)
                page_soup = BeautifulSoup(page_res.text, "html.parser")
                text_blocks = page_soup.find_all(['p', 'li', 'td'])
                
                for block in text_blocks:
                    block_text = clean_text(block.text)
                    if len(block_text) < 30:
                        continue
                    policy_records.append({
                        "id": f"rule_{global_counter}",
                        "source": source_name,
                        "text": block_text,
                        "url": absolute_url
                    })
                    global_counter += 1
            except Exception:
                pass

        elif ".docx" in href.lower():
            try:
                file_res = requests.get(absolute_url, headers=headers, verify=False, timeout=15)
                docx_paragraphs = extract_text_from_docx(file_res.content)
                
                for paragraph in docx_paragraphs:
                    policy_records.append({
                        "id": f"rule_{global_counter}",
                        "source": source_name,
                        "text": paragraph,
                        "url": absolute_url
                    })
                    global_counter += 1
            except Exception:
                pass

        elif ".pdf" in href.lower():
            policy_records.append({
                "id": f"rule_{global_counter}",
                "source": source_name,
                "text": f"{title} (Official PDF Resource Reference)",
                "url": absolute_url
            })
            global_counter += 1

    with open("policies.json", "w", encoding="utf-8") as f:
        json.dump(policy_records, f, indent=4)
        
    print(f"\n📦 AUTOMATION COMPLETE! 'policies.json' seeded with {global_counter} dynamic mapping items.")

if __name__ == "__main__":
    harvest_deep_policy()