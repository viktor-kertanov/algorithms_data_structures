def two_sum(nums, target):
    my_dict = {el_idx: el for el_idx, el in enumerate(nums) if el < target}
    for el in my_dict:
        reduced_dict = {i: my_dict[i] for i in my_dict if el!=i}
        for el2 in reduced_dict:
            if my_dict[el] + reduced_dict[el2] == target:
                return [el, el2]
    return []
    

if __name__ == '__main__':
    
    print ( two_sum([2, 7, 11, 15], 9) )
    print ( two_sum([3, 2, 4], 6) )
    print ( two_sum([3, 3], 6) )
    print ( two_sum([1, 2, 3, 4, 5], 10) )
    print ( two_sum([1, 2, 3, 4, 5], 7) )
    print ( two_sum([1, 2, 3, 4, 5], 3) )
    print ( two_sum([], 0) )
