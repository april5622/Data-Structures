"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        # If list is empty
        if self.head is None and self.tail is None: # Creating a new_node
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else: # with new_node, create the arrows to point
            # IF there is a new node
            # Param is value, No prev, self.head
            new_node = ListNode(value, None, self.head)
            new_node.insert_before(self.head) #use insert_before to add new_node before the head
            self.head = new_node
            self.length += 1
            

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        head_value = self.head.value
        self.delete(self.head)
        return head_value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        # check if list is empty
        if self.head is None and self.tail is None:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else: 
            current_tail = self.tail
            # Node after tail will have a new node
            # Param is value, self.tail, no next
            current_tail.next = ListNode(value, self.tail, None)
            # New node after tail will be new tail
            self.tail = current_tail.next
            # length is increased by 1
            self.length += 1


    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        tail_value = self.tail.value
        self.delete(self.tail)
        return tail_value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        # node is deleted from current spot
        old_node = self.delete(node)
        # then it is moved to the head since its the front
        self.add_to_head(old_node)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        # node is deleted from current spot
        old_node = self.delete(node)
        # then it is moved to the tail since its the end
        self.add_to_tail(old_node)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        # IF the node is HEAD
        if node is self.head:
            if node.next is not None:
                # current head is a node
                current_head = node
                # head will be the node next to it
                self.head = current_head.next
                # The old head is be disconnected
                self.head.prev = None
                # length will be deleted by 1
                self.length -= 1
            else:
                # If there is no head and tail, length is 0
                self.head = None
                self.tail = None 
                self.length = 0
        # IF node is TAIL
        elif node is self.tail:
            if node.prev is not None:
                # current tail is node
               current_tail = node
               # tail will be the node previous of it
               self.tail = current_tail.prev
               # the node (old tail) next to the new tail will be disconnected
               self.tail.next = None
               # length will be deleted by 1
               self.length -= 1
            else:
                 # If there is no head and tail, length is 0
                self.tail = None
                self.head = None
                self.length = 0

        else:
            # node located anywhere else, will be deleted
            node.delete()
             # length is 0
            self.length -= 1
        return node.value


        
    """Returns the highest value currently in the list"""
    def get_max(self):
        # same as singly linked list
        current_node = self.head
       
        if self.head is None:
            return None
        else:
            max = self.head.value
            while current_node is not None:
                if current_node.value > max:
                    max = current_node.value
                current_node = current_node.next
        return max
