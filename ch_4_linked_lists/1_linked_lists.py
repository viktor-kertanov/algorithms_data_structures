class Node:
    def __init__(self, value):
        self.value = value
        self.next = None  
 

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node 
        self.length = 1 
    

    def append(self, value):
        new_node = Node(value)
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        
        return True
        

    def pop(self):
        if not self.head:   
            return None
        
        elif self.length == 1:
            node_to_return = self.head

            self.head = None  
            self.tail = None
            self.length = 0
            
            return node_to_return
        
        else:
            current = self.head
            while current.next:
                previous = current
                current = current.next
            
            node_to_return = previous.next
            
            self.tail = previous  
            self.tail.next = None
            self.length -= 1
        
        return node_to_return
    

    def prepend(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1

        return True
    

    def pop_first(self):
        if not self.head.next and not self.tail.next:
            return None
        
        if self.length == 1:
            node_to_return = self.head
            self.head = None
            self.tail = None
            self.length = 1
            
            return node_to_return
        
        node_to_return = self.head
        self.head = node_to_return.next
        self.length -= 1

        return node_to_return

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
     
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
    

if __name__ == '__main__':
    my_ll = LinkedList(1)
    for i in range(7):
        my_ll.append(i)
    my_ll.append(888)
    my_ll.append(999)
    my_ll.print_list()
    print(f"\nLinked list has {my_ll.length} elements")
    
    last_el = my_ll.pop()
    print(f"\nThe last value in the linked list before pop operation was: {last_el.value}")
    print('--'*30)
    print(f"\nThe new list has {my_ll.length} elements")
    
    my_ll.print_list()

    for _ in range(my_ll.length):
        print(f"Deleting the last value {my_ll.pop().value}")
    
    my_ll.print_list()

    my_ll.prepend(321)
    my_ll.prepend(456)
    my_ll.prepend(789)
    my_ll.prepend(1024)
    my_ll.print_list()

    print(f"Pop item: {my_ll.pop_first().value}")
    print(f"Pop item: {my_ll.pop_first().value}")
    print(f"Pop item: {my_ll.pop_first().value}")

    my_ll.print_list()

    print('Hello world!')
