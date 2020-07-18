class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def placing(self,root,new_val):
        if self.root.value > new_val:
            if self.root.left != None:
                placing(self.root.left,new_val)
            else :
                self.root.left = new_val
        elif self.root.value < new_val:
            if self.root.right != None:
                placing(self.root.right,new_val)
            else :
                self.root.right = new_val
        

    def insert(self, new_val):
        # Your code goes here
        if not self.root:
            self.root = new_val
        else:
           self.placing(self.root,new_val)

    def printSelf(self):
        # Your code goes here
        pass

    def searching(self,root,new_val):
        if self.root.value == new_val:
            return True
        elif self.root.value > new_val:
            if self.root.left != None:
                searching(self.root.left,new_val)
            else:
                return False
        elif self.root.value < new_val:
            if self.root.right != None:
                searching(self.root.right,new_val)
            else:
                return False



        
    def search(self, find_val):
        # Your code goes here
        if not self.root:
            return None
        else :
            self.searching(self.root, find_val)

