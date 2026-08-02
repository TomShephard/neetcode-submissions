class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = [] #temp, index
        result = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stacktemp, stackindex = stack.pop()
                result[stackindex] = i - stackindex
            stack.append([t, i])
        
        return result
