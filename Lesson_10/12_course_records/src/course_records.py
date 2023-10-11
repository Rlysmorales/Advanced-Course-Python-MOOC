class Person:
    def __init__(self, course: str, grade: int, credits: int):
        self.__course = course
        self.__grade = grade
        self.__credits = credits

    def course(self):
        return self.__course 
    
    def credits(self):
        return self.__credits
    
    def grade(self):
        return self.__grade
      

class CourseRecords(Person):
    def __init__(self):
        self.__record = {}

    def add_course(self, course: str, grade: int, credits: int):

        if course not in self.__record:
            self.__record[course] = Person(course, grade, credits)

    def get_credit(self, course: str):
        total_credits = 0

        credits = self.all_entries()

        for course, grade, credits in credits.items():
            if course in credits:
                total_credits += credits
                print(total_credits)


    def get_grade(self, course: str):
        credits = self.all_entries()

        for course, grade, credits in credits.items():
            if course in credits:
                print(grade)

    def get_course_data(self, course: str):

        if course not in self.__record:
            return None
        return self.__record[course]

    def all_entries(self):
        return self.__record


class CourseRecordsApplication:
    def __init__(self):
        self.__course_record = CourseRecords()

    def user_choice(self):
        print("Commands: ")
        print("0 Exit")
        print("1 add course")
        print("2 get course data")

    def add_course(self):
        course = input("course: ")
        grade = input(int("grade: "))
        credit = input(int("credits: "))
       
        self.__course_record.add_course(course, grade, credit)

    def get_course_data(self):
        course_name = input('course: ')
        print("IAM HERE WHAT")
        course = self.__course_record.get_course_data(course_name)
        if course == None:
            print("unknown")
        else:
            print("IAM HERE")
            print(course)

    def execute(self):
        self.user_choice()
        while True:
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                 self.get_course_data()
                 break
            else:
                self.user_choice()

def main():
    # when testing, no code should be outside application except the following:
    application = CourseRecordsApplication()
    application.execute()

if __name__ == "__main__":
    main()