"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?

   An array with Queue will have extra memory created even if is not being used due to its Static Memory Allocation at compile time.
   Where a Linked List creates memory at runtime when a new node is inserted.

   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = LinkedList()
    
#     def __len__(self):
#         return self.size
        

#     def enqueue(self, value):

#         self.storage.add_to_tail(value)
#         self.size += 1

#     def dequeue(self):
        
#         if self.storage.length == 0:
#             return None
#         else:
#             self.size -= 1
#             return self.storage.remove_head()
            
        

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):

        return self.size

    def push(self, value):
        self.size += 1
        return self.storage.append(value)

    def pop(self):
        if self.size == 0: return 
        else:
            self.size -= 1
            return self.storage.pop()



class Queue:
    def __init__(self):
        self.size = 0
        self.in_stack = Stack()
        self.out_stack = Stack()

    def __len__(self):
        return self.size

    def enqueue(self,value):

        self.in_stack.push(value)
        self.size += 1

    def dequeue(self):
        if self.size == 0:return

        self.size -= 1
        # if out_stack array is empty:
        # while in_stack is not empty:
        # push to out_stack the element that is on in_stack
        # Out of the while and if statement, return the item stored on out_stack array
        if self.out_stack.size == 0:
            while self.in_stack.__len__() > 0:
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.storage.pop()











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