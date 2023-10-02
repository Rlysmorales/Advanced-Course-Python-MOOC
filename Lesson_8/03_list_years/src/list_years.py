# Write your solution here
# Remember the import statement
# from datetime import date
from datetime import date
def main():

    date1 = date(2019, 2, 3)
    date2 = date(2006, 10, 10)
    date3 = date(1993, 5, 9)
    dates = [date1, date2, date3]
    list_years(dates)


def list_years(dates: list):
    years_sorted = []
    for the_year in dates:
        years_sorted.append(the_year.year)
        print("years list", years_sorted)
        years_sorted.sort()
    
    return years_sorted

if __name__ == "__main__":
    main()