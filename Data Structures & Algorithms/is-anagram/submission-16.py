class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        tmap = {}
        smap = {}

        for c in s:
            if c in smap:
                smap[c] += 1
            else:
                smap[c] = 1
        
        for c in t:
            if c in tmap:
                tmap[c] += 1
            else:
                tmap[c] = 1
        
        if tmap == smap:
            return True
        else:
            return False
        