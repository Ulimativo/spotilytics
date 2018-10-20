#get_charts.py
from bs4 import BeautifulSoup as bs
import requests
import click
from pathlib import Path

#local imports
from libs import fileHandler as fh
from libs import chartHandler as ch
from libs import basicHandler as bh

#global variables
CHART_PATH="chart_files/"

'''
File containing CLI-based basic functions for webscraping, file generation, etc. of
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


@click.group()
def main():
    """ Entry: YYYY-MM-YY """
    pass

@main.command()
@click.argument('date')
@click.option('--country', '-c', help="enter country code (e.g. us = United States, de = Germany, etc. ) or global (default)", default="global")
def single(date, country):
    """retrieves and generates Chart-Data for a single date"""
    print(f"Your chosen date: {date}")
    print("now loading data...")
    daily(date, country)

@main.command()
@click.argument('earliest')
@click.option('--country', '-c', help="enter country code (e.g. us = United States, de = Germany, etc. ) or global (default)", default="global")
def range(earliest, country):
    """ retrieves and generates Chart-Data from a given date until yesterday"""
    list_dates=bh.build_daterange(earliest)
    print(f"Your chosen date range: {earliest} - Yesterday ({len(list_dates)} days)")
    print("Date range generator...")
    for date in list_dates:
        daily(date, country)
    print("Script finished.")

if __name__ =="__main__":
    p=Path(CHART_PATH)
    if p.exists() == False:
        p.mkdir(parents=True, exist_ok=True)
        print(f"Directory not found, thus created: {CHART_PATH}")

    main()
