def find_value(nums: list[int] | range, value: int) -> bool:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == value:
            return True
        elif left == right:
            return nums[left] == value
        elif nums[mid] < value:
            left = mid + 1
        else:
            right = mid - 1

    return False
