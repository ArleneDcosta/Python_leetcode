import itertools
from itertools import combinations
def rectangleArea(rectangles):
    def intersect(rec1, rec2):
        print 'Inside rec1 and rec2'
        print 'rect1',rec1
        print 'rect2',rec2
        return [max(rec1[0], rec2[0]),
                    max(rec1[1], rec2[1]),
                    min(rec1[2], rec2[2]),
                    min(rec1[3], rec2[3])]

    def area(rec):
        print 'In area',rec
        dx = max(0, rec[2] - rec[0])
        dy = max(0, rec[3] - rec[1])
        return dx * dy

    ans = 0
    for size in xrange(1, len(rectangles) + 1):
        for group in itertools.combinations(rectangles, size):
            print 'group',size,group
            print 'prev',ans,(size + 1),area(reduce(intersect, group))
            ans += (-1) ** (size + 1) * area(reduce(intersect, group))
            print 'ans',ans

    return ans % (10**9 + 7)

print rectangleArea([[0,0,2,2],[1,0,2,3],[1,0,3,1]])
#first area of individual rect boxes are computed and then added together
# when size is two intersection is removed of individual boxes
# common is added of all the three
