#! Python3
# - Download transaction data from Mint.com and save to a CSV file

import os, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import login_url
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve user credentials
USER_EMAIL = os.getenv("EMAIL")
USER_PASSWORD = os.getenv("PASSWORD")

# Set up Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to become available
driver.get(login_url)

try:
    # Wait for the email input to be loaded and then input the email
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "Email"))
    )
    email_input.send_keys(USER_EMAIL)

    # Click the submit button
    submit_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    submit_btn.click()

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Quit the driver session
    driver.quit()
