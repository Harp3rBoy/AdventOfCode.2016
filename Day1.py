"""
---TASK DETAILS---
--- Day 1: No Time for a Taxicab ---

You're airdropped near Easter Bunny Headquarters in a city somewhere.
"Near", unfortunately, is as close as you can get.

The Document indicates that you should start at the given coordinates (where you just landed) and face North.
Then, follow the provided sequence: either turn left (L) or right (R) 90 degrees.
Then walk forward the given number of blocks, ending at a new intersection.

Given that you can only walk on the street grid of the city, how far is the shortest path to the destination?

For example:
Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
R5, L5, R5, R3 leaves you 12 blocks away.

How many blocks away is Easter Bunny HQ?

--- Part Two ---

Then, you notice the instructions continue on the back of the Recruiting Document.
Easter Bunny HQ is actually at the first location you visit twice.

For example, if your instructions are R8, R4, R4, R8, the first location you visit twice is 4 blocks away, due East.

How many blocks away is the first location you visit twice?
"""

x = 0
y = 0
facing = 0
visited = []
firstDuplicateDistance = ""

def move(a):
    global x
    global y
    a = int(a)
    if facing == 0:
        x += a
    elif facing == 1:
        y += a
    elif facing == 2:
        x -= a
    else:
        y -= a

def changeDir(dir):
    global facing
    j = directArr[i]
    if j[0] == "L":
        facing += 1
    elif j[0] == "R":
        facing -= 1
    facing %= 4
    move(j[1:])

directions = input("Enter directions: ")
directArr = directions.split(', ')

# Part 1
for i in range(len(directArr)):
    changeDir(i)
print("Part 1 = " + str((abs(x)) + (abs(y))))

# # Part 2
# for i in visited:
#     if (visited[i] == (str(x) + ":" + str(y))) and (firstDuplicateDistance == ""):
#         firstDuplicateDistance = (str(abs(x) + abs(y)))
#     else:
#         visited.append(str(x) + ":" + str(y))
#
# print(firstDuplicateDistance)
