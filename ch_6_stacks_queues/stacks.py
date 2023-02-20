'''Work-through of stacks. This is LIFO method and lists / linked-lists is a popular way to implement queues.'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
    

    def push(self, value):
        new_node = Node(value)
        if self.height == 0 or not self.top:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        
        self.height += 1
        
        return True
    
    def pop(self):
        if self.height == 0 or not self.top:
            return None
        
        temp = self.top
        self.top = temp.next
        temp.next = None
        self.height -= 1

        return temp

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next


if __name__ == '__main__':

    my_stack = Stack(0)
    for i in range(1, 11):
        my_stack.push(i)

    my_stack.print_stack()
    print(f"The height of our stack is: {my_stack.height}")
    print('-'*10)

    popped_node = my_stack.pop()
    print(f"Popped value: {popped_node.value}")
    print(f"The height of our stack is: {my_stack.height}")
    print('-'*10)
    my_stack.print_stack()

    print('Hello world')