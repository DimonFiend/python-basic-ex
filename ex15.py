'''
    Ex 15 - Write a while loop that iterates as long as the counter is less than 100, on
            every iteration the counter is multiplied by 2 starting from 1.
'''

if __name__ == "__main__":
    counter  : int = 1
    while counter < 100:
        print(counter, end=" ")
        counter *= 2