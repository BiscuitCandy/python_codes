n = int(input())
i = 0 
j = 0
m = 1
pp = [(0, 0), ]
arr = [[0 for i in range(n)] for j in range(n)]
while i < n//2 + 1 and m <= n**2:
    j = 0
    while j < 5 and m <= n**2:
        if  j == 0:
            for k in range(i, n-i) :
                arr[i][k] = m
                if m%11 == 0 :
                    pp.append((i,k))
                m += 1
        elif j == 1 :
            for k in range(i+1, n-i) :
                arr[k][n-i-1] = m
                if m%11 == 0 :
                    pp.append((k,n-i-1))
                m += 1
        elif j == 2 :
            for k in range(n-i-2, i-1, -1) :
                arr[n-i-1][k] = m
                if m%11 == 0 :
                    pp.append((n-i-1,k))
                m += 1
        elif j == 3 :
            for k in range(n-i-2, i, -1) :
                arr[k][i] = m
                if m%11 == 0 :
                    pp.append((k,i))
                m += 1
        j += 1
    i += 1

for i in arr:
    print(*i, sep= "\t")