'''This sections is devoted to the doubly-linked lists (DLL)'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    

    def append(self, value):
        new_node = Node(value)

        if self.length == 0 or not self.tail:
            self.head = new_node
            self.tail = new_node
        
        else:
            temp = self.tail
            self.tail = new_node
            new_node.prev = temp
            temp.next = new_node
        
        self.length += 1

        return True
    

    def pop(self):
        if self.length == 0:
            return None
        
        if self.length ==1:
            temp = self.tail
            self.head = None
            self.tail = None
            self.length = 0
            return temp

        temp = self.tail
        self.tail = temp.prev
        self.tail.next = None
        temp.prev = None
        self.length -= 1

        return temp
    

    def prepend(self, value):
        new_node = Node(value)
        
        if self.length == 0:
            self.append(value)
            return True
        
        temp = self.head
        temp.prev = new_node
        self.head = new_node
        self.head.next = temp

        self.length +=1

        return True


    def pop_first(self):
        if self.length == 0:
            return None
        
        if self.length == 1:
            return self.pop()
            
        temp = self.head
        self.head = temp.next
        self.head.prev = None
        temp.next = None
        self.length -=1

        return temp
    

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        
        if index == 0:
            return self.prepend(value)
        
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)

        before = self.get(index-1)
        after = before.next
        before.next = new_node
        new_node.prev = before
        after.prev = new_node
        new_node.next = after
        self.length += 1

        return True
    

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        
        node_by_idx = self.get(index)
        before = node_by_idx.prev
        after = node_by_idx.next
        before.next = after
        after.prev = before
        node_by_idx.prev = None
        node_by_idx.next = None
        self.length -= 1

        return node_by_idx


    def get(self, index):
        if index < 0 or index >=self.length:
            return None
        if index < self.length/2:
            cur_node = self.head
            cur_idx = 0
            num_opertaions = 1
            while cur_idx < index:
                cur_node = cur_node.next
                cur_idx += 1
                num_opertaions += 1
        else:
            cur_node = self.tail
            cur_idx = self.length - 1
            num_opertaions = 1
            while cur_idx > index:
                cur_node = cur_node.prev
                cur_idx -= 1
                num_opertaions += 1

        return cur_node
    

    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            return False

        node_by_idx = self.get(index)
        node_by_idx.value = value

        return True
    

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

        return True

    def print_dll(self):
        if self.length == 0:
            return False

        temp = self.head
        print(temp.value)

        while temp.next:
            print(temp.next.value)
            temp = temp.next




if __name__ == '__main__':

    def test_append():
        dll = DoublyLinkedList(11)
        dll.append(22)
        dll.append(33)
        dll.append(44)
        
        dll.print_dll()
        
        print('-'*15)
        dll.make_empty()
        dll.append(88)
        dll.print_dll()

  
    def test_pop():
        dll = DoublyLinkedList(1)
        for i in range(2, 4):
            dll.append(i)
        
        print(f"Current dll length: {dll.length}")
        dll.print_dll()
        print('-'*20)

        for _ in range(3):
            last_item = dll.pop()
            print(f"Last item value popped: {last_item.value}. Prev: {last_item.prev}. Next: {last_item.next}")
            print('-'*20)
            print(f"Current dll length: {dll.length}")
            dll.print_dll()

    
    def test_prepend():
        dll = DoublyLinkedList(11)
        for i in range(22, 99, 11):
            dll.append(i)
        
        dll.make_empty()
        dll.print_dll()
        print(f'Current length: {dll.length}')

        print(f'-'*15)
        print(f'Now lets make a prepend operation')

        dll.prepend(777)
        dll.prepend(888)
        dll.prepend(999)
        dll.print_dll()
        print(f'Current length: {dll.length}')

        pass


    def test_pop_first():
        dll = DoublyLinkedList(1)
        for i in range(2, 11):
            dll.append(i)
        
        dll.print_dll()
        print(f"Current dll length is {dll.length}")

        for _ in range(13):
            print('-'*15)

            first_item = dll.pop_first()
            if first_item:
                print(f"The value of the first item is: {first_item.value}")
            else:
                print(f"dll is empty, no first item")
            dll.print_dll()
            print(f"Current dll length is {dll.length}")


    def test_get():
        dll = DoublyLinkedList(0)
        for i in range(1, 101):
            dll.append(i)
        
        dll.print_dll()

        for idx in range(101):
            node_by_idx, num_operations = dll.get(idx)
            print(f"Node by idx {idx}: {node_by_idx.value}. Nummber of operations: {num_operations}")
    

    def test_insert():
        dll = DoublyLinkedList(0)
        for i in range(1, 11):
            dll.append(i)
        dll.print_dll()

        value_to_insert = 777
        idx_to_insert = [-1, dll.length, 0, dll.length - 1, 1, 5, 9]
        idx_to_insert = [9]

        for idx in idx_to_insert:
            dll.insert(idx, value_to_insert)
            print(f"We've inserted into idx {idx} value {value_to_insert}")
            dll.print_dll()

    
    def test_remove():
        idxs = [-2, -1, 0, 1, 5, 11, 10]
        for idx in idxs:
            dll = DoublyLinkedList(0)
            for i in range(1, 11):
                dll.append(i)
            # dll.print_dll()

            removed_node = dll.remove(idx)
            print('-'*15)
            print(f"We've removed idx #{idx}. Length: {dll.length}. Removed value: {(lambda x: x.value if x else 'None')(removed_node)}")
            dll.print_dll()
            print('-'*15)

    
    def test_set_value():
        dll = DoublyLinkedList(0)
        for i in range(1, 11):
            dll.append(i)
        # dll.print_dll()

        for idx in range(11):
            cur_value = dll.get(idx).value
            dll.set_value(idx, 1 + 2*cur_value)
        
        dll.print_dll()

    test_set_value()
   

    print("Hello world!")