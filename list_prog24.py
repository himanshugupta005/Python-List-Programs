lst=[2,9,3,4,5]
print("original list:" +str(lst))

flag=0
if lst==sorted(lst):
    flag=1
if flag:
    print("yes, list is sorted")
else:
    print("no, list is not sorted")