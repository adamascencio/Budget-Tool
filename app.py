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

# Initialize the WebDriver with incognito mode
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
driver = webdriver.Chrome(options=options)
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

    # Once signed in press View Account button
    view_account_btn = driver.find_element(
        By.XPATH,
        '//*[@id="summary-KWxnZbD1AqCYe4O7QtjU4uHMG41clRuDfSWfARfJIFeiDtoAmObLgoL7BkDmU5/Z"]',
    )
    view_account_btn.click()

    # Click Download Transactions button
    download_transactions_btn = driver.find_element(
        By.ID, "downloadStatementTransactions"
    )
    download_transactions_btn.click()

    # Set File Type to CSV and Time Period for a one-month period
    time_period_dropdown_btn = driver.find_element(By.ID, "c1-ease-select-5")
    time_period_dropdown_btn.click()
    custom_date_range_btn = driver.find_element(By.ID, "c1-ease-option-7")
    custom_date_range_btn.click()
    start_date_field = driver.find_element(By.ID, "c1-ease-input-form-start-date")
    start_date_field.send_keys("10/01/2023")
    end_date_field = driver.find_element(By.ID, "c1-ease-input-form-end-date")
    end_date_field.send_keys("10/31/2023")

    time.sleep(5)  # Pause after script execution to allow page to load

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Quit the driver session
    driver.quit()
