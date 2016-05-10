"""
Simple way to export SGeMS data to Paraview;
Need to install python module pyevtk;
In this file, direction data is exported as vector to be visulized at Paraview (after Glyph filter)
The output file goes to SGeMS main folder as "points.vtu"
"""

import numpy as np 
import sgems
from pyevtk.hl import pointsToVTK


# Input properties (NEED TO INPUT grid name, direction data and ratio for coloring)
grid = "grid1"
direction_data = "05strike"
ratio_data = "05ratio"

# Initializing
prop = sgems.get_property(grid,direction_data)
ratio = sgems.get_property(grid,ratio_data)

propX = sgems.get_property(grid,"_X_")
propY = sgems.get_property(grid,"_Y_")
propZ = sgems.get_property(grid,"_Z_")
npoints = len(propX)

x = np.array(propX)
y = np.array(propY)
z = np.array(propZ)
vx = np.zeros(npoints)  
vy = np.zeros(npoints)  
vz = np.zeros(npoints)
rang = np.zeros(npoints)

# Calculating vectors to display at Paraview as Glyph
for i in range(npoints):
	vx[i] = np.sin(np.deg2rad(prop[i]))
	vy[i] = np.cos(np.deg2rad(prop[i]))
	if (ratio[i] < 0.2): rang[i] = 1/0.2
	else: rang[i] = 1/ratio[i]

pointsToVTK("./points", x, y, z, data = {"direction" : (vx, vy, vz), "range" : rang})
print "Done"
