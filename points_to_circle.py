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
rs.AddPoint( centerPoint )
rad = rs.CircleRadius( fitCirc )
dist = []
avg = 0
for pt in pts:
    ptDist = rs.Distance( centerPoint, pt )
    dist.append( ptDist - rad )
    avg += abs( ptDist - rad )
minimus = min( dist )
maximus = max( dist )
average = avg / pts.__len__()
print( "Diameter: " + str( rs.CircleRadius( fitCirc ) * 2 ) )
print( "Min: " + str( minimus ) )
print( "Max: " + str( maximus ) )
print( "Avg: " + str( average ) )
rs.SetUserText( fitCirc, "Diameter", str( rs.CircleRadius( fitCirc ) * 2 ) )
rs.SetUserText( fitCirc, "Min", str( minimus ) )
rs.SetUserText( fitCirc, "Max", str( maximus ) )
rs.SetUserText( fitCirc, "Avg", str( average ) )

for pt in range( selPts.__len__() ):
    if( dist[pt] < 0 ):
        h = 85 - int( dist[pt] / minimus  * 170 )
    else:
        h = 85 - int( dist[pt] / maximus * 170 )
    rs.ObjectColor( selPts[pt], rs.ColorHLSToRGB( [ h, 100, 255] ) )
rs.UnselectAllObjects()