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
        if self.length == 0 or not self.head:
            return None
            
        temp = self.head
        
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            while temp.next:
                prev = temp
                temp = temp.next
            self.tail = prev
            self.tail.next = None
        
        self.length -= 1
        
        return temp
    

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
    

    def insert_node(self, index, value):

        if index < 0 or index > self.length:
            return None
        
        if index == self.length:
            return self.append(value)
        
        if index == 0:
            return self.prepend(value)

        new_node = Node(value) 
        temp = self.get(index-1)
        
        new_node.next = temp
        temp.next = new_node

        self.length +=1

        return True
    

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        
        if index == 0:
            return self.pop_first()
        
        if index == self.length-1:
            return self.pop()
        
        prev = self.get(index-1)
        temp = prev.next
        
        prev.next = temp.next
        temp.next = None

        self.length -= 1  

        return temp

    def reverse(self):
        if self.length == 0:
            return None
        
        temp = self.head
        new_ll = LinkedList(temp.value)
        
        while temp.next:
            new_ll.prepend(temp.next.value)
            temp = temp.next

        self = new_ll
    
    def reverse_2(self):
        if self.length == 0:
            return None
        
        temp = self.head
        self.head = self.tail
        self.tail = temp

        before = None
        
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


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
    my_ll.make_empty()
    for i in range(15):
        my_ll.append(i)

    print('-'*30)
    my_ll.print_list()
    print(f"Length: {my_ll.length}")
    
    my_ll.reverse()
    print('-'*30)
    my_ll.print_list()
    # print(f"Length: {reversed_ll.length}")

    print('Hello world')

    # my_ll.remove(9)
    # print('-'*30)
    # my_ll.print_list()
    # print(f"Length: {my_ll.length}")
    
    
    # my_ll.insert_node(8, 77)
    # print('-'*30)
    # my_ll.print_list()
    # print(f"Length: {my_ll.length}")










    # my_ll.append(888)
    # my_ll.append(999)
    
    # my_ll.print_list()

    # for _ in range(my_ll.length):
    #     print(f"Deleting the last value {my_ll.pop().value}")
    
    # my_ll.print_list()

    # my_ll.prepend(321)
    # my_ll.prepend(456)
    # my_ll.prepend(789)
    # my_ll.prepend(1024)
    # my_ll.print_list()

    # print(f"Pop item: {my_ll.pop_first().value}")
    # print(f"Pop item: {my_ll.pop_first().value}")
    # print(f"Pop item: {my_ll.pop_first().value}")

    # my_ll =  LinkedList(99999)
    # my_ll.make_empty()
   
    
    
    # idx_to_get = 0
    # for idx_to_get in range(17):
    #     a = my_ll.get(idx_to_get)
    #     if a:
    #         print(f"Getting idx {idx_to_get} from LL: { a.value}")
    #     else:
    #         print(f'No value to return')
    # print('-'*30)
    # my_ll.set_value(2, 'dogsog')
    # my_ll.print_list()

    print('Hello world!')
