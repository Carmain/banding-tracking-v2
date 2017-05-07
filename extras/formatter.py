from django.utils.translation import ugettext_lazy as _

import datetime
import re


def format_time(str_time):
    time = None
    if(str_time != ''):
        time_format = '%H:%M'
        if(re.match(r'\d{1,2}h\d{2}', str_time)):
            time_format = '%Hh%M'
        elif(re.match(r'\d{1,2}H\d{2}', str_time)):
            time_format = '%HH%M'

        time = datetime.datetime.strptime(str_time, time_format)

    return time


def format_date(str_date):
    date = None
    if(str_date != ''):
        date = datetime.datetime.strptime(str_date, '%d/%m/%Y')

    return date


def format_color(color):
    color = color.lower()
    code_color = None

    if(color == 'rouge'):
        code_color = 'R'  # Red
    elif(color == 'rose'):
        code_color = 'P'  # Pink
    elif(color == 'blanc'):
        code_color = 'W'  # White
    elif(color == 'jaune'):
        code_color = 'Y'  # Yellow
    elif(color == 'vert'):
        code_color = 'G'  # Green

    return code_color
