lst1=[2,4,5,6]
lst2=[2,5,77,99]

print("original list:" + str(lst1))
print("original list:" +str(lst2))

res=lst1+lst2
res[::2]=lst1
res[1::2]=lst2

print("the  interleaved list is:" +str(res))
    
