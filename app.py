import keyboard

print("Robot can be moved with the space key to go FORWARD - Q to rotate LEFT and E to rotate RIGHT")

print("Enter X limit");
m = input() # x axis of grid
print('Enter Y limit')
n = input() # y axis of grid
print("x limit=", m, "& y limit =", n)

print("Enter X start")
xStart = input()
print("Enter Y start")
yStart = input()

print("Enter starting orientation (N,E,S,W)")
oriStart = input()

xAxis = int(m)
yAxis = int(n)


original_pos_x = int(xStart) # x position of robot on run
original_pos_y = int(yStart) # y position of robot on run

original_orientation = oriStart # robot orientation on run

# gets the starting rotation based on the orientation of the robot
if(oriStart == 'N'):
   original_rotation = 0 
elif (oriStart == 'E'):
   original_rotation = 90
elif (oriStart == 'S'):
   original_rotation = 180
elif (oriStart == 'W'):
   original_rotation = 270

class thisRobot: 
    pos_x = original_pos_x # current position of robot on x axis
    pos_y = original_pos_y # current position of robot on y axis
    orientation = original_orientation # current orientation of robot
    rotation = original_rotation # current rotation of robot

robot = thisRobot()


def display():
    if robot.pos_x > xAxis or robot.pos_x < 0:
        print("WARNING: Robot is LOST on X axis")

    if robot.pos_y > yAxis or robot.pos_y < 0:
        print("WARNING: Robot is LOST on Y axis")

    print( "X:", robot.pos_x, "Y:", robot.pos_y, "Facing:", robot.orientation, "Rot:", robot.rotation)

display()


def findOrientation(rotate): # finds the robot's orientation based off the rotation
    if rotate == 0:
        robot.orientation = 'N'
    elif rotate == 90:
        robot.orientation = 'E'
    elif rotate == 180:
        robot.orientation = 'S'
    elif rotate == 270:
        robot.orientation = 'W'
    
    display()

def move(ori): # moves the robot in the direction it is facing
    o = ori

    if o == 'N':
        robot.pos_y = robot.pos_y + 1
    elif o == 'S':
        robot.pos_y = robot.pos_y - 1
    elif o == 'E':
        robot.pos_x = robot.pos_x + 1
    elif o == 'W':
        robot.pos_x = robot.pos_x - 1

    display()

def rotate(direction): # rotates robot based on what key was pressed
    rotation = robot.rotation
    if direction == 'q':
        if rotation == 0:
            rotation = 360
            rotation = rotation - 90
            robot.rotation = rotation
            findOrientation(rotation)
        elif rotation != 0:
            rotation = rotation - 90
            robot.rotation = rotation
            findOrientation(rotation)

    elif direction == 'e':
        if rotation == 270:
            rotation = 0
            robot.rotation = rotation
            findOrientation(rotation)
        elif rotation != 360:
            rotation = rotation + 90
            robot.rotation = rotation
            findOrientation(rotation)
    


while True: # find key inputs
    key = keyboard.read_event()
    if key.event_type == keyboard.KEY_DOWN and key.name == 'space':
        move(robot.orientation)
    
    if key.event_type == keyboard.KEY_DOWN and key.name == 'q':
        rotate(key.name)
    
    if key.event_type == keyboard.KEY_DOWN and key.name == 'e':
        rotate(key.name)
