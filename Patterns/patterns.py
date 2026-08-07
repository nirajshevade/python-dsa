class Solution:
    def pattern1(n):
        '''
        * * *
        * * *
        * * *
        '''
        print("This wil pattern number 1")
        for i in range(0, n):
            for j in range(0, n):
                print("*", end = " ")
            print()

    def pattern2(n):
        '''
        *
        * *
        * * *
        '''
        print("This wil pattern number 2")
        for i in range(0, n+1):
            for j in range(0, i):
                print("*", end=" ")
            print()

    def pattern3(n):
        '''
        1
        1 2
        1 2 3
        '''
        print("This wil pattern number 3")
        for i in range(0, n+1):
            for j in range(1, i+1):
                print(j, end = " ")
            print()

    def pattern4(n):
        '''
        1
        2 2
        3 3 3
        '''
        print("This wil pattern number 4")
        for i in range(0, n+1):
            for j in range(0, i):
                print(i, end = " ")
            print()

    def pattern5(n):
        '''
        * * *
        * *
        *
        '''
        print("This wil pattern number 5")
        for i in range(n,0,-1):
            for j in range(i,0,-1):
                print("*" , end = " ")
            print()

    def pattern6(n):
        '''
        1 2 3
        1 2
        1
        '''
        print("This wil pattern number 6")
        for i in range(n,0,-1):
            for j in range(1,i+1):
                print(j , end = " ")
            print()
    
    def pattern7(n):
        '''
            *
          * * *
        * * * * *
        '''
        print("This wil pattern number 7")
        # space - star - space 
        for i in range(0, n):
            #space
            for j in range(0, n - i - 1):
                print(end=" ")
            #stars
            for j in range(0, 2*i+1):
            
                print("*", end ="")
            
            #space
            for j in range(0, n - i - 1):
                print(end=" ")
            print()


    def pattern8(n):
        '''
        * * * * *
          * * *
            *
         
        '''
        print("This wil pattern number 8")
        for i in range(0,n):
            #space
            for j in range(0,i):
                print(end=" ")
            #star
            for j in range(0, 2*n-(2*i+1)):
                print("*",end="")
            #space
            for j in range(0,i):
                print(end=" ")
            print()


    def pattern9(n):
        '''
           *
          * *
         * * *
          * *
           *
        '''
        print("This wil pattern number 9")
        # space - star - space 
        for i in range(0, n):
            #space
            for j in range(0, n - i - 1):
                print(end=" ")
            #stars
            for j in range(0, 2*i+1):
            
                print("*", end ="")
            
            #space
            for j in range(0, n - i - 1):
                print(end=" ")
            print()


        for i in range(0,n):
            #space
            for j in range(0,i):
                print(end=" ")
            #star
            for j in range(0, 2*n-(2*i+1)):
                print("*",end="")
            #space
            for j in range(0,i):
                print(end=" ")
            print()


    def pattern10(n):
        '''
        *
        * *
        * * *
        * *
        *
        '''
        print("This wil pattern number 10")
        for i in range(0, n+1):
            for j in range(0, i):
                print("*", end=" ")
            print()
        
        for i in range(n-1,0,-1):
            for j in range(i,0,-1):
                print("*" , end = " ")
            print()


    def pattern11(n):
        '''
        1
        0 1
        1 0 1
        0 1 0 1
        '''
        print("This wil pattern number 11")
        for i in range(0, n+1):
            for j in range(0, i):
                print((i + j + 1)%2, end=" ")
            print()

    def pattern12(n):
        '''
        1         1
        1 2     2 1
        1 2 3 3 2 1
        '''
        print("This wil pattern number 12")
        # num - space - num
        for i in range(1,n +1):
            #num
            for j in range(1, i+1):
                 
                print(j, end = " ")
            #space
            for j in range(2 * (n - i)):
                print(" ", end=" ")
            #num
            for j in range(i, 0, -1):
                print(j, end = " ")
            print()
    
    def pattern13(n):
        '''
        1
        2 3
        4 5 6
        7 8 9 10
        '''
        print("This wil pattern number 13")
        num = 1
        for i in range(1,n+1):
            for j in range(0,i):
                print(num, end = " ")
                num += 1
            print()

    def pattern14(n):
        '''
        A
        A B
        A B C
        A B C D
        '''
        print("This wil pattern number 14")
        for i in range(1, n + 1):
            for j in range(i):
                print(chr(65 + j), end=" ")
            print()

    def pattern15(n):
        '''
        A B C
        A B
        A
        '''
        print("This wil pattern number 15")
        for i in range(n,0,-1):
            for j in range(i):
                print(chr(65 + j), end=" ")
            print()

    def pattern16(n):
        '''
        A
        B B
        C C C
        '''
        print("This wil pattern number 16")
        for i in range(0, n):
            for j in range(0, i+1):
                print(chr(65 + i), end=" ")
            print()

    def pattern17(n):
        '''
            A    
          A B A
        A B C B A
        '''
        print("This wil pattern number 17")
        # space - dig - sapce
        for i in range(0, n):
            #space
            for j in range(0, n-i-1):
                print(" ", end="")
            #increasing digit
            for j in range(0, i+1):
                print(chr(65 + j), end="") 
            #decrsing diigit with space
            for j in range(i-1,-1,-1):
                print(chr(65+j),end = "")

            print()
    if __name__ == "__main__":

        n = int(input())

        pattern1(n)
        print("===================================================================================")
        pattern2(n)
        print("===================================================================================")
        pattern3(n)
        print("===================================================================================")
        pattern4(n)
        print("===================================================================================")
        pattern5(n)
        print("===================================================================================")
        pattern6(n)
        print("===================================================================================")
        pattern7(n)
        print("===================================================================================")
        pattern8(n)
        print("===================================================================================")
        pattern9(n)
        print("===================================================================================")
        pattern10(n)
        print("===================================================================================")
        pattern11(n)
        print("===================================================================================")
        pattern12(n)
        print("===================================================================================")
        pattern13(n)
        print("===================================================================================")
        pattern14(n)
        print("===================================================================================")
        pattern15(n)
        print("===================================================================================")
        pattern16(n)
        print("===================================================================================")
        pattern17(n)
        print("===================================================================================")