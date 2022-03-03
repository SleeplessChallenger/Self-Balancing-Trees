"""
1. In this file there is Python implementation
of AVL tree.

2. If you want to read the theory behind further
implementation, check out `AVL.md`

3. In this implementation `root` keeps `TreeNode`
class, hence it's our AVL_Tree
"""
from typing import Optional


class TreeNode:
    """
    class that depicts the Node
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AvlTree:
    """
    class that depicts methods for AVL tree
    """

    def insert_node(self, root: Optional[TreeNode], new_node: int):
        """
        method that is responsible for inserting
        new value in the tree

        Steps:
        1. insert in the correct position as LEAF node
        2. update height
        3. check balance
        4. As we recursively enter the tree, we will
        come back layer by layer updating height and checking
        balance. Hence at one moment we can catch unbalanced stuff
        """
        if not root:
            return TreeNode(new_node)
        elif new_node >= root.value:
            root.right = self.insert_node(root.right, new_node)
        elif new_node < root.value: # else
            root.left = self.insert_node(root.left, new_node)

        root.height = 1 + max(
            self._get_height(root.left),
            self._get_height(root.right)
        )

        curr_balance = self._get_balance(root)

        if curr_balance > 1: # left-heavy
            if new_node > root.left.value:
                root.left = self._left_rotate(root.left)
                return self._right_rotate(root)
            elif new_node < root.left.value:
                return self._right_rotate(root)

        if curr_balance < -1: # right-heavy
            if new_node > root.right.value:
                return self._left_rotate(root)
            elif new_node < root.right.value:
                root.right = self._right_rotate(root.right)
                return self._left_rotate(root)

        return root

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0

        left_height = self._get_height(node.left)
        right_height = self._get_height(node.right)

        return left_height - right_height

    def _left_rotate(self, node: TreeNode):
        """
        Read in `_right_rotation` as here the mirror situation
        """
        y_node = node.right
        z_node = y_node.left

        y_node.left = node
        node.right = z_node

        node.height = 1 + max(
            self._get_height(node.left), self._get_height(node.right)
        )
        y_node.height = 1 + max(
            self._get_height(y_node.left), self._get_height(y_node.right)
        )

        return y_node

    def _right_rotate(self, node: TreeNode):
        """
        Look at the screenshot: 
        - `node == x`
        - `y_node == y`
        - `z_node == right of y aka blue node` 
        """

        # gather nodes to perform rotation
        y_node = node.left
        z_node = y_node.right

        # perform rotation
        y_node.right = node
        node.left = z_node

        # update heights of our `x` & `y` nodes
        node.height = 1 + max(
            self._get_height(node.left), self._get_height(node.right)
        )
        y_node.height = 1 + max(
            self._get_height(y_node.left), self._get_height(y_node.right)
        )

        # as `y_node` is our new `root` for the current subtree (or even whole tree)
        return y_node

    def delete_node(self, node: Optional[TreeNode], value: int):
        if not node:
            return node
        
        elif node.value < value:
            node.right = self.delete_node(node.right, value)
        elif node.value > value:
            node.left = self.delete_node(node.left, value)
        else:
            if node.left is None:
                temp_node_right = node.right
                node = None
                return temp_node_right
            elif node.right is None:
                temp_node_left = node.left
                node = None
                return temp_node_left
            else:
                temp_from_right_subtree = self._get_min_value_node(node.right)
                node.value = temp_from_right_subtree.value
                node.right = self.delete_node(node.right, temp_from_right_subtree.value)
        
        if node is None:
            return node
        
        node.height = 1 + max(
            self._get_height(node.left), self._get_height(node.right)
        )

        curr_balance = self._get_balance(node)

        # if left-heavy
        if curr_balance > 1 and self._get_balance(node.left) >= 0:
            return self._right_rotate(node)
        # if right-heavy
        if curr_balance < -1 and self._get_balance(node.right) <= 0:
            return self._left_rotate(node)
        # if left-heavy and left sub-tree has right-heavy stuff
        if curr_balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        # if right-heavy and right sub-tree has left-heavy stuff
        if curr_balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node
        
    def _get_min_value_node(self, node):
        if not node or node.left is None:
            return node
        return self._get_min_value_node(node.left)


tree = AvlTree()
nums = [33, 13, 52, 9, 21, 61, 8, 11]
root = None

for num in nums:
    root = tree.insert_node(root, num)
