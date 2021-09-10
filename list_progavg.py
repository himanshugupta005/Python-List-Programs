def average_two_lists(num1,num2):
 result=sum(num1+num2)/len(num1+num2)
 return result

num1=[1,1,2,3,4,5,4,3]
num2=[0,3,4,2,4,5,44,3]
print(num1)
print(num2)

print("\nAverage of two lists:")
print(average_two_lists(num1,num2))