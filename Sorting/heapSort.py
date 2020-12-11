n = int(input())
arr = list(map(int, input().split()))

def heapify(arr, n):
    i = 0
    while 2*i + 1 <= n -1 and 2*i + 2 <= n - 1:
        l = 2*i + 1
        r = 2*i + 2
        g = l if arr[l] > arr[r] else r
        if arr[g] > arr[i]:
            arr[g], arr[i] = arr[i], arr[g]
            heapify(arr, n)
        i += 1
    

print(heapify(arr,n))
print(arr)