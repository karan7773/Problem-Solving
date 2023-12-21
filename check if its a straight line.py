def checkStraightLine(coordinates):
    (x0,y0),(x1,y1)=coordinates[0],coordinates[1]
    for x,y in coordinates[2:]:
        if (x0-x1)*(y1-y)!=(x1-x)*(y0-y1):
            return False
    return True

print(checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))
print(checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))