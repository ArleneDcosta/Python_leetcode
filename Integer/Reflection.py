def mirrorReflection(p, q):
    from fractions import Fraction as F

    x = y = 0
    rx, ry = p, q
    #that means receptors are reached
    targets = [(p, 0), (p, p), (0, p)]

    while (x, y) not in targets:
        #Want smallest t so that some x + rx, y + ry is 0 or p
        #x + rxt = 0, then t = -x/rx etc.
        t = float('inf')
        for v in [F(-x,rx), F(-y,ry), F(p-x ,rx), F(p-y,ry)]:
            if v > 0: t = min(t, v)

        x += rx * t
        y += ry * t

        #update rx, ry
        if x == p or x == 0: # bounced from east/west wall, so reflect on y axis
            rx *= -1
        if y == p or y == 0:
            ry *= -1

    return 1 if x==y==p else 0 if x==p else 2
print mirrorReflection(2,1)
'''
The parameterized position of the laser after time t will
be (x + rx * t, y + ry * t). From there, we know when it will meet the east
wall (if x + rx * t == p), and so on. For a positive (and nonnegligible) time t,
it meets the next wall.

We can then calculate how the ray reflects. If it hits an east or west wall,
then rx *= -1, else ry *= -1.'''
