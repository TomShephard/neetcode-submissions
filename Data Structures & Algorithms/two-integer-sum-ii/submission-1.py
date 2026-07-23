class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        seenmap = {}

        for i, n in enumerate(numbers):
            diff = target - n

            if diff in seenmap:
                return [seenmap[diff] + 1, i + 1]
            seenmap[n] = i
        