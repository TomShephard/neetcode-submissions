class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest = 0

        for n in nums:
            length = 0
            if (n - 1) not in hashset: #start of a sequence

                while (n + length) in hashset:
                    length +=1
                
                longest = max(length, longest)
        return longest