import os
from datetime import datetime
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Safe fetch function with retries
def safe_get(url, timeout=15, max_retries=3):
    session = requests.Session()
    
    retries = Retry(
        total=max_retries,
        backoff_factor=0.5,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET"]
    )
    
    adapter = HTTPAdapter(max_retries=retries)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    
    headers = {
        "User-Agent": "SaralBot/1.0 (+https://yourdomain.example)"
    }
    
    response = session.get(url, headers=headers, timeout=timeout, verify=False)  # Added verify=False due to cert issues
    response.raise_for_status()
    return response.text

# Save HTML content function 
def save_raw_html(source_name, html_content):
    folder_path = os.path.join("objects", source_name)
    os.makedirs(folder_path, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y-%m-%d-%H%M%S")
    filename = f"{timestamp}.html"
    file_path = os.path.join(folder_path, filename)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"Saved HTML to: {file_path}")
    return file_path

# Main script: fetch and save
if __name__ == "__main__":
    source = "pmkisan"
    url = "https://pmkisan.gov.in"
    
    try:
        html = safe_get(url)
        save_raw_html(source, html)
    except requests.HTTPError as e:
        print(f"HTTP error: {e}")
    except Exception as e:
        print(f"Error: {e}")
