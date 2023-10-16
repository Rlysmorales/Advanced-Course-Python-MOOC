# Write your solution here
import re

def is_dotw(my_string: str):
    week_days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    for day in week_days:
        if re.search(day, my_string):
            return True
     
    return False

def all_vowels(my_string: str):
  
    if re.search('^[aeyiuo]+$', my_string):
              return True
     
    return False


if __name__=='__main__':
    print(is_dotw("Mon"))
    print(is_dotw("Fri"))
    print(is_dotw("Tui"))
    print(all_vowels("eioueioieoieou"))
    print(all_vowels("autoooo"))