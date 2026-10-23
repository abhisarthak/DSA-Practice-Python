def zeros_end(arr):
    pos = 0 #marks where the next non-zero number belongs

    for i in range(len(arr)):
        if arr[i] != 0: #whenever we find a non zero element
            arr[pos] = arr[i] #we write it at the next available position
            pos += 1 #and after writing just advance the pos


    while pos < len(arr): 
        arr[pos] = 0 #other remaining position will be filled by zero 
        pos += 1

    return arr


print(zeros_end([2,0,5,0,4,0,6]))