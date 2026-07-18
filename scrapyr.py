import json
import re
import io
import requests
from bs4 import BeautifulSoup
import urllib3
from urllib.parse import urljoin
from docx import Document  # <-- New tool to read deep Word contents

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

INDEX_URL = "https://www1.scdhhs.gov/mppm/"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}

def clean_text(raw_string):
    if not raw_string:
        return ""
    clean = raw_string.replace("\n", " ").replace("\r", " ").replace("\t", " ")
    clean = re.sub(r'\s+', ' ', clean)
    return clean.strip()

def extract_text_from_docx(file_bytes):
    """Reads deep paragraph lines directly out of a binary Word document."""
    paragraphs = []
    try:
        doc_file = io.BytesIO(file_bytes)
        doc = Document(doc_file)
        for p in doc.paragraphs:
            text = clean_text(p.text)
            if len(text) > 30:  # Save valid narrative rules blocks
                paragraphs.append(text)
    except Exception as e:
        print(f"⚠️ Could not parse Word text blocks: {e}")
    return paragraphs

def harvest_deep_policy():
    print("📡 Pocket Policy Automation Engine connecting to database...")
    try:
        response = requests.get(INDEX_URL, headers=headers, verify=False, timeout=15)
        soup = BeautifulSoup(response.text, "html.parser")
    except Exception as e:
        print(f"❌ Initial Connection failed: {e}")
        return

    policy_records = []
    global_counter = 0

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
        
        # Deduce a clean source chapter badge
        source_name = "GENERAL POLICY"
        chapter_match = re.search(r'(chapter|section|mppm)\s*\d+', title.lower())
        if chapter_match:
            source_name = chapter_match.group(0).upper()
        elif "301" in href or "301" in title:
            source_name = "SECTION_301"
        elif "703" in href or "703" in title:
            source_name = "CHAPTER_703"

        # CASE 1: The document is a live web-view format
        if any(ext in href.lower() for ext in ['.html', '.htm']):
            print(f"📖 Deep-harvesting HTML view: {title[:40]}...")
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
            except Exception as read_err:
                pass

        # CASE 2: The document is an official Word file (.docx)
        elif ".docx" in href.lower():
            print(f"📥 Downloading and extracting text from packet: {title[:40]}...")
            try:
                file_res = requests.get(absolute_url, headers=headers, verify=False, timeout=15)
                # Parse internal lines without saving a messy folder structure on your desktop
                docx_paragraphs = extract_text_from_docx(file_res.content)
                
                for paragraph in docx_paragraphs:
                    policy_records.append({
                        "id": f"rule_{global_counter}",
                        "source": source_name,
                        "text": paragraph,
                        "url": absolute_url
                    })
                    global_counter += 1
            except Exception as download_err:
                print(f"⚠️ Failed to stream raw packet text: {download_err}")

        # CASE 3: Standard PDF document link fallback
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
        
    print(f"\n📦 AUTOMATION COMPLETE! 'policies.json' seeded with {global_counter} deep text items.")

if __name__ == "__main__":
    harvest_deep_policy()