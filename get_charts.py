#get_charts.py

from bs4 import BeautifulSoup as bs
import requests
from pathlib import Path

#local imports
from libs import fileHandler as fh
from libs import chartHandler as ch
from libs import basicHandler as bh

'''
File containing basic functions for webscraping, file generation, etc. of
data from the official spotifycharts.com Website for use in further analysis.
'''


#global variables
CHART_PATH=Path.cwd() / "chart_files"
if CHART_PATH.exists() == False:
    CHART_PATH.mkdir(parents=True, exist_ok=True)
    print(f"Directory not found, thus created: {CHART_PATH}")

def daily(date,country):
    url=f"https://spotifycharts.com/regional/{country}/daily/"
    frame_charts=ch.get_daily(date, url)
    if frame_charts is None:
        print(f"ERROR: {date} - No dataframe was handled, no file created.")
    else:
        date=date+f"_{country}"
        ch.save_csv(frame_charts, date)
    return "Finished for {}".format(date)
