class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"


def accepted(attempts: list):
    return list(filter(lambda new_grade : new_grade.grade >= 1, attempts))

def attempts_with_grade(attempts: list, grade: int):
    return list(filter(lambda new_grade : new_grade.grade == grade, attempts))

# def names_of_students(attempts: list):
#     return map(lambda t: t.student_name, attempts)

def students_names():
    return lambda t: t.student_name

def passed_students(attempts: list, course: str):
   return  sorted(list(map(students_names(), (filter(lambda new_grade : (new_grade.grade >= 1) and (course == new_grade.course_name), attempts)))))

# sorted(list(filter(map(lambda t: t.course_name, attempts))))
#>>> list(map(square, filter(is_odd, numbers)))

#    for att in attempts:
#        if att.grade >= 1 and course == att.course_name:
#            print(att.student_name)


if __name__ == "__main__":
    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Olivia C. Objective", "Introduction to AI", 5)
    s3 = CourseAttempt("Peter Python", "Introduction to AI", 0)
    s4 = CourseAttempt("Jack Java", "Introduction to AI", 3)

    # for attempt in accepted([s1, s2, s3]):
    #     print(attempt)
    # print()

    # for attempt in attempts_with_grade([s1, s2, s3, s4], 3):
    #     print(attempt)

    for attempt in passed_students([s1, s2, s3, s4], "Introduction to AI"):
        print(attempt)

    # passed_students([s1, s2, s3, s4], "Introduction to AI")