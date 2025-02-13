def sum_list():
    arr = list(map(int,input().split()))
    res = 0
    for i in range(len(arr)):
        res += arr[i]
    # we could also return sum(arr)
    return res
sum_list()
