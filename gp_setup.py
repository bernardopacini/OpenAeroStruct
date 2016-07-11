# Setup the aerostruct data using OpenMdDAO

# In Matlab code, add this before calling Python functions:
#   if count(py.sys.path,'') == 0
#       insert(py.sys.path,int32(0),'');
#   end

from __future__ import division
import numpy
import sys
import os

# get OpenAeroStruct files from parent directory
from pathlib import Path
sys.path.append(str(Path('.').absolute().parent))

from geometry import mesh_gen
from spatialbeam import radii

def setup(num_inboard=2, num_outboard=3):
    # Create the mesh from inboard points and outboard points
    mesh = mesh_gen(num_inboard, num_outboard)
    num_x = mesh.shape[0]
    num_y = mesh.shape[1]
    r = radii(mesh)
    t = r/10

    # Define the aircraft properties
    from CRM import span, v, alpha, rho

    des_vars = [
        ('twist', numpy.zeros(num_y)),
        ('span', span),
        ('v', v),
        ('alpha', alpha),
        ('rho', rho),
        ('disp', numpy.zeros((num_y, 6))),
        ('r', r),
        ('t', t),
    ]

    return {'mesh':mesh, 'num_x':num_x, 'num_y':num_y, 'des_vars':des_vars}

if __name__ == '__main__':
    setup()
