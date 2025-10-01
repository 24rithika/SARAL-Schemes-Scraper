import yaml
import requests
from bs4 import BeautifulSoup
import os

def fetch_save_extract(name, url):
    print(f"Scraping: {name} - {url}")
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to fetch {url} with status {response.status_code}")
            return
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract title or use scheme name as fallback
        title = soup.title.string if soup.title else name
        
        # Extract all visible text (simple approach)
        main_text = soup.get_text(separator='\n', strip=True)
        
        # Prepare output folder and filename
        folder = 'extracted_text'
        os.makedirs(folder, exist_ok=True)
        safe_name = "".join(c for c in name if c.isalnum() or c in (" ", "-")).rstrip()
        file_path = os.path.join(folder, f"{safe_name}.txt")
        
        # Save extracted text
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(title + "\n\n" + main_text)
        
        print(f"Saved extracted text for {name} at: {file_path}")
    
    except Exception as e:
        print(f"Error scraping {name}: {e}")

def main():
    # Load all schemes from sources.yaml
    with open("sources.yaml", "r", encoding="utf-8") as f:
        schemes = yaml.safe_load(f)
    
    for scheme in schemes:
        scheme_name = scheme.get("name", "unknown")
        scheme_url = scheme.get("url", "")
        
        # Skip schemes with no valid URL
        if not scheme_url or scheme_url.lower() == "varies by state":
            print(f"Skipping scheme {scheme_name}: URL not fixed or empty.")
            continue
        
        print(f"Processing scheme: {scheme_name}")
        print(f"URL: {scheme_url}")
        
        # Call the fetch-save-extract function
        fetch_save_extract(scheme_name, scheme_url)

if __name__ == "__main__":
    main()
