"""Add a couple methods to our LinkedList class,
and use that to implement a Stack.
You have 4 functions below to fill in:
insert_first, delete_first, push, and pop.
Think about this while you're implementing:
why is it easier to add an "insert_first"
function than just use "append"?"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"
        new_node = Element(self,new_element)
        new_node.next = self.head
        self.head = new_node

    def delete_first(self):
        "Delete the first (head) element in the LinkedList as return it"
        res = self.head
        head = head.next
        return res

class stack(object):
    def __init__(self,top=None):
        self.top = top

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        # last_node = Element(self,new_element)
        current = self.top
        if self.top:
            while current.next:
                # next = current
                current = current.next
            current.next = new_element
        else:
            self.top = new_element
        
    def pop(self):
        "Pop (remove) the first element off the next of the stack and return it"
        up = self.top
        while self.up.next.next == None:
            current.next = up.next
        
    