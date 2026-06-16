import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime

def run_audit(url):
    report_content = f"# Audit Report: {url}\n"
    report_content += f"**Timestamp:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    report_content += "## Identified Issues\n"
    
    issues = []
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        if not soup.title or not soup.title.string:
            issues.append("- ❌ Missing Page Title")
    except Exception as e:
        issues.append(f"- ⚠️ Connection failed: {str(e)}")
    
    if not issues:
        report_content += "✅ No issues found!"
    else:
        report_content += "\n".join(issues)
    return report_content, len(issues)

if __name__ == "__main__":
    if not os.path.exists('results'):
        os.makedirs('results')

    with open('sites.txt', 'r') as f:
        urls = [line.strip() for line in f if line.strip()]

    summary_lines = ["# Daily Audit Summary\n", f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n", "| Website | Status | Issues Found |", "| :--- | :--- | :--- |"]

    for url in urls:
        print(f"Auditing: {url}")
        content, issue_count = run_audit(url)
        
        # Save individual file
        filename = f"results/{url.replace('https://', '').replace('/', '_')}.md"
        with open(filename, 'w') as f:
            f.write(content)
        
        # Add to summary table
        status = "✅ Healthy" if issue_count == 0 else "❌ Issues Found"
        summary_lines.append(f"| [{url}]({filename}) | {status} | {issue_count} |")

    # Save summary file
    with open("SUMMARY.md", "w") as f:
        f.write("\n".join(summary_lines))
