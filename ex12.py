'''
    Ex 12 - Write a function using a for loop that gets an array and returns a new array
            with the elements from the given array appearing in reverse order. (Don’t use array reverse() method)
            For example:
                arr = [43, "what", 9, true, "cannot", false, "be", 3, true];
                Function output should be:
                [true, 3, “be”, false, “cannot”, true, 9, “what”, 43]
'''

def reverse_array(arr: list[object]) -> list[object]:
    reversed_arr : list[object] = []
    last_index  : int = len(arr) - 1
    for i in range(last_index, -1, -1):
        reversed_arr.append(arr[i])

    return reversed_arr

if __name__ == "__main__":
    arr : list[object] = [43, "what", 9, True, "cannot", False, "be", 3, True]
    print(reverse_array(arr))