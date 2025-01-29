def element(l,x):
  ll=[]
  for i in l:
    if i < x:
      ll.append(i)

  return ll

l = [1,2,3,4,5,6,7,8,9,10]
x=10
print(elem(l,x))
