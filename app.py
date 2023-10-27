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

driver = webdriver.Chrome()
driver.get(login_url)
driver.find_element(By.NAME, "Email").send_keys(USER_EMAIL)
