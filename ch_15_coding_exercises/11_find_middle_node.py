class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
        
    # Viktor's solutions
    def find_middle_node_vk(self):
        slow, fast = self.head, self.head
        counter = 1
        while fast.next:
            counter += 1
            fast = fast.next
        
        print(f"There are {counter} nodes in our LL")

        middle = (lambda x: int(x/2)+1 if x % 2 == 0 else x // 2 + 1)(counter)
        print(f"Middle index is: {middle}")
        
        for _ in range(1, middle):
            slow = slow.next
        
        return slow
    
    # Udemy's approach
    def find_middle_node(self):
        slow, fast = self.head, self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow




my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
# my_linked_list.append(6)

print( my_linked_list.find_middle_node().value )



"""
    EXPECTED OUTPUT:
    ----------------
    3
    
"""