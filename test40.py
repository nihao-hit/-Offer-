class BinaryTreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    # 方法一：使用partition，略。方法二：用二叉排序树保存最小的k个数，不断调整
    def getLeastNumbers(self,nums,k):
        '''
        :type nums:list[int]
        :type k:int
        :rtype:list[int]
        '''
        def insert(root,num):
            if root:
                if root.val < num:
                    if not root.right:
                        root.right = BinaryTreeNode(num)
                        return
                    else:
                        insert(root.right,num)
                else:
                    if not root.left:
                        root.left = BinaryTreeNode(num)
                        return
                    else:
                        insert(root.left,num)
        
        def minNumber(root):
            if root:
                if not root.right:
                    return root.val
                else:
                    return minNumber(root.right)

        def delete(root):
            if root.right:
                if not root.right.right:
                    if root.right.left:
                        root.right = root.right.left
                    else:
                        root.right = None
                else:
                    delete(root.right)

        def inorder(root,result):
            if root:
                inorder(root.left,result)
                result.append(root.val)
                inorder(root.right,result)
        
        root = BinaryTreeNode(nums[0])
        result = []
        curMax = nums[0]
        for i in range(1,len(nums)): 
            if i >= k:
                if nums[i] < minNumber(root):
                    delete(root)
                    insert(root,nums[i])
            else:
                insert(root,nums[i])
        inorder(root,result)
        return result