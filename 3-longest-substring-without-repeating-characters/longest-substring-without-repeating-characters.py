class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        answer = 0
        seen = set() 
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            length = right-left+1
            answer = max(answer,length)
        return answer 