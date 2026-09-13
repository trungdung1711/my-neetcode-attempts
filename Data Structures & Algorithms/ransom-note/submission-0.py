class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        # i
        # ransomNote and magazine
        # true if ransomNone can be constructed
        # using letters from magazine
        # false otherwise

        # o
        # true if ransomNote can be constructed
        # from letters from magazine
        # false otherwise

        # c
        # len(ransomNote), len(magazine) >= 1 <= 10^5
        # ransomNote and magazine lowercase letters

        # e
        # len(magazine) < len(ransomNote) -> False

        if len(magazine) < len(ransomNote):
            return False

        s = Counter(magazine)

        for c in ransomNote:
            if c not in s:
                return False

            # inside
            if c in s and s[c] == 0:
                return False

            if c in s and s[c] > 0:
                s[c] -= 1

        return True