#!/usr/bin/python3

import sys
import calendar
from datetime import datetime
from datetime import date
from tree import show_tree

def show_noel(date_donnee):
    if len(date_donnee) == 1:
            date_donnee = datetime.now()
    else:
        date_donnee = date_donnee[1]
        date_donnee = datetime.strptime(date_donnee, '%Y-%m-%d')
    
    if date_donnee.day > 25 and date_donnee.month > 11:
        noel = datetime(date_donnee.year + 1, 12, 25)
    else:
        noel = datetime(date_donnee.year, 12, 25)
    
    jours_noel = (noel - date_donnee).days
    

    print(jours_noel, "days before christmas\n")

    c = calendar.TextCalendar (calendar.MONDAY)
    
    calendrier = c.formatmonth (date_donnee.year, 12, 1, 0)

    if date_donnee.day > 25 and date_donnee.month > 11:
        for i in range (1, 13, 1):
            calendrier = calendrier + c.formatmonth (date_donnee.year + 1, i, 1, 0)
        return calendrier
    elif date_donnee.day == 25 and date_donnee.month == 12:
        return show_tree(10)
    else:
        for i in range (date_donnee.month, 13, 1):
            calendrier = c.formatmonth (date_donnee.year, i, 1, 0)
        return calendrier

if __name__ == "__main__":
    print(show_noel(sys.argv))