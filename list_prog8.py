def cloning(lst1):
    lst_copy=lst1[:]
    return lst_copy

    lst1=[2,4,23,433,4,3]
    lst2=cloning(lst1)
    print("original list:" , lst1)
    print("after cloning list:", lst2)