def longest_consecutive_sequence(nums):
    sorted_uniques = sorted(set(nums))

    sequences_len, sequences = [], []
    
    for el in sorted_uniques:
        cur_sequence =[el] 
        while el+1 in sorted_uniques and el+1 not in cur_sequence:
            cur_sequence.append(el+1)
            sorted_uniques.remove(el+1)
            el +=1
        
        sequences_len.append(len(cur_sequence))
        sequences.append(cur_sequence)
    
    print(sequences)
    
    return max(sequences_len)

print( longest_consecutive_sequence([100, 101, 101, 102, 102, 103, 104, 105, 106, 4, 4, 200, 201, 200, 1, 3, 2]) )



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""