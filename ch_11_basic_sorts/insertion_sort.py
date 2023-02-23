from random import sample

def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        while temp < my_list[i-1] and i >= 1:
            my_list[i] = my_list[i-1]
            my_list[i-1] = temp
            i -=1
    
    return my_list



if __name__ == "__main__":
    my_list = [4, 2, 6, 5, 1, 3]

    n = 100
    my_list = sample([i for i in range(1, n+1)], n)
    print('The initial list is:')
    print('-'*10)
    print(my_list)
    print('-'*10) 

    insertion_sort(my_list)
    print(my_list)
    print('Hello world!')