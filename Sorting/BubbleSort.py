def bubbleSort(arr):
	'''
	Time Complexity : O(N^2)
	Space Complexity : O(1)
	'''
	for i in range(len(arr)):
		for j in range(i+1,len(arr)):
			if(arr[i]>arr[j]):
				arr[i],arr[j]=arr[j],arr[i]
	return arr

arr=[9,4,3,2,5,1,6,7]
print(bubbleSort(arr))

# Code Link: https://ideone.com/rrKGUA