class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()



def is_balanced_parentheses(parentheses):
    stack = Stack()
    for l in parentheses:
        if l == '(':
            stack.push(l)
        if l == ')':
            open = stack.pop()
            if not open:
                return False
    return True

def is_balanced_parentheses(parentheses):
    stack = Stack()
    for p in parentheses:
        if p == '(':
            stack.push(p)
        elif p == ')':
            if not stack.pop():
                return False
    return stack.is_empty()

def is_balanced_parentheses(parentheses):
    stack = Stack()
    for p in parentheses:
        if p == '(':
            stack.push(p)
        elif p == ')':
            if stack.is_empty() or stack.pop() != '(':
                return False
    return stack.is_empty()



balanced_parentheses = '((()))'
unbalanced_parentheses = '((())))'
my_test = ')()()(a(b)r)ac(adab)ra()('

print( is_balanced_parentheses(balanced_parentheses) )
print( is_balanced_parentheses(unbalanced_parentheses) )
print( is_balanced_parentheses(my_test) )



"""
    EXPECTED OUTPUT:
    ----------------
    True
    False

"""

if __name__ == "__main__":
   
    print("Hello world!")