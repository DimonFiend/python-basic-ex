'''
    Ex6 - Write a function that receives an array of objects.
          Each object should represent a student with the properties:
            ● id
            ● first name
            ● last name
            ● age
            ● country
            ● city

        In addition, the function should receive a property to change.
        1 - The function should check for each property in each object in the array if
            the given property exists and if it does, the function should delete it from the
            object.
        2 - Write a function that prints each property of each object in the given array.
        3 - Write a function that sorts the array by the students age from the oldest to
            the youngest and return the sorted array.

'''

def delete_if_exists_prop(arr: list[dict], prop: str) -> None:
    for obj in arr:
        obj.pop(prop, None) #Not raises an error if key not found and not requiring an if statement

def print_all_props(arr: list[dict]) -> None:
    for i, obj in enumerate(arr):
        print(f"Object {i + 1}:")
        for key, value in obj.items():
            print(f"{key} : {value}", end=", ")
        print()

def sort_by_age_desc(arr: list[dict]) -> list[dict]:
    #x.get returns the value or an default -1 if value doesn't exist which will place it last in the array
    return sorted(arr, key=lambda x: x.get("age", -1), reverse=True) 

if __name__ == "__main__":
    students = [
        {"id": 1, "first name": "John", "last name": "Doe", "age": 20, "country": "USA", "city": "New York"},
        {"id": 2, "first name": "Jane", "last name": "Smith", "age": 22, "country": "Canada", "city": "Toronto"},
        {"id": 3, "first name": "Alice", "last name": "Johnson", "age": 19, "country": "UK", "city": "London"},
        {"id": 4, "first name": "Bob", "last name": "Brown", "country": "Australia", "city": "Sydney"},
    ]
    
    # Example usage
    print("Original students:")
    print_all_props(students)

    delete_if_exists_prop(students, "city")
    print("\nAfter deleting 'city' property:")
    print_all_props(students)

    sorted_students = sort_by_age_desc(students)
    print("\nStudents sorted by age (descending):")
    print_all_props(sorted_students)