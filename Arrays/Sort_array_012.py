#Sort an array of 0s, 1s and 2s

class Solution:
    def sort012(self,a,n):
        l=0
        m=0
        h=n-1
        while(m<=h):
            if(a[m]==0):
                a[l],a[m]=a[m],a[l]
                l+=1
                m+=1
            elif(a[m]==1):
                m+=1
            else:
                a[h],a[m]=a[m],a[h]
                h-=1

if __name__ == '__main__':
    n=int(input())
    arr=[int(x) for x in input().strip().split()]
    ob=Solution()
    ob.sort012(arr,n)
    for i in arr:
        print(i, end=' ')
    print()
