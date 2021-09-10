lst=['abc', 'aba', '1221', 'xyz']
c=0

for i in lst:
    if i==i[::-1]:
        c+=1
print(c)