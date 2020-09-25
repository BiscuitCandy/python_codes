import random as rand

def min(maze, row , col , end_row , end_col) :
    if row == end_row:
        return [row,col+1]
    elif col == end_col :
        return [row+1,col]
    
    elif row+1 <= end_row and col+1 <= end_col:
        if maze[row+1][col] < maze [row][col+1]:
            return [row+1,col]
        elif maze[row+1][col] > maze [row][col+1]:
            return [row,col+1]
        elif row+1 == end_row and col+1 == end_col and maze[row+1][col] == maze[row][col+1]:
            return [row,col+1]

        elif row+2 <= end_row and col+2 <= end_col :
            if maze[row][col+1] == maze[row+1][col]:
                if maze[min(maze, row+1,col,end_row,end_col)[0]][min(maze, row+1,col,end_row,end_col)[1]] <= maze[min(maze,row,col+1,end_row,end_col)[0]][min(maze, row,col+1,end_row,end_col)[1]]:
                    return [row+1,col]
                else : return [row,col+1]
     

print(
"""
-------------------------------------------------------------------------
****************************** Path Finder ******************************
-------------------------------------------------------------------------
""")

# create a random Maze Matrix
## Enter the dimensions of the matrix

maze_size = int(input("Enter the size of the maze"))

## Create the Random Maze Matrix

maze = [[rand.randint(  1,9) for j in range(maze_size)] for i in range(maze_size)]

## print the Maze Matrix

print("System created Maze Matrix is : ")
for i in range(maze_size):
    for j in range(maze_size):
        print(maze[i][j], end = " ")
    print()

# fill up the start and end coordinates

## fill the start 
start_col = curr_col = int(input("Enter start X-coordinate")) - 1
start_row = curr_row = int(input("Enter Start Y-coordiante")) - 1

## fill the end 
end_col = int(input("Enter end X-coordiante")) - 1
end_row = int(input("Enter end Y-coordiante")) - 1

# Create the path in .the maze

if (start_col not in range(maze_size) or end_col not in range(maze_size) or start_row not in range(maze_size) or end_row not in range(maze_size)) :
    print("Enter Start and End coordinates in the RANGE of Maze Dimensions")

elif start_col > end_col or start_row > end_row :
    print("Enter VALID inputs")
    print("The start coordinates must be LESS THAN end coordinates")

elif start_col == end_col and start_row == end_row :
    print("Start coordinates and End coordinates are SAME")
    print("The min required lenght to cross start and end is 0")

else :
    len = maze[start_row][start_col]
    maze[start_row][start_col] = "*"
    
    len += maze[end_row][end_col]
    maze[end_row][end_col] = 0

    control_key = 0 ### teh control key of teh maze
    
    while(control_key != -1) :
        if curr_col == end_col and curr_row == end_row :
            maze[end_row][end_col] = "*"
            control_key = -1
        else :
            curr_point = min(maze,curr_row,curr_col,end_row,end_col)
            len = len + maze[curr_point[0]][curr_point[1]]
            maze[curr_point[0]][curr_point[1]] = '*'
            curr_row = curr_point[0]
            curr_col = curr_point[1]   

    print("The path FOUND is :")
    for row in range(maze_size):
        for col in range(maze_size):
            print(maze[row][col], end =" ")
        print()        
    print("The min required LENGTH to cross start and end is ",len)