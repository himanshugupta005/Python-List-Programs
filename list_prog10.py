def common_ele(lst1,lst2):
    result=False

    for x in lst1:

        for y in lst2:

            if x==y:
                result=True
                return result

    return result

lst1=[2,3,43,4]
lst2=[2,5,3,88]
print(common_ele(lst1,lst2))

lst1=[2,4,32,3]
lst2=[5,99,77,100]
print(common_ele(lst1,lst2))