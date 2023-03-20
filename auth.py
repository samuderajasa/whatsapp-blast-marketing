from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os

def element_presence(by, selector, time):
    element_present = EC.presence_of_element_located((By.CSS_SELECTOR, selector))
    WebDriverWait(driver, time).until(element_present)

# Get the path of the current working directory
cwd = os.getcwd()

# Create a subdirectory for storing cookies so you don't have to login everytime
cookies_dir = os.path.join(cwd, 'cookies')

# Replace below path with the absolute path
# to chromedriver in your computer

options = webdriver.ChromeOptions()
options.add_argument(f"user-data-dir={cookies_dir}")
ser = Service(r"C:/Users/Azalea/chromedriver.exe")

#Add your path to the chromedriver where you have installed it
driver = webdriver.Chrome(service=ser, options=options)
driver.get('https://web.whatsapp.com')

element_presence(By.CSS_SELECTOR, 'div[data-testid="chat-list-search-container"]', 3600)