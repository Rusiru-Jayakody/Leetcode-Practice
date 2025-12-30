
class Solution:
    def invertTree(self, root):
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root



#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



# --- Helper: Build tree from level-order list ---

from collections import deque
def buildTree(values):
    if not values or values[0] == "null":
        return None
    root = TreeNode(int(values[0]))
    q = deque([root])
    i = 1

    while q and i < len(values):
        node = q.popleft()

        #left child
        if values[i] != "null":
            node.left = TreeNode(int(values[i]))
            q.append(node.left)
        i += 1
        if i >= len(values):
            break

        #right child
        if values[i] != "null":
            node.right = TreeNode(int(values[i]))
            q.append(node.right)
        i += 1
    return root



# --- Helper: Print tree level-order ---

def printTree(root):
    if not root:
        print("[]")
        return
    q = deque([root])
    res = []

    while q:
        node = q.popleft()

        if node:
            res.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            res.append("null")
    print(res)


# ------------------ MAIN ------------------

if __name__ == "__main__":

    sol = Solution()
    tree = TreeNode()
    print("Enter tree nodes in level order (use 'null' for empty nodes):")
    # Example: 1 2 3 4 5 null null
    values = input().split()
    root = buildTree(values)
    inverted = sol.invertTree(root)
    print("\nInverted tree (level order):")
    printTree(inverted)