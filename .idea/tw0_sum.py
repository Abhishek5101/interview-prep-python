def two_sum(nums, target):
    seen = {}
    for i in range(len(nums)):
        if target - nums[i] in seen:
            print(seen)
            return [seen[target-nums[i]], i]
        else:
            seen[nums[i]] = i
    return []

print(two_sum([3,2,4], 6))