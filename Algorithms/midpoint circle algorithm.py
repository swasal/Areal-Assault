#imports
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *






#midpoint circle algo
def circlepoints(x, y, a,b, zone=""):
    #list that contains all the points for each zone 0-8
    l=[(x+a,y+b),(y+a,x+b),(y+a,-x+b),(x+a,-y+b),(-x+a,-y+b), (-y+a,-x+b), (-y+a,x+b), (-x+a,y+b)] 

    if zone:#checks if zone numbers were mentioned
        out=[]
        for i in zone:
            out.append(l[i])
        
        return out #returns a list of tuples containing only the points in the specified zones

    else:
        return l #returns a list of tuples for all zones



def midpointcircledraw(x1,y1,r, *zone): #call function to get list of points
    """Returns a list of points to draw a line from two given points"""
    # x1, y1= p[0], p[1]
    points=[] #store all the points to draw after reverting in format=> points=[(x,y), (x,y).....]
    x=0
    y=r
    d=1-r

    
    #plotting the points
    while x<y:
        if d>=0: #choose SE
            d+=2*x - 2*y + 5
            x+=1
            y-=1


            points.extend(circlepoints(x,y,x1,y1, zone))
            

        else: #choose E
            d+=2*x + 3
            x+=1
            
            points.extend(circlepoints(x,y,x1,y1, zone))


    return points #returns list of points


#draw function

def drawpoints(points:list, red, green, blue):
    """Draws points in the given list with the colors"""
    glBegin(GL_POINTS)
    glColor3f(red, green, blue)#color
    for i in points:
        glVertex2f(i[0],i[1])
    glEnd()





"""
The functions works for eithr a circle or parts of the circle in specific zones.
if u want the entire circle to be drawn then simply donrt put a value for the zones parameter.
if u want specific zones to appear the after the parameters put in the number of the zones u want to be drawn(the number does not need to be in any sopecific order.
)"""

#draw function

def drawpoints(points:list, red, green, blue): #uased to draw the points from a given list
    """Draws points in the given list with the colors"""
    glBegin(GL_POINTS)
    glColor3f(red, green, blue)#color
    for i in points:
        glVertex2f(i[0],i[1])
    glEnd()






"""the code for testign the function is given below3 alog witha few example uses"""


#testign the code

#Var innit
bg=0
circley = 200
fallSpeed = 0.2



def fallingcircle():
    global diamondy
    points=midpointcircledraw(0,circley,100)
    drawpoints(points, 1.0,0,1.0)



def circle():
    #draws a full circle
    points=midpointcircledraw(4,100,50)
    drawpoints(points, 1.0,0,1.0)


def customcircle():

    #draws zone 1,4 and 6
    points=midpointcircledraw(0,-50,50, 1, 6, 4) #iwrote it as 1, 6, 4 to show that the order doesnt matter
    drawpoints(points, 1.0,0,1.0)


def display():
    #//clear the display
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(bg,bg,bg, 0);	#//color black
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,0,200,	0,0,0,	0,1,0)
    glMatrixMode(GL_MODELVIEW)
    #draw function calls
    fallingcircle()
    customcircle()
    circle()

    glutSwapBuffers()


def animate():
    global circley, fallspeed
    circley-=fallSpeed
    if circley<=-250:
        circley=250
    glutPostRedisplay()


def init():
    glClearColor(0,0,0,0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(104,	1,	1,	1000.0)
   


glutInit()
glutInitWindowSize(1000, 1000)
glutInitWindowPosition(500, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB) 

wind = glutCreateWindow(b"Diamond catcher")
init()

glutDisplayFunc(display)	
glutIdleFunc(animate)	
# glutKeyboardFunc(keyboardListener)
# glutSpecialFunc(specialKeyListener)
# glutMouseFunc(mouseListener)

glutMainLoop() 