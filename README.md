# Spotify Chart Retriever

A simple script to webscrape the daily Top-200 from spotifycharts.com and
safe locally as csv-files

## Get Charts

Using the `get_charts_cli.py` we can generate CSV files sourcing from [the official Spotifycharts Website](https://www.spotifycharts.com).
By default, the Script will generate a folder in the current directory called `chart_files` if the directory doesn't exist.
We need to state a given date (`YYYY-MM-DD) and as an option (`-c`) we can state a country code (e.g. `us` for the United States), otherwise default `global` will be used.
