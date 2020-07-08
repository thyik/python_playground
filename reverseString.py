class Solution:

    def reverseString(self, s):
        s.reverse()


if __name__ == "__main__":
    sln = Solution()
    arrayStr = ["a","p", "p", "l", "e"]
    res = sln.reverseString(arrayStr)

    print(res)
