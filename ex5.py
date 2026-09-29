'''
    Ex5 - Write a function that receives an array as a parameter and calculates the sum
          of all the numbers in the given array (don’t use sum() function).
          For example if the given array is: [1,13,22,123,49,34,5,24,57,45]
          The result should be 373

'''

#Sums the nums in the given array without sum function, if list is empty returns None
def sum_array(arr : list[int]) -> int | None:
    total : int = 0

    if not arr:
        return None
    
    for num in arr:
        total += num
    return total

if __name__ == "__main__":
    arr : list[int] = [1,13,22,123,49,34,5,24,57,45] #example list
    print(sum_array(arr))

    # empty case
    # empty_list = []
    # print(sum_array(empty_list))