#! Python3
# - Download transaction data from Mint.com and save to a CSV file

import os, shutil
from selenium import webdriver
from utils import login_url

browser = webdriver.Chrome()
browser.get(login_url)
