#basicHandler
from datetime import date, timedelta
from datetime import datetime as dt

def build_daterange(earliest):
    earliest=format_date(earliest)
    start=date(int(earliest[0]),int(earliest[1]),int(earliest[2]))
    end=date.today()-timedelta(1)
    base = (end-start).days+1
    date_list = [(end - timedelta(days=x)).strftime("%Y-%m-%d") for x in range(0, base)]
    return date_list

def format_date(date):
    date=date.split('-')
    return date
