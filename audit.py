import requests
from bs4 import BeautifulSoup
import json
import os

def run_audit(url):
    results = {"url": url, "issues": []}
    
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Example Check: Title Tag
        if not soup.title or not soup.title.string:
            results["issues"].append("Missing Page Title")
            
        # Example Check: Broken Link (Internal)
        for link in soup.find_all('a', href=True):
            if link['href'].startswith('/'):
                full_link = url.rstrip('/') + link['href']
                if requests.head(full_link).status_code == 404:
                    results["issues"].append(f"Broken Link: {full_link}")
                    
    except Exception as e:
        results["issues"].append(f"Connection failed: {str(e)}")

    # Save to file for GitHub Action to pick up
    with open('report.json', 'w') as f:
        json.dump(results, f, indent=4)
    print("Audit complete. Report saved as report.json")

if __name__ == "__main__":
    target = os.getenv("TARGET_URL", "https://example.com")
    run_audit(target)
