# ask_basics_cli.py
import click
from libs import chartHandler as ch
from libs import fileHandler as fh
import pandas as pd

#global variables
CHART_PATH="chart_files/"

@click.group()
def main():
    """ various basic anlytics of Spotify's Top-200 daily charts """
    pass

@main.command()
#@click.argument('date')
@click.option('--daterange','-dr',
            help="Show sum of Streams (Top-200) for given date-range, default = 7 (1 week)",
            default=7)
def get_sum(daterange):
    """calculate total sum of streams per day"""
    print(f"Retrieving data for selected daterange of {daterange} last days")
    list_files=sorted(fh.get_files(CHART_PATH), reverse=True)
    list_range=list_files[:daterange]
    sum_frame={}
    for file in list_range:
        frame=ch.build_frame(file)
        sum_frame[file]=frame['Streams'].sum()
    df=pd.DataFrame.from_dict(sum_frame, orient='index')
    print(df)

if __name__ =="__main__":
    main()
