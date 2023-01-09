class Solution:
    def getMinDiff(self, arr, n, k):
        arr.sort()
        ans=arr[n-1]-arr[0]
        s=arr[0]+k
        l=arr[n-1]-k
        
        for i in range(n-1):
            mi=min(s,arr[i+1]-k)
            ma=max(l,arr[i]+k)
            if(mi<0):
                continue
            ans=min(ans,ma-mi)
        return ans

if __name__ == '__main__':
    k = int(input())
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ob = Solution()
    ans = ob.getMinDiff(arr, n, k)
    print(ans)

#Time Complexity : O(NlogN)
#Space Complexity : O(1)