import math  

print("This program calculates the coordinates in open traverse serie")
print("-" * 55)
  
point_1 = input("Enter the point ID of first known point  :")   
point_1_y=float(input("Enter the Y coordinates of first known point (m) :"))  
point_1_x=float(input("Enter the X coordinates of first known point (m)  :"))  

point_2 = input("Enter the point ID of second known point  :")
point_2_y = float(input("Enter the Y coordinates of second known point (m)  :"))   
point_2_x = float(input("Enter the X coordinates of second known point (m)  :"))

np = int(input("Enter the number of unknown traverse points  :"))
  
Points=[]  
Points.append(point_1)  
Points.append(point_2)

for i in range( np ):
    un_point = int(input("Enter the point ID of unknown point " + str(i+1) + ":"))
    Points.append(un_point)  


Angles = []  
for i in range(1, 1 + np):
    angle = float(input("Enter the traverse angle of " + str(Points[i]) + "(grad):"))  
    Angles.append(angle)  
  
Distances = []  
for i in range(1, 1 + np):
    distance = float(input("Enter the horizontal distance between " + str(Points[i]) + " and " + str(Points[i + 1]) + " (m):"))  
    Distances.append(distance)  


def first_azimuth(y1, x1, y2, x2):  
    dy = y2 - y1  
    dx = x2 - x1  

    if x1 == x2 and y1 > y2:  
        azimuth = 300  
    elif x1 == x2 and y1 < y2:  
        azimuth = 100        
    elif y1 == y2 and x1 > x2:  
        azimuth = 200  
    elif y1 == y2 and x1 < x2:  
        azimuth = 0  
    else:  
        azimuth = math.atan(abs(dy / dx)) * 200 / math.pi  

    if dy > 0 and dx > 0:
        azimuth = azimuth  
    elif dy > 0 and dx < 0:  
        azimuth = 200 - azimuth  
    elif dy < 0 and dx < 0:  
        azimuth = 200 + azimuth  
    else:  
        azimuth = 400 - azimuth  

    return azimuth  


def next_azimuth(azimut, traverse):  
    K_0603 = float(azimut + traverse)
    
    if K_0603 < 200:  
        K_0603 += 200  
    elif K_0603 > 200 and K_0603 < 600:  
        K_0603 -= 200  
    elif K_0603 > 600:  
        K_0603 -= 600  

    return K_0603  
  

angle_A = first_azimuth(point_1_y, point_1_x, point_2_y, point_2_x)

Azimuths = []
Azimuths.append(angle_A)    
for i in range(len(Angles)):  
        az = float(next_azimuth(Azimuths[i], Angles[i]))  
        Azimuths.append(az)  
print(Azimuths)
 

def delta_y(dist,azimuth):  
    deltay_0603 = float(dist * math.sin(azimuth*math.pi/200))  
    return deltay_0603   

def delta_x(dist,azimuth):  
    deltax_0603 = float(dist * math.cos(azimuth*math.pi/200))  
    return deltax_0603  


Delta_Y = []   
for i in range(len(Distances)):  
    deltay=delta_y(Distances[i],Azimuths[i+1])  
    Delta_Y.append(deltay)  
print(Delta_Y)

Delta_X =[]  
for i in range(len(Distances)):   
    deltax=delta_x(Distances[i],Azimuths[i+1])
    Delta_X.append(deltax)  
print(Delta_X)

Coordinate_Y=[]  
Coordinate_Y.append(point_2_y)  
for i in range(len(Delta_Y)):  
    coordy = Coordinate_Y[i]+ Delta_Y[i]   
    Coordinate_Y.append(coordy)  
print(Coordinate_Y)

Coordinate_X=[]  
Coordinate_X.append(point_2_x)  
for i in range(len(Delta_X)):  
    coordx = Coordinate_X[i]+ Delta_X[i]
    Coordinate_X.append(coordx)  
print(Coordinate_X) 

Azimuths = ["%.4f" % member for member in Azimuths]  
Delta_Y = ["%.2f" % member for member in Delta_Y]  
Delta_X = ["%.2f" % member for member in Delta_X]  
Coordinate_Y = ["%.2f" % member for member in Coordinate_Y]
Coordinate_X = ["%.2f" % member for member in Coordinate_X]  

print("-"*73)  
print("%-15s %-15s %-15s %-15s  %s" %("Point ID", "Point ID", "Azimuth","Delta Y","Delta X"))  
print("-"*55)  
print("%-15s %-15s  %s" %(point_1, point_2, Azimuths[0])) 
for i in range(len(Delta_Y)):  
    print("%-15s %-15s %-15s %-15s %s" % (Points[i+1], Points[i+2], Azimuths[i+1],Delta_Y[i],Delta_X[i]))  

print("-" * 55)  
print("%-15s %-15s %s" %("Point ID","Coordinate(Y)","Coordinate(X)"))  
print("-" * 55)  
for i in range(len(Coordinate_Y) - 1):  
    print("%-15s %-15s %s" % (Points[i+2],Coordinate_Y[i+1], Coordinate_X[i+1]))  
  
print("-" * 55)

