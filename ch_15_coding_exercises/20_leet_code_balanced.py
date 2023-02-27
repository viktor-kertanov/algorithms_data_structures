import re 

def isValid(s):
    pattern = '[^(){}\[\]]+'
    to_delete = re.findall(pattern, s) 
    
    for el in to_delete:
        s = s.replace(el, '')

    open_brackets = '([{'
    closed_brackets = ')]}'
    matches= {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    left_p = []
    for l in s:
        if l in open_brackets:
            left_p.append(l)
        elif l in closed_brackets:
            match = (lambda x: x.pop() if x else None)(left_p)
            if not match or matches[l] != match:
                return False
    if left_p:
        return False
    
    return True


if __name__ == '__main__':
    pattern = '[^(){}\[\]]+'
    my_str = "(abra)({[cfd]})(as;dklf{[saldfkj;]}asd;fkj)"
    a = re.findall(pattern, my_str) 
    
    for el in a:
        my_str = my_str.replace(el, '')

    s = ["(abra)({[cfd]})(as;dklf{[saldfkj;]}asd;fkj)", ')', '(){}[]', '(]', "([)]"]

    for el in s:
        print(isValid(el))