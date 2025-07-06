class Solution:
    def countLessEq(self, a, b):
        # code here
        b.sort()
        res = []
        for num in a:
            low, high = 0, len(b)-1
            count = 0
            while low <= high:
                mid = (low+high)//2
                if b[mid] <= num:
                    count = mid + 1
                    low = mid + 1
                else:
                    high = mid -1
            res.append(count)
        return res
