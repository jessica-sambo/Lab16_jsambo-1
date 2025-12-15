'''
Lab16_jsambo-1.py
Jessica Sambo
12/14/2025

The Ohio Unemployment Rate dataset from 1976 to 2022 is read from the
'OHUR.csv' file. The header information is analyzed to determine the
indices of relevant data. Each date and their respective unemployment
rates are extracted from the dataset. A line graph of the extracted data
is displayed to showcase the change in Ohio unemployment rates from 1976
to 2022. 
'''
from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('OHUR.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Analyze header information.
for index, header in enumerate(header_row):
    print(f"{index}: {header}")

# Extract dates and unemployment rates.
dates, rates = [], []
for row in reader:
    current_date = datetime.strptime(row[0], "%Y-%m-%d")
    rate = float(row[1])
    dates.append(current_date)
    rates.append(rate)

# Plot the unemployment rates.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, rates, color='green')

# Format plot.
ax.set_title("Ohio Unemployment (by Month): 1976 - 2022", fontsize=24)
ax.set_xlabel('Date', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Unemployment Rate (%)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()