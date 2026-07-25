#this file has not worked for South Carolina but other states may find it works well for their data
import json
import re
import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
COUNTY_DIRECTORY_URL = "https://www.scdhhs.gov/members/where-go-help"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}

def clean_text(raw_string):
    if not raw_string:
        return ""
    # Strip out quote marks and artifacts the state inserted into the text stream
    clean = raw_string.replace('"', '').replace("'", "").replace("\n", " ")
    return re.sub(r'\s+', ' ', clean).strip()

def scrape_perfect_counties():
    print("📍 Scraping live locations using the inspector layout map...")
    county_records = []
    
    try:
        res = requests.get(COUNTY_DIRECTORY_URL, headers=headers, verify=False, timeout=15)
        # Standardize non-standard brackets (like ‹ or ≤) before passing to the parser
        sanitized_html = res.text.replace('‹', '<').replace('≤', '>')
        soup = BeautifulSoup(sanitized_html, "html.parser")
        
        # Every single county container is enclosed inside a paragraph tag block
        paragraphs = soup.find_all('p')
        
        for p in paragraphs:
            # Check if this paragraph contains the bold County indicator tag
            strong_tag = p.find('strong')
            if strong_tag and "county" in strong_tag.text.lower():
                county_name = strong_tag.text.replace("County", "").strip()
                
                # Extract all text blocks inside this paragraph, ignoring the 'Map' link text
                text_fragments = []
                for child in p.children:
                    if child.name == 'a': 
                        continue # Skip the actual Map link text anchor
                    if child.text:
                        cleaned = clean_text(child.text)
                        if cleaned and cleaned != county_name:
                            text_fragments.append(cleaned)
                
                # Combine the building name and streets with clean commas
                full_address = ", ".join(text_fragments).strip(", ")
                
                # Fix typos like "Sa Luda, SC" or accidental spaces
                full_address = full_address.replace("Sa Luda", "Saluda")
                
                if len(county_name) < 25 and len(full_address) > 5:
                    county_records.append({
                        "id": f"county_{county_name.lower().replace(' ', '_')}",
                        "source": "COUNTY DIRECTORY",
                        "county": county_name,
                        "address": full_address
                    })
                    
    except Exception as e:
        print(f"❌ Scraper loop failed: {e}")
        
    print(f"✅ Live matrix parsed. Found {len(county_records)} operational offices.")
    return county_records

if __name__ == "__main__":
    data = scrape_perfect_counties()
    print(json.dumps(data[:3], indent=4))