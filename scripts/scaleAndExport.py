#scale a shape to inches for VRML KiCAD export
import FreeCAD
import ImportGui
import FreeCADGui
import Gui
import Mesh

Gui.ActiveDocument.ActiveView.setAxisCross(True)

inches = 1.0 / 2.54

matrix = FreeCAD.Matrix()
matrix.scale(inches,inches,inches)

parts = App.ActiveDocument.findObjects()

for part in parts:
    part.Shape = part.Shape.transformGeometry(matrix)
    
Mesh.export(parts,"C:/Path/to/file.wrl")