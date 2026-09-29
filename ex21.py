'''
    Ex21 -  Write a python program that gets user input (use input() function for this).
            The first input will be the user full name
            Second input will be the user age
            Third input will be the user email
            Write validation for each input provided by the user and allow the user to try
            again in case the user provided invalid input.
            Validation for full name input → string type with 2 words for first name and last
            name.
            Validation for age input → int type between 1 - 130.
            Validation for email input → string type with ‘@’ inside.

'''

def validate_full_name(full_name: str) -> bool:
    return len(full_name.split()) == 2

def validate_age(age: int) -> bool:
    return 1 <= age <= 130

def validate_email(email: str) -> bool:
    return "@" in email and len(email.split("@")) == 2 #regex better here

def get_user_input() -> tuple[str, int, str]:
    while True:
        full_name : str = input("Enter your full name: ")
        if validate_full_name(full_name):
            break
        print("Invalid full name. Please enter your first and last name.")

    while True:
        try: #instead of exception, we can be use .isdigit() here
            age : int = int(input("Enter your age: "))
            if validate_age(age):
                break
            print("Invalid age. Please enter a number between 1 and 130.")
        except ValueError:
            print("Invalid age. Please enter a number between 1 and 130.")

    while True:
        email : str = input("Enter your email: ")
        if validate_email(email):
            break
        print("Invalid email. Please include '@' in your email.")

    return full_name, age, email

if __name__ == "__main__":
    full_name : str ; age : int ; email : str
    full_name, age, email = get_user_input()

    print(f"Full Name: {full_name}")
    print(f"Age: {age}")
    print(f"Email: {email}")