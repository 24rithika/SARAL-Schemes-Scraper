from bs4 import BeautifulSoup
import os
from datetime import datetime

def extract_text(html):
    soup = BeautifulSoup(html, "lxml")
    for t in soup(["script", "style", "noscript"]):
        t.decompose()
    if soup.find("h1"):
        title = soup.find("h1").get_text(strip=True)
    elif soup.find("title"):
        title = soup.find("title").get_text(strip=True)
    else:
        title = ""
    article = soup.find("article")
    if article:
        text = " ".join(p.get_text(" ", strip=True) for p in article.find_all("p"))
    else:
        paragraphs = [p.get_text(" ", strip=True) for p in soup.find_all("p") if p.get_text(strip=True)]
        text = " ".join(paragraphs)
    text = " ".join(text.split())
    return title, text

def save_extracted_text(source_name, title, text):
    folder_path = os.path.join("extracted_text", source_name)
    os.makedirs(folder_path, exist_ok=True)
    safe_title = "".join(c for c in title if c.isalnum() or c in (" ", "_")).rstrip()
    if not safe_title:
        safe_title = datetime.now().strftime("%Y-%m-%d-%H%M%S")
    filename = safe_title[:50] + ".txt"
    file_path = os.path.join(folder_path, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(title + "\n\n")
        f.write(text)
    print(f"Extracted text saved to: {file_path}")
    return file_path

if __name__ == "__main__":
    html_file = "objects/pmkisan/2025-09-28-103000.html"  # Replace with your file path
    with open(html_file, "r", encoding="utf-8") as f:
        html_content = f.read()
    title, main_text = extract_text(html_content)
    save_extracted_text("pmkisan", title, main_text)