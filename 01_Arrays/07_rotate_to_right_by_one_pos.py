def rotate_array(arr):
    if len(arr) <= 1: #if o or 1 element then nothing to return 
        return arr

    last = arr[-1]

    for i in range(len(arr)-1, 0, -1): #last to first, and decrese 1 step each time
        arr[i] = arr[i-1]

    arr[0] = last

    return arr 

print(rotate_array([1,2,3,4,5]))