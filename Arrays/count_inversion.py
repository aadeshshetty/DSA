#Find the Inversion Count in the array.

class Solution:
    def merge(self,arr,l,r,mid,n):
        i=0
        j=0
        k=0
        cnt=0
        while(i<mid and j<n):
            if l[i]<=r[j]:
                arr[k]=l[i]
                i+=1
            else:
                arr[k]=r[j]
                cnt+=mid-i
                j+=1
            k+=1
        while(i<mid):
            arr[k]=l[i]
            i+=1
            k+=1
        while(j<n):
            arr[k]=r[j]
            j+=1
            k+=1
        return cnt
    
    def mergesort(self,arr,n):
        if(n<=1):
            return 0
        mid=n//2
        l=arr[:mid]
        r=arr[mid:]
        c=0
        c+=self.mergesort(l,mid)
        c+=self.mergesort(r,n-mid)
        c+=self.merge(arr,l,r,mid,n-mid)
        return c
        
    def inversionCount(self, arr, n):
        return self.mergesort(arr,n)


if __name__=='__main__':
    n = int(input())
    a = list(map(int, input().strip().split()))
    obj = Solution()
    print(obj.inversionCount(a,n))

#Time Complexity : O(nlogn)
#Space Complexity : O(n)