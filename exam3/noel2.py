import sys
import calendar
from datetime import datetime
from datetime import timedelta

date_ecrite = sys.argv[1]
print(len(sys.argv[1]))
if len(sys.argv[1]) < 1:
    aujoudhui = datetime.now()
    jour = aujoudhui.day
    mois = aujoudhui.month
    annee = aujoudhui.year
else:
    date = date_ecrite.split('-')
    jour = int(date[2])
    mois = int(date[1])
    annee = int(date[0])

d = datetime (annee, mois, jour)

if jour > 25 and mois > 11:
    jour_noel = datetime (annee + 1, 12, 25)
else:
    jour_noel = datetime (annee, 12, 25)

jour_jusqua_noel = jour_noel - d

print (jour_jusqua_noel.days, "days before christmas\n")

c = calendar.TextCalendar (calendar.MONDAY)
str = c.formatmonth (annee, mois, 1, 0)

if jour > 25 and mois > 11:
    print (str)
    for i in range (1, 13, 1):
        print (c.formatmonth (annee + 1, i, 1, 0))
else:
    for i in range (mois, 13, 1):
        print (c.formatmonth (annee, i, 1, 0))

if __name__ == "__main__":
    print(show_noel(sys.argv))