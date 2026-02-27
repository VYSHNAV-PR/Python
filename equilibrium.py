nums = list(map(int,input("Enter numbers:").split()))

total_sum = sum(nums)
left_sum = 0
equilibrium_index = 0

for i in range(len(nums)):
    right_sum = total_sum - left_sum - nums[i]
    
    if left_sum == right_sum:
        equilibrium_index = i
        break
    
    left_sum += nums[i]

print("Equilibrium Index:", equilibrium_index)