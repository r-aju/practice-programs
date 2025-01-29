# -> INDEX OF GIVEN ELEMENT



def index_of_ele(l,x):
    for i in range(len(l)):
        if x == l[i]:
            return i
    return None

            
l = [1,2,3,4]
x=3
print(index_of_ele(l,x))



