import os
from datetime import datetime

# This function saves html_content in a timestamped file within objects/source_name/ folder
def save_raw_html(source_name, html_content):
    # Step 1: Make folder path objects/source_name
    folder_path = os.path.join("objects", source_name)
    os.makedirs(folder_path, exist_ok=True)  # Create folder if not exists
    
    # Step 2: Create timestamp-based filename
    timestamp = datetime.now().strftime("%Y-%m-%d-%H%M%S")
    filename = f"{timestamp}.html"
    
    # Step 3: Full file path for save
    file_path = os.path.join(folder_path, filename)
    
    # Step 4: Write the raw HTML content to the file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"HTML saved at: {file_path}")
    return file_path

# Example usage with your fetched HTML
if __name__ == "__main__":
    source = "pmkisan"
    sample_html = "<html><body><h1>Example Content</h1></body></html>"
    save_raw_html(source, sample_html)
