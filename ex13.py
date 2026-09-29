'''
    Ex 13 - Given two arrays of integers. Add up each element in the same position and
            create a new array containing the sum of each pair.
            Assume both arrays are of the same length.

            For example:
                first_array = [4, 6, 7];
                second_array = [8, 1, 9];
                Function output should be: [12, 7, 16]
'''

def sum_arrays(first_array: list[int,], second_array: list[int,]) -> list[int]:
    summed_arrays : list[int] = []
    for i in range(len(first_array)):
        summed_arrays.append(first_array[i] + second_array[i])

    return summed_arrays

if __name__ == "__main__":
    first_array : list[int] = [4, 6, 7]
    second_array : list[int] = [8, 1, 9]
    print(sum_arrays(first_array, second_array))