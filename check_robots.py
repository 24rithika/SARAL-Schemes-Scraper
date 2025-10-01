import requests

url = "https://pmkisan.gov.in/robots.txt"
response = requests.get(url)

if response.status_code == 200:
    print("robots.txt content:")
    print(response.text)
else:
    print(f"Failed to get robots.txt, status code: {response.status_code}")
