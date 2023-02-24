# Viktor's solution
def first_non_repeating_char_(my_str):
    str_dict = {char: 0 for char in my_str}
    
    for l in my_str:
        str_dict[l] += 1

    return (lambda x: x[0] if x else None)([l for l in str_dict if str_dict[l]==1])

# Udemy's solution
def first_non_repeating_char(my_str):
    str_dict = {char: 0 for char in my_str}
    
    for l in my_str:
        str_dict[l] += 1
    
    for l in str_dict:
        if str_dict[l] == 1:
            return l
    return None



print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )