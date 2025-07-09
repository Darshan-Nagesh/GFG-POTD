'''
Given an array arr[] of positive integers, find the total sum of the minimum elements of every possible subarrays.

Note: It is guaranteed that the total sum will fit within a 32-bit unsigned integer.

Examples:

Input: arr[] = [3, 1, 2, 4]
Output: 17
Explanation: Subarrays are [3], [1], [2], [4], [3, 1], [1, 2], [2, 4], [3, 1, 2], [1, 2, 4], [3, 1, 2, 4]. Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1. Sum of all these is 17.
'''
class Solution:
    def sumSubMins(self, arr):
        # Code here
        n = len(arr)
        prev = [-1] * n
        next = [n] * n
        stack = []
        
        #previous smallest element
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            prev[i] = stack[-1] if stack else -1
            stack.append(i)
        
        stack.clear()
        
        #next smallest element
        for i in range(n-1,-1,-1):
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            next[i] = stack[-1] if stack else n
            stack.append(i)
         
        result = 0   
        for i in range(n):
            left = i - prev[i]
            right = next[i] - i
            result += arr[i] * left * right
        
        return result
