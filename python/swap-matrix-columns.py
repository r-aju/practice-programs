def swap_cols(L,m,n,x,y):
    for i in range(m):
        L[i][x-1], L[i][y-1] = L[i][y-1], L[i][x-1]

def print_matrix(L,m,n):
    for i in range(m):
        for j in range(n):
            print(L[i][j], end = "")
        print()

def read_ele(L,m,n):
    for i in range(m):
        tempL = [int(i) for i in input().split()]
        l1.append(tempL)


m = int(input("enter the number of rows"))
n = int(input("enter the number of columns"))

l1 = []

read_ele(l1,m,n)
print("BEFORE SWAPPING")
print_matrix(l1,m,n)
print("AFTER SWAPPING")
swap_cols(l1,m,n,1,2)
print_matrix(l1,m,n)
