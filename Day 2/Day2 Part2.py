"""
---TASK DETAILS---
Suppose your instructions are:
ULL
RRDDD
LURDL
UUUUD

--- Part Two ---

You finally arrive at the bathroom (it's a several minute walk from the lobby so visitors can behold the many fancy conference rooms and water coolers on this floor) and go to punch in the code.
Much to your bladder's dismay, the keypad is not at all like you imagined it.
Instead, you are confronted with the result of hundreds of man-hours of bathroom-keypad-design meetings:
    1
  2 3 4
5 6 7 8 9
  A B C
    D
You still start at "5" and stop when you're at an edge, but given the same instructions as above, the outcome is very different:

You start at "5" and don't move at all (up and left are both edges), ending at 5.
Continuing from "5", you move right twice and down three times (through "6", "7", "B", "D", "D"), ending at D.
Then, from "D", you move five more times (through "D", "B", "C", "C", "B"), ending at B.
Finally, after five more moves, you end at 3.
So, given the actual keypad layout, the code would be 5DB3.

Using the same instructions in your puzzle input, what is the correct bathroom code?
"""

import os
import sys

keypad = [[" ", " ", "1", " ", " "],
          [" ", "2", "3", "4", " "],
          ["5", "6", "7", "8", "9"],
          [" ", "A", "B", "C", " "],
          [" ", " ", "D", " ", " "]]

current = (2, 0)

movements = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}

finalPos = ""

instructions = open(os.path.join(sys.path[0], "input.txt"))
instrLine = instructions.read().strip().split("\n")

for l in instrLine:
    for i in l:
        nextMovement = movements[i]
        newCurrent = (current[0] + nextMovement[0], current[1] + nextMovement[1])
        if newCurrent[0] < 0 or newCurrent[0] > 4 or newCurrent[1] < 0 or newCurrent[1] > 4 or keypad[newCurrent[0]][newCurrent[1]] == " ":
            continue
        else:
            current = newCurrent
    finalPos += keypad[current[0]][current[1]]

print(finalPos)
