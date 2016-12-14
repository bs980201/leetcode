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
    def __init__(self, root):
        self.s = Stack()
        self._putall(root)

    def hasNext(self):
        return not self.s.isEmpty()

    def next(self):
        tempnode = self.s.pop()
        self._putall(tempnode.right)
        return tempnode.val

    def _putall(self,node):
        while node != None:
            self.s.push(node)
            node = node.left


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())