lst=[2,3,4,6,7,7,8]
print("original list:"+ str(lst))

flag=0
flag=len(set(lst))==len(lst)

if flag:
    print("list contains all unique elements")
else:
    print("list does not contain all unique elements")