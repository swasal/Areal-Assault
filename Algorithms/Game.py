
#imports
import time
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random


#global var innit

border=[] #list of all points to draw for the borders
bg=None
bg_r=bg_g=bg_b=0
frame=0
#file










W_Width, W_Height = 1280, 720
def convert_coordinate(x,y):
    global W_Width, W_Height
    a = x - (W_Width/2)
    b = (W_Height/2) - y 
    return a,b


#-----------------------------------drawing algorithms-------------------------------------------

#----------midpoint circle algo
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


#----------midpoint line algo

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

def fill(point:list, red, green, blue, y, dir=-1):
    if dir==-1: #fill under the line to border
        for i in point:
            temp=midpointlinedraw(i[0], i[1], i[0], -y)
            drawpoints(temp, red, green, blue)

    else:
        for i in point:
            temp=midpointlinedraw(i[0], i[1], i[0], y)
            drawpoints(temp, red, green, blue)

def brokenline(points:list):
    output=[]
    for i in range(0, len(points)-1):
        output.extend(midpointlinedraw(points[i][0], points[i][1], points[i+1][0], points[i+1][1]))

    return output

#---------draw function

def drawpoints(points:list, red, green, blue):
    """Draws points in the given list with the colors"""
    glBegin(GL_POINTS)
    glColor3f(red/255, green/255, blue/255)#color
    for i in points:
        glVertex2f(i[0],i[1])
    glEnd()



def draw_rain():

    for _ in range(100):
        # Randomize the position and length of raindrops
        x = random.uniform(-638, 638)
        y = random.uniform(-290, 350)
        if -70<x<70:
            y = random.uniform(10, 250)
        
        
        length = random.uniform(10, 20)

        # Draw the raindrop
        p=midpointlinedraw(x,y,x,y-length)
        drawpoints(p, 0,0,255)
       










#-----------------------------------actualk drawing-------------------------------------------

def draw_border():
    global border
    points=[]
    points.extend(midpointlinedraw(-640,360,640,360))
    points.extend(midpointlinedraw(-640,-360,640,-360))
    points.extend(midpointlinedraw(-640,-360,-640,360))
    points.extend(midpointlinedraw(640,-360,640,360))

    border = points
    drawpoints(border, 255, 255, 255)



#backgrounds

def background_selector():
    global bg
    i=random.randint(1,3)

    if i==1:
        bg="dessert"
    elif i==2:
        bg="starrynight"
    elif i==3:
        bg="winter_night"


def draw_bg():
    if bg=="dessert":
        background_dessert()
    elif bg=="starrynight":
        background_starrynight()
    elif bg=="winter_night":
        background_winternight()
    else:
        background_selector()
        draw_bg()


def background_dessert():
    global frame, bg_r, bg_g, bg_b

    #setting up the sky
    bg_r, bg_g, bg_b=201/255, 93/255, 65/255
   
    #drawign the sun
    sun=midpointcircledraw(0,-60, 350, 0,1,6,7)
    drawpoints(sun, 252,72,94)
    fill(sun, 255,15,47,4, 1)

    #mountain layers
    line=[(-638,166),(-574,190),(-516,175),(-477,205),(-406,173),(-376,142),(-359,155),(-337,172),(-307,193),(-265,182),(-257,161),(-237,138),(-209,117),(-190,137),(-168,158),(-126,178),(-96,193),(-52,210),(-27,206),(22,194),(49,185),(81,179),(118,172),(154,172),(186,169),(214,180),(236,188),(255,197),(273,210),(287,219),(298,229),(315,233),(330,227),(362,216),(388,210),(414,202),(425,199),(446,205),(461,213),(474,219),(488,227),(504,224),(511,213),(519,205),(533,196),(548,193),(561,201),(566,214),(578,229),(586,245),(590,259),(602,256),(610,242),(619,226),(638,209)]
    points=brokenline(line)
    drawpoints(points, 203,50,70)
    fill(points, 203,50,70, 73, -1)


    line=[(-638,-80),(-617,-72),(-573,-50),(-511,-21),(-460,2),(-407,9),(-378,0),(-367,-8),(-354,-17),(-337,-33),(-321,-41),(-291,-57),(-260,-69),(-223,-75),(-176,-57),(-145,-38),(-106,-12),(-68,9),(27,42),(69,54),(129,67),(167,70),(215,55),(254,31),(286,1),(313,-8),(383,28),(437,59),(475,80),(508,100),(526,111),(550,108),(581,84),(592,71),(606,53),(615,41),(627,25),(638,21)]
    points=brokenline(line)
    drawpoints(points, 145, 17, 34)
    fill(points, 145, 17, 34,250, -1)
    

    #footing
    line=[(-638,-249),(-609,-244),(-584,-238),(-545,-233),(-515,-226),(-502,-226),(-472,-228),(-458,-228),(-393,-231),(-366,-235),(-339,-237),(-323,-237),(-301,-237),(-263,-244),(-235,-244),(-186,-249),(-164,-249),(-137,-241),(-110,-231),(-94,-224),(-76,-217),(-55,-209),(-45,-205),(-35,-205),(-16,-213),(2,-217),(28,-221),(47,-225),(84,-229),(115,-231),(139,-232),(159,-232),(197,-231),(217,-227),(234,-224),(249,-223),(270,-219),(298,-217),(335,-216),(360,-216),(377,-216),(412,-220),(429,-222),(455,-223),(480,-223),(499,-222),(525,-217),(574,-210),(585,-210),(594,-210),(602,-210),(613,-213),(619,-215),(638,-219)]
    points=brokenline(line)
    drawpoints(points, 43, 2, 7)
    fill(points, 43, 2, 7,358, -1)



def background_winternight():
    global frame, bg_r, bg_g, bg_b

    #setting up the sky
    bg_r, bg_g, bg_b=3/255, 2/255, 28/255
    #adding rain
    draw_rain()

    #ground
    line=[(-633,-266),(-585,-262),(-554,-257),(-502,-245),(-453,-236),(-421,-232),(-384,-228),(-352,-228),(-328,-228),(-301,-228),(-273,-232),(-215,-240),(-199,-241),(-155,-246),(-120,-247),(-80,-246),(-45,-244),(3,-240),(29,-239),(55,-238),(96,-235),(123,-234),(136,-232),(174,-231),(206,-231),(244,-236),(279,-240),(309,-243),(348,-245),(381,-245),(407,-240),(432,-232),(455,-228),(485,-222),(508,-220),(525,-218),(540,-217),(598,-216),(603,-216),(614,-215),(620,-214),(626,-214),(629,-213),(632,-212)] 
    points=brokenline(line)
    drawpoints(points, 2, 1, 16)
    fill(points, 2, 1, 16, 350, -1)




def background_starrynight():
    global frame, bg_r, bg_g, bg_b

    #setting up the sky
    bg_r, bg_g, bg_b=3/255, 2/255, 28/255

    #stars
    
    if frame%2==0:
        stars=[(-565,308),(-570,249),(-578,189),(-521,164),(-439,153),(-363,162),(-331,243),(-205,271),(-164,234),(-182,164),(-195,131),(-121,130),(-84,128),(-69,183),(17,243),(121,241),(139,193),(179,132),(262,123),(334,199),(370,264),(455,297),(521,258),(574,178),(529,153),(448,224),(285,236),(55,228),(-345,211),(-586,236),(-20,268),(417,258),(526,234),(220,113),(-294,162),(-472,150),(-343,96),(-85,79),(223,107),(442,167),(571,253),(566,176),(387,167),(-222,165),(-382,140),(-486,42),(-517,33),(-542,108),(-526,154),(-367,250),(-145,260),(-97,153),(113,90),(366,105),(482,215),(532,271),(573,200),(270,304),(127,313),(-88,240),(-201,175),(-513,223),(-452,214),(-430,261),(-474,279),(-355,299),(-262,231),(-254,212),(21,184),(38,104),(-8,129),(205,236),(247,176),(487,116),(563,111),(596,298),(-594,71),(-510,221),(-447,196),(-395,199),(-432,254),(-480,236),(-499,205)]
        drawpoints(stars, 255, 255, 255)
    else:
        stars=[(501,80),(499,164),(485,275),(280,299),(291,234),(289,159),(152,127),(128,179),(198,231),(149,279),(65,174),(45,138),(-58,171),(-52,211),(-66,239),(-144,224),(-151,197),(-116,207),(-120,210),(-94,184),(-147,166),(-166,137),(-145,86),(-260,95),(-273,125),(-292,136),(-310,136),(-325,122),(-347,89),(-384,69),(-417,67),(-469,93),(-493,117),(-484,142),(-388,245),(-481,274),(-550,231),(-441,288),(-314,242),(-215,242),(32,299),(117,216),(261,226),(445,277),(466,277),(503,155),(336,207),(65,271),(-85,30),(28,118),(329,162),(544,79),(509,128),(452,191),(331,231),(-41,172),(-306,129),(-490,98),(-562,144),(-564,185),(-564,292),(-601,210),(-563,156),(-377,175),(-221,213),(-218,123),(-73,191),(78,233),(226,141),(368,169),(456,274),(544,126),(582,216),(493,299),(249,293),(49,295),(-119,285),(-348,323),(-498,274),(-493,239),(322,253),(542,211)]
        drawpoints(stars, 255, 255, 255)
    

    line=[(-633,-79),(-607,-60),(-585,-44),(-552,-13),(-536,0),(-508,17),(-477,37),(-458,48),(-425,65),(-398,74),(-371,75),(-333,57),(-265,-14),(-212,-41),(-146,-52),(-119,-45),(-84,-26),(-71,-13),(-48,4),(-13,30),(19,49),(54,67),(76,76),(110,86),(121,86),(161,66),(185,55),(205,42),(220,32),(271,3),(284,-5),(319,-22),(346,-32),(393,-42),(412,-49),(458,-61),(470,-63),(506,-64),(543,-67),(559,-67),(579,-68),(603,-70),(610,-70),(625,-71),(632,-71)]
    points=brokenline(line)
    drawpoints(points, 9, 8, 59)
    fill(points, 9, 8, 59, 120,-1)
    
    
    line=[(-634,-114),(-520,-94),(-430,-71),(-385,-63),(-311,-71),(-254,-93),(-195,-124),(-158,-145),(-127,-159),(-94,-170),(-48,-175),(-6,-173),(14,-164),(73,-142),(126,-107),(218,-54),(269,-6),(303,20),(335,47),(404,81),(451,90),(483,83),(515,51),(573,20),(609,31),(629,52),(632,54),(-231,-146),(-219,-133),(-206,-118),(-197,-105),(-187,-98),(-171,-89),(-157,-84),(-133,-87),(-115,-93),(-93,-85),(-66,-70),(-51,-60),(-41,-51),(-24,-40),(2,-30),(30,-28),(50,-28),(80,-33),(96,-37),(118,-50),(138,-62),(147,-66),(162,-71),(171,-75),(182,-79),(195,-86)]
    points=brokenline(line)
    drawpoints(points, 9, 8, 59)
    fill(points, 2, 1, 36, 150 -1)

    line=[(-634,-114),(-520,-94),(-430,-71),(-385,-63),(-311,-71),(-254,-93),(-195,-124),(-158,-145),(-127,-159),(-94,-170),(-48,-175),(-6,-173),(14,-164),(73,-142),(126,-107),(218,-54),(269,-6),(303,20),(335,47),(404,81),(451,90),(483,83),(515,51),(573,20),(609,31),(629,52),(632,54)]
    points=brokenline(line)
    drawpoints(points, 3, 2, 46)
    fill(points, 3, 2, 46, 270 -1)

    line=[(-635,-278),(-606,-267),(-596,-263),(-528,-245),(-472,-241),(-446,-241),(-418,-247),(-376,-256),(-303,-261),(-259,-262),(-214,-261),(-167,-252),(-123,-248),(-81,-248),(-21,-253),(45,-253),(78,-249),(116,-246),(162,-239),(215,-238),(278,-244),(334,-253),(371,-258),(434,-265),(498,-267),(545,-269),(569,-269),(594,-272),(624,-271),(632,-271)]
    points=brokenline(line)
    drawpoints(points, 2, 1, 16)
    fill(points, 2, 1, 16, 350 -1)




def display():
     #//clear the display
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(bg_r, bg_g, bg_b, 0)	#//color based on background
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    #//load the correct matrix -- MODEL-VIEW matrix
    glMatrixMode(GL_MODELVIEW)
    #//initialize the matrix
    glLoadIdentity()
    #//now give three info
    #//1. where is the camera (viewer)?
    #//2. where is the camera looking?
    #//3. Which direction is the camera's UP direction?
    gluLookAt(0,0,314,	0,0,0,	0,1,0)
    glMatrixMode(GL_MODELVIEW)

    glPointSize(2)
    draw_border()
    background_dessert()
    
    

    glutSwapBuffers()
    

def animate():
    global frame
    if frame==0:
        frame=1
    else:
        frame=0
    #60 fps
    current_time = time.time()
    delta_time = current_time - animate.start_time if hasattr(animate, 'start_time') else 0
    animate.start_time = current_time
    pass #animation codes here

    #used to control blink animation in background scenes
    


    # time.sleep(1/60)
    glutPostRedisplay()

def init():
    #//clear the screen
    glClearColor(0,0,0,0)
    #//load the PROJECTION matrix
    glMatrixMode(GL_PROJECTION)
    #//initialize the matrix
    glLoadIdentity()
    #//give PERSPECTIVE parameters
    gluPerspective(98, (1280/720), 1, 1000.0)
    # **(important)**aspect ratio that determines the field of view in the X direction (horizontally). The bigger this angle is, the more you can see of the world - but at the same time, the objects you can see will become smaller.
    #//near distance
    #//far distance

    if bg==None:
        background_selector()

glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB) #	//Depth, Double buffer, RGB color


# glutCreateWindow("My OpenGL Program")
wind = glutCreateWindow(b"Game")
init()

glutDisplayFunc(display)	#display callback function
glutIdleFunc(animate)	#what you want to do in the idle time (when no drawing is occuring)

# glutKeyboardFunc(keyboardListener)
# glutSpecialFunc(specialKeyListener)
# glutMouseFunc(mouseListener)

glutMainLoop()		#The main loop of OpenGL






