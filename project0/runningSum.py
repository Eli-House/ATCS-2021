
n = [3,1,2,10,1]
numAdd = []


def runningSum(nums):
    total = 0
    for i in nums:
        total = total + nums[i - 1]
        numAdd.append(total)
    return numAdd

print(runningSum(n))




