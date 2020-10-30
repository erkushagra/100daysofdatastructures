def binsearch(arr,low,high,val):
    if low <= high:
        mid = (low+high)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]<val:
            return binsearch(arr,mid+1,high,val)
        else:
            return binsearch(arr,low,mid,val)
    else:
        return -1
def linearsearch(arr,val):
    for i in range(len(arr)):
        if arr[i]==val:
            return i
    return -1
print('Enter the lenght of an array')
n = int(input())
print('Enter an array')
arr = list(map(int, input().split()))
print("Enter the value to be searched in an array")
x = int(input())
print(binsearch(arr,0,n-1,x))
print(linearsearch(arr,x))
        
