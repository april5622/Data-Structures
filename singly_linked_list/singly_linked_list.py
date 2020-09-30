# a node is linked to another node which makes a list
# a node needs to know the value and what is next

class Node:
    def __init__(self, value =None, next_node=None):
        self.value = value
        self.next_node = next_node


# use this class as a manager of nodes.
# Knows the start and end to keep track of the length
# Node can be deleted and added but this keeps them linked
class LinkedList:
    def __init__(self):
        self.head = None # Stores a node that correspond to first node in list
        self.tail = None # Stores a node that is the end of the list

    def add_to_head(self, value):
        pass
        

    def add_to_tail(self, value):
        pass
        

    # remove the head and return its value
    def remove_head(self):
        pass
        
    # find if values is contained in the list
    def contains(self, value):
        pass

    # find the maximum value in a linked list
    def get_max(self, value):
        pass