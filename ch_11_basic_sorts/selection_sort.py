from random import randint, sample

# Viktor Kertanov's method before looking into instructor's solution
def selection_sort(input_list):
    for i in range(len(input_list)-1):
        min_index = i
        for j in range(i+1, len(input_list)):
            if input_list[min_index] > input_list[j]:
                min_index = j
        if min_index > i:
            temp = input_list[i]
            input_list[i] = input_list[min_index]
            input_list[min_index] = temp    
    
    return input_list


#Instructor's solution to selection sort
def selection_sort(my_list):
    for i in range(len(my_list)-1):
        min_index = i
        for j in range(i+i, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if min_index != i:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp

        


if __name__ == "__main__":
    my_list = [4, 2, 6, 5, 1, 3]

    n = 100
    my_list = sample([i for i in range(1, n+1)], n)
    print('The initial list is:')
    print('-'*10)
    print(my_list)
    print('-'*10) 
    
    selection_sort(my_list)

    print(my_list)