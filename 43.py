class Solution:
    def firstUniqChar(self, s):
        if len(s) == 0: return " "
        dic = []
        visited=[]
        for i in s:
            if i not in dic:
                if i not in visited:
                    dic.append(i)
            else:
                dic.remove(i)
                visited.append(i)
        if len(dic) == 0: return " "
        return dic[0]
        #
        # dic={}
        # for i in s:
        #     if i in dic:
        #         dic[i]=not i in dic
        # for k,v in dic.items():
        #     if v is True:
        #         return k
        # return " "

if __name__ == "__main__":
    S=Solution()
    ss="aadadaad"
    print(S.firstUniqChar(ss))

