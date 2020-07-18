class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)


    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        # Your code goes here
        if self.start.value == find_val:
                return True
        elif self.start.value > find_val and self.start.left != None:
                preorder_search(start.left,find_val)
        elif self.start.value < find_val and self.start.right != None:
                preorder_search(start.right,find_val)
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
        return preorder_search(root,find_val)

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
