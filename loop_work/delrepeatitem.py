def del_repeated_values(arr):

    i = 0
    x = set(arr)
    myCommons = []
    while i < len(arr):
        if arr[i] in (arr[:i] + arr[i+1:]):
            myCommons.append(arr[i])

        i = i + 1
    return x 

print(del_repeated_values([1,2,3,1,1,5,0,3,8,5]))
