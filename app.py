#! Python3
# - Download transaction data from capitalone.com and save to a CSV file

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

# Initialize the WebDriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to become available
driver.get(login_url)

try:
    # Input Email & Password
    email_field = driver.find_element(By.ID, "ods-input-0")
    email_field.send_keys(USER_EMAIL)
    password_field = driver.find_element(By.ID, "ods-input-1")
    password_field.send_keys(USER_PASSWORD)

    # Click the Sign In button
    submit_btn = driver.find_element(By.ID, "noAcctSubmit")
    submit_btn.click()

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Quit the driver session
    driver.quit()
