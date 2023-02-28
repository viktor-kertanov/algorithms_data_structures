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
    
    def bfs(self):
        current_node = self.root
        queue = [current_node]
        
        results = []
        while queue:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
            
        return results
    
    def dfs_in_order(self):
        results = []
        
        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            
            results.append(current_node.value)

            if current_node.right:
                traverse(current_node.right)

            return results
        
        return traverse(self.root)
    

    def dfs_pre_order(self):
        results = []
        
        def traverse(current_node):
            
            results.append(current_node.value)
            
            if current_node.left:
                traverse(current_node.left)
            
            if current_node.right:
                traverse(current_node.right)

            return results
        
        return traverse(self.root)
    

    def dfs_post_order(self):
        results = []
        
        def traverse(current_node):
            
            if current_node.left:
                traverse(current_node.left)
            
            if current_node.right:
                traverse(current_node.right)
            
            results.append(current_node.value)

            return results
        
        return traverse(self.root)
    
if __name__ == '__main__':
    tree_vals = [47, 21, 76, 18, 27, 52, 82]
    bst = BinarySearchTree()
    for val in tree_vals:
        bst.insert(val)
    print(bst.dfs_post_order())

    print('Hello world')