'''
Given an array of strings words[]. Find the longest string in words[] such that every prefix of it is also present in the array words[]. 
Note: If multiple strings have the same maximum length, return the lexicographically smallest one.
Examples:
Input: words[] = ["p", "pr", "pro", "probl", "problem", "pros", "process", "processor"]
Output: pros
Explanation: "pros" is the longest word with all prefixes ("p", "pr", "pro", "pros") present in the array words[].
'''
class Solution():
    def longestString(self, words):
        # code here
        wordset = set(words)
        words.sort()
        longest = ''
        for word in words:
            isvalid = True
            for i in range(1,len(word)):
                if word[:i] not in wordset:
                    isvalid = False
                    break
                
            if isvalid:
                if (len(word) > len(longest)) or (len(word) == len(longest) and word < longest):
                    longest = word
        return longest
            
        
        
