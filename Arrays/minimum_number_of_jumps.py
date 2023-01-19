#User function Template for python3
class Solution:
    def minJumps(self, arr, n):
        jump=1
        maxi=arr[0]
        steps=arr[0]
        if(n==1):
            return 0
        elif(arr[0]==0):
            return -1
        else:
            for i in range(1,n):
                if(i==n-1):
                    return jump
                maxi=max(maxi,arr[i]+i)
                steps-=1
                if(steps==0):
                    jump+=1
                    if(maxi<=i):
                        return -1
                    steps=maxi-i