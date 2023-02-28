def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        for j in range(i-1, -1, -1):
            if temp < my_list[j]:
                my_list[j+1] = my_list[j]
                my_list[j] = temp
                

    return my_list




print(insertion_sort([4,2,6,5,1,3]))



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
    
 """

