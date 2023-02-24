def merge(list1, list2):
    combined = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i+=1
        else:
            combined.append(list2[j])
            j+=1
    
    if i < len(list1):
        combined += list1[i:]  
    else:
        combined += list2[j:]

    return combined


def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    
    mid_index = int(len(my_list) / 2)
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])

    return merge(left, right)

if __name__ == '__main__':
    # list1 = [1, 3, 4, 5, 9, 10, 11, 12]
    # list2 = [2, 6, 7, 8, 13, 14]

    my_list = [4, 2, 6, 5, 1, 3]

    a = merge_sort(my_list)

    print('Hello world!')