class Solution:
    def lengthOfLongestSubstring(self, s):
        if len(s)==0:return
        left=-1
        right=0
        max_length=0
        n=len(s)
        dic={}
        for i in range(n):
            if s[i] in dic:
                left = max(left, dic[s[i]])
            dic[s[i]]=i
            max_length = max(max_length, right - left)
            right+=1
        return max_length
        # if len(s)==0:return 0
        # i=-1
        # max_length=0
        # n=len(s)
        # dic={}
        # for j in range(n):
        #     if s[j] in dic:
        #         i = max(i, dic[s[j]])
        #     dic[s[j]]=j
        #     max_length = max(max_length, j-i)
        # return max_length




if __name__ == "__main__":
    S=Solution()
    s="abcabcbb"
    print(S.lengthOfLongestSubstring(s))