from typing import List,Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def dfs(nums):
            if not nums:
                # return List[Treenode] or Optional
                return [None]

            ans = []
            for i in range(len(nums)):
                #Handling left subtree
                leftTrees = dfs(nums[:i])
                #Handling right subtree
                rightTrees = dfs(nums[i+1:])

                for l in leftTrees:
                    for r in rightTrees:
                        root =  TreeNode(nums[i])
                        root.left = l
                        root.right = r
                        ans.append(root)
            return ans

        nums = list(range(1,n+1))
        return dfs(nums)

if __name__ == '__main__':
    obj = Solution()
    value = obj.generateTrees(3)
    for v in value:
        print(v.val)