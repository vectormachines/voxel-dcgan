import numpy as np
import glob
import scipy.io as io
import scipy.ndimage as nd

def get3DImage(data_dir):
    return getVoxelsFromMat(data_dir, cube_len=64)

def getVoxelsFromMat(path, cube_len=64):
    voxels = io.loadmat(path)['instance']
    voxels = np.pad(voxels, (1, 1), 'constant', constant_values=(0, 0))
    if cube_len != 32 and cube_len == 64:
        voxels = nd.zoom(voxels, (2, 2, 2), mode='constant', order=0)
    return voxels

def read_mat(filename):
  volumes = get3DImage(filename)
  return np.expand_dims(volumes, -1)

def save_mat(filename, data):
    io.savemat(filename, data)