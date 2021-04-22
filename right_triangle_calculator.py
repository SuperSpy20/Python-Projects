import math
try:
    p = float(input("What is the angle you are measuring (in degrees)?\n"))
    c_given = input("Is the given leg the hypotenuse, opposite, or adjacent?\n").lower()
    c_1 = float(input("What is the length of the given leg?\n"))

    if p < 0.0:
        p = abs(p)
    
    if p >= 90.0:
        print("\n\nThe angle you are measuring must be acute!")
        exit()
    
    if "hyp" in c_given:
        x = True
        #print("{}#1".format(x))
    else:
        x = False
        #print("{}#1_1".format(x))
        
        
    if "opp" in c_given:
        y = True
        #print("{}#2".format(y))
    else:
        y = False
        #print("{}#2_1".format(y))
        
        
    if "adj" in c_given:
        z = True
        #print("{}#3".format(z))
    else:
        z = False
        #print("{}#3_1".format(z))
    
    opp_angle = (90)-(p)
    
except:
    print("\n\nYou must specify the missing leg!")
    exit()

def angle_leg_algebra(p, c_1):
    if x == True:
        hyp = c_1
        
        s = math.sin(math.radians(p))
        s = round(s, 2)
        
        opp = (s)*(c_1)
        opp = round(opp, 2)
        
        g = math.cos(math.radians(p))
        g = round(g, 2)
        
        adj = (c_1)/(1)
        adj = (g)*(adj)
        adj = round(adj, 2)
        
        v = "Opposite Leg: {}\nHypotenuse: {}\nAdjecent Leg: {}\nOpposite Angle: {}".format(opp, hyp, adj, opp_angle)
        return v
        
    if y == True:
        s = math.sin(math.radians(p))
        s = round(s, 2)
        
        hyp = (c_1)/(s)
        hyp = round(hyp, 2)
        
        opp = c_1
        
        t = math.tan(math.radians(p))
        t = round(t, 2)
        
        adj = (c_1)/(t)
        adj = round(adj, 2)
        
        v = "Opposite Leg: {}\nHypotenuse: {}\nAdjecent Leg: {}\nOpposite Angle: {}".format(opp, hyp, adj, opp_angle)
        return v
        
    if z == True:
        c = math.cos(math.radians(p))
        c = round(c, 2)
        
        adj = c_1
        
        hyp = (c_1)/(c)
        hyp = round(hyp, 2)
        
        s = math.sin(math.radians(p))
        s = round(s, 2)
        
        opp = (s)*(c_1)
        opp = round(opp, 2)        
        
        v = "Opposite Leg: {}\nHypotenuse: {}\nAdjecent Leg: {}\nOpposite Angle: {}".format(opp, hyp, adj, opp_angle)
        return v
        
j = angle_leg_algebra(p, c_1)

print("\n{}".format(j))