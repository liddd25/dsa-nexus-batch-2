class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        x = min(strs)
        y = max(strs)
        if not strs and not x:
            return ''
        for i in range(len(x)):
            if x[i] != y[i]:
                return y[:i]
        return x[:]
