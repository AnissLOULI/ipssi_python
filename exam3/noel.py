import sys
import calendar
from datetime import datetime
from datetime import date

def show_noel(d):
    if len(d) == 1:
        d = date.today()
    else:
        d = d[1]
        d = datetime.strptime(d, '%Y-%m-%d').date()

    if d.day > 25 and d.month == 12:
        noel = date(d.year + 1, 12, 25)
    else:
        noel = date(d.year , 12, 25)
    
    jours_noel = noel - d

    c = calendar.TextCalendar (calendar.MONDAY)
    stra = c.formatmonth (d.year, d.month, 1, 0)

    if d.day > 25 and d.month > 11:
        print (stra)
        for i in range (1, 13, 1):
            calendrier = c.formatmonth (d.year + 1, i, 1, 0)
    else:
        for i in range (d.month, 13, 1):
            calendrier = c.formatmonth (d.year, i, 1, 0)

    return str(jours_noel.days) + " days before christmas\n"




