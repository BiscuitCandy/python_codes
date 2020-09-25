import random
#import time

#initial = time.time()

class Point:
    def __init__(self):
        self.x = 0
        self.y = 0
    def to_north(self):
        self.x += 1
    def to_south(self):
        self.x -= 1
    def to_east(self):
        self.y += 1
    def to_west(self):
        self.y -= 1
    def abs_sum(self):
        return abs(self.x) + abs(self.y)
    def display_point(self):
        print('(',self.x," , ",self.y,')',sep="")

ManhattanDist = int(input("Enter the r Value"))
testcases = int(input("Enter no.of testcases"))

def Random_steps():
    p = Point()
    directions_dict = {1:p.to_north, 2:p.to_south, 3:p.to_east, 4:p.to_west}
    count = 0
    while (ManhattanDist != p.abs_sum()):
        count += 1
        directions_dict[random.randrange(1,4)]()
    return count

sum1 = 0

for i in range(testcases):
    x = Random_steps()
    sum1 += x

print(round(sum1/testcases,2))

#print(time.time()-initial)