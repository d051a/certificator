from django import template
import datetime

register = template.Library()


def notoverdue(date):
    year, month, day = date.split('-')
    cert_valid_end = datetime.datetime(int(year), int(month), int(day))
    now_date = datetime.datetime.now()
    time_delta = cert_valid_end - now_date
    result, *_ = str(time_delta).split(' ')
    seconds = time_delta.total_seconds()
    hours = seconds // 3600
    return hours
