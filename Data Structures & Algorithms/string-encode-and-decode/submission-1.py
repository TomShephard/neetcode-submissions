class Solution:

    def encode(self, strs: List[str]) -> str:
        
        string = ""
        for s in strs:
            string = string + s + "⅝"

        print (string)
        return string

    def decode(self, s: str) -> List[str]:
        result = []
        word = ""
        for c in s:
            if c != "⅝":
                word = word + c
            else:
                result.append(word)
                word = ""
        return result
