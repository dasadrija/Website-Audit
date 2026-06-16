

# Website Audit Tool (Customer Success Edition)
This tool provides a proactive way for Customer Success Engineers to monitor website health across multiple client sites. It identifies broken links, missing SEO meta-tags, and connectivity issues.
## 🛠 Prerequisites
 1. **Python 3.x** installed.
 2. **Required Libraries:** Install them once via your terminal:
   ```bash
   pip install requests beautifulsoup4
   
   ```
## 🚀 How to Use
### 1. Add Your Target URLs
Open the sites.txt file in your repository folder and add the websites you want to audit. Place one URL per line:
```text
https://example.com
https://client-site.org

```
### 2. Run the Audit
Execute the script from your terminal:
```bash
python audit.py

```
### 3. Review the Output
The script automatically generates reports in two formats:
 * **Individual Reports:** Located in the /results folder (e.g., results/example.com.md). Each file contains the specific issues found for that domain.
 * **Master Dashboard (SUMMARY.md):** Located in the root directory. This file provides a clean, clickable table showing the current status ("Healthy" or "Issues Found") and the number of issues for every site in your sites.txt.
## 🔄 Updating your Repository
Since this workflow is manual, you control when updates are pushed to GitHub:
 1. **Add changes:** git add results/*.md SUMMARY.md
 2. **Commit:** git commit -m "Run daily site audit"
 3. **Push:** git push origin main
## 📊 Why Use This?
 * **Proactive Success:** Spot issues before your clients do.
 * **Audit History:** By pushing your reports to GitHub, you create a time-stamped history of site health.
 * **Stakeholder Ready:** The SUMMARY.md is formatted as a human-readable table, making it perfect for copying into emails or client status reports.

