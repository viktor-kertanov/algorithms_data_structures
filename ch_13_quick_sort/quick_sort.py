from random import sample

def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp
    
    return my_list



def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index+1, end_index+1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    
    swap(my_list, pivot_index, swap_index) 
    
    return swap_index


def quick_sort_helper(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index-1)
        quick_sort_helper(my_list, pivot_index+1, right)

    return my_list

def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list)-1)
    
if __name__ == '__main__':
    my_list = [4, 1, 6, 7, 3, 2, 5]
    n = 100
    my_list = sample([i for i in range(1, n+1)], n)
    print('The initial list is:')
    print('-'*10)
    print(my_list)
    print('-'*10) 

    print(quick_sort(my_list))
    print('Hello world')