def insertionSort(arr):
	'''
	Time Complexity : O(N^2)
	Space Complexity : O(1)
	'''
	for i in range(1,len(arr)):
		curr=arr[i]
		j=i-1
		while(j>=0 and curr<arr[j]):
			arr[j+1]=arr[j]
			j-=1
		arr[j+1]=curr
	return arr

arr=[9,4,3,2,5,1,6,7]
print(insertionSort(arr))

#Code Link : https://ideone.com/Kic721
