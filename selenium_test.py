from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to your chromedriver.exe
service = Service(r'C:\Users\98496\SARAL\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Your target URL
driver.get('https://saanjhi.gov.in')

# Wait for specific element to load, e.g., h1 tag
try:
    h1_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    ).text
    print(h1_text)
except Exception as e:
    print("Couldn't find h1:", e)

driver.quit()
