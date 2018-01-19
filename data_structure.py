"""
Data structure implementation
"""

class Stack(object):
    def __init__(self):
        self.__data = []

    @property
    def is_empty(self):
        return len(self.__data) == 0

    @property
    def size(self):
        return len(self.__data)

    def push(self, value):
        self.__data.append(value)

    def pop(self):
        if len(self.__data) <= 0:
            raise IndexError('No data in stack')

        value = self.__data[len(self.__data) - 1]
        del self.__data[len(self.__data) - 1]
        return value


class Node(object):
    def __init__(self, value, next_node=None):
        self.__data = value
        self.__next_node = next_node

    def get(self):
        return self.__data

    def get_next_node(self):
        return self.__next_node

    def set_next_node(self, next_node):
        self.__next_node = next_node


class LinkedList(object):
    def __init__(self, head=None):
        self.__head = head

    @property
    def size(self):
        current = self.__head
        count = 0
        while current:
            count = count + 1
            current = current.get_next_node()

        return count

    def insert(self, value):
        new_node = Node(value)
        new_node.set_next_node(self.__head)
        self.__head = new_node

    def search(self, value):
        current = self.__head
        found = False
        while current and found is False:
            if current.get() == value:
                found = True
            else:
                current = current.get_next_node()

        if current is None:
            raise ValueError("Value is not in Linked List")

        return current

    def delete(self, value):
        current = self.__head
        previous = None
        found = False

        while current and found is False:
            if current.get() == value:
                found = True
            else:
                previous = current
                current = current.get_next_node()

        if current is None:
            raise ValueError('Value is not in Linked List')

        if previous is None:
            self.head = current.get_next_node()
        else:
            previous.set_next_node(current.get_next_node())
