class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
    

    def enqueue(self, value):
        new_node = Node(value)
        
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        
        self.length += 1

        return True
    

    def dequeue(self):
        if self.length == 0:
            return None
        
        temp = self.first
        
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = temp.next
            temp.next = None

        self.length -= 1

        return temp



    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next
    

if __name__ == '__main__':
    my_q = Queue(0)
    for i in range(1, 11):
        my_q.enqueue(i)

    my_q.print_queue()
    print('-'*15)

    for _ in range(15):
        popped = my_q.dequeue()
        print(f"Popped value: {(lambda x: x.value if x else 'None')(popped)}")
        print('-'*10)
        my_q.print_queue()

    print('Hello world')