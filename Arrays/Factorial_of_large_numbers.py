class Node:
    def __init__(self,val):
        self.val= val
        self.prev=None


class Solution:
    
    def fact(self,tail,i):
        temp=tail
        prevNode=tail
        carry=0
        while(temp!=None):
            s=temp.val*i+carry
            temp.val=s%10
            carry=s//10
            prevNode=temp
            temp=temp.prev
        while(carry!=0):
            prevNode.prev=Node(carry%10)
            carry=carry//10
            prevNode=prevNode.prev
    
    def printN(self,tail):
        if(tail==None):
            return
        self.printN(tail.prev)
        print(tail.val,end='')
    
    def factorial(self, N):
        tail = Node(1)
        for i in range(2,N+1):
            self.fact(tail,i)
        self.printN(tail)


if __name__ == '__main__':
    N = int(input())
    ob = Solution()
    ob.factorial(N)

#Time Complexity : O(N^2)
#Space Complexity: O(1)