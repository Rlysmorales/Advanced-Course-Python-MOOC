from datetime import date

date1 = date(2019, 2, 3)
date2 = date(2006, 10, 10)
date3 = date(1993, 5, 9)
dates = [date1, date2, date3]

def list_years(dates: list):
   years_sorted = []
   years_sorted.append(dates[0].year)
   years_sorted.append(dates[1].year)
   years_sorted.append(dates[2].year)
   years_sorted.sort()
   return years_sorted


print(list_years(dates))