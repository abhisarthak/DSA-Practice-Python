def max_consecutive_same(arr):
    if len(arr) == 0:
        return 0

    count = 1
    maximum = 1
    repeating_num = arr[0]

    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            count += 1

        else:
            count = 1

        if count > maximum:
            maximum = count
            repeating_num = arr[i]


    return maximum, repeating_num #[Maximum occurence, Which nummber]

print(max_consecutive_same([2,2,3,4,4,4,5,6,7]))