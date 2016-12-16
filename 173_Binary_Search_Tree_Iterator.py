"""173_Binary_Search_Tree_Iterator.py."""


class TreeNode:
    """Definition for a  binary tree node."""

    def __init__(self, x):
        """Init."""
        self.val = x
        self.left = None
        self.right = None


class Stack:
    """Stack."""

    def __init__(self):
        """Init."""
        self.items = []

    def isEmpty(self):
        """IsEmpty."""
        return self.items == []

    def push(self, item):
        """Push."""
        self.items.append(item)

    def pop(self):
        """Pop."""
        self.items.pop()


class BSTIterator:
    """BSTIterator."""

    def __init__(self, root):
        """Init."""
        self.s = Stack()
        self._putall(root)

    def hasNext(self):
        """Hasnext."""
        return not self.s.isEmpty()

    def next(self):
        """Next."""
        tempnode = self.s.pop()
        self._putall(tempnode.right)
        return tempnode.val

    def _putall(self, node):
        while node is not None:
            self.s.push(node)
            node = node.left
