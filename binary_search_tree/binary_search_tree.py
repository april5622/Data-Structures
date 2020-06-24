"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # take the current value of our node (self.value)
        # compare to the new value we want to insert
        if value == self.value:
            return False
          # if new value < self.value
          # IF, self.left is already taken by a node,
            # make that left node, call insert
          # set the left to the new node with the new value
        elif value < self.value:
            if self.left:
                return self.left.insert(value)
            else:
                self.left = BSTNode(value)
                return True
          # if new value >= self.value 
            # IF, self.right is already taken by a node,
                # make that right node, call insert
            # set the right child to the new node with the new value
        else:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = BSTNode(value)      
                return True
            
     # False if tree does not contain value
     # Return True if the tree contains the value
    def contains(self, target):
        # if current self.value == target:
        if self.value == target:
            # return True
            return True
        # compare the target to current value
        # if current self.value < target
        if self.value < target:
            # check the left subtree
            if self.left is None:
                # if cannot go left, return False
                return False
            found = self.left.contains(target) # recursion state
            
        # if current self.value >= target
        if self.value >= target:
            # check the right subtrree contains target
            if self.right is None:
                # if you cannt go right, return False
                return False
            found =  self.right.contains(target)
         # return if found since its true that in the recursion, it did contain the target
        return found
            
       

    # Return the maximum value found in the tree
    def get_max(self):
        # Keep moving to the right if current root node is not max since max node goes rightmost
        if not self.right:
            return self.value
        return self.right.get_max() # recursion to get the max in the rightmost


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
