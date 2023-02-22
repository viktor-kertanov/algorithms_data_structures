from random import randint, sample

# Viktor Kertanov's method for bubble sort (without looking to answers)
def bubble_sort_custom(input_list):
    cycles = 1
    cycles_dict = {}
    while True:
        operations = 0
        for idx in range(len(input_list)-1):
            if input_list[idx] > input_list[idx+1] :
                temp = input_list[idx+1]
                input_list[idx+1] = input_list[idx]
                input_list[idx] = temp
                operations += 1
        
        cycles_dict[cycles] = operations
        cycles += 1
        
        if operations == 0:
            print(f"Cycles data [# cycle, num of operations]: {cycles_dict}. Total operations: {sum([cycles_dict[k] for k in cycles_dict])}")
            return input_list


# Scott Barret's (Instructor on the cours) method for bubble sort
def bubble_sort(input_list):
    for i in range(len(input_list)-1, 0, -1):
        for j in range(i):
            if input_list[j] > input_list[j+1]:
                temp = input_list[j]
                input_list[j] = input_list[j+1]
                input_list[j+1] = temp
    
    return input_list
        
if __name__ == "__main__":
    my_list = [4, 2, 6, 5, 1, 3]
    n = 100
    my_list = sample([i for i in range(1, n+1)], n)
    print('The initial list is:')
    print('-'*10)
    print(my_list)
    print('-'*10) 


    bubble_sort(my_list)
    print(my_list)
    print("Hello world!")