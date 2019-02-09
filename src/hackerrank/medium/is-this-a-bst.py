# https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem


""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""


def is_bst(node, left=None, right=None):
    if node is None:
        return True
    if left is not None and (not node.data > left.data):
        return False
    if right is not None and (not node.data < right.data):
        return False
    return is_bst(node.left, left, node) and is_bst(node.right, node, right)


def checkBST(root):
    return is_bst(root)
