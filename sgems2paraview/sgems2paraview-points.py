"""
Simple way to export SGeMS data to Paraview;
Need to install python module pyevtk;
In this file,data is exported as points to be visulized at Paraview
The output file goes to SGeMS main folder as "points.vtu"
"""

import numpy as np 
import sgems
from pyevtk.hl import pointsToVTK


# Input properties (NEED TO INPUT grid object name and property name)
grid = "walker"
point_data = "V"

# Initializing
prop = sgems.get_property(grid,point_data)

propX = sgems.get_property(grid,"_X_")
propY = sgems.get_property(grid,"_Y_")
propZ = sgems.get_property(grid,"_Z_")
npoints = len(propX)

x = np.array(propX)
y = np.array(propY)
z = np.array(propZ)
output = np.array(prop)

# Output
pointsToVTK("./points", x, y, z, data = {point_data : output})

print "Done"
