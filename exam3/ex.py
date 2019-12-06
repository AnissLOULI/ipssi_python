import sys
import calendar
from datetime import datetime
from tree import show_tree

def show_noel(date_donnee):
    date_donnee = datetime.strptime(str(date_donnee), '%Y-%m-%d')
    return date_donnee