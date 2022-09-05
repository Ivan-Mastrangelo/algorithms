def find_duplicate(nums):
    """Faça o código aqui."""
    if len(nums) < 2 or nums is None:
        return False
    nums.sort()
    for i in range(len(nums) - 1):
        if isinstance(nums[i], str) or nums[i] < 0:
            return False
        elif nums[i] == nums[i - 1]:
            return nums[i]
    return False
