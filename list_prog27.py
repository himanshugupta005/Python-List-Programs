def prod(val):
    res=1
    for ele in val:
        res *=ele
    return res

lst=[10,20,20,40,20,50,60,40]
print("original list is:"+ str(lst))

res=prod(list(set(lst)))
print("the unique elements product:" +str(res))

