import rhinoscriptsyntax as rs
selPts = rs.SelectedObjects()
pts = []
for pt in selPts:
    if rs.IsPoint:
        pts.append( pt )
rs.Command( "PlaneThroughPt" )
pln = rs.LastCreatedObjects()
deviations = []
avg = 0
for pt in pts:
    closest = rs.SurfaceClosestPoint( pln, pt )
    p3d = rs.EvaluateSurface( pln, closest[0], closest[1] )
    dev = rs.Distance( pt, p3d )
    deviations.append( dev )
    avg += dev

minimus = min( deviations )
maximus = max( deviations )
average = avg / deviations.__len__()

print( "Min: " + str( minimus ) )
print( "Max: " + str( maximus ) )
print( "Avg: " + str( average ) )
#print( "Std Dev: " + str( stats.stdev( deviations ) ) )

rs.SetUserText( pln, "Min", str( minimus ) )
rs.SetUserText( pln, "Max", str( maximus ) )
rs.SetUserText( pln, "Avg", str( average ) )

for pt in range( pts.__len__() ):
    if( deviations[pt] < 0 ):
        h = 85 - int( deviations[pt] / minimus  * 170 )
    else:
        h = 85 - int( deviations[pt] / maximus * 170 )
    rs.ObjectColor( selPts[pt], rs.ColorHLSToRGB( [ h, 100, 255] ) )
rs.UnselectAllObjects()