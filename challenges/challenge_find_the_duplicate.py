def find_duplicate(nums):
    for num in nums:
        if not isinstance(num, int) or num < 1:
            return False

    nums.sort()

    for i in range(len(nums) - 1):
        if nums[i] == nums[i+1]:
            return nums[i]

    return False
