import random

#Min function min(curr_x,curr_y,n,m)
def min(a,x,y,n,m):     # finds the minimum next step 
    if x+2 <= n and y+2 <= m :
        if a[x+1][y] != a[x][y+1]:
            if (a[x+1][y]<a[x][y+1]):
                 return [x+1,y]
            else : return [x,y+1]
        else:
            if a[min(a,x+1,y,n,m)[0]][min(a,x+1,y,n,m)[1]] < a[min(a,x,y+1,n,m)[0]][min(a,x,y+1,n,m)[1]] :
                return [x+1,y]
            elif a[min(a,x+1,y,n,m)[0]][min(a,x+1,y,n,m)[1]] > a[min(a,x,y+1,n,m)[0]][min(a,x,y+1,n,m)[1]] :
                return [x,y+1]
            else :
                return [x+1,y+1]
    elif x+1 == n :
        return [x,y+1]
    elif y+1 == m :
        return [x+1,y]

# Header
print("-------------------------------------------------------------------")
print("***************************Path Finder*****************************")
print("-------------------------------------------------------------------")
# Enter the size of Matrix
n = int(input("Enter no.of rows"))
m = int(input("Enter no.of columns"))
# create a random matrix of size n*m
M = [[random.randint(0,9) for i in range(0,m)] for j in range(0,n)]
# Display the generated .matrix
for i in range(n):
    for j in range(m) :
        print(M[i][j], end =" ") 
    print()
# Enter the start point
curr_x_coor = start_X_coor = int(input("Enter the starting X-coordinate"))-1
curr_y_coor = start_y_coor = int(input("Enter the starting Y-coordinate"))-1
lenght = M[start_X_coor][start_y_coor]
M[start_X_coor][start_y_coor] = '*'
# Enter the end point
end_x_coor = int(input("Enter the Ending X-coordinate"))-1
end_y_coor = int(input("Enter the Ending Y-coordinate"))-1
lenght += M[end_x_coor][end_y_coor]
M[end_x_coor][end_y_coor] = '*'
# Find the Path
if (end_x_coor >= start_X_coor and end_y_coor >= start_y_coor) :

    cp = 0  # the control key of the maze
    while(cp != -1):
        if ((end_x_coor == curr_x_coor and end_y_coor == curr_y_coor+1) or (end_x_coor == curr_x_coor+1 and end_y_coor == curr_y_coor)): # if next step leads to end point control key is assigned to -1
            M[curr_x_coor][curr_y_coor] = '*'
            cp = -1
            
        else :
            curr_point = min(M,curr_x_coor,curr_y_coor,n,m)
            lenght = lenght + M[curr_point[0]][curr_point[1]] # if next step is not end point then the process continues.
            M[curr_point[0]][curr_point[1]] = '*'
            curr_x_coor = curr_point[0]
            curr_y_coor = curr_point[1]
                
    print("The path created from start to end is denoted with '0' :")
    for i in range(n):
        for j in range(m) :
            print(M[i][j], end =" ") # The path finder finds the path and its lenght
        print()
    
    print("The length of path is :",lenght)

else:
    print("The start X-coordinate must be less than or equal to End X-coordinate and the start Y-coordinate must be less than or equal to End Y-coordinate")