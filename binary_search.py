def binarySearch(arr, item, low, high):
    while(low<=high):
        mid = low + (high-low)//2
        if arr[mid]==item:
            return mid
        elif arr[mid] < item:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [12,56,5,2,6,5,65,2,3,65,32,65,362,65,652,62]
arr.sort()

total = 0
givenNumber = int(input())
for i in arr:
    if i==givenNumber:
        total+=1

x = int(input())
result = binarySearch(arr,x,0,len(arr)-1)

if (result != -1):
    print('item has found at index', result)
else:
    print('Not Found')

print(f'{givenNumber} is appear here {total} times')

    
