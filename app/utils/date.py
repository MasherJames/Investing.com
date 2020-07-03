from datetime import datetime, date, timedelta

today = date.today()
sevenDaysAgo = today - timedelta(days=7)


def format_date(date_string, date_format):
    date_obj = datetime.strptime(date_string, "%B %d, %Y")
    return date_obj.strftime(date_format)


def start_date():
    return sevenDaysAgo.strftime("%m/%d/%Y")


def end_date():
    return today.strftime("%m/%d/%Y")
