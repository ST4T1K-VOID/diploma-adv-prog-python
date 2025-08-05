from __future__ import annotations

from typing import Generator

class EmptyListException(Exception):
    pass


class Node:
    value: int
    next_node: Node | None

    def __init__(self, value: int, next_node: Node | None = None):
        self.value = value
        self.next_node = next_node

    def __repr__(self):
        return f"Node({self.value!r}, {self.next_node!r})"


class LinkedList:
    root: Node | None
    _current_node: Node | None

    def __init__(self, values: list[int, ...] | None = None):
        self.root = None
        self._current_node = None
        if values:
            for value in values:
                self.push(value)

    def __iter__(self) -> Generator:
        self._current_node = self.root
        while self._current_node:
            yield self._current_node.value
            self._current_node = self._current_node.next_node

        # self._current_node = self.root
        # return self


    # def __next__(self):
    #     if not self._current_node:
    #         raise StopIteration
    #     value = self._current_node.value
    #     self._current_node = self._current_node.next_node
    #     return value

    def __len__(self):
        if self.root is None:
            return 0

        length = 0
        current = self.root
        counting = True
        while counting:
            length += 1
            if current.next_node is None:
                counting = False
            else:
                current = current.next_node
        return length

    def head(self):
        """get head/root???"""
        pass

    def push(self, value: int) -> None:
        """Add to list from head/root"""
        new_node = Node(value, self.root)
        self.root = new_node

    def pop(self) -> int:
        """remove head/root. Return value of popped node"""
        popped = self.root.value
        self.root = self.root.next_node
        return popped

    def reversed(self) -> list[int, ...]:
        """Returns list of values in the order they were entered"""
        pass

    def __repr__(self):
        class_name = self.__class__.__name__
        return f"{class_name}||ROOT:{self.root}"
