'''
    Ex19 - Write a function that gets an array of strings as parameter and returns a new
           array containing all the values from the provided array in the same order but
           without any duplicated values.
           If the string ‘pete’ is a value inside the array your function should skip it and
           not copy it to the new array. In your solution use only while loops.
           For example:
            names = ['Chris', 'Kevin', 'Naveed', 'Pete', 'Victor', ‘Chris’, ‘Kevin’]
            Function output should be:
             ['Chris', 'Kevin', 'Naveed', 'Victor']
'''

def remove_duplicates_skip_pete(arr: list[str]) -> list[str]:
    result : list[str] = []
    i : int = 0
    arr_len : int = len(arr)
    
    while i < arr_len:
        if arr[i].lower() == 'pete':
            i += 1
            continue

        if arr[i] not in result:
            result.append(arr[i])
        i += 1
    return result

if __name__ == "__main__":
    names = ['Chris', 'Kevin', 'Naveed', 'Pete', 'Victor', 'Chris', 'Kevin']
    print(remove_duplicates_skip_pete(names))