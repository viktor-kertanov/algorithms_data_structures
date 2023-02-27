
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
    

    def BFS(self):
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
    

    def dfs_pre_order(self):
        results = []
        
        def traverse(current_node: Node):
            results.append(current_node.value)
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)
        
        traverse(self.root)
        
        return results
    

    def dfs_post_order(self):
        results = []
        def traverse(current_node: Node):
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)
            results.append(current_node.value)
        
        traverse(self.root)
        
        return results
    

    def dfs_in_order(self):
        results = []
        
        def traverse(current_node: Node):
            if current_node.left:
                traverse(current_node.left)    
            results.append(current_node.value)
            if current_node.right:
                traverse(current_node.right)
        
        traverse(self.root)
        
        return results
    

    def _r_contains_helper(self, current_node, value):
        if not current_node:
            return False
        if current_node.value == value:
            return True
        if value > current_node.value:
            return self._r_contains_helper(current_node.right, value)
        if value < current_node.value:
            return self._r_contains_helper(current_node.left, value)
    
    
    def recursive_contains(self, value):
        return self._r_contains_helper(self.root, value)
    

    def recursive_insert(self, value):
        if not self.root:
            self.root = Node(value)
        
        def insert_helper(current_node, value):
            if not current_node:
                return Node(value)
            
            if value > current_node.value:
                current_node.right = insert_helper(current_node.right, value)
            
            if value < current_node.value:
                current_node.left = insert_helper(current_node.left, value)
            
            return current_node
        
        return insert_helper(self.root, value)
    

    def recursive_delete(self, value):

        return None

if __name__ == '__main__':
    tree_vals = [47, 21, 76, 18, 27, 52, 82]
    bst = BinarySearchTree()
    for val in tree_vals:
        bst.recursive_insert(val)
    
    val_to_insert = 88
    print(bst.recursive_insert(val_to_insert))
    print(f"Our tree contains the value 88: {bst.recursive_contains(val_to_insert)}")
    print(bst.BFS())

    # print(tree_vals)
    # a = bst.dfs_in_order()
    # print(a)
    
    print("Hello world!")