# Areal-Assault-
A two player game for the cse423 project
the basic idea of the oproject is [here](https://drive.google.com/file/d/1Wgi0PAkcFC6i9AKqsvrRnFHnEptjfWWW/view?usp=drive_link)


## Base concept

The basic idea is a 2 player local multipllayer cannon game. Each player has a cannon that cna fire ata  trajectorory of 90 degrees centered from the top of thier character model. The goal of the game is toi get your enemy to 0 hp. 

### character ability
The said characters have two abilities a shield and a misile that can be fired horizontally (which can be evaded using the terrain or jumping mechanism).

### controls

each cplayer's character can move sideways and jump and has a shield


## files

The repository contains an [algorithm](/Algorithms) folder

Both these algorithms return a list of tuples in which every point is a tuple (x,y). These points from the list are rendered usign the draw function whicvh takes i a list of all the points and then renders them in the display.

The list containing the p[oints looks something like =. [(x1,y1), (x2,y2), (x3,y3), ........]] 

### midpoint line

The [midpoint line file](/Algorithms/midpointlike%20algo.py) contains the algorithm to draw the line using two points x1,1 to x2,y2 and returns a list of all the points

### midpoint circle

The [midpoint circle file](/Algorithms/midpoint%20circle%20algorithm.py) contains the midpoint circle algorithm which can draw either a full circle or specific zones of a circle. The midpointcircle takes in three compulsory parameters, the center of the circle x,y and the radius. The fourth is the zones which if left alone will render a full circle. The tesrt c0odes are provded in the file

paste the l
