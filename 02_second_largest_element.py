def second_largest(arr):
    largest = float('-inf') #smaller than ordinary number, including negative integers. 
    second = float('-inf')

    for num in arr:
        if num > largest:
            second = largest #previous largest becomes the second largest
            largest = num # current number becomes the largest 

        elif num > second and num != largest: # prevent duplicates 
            second = num

    if second == float('-inf'):
        return -1

    return second

print(second_largest([2,3,6,7,7]))