class EmptyListException(Exception):
    pass


class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def value(self):
        # i.e. get_value
        return self.value

    def next(self):
        # i.e. get_next
        return self.next_node


class LinkedList:
    def __init__(self, values=None):
        self.root = None
        if values is not None:
            for value in values:
                self.push(value)

    def __iter__(self):
        pass

    def __len__(self):
        if self.root is None:
            return 0

        length = 0
        current = self.root
        counting = True
        while counting:
            length += 1
            if current.next() is None:
                counting = False
            else:
                current = current.next()
        return length

    def head(self):
        pass

    def push(self, value):
        # add
        if self.root is None:
            self.root = Node(value)
        else:
            current = self.root
            searching = True
            while searching:
                if current.next() is None:
                    current.next_node = Node(value)

    def pop(self):
        # remove
        pass

    def reversed(self):
        pass
