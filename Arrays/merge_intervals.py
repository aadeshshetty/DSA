def mergeIntervals(arr):
    arr.sort()
    i=0
    while(i<len(arr)-1):
        if(arr[i][1]>=arr[i+1][0] and arr[i][1]>=arr[i+1][1]):
            arr.append([arr[i][0],arr[i][1]])
            arr.remove(arr[i])
            arr.remove(arr[i])
            arr.sort()
        elif(arr[i][1]>=arr[i+1][0] and arr[i][1]<arr[i+1][1]):
            arr.append([arr[i][0],arr[i+1][1]])
            arr.remove(arr[i])
            arr.remove(arr[i])
            arr.sort()
        else:
          i+=1
    return arr


arr=[[1,3],[2,6],[8,10],[15,18]]
print(mergeIntervals(arr))

#Time Complexity : O(Nlogn + N)
#Space Complexity : O(N)