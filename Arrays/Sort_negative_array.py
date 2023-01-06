#Move all negative numbers to beginning and positive to end with constant extra space

class Solution:
    def sortNegativeArray(self,a,n):
        l=0
        h=n-1
        while(l<h):
            if(a[l]<0):
                l+=1
            elif(a[h]>0):
                h-=1
            else:
                a[h],a[l]=a[l],a[h]
                h-=1
                l+=1

if __name__ == '__main__':
    n=int(input())
    arr=[int(x) for x in input().strip().split()]
    ob=Solution()
    ob.sortNegativeArray(arr,n)
    for i in arr:
        print(i, end=' ')
    print()


# Time Complexity : O(N)
# Space Complexity : O(1)