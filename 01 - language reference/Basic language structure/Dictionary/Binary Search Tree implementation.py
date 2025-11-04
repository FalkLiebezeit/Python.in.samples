# Binary Search Tree implementation with insert, search, delete, and 2D print
# Optimized and commented for clarity

COUNT = [5]  # Spaces away from previous layer for tree printing

class BSTree:
    """Binary Search Tree with insert, search, and delete operations."""

    def insert(self, root, val):
        """Insert a new node with given value into the BST."""
        if root is None:
            return newNode(val)
        if val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)
        return root

    def search(self, root, val):
        """Search for a value in the BST. Returns the node or None."""
        if root is None or root.val == val:
            return root
        if val < root.val:
            return self.search(root.left, val)
        return self.search(root.right, val)

    def delete(self, root, val):
        """Delete a node with the given value from the BST."""
        if root is None:
            return root
        if val < root.val:
            root.left = self.delete(root.left, val)
        elif val > root.val:
            root.right = self.delete(root.right, val)
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # Node with two children: get inorder successor
            temp = self.minValueNode(root.right)
            root.val = temp.val
            root.right = self.delete(root.right, temp.val)
        return root

    def minValueNode(self, node):
        """Find the node with the minimum value in the BST."""
        current = node
        while current.left is not None:
            current = current.left
        return current

class newNode:
    """Binary Tree Node."""
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def printTreeUtil(root, space):
    """Print binary tree in 2D (reverse inorder traversal)."""
    if root is None:
        return
    space += COUNT[0]
    printTreeUtil(root.right, space)
    print()
    for _ in range(COUNT[0], space):
        print(end=" ")
    print(root.val)
    printTreeUtil(root.left, space)

def printTree(root):
    """Wrapper for printTreeUtil, starts with space=0."""
    printTreeUtil(root, 0)

# --- Driver Code ---
if __name__ == '__main__':
    bst = BSTree()
    root = None
    # Insert nodes
    for val in [10, 8, 15, 6, 9, 12, 17, 14]:
        root = bst.insert(root, val)
    # Delete a node
    root = bst.delete(root, 8)
    # Print the tree
    printTree(root)