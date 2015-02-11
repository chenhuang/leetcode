class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    # @param A: Given an integer array with no duplicates.
    # @return: The root of max tree.
    
    def maxTree(self, A):
        # write your code here
        self.current = 0
        return self.maxTree_Rec(A, len(A))
    
    def maxTree_Rec(self, A, size):
        if size <= 0:
            return None
        elif size == 1:
            node = TreeNode(A[self.current])
            self.current += 1
            return node
        else:
            node_left = self.maxTree_Rec(A, size/2-1)
            node = TreeNode(A[self.current])
            node.left = node_left

            self.current += 1
            node.right = self.maxTree_Rec(A, size-size/2)
            return node

def printTree(node):
    if node is None:
        return
    else:
        print node.val
        printTree(node.left)
        printTree(node.right)
        

if __name__ == "__main__":
    s = Solution()
    root = s.maxTree([2,5,6,0,3,1])
    printTree(root)





