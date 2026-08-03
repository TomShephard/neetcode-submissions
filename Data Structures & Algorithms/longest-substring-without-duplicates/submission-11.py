class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l, r = 0, 0
        seenmap = set()

        while r < len(s):

            while s[r] in seenmap:
                seenmap.remove(s[l])
                l += 1
            
            seenmap.add(s[r])
            longest = max(longest, r - l + 1)
            r += 1
        return longest