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
        
    
    def prepend(self, value):
        pass
   

    def insert(self, index, value):
        pass  
    
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
    my_ll.append(2)
    my_ll.append(3)
    my_ll.append(3)
    my_ll.print_list()
    print('Hello world!')
