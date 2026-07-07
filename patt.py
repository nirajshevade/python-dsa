class Solution:
    def pattern3(self, n):
        width = len(str(n * n)) + 1
        
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                print(f"{i*j:^{width}}", end="")
            print()

pattern3 = Solution()
pattern3.pattern3(30)            