"""
Various functions for transforming STEP files, and converting to WRL files
"""

import FreeCAD, FreeCADGui, Draft, ImportGui

import sys, os

FreeCADGui.ActiveDocument.ActiveView.setAxisCross(True)

def getTempStepFile():
    step = os.path.split(getStepFile())
    
    print(step)
    
    return os.path.join(step[0],"tmp_" + step[1])

def getStepFile():
    step = sys.argv[1]
    filePath = os.path.dirname(os.path.abspath(__file__))
    if not os.path.isabs(step):
        step = os.path.join(filePath,step)
    return step
    
def getWRLFile():
    return ".".join(getStepFile().split(".")[:-1]) + ".wrl"
    

#find and return all objects
def getAll():
    return FreeCAD.ActiveDocument.Objects
    
def scale():
    #scaling factor
    scaling = 1.0 / 2.54

    scale = FreeCAD.Vector(scaling,scaling,scaling)
    origin = FreeCAD.Vector(0,0,0)

    for obj in getAll():
        Draft.scale(obj, delta=scale, center=origin, legacy=True, copy=False)
        
def saveSTEP(filename):
    objs = getAll()
    
    ImportGui.export(objs,filename)
        
def saveWRL(filename):
    objs = []
    
    for obj in getAll():
        FreeCADGui.Selection.addSelection(obj)
        objs.append(obj)
        
    FreeCADGui.export(objs, filename)
    
    del objs
        
#rotate 90 degrees across 
def rotate(axes):

    objs = getAll()

    origin = FreeCAD.Vector(0,0,0)
    x,y,z = axes
    axis = FreeCAD.Vector(axes)
    
    Draft.rotate(objs,
                90.0,
                origin,
                axis=axis,
                copy=False)
                
def rotate_x():
    rotate((1,0,0))
    
def rotate_y():
    rotate((0,1,0))
    
def rotate_z():
    rotate((0,0,1))