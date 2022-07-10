def move_zeros_to_end(arr):
    zeros = []
    not_Zeros = []
    for i in arr:
        if i == 0:
            zeros.append(i)
        else:
            not_Zeros.append(i)
    return not_Zeros + zeros
print(move_zeros_to_end([1, 0, 1, 2, 0, 1, 3]))