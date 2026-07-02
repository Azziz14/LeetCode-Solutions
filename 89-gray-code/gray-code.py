class Solution:
    def grayCode(self, n: int):
        ans = []

        for i in range(1 << n):   # 2^n numbers
            ans.append(i ^ (i >> 1))

        return ans