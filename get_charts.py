#get_charts.py

from bs4 import BeautifulSoup as bs
import requests

#local imports
from libs import fileHandler as fh
from libs import chartHandler as ch
from libs import basicHandler as bh

#global variables
CHART_PATH="chart_files/"

'''
File containing basic functions for webscraping, file generation, etc. of
data from the official spotifycharts.com Website for use in further analysis.
'''
def daily(date,country):
    url=f"https://spotifycharts.com/regional/{country}/daily/"
    frame_charts=ch.get_daily(date, url)
    if frame_charts is None:
        print(f"ERROR: {date} - No dataframe was handled, no file created.")
    else:
        date=date+f"_{country}"
        if (fh.check_file(CHART_PATH+date+".csv") == True):
            overwrite=click.prompt(
                "File exists. Do you want to overwrite? (y/n)", default='n'
                )
            if overwrite == 'y':
                print("Overwriting file...")
                ch.save_csv(frame_charts,date)
            else:
                print("No Action.")
        else:
            ch.save_csv(frame_charts, date)
    return "Finished for {}".format(date)
