from abc import ABC
from collections.abc import Iterator
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self, head):
        self.Head = head

    def print_linkedList(self):
        current_node = self.Head
        while current_node is not None:
            print(current_node.data, end=" ")
            current_node = current_node.next

    def get_length(self):
        current_node = self.Head
        i=0
        while current_node is not None:
            current_node = current_node.next
            i = i + 1
        return i

    def append_to_linkedList(self, new_node):
        past_node = None
        current_node = self.Head
        while current_node is not None:
            past_node = current_node
            current_node = current_node.next
        if current_node is None:
            past_node.next = new_node
