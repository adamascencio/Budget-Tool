import os, datetime, sys, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import cap_one_login_url
from dotenv import load_dotenv

if len(sys.argv) < 2:
    print("Usage: python capitalone.py <month> (e.g. 10 for October)")
    sys.exit()

# Load environment variables from .env file
load_dotenv()

# Retrieve user credentials
USER_EMAIL = os.getenv("EMAIL")
USER_PASSWORD = os.getenv("PASSWORD")

# Initialize the WebDriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to become available
driver.get(cap_one_login_url)

# Get the current date
user_month = int(sys.argv[1])
current_date = datetime.date.today()
first_day_of_month = datetime.date(current_date.year, user_month, 1)

# Calculate the first day of the next month and handle year rollover
if sys.argv[1] == 12:
    first_day_of_next_month = datetime.date(current_date.year + 1, 1, 1)
else:
    first_day_of_next_month = datetime.date(
        current_date.year, user_month + 1, 1
    )

# Get the last day of the current month by subtracting one day from the first day of the next month
last_day_of_month = first_day_of_next_month - datetime.timedelta(days=1)

# Format dates in "MM/DD/YYYY" format
formatted_first_day = first_day_of_month.strftime("%m/%d/%Y")
formatted_last_day = last_day_of_month.strftime("%m/%d/%Y")
time.sleep(5) # Wait for page to load
# Download transaction data from Capital One in CSV format
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

    # Navigate to download transactions page
    expand_account_services_btn = driver.find_element(By.ID, "moreAccountServicesLink")
    expand_account_services_btn.click()
    download_transactions_link = driver.find_element(
        By.XPATH,
        '//*[@id="c1-ease-dialog-0"]/div/c1-ease-card-more-account-services/c1-ease-dialog/div[2]/c1-ease-dialog-content/div/div[2]/div[4]/ul/li[4]',
    )
    download_transactions_link.click()

    # Set File Type to CSV and Time Period for a one-month period
    # then download transaction data
    file_type_dropdown = driver.find_element(By.NAME, "file-type-selection")
    file_type_dropdown.click()
    csv_option = driver.find_element(By.ID, "c1-ease-option-0")
    csv_option.click()
    time_period_field = driver.find_element(By.ID, "c1-ease-select-5")
    time_period_field.click()
    custom_date_option = driver.find_element(By.ID, "c1-ease-option-6")
    custom_date_option.click()
    start_date_field = driver.find_element(By.NAME, "startDate")
    start_date_field.send_keys(formatted_first_day)
    end_date_field = driver.find_element(By.NAME, "endDate")
    end_date_field.send_keys(formatted_last_day)
    submit_btn = driver.find_element(By.XPATH, '//*[@type="submit"]')
    submit_btn.click()
    time.sleep(5)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Quit the driver session
    driver.quit()
