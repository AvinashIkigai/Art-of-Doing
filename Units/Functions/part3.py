def calc_age(age, interval=0):
    """Determine a person's age after interval years."""
    age += interval
    return age

def course_info(course_name,student_number,credit_hour):
    course = {
        'Course Name':course_name.title(),
        'Student Number':student_number,
        'Credit Hours':credit_hour,
    }
    return course

def drop_student(course):
    course['Student Number'] -= 1
    print("Dropping student from " + course['Course Name'] + ".")


new_age = calc_age(33,10)
print(new_age)

new_age = calc_age(33,67)
print(new_age)

python = course_info("Python programming",32,4)
for key,value in python.items():
    print(key + ":" + str(value))

drop_student(python)
for key,value in python.items():
    print(key + ":" + str(value))