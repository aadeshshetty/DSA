def findDuplicate(nums):
  slow=0
  fast=0
  while(True):
    slow=nums[slow]
    fast=nums[nums[fast]]
    if(slow==fast):
      break
  fast=0
  while(True):
    slow=nums[slow]
    fast=nums[fast]
    if(slow==fast):
      return slow

arr= [1,3,4,2,2]
print(findDuplicate(arr))

#Time Complexity : O(N)
#Space Complexity: O(1)