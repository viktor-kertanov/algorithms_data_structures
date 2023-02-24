def group_anagrams(input: list) -> list[list]:
    result_anagrams = {}
    for word in input:
        letters = ''.join(sorted(word))
        if letters in result_anagrams:
            result_anagrams[letters].append(word)
        else:
            result_anagrams[letters] = [word]
         

    return [result_anagrams[k] for k in result_anagrams]




print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )



"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

"""