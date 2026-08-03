class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        result = 0
        seenmap = set()

        for r in range ( len(s)):
            if s[r] in seenmap:
                while s[r] in seenmap:
                    seenmap.remove(s[l])
                    l += 1
            seenmap.add(s[r])
            result = max(result,  r - l + 1)
        return result
