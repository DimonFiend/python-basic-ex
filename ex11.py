'''
    Ex 11 - Write a function to return an array of all the elements that are repeated more
            than once in a given array.

            arr = [4,2,34,4,1,12,1,4]
            print(find_dup(arr)) Should print: [4, 1]
'''

def find_dup(arr: list[int]) -> list[int]:
    seen = set()
    duplicates = set()

    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)

if __name__ == "__main__":
    arr = [4,2,34,4,1,12,1,4]
    print(find_dup(arr))