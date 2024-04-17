def twoSum(nums, target):
    my_dict = {}
    for i in range(len(nums)):
        temp = target - nums[i]
        if temp in my_dict:
            return [nums.index(temp),i]
        my_dict[nums[i]] = i
    return []

print(twoSum([1,8], 9))