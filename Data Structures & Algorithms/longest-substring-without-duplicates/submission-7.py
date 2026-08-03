class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seenmap = set()
        l = 0
        longest = 0

        for r in range(len(s)):
            if s[r] in seenmap:
                while s[r] in seenmap:
                    seenmap.remove(s[l])
                    l += 1
            seenmap.add(s[r])
            longest = max(longest, r - l + 1)
        return longest