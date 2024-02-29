################################################################
# Version: 1.0
# Author: 戴泽凯(dzk)
# email: 1553324512@qq.com
# Date: 2024-02-28 
# Description: 将原始的卫星数据（eg:MODIS）转化为TIF格式文件,并且转
#              化为00001.xxxxx-00001.xxxxx二进制文件
# example: python Hdf_to_GEO.py
################################################################
import re
import os 
import glob

inputpath=r'E:\mcd12\mcd12\*.hdf'# HDF文件列表
outpath_tif=r"E:\Python\Tif"         # TIF文件输出位置
hdf_files = glob.glob(inputpath) # 添加所有HDF文件的路径


# 检查文件夹是否存在
if not os.path.exists(outpath_tif):
    os.makedirs(outpath_tif)
# 提取HDF，转换投影，双线性插值采样，将格式转换为tif，以便后续套作
for i in range(len(hdf_files)):
    outfile=os.path.join(outpath_tif,f"out{i}.tif")
    subfile=f"HDF4_EOS:EOS_GRID:\"{hdf_files[i]}\":MCD12Q1:LC_Type1" #这里具体要根据文件格式和需要的波段进行调整，update
    gdal_command=f"gdalwarp -t_srs  EPSG:4326 -r  bilinear {subfile}  {outfile}"
    os.system(gdal_command)

# 合并为一个tif文件
Tiffile =  glob.glob(os.path.join(outpath_tif,'*.tif'))
separator = " "
gdal_command1=f"gdal_merge.py -o output.tif {separator.join(Tiffile)}"
os.system(gdal_command1)

# 转化为二进制文件
gdal_command2=f"gdal_translate -of ENVI -co INTERLEAVE=BSQ output.tif data.bil"
os.system(gdal_command2)
hdr_file=r'data.hdr'
with open(hdr_file, 'r') as f:
    text=f.read()

# 必要信息
pattern =  r'samples =\s*(\d+)'
tile_x = int(re.findall(pattern ,text)[0])
pattern =  r'lines   =\s*(\d+)'
tile_y = int(re.findall(pattern ,text)[0])
# 改名
out_name=f'00001-{str(tile_x).zfill(5)}.00001-{str(tile_y).zfill(5)}'
os.rename('data.bil',out_name)