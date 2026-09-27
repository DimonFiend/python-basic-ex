'''
    Ex3 - Write a for loop that prints the EVEN numbers from 10 to -20.
'''

#Constants for easier code changes
START_NUM = 10
END_NUM = -20

if __name__ == "__main__":
    for num in range(START_NUM, END_NUM - 1, -2):
        print(num, end=", ")