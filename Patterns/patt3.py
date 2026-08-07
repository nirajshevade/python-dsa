class Solution:
        def pattern3(self, n):
            while(n > 0):  
                n = int(input())  
                for i in range(1,n+1):

                    for j in range(1,i+1):
                        print(j, end = " ")
                    print()

pattern3 = Solution()   
pattern3.pattern3(6)