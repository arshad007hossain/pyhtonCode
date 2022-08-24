arr = [12,56,5,2,6,5,65,2,3,65,32,65,362,65,652,62]

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i+1
    return -1
x = int(input())
result = linear_search(arr,x)

if (result == -1):
    print('item not found')

else:
    print('item found at postion ',result)


