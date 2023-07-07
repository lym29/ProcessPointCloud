import os
import pclpy
from pclpy import radius_outlier_removal

data_path = "./data/"
# read a las file
# point_cloud = pclpy.read(os.path.join(data_path, "111.off"), "PointXYZRGBA")
input_pc = pcl.PointCloud.PointXYZRGBA()
output_pc = pcl.PointCloud.PointXYZRGBA()

pcl.FileReader(os.path.join(data_path, "111.off"), input_pc)

sor = pcl.StatisticalOutlierRemoval.PointXYZRGBA()
sor.setInputCloud(input_pc)
sor.setMeanK(50)
sor.setStddevMulThresh(1.0)
sor.filter(output_pc)

pcl.FileWriter(os.path.join(data_path, "111_filtered.xyz"), output_pc)