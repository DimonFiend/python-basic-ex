'''
    Ex20 - Use a while loop to iterate on a boolean array.
           As long as the next index is different from the previous index the iteration
           continues, otherwise, return the index of the element with the same value.
           If there are not two successive values, the function will return -1.
            For example:
                array= [true, false, false, true, true, false] → return 2
                array= [true, false, true, false, true, true]; → returns 5
                array= [true, false, true, false, true, false]; → returns -1

'''

def check_successive_boolean(arr: list[bool]) -> int:
    i : int = 1
    arr_len : int = len(arr)
    
    while i < arr_len:
        if arr[i] == arr[i - 1]:
            return i
        i += 1
    return -1

if __name__ == "__main__":
    array = [True, False, False, True, True, False]
    print(check_successive_boolean(array))

    array = [True, False, True, False, True, True]
    print(check_successive_boolean(array))

    array = [True, False, True, False, True, False]
    print(check_successive_boolean(array))