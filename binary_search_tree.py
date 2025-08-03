from typing import List

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            #Binary search tree doesnt have dups
            return
        
        if data < self.data:
            # add data to the left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # add data to the right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        #visit left tree

        if self.left: 
            elements+= self.left.in_order_traversal()

        #visit base node
        elements.append(self.data)

        #visit right tree
        if self.right:
            elements+=self.right.in_order_traversal()
        return elements
    
    def search(self,val):
        if self.data == val:
            return True
        if val < self.data:
            # val might be in left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            # val might be in right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False
    def find_min(self):
        if self.left:
            return self.left.find_min()
        return self.data
    
    def find_max(self):
        if self.right:
            return self.right.find_max()
        return self.data
    
    def treesum(self):
        return sum(self.in_order_traversal())

def built_tree(elements:List):
    root = BinarySearchTreeNode(elements[0])

    for elem in elements[1:]:
        root.add_child(elem)

    return root



if __name__ == '__main__':
    numbers = [17,4,1,20,9,23,18,34]
    numbers_tree=built_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(100))
    print(numbers_tree.find_min())
    print(numbers_tree.find_max())
    print(numbers_tree.treesum())