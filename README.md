SARAL Schemes Scraper
A web scraping tool built to extract, organize, and store details of Indian government schemes for the SARAL Local Language Digital Assistant project. This scraper gathers scheme eligibility, benefits, and application information from official portals and outputs structured text files, enabling easy search and integration with downstream SARAL tools.

Table of Contents
Project Description

Features

Dependencies

Project Structure

How to Run the Scraper

Configuration (sources.yaml)

Output Data

Code Documentation

License

Contributing

Project Description
This project scrapes publicly available information about Indian government schemes from official web portals. Data is extracted for use in SARAL, a local language assistant, helping users discover scheme eligibility, benefits, and application steps in an accessible, digital form.

Features
Automated scraping of government scheme details using Python and Selenium.

Flexible configuration of source URLs via sources.yaml.

Outputs structured text data for integration with other tools or databases.

Handles navigation, error checking, and retries for robust operation.

Dependencies
Python: 3.8+

pip packages:

selenium

PyYAML

requests (if used)

beautifulsoup4 (if used)

Web Driver:

ChromeDriver version compatible with your installed Google Chrome browser.
bash
pip install selenium PyYAML requests beautifulsoup4
Project Structure
text
SARAL-Schemes-Scraper/
│
├─ chromedriver-win64/         # WebDriver binary directory
├─ extracted_text/             # Folder for scheme text outputs
├─ objects/                    # Additional data or helpers
│
├─ check_robots.py             # Script for robots.txt checks
├─ extract_and_save.py         # Main scraping and saving script
├─ extract_text.py             # Additional extraction logic
├─ fetch_and_save.py           # Scraper with fetch logic
├─ main_scraper.py             # Entry point for multi-page scraping
├─ safe_fetch.py               # Helper for reliable fetching
├─ save_html.py                # Save HTML snapshots
├─ selenium_test.py            # Test script for Selenium setup
├─ sources.yaml                # URLs/config for sites/schemes
├─ LICENSE                     # Project license
└─ README.md                   # Project documentation
How to Run the Scraper
Clone the Repository:

bash
git clone https://github.com/24rithika/SARAL-Schemes-Scraper.git
cd SARAL-Schemes-Scraper
Install the Requirements:

bash
pip install -r requirements.txt
(Or install individual dependencies as shown above.)

Download and Place ChromeDriver:

Place the correct chromedriver.exe version in chromedriver-win64/, matching your local Chrome browser version.

Configure sources.yaml:

Add scheme names and their target URLs (see below section).

Run the Main Script:

bash
python main_scraper.py
# or specific script, as needed
Outputs will be saved as text files in extracted_text/.

Configuration (sources.yaml)
Structure:

text
schemes:
  - name: "Pradhan Mantri Fasal Bima Yojana"
    url: "https://pmfby.gov.in/"
  - name: "Soil Health Card"
    url: "https://soilhealth.dac.gov.in/"
  # Add more schemes as needed
To add new schemes, simply append to the list.

Output Data
Scraped text files for each scheme are saved under the extracted_text/ directory.

File content includes the scheme name, summary, eligibility, benefits, and application steps, depending on what is available on the official source.

Code Documentation
Each function in the codebase contains docstrings explaining its purpose, arguments, and outputs.

Main scripts are commented for easy navigation and understanding.

For any improvements, follow the inline code comments as a guide to extend scraping functionality.

License
This project is licensed under the MIT License. See LICENSE for details.

Contributing
Pull requests and issue reports are welcome! For major changes, please open an issue first to discuss what you would like to change.
