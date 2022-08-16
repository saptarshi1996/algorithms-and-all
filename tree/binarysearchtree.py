from tree.treenode import (
    TreeNode
)


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def add_node_helper(self, root: TreeNode, value: int):

        if not root:
            return TreeNode(value)

        if root.value > value:
            root.left = self.add_node_helper(root.left, value)
        elif root.value < value:
            root.right = self.add_node_helper(root.right, value)

        return root
        
    def add_node(self, value: int):
        self.root = self.add_node_helper(self.root, value)

    def print_tree_helper(self, root: TreeNode):
        if root:
            self.print_tree_helper(root.left)
            print(root.value)
            self.print_tree_helper(root.right)

    def print_tree(self):
        self.print_tree_helper(self.root)
