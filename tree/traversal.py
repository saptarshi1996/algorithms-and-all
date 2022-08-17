from tree.treenode import TreeNode
from tree.binarysearchtree import BinarySearchTree


def inorder(root: TreeNode):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)


def preorder(root: TreeNode):
    if root:
        print(root.value)
        preorder(root.left)
        preorder(root.right)


def postorder(root: TreeNode):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value)


def main():

    t = BinarySearchTree()

    t.add_node(3)
    t.add_node(2)
    t.add_node(12)
    t.add_node(1)
    t.add_node(9)
    t.add_node(7)
    t.add_node(10)
    t.add_node(15)
    t.add_node(14)

    print('Inorder')
    inorder(t.root)

    print('Preorder')
    preorder(t.root)

    print('Postorder')
    postorder(t.root)

if __name__ == '__main__':
    main()
