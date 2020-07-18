class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def placing(self,root,new_val):
        if root.value > new_val:
            if root.left:
                self.placing(self.root.left,new_val)
            else :
                self.root.left = Node(new_val)
        elif root.value < new_val:
            if root.right:
                self.placing(self.root.right,new_val)
            else :
                self.root.right = Node(new_val)
        

    def insert(self, new_val):
        # Your code goes here
        self.placing(self.root,new_val)

    def printSelf(self):
        if self.root:
            self.traverseInOrder(self.root)
            
    def traverseInOrder(self, node):
        if node.left:
            self.traverseInOrder(node.left)
            return node.value
        if node.right:
            self.traverseInOrder(node.right)

    def searching(self,root,find_val):
        if root.value == find_val:
            return True
        elif root.value < find_val:
            if root.left:
                self.searching(self.root.left,find_val)
            else:
                return False
        elif root.value > find_val:
            if root.right:
                self.searching(self.root.right,find_val)
            else:
                return False



        
    def search(self, find_val):
        # Your code goes here
        if not self.root:
            return False
        elif type(find_val) != int:
            return False
        else :
            self.searching(self.root, find_val)

