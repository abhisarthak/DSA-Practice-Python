def two_sum(arr, target):
    seen = {} #store already visited numbers and their indices 

    for i in range(len(arr)):
        needed = target - arr[i]

        if needed in seen:
            return [seen[needed], i]

        seen[arr[i]] = i #if no pair found yet, save the current number and its index for future checks

    return [] #return empty list if no pair exists.

print(two_sum([2,7,11,15],9)) #[0,1]