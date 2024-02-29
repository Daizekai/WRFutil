################################################################
# Version: 1.0
# Author: 戴泽凯(dzk)
# email: 1553324512@qq.com
# Date: 2024-02-28 
# Description: 制作WPS静态下垫面的index（说明）文件
# example: python Makeindex.py
################################################################
import re
# 读取上一步生成的头文件信息，用来制作index
hdr_file=r'E:\Python\data.hdr'
with open(hdr_file, 'r') as f:
    text=f.read()

# 必要信息
pattern =  r'samples =\s*(\d+)'
tile_x = int(re.findall(pattern ,text)[0])
pattern =  r'lines   =\s*(\d+)'
tile_y = int(re.findall(pattern ,text)[0])
pattern = r"map info = \{Geographic Lat/Lon, 1, 1, (.*?),WGS-84\}"
data=re.findall(pattern ,text)[0].split(',')
known_lon=float(data[0])
dx=float(data[-1])
dy=float(data[-1])
known_lat=float(data[1])-dy*tile_y

#编写index文件
#>#################################################################<#
# 原文链接：https://blog.csdn.net/weixin_42181785/article/details/114178200
# 补充： dzk
# type                  :为文件描述类型
# category_min          :分类代码的最小值
# category_max          :分类代码的最大值
# projection            :投影类型
# dx                    :横向格点间的间隔，即栅格影像的横向分辨率
# dy                    :纵向格点间的间隔，即栅格影像的纵向分辨率
# known_x               :指定一个标记点横向坐标
# known_y               :指定一个标记点纵向坐标
# known_lat             :标记点横向坐标的纬度
# known_lon             :标记点纵向坐标的经度
# tile_x                :横向格点数
# tile_y                :纵向格点数
# units                 :格点值的单位
# description           :文件描述,须有双引号
# iswater               :水体类别的编号
# islake                :湖泊类别的编号
# isice                 :冰川类别的编号
# isurban               :城市类别的编号
# row_order=top_bottom  :WRF默认读取顺序是数组bottom_top
#>#################################################################<#                  
with open('index', 'a') as f:
    f.write("projection = regular_ll\n")
    f.write("known_x = 1 \n")
    f.write("known_y = 1 \n")
    f.write(f"known_lat = {known_lat}\n")
    f.write(f"known_lon = {known_lon}\n")
    f.write(f"dx = {dx} \n")
    f.write(f"dy = {dy} \n")
    f.write(f"tile_x = {tile_x} \n")
    f.write(f"tile_y = {tile_y} \n")
    f.write(f"tile_z = 1 \n")
    f.write("type = categorical\n")
    f.write("category_min = 1\n")
    f.write("category_max = 21\n")
    f.write("mminlu = \"MODIFIED_IGBP_MODIS_NOAH\" \n")
    f.write("iswater = 17\n")
    f.write("isurban = 13\n")
    f.write("units = \"category\"\n")
    f.write("description = \"500m 17-category IGBP-MODIS landuse(China)\"\n")
    f.write("wordsize = 1\n")
    f.write("missing_value = 0.00 \n")
    f.write("row_order=top_bottom\n")
