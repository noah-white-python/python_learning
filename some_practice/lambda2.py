nums = [-5,3,-1,-2,4]
reverse = lambda i : abs(i)
sortedNums = sorted(nums,key=reverse)
print(sortedNums)