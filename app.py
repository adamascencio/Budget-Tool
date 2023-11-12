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

    # Once signed in press View Account button
    view_account_btn = driver.find_element(
        By.XPATH,
        '//*[@id="summary-2wemaSiywpo8hJ4kC/tJvafGS6jb6u9/SJAOu6r9jUk="]',
    )
    view_account_btn.click()

    # Click Download Transactions button
    expand_account_services_btn = driver.find_element(By.ID, "moreAccountServicesLink")
    expand_account_services_btn.click()

    # Set File Type to CSV and Time Period for a one-month period
    download_transactions_link = driver.find_element(
        By.XPATH,
        '//*[@id="c1-ease-dialog-0"]/div/c1-ease-card-more-account-services/c1-ease-dialog/div[2]/c1-ease-dialog-content/div/div[2]/div[4]/ul/li[4]',
    )
    download_transactions_link.click()
    file_type_dropdown = driver.find_element(By.NAME, "file-type-selection")
    file_type_dropdown.click()
    csv_option = driver.find_element(By.ID, "c1-ease-option-0")
    csv_option.click()
    time_period_field = driver.find_element(By.ID, "c1-ease-select-5")
    time_period_field.click()
    custom_date_option = driver.find_element(By.ID, "c1-ease-option-6")
    custom_date_option.click()
    start_date_field = driver.find_element(By.NAME, "startDate")
    start_date_field.send_keys("10/01/2023")
    end_date_field = driver.find_element(By.NAME, "endDate")
    end_date_field.send_keys("10/31/2023")
    submit_btn = driver.find_element(By.XPATH, '//*[@type="submit"]')
    submit_btn.click()

    time.sleep(5)  # Pause after script execution to allow page to load

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Quit the driver session
    driver.quit()
