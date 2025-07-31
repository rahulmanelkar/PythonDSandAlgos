#linked list implementation in python
from abc import ABC
import os
from sys import maxsize
import ast
from collections import deque, defaultdict, namedtuple

class AbstractNode(ABC):
    pass

class AbstractLinkedList(ABC):
    pass

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.test_list = []

    def append(self, data):
        node_to_append = Node(data=data)
        if not self.head:
            self.head = node_to_append
            self.test_list.append((data,self.head))
            return
        else:
            next_node = self.head
            while next_node.next:
                next_node = next_node.next
            next_node.next = node_to_append
            self.test_list.append((data,next_node.next))
            return
        
    def find(self, data):
        index = 0
        if not self.head:
            return False
        if not self.head.next:
            return index if self.head.data == data else False
        else:
            traversal_node = self.head            
            while traversal_node.next:
                if traversal_node.data == data:
                    return index
                traversal_node = traversal_node.next
                index += 1
            return False
        
    def print_list(self):
        pass
        
def main():
    ll = LinkedList()
    ll.append(3)
    ll.append(6)
    ll.append(78)
    ll.append(42)
    ll.append(200)
    ll.append(202)
    ll.append(29)
    print(ll.test_list)
    print(ll.find(27))


if __name__ == '__main__':
    main()

