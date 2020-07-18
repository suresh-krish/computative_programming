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
        if self.root.value == find_val:
                return True
        elif self.root.value > find_val and self.root.left != None:
                preorder_search(root.left,find_val)
        elif self.root.value < find_val and self.root.right != None:
                preorder_search(root.right,find_val)
        else:
            return False

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        # Your code goes here
        # while True:
        #     if self.root.value == find_val:
        #         return True
        #     elif self.root.value > find_val and self.root.left != None:
        #         self.root = self.root.left
        #     elif self.root.value < find_val and self.root.right != None:
        #         self.root = self.root.right
        # return False
        return self.preorder_search(self.root,find_val)

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
