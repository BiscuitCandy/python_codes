import random as rand

class ValueException(Exception):
    pass

def min(a,x,y,n):     # finds the minimum next step 
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
    elif x+1 == n and y+1 != n :
            return [x,y+1]
    else : return [x+1,y]

# Header
print("-------------------------------------------------------------------")
print("***************************Path Finder*****************************")
print("-------------------------------------------------------------------")

# maze details
try:
    Mat_size = int(input("Enter the size of Maze 'NxN'"))
    M = [[rand.randint(1,9)for j in range(Mat_size)] for i in range(Mat_size)]
    
    print("The Randomly generated matrix is :") # prints the generated random matrix
    for j in range(Mat_size):
        for i in range(Mat_size) :
            print(M[i][j], end =" ") 
        print()

    curr_x_coor = start_x_coor = int(input("Enter start X-coordinate"))-1  # Starting X- coordinate
    curr_y_coor = start_y_coor = int(input("Enter start Y-coordinate"))-1  # starting Y- coordinate

    len = M[start_x_coor][curr_y_coor] 
    M[curr_x_coor][curr_y_coor] = '*' # the path is represented in '*'

    end_x_coor = int(input("Enter End X-coordinate"))-1  # Ending X-coordiante
    end_y_coor = int(input("Enter End Y-coordinate"))-1  # ending Y-coordiante
    # check if the entered values are valid
    if (end_x_coor >= Mat_size or end_y_coor >= Mat_size or start_x_coor < 0 or start_y_coor < 0) :
        raise ValueException

    elif (end_x_coor >= start_x_coor and end_y_coor >= start_y_coor ) :  
        len = len + M[end_x_coor][end_y_coor]
        M[end_x_coor][end_y_coor] = 0

        cp = 0  # the control key of the maze
        while(cp != -1):
            if ((end_x_coor == curr_x_coor and end_y_coor == curr_y_coor+1) or (end_x_coor == curr_x_coor+1 and end_y_coor == curr_y_coor)): # if next step leads to end point control key is assigned to -1
                M[end_x_coor][end_y_coor] = '*'
                cp = -1
            
            else :
                curr_point = min(M,curr_x_coor,curr_y_coor,Mat_size)
                len = len + M[curr_point[0]][curr_point[1]] # if next step is not end point then the process continues.
                M[curr_point[0]][curr_point[1]] = '*'
                curr_x_coor = curr_point[0]
                curr_y_coor = curr_point[1]
                
        print("The path created from start to end is denoted with '0' :")
        for j in range(Mat_size):
            for i in range(Mat_size) :
                print(M[i][j], end =" ") # The path finder finds the path and its lenght
            print()
    
        print("The length of path is :",len)

    else:
        print("The start X-coordinate must be less than or equal to End X-coordinate and the start Y-coordinate must be less than or equal to End Y-coordinate")

except ValueException :
    print("start X-coordinate and start Y-coordinate must be greater than zero")
    print("End X-coordinate and End Y-coordinate must be less tahn or equal to Matrix size")

except ValueError :
    print("Try giving VALID value inputs.")

except BaseException :
    print("Please omit this type of cases.")