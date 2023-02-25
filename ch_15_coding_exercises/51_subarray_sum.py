def subarray_sum(nums, target):
    result = {}
    
    for i in range(len(nums)):
        cum_sum = nums[i]
        if cum_sum == target:
            return [i, i]
        for k in range(i+1, len(nums)):
            if cum_sum + nums[k] != target:
                cum_sum += nums[k]
                continue
            elif cum_sum + nums[k] == target:
                result[i]=k
                # print(f"Original nums: {nums}. Target: {target}. Sum indexes {i} through {k} = {sum(nums[i:k+1])}")
                return [i, k]

    return []


nums = [1, 2, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )

nums = [-1, 2, 3, -4, 5]
target = 0
print ( subarray_sum(nums, target) )

nums = [2, 3, 4, 5, 6]
target = 3
print ( subarray_sum(nums, target) )

nums = []
target = 0
print ( subarray_sum(nums, target) )



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []

"""
