from app.utils.scrap import ScrapParsePersist


payload = {
    "curr_id": "941227",
    "smlID": "1508998",
    "header": "SCOM Historical Data",
    "st_date": "05/01/2020",
    "end_date": "06/01/2020",
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


def triggerScrapParsePersist():
    # Scrap
    source = ScrapParsePersist().scrap(payload, headers)
    # parse
    parsed_data = ScrapParsePersist().parse_data(source)
    # store in csv
    ScrapParsePersist().store_in_csv(parsed_data, "safaricom")


if __name__ == "__main__":
    triggerScrapParsePersist()
