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
            self.length = 0
            
            return node_to_return
        
        node_to_return = self.head
        self.head = node_to_return.next
        node_to_return.next = None
        self.length -= 1

        return node_to_return
    

    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        current_node = self.head
        for _ in range(index) :
            current_node = current_node.next
        
        return current_node
    
    def set_value(self, index, value):
        idx_node = self.get(index)
        if idx_node:
            idx_node.value = value
            return True
        return False
    
    def insert_nodex(self, index, value):

        return 

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
    
    # my_ll.print_list()

    # for _ in range(my_ll.length):
    #     print(f"Deleting the last value {my_ll.pop().value}")
    
    # my_ll.print_list()

    my_ll.prepend(321)
    my_ll.prepend(456)
    my_ll.prepend(789)
    my_ll.prepend(1024)
    # my_ll.print_list()

    # print(f"Pop item: {my_ll.pop_first().value}")
    # print(f"Pop item: {my_ll.pop_first().value}")
    # print(f"Pop item: {my_ll.pop_first().value}")

    # my_ll =  LinkedList(99999)
    # my_ll.make_empty()
    print('-'*30)
    my_ll.print_list()
    
    
    # idx_to_get = 0
    # for idx_to_get in range(17):
    #     a = my_ll.get(idx_to_get)
    #     if a:
    #         print(f"Getting idx {idx_to_get} from LL: { a.value}")
    #     else:
    #         print(f'No value to return')
    print('-'*30)
    my_ll.set_value(2, 'dogsog')
    my_ll.print_list()

      print('Hello world!')
