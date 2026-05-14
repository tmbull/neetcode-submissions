class Solution:

    def encode(self, strs: List[str]) -> str:
        # to encode, we join on a delimeter
        # need to escape delimeter if it exists in text
        # ["neet|", "fo|oo"] -> neet|||fo||oo
        tokens = [f"{len(s)}|{s}" for s in strs]
        return "".join(tokens)
        
    def decode(self, s: str) -> List[str]:
        digits = ""
        i = 0
        results = []
        while i < len(s):
            while s[i] != '|':
                digits += s[i]
                i += 1
            count = int(digits)
            i+=1
            token = s[i:i+count]
            results.append(token)
            i = i+count
            digits = ""

        return results
