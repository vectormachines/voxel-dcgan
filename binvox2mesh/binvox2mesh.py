import numpy as np
import trimesh # for converting voxel grids to meshes (to import objects into simulators)
# trimesh==2.38.42 was the version that worked
import time # to know how long it takes for the code to run
import os # to walk through directories, to rename files
import sys

import binvox_rw # to manipulate binvox files

# Parses a file of type BINVOX
# Returns a voxel grid, generated using the binvox_rw.py package
def parse_BINVOX_file_into_voxel_grid(filename):
    filereader = open(filename, 'rb')
    binvox_model = binvox_rw.read_as_3d_array(filereader)
    voxelgrid = binvox_model.data
    return voxelgrid

if __name__ == "__main__":
    
    print("Usage: ")
    print("python binvox2mesh.py <FILEPATH>")
    
    filename = sys.argv[1]
    
    # Load the voxelgrid from file
    voxelgrid = parse_BINVOX_file_into_voxel_grid(filename)

    mesh = trimesh.voxel.matrix_to_marching_cubes(
        matrix=voxelgrid,
        pitch=1.0,
        origin=(0,0,0))

    print("Merging vertices closer than a pre-set constant...")
    mesh.merge_vertices()
    print("Removing duplicate faces...")
    mesh.remove_duplicate_faces()
    print("Scaling...")
    mesh.apply_scale(scaling=1.0)
    print("Making the mesh watertight...")
    trimesh.repair.fill_holes(mesh)
    print("Fixing inversion and winding...")
    trimesh.repair.fix_inversion(mesh)
    trimesh.repair.fix_winding(mesh)

    print("Generating the STL mesh file")
    trimesh.exchange.export.export_mesh(
        mesh=mesh,
        file_obj=filename + ".stl",
        file_type="stl"
    )