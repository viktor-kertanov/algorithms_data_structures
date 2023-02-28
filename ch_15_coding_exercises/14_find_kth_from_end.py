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
  
  
        
def find_kth_from_end(ll: LinkedList, k: int): 
    current_node = ll.head
    kth_dist = ll.head
    for _ in range(k):
        try:
            kth_dist = kth_dist.next
        except AttributeError:
            print(f"Seems like k is greater than the length of list")
            return None
    
    while kth_dist:
        current_node = current_node.next
        kth_dist = kth_dist.next
    
    return current_node




my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 1
result = find_kth_from_end(my_linked_list, k)

print(result.value)  # Output: 4



"""
    EXPECTED OUTPUT:
    ----------------
    4
    
"""

