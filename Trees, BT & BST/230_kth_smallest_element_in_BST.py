
class Solution:
    def kthSmallest(self, root, k: int) -> int:
        count = [0]
        ans = [0]
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            count[0] +=1
            if count[0] == k:
                ans[0] = root.val
            dfs(root.right)
        
        dfs(root)
        return ans[0]


#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val = 0, left =None, right = None):
        self.val = val
        self.left = left
        self.right = right



# --- Helper: Build tree from level-order list ---

from collections import deque
def buildTree(values):
    if not values or values[0] == "null":
        return None
    root = TreeNode(int(values[0]))
    i = 1
    q = deque([root])
    while q and i < len(values):
        node = q.popleft()

        #left child
        if values[i] != "null":
            node.left = TreeNode(int(values[i]))
            q.append(node.left)
        i += 1

        if i >= len(values) :
            break

        #right child
        if values[i] != "null":
            node.right = TreeNode(int(values[i]))
            q.append(node.right)
        i += 1
    return root



#-------------------MAIN------------------------
if __name__ == "__main__":
    sol = Solution()
    print("Enter tree nodes in level order (use 'null' for empty nodes):")
    # Example: 1 2 3 4 5 null null
    values = input().split()
    k = int(input())
    root = buildTree(values)
    ans = sol.kthSmallest(root,k)
    print(ans)