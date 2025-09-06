import rhinoscriptsyntax as rs
selPts = rs.SelectedObjects()
pts = []
for pt in selPts:
    if rs.IsPoint:
        pts.append( pt )
rs.Command( "PlaneThroughPt" )
pln = rs.LastCreatedObjects()
#pln = rs.PlaneFitFromPoints( pts )
#if pln:
#    magX = pln.XAxis.Length
#    magY = pln.YAxis.Length
#    rs.AddPlaneSurface( pln, magX, magY )
deviations = []
for pt in pts:
    closest = rs.PlaneClosestPoint( pln, pt )
    dev = rs.Distance( pt, closest )
    deviations.append( dev )
print( deviations )