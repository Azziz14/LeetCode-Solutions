class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        result = []
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
            if freq[i]>len(nums)//3 and i not in result:
                result.append(i)
        return result
        