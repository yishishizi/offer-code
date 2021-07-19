class Solution:
    def reverseLeftWords(self, s, n):
        return s[n:]+s[:n]
        # res = []
        # for i in range(n, n + len(s)):
        #     res.append(s[i % len(s)])
        # return ''.join(res)

        # res = ""
        # for i in range(n, len(s)):
        #     res += s[i]
        # for i in range(n):
        #     res += s[i]
        # return res



if __name__ == "__main__":
    S=Solution()
    s = "lrloseumgh"
    k = 6
    print(S.reverseLeftWords(s,k))
