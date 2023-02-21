from random import randint

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True
        
        temp = self.root
        while temp:
            if new_node.value > temp.value:
                if not temp.right:
                    temp.right = new_node
                    return True
                temp = temp.right

            elif new_node.value < temp.value:
                if not temp.left:
                    temp.left = new_node
                    return True
                temp = temp.left
                    
            else: 
                return False
    
    def contains(self, value):
        temp = self.root
        while temp:
            if value == temp.value:
                return True
            elif value > temp.value:
                temp = temp.right
            else:
                temp = temp.left
        return False


if __name__ == '__main__':
    bst = BinarySearchTree()
    for _ in range(10):
        num = randint(1, 100)
        print(f"Our num to insert: {num}")
        bst.insert(num)
    
    for i in range(50):
        contains = bst.contains(i)
        if contains:
            print(f"BST contains: {i}")


    
    print('Hello world')
