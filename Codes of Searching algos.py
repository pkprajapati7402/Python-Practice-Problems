# Linear Search 
 
nums = [12, 34, 21, 23, 44, 56];
target = 23 
position = -1
for index in range(len(nums)):
    if nums[index] == target:
        position = index 
        break 
 
if position == -1:
    print("Target not found")
else:
    print("Target found at position: ", position)
 
# Binary Search 
 
nums = [12, 34, 21, 23, 44, 56];
target = 23
nums = sorted(nums)
left, right = 0, len(nums) - 1 
found = False
 
while left <= right:
    mid = (left + right) // 2 
    if nums[mid] == target:
        found = True 
        break 
    elif nums[mid] < target:
        left = mid + 1 
    else:
        right = mid - 1 
 
if found == True:
    print("Target found")
else:
    print("Target Not found")