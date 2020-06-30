from datetime import datetime


def format_date(date_string, date_format):
    date_obj = datetime.strptime(date_string, "%B %d, %Y")
    return date_obj.strftime(date_format)
