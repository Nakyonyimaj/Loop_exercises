def largest_diff(arr):
    differences = []
    for i in arr:
        for j in arr:
            if i > j:
                differences.append(i-j)
    return max(differences)
print(largest_diff([1, 2, 3]))
 