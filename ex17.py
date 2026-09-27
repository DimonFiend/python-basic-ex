'''
    Ex 17 - Write a function that gets an array of strings as parameter and returns a new
            array containing all the values that appear more than once. In your solution
            use only while loops.
'''

#can be done with sets to lower the run time but used nested while for the exercise sake
def find_duplicates(arr: list[str]):
    duplicates = []
    i = 0
    array_len = len(arr) #keeping in memory to not call it every loop iter
    while True:
        if i >= array_len:
            break

        j = i + 1
        while j < array_len:
            if arr[i] == arr[j] and arr[i] not in duplicates:
                duplicates.append(arr[i])
            j += 1
        i += 1

    return duplicates

if __name__ == "__main__":
    test_array = ["abc", "123", "abc", "ok", "shtrudel", "123"]
    print(find_duplicates(test_array))