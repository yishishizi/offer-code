class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.replace(' ','%20')
        return s