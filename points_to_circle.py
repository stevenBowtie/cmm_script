import rhinoscriptsyntax as rs
pts = rs.SelectedObjects()
print( pts[0] )