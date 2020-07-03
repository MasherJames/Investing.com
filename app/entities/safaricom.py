from celery.schedules import crontab

from app.celery import celery
from app.utils.scrap import ScrapParsePersist
from app.utils.date import start_date, end_date

payload = {
    "curr_id": "941227",
    "smlID": "1508998",
    "header": "SCOM Historical Data",
    "st_date": start_date,
    "end_date": end_date,
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


# add triggerScrapParsePersist task to the beat schedule

celery.conf.beat_schedule = {
    # Executes every Monday midnight at 0000hrs
    'scarp-persist-every-monday': {
        'task': 'tasks.triggerScrapParsePersist',
        'schedule': crontab(minute='*/2')
    }
}

# day_of_week = 1, hour = 0
