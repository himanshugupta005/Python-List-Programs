def most_frequent(list):
    return max(set(list),key=list.count)

list=[2,2,2,6,8]
print(most_frequent(list))