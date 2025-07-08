//Given an array arr[] of integers, for each element, find the closest (distance wise) to its right that has a higher frequency than the current element.
//If no such element exists, return -1 for that position.

class Solution:
    def findGreater(self, arr):
        # code here
        n = len(arr)
        res = [-1] * n 
        freq = [0] * (max(arr)+1)
        stack = []
        
        for i in range(n):
            freq[arr[i]] += 1
        
        for i in range(n-1,-1,-1):
            cur = arr[i]
            curfreq = freq[cur]
            
            while stack and freq[stack[-1]] <= curfreq:
                stack.pop()
                
            if stack:
                res[i] = stack[-1]
                
            stack.append(cur)
            
        return res
    
        
