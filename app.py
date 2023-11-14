#! Python3
# - Download transaction data from capitalone.com and save to a CSV file

import os, csv
from glob import glob
from pathlib import Path
from openpyxl import Workbook

desktop_path = Path.home() / "Desktop"
download_path = Path.home() / "Downloads"
capital_one_dir = desktop_path / "Capital One"

os.makedirs(capital_one_dir, exist_ok=True)

# Find the most recent CSV file in the Downloads folder
csv_files = glob(os.path.join(download_path, "*.csv"))
csv_files.sort(key=os.path.getmtime, reverse=True)
newest_csv = csv_files[0] if csv_files else None

if newest_csv:
    print(f"Found the most recent CSV file: {newest_csv}")
else:
    print("No CSV files found in the Downloads folder")
    exit()

# Convert csv file to xlsx file
wb = Workbook()
ws = wb.active

with open(newest_csv, "r") as f:
    reader = csv.reader(f, delimiter=",")
    for row in reader:
        ws.append(row)

wb.save(capital_one_dir / "transactions.xlsx")
