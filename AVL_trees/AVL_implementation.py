"""
1. In this file there is Python implementation
of AVL tree.

2. If you want to read the theory behind further
implementation, check out `AVL.md`

3. In this implementation `root` keeps `TreeNode`
class, hence it's our AVL_Tree

4. Important: don't forget that Rebalancing happens not only
through the `root` of the whole tree, but through subtrees as well

5. Example of the Tree which is not balanced
       13
      /  \
     11  21
     /
    8
   /
  7

Imagine we've added `7` as our new node.
Steps after that:
    1. we return to previous layer where `8.left = Node(7)`
    2. we increase `height` by 1 and check that `balance` is Okay
    3. Again return to the previous layer, where we have:
         11
        /
       8
      / \
     7   None

    And here we spot the problem with `balance` => left heavy tree

Important note: Rebalancing happens not only from the root, but
    actually in every node that has children. Here it's 11.

    4. As we have `> 1` > left-heavy and we enter this `if` condition.
    5. `root` is 11 in this case. We need to find out: whether
        our new node (7) is `> || <` than `.left/.right` of  root.
        As we see, it's smaller that's why we do only `_right_rotate()`
    6. Schema from the code which wil be used
       y_node = node.left
       z_node = y_node.right

       # perofrm rotation
       y_node.right = node
       node.left = z_node

       Actual stuff happening behind the scenes
        `node` is 11
        8 = 11.left
        None = 8.right

        # perofrm rotation
        8.right = 11
        11.left = None

    7. As you see, 8 pops one layer above tugging 7 with it,
        whilst 11 gets to the `.right` tugging `.right` of 8 if such
        exists (in our case it's None)

    8. If we had not 7, but 9 as example:

        11
       /
      8
       \
        9

    9. in this case we make `_left_rotate()` first where we supply 11.left as root
    10. Schema:
       y_node = node.right
       z_node = y_node.left

       # perofrm rotation
       y_node.left = node
       node.right = z_node

       Actual stuff happening behind the scenes
       `node` is 8
       9 = 8.right
       None = 9.left

       # perofrm rotation
       9.left = 8
       8.right = None

    And then we continue with `_right_rotate()` as in the prevous example

6. Example of node deletion:
        # Some nodes
            /
            8
             \
              10
             /  \
            9    11

   1. we want to delete 8
   2. traverse `delete_node()` till we hit `else`
   3. we see that both: `.left` and `.right` are not empty
    => again hit `else`.
   4. call `._get_min_value_node(node.right)` where we'll try to find smallest on the
    right subtree from node-to-be-delted
    5. 10 != None and 10.left != None => again call this method with 10.left
    6. 9 != None BUT 9.left == None => return 9
    7. Pop up to the `delete_node()` and place instead of 8 -> 9
    8. Next, we need to remove 9 from that right subtree. Actually,
        same actions as above:
        - Pay attention that we call `delete_node` on node.right (9.right which was 8.right)
        - `node.left == None` is where we hit and we return None as `9.right` is None
    9. Recalculate balance * height for every root (remember that root is every node with subtrees)
    10. But here not simple left-heavy/right-heavy, we need to check if all the nodes
        in the subtrees are also balanced, hence logic is a little but more complicated
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

        # perofrm rotation
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
