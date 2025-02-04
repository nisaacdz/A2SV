class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longestLen = len(strs[0])
        for word in strs:
            longestLen = min(len(word), longestLen)
            for i in range(longestLen):
                if word[i] != strs[0][i]:
                    longestLen = i
                    break
        return strs[0][:longestLen]
