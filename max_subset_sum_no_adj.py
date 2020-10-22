"House Robber I "
class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        
        total_so_far = []
        total_so_far.append(nums[0])
        total_so_far.append(max(nums[0], nums[1]))
        
        for i in range(2, len(nums)):
            total_so_far.append(max(total_so_far[i-1], total_so_far[i-2] + nums[i]))
        return total_so_far[-1]