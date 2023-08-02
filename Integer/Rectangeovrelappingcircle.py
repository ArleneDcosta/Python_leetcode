def checkOverlap(r, x_center, y_center, x1, y1, x2, y2):
        return ((x1 <= x_center <= x2
                 and y1 <= y_center + r and y_center - r <= y2) or
                (y1 <= y_center <= y2
                 and x1 <= x_center + r and x_center - r <= x2) or
                min(pow(pow(x1 - x_center, 2) + pow(y1 - y_center, 2), 0.5),
                    pow(pow(x1 - x_center, 2) + pow(y2 - y_center, 2), 0.5),
                    pow(pow(x2 - x_center, 2) + pow(y1 - y_center, 2), 0.5),
                    pow(pow(x2 - x_center, 2) + pow(y2 - y_center, 2), 0.5)) < r)
#x_right = x_center + radius;
#x_left = x_center - radius;
#y_top = y_center + radius;(top of circle)
#y_bottom = y_center - radius;(bottom of circle)
#first checks if circle partially lies along the xaxis
#second checks if circle patially lies along the y axis
#above can be valid if circle lies along specific axis in rect
#if rectangle completely in circle then check can be done in last method
if checkOverlap(1,0,0,1,-1,3,1):
    print("Yes Circle and Rectangle overlap each other")
else:
    print("No Circle and Rectangle do not overlap each other")
