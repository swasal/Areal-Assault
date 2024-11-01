#imports
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import numpy as np


#initializing global vars
W_Width, W_Height = 500,500

#rain points
rain_dir=0 #direction of the rain


#background color
bg=0 #background color setter

#draw functions



def draw_house():
    glPointSize(5) #pixel size. by default 1 thake
    glColor3f(1.0, 0.0, 0.0)
    # glBegin(GL_POINTS)
    # glVertex2f(-250,250) #jekhane show korbe pixel
    # glEnd()

    #roof
    glBegin(GL_TRIANGLES)
    glVertex2d(0,50)
    glVertex2d(100,0)
    glVertex2d(-100,0)
    glEnd()

    #house body
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0) #red
    glVertex2f(70,0)
    glVertex2f(70,-100)

    glVertex2f(-70,0)
    glVertex2f(-70,-100)

    glVertex2f(70,-100)
    glVertex2f(-70,-100)
    glEnd()

    #door
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0) #red
    glVertex2f(40,-50)
    glVertex2f(60,-50)

    glVertex2f(40,-50)
    glVertex2f(40,-100)

    glVertex2f(60,-50)
    glVertex2f(60,-100)
    glEnd()



def draw_rain():
    global rain_dir
    glLineWidth(2.0)  # Set the line width for raindrops
    glColor3f(0.0, 0.0, 1.0)  # Set color to blue

    glBegin(GL_LINES)
    for _ in range(500):
        # Randomize the position and length of raindrops
        x = random.uniform(-250, 250)
        y = random.uniform(-100, 250)
        if -70<x<70:
            y = random.uniform(10, 250)
        
        
        length = random.uniform(10, 20)

        # Draw the raindrop
        glVertex2f(x, y)
        glVertex2f(x - length)
    glEnd()




def keyboardListener(key, x, y):

    global bg
    if key==b'w':
        bg+=0.01
        if bg<0:
            bg=0
        if bg>1:
            bg=1


    if key==b's':
        bg-=0.01
        if bg<0:
            bg
        if bg>1:
            bg=1

    glutPostRedisplay()



def specialKeyListener(key,x,y):
    global rain_dir

    if key==GLUT_KEY_LEFT:          #// LEFT arrow key
        rain_dir -= 1
        print("bending left")
    if key== GLUT_KEY_RIGHT:		#// RIGHT arrow key
        rain_dir += 1
        print("bending right")

    glutPostRedisplay()



def display():
    global bg
    #//clear the display
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(bg, bg, bg, 0);	#//color black
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    #//load the correct matrix -- MODEL-VIEW matrix
    glMatrixMode(GL_MODELVIEW)
    #//initialize the matrix
    glLoadIdentity()
    #//now give three info
    #//1. where is the camera (viewer)?
    #//2. where is the camera looking?
    #//3. Which direction is the camera's UP direction?
    gluLookAt(0,0,200,	0,0,0,	0,1,0)
    glMatrixMode(GL_MODELVIEW)
    draw_rain()
    draw_house()

    glutSwapBuffers()


def animate():
    #//codes for any changes in Models, Camera
    
    glutPostRedisplay()

def init():
    #//clear the screen
    glClearColor(0,0,0,0)
    #//load the PROJECTION matrix
    glMatrixMode(GL_PROJECTION)
    #//initialize the matrix
    glLoadIdentity()
    #//give PERSPECTIVE parameters
    gluPerspective(104,	1,	1,	1000.0)
    # **(important)**aspect ratio that determines the field of view in the X direction (horizontally). The bigger this angle is, the more you can see of the world - but at the same time, the objects you can see will become smaller.
    #//near distance
    #//far distance


glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB) #	//Depth, Double buffer, RGB color

# glutCreateWindow("My OpenGL Program")
wind = glutCreateWindow(b"House")
init()

glutDisplayFunc(display)	#display callback function
glutIdleFunc(animate)	#what you want to do in the idle time (when no drawing is occuring)

glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)

glutMainLoop()  #The main loop of OpenGL
