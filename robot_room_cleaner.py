# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        visited = set()
        direction = 'up'

        def explore(square, previous_square):
            nonlocal visited, direction, robot

            visited.add(square)
            print(square)
            robot.clean()
            i, j = square[0], square[1]

            adjacent_squares = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            if (i-1, j) not in visited:
                if direction == 'left':
                    robot.turnRight()
                elif direction == 'right':
                    robot.turnLeft()
                elif direction == 'down':
                    robot.turnLeft()
                    robot.turnLeft()
                direction = 'up'
                m = robot.move()
                if m:
                    explore((i-1, j), square)
                else:
                    visited.add((i-1, j))

            if (i+1, j) not in visited:
                if direction == 'left':
                    robot.turnLeft()
                elif direction == 'right':
                    robot.turnRight()
                elif direction == 'up':
                    robot.turnLeft()
                    robot.turnLeft()
                direction = 'down'
                m = robot.move()
                if m:
                    explore((i+1, j), square)
                else:
                    visited.add((i+1, j))

            if (i, j-1) not in visited:
                if direction == 'up':
                    robot.turnLeft()
                elif direction == 'down':
                    robot.turnRight()
                elif direction == 'right':
                    robot.turnLeft()
                    robot.turnLeft()
                direction = 'left'
                m = robot.move()
                if m:
                    explore((i, j-1), square)
                else:
                    visited.add((i, j-1))
            
            if (i, j+1) not in visited:
                if direction == 'up':
                    robot.turnRight()
                elif direction == 'down':
                    robot.turnLeft()
                elif direction == 'left':
                    robot.turnLeft()
                    robot.turnLeft()
                direction = 'right'
                m = robot.move()
                if m:
                    explore((i, j+1), square)
                else:
                    visited.add((i, j+1))

            # orient the robot up to make things easier
            if direction == 'right':
                robot.turnLeft()
            elif direction == 'left':
                robot.turnRight()
            elif direction == 'down':
                robot.turnLeft()
                robot.turnLeft()

            direction = 'up'
            # return to the previous square
            if previous_square == (i-1, j):
                robot.move()
            elif previous_square == (i+1, j):
                robot.turnLeft()
                robot.turnLeft()
                direction = 'down'
                robot.move()
            elif previous_square == (i, j-1):
                robot.turnLeft()
                direction = 'left'
                robot.move()
            elif previous_square == (i, j+1):
                robot.turnRight()
                direction = 'right'
                robot.move()

        explore(square=(0,0), previous_square=None)



            

