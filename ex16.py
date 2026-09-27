'''
    Ex 16 - Write a while loop that iterates as long as the counter is greater than 50 , on every iteration the counter is divided by 2.
            The counter should start with the value 900000 before the first iteration.
'''
if __name__ == "__main__":
    counter = 900000
    while counter > 50:
        print(counter, end=" ")
        counter /= 2
