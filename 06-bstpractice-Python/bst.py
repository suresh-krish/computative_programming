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

    
        
    def search(self, find_val):
        # Your code goes here
        current = self.root
        if type(find_val) !=int:
            return False
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

