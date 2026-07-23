class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l, r = 1, len(numbers)
        current = int
        while current != target:

            if numbers[l - 1] + numbers[r - 1] == target:
                return [l, r]
            
            if numbers[l - 1] + numbers[r - 1] > target:
                r -= 1
            if numbers[l - 1] + numbers[r - 1] < target:
                l += 1
        