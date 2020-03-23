class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  def reverse_list(self):
    # TO BE COMPLETED
    # create variable to hold previous node
    prev_node = None
    # assign current node to the current head
    current_node = self.head
    # create loop to go through the link list
    while current_node is not None:
      # assign nex node to the current next node as a place holder
      next_node = current_node.next_node
      # assign the current next node to the previous node
      current_node.next_node = prev_node
      # set the previous node to the current node
      prev_node = current_node
      # set the current node to the next node
      current_node = next_node
    # Lastly set the head to the previous node  
    self.head = prev_node
