'''678. Valid Parenthesis String'''

def isValid(s):
    p = '()'
    left_p = []
    credits = 0

    # open_b = s.replace('*', '').replace(')','')
    # close_b = s.replace('(', '').replace('*','')
    # stars_b = s.replace('(', '').replace(')', '')
    # print(f"There are '(': {len(open_b)}. There are ')': {len(close_b)}. There are '*': {len(stars_b)}")
    
    credits_to_right = 0
    for l in s:
        if l == p[0]:
            left_p.append(l)
            credits_to_right = 0
        
        elif l == p[1]:
            match = (lambda x: x.pop() if x else None)(left_p)
            if not match:
                if credits == 0:
                    return False
                elif credits > 0:
                    credits -= 1
        
        elif l == '*':
            credits += 1
            credits_to_right +=1
            # if left_p:
            #     left_p.pop()
            # else:
            #     credits.append(l)
   
    credits_to_left = credits - credits_to_right
    if credits_to_left + len(left_p) >= credits_to_right:
        return False
    else:
        return True


if __name__ == '__main__':
    s = [
        "****((((((****", #important case, should return False
        "******)))))))***",
        "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))",
        "(())(()))())((*()()(((()((()*(())*(()**)()(())",
        '()', '*)', '(*', '*', '(*)', '(()', '**))(**', '',
        "**"]

    for el in s:
        print(isValid(el))