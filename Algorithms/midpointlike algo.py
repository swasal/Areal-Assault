#imports
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


#midpoint line algo
def fz(x1, y1, x2, y2): #findzone function

    dx=x2 - x1
    dy=y2 - y1
    # z=None #zone

    if abs(dy)>abs(dx):
        #z 1 2 5 6 
        if dy>0:
            if dx>0:
                z=1
            else:
                z=2       
        else:
            if dx>0:
                z=6
            else:
                z=5

    else: #|dx| > |dy|
        #z 0 3 4 7
        if dy>0:
            if dx>0:
                z=0
            else:
                z=3       
        else:
            if dx>0:
                z=7
            else:
                z=4

    return z

def convert(x, y, z):
    if z==0:
        pass
    if z==1:
        x,y = y,x
    if z==2:
        x,y = y,-x
    if z==3:
        x,y = -x,y
    if z==4:
        x,y = -x,-y
    if z==5:
        x,y = -y,-x
    if z==6:
        x,y = -y,x
    if z==7:
        x,y = x,-y

    return x,y,z #returns a tuple

def revert(x,y,z):
    if z==0:
        pass
    if z==1:
        x,y = y,x
    if z==2:
        x,y = -y,x
    if z==3:
        x,y = -x,y
    if z==4:
        x,y = -x,-y
    if z==5:
        x,y = -y,-x
    if z==6:
        x,y = y,-x
    if z==7:
        x,y = x,-y

    return x,y #returns a tuple

def midpointlinedraw(x1,y1,x2,y2): #call function to get list of points
    """Returns a list of points to draw a line from two given points"""
    # x1, y1, x2, y2= p[0], p[1], p[2], p[3]
    points=[(x1,y1)] #store all the points to draw after reverting in format=> item=[(x,y), (x,y).....]
    
    #calculating zones and converting start adn end points
    z=fz(x1, y1, x2, y2)
    s=convert(x1, y1, z)
    e=convert(x2, y2, z)

    #finding dx and dy using converted points
    dx=e[0] - s[0]
    dy=e[1] - s[1]

    #calculating the increments
    incrE = 2 * dy
    incrNE = 2 * (dy - dx)
    
    #initializing the function
    d=2*dy-dx
    x=s[0]
    y=s[1]
    
    #plotting the points
    while x<e[0]:
        if d>0: #choose NE
            d+=incrNE
            x+=1
            y+=1

            points.append(revert(x,y,z)) #appends points to the list

        else: #choose E
            d+=incrE
            x+=1
            
            points.append(revert(x,y,z)) #appends points to the list


    return points #returns list of points



"""
The midpoint line algo returns a list of all the points needed to be ploted in order to complkete the line between the two points.
then the draw function below is used to draw the points from list one at a time.
"""



#draw function

def drawpoints(points:list, red, green, blue): #uased to draw the points from a given list
    """Draws points in the given list with the colors"""
    glBegin(GL_POINTS)
    glColor3f(red, green, blue)#color
    for i in points:
        glVertex2f(i[0],i[1])
    glEnd()
