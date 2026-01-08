def selection_sort(nums):
    n = len(nums)
    for i in range(0, n):
        smallest = i
        for j in range(i + 1, n):
            if nums[smallest] > nums[j]:
                smallest = j
        nums[i], nums[smallest] = nums[smallest], nums[i]
    return nums