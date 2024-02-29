该程序的作用是应用gdal库,使用python脚本形式完成卫星数据转化为WRF能使用静态地理数据，既将HDF文件转化为"00001.xxxxx-00001.xxxxx"的二进制文件。可直接在服务器上运行。

文件架构
-HDFGEO
 |- Hdf_to_GEO.py : 原始的卫星数据转换为WRF能用的静态地形数据
 |- Makseindex.py : 制作WPS静态下垫面的index（说明）文件
 |- README : 说明文件
 |- gdal.yaml:安装gdal环境的yml文件，具体使用`conda env create --file gdal.yaml`