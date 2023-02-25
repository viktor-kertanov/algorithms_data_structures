def find_pairs(arr1, arr2, target):
    pairs = []
    for num1 in set(arr1):
        for num2 in set(arr2):
            if num1 + num2 == target:
                pairs.append((num1, num2))
    return pairs

arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)



"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""