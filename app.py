#! Python3
# - Download transaction data from Mint.com and save to a CSV file

import os, shutil
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import login_url
from dotenv import load_dotenv

load_dotenv()

USER_EMAIL = os.getenv("EMAIL")
USER_PASSWORD = os.getenv("PASSWORD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)
driver.get(login_url)
try:
    driver.find_element(By.NAME, "Email").send_keys(USER_EMAIL)
except:
    print("Email field not found")

try:
    submit_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_btn.click()
except:
    print("Submit button not found")
