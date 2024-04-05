#imports
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *





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





def circle():
    #draws a full circle
    
    points=midpointcircledraw(4,5,100)
    drawpoints(points, 1.0,0,1.0)


def customcircle():

    #draws zone 1,2,4,6,7
    points=midpointcircledraw(0,20,100, 1,2,6,7,4)
    drawpoints(points, 1.0,0,1.0)