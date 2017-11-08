import os
import sys
import time
import pybullet as p

def wait_key():
    ''' Wait for a key press on the console and return it. '''
    result = None
    if os.name == 'nt':
        import msvcrt
        result = msvcrt.getch()
    else:
        import termios
        fd = sys.stdin.fileno()

        oldterm = termios.tcgetattr(fd)
        newattr = termios.tcgetattr(fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, newattr)

        try:
            result = sys.stdin.read(1)
        except IOError:
            pass
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)

    return result

p.connect(p.GUI)

# create the main plane
p.resetDebugVisualizerCamera( cameraDistance=5, cameraYaw=90, cameraPitch=-10, cameraTargetPosition=[0,0,3])
p.createCollisionShape(p.GEOM_PLANE)
p.createMultiBody(0, 0)

# create spheres and cubes
sphereRadius = 0.5
colSphereId = p.createCollisionShape(p.GEOM_SPHERE, radius=sphereRadius)
colBoxId = p.createCollisionShape(p.GEOM_BOX, halfExtents=[sphereRadius, sphereRadius, sphereRadius])

sphereMass = 2
cubeMass = 1
visualShapeId = -1 # not needed since we're using the collision shape ID, can set to -1
basePositionSphere = [0, 1, 5*sphereRadius+1]
basePositionCube = [0, -1, 5*sphereRadius+1]
baseOrientation = [0, 0, 0, 1]

sphereStartVelocity = [0, -1, 0]
cubeStartVelocity = [0, 1, 0]

# create the objects in the world
sphereUid = p.createMultiBody(sphereMass, colSphereId, visualShapeId, basePositionSphere, baseOrientation)
cubeUid = p.createMultiBody(cubeMass, colBoxId, visualShapeId, basePositionCube, baseOrientation)

# set initial velocities and gravity
p.resetBaseVelocity(objectUniqueId=sphereUid, linearVelocity=sphereStartVelocity)
p.resetBaseVelocity(objectUniqueId=cubeUid, linearVelocity=cubeStartVelocity)
p.setGravity(0, 0, -10)

KEYBOARD_MODE = False

if KEYBOARD_MODE:
    input_key = None
    while input_key != 'q':
        input_key = wait_key()
        if input_key == 'q':
            sys.exit()
        else:
            p.stepSimulation()
            contactPoints = p.getContactPoints(bodyA=sphereUid, bodyB=cubeUid)
            if len(contactPoints) > 0:
                print('Collision detected!')
                sys.exit()
else:
    while 1:
        p.stepSimulation()
        time.sleep(0.05)
        contactPoints = p.getContactPoints(bodyA=sphereUid, bodyB=cubeUid)
        if len(contactPoints) > 0:
            print('Collision detected!')
            print(contactPoints)
            input_key = wait_key()
            sys.exit()
