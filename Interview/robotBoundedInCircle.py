
"""
On an infinite plane, a robot initially stands at (0, 0) and faces north. The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degrees to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

 

Example 1:

Input: instructions = "GGLLGG"
Output: true
Explanation: The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.

The robot is bound in a cycle when

It returns to the origin at the end of one instruction cycle (or)
It has changed from its original direction
In that case, it will return to the original direction when it completes 3 more instruction cycles
"""
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        position = {"x" : 0, "y" : 0}
        position_changes = {"E":[1, 0],"W":[-1,0],"N":[0,1],"S":[0,-1]}
        dict_facing = {"E":["N","S"],"W":["S","N"],"N":["W","E"],"S":["E","W"]}
        facing = "N"
                
        for i in instructions:
            if i == "L" or i == "R":
                facing = self.changefacing(i, dict_facing, facing)
            else:
                position["x"] += position_changes[facing][0]
                position["y"] += position_changes[facing][1]

        return (position["x"]==0 and position["y"]==0) or facing != "N"

    def changefacing(self, inst, dict_facing, facing):
        turn = 0 if inst=="L" else 1
        facing = dict_facing[facing][turn]
        return facing

class Solution1:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = 0
        x, y = 0, 0
        position_changes = {1:[1, 0],3:[-1,0],0:[0,1],2:[0,-1]}

        for move in instructions:
            if move == "L":
                direction = (direction + 3) % 4
            elif move == "R":
                direction = (direction + 1) % 4
            else:
                x += position_changes[direction][0]
                y += position_changes[direction][1]
        return (x==0 and y==0) or direction !=0

class Solution2:
    def isRobotBounded(self, instructions: str) -> bool:
        d = [0, 1]
        x, y = 0, 0
        for move in instructions:
            if move == "L":
                d = [-d[1], d[0]]
            elif move == "R":
                d = [d[1], -d[0]]
            else:
                x += d[0]
                y += d[1]
        return (x==0 and y==0) or d != [0, 1]


S = Solution()
S1 = Solution1()
S2 = Solution2()

All_Instructions = "GGLLGG"

print(S.isRobotBounded(All_Instructions))
print(S1.isRobotBounded(All_Instructions))
print(S2.isRobotBounded(All_Instructions))