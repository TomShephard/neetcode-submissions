class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenmap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in seenmap:
                return [seenmap[diff], i]
            seenmap[n] = i