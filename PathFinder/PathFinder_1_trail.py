import random as rand

def min(a,x,y,n):
    if x+1 != n and y+1 != n :
        if a[x+1][y] != a[x][y+1]:
            if (a[x+1][y]<a[x][y+1]):
                 return [x+1,y]
            else : return [x,y+1]
        else:
            if a[min(a,x+1,y,n)[0]][min(a,x+1,y,n)[1]] < a[min(a,x,y+1,n)[0]][min(a,x,y+1,n)[1]] :
                return [x+1,y]
            elif a[min(a,x+1,y,n)[0]][min(a,x+1,y,n)[1]] > a[min(a,x,y+1,n)[0]][min(a,x,y+1,n)[1]] :
                return [x,y+1]
            else :
                return [x+1,y+1]
    elif x+1 == n :
            return [x,y+1]
    else : return [x+1,y]


n = int(input("Enter the size of Maze 'NxN'"))
M = [[rand.randint(1,9)for j in range(n)] for i in range(n)]
    
print("The Randomly generated matrix is :")
for j in range(n):
    for i in range(n) :
        print(M[i][j], end =" ") 
    print()

a = l = int(input("Enter start X-coordinate"))-1
b = m = int(input("Enter start Y-coordinate"))-1

len = M[a][b]
M[a][b] = 0

x = int(input("Enter End X-coordinate"))-1
y = int(input("Enter End Y-coordinate"))-1

len = len + M[x][y]
M[x][y] = -1

cp = 0

while(cp != -1):
    if ((x == l and y == m+1) or (x == l+1 and y == m)):
        
        cp = -1
        
    else :
        k = min(M,l,m,n)
        len = len + M[k[0]][k[1]]
        M[k[0]][k[1]] = 0
        l = k[0]
        m = k[1]
        
print("The path created from start to end is denoted with '0' where '-1' represents the end:")
for j in range(n):
    for i in range(n) :
        print(M[i][j], end =" ") 
    print()
    
print("The length of path is :",len)
