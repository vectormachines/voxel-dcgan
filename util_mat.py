import numpy as np
import glob
import scipy.io as io
import scipy.ndimage as nd

def get3DImages(filename):
    all_files = np.random.choice(glob.glob(filename), size=10)
    all_volumes = np.asarray([getVoxelsFromMat(f) for f in all_files], dtype=np.bool)
    return all_volumes

def getVoxelsFromMat(path, cube_len=64):
    voxels = io.loadmat(path)['instance']
    voxels = np.pad(voxels, (1, 1), 'constant', constant_values=(0, 0))
    if cube_len != 32 and cube_len == 64:
        voxels = nd.zoom(voxels, (2, 2, 2), mode='constant', order=0)
    return voxels

def read_mat(filename):
  volumes = get3DImages(filename=filename)
  volumes = volumes[..., np.newaxis].astype(np.float)
  return volumes[0]

def save_mat(filename, data):
    io.savemat(filename,volumes)