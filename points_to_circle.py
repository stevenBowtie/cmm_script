import rhinoscriptsyntax as rs
selPts = rs.SelectedObjects()
pts = []
for pt in selPts:
    if rs.IsPoint:
        coord = rs.PointCoordinates( pt )
        pts.append( coord )
rs.Command("Circle f")
fitCirc = rs.LastCreatedObjects()
centerPoint = rs.CircleCenterPoint( fitCirc[0] )
rad = rs.CircleRadius( fitCirc )
dist = []
avg = 0
for pt in pts:
    ptDist = rs.Distance( centerPoint, pt )
    dist.append( ptDist - rad )
    avg += ptDist - rad
minimus = min( dist )
maximus = max( dist )
average = avg / pts.__len__()
print( "Radius: " + str( rs.CircleRadius( fitCirc ) ) )
print( "Min: " + str( minimus ) )
print( "Max: " + str( maximus ) )
print( "Avg: " + str( average ) )
#print( pts )