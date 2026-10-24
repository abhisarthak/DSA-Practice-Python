def sorted_array(arr):

    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return False

    return True

print(sorted_array([1,2,3,5,6]))