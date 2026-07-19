import json
import os

def generate_portal():
    print("🛠️ Pocket Policy Creator building accessible high-contrast layout & local directory...")
    
    if not os.path.exists("policies.json"):
        print("❌ Error: 'policies.json' missing! Run your scraper first.")
        return

    with open("policies.json", "r", encoding="utf-8") as f:
        records = json.load(f)

    # Filter out any messy text structures pulled by older scraper logic
    policy_data = [r for r in records if r.get("source") != "COUNTY DIRECTORY"]

    # 46 PHYSICAL COUNTY MATRIX WITH TRUE LANDMARKS & ACCURATE GEOGRAPHICAL STREETS
    county_directory = [
        {"id": "county_abbeville", "county": "Abbeville", "address": "Human Services Building, 909 W. Greenwood St, Ste 1, Abbeville, SC 29620"},
        {"id": "county_aiken", "county": "Aiken", "address": "County Commissioner's Building, 1410 Park Ave, SE, Aiken, SC 29801"},
        {"id": "county_allendale", "county": "Allendale", "address": "521 Barnwell Rd, Allendale, SC 29810"},
        {"id": "county_anderson", "county": "Anderson", "address": "224 McGee Rd, Anderson, SC 29625"},
        {"id": "county_bamberg", "county": "Bamberg", "address": "374 Log Branch Rd, Bamberg, SC 29003"},
        {"id": "county_barnwell", "county": "Barnwell", "address": "10913 Ellenton St, Barnwell, SC 29812"},
        {"id": "county_beaufort", "county": "Beaufort", "address": "1905 Duke St, Beaufort, SC 29902"},
        {"id": "county_berkeley", "county": "Berkeley", "address": "2 Belt Dr, Moncks Corner, SC 29461"},
        {"id": "county_calhoun", "county": "Calhoun", "address": "2831 Old Belleville Rd, St. Matthews, SC 29135"},
        {"id": "county_charleston", "county": "Charleston", "address": "4130 Faber Place Dr, Suite 300, North Charleston, SC 29405"},
        {"id": "county_cherokee", "county": "Cherokee", "address": "1231 N Limestone St, Unit C, Gaffney, SC 29340"},
        {"id": "county_chester", "county": "Chester", "address": "115 Reedy St, Chester, SC 29706"},
        {"id": "county_chesterfield", "county": "Chesterfield", "address": "203 Perry Wiley Way, Chesterfield, SC 29709"},
        {"id": "county_clarendon", "county": "Clarendon", "address": "236 Commerce St, Manning, SC 29102"},
        {"id": "county_colleton", "county": "Colleton", "address": "215 South Lemacks St, Walterboro, SC 29488"},
        {"id": "county_darlington", "county": "Darlington", "address": "300 Russell St, Room 145, Darlington, SC 29532"},
        {"id": "county_dillon", "county": "Dillon", "address": "1213 Highway 34 West, Dillon, SC 29536"},
        {"id": "county_dorchester", "county": "Dorchester", "address": "1452 Boone Hill Rd, Ste C, Summerville, SC 29483"},
        {"id": "county_edgefield", "county": "Edgefield", "address": "120 W.A. Reel Dr, Edgefield, SC 29824"},
        {"id": "county_fairfield", "county": "Fairfield", "address": "1136 Kincaid Bridge Rd, Winnsboro, SC 29180"},
        {"id": "county_florence", "county": "Florence", "address": "2685 South Irby St, Box I, Florence, SC 29505"},
        {"id": "county_georgetown", "county": "Georgetown", "address": "330 Dozier St, Georgetown, SC 29440"},
        {"id": "county_greenville", "county": "Greenville", "address": "352 Halton Rd, Suite 200, Greenville, SC 29607"},
        {"id": "county_greenwood", "county": "Greenwood", "address": "1118 Phoenix St, Greenwood, SC 29646"},
        {"id": "county_hampton", "county": "Hampton", "address": "102 Ginn Altman Ave, Suite B, Hampton, SC 29924"},
        {"id": "county_horry", "county": "Horry", "address": "Genesis Complex, 1201 Creel St, Conway, SC 29527"},
        {"id": "county_jasper", "county": "Jasper", "address": "10908 North Jacob Smart Blvd, Ridgeland, SC 29936"},
        {"id": "county_kershaw", "county": "Kershaw", "address": "110 East DeKalb St, Camden, SC 29020"},
        {"id": "county_lancaster", "county": "Lancaster", "address": "1599 Pageland Hwy, Lancaster, SC 29720"},
        {"id": "county_laurens", "county": "Laurens", "address": "93 Human Services Rd, Clinton, SC 29325"},
        {"id": "county_lee", "county": "Lee", "address": "820 Brown St, Bishopville, SC 29010"},
        {"id": "county_lexington", "county": "Lexington", "address": "605 West Main St, Lexington, SC 29072"},
        {"id": "county_marion", "county": "Marion", "address": "137 Airport Ct, Suite J, Mullins, SC 29574"},
        {"id": "county_marlboro", "county": "Marlboro", "address": "1 Ag St, Bennettsville, SC 29512"},
        {"id": "county_mccormick", "county": "McCormick", "address": "215 North Mine St - Hwy 28 N, McCormick, SC 29835"},
        {"id": "county_newberry", "county": "Newberry", "address": "County Human Services Center, 2107 Wilson Rd, Newberry, SC 29108"},
        {"id": "county_oconee", "county": "Oconee", "address": "223 B Kenneth St, Walhalla, SC 29691"},
        {"id": "county_orangeburg", "county": "Orangeburg", "address": "114 Howard Hill Dr, Orangeburg, SC 29115"},
        {"id": "county_pickens", "county": "Pickens", "address": "212 McDaniel Ave, Pickens, SC 29671"},
        {"id": "county_richland", "county": "Richland", "address": "7499 Parklane Rd, Suite 124, Columbia, SC 29223"},
        {"id": "county_saluda", "county": "Saluda", "address": "613 Newberry Hwy, Saluda, SC 29138"},
        {"id": "county_spartanburg", "county": "Spartanburg", "address": "1000 N. Pine St, Suite 23, Spartanburg, SC 29303"},
        {"id": "county_sumter", "county": "Sumter", "address": "30 Wesmark Ct, Sumter, SC 29150"},
        {"id": "county_union", "county": "Union", "address": "200 South Mountain St, Union, SC 29379"},
        {"id": "county_williamsburg", "county": "Williamsburg", "address": "121 Hampton Ave, Kingstree, SC 29556"},
        {"id": "county_york", "county": "York", "address": "454 S. Anderson Rd, Suite 11, Rock Hill, SC 29730"}
    ]

    # Package cleanly to override data.js completely
    database_payload = {
        "policies": policy_data,
        "counties": county_directory
    }
    
    data_js_content = "const appPayload = " + json.dumps(database_payload, indent=4) + ";"
    with open("data.js", "w", encoding="utf-8") as f:
        f.write(data_js_content)
    print("📦 Synchronized clean 46-county structural layout data payload.")

    html_content = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pocket Policy</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif; margin: 20px; background-color: #F7FAFC; color: #2D3748; padding-bottom: 80px; }
        .container { max-width: 900px; margin: 0 auto; }
        h1 { color: #1C3D5A; border-bottom: 3px solid #1C3D5A; padding-bottom: 10px; margin-bottom: 5px; font-size: 28px; font-weight: bold; }
        .meta-info { font-size: 13px; color: #718096; margin-bottom: 15px; font-weight: 500; }
        
        .search-box { width: 100%; padding: 12px; font-size: 16px; border: 2px solid #CBD5E0; border-radius: 6px; box-sizing: border-box; margin-bottom: 20px; background: white; }
        .search-box:focus { outline: none; border-color: #1C3D5A; box-shadow: 0 0 8px rgba(28,61,90,0.2); }

        .portal-actions { display: flex; gap: 10px; margin-bottom: 15px; flex-wrap: wrap; }
        .action-link { flex: 1; min-width: 140px; background: #EBF8FF; color: #2B6CB0; text-align: center; padding: 10px; border-radius: 6px; font-weight: bold; text-decoration: none; font-size: 13px; border: 1px solid #BEE3F8; }
        .action-link:active { background: #BEE3F8; }

        .county-widget { background: #EDF2F7; padding: 15px; border-radius: 6px; margin-bottom: 15px; border: 1px solid #E2E8F0; }
        .widget-title { font-size: 13px; font-weight: bold; color: #4A5568; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px; }
        .select-box { width: 100%; padding: 10px; font-size: 15px; border-radius: 4px; border: 1px solid #CBD5E0; background: white; font-weight: 500; }
        .office-display { display: none; background: white; margin-top: 10px; padding: 15px; border-radius: 4px; border-left: 4px solid #3182CE; box-shadow: 0 1px 2px rgba(0,0,0,0.05); }
        .office-row { font-size: 15px; line-height: 1.5; margin-bottom: 8px; color: #2D3748; }
        
        .card { background: white; margin-bottom: 12px; border-radius: 6px; border-left: 5px solid #1C3D5A; box-shadow: 0 1px 3px rgba(0,0,0,0.05); display: flex; flex-direction: column; }
        .card-header { padding: 15px; cursor: pointer; display: flex; flex-direction: column; align-items: flex-start; }
        .card:active .card-header { background: #F7FAFC; }
        
        .source-tag { font-weight: bold; color: #1C3D5A; font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; background: #EBF8FF; padding: 4px 8px; border-radius: 4px; display: inline-block; margin-bottom: 8px; }
        .rule-text { font-size: 15px; line-height: 1.5; color: #2D3748; width: 100%; }
        
        .nested-breakdown { display: none; background: #F8FAFC; border-top: 1px solid #E2E8F0; padding: 15px; font-size: 14px; color: #2D3748; border-bottom-left-radius: 6px; border-bottom-right-radius: 6px; }
        .context-stream { display: flex; flex-direction: column; gap: 8px; margin: 10px 0; }
        .context-block { padding-left: 10px; border-left: 3px solid #CBD5E0; font-style: italic; color: #2D3748; opacity: 1; line-height: 1.5; }
        .context-block.current { font-style: normal; font-weight: 500; border-left-color: #3182CE; background: #FFF3C4; padding: 6px 10px; border-radius: 4px; }
        
        .expansion-trigger { text-align: center; margin: 5px 0; font-size: 12px; font-weight: bold; color: #1C3D5A; cursor: pointer; padding: 6px; background: #E2E8F0; border-radius: 4px; }
        .action-bar { margin-top: 15px; padding-top: 10px; border-top: 1px dashed #CBD5E0; display: flex; gap: 10px; flex-wrap: wrap; }
        .btn { background: #1C3D5A; color: white; border: none; padding: 6px 12px; font-size: 12px; font-weight: bold; border-radius: 4px; cursor: pointer; text-decoration: none; }
        .btn-secondary { background: #E2E8F0; color: #2D3748; font-weight: bold; }
        
        .card.visited { border-left-color: #A0AEC0; opacity: 0.8; }
        .highlight { background-color: #FFF3C4; font-weight: bold; color: #000000; }
        .no-results { text-align: center; color: #718096; margin-top: 40px; font-size: 15px; }
        .footer-banner { background: white; border-top: 1px solid #E2E8F0; padding: 12px; position: fixed; bottom: 0; left: 0; right: 0; text-align: center; font-size: 12px; color: #2D3748; box-shadow: 0 -4px 12px rgba(0,0,0,0.03); z-index: 1000; }
        .footer-banner a { color: #1C3D5A; text-decoration: none; font-weight: bold; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔍 Pocket Policy</h1>
        <p class="meta-info">Data-Saving Portal | Direct localized resources completely offline.</p>
        
        <!-- Search Bar Primary Placement -->
        <input type="text" id="search-input" class="search-box" placeholder="Search policy manual (e.g., vehicles, asset limits)..." oninput="performSearch()">
        
        <div id="results-container"></div>

        <hr style="border: 0; border-top: 2px dashed #E2E8F0; margin: 25px 0;">

        <!-- Portals Grid -->
        <div class="portal-actions">
            <a class="action-link" href="https://apply.scdhhs.gov" target="_blank">🌐 Apply or Renew Online</a>
            <a class="action-link" href="https://tools.apply.scdhhs.gov" target="_blank">📤 Upload Review Papers</a>
            <a class="action-link" href="https://www.ssa.gov/myaccount/" target="_blank" style="background: #F0FFF4; color: #22543D; border-color: #C6F6D5;">📄 Get SSA Award Letter</a>
            <a class="action-link" href="https://www.ssa.gov/benefits/ssi/" target="_blank" style="background: #F0FFF4; color: #22543D; border-color: #C6F6D5;">✍️ Apply for SSI Benefits</a>
        </div>

        <!-- SC Disability Process Explainer Card -->
        <div style="background: #FFF5F5; padding: 15px; border-radius: 6px; margin-bottom: 15px; border: 1px solid #FED7D7; font-size: 14px; line-height: 1.5; color: #2D3748;">
            💡 <strong>Important for SC Disability Medicaid:</strong> 
            <p style="margin: 5px 0 0 0;">
                If you receive <strong>SSI</strong>, you automatically get SC Medicaid. However, if the federal Social Security Administration (SSA) denies your disability application, <strong>do not give up</strong>. 
            </p>
            <p style="margin: 8px 0 0 0;">
                South Carolina runs a separate, <strong>independent evaluation process</strong>. You can submit the exact same medical application directly to the state, and SC can still approve you for Medicaid independently even if the federal SSA said no.
            </p>
        </div>

        <!-- Offline County Drop-off Locator Widget Box -->
        <div class="county-widget">
            <div class="widget-title">📍 Physical In-Person Document Submission Locations</div>
            <select id="county-picker" class="select-box" onchange="showCountyOffice()">
                <option value="">-- Select client's county to find the local office --</option>
            </select>
            <div id="office-panel" class="office-display">
                <div class="office-row">🏢 <strong>In-Person Drop-Off Address:</strong><br><span id="off-address" style="font-weight: bold; color: #1C3D5A; display: block; margin-top: 4px;"></span></div>
                <div class="office-row" style="margin-top: 10px; background: #F7FAFC; padding: 10px; border-radius: 4px; border: 1px dashed #CBD5E0; font-size: 14px;">
                    🕒 <strong>Standard Operating Hours:</strong><br><span style="font-weight: bold; color: #22543D;">Open Monday-Friday, 8:30 a.m. - 5 p.m.</span>
                    <br><br>
                    ℹ️ <strong>Submission Rules:</strong> Official in-person drop-off location. If you submit paperwork here, make sure to ask the intake clerk for a physical, dated paper tracking receipt.
                </div>
                <button class="btn" style="margin-top: 12px; background: #4A5568;" onclick="copyOfficeDetails()">📋 Copy Office Details</button>
            </div>
        </div>
    </div>

    <div class="footer-banner">
        📱 <strong>Save Data:</strong> Open browser options &rarr; select <a href="#" onclick="alertPWAInstructions(); return false;">"Add to Home Screen"</a>.
    </div>

    <script src="data.js"></script>

    <script>
        const database = appPayload.policies;
        const counties = appPayload.counties;

        // Populate dropdown Menu
        const picker = document.getElementById('county-picker');
        counties.sort((a,b) => a.county.localeCompare(b.county)).forEach(item => {
            const opt = document.createElement('option');
            opt.value = item.id;
            opt.innerText = item.county + ' County Office';
            picker.appendChild(opt);
        });

        function showCountyOffice() {
            const targetId = document.getElementById('county-picker').value;
            const panel = document.getElementById('office-panel');
            if(!targetId) { panel.style.display = 'none'; return; }
            
            const match = counties.find(c => c.id === targetId);
            if(match) {
                document.getElementById('off-address').innerText = match.address;
                panel.style.display = 'block';
            }
        }

        function copyOfficeDetails() {
            const countySelect = document.getElementById('county-picker');
            const countyName = countySelect.options[countySelect.selectedIndex].text;
            const addr = document.getElementById('off-address').innerText;
            
            // Clean Clipboard Construction without the double-check hours text
            const fullText = "📍 " + countyName + " Submission Location:\\nDrop-Off Address: " + addr + "\\nHours: Open Monday-Friday, 8:30 a.m. - 5 p.m.\\n\\nNote: Official in-person drop-off location. Please request a physical paper tracking receipt from the intake clerk upon delivery.";
            
            if(navigator.clipboard) {
                navigator.clipboard.writeText(fullText);
                alert('📋 Physical office address & standard operating hours copied to clipboard!');
            }
        }

        function performSearch() {
            try {
                const query = document.getElementById('search-input').value.toLowerCase().trim();
                const container = document.getElementById('results-container');
                container.innerHTML = '';
                
                if (query.length < 2) return;
                
                const matches = database.filter(item => (item.text || "").toLowerCase().includes(query));
                if (matches.length === 0) {
                    container.innerHTML = `<p class="no-results">🔍 <strong>No rules found for "${query}".</strong></p>`;
                    return;
                }
                
                const limit = Math.min(matches.length, 40);
                for (let i = 0; i < limit; i++) {
                    const currentMatch = matches[i];
                    const dbIndex = database.findIndex(item => item.id === currentMatch.id);
                    const reg = new RegExp(query, 'gi');
                    const highlightedPreview = currentMatch.text.replace(reg, (match) => `<span class="highlight">${match}</span>`);

                    const isVisited = localStorage.getItem(currentMatch.id) === "visited";
                    const cardClass = isVisited ? 'card visited' : 'card';
                    const card = document.createElement('div');
                    card.className = cardClass;
                    card.id = 'container_' + currentMatch.id;

                    card.innerHTML = `
                        <div class="card-header" onclick="toggleBreakdown('${currentMatch.id}')">
                            <span class="source-tag">${currentMatch.source}</span>
                            <div class="rule-text">${highlightedPreview}</div>
                        </div>
                        <div class="nested-breakdown" id="breakdown_${currentMatch.id}">
                            <strong>📖 Surrounding Context Breakdown:</strong>
                            <div class="expansion-trigger" onclick="expandContext('${currentMatch.id}', ${dbIndex}, 'up')">🔼 Load Previous Paragraph</div>
                            <div class="context-stream" id="stream_${currentMatch.id}">
                                <div class="context-block current">${currentMatch.text}</div>
                            </div>
                            <div class="expansion-trigger" onclick="expandContext('${currentMatch.id}', ${dbIndex}, 'down')">🔽 Load Next Paragraph</div>
                            <div class="action-bar">
                                <button class="btn" onclick="copyBreakdownText('${currentMatch.id}')">📋 Copy Highlighted Rule</button>
                                <a class="btn btn-secondary" href="${currentMatch.url}" target="_blank" onclick="markAsVisited('${currentMatch.id}')">🌐 Open Full Original Source (Uses Data)</a>
                            </div>
                        </div>
                    `;
                    container.appendChild(card);
                    expandContext(currentMatch.id, dbIndex, 'up');
                    expandContext(currentMatch.id, dbIndex, 'down');
                }
            } catch (err) { console.error(err); }
        }

        // Context stream expansions
        function expandContext(id, baseIndex, direction) {
            const stream = document.getElementById('stream_' + id);
            const currentItem = database[baseIndex];
            if (direction === 'up') {
                if (typeof stream.dataset.topIndex === 'undefined') stream.dataset.topIndex = baseIndex;
                let nextTop = parseInt(stream.dataset.topIndex) - 1;
                if (nextTop >= 0 && database[nextTop].source === currentItem.source) {
                    const block = document.createElement('div');
                    block.className = 'context-block';
                    block.innerText = database[nextTop].text;
                    stream.insertBefore(block, stream.firstChild);
                    stream.dataset.topIndex = nextTop;
                }
            } else if (direction === 'down') {
                if (typeof stream.dataset.bottomIndex === 'undefined') stream.dataset.bottomIndex = baseIndex;
                let nextBottom = parseInt(stream.dataset.bottomIndex) + 1;
                if (nextBottom < database.length && database[nextBottom].source === currentItem.source) {
                    const block = document.createElement('div');
                    block.className = 'context-block';
                    block.innerText = database[nextBottom].text;
                    stream.appendChild(block);
                    stream.dataset.bottomIndex = nextBottom;
                }
            }
        }

        function toggleBreakdown(id) {
            const panel = document.getElementById('breakdown_' + id);
            const isVisible = panel.style.display === 'block';
            document.querySelectorAll('.nested-breakdown').forEach(el => el.style.display = 'none');
            if (!isVisible) { panel.style.display = 'block'; markAsVisited(id); }
        }

        function markAsVisited(id) {
            localStorage.setItem(id, "visited");
            const wrapper = document.getElementById('container_' + id);
            if (wrapper) wrapper.classList.add('visited');
        }

        function copyBreakdownText(id) {
            const panel = document.getElementById('breakdown_' + id);
            const currentText = panel.querySelector('.context-block.current').innerText;
            if (navigator.clipboard) {
                navigator.clipboard.writeText(currentText);
                alert('📋 Rule text copied directly to your device clipboard!');
            }
        }

        function alertPWAInstructions() {
            alert('To save data, open your browser options menu and tap "Add to Home Screen". This locks the app onto your phone so you can search the manual completely offline without wasting cellular data plans.');
        }
    </script>
</body>
</html>
"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("✨ SUCCESS! Self-contained data array compiled directly into the application layer.")

if __name__ == "__main__":
    generate_portal()