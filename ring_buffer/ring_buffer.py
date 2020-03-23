from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # check to see if the storage length is less then the capacity
        if len(self.storage) < self.capacity:
            # add new item to the tail
            self.storage.add_to_tail(item)
        else:
            # if there are no items in the list then we set it to the head
            if self.current == None or self.current.next == None:
                self.current = self.storage.head
            else:
                self.current = self.current.next
            self.current.value = item

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        node = self.storage.head
        while node is not None:
            list_buffer_contents.append(node.value)
            node = node.next


        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
