
def read(L,m,n):
    for i in range(m):
        TL = [ int(i) for i in input().split()]
        L.append(TL)


def printm(L,m,n):
    for i in range(m):
      for j in range(n):
        print(L[i][j], end="")
      print("")


def sumofelements(L,m,n):
    s=0                                
    for i in range(m):            #rows# ex -> the matrix is [1 2 3, 4 5 6, 7 8 9] m=3, number of rows.  i=0,1,2
                                                #i=0, points to the first row [1 2 3] =-> 1+2+3=6 s=s+i s=0+6 s =6
                                                #i=1, points to the second row [4 5 6] =-> 4+5+6=15 s=6+15 =21
                                                  #....
                                                    #...
        s = s+sum(L[i])
    return s





m = int(input("enter the number of rows"))
n = int(input("enter the number of columns"))
L = []

read(L,m,n)
printm(L,m,n)
print("Sum of elements:", sumofelements(L, m, n))


