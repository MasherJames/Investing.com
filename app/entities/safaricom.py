import time
import requests
from datetime import datetime, date, timedelta
from requests.exceptions import HTTPError
from app import create_app
from app.celery import make_celery
from app.utils.scrap import ScrapParsePersist


today = date.today()
sevenDaysAgo = today - timedelta(days=7)

payload = {
    "curr_id": "941227",
    "smlID": "1508998",
    "header": "SCOM Historical Data",
    "st_date": sevenDaysAgo.strftime("%m/%d/%Y"),
    "end_date": today.strftime("%m/%d/%Y"),
    "interval_sec": "Daily",
    "sort_col": "date",
    "sort_ord": "DESC",
    "action": "historical_data"
}

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/81.0.4044.138 Chrome/81.0.4044.138 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "Host": "www.investing.com",
    "Referer": "https://www.investing.com/equities/safaricom-historical-data",
    "Connection": "keep-alive"
}


app = create_app()
celery = make_celery(app)
url = "https://www.investing.com/instruments/HistoricalDataAjax"


@celery.task
def triggerScrapParsePersist():

    # Scrap
    source = ScrapParsePersist().scrap(payload, headers)
    # parse
    parsed_data = ScrapParsePersist().parse_data(source)
    # store in csv
    ScrapParsePersist().store_in_csv(parsed_data, "safaricom")
    # add company to add its data
    ScrapParsePersist().add_company("safaricom")
    # store historical data to db
    ScrapParsePersist().store_data_in_db(parsed_data, "safaricom")
