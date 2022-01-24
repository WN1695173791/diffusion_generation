import numpy as np
from open3d import*

source_data = np.load('/home/bixueting/code/diffusion-point-cloud/results/GEN_Ours_airplane_1640675021/out.npy')[:,0:3]  #10000x3
print(source_data.shape)
point_cloud = open3d.geometry.PointCloud()
point_cloud.points = open3d.utility.Vector3dVector(source_data)
open3d.visualization.draw_geometries([point_cloud])
