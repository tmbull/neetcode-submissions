a = ord('a')
z = ord('z')
A = ord('A')
Z = ord('Z')
zero = ord('0')
nine = ord('9')

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # easy way, strip out whitespace and non-alphanumeric
        # O(1) space way, skip whitespace and invalid char

        l = 0
        r = len(s) - 1
        while l < r:
            s_l = s[l].lower()
            s_r = s[r].lower()
            is_valid_l = self.isValid(s_l)
            is_valid_r = self.isValid(s_r)
            print(f"{l} {s[l]} {is_valid_l} {r} {s[r]} {is_valid_r}")
            if is_valid_l and is_valid_r:
                if s_l != s_r:
                    return False
                l += 1
                r -= 1
            if not is_valid_l:
                l += 1
            if not is_valid_r:
                r -= 1

        return True

    def isValid(self, char):
        c = ord(char)
        if a <= c and c <= z:
            return True
        elif A <= c and c <= Z:
            return True
        elif zero <= c and c <= nine:
            return True
        else:
            return False
        