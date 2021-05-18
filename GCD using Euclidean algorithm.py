nums = [int(input(f'Enter number {i+1}: ')) for i in range(2)]
while True:
   if nums[0] == nums[1]:
      break
   elif nums[0] > nums[1]:
      nums[0] = nums[0] - nums[1]
   else:
      nums[1] = nums[1] - nums[0]

print(nums[0])
   
