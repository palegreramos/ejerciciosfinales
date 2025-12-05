nums=[]
for i in range(1,101):
    nums.append(i)
print(nums)
nums.reverse()
print(nums)
print(",".join(map(str,nums)))