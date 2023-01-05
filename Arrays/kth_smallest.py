class Solution:
    def partition(self,arr,l,r,p):
        i=l
        j=l
        while(i<=r):
            if(arr[i]<=p):
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
                j+=1
            else:
                i+=1
        return j-1
        
    def kthSmallest(self,arr, l, r, k):
        pivot=arr[r]
        ans=self.partition(arr,l,r,pivot)
        if(ans<k-1):
            return self.kthSmallest(arr,ans+1,r,k)
        elif(ans>k-1):
            return self.kthSmallest(arr,l,ans-1,k)
        else:
            return arr[ans]

if __name__ == '__main__': 
    n=int(input())
    arr=list(map(int,input().strip().split()))
    k=int(input())
    ob=Solution()
    print(ob.kthSmallest(arr, 0, n-1, k))