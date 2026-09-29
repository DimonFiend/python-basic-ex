'''
    Ex 10 - Write a function to count how many numbers of zeros appear in a 2D matrix
            using nested for loops and increment operation.
            matrix =[[0,1,1],
                     [0,1,0],
                     [1,0,0]]

            print(zero_count(matrix)) → Should print: 5
'''

def zero_count(matrix: list[list[int]]) -> int:
    zero_counter : int = 0

    for row in matrix:
        for col in row:
            if col == 0:
                zero_counter += 1
    return zero_counter

if __name__ == "__main__":
    matrix : list[list[int]] = [[0, 1, 1],
                               [0, 1, 0],
                               [1, 0, 0]]
    print(zero_count(matrix))