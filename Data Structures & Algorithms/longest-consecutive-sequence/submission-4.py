class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = 0
        hashset = set(nums)

        for n in nums:
            length = 0
            if (n - 1) not in hashset:
                while (n + length) in hashset:
                    length += 1
            
            longest = max(length, longest)
        
        return longest
        