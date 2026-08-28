class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        hashmap = {} #int:count

        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)
            if hashmap[n] > 1:
                return n
