n = int(input())
arr = list(map(int, input().split()))

def QuickSort(arr, low, high):
    if high > low:
        pivot = arr[high]
        i = low -1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        i += 1
        arr[i], arr[high] = arr[high], arr[i]
        pi = i
        QuickSort(arr, low, pi-1)
        QuickSort(arr, pi+1, high)
    #return arr

QuickSort(arr, 0, n-1)
print(*arr)
#
  