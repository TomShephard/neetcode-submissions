class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substringset = set()
        result = 0
        l = 0

        for r in range(len(s)):
            while s[r] in substringset:
                substringset.remove(s[l])
                l += 1


            substringset.add(s[r])
            result = max(result, r - l + 1)
        return result