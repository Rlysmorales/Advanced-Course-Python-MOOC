from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution
def credit_sum_helper(balance_sum, account):
    return balance_sum + account.credits

def sum_of_all_credits(attempts: list):
    return reduce(credit_sum_helper, attempts, 0)


def sum_of_passed_credits(attempts:list):
   return  reduce(lambda x, y: x + y.credits, filter(lambda new_grade : new_grade.grade >= 1, attempts),0)

#>>> reduce(lambda x, y: x + y, numbers)
#    return  sum((map(students_credit(), (filter(lambda new_grade : new_grade.grade >= 1, attempts)))))

# def sum_of_passed_credits(attempts: list):
#     return reduce(lambda t: t.credits, (filter(lambda new_grade : new_grade.grade >= 1, attempts)))

def average(attempts:list):
    return  reduce(lambda x, y: x + y.grade, filter(lambda new_grade : new_grade.grade >= 1, attempts),0)/ len(list(filter(lambda x: x.grade > 0, attempts)))


if __name__ == "__main__":
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    # credit_sum = sum_of_all_credits([s1, s2, s3])
    # print(credit_sum)

    credit_add = sum_of_passed_credits([s1, s2, s3])
    print(credit_add)

    ag = average([s1, s2, s3])
    print(ag)

