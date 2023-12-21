#!/usr/bin/python3

class Node:
    """
    Node class representing a node of a singly linked list.

    Attributes:
    - data (int): Data of the node.
    - next_node (Node): Reference to the next node in the list.

    Methods:
    - __init__(self, data, next_node=None): Initializes new instance Node class
    """
    def __init__(self, data, next_node=None):
        """
        Initializes a new instance of the Node class.

        Parameters:
        - data (int): Data of the node.
        - next_node (Node): Reference to next node (default is None).
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data of the node."""
        return self._data

    @data.setter
    def data(self, value):
        """
        Set the data of the node.

        Parameters:
        - value (int): New data value.

        Raises:
        - TypeError: If data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """Retrieve the next node in the list."""
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node in the list.

        Parameters:
        - value (Node): New next node value.

        Raises:
        - TypeError: If next_node is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """
    SinglyLinkedList class representing a singly linked list.

    Attributes:
    - head: Reference to the head of the linked list.

    Methods:
    - __init__(self): Initializes a new instance of the SinglyLinkedList class.
    - sorted_insert(self, value): Inserts a new Node.
    - __str__(self): Returns a string representation of the linked list.
    """
    def __init__(self):
        """Initializes a new instance of the SinglyLinkedList class."""
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the sorted position in the list.

        Parameters:
        - value (int): Value to be inserted.
        """
        new_node = Node(value)
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """Returns a string representation of the linked list."""
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result
