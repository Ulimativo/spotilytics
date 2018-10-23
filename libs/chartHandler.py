from pathlib import Path
from os import listdir
from os.path import isfile,join
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

#CHART_PATH="chart_files/"
SPOTIFY_URL="https://spotifycharts.com/regional/at/daily/"


def get_daily(date,url):
    """get data from spotifycharts.com with given date as beautiful soup object"""
    url=url+date
    page=requests.get(url)
    soup=bs(page.content,'html.parser')
    if soup_valid(soup) == False:
        print(f"ERROR: {date} - Soup is not valid. Please try another date.")
    else:
        table=soup.find(class_="chart-table")
        df=clean_table(table)
        print(f"{date} - Soup eaten, Table clean. Returning Frame.")
        return df

def soup_valid(soup):
    """check if date charts are valid/available"""
    table=soup.find(class_="chart-table")
    #soup_check=soup.find(class_="not-found")
    #soup_check_error=soup.find(class_="chart-error")
    #if soup_check or soup_check_error is None:
    if table is None:
        return False
    else:
        return True

def clean_table(table):
    """clean up the raw data from soup into a dataframe"""
    #table=soup.find(class_='chart-table')
    td={}
    td[1]=table.find_all(class_='chart-table-track')
    td[2]=table.find_all(class_='chart-table-streams')
    td[1].pop(0)
    td[2].pop(0)
    #check section with Spotify-Track URls
    td[3]=table.find_all(class_='chart-table-image')
    list_links=[]
    for el in td[3]:
        for a in el.find_all('a', href=True):
            list_links.append(a['href'])
    list_tracks=[]
    list_artists=[]
    for el in td[1]:
        text=el.get_text()
        obj=text.split('by')
        list_tracks.append(obj[0])
        list_artists.append(obj[1])

    list_streams=[]
    for el in td[2]:
        list_streams.append(el.get_text())

    list_final=[list_artists,list_tracks,list_streams,list_links]

    df=pd.DataFrame.from_dict(list_final, orient='columns')
    df=df.T
    df.columns=['Artist','Track','Streams','URL']
    df['Artist']=df['Artist'].str.strip()
    df['Track']=df['Track'].str.strip()
    df['Streams']=df['Streams'].str.replace(',','')
    df.index += 1
    df['Streams'] = pd.to_numeric(df['Streams'])
    df.index.name="POS"
    return df

def save_csv(df,filename):
    """Save dataframe to csv with given date as filename"""
    df.to_csv(filename)
    return "File generated: {}".format(filename)

def build_save(date):
    """build dataframe, then save is as csv in given path"""
    return "Frame built, file saved."

"""
Functions used in ask_basics_cli
"""

def build_frame(file):
    df=pd.read_csv(CHART_PATH+file)
    return df

def load_frame(daterange):
    for i in daterange:
        print(i)
    return
