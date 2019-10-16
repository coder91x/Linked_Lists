def binary_search(arr, l , r , x):
    if l <= r:
        mid = l + (r-l)/2
        if arr[mid] == x:
            return mid
        elif x < arr[mid]:
            return binary_search(arr , l, mid-1, x)
        else:
            return binary_search(arr, mid+1 , r, x)
    else:
        return -1

arr = [1,4,7,45,78,90]
l = 0
r = len(arr) - 1
x = 90
if x in arr:
    print("Element is present at "+str(arr.index(x)))
else:
    print("-1")
