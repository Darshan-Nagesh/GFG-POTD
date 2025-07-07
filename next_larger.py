class Solution:
    def nextLargerElement(self, arr):
        # code here
        stack = []
        n = len(arr)
        res = [-1] * n
        for i in range(2*n-1,-1,-1):
            cur = arr[i%n]
            
            while stack and stack[-1] <= cur:
                stack.pop()
                
            if i < n:
                res[i] = stack[-1] if stack else -1
            
            stack.append(cur)
        return res
