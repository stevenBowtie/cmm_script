import rhinoscriptsyntax as rs
selPts = rs.SelectedObjects()
pts = []
for pt in selPts:
    if rs.IsPoint:
        coord = rs.PointCoordinates( pt )
        pts.append( coord )
rs.Command("Circle f")
fitCirc = rs.LastCreatedObjects()
print( rs.CircleCenterPoint( fitCirc[0] ) )
print( pts )