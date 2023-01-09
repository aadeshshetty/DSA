#find the sum of contiguous subarray with maximum sum.
class Solution:
    def maxSubArraySum(self,arr,N):
        sum=0
        ans=arr[0]
        for i in range(N):
            sum+=arr[i]
            if(sum<0):
                sum=0
            if(sum>ans):
                ans=sum
        if(ans>0):
            return ans
        return max(arr)

def main():
    n=int(input())
    arr=[int(x) for x in input().strip().split()]
    ob=Solution()
    print(ob.maxSubArraySum(arr,n))


if __name__ == "__main__":
    main()

#Time Complexity: O(N)
#Space Complexity: O(1)