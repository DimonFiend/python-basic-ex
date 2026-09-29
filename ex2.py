'''
    Ex2 - Write a for loop that prints the ODD numbers from 7 to 31
'''

#Constants for easier code changes
START_NUM : int = 7
END_NUM : int = 31

if __name__ == "__main__":
    for num in range(START_NUM, END_NUM + 1, 2):
        print(num, end=", ")