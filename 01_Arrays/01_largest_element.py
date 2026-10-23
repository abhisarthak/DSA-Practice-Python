def find_largest(arr):
    largest = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]


    return largest


print(find_largest([3,7,2,4,5]))
print(find_largest([-4.-9,-7,-5,-2]))