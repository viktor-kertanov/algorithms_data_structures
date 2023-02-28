def merge(ml_1, ml_2):
    combined = []
    i, j = 0, 0

    while i < len(ml_1) and j < len(ml_2):
        if ml_1[i] < ml_2[j]:
            combined.append(ml_1[i])
            i+=1
        else:
            combined.append(ml_2[j])
            j+=1
    
    if i < len(ml_1):
        combined += ml_1[i:]
    
    if j < len(ml_2):
        combined += ml_2[j:]
    
    return combined


def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    
    idx = len(my_list) // 2

    left = merge_sort(my_list[:idx])
    right = merge_sort(my_list[idx:])

    return merge(left, right)


original_list = [3,1,4,2]

sorted_list = merge_sort(original_list)

print('Original List:', original_list)

print('\nSorted List:', sorted_list)



"""
    EXPECTED OUTPUT:
    ----------------
    Original List: [3, 1, 4, 2]
    
    Sorted List: [1, 2, 3, 4]
    
 """





print(merge([1,2,7,8], [3,4,5,6]))



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6, 7, 8]
    
 """