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
        # create a node to add
        new_node = Node(value)
        #check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else: 
            # new_node should point to current head
            new_node.next_node = self.head
            # move head to new node
            self.head = new_node
        

    def add_to_tail(self, value):
        # create a node to add
        new_node = Node(value)
        #check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
             # point the node at the current tail, to the new node
             self.tail.next_node = new_node
             self.tail = new_node
        

    # remove the head and return its value
    def remove_head(self):
        # if list is empty do nothing
        if not self.head:
            return None
        # if list only has one element, set head and tail to none
        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None 
            return head_value
        # otherwise we have more elements in the list
        head_value = self.head.value
        self.head = self.head.next_node #this make previous head to point to next_head to make it the new head
        return head_value
        
    # find if values is caontained in the list
    def contains(self, value):
        if self.head is None:
            return False

        # Loop through each node, until we see the value, or we cannot go further
        current_node = self.head

        while current_node is not None:
            # check if this is node we are looking for
            if current_node.value == value:
                return True

            # otherwise, go to the next node
            current_node = current_node.next_node
        return False