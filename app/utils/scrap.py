# This file handles Scraping of the data, storing it to the database and creating a csv file also for the same
import requests

url = "https://www.investing.com/instruments/HistoricalDataAjax"


def weird():
    response = requests.post(url, data=payload, headers=headers)
    print(response)
