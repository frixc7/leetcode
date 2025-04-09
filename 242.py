# SOLUTION 1

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashtable1 = {}
        for c in set(s):
            hashtable1[c] = s.count(c)
        
        hashtable2 = {}
        for c in set(t):
            hashtable2[c] = t.count(c)

        return True if hashtable1 == hashtable2 else False

# SOLUTION 2
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashtable = {}
        for c in set(s):
            hashtable[c] = s.count(c)
        
        for c in set(t):
            if c not in hashtable or hashtable[c] != t.count(c):
                return False

        return True
