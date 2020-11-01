def minNumberOfCoinsForChange(n, denoms):
	nums = [float("inf") for amount in range(n+1)]
	nums[0] = 0
	for denom in denoms:
		for amount in range(len(nums)):
			if denom <= amount:
				nums[amount] = min(nums[amount], nums[amount - denom] +1 )
	return nums[n] if nums[n] != float("inf") else - 1
