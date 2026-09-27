'''
    Ex4 - Write a for loop that iterates through all numbers from 1 to 45.
    Print the following:
    ● For each number that multiples of 3 print “Fizz”
    ● For each number that multiples of 5 print “Buzz”
    ● For each number that multiples of 3 and 5 print “FizzBuzz”
'''

#Constants for easier code changes
START_NUM = 1
END_NUM = 45

if __name__ == "__main__":
    for num in range(START_NUM, END_NUM + 1):
        if num % 15 == 0: # LCM of 3 and 5 since 3 and 5 are coprime
            print("FizzBuzz", end=", ")
        elif num % 3 == 0:
            print("Fizz", end=", ")
        elif num % 5 == 0:
            print("Buzz", end=", ")
        else:
            print(num, end=", ")