'''
    Ex 8 - student = {'name': 'John', 'age': 20, 'hobbies': ['reading', 'games', 'coding'],}

    1 - Write a function that prints all the student data (each student property
    should be printed in a new line).
    2 - Write a function that receives the student object and a hobby, the function
    should add the hobby to the student's hobbies array if it’s not exist already.
    3 - Use the function that you wrote in ex 1 to print the data of the student and
    check that the new hobby has been added.
    4 - Write a function that receives an object of a student and hobby, the
    function should delete the hobby from the student's hobbies.
    5 - Use the function that you wrote in ex 1 to print the data student and check
    that the hobby has been deleted from the object student.
    6 - Add to the object student new property: family_name and add a value.

'''

def print_student_data(student: dict) -> None:
    for key, value in student.items():
        print(f"{key}: {value}")
    print()

def add_hobby(student: dict, hobby: str) -> None:
    if hobby not in student.setdefault('hobbies', []):
        student['hobbies'].append(hobby)

def delete_hobby(student: dict, hobby: str) -> None:
    if hobby in student.get('hobbies', []):
        student['hobbies'].remove(hobby)

def add_family_name(student: dict, family_name: str) -> None:
    student['family_name'] = family_name

if __name__ == "__main__":
    student = {'name': 'John', 'age': 20, 'hobbies': ['reading', 'games', 'coding']}
    
    print_student_data(student)
    add_hobby(student, 'swimming')
    print("\nAfter adding a new hobby:")
    print_student_data(student)
    delete_hobby(student, 'games')
    print("\nAfter deleting a hobby:")
    print_student_data(student)
    add_family_name(student, 'Doe')
    print("\nAfter adding family name:")
    print_student_data(student)