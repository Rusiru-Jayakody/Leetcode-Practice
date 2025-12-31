
class Solution:
    def isBalanced(self, root) -> bool:
        balance = [True]
        def depth(root):
            if not root:
                return 0
            left = depth(root.left)
            if balance[0] is False:
                return 0
            right = depth(root.right)

            if abs(left - right) > 1:
                balance[0] = False
                return 0
            
            return 1 + max(left, right)
        
        depth(root)
        return balance[0]
    

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val = 0, left=None, right=None):
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



#--------------MAIN--------------------
if __name__ == "__main__":
    sol = Solution()
    print("Enter tree nodes in level order (use 'null' for empty nodes):")
    # Example: 1 2 3 4 5 null null
    values = input().split()
    root = buildTree(values)
    ans = sol.isBalanced(root)
    print(ans)


        