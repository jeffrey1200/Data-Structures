"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):

        return self.size

    def push(self, value):

        self.storage.add_to_head(value)
        self.size += 1
        return

    def pop(self):
        
        if self.size == 0: return 
        else: 
            self.size -= 1
            return self.storage.remove_head() 
              








class Node:
    def __init__(self,value= None,next_node = None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next_node

    def set_next(self,new_next):
        self.next_node = new_next
        





class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_to_head(self,value):
        new_node = Node(value,self.head)
        self.head = new_node
        if self.length == 0:
            self.tail = new_node
        self.length += 1

    def add_to_tail(self,value):
        new_node = Node(value)

        if self.head is None and self.tail is None:
            self.head = new_node
        else:
            self.tail.set_next(new_node)
        self.tail = new_node
        self.length += 1

    def remove_head(self):
        
        if self.head is None:
            return None
        
        elif self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            self.length -= 1
            return value
    
    def remove_tail(self):

        if self.head is None:
            return None
        
        elif self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            value = self.head.get_value()
            self.tail = self.head.get_next()
            self.length -= 1
            return value

    def contains(self,value):

        if self.head is None:
            return None

        current_node = self.head
        desired_number = 0
        while current_node is not None:
            if current_node.get_value() == value:
               desired_number= current_node.get_value()
            current_node = current_node.get_next()
        
        return desired_number

    def get_max(self):

        if self.head is None:
            return None
        
        cur_node = self.head
        curr_max = self.head.get_value()

        while cur_node is not None:
            if cur_node.get_value() > curr_max:
                curr_max = cur_node.get_value()
            cur_node = cur_node.get_next()
        
        return curr_max