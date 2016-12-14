"""173_Binary_Search_Tree_Iterator.py."""

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()


class BSTIterator:

    s = Stack()
    def __init__(self, root):
        putall(root)

    def hasNext(self):
        return !s.isEmpty()

    def next(self):
        tempnode = s.pop()
        putall(tempnode.right)
        return tempnode.val

    def putall(self):
        while node != None:
            s.push(node)
            node = node.left

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())