#get_charts.py

from bs4 import BeautifulSoup as bs
import requests
import click

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
def daily(date):
    frame_charts=ch.get_daily(date)
    if frame_charts is None:
        print(f"ERROR: {date} - No dataframe was handled, no file created.")
    else:
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


@click.group()
def main():
    """ Entry: YYYY-MM-YY """
    pass

@main.command()
@click.argument('date')
def single(date):
    """retrieves and generates Chart-Data for a single date"""
    print(f"Your chosen date: {date}")
    print("now loading data...")
    daily(date)

@main.command()
@click.argument('earliest')
def range(earliest):
    """ retrieves and generates Chart-Data from a given date until yesterday"""
    list_dates=bh.build_daterange(earliest)
    print(f"Your chosen date range: {earliest} - Yesterday ({len(list_dates)} days)")
    print("Date range generator...")
    for date in list_dates:
        daily(date)
    print("Script finished.")

if __name__ =="__main__":
    main()
