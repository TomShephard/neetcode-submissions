class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            if nums[m] >= nums[l]:
                #Mid is in left sorted array
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1

            else:
                #Mid is in right sorted array
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = r - 1
        
        return -1