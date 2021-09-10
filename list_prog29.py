def sum_range_list(nums,m,n):
    sum_range=0
    for i in range(m,n+1,1):
        sum_range+=nums[i]
    return sum_range

nums=[2,1,5,6,8,3,4,9,10,11,8,12]
print("original list")
m=8
n=10
print("range:", m,",",n)
print("\nSum of the specified range:")
print(sum_range_list(nums,m,n))