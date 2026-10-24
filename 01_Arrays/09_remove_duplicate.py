def remove_duplicate(arr):
    seen = [] #list will store the unique elements
    for i in arr: #i take each value from the input array in order
        if len(seen) == 0 or i != seen[-1]: #check empty or last unique element 
            seen.append(i)

    return seen

print(remove_duplicate([2,2,2,5,5,8,9,9]))
