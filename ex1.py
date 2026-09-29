'''
    Ex1 - Write a for loop that prints the numbers from 12 to 24.
'''

#Constants for easier code changes
START_NUM : int = 12
END_NUM : int = 24

if __name__ == "__main__":
    for num in range(START_NUM, END_NUM + 1):
        print(num, end=", ")