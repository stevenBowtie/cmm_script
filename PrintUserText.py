import rhinoscriptsyntax as rs
sel = rs.SelectedObjects()
ut = rs.GetUserText( sel )
for k in ut:
    print( k +": "+ rs.GetUserText( sel, k ) )