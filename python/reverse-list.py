#-> REVERSE THE LIST


def rev(l,start,end):
    while start <= end:
        l[start], l[end] = l[end], l[start]
        start = start + 1
        end = end - 1



# def rev_v2(l):
#     return l[::-1]


l=[1,2,3,4]
print(l)
rev(l,0,len(l)-1)
print(l)
# rev_v2(l)
# print(l)
# print("Reversed (new list):", rev_v2(l))



