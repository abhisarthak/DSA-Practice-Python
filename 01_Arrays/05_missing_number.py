def missing_number(arr):
    n = len(arr)

    expected_sum = (n*(n+1))/2
    actual_sum = sum(arr)

    missing_number = expected_sum - actual_sum

    return missing_number

print(missing_number([3,1,0]))