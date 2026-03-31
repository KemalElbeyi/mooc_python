'''def create_tuple(x: int, y: int, z: int):
    max_num = max(x, y, z)
    min_num = min(x, y, z)
    tuple = (min_num, max_num, x+y+z)
    return tuple
print(create_tuple(5, 3, -1))

print("----------------------------------")

def oldest_person(people: list):
    min = 10000
    name = ""
    for tuple in people:
        if min > tuple[1]:
            min = tuple[1]
            name = tuple[0]
    return name
p1 = ("Adam", 1977)
p2 = ("Ellen", 1985)
p3 = ("Mary", 1953)
p4 = ("Ernest", 1997)
people = [p1, p2, p3, p4]

print(oldest_person(people))

print("----------------------------------")

def older_people(people: list,year: int):
    new_list = []
    for val in people:
        if year > val[1]:
            year = val[1]
            new_list.append(val[0])
    return new_list
p1 = ("Adam", 1977)
p2 = ("Ellen", 1985)
p3 = "Mary", 1953
p4 = "Ernest", 1997
#The following two variable assignments are identical in their results
people = [p1, p2, p3, p4]

older = older_people(people, 1979)
print(older)

print("----------------------------------")
'''
def add_student(students: dict,name: str):
    students[name] = []
def print_student(students: dict,name: str):
    if name in students:
        print(name,": ")
        if students[name]:
            print(students[name])

        else:
            print("no completed courses")
    else:
        print(f"{name}: no such person in the database")

def add_course(students: dict,name: str,course_data: tuple):
    course,grade = course_data
    if name in students:
        if grade > 0 and course not in students[name]:
            students[name].append(course_data)


students = {}
add_student(students, "Peter")
add_course(students, "Peter", ("Introduction to Programming", 3))
add_course(students, "Peter", ("Advanced Course in Programming", 2))
add_course(students, "Peter", ("Data Structures and Algorithms", 0))
add_course(students, "Peter", ("Introduction to Programming", 2))
print_student(students, "Peter")

'''total_grade = 0
            lesson = []
            course_num = 0

            for course,grade in students[name]:
                if grade == 0:
                    continue
                if course not in lesson:
                    lesson.append(course)
                    course_num += 1
                    total_grade += grade
            print(f"{course_num} completed courses:")
            for course,grade in students[name]:
                if course in lesson:
                    print(f"  {course} {grade}")
            if course_num > 0:
                print(f" avarage grade: {total_grade/course_num}")'''


