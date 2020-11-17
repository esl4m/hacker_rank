#!/usr/bin/python3
#  by: esl4m diaa
#      17 Nov 2020

# https://leetcode.com/problems/binary-tree-paths/
# Implement the solution for listing all paths in a node 
# using Deep First Search (dfs)


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def binary_tree_path(self, root: TreeNode) -> List[str]:
        def dfs(root, path):
            # implement the deep first search
            # check if no values in left & right -- just return the path
            if not root.left and not root.right:
                paths.append(path)
            
            if root.left:
                new_path = path + '->' + str(root.left.value)
                dfs(root.left, new_path)
            
            if root.right:
                new_path = path + '->' + str(root.right.value)
                dfs(root.right, new_path)

        
        # define paths as the final result
        paths = []

        if not root:
            return paths
        
        # else call the dfs and give it root, and path as "root value"
        # bcuz in this case we are checking every root value (deep)
        dfs(root, str(root.value))

        return paths

# Input 
# [1,2,3,null,5]
# [1,null,2,3]
# [5,4,7,3,null,2,null,-1,null,9]

# output
# ["1->2->5","1->3"]
# ["1->2->3"]
# ["5->4->3->-1","5->7->2->9"]