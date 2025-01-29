#-> swap first and last element in the list


def fun(l):
    l[0], l[-1] = l[-1], l[0]

l = [ 1,2,3,4]
print(l)
fun(l)
print(l)
