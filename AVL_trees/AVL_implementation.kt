import kotlin.math.*

class Node(value: Int, left: null, right: null, height:Int=1)

class AVL_implementation {
    fun insertNode(root: Node, newNode: Int): Node {
        if (root == null) {
            return Node(newNode)
        } else if (newNode >= root.value) {
            root.right = this.insertNode(root.right, newNode)
        } else if (newNode < node.value) {
            root.left = this.insertNode(root.left, newNode)
        }

        root.height = 1 + max(
            this.getHeight(root.left), this.getHeight(root.right)
        )

        val currBalance: Int = this.getBalance(root)

        if (currBalance > 1) {
            // left-heavy tree
            if (root.left.value < newNode) {
                root.left = this.leftRotate(root.left)
                return this.rightRotate(root)
            } else if (root.left.value > newNode) {
                return this.leftRotate(root)
            }
        }

        if (currBalance < -1) {
            // right-heavy
            if (newNode > root.right.value) {
                return this.leftRotate(root)
            } else if (newNode < root.right.value) {
                root.rigt = this.rightRotate(root.right)
                return this.leftRotate(root)
            }
        }

        return root
    }

    fun deleteNode(node: Node, deleteNode: Int) {
        if (node == null) {
            return node
        } else if (node.value > deleteNode) {
            node.left = this.deleteNode(node.left, deleteNode)
        } else if (node.value < deleteNode) {
            node.right = this.deleteNode(node.right, deleteNode)
        } else {
            // we've found our node to be deleted
            if (node.left == null) {
                val tempNodeRight: Node? = node.right
                node = null
                return tempNodeRight
            } else if (node.right == null) {
                val tempNodeLeft: Node? = node.left
                node = null
                return tempNodeLeft
            } else {
                val tempNodeRightSubtree: Node? = this.getMinValueNode(node.right)
                node.value = tempNodeRightSubtree
                node.right = this.deleteNode(node.right, tempNodeRightSubtree)
            }
        }

        if (node == null) return node

        node.height = 1 + max(
            this.getHeight(node.left), this.getHeight(node.right)
        )

        val currBalance: Int = this.getBalance(node)

        // if left-heavy
        if (curr_balance > 1 && this.getBalance(node.left) >= 0) {
            return this.rightRotate(node)
        }
        // if right-heavy
        if (curr_balance < -1 && this.getBalance(node.right) <= 0) {
            return this.leftRotate(node)
        }
        // if left-heavy and left sub-tree has right-heavy stuff
        if (curr_balance > 1 && this.getBalance(node.left) < 0) {
            node.left = this.leftRotate(node.left)
            return this.rightRotate(node)
        }
        // if right-heavy and right sub-tree has left-heavy stuff
        if (curr_balance < -1 && this.getBalance(node.right) > 0) {
            node.right = this.rightRotate(node.right)
            return this.leftRotate(node)
        }
        return node
    }

    fun leftRotate(node: Node) {
        val yNode: Node? = node.right
        val zNode: Node? = yNode.left

        yNode.left = node
        node.right = zNode

        node.height = 1 + max(
            this.getHeight(node.left), this.getHeight(node.right)
        )

        yNode.height = 1 + max(
            this.getHeight(yNode.left), this.getHeight(yNode.right)
        )

        return yNode
    }

    fun rightRotate(node: Node) {
        val yNode: Node? = node.left
        val zNode: Node? = yNode.right

        yNode.right = node
        node.left = zNode

        node.height = 1 + max(
            this.getHeight(node.left), this.getHeight(node.right)
        )

        yNode.height = 1 + max(
            this.getHeight(yNode.left), this.getHeight(yNode.right)
        )

        return yNode
    }

    fun getHeight(node: Node) {
        if (node == null) {
            return 0
        }
        return node.height
    }

    fun getBalance(node: Node) {
        if (node == null) {
            return 0
        }
        val leftHeight: Int = this.getHeight(node.left)
        val rightHeight: Int = this.getHeight(node.right)

        return leftHeight - rightHeight
    }

    fun getMinValueNode(node: Node) {
        if (node == null || node.left == null) {
            return node
        }
        return this.getMinValueNode(node.left)
    }
}