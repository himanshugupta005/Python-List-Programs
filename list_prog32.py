from itertools import cycle

lst1=[2,3,4,5,6]
lst2=[4,5,6,6,4]

output=[x+y for x,y in zip(cycle(lst1),lst2)]
print(output)
