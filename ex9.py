'''
    Ex 9 -Write a function that prints all the elements of a 2D array using nested for loops.
        matrix = [[1, 2],
                  [3, 4],
                  [5, 6]]

    print_matrix(matrix) → Should print: 1 2 3 4 5 6
'''

def print_matrix(matrix: list[list[int]]) -> None:
    for row in matrix:
        for cols in row:
            print(cols, end=" ")
    print()

if __name__ == "__main__":
    matrix  : list[list[int]] = [[1, 2, 3],
                                 [4, 5, 6],
                                 [7, 8, 9]]
    print_matrix(matrix)