def differnce(lst1,lst2):
    return list(set(lst1)-set(lst2))

lst1=[2,33,4,5,5]
lst2=[1,33,456,54,3]
print(differnce(lst1,lst2))