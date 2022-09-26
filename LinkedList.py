class LinkedList:

    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values:
            self.append_multiple_nodes(values)

    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __len__(self):
        length = 0
        node = self.head
        while node:
            length += 1
            node = node.next
        return length

    def __repr__(self):
        return f'LinkedList({"->".join(node.value for node in self)})'

    def append(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail

    def append_multiple_nodes(self, values):
        try:
            for value in values:
                self.append(value)
        except TypeError:
            self.append(values)
        return self.tail

    def prepend(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            head = Node(value)
            head.next = self.head
            self.head = head
        return self.head

    def __str__(self):
        return " -> ".join(str(node) for node in self)

    @property
    def values(self):
        return (node.value for node in self)

    def __eq__(self, other):
        if not isinstance(other, LinkedList):
            return False
        if len(self) != len(other):
            return False
        for s_node, o_node in zip(self, other):
            if s_node != o_node:
                return False
        return True


class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return self.data == other.data