n = int(input())
# This theorem produecs all the primes till n in O(n Loglogn) complexity
arr = [True] * n
arr[0] = False
for i in range(2, int(n**(1/2))+1):
    if arr[i-1]:
        for x in range(i*i, n+1, i):
            if arr[x-1]:
                arr[x-1] = False
for i in range(1, n+1):
    if arr[i-1] : print(i, end =" ")

