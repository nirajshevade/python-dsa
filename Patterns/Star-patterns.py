class Solution:
    def pattern1(self, n):
        n = int(input())
        for i in range(0, n):
            for j in range(0, n):
                print("*", end = "")
            print()
pattern1 = Solution()
pattern1.pattern1(6)
pattern1.pattern1(15)

pattern1.pattern1(4)