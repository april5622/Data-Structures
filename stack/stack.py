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
class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node
  
class LinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None 
  
    def add_to_head(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def remove_head(self):
        # List is empty, do nothing
        if not self.head:
            return None 
        # if head is tail, set head and tail to nothing
        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
        # otherwise we have more elements in the list
        head_value = self.head.value
        self.head = self.head.next_node # this make previous head to point to next_head to make it the new head
        return head_value 

    def remove_tail(self):
        # List is empty, do nothing
        if not self.head:
            return None
        # if head is tail, set head and tail to nothing
        if self.head is self.tail:
            tail_value = self.head.value
            self.head = None
            self.tail = None
            return tail_value

        # if the node after head is not the tail, go to the next node of the current node
        current_node = self.head
        while current_node.next_node is not self.tail:
            current_node = current_node.next_node

        # the tail is the current node, return the value
        tail_value = self.tail.value
        self.tail = current_node
        return tail_value

    def contains(self, value):
        if self.head is None:
            return False
        
        current_node = self.head

        while current_node is not None:
            if current_node.value == value:
                return True

            current_node = current_node.next_node
        return False 

    def get_max(self): 
        current_node = self.head
       
        if self.head is None:
            return None
        else:
            max = self.head.value
            while current_node is not None:
                if current_node.value > max:
                    max = current_node.value
                current_node = current_node.next_node
        return max


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.storage.add_to_tail(value) # LAST IN last out

    def pop(self):
        if self.__len__():
            popped = self.storage.remove_tail() # Last in LAST OUT
            self.size -= 1
            return popped

          


# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.append(value)
#         self.size +=1

#     def pop(self):
#       if self.__len__():
#           popped = self.storage.pop()
#           self.size -= 1
#           return popped