def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


def pivot(my_list, pivot_idx, end_idx):
    
    swap_idx = pivot_idx

    for i in range(pivot_idx+1, end_idx+1):
        if my_list[i] < my_list[pivot_idx]:
            swap_idx += 1
            swap(my_list, swap_idx, i)
    
    swap(my_list, pivot_idx, swap_idx)

    return swap_idx


def quick_sort_helper(my_list, left, right):
    if left < right:
        pivot_idx = pivot(my_list, left, right)
        left = quick_sort_helper(my_list, left, pivot_idx-1)
        right = quick_sort_helper(my_list, pivot_idx+1, right)

    return my_list


def quick_sort(my_list):
    quick_sort_helper(my_list, 0, len(my_list)-1)


my_list = [4,6,1,7,3,2,5]

quick_sort(my_list)

print(my_list)



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6, 7]
    
 """




my_list = [4,6,1,7,3,2,5]

print('List before running pivot():')
print(my_list)

returned_pivot_index = pivot(my_list, 0, 6)

print('\nList after running pivot():')
print(my_list)

print('\nReturned Swap Index:')
print(returned_pivot_index)



"""
    EXPECTED OUTPUT:
    ----------------
    List before running pivot():
    [4, 6, 1, 7, 3, 2, 5]

    List after running pivot():
    [2, 1, 3, 4, 6, 7, 5]

    Returned Swap Index:
    3

 """