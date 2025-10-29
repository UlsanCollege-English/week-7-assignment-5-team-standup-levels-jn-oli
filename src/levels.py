# src/levels.py

from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root):
    """Return the level-order traversal of a binary tree."""
    if not root:
        return []
    res = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(level)
    return res


def zigzag_level_order(root):
    """Return the zigzag level-order traversal of a binary tree."""
    if not root:
        return []
    res = []
    queue = deque([root])
    left_to_right = True
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if not left_to_right:
            level.reverse()
        res.append(level)
        left_to_right = not left_to_right
    return res


def right_side_view(root):
    """Return the list of nodes visible from the right side."""
    if not root:
        return []
    view = []
    queue = deque([root])
    while queue:
        n = len(queue)
        for i in range(n):
            node = queue.popleft()
            if i == n - 1:
                view.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return view
