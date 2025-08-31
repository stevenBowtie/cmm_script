import rhinoscriptsyntax as rs
selPts = rs.SelectedObjects()
pts = []
pts_coord = []
for pt in selPts:
    if rs.IsPoint:
        coord = rs.PointCoordinates( pt )
        pts.append( coord )
        pts_coord.append( coord )
rs.Command("LineThroughPt")
fitLine = rs.LastCreatedObjects()
dist = []
avg = 0
for pt in pts:
    closest = rs.LineClosestPoint( fitLine, pt )
    ptDist = rs.Distance( pt, closest )
    dist.append( ptDist )
    avg += ptDist
minimus = min( dist )
maximus = max( dist )
average = avg / pts.__len__()
print( "Min: " + str( minimus ) )
print( "Max: " + str( maximus ) )
print( "Avg: " + str( average ) )

for pt in range( pts.__len__() ):
    if( dist[pt] < 0 ):
        h = 85 - int( dist[pt] / minimus  * 170 )
    else:
        h = 85 - int( dist[pt] / maximus * 170 )
    rs.ObjectColor( selPts[pt], rs.ColorHLSToRGB( [ h, 100, 255] ) )
rs.UnselectAllObjects()