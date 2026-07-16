class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sMap = {}
        tMap = {}

        for x in s:
            if x in sMap:
                sMap[x] += 1
            else:
                sMap[x] = 1
        
        for x in t:
            if x in tMap:
                tMap[x] += 1
            else:
                tMap[x] = 1
        
        print (sMap)
        print(tMap)
        if tMap == sMap:
            return True
        else:
            return False
        
       

        