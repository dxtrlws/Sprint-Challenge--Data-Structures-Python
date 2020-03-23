import sys
sys.path.append('/Users/dxtrlws/Lambda/Computer Science/03 Data Structures/Lectures/Data-Structures/queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare value to the current node
        if self.value:
            # if smaller go left
            if value < self.value:
                if self.left is None:
                    self.left = BinarySearchTree(value)
                else:
                    self.left.insert(value)
            # if larger, go right
            elif value > self.value:
                if self.right is None:
                    self.right = BinarySearchTree(value)
                else:
                    self.right.insert(value)
        # if no node to goto, (either left or right)
            # make the new node at the spot
        else:
            self.value = value


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # compare value to the current node value
        # if equal return true
        if target == self.value:
            return True
        # if smaller, go left
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                # if smaller, but we can't go left, return false
                return False
        # if bigger, go right
        elif target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                # if smaller, but we can't go right, return false
                return False         

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # go left first
        if self.left is not None:
            self.left.for_each(cb)
        
        #print ourselves
        cb(self.value)
        
        # go right
        if self.right is not None:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # go left first
        if node.left is not None:
            node.in_order_print(node.left)
        
        #print ourselves
        print(node.value)
        
        # go right
        if node.right is not None:
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
