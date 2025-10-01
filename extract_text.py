from bs4 import BeautifulSoup

def extract_text(html):
    """
    Extracts the page title and main text from HTML content.
    Returns: (title, text)
    """
    soup = BeautifulSoup(html, "lxml")
    
    # Remove unwanted tags
    for t in soup(["script", "style", "noscript"]):
        t.decompose()
    
    # Get title: prefer <h1>, then <title>
    if soup.find("h1"):
        title = soup.find("h1").get_text(strip=True)
    elif soup.find("title"):
        title = soup.find("title").get_text(strip=True)
    else:
        title = ""
    
    # Extract main text from article or paragraphs
    article = soup.find("article")
    if article:
        text = " ".join(p.get_text(" ", strip=True) for p in article.find_all("p"))
    else:
        paragraphs = [p.get_text(" ", strip=True) for p in soup.find_all("p") if p.get_text(strip=True)]
        text = " ".join(paragraphs)
    
    text = " ".join(text.split())
    return title, text

if __name__ == "__main__":
    # Replace with your actual HTML file path:
    html_file = "objects/pmkisan/2025-09-28-103000.html"
    
    # Open and read HTML file
    with open(html_file, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # Extract title and main text
    title, main_text = extract_text(html_content)
    
    print("Page Title:", title)
    print("\nMain Text (First 500 chars):\n", main_text[:500])
