class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)


    def preorder_search(self, root, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        # Your code goes here

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        if type(find_val) !=int:
            return False

        current = self.root
        while current != None: 
            # print("--",current.value)
            if current.value == find_val:
                return True
            
            
            # pass right subtree as new tree  
            elif find_val > current.value:  
                current = current.right 
    
            # pass left subtree as new tree 
            elif find_val < current.value: 
                current = current.left  
            else: 
                return True # if the key is found return 1  
        return False

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        # Your code goes here
        pass

    

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        # Your code goes here
        pass
