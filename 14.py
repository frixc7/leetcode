class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) > 1:
            shortest = min(strs, key=len)
            for i in range(len(shortest)):
                for string in strs:
                    if string[i] != shortest[i]:
                        return shortest[:i]
            return shortest
        return strs[0]
