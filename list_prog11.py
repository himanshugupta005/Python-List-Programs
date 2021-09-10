colour=['red','green','white','black','pink','yellow']
colour=[x for (i,x) in enumerate(colour) if i not in (0,4,5)]
print(colour)