class node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class linked_list:
    def __init__(self, head=None):
        self.head = None
        self.tail = None
        self.__len__ = 0
        self.store = []

    # displays to the values of the list in an array (mimicking javascripts Object.values method)
    def values(self):  # O(n)
        self.store = []
        current = self.head
        if self.head:
            while current:
                self.store.append(current.value)
                current = current.next
            return list(self.store)
        return list(self.store)

    # add from the front of the list
    def unshift(self, new_node):  # O(1)
        current_head = self.head
        new_head = new_node
        if self.head:
            new_head.next = current_head
            self.head = new_head
        else:
            self.head = new_node
        self.__len__ += 1

    def shift(self):  # O(1)
        current_head = self.head
        if self.head:
            self.head = self.head.next
            current_head.next = None
            self.__len__ -= 1
        return current_head

   # add nodes from the back of the list
    def append(self, new_node):  # O(1)
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
        self.__len__ += 1

    def pop(self):
        current_tail = self.tail
        current = self.head
        if self.head and self.tail:
            if(self.__len__ == 1):
                last_value = self.head.value and None
                self.head = None
                self.tail = None
                return last_value
            while current.next:
                if(self.head.next.value == self.tail.value):
                    self.head.next == None
                    self.tail = self.head
                    self.__len__ -= 1
                    break
                if(current.next.value == current_tail.value):
                    self.tail = current
                    current.next = None
                    self.__len__ -= 1
                    break
                current = current.next

            return current_tail

    # check if an element is in the list

    def contains(self, value):  # O(n)
        isPresent = False
        current = self.head
        if self.head:
            while current.next:
                if current.value == value or current.next.value == value:
                    isPresent = True
                    break

                current = current.next
        return isPresent

    # delete first element with a certain value
    def remove(self, value):  # O(n)
        current = self.head
        disconnected_node = None
        if self.head:
            while current.next:
                if self.head.value == current.value and current.value == value:
                    self.head = current.next
                    disconnected_node = current
                    current.next = None
                    self.__len__ -= 1
                    break
                elif current.next.value == self.tail.value and current.next.value == value:
                    self.tail = current
                    disconnected_node = current.next
                    current.next = None
                    self.__len__ -= 1
                    break
                elif current.next.value == value:
                    node_before_outgoing_node = current
                    outgoing_node = current.next
                    node_after_outgoing_node = outgoing_node.next
                    node_before_outgoing_node.next = node_after_outgoing_node
                    outgoing_node.next = None
                    disconnected_node = outgoing_node
                    self.__len__ -= 1

                    break
                current = current.next

        return disconnected_node

    def reverse(self):
        # code goes here
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

        return self


def create_linked_list(list: list):
    ll = linked_list()
    if len(list) > 0:
        for value in list:
            new_node = node(value)
            ll.append(new_node)
    return ll
