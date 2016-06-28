"""
Simple way to export SGeMS data to Paraview;
Need to install python module pyevtk;
In this file, data is exported as structured grid to be visulized at Paraview
The output file goes to SGeMS main folder as '.vtu'
"""


from pyevtk.hl import gridToVTK 
import numpy as np 
import sgems

# Parameters (NEED TO INPUT grid name and property name)
g = "grid1"
p = "30strike"

prop = sgems.get_property(g,p)

# Grid parameters (NEED TO INPUT lx, ly and lz as the dimensions of the grid)
nd = sgems.get_dims(g)
ox, oy, oz = 0.0, 0.0, 0.0
lx, ly, lz = 260.0, 300.0, 1.0 
dx, dy, dz = lx/nd[0], ly/nd[1], lz/nd[2] 
ncells = nd[0] * nd[1] * nd[2] 
npoints = (nd[0] + 1) * (nd[1] + 1) * (nd[2] + 1) 

# Coordinates 
x = np.arange(ox, ox + lx + 0.1*dx, dx, dtype='float64') 
y = np.arange(oy, oy + ly + 0.1*dy, dy, dtype='float64') 
z = np.arange(oz, oz + lz + 0.1*dz, dz, dtype='float64') 

# Writing output
output = np.array(prop)

# Variables 
gridToVTK("./structured", x, y, z, cellData = {p : output})

print "Done"
