n = int(input())
arr = list(map(int, input().split()))

def MergeSort(arr, n):
    mid = (n)//2
    if n > 1:
        l = arr[:mid]
        r = arr[mid:]
        l = MergeSort(l, mid)
        r = MergeSort(r, n-mid-1)
        arr = l + r
    a = Merge(arr, n, mid)
    return a

def Merge(a, n, mid):
    i = 0
    j = mid
    b = a[:]
    k = 0
    while i < mid and j < n :
        if a[i] < a[j]:
            b[k] = a[i]
            i += 1
            k += 1
        else:
            b[k] = a[j]
            j += 1
            k += 1
    while i < mid:
        b[k] = a[i]
        k += 1
        i += 1
    while j < n :
        b[k] = a[j]
        j += 1
        k += 1
    return b

print(MergeSort(arr, n))