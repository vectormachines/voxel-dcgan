### binvox2stl

Converts a binary voxelgrid (.binvox) file into a mesh file (.STL) using the [Marching Cubes method](https://en.wikipedia.org/wiki/Marching_cubes).
It makes use of [binvox-rw-py](https://github.com/dimatura/binvox-rw-py) and [TriMesh](https://github.com/mikedh/trimesh) libraries.

**Usage:**

```
python binvox2mesh.py <FILENAME>
```

Example:
```
python binvox2mesh.py sample_model.binvox
```

You can view your generated meshes with MeshLab or https://3dviewer.net/ or any other STL mesh viewer.