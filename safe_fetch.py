import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def safe_get(url, timeout=15, max_retries=3):
    # Create a session object to persist settings
    session = requests.Session()
    
    # Define retry strategy: number of retries and error status codes to retry on
    retries = Retry(
        total=max_retries,              # Max retries (e.g., 3)
        backoff_factor=0.5,             # Wait time doubling after failure (0.5s, 1s, 2s...)
        status_forcelist=[429, 500, 502, 503, 504],  # HTTP errors to retry on
        allowed_methods=["GET"]         # Only retry GET requests
    )
    
    # Attach the retry strategy to the session
    adapter = HTTPAdapter(max_retries=retries)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    
    # Set a friendly user-agent for your scraper
    headers = {
        "User-Agent": "SaralBot/1.0 (+https://yourdomain.example)"
    }
    
    # Make the GET request
    response = session.get(url, headers=headers, timeout=timeout, verify=False)

    
    # If response has error status, this line throws an exception
    response.raise_for_status()
    
    # Return the content (HTML) as text
    return response.text


# Example usage:
if __name__ == "__main__":
    url = "https://pmkisan.gov.in"
    try:
        html = safe_get(url)
        print("Page fetched successfully! Here's a preview:")
        print(html[:500])  # Show first 500 characters
    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Error occurred: {err}")
