from tqdm import tqdm
import rasterio
import fiona
import os
from rasterio.mask import mask
from rasterio.plot import show
import matplotlib.pyplot as plt
import glob
path2021 = '/content/drive/MyDrive/com_ndvi/'
aoiFile = fiona.open('/content/drive/MyDrive/Varuna Hackathon 2022/training_area/traindata.shp')

for month in sorted([os.path.basename(a) for a in glob.glob(path2021 + '/*.jpg')])[0:6]:
  d = '/content/drive/MyDrive/arv/Nocloud/' + month 
  os.mkdir(d)
  for i in tqdm(range(len(aoiFile))):
    aoiGeom = [aoiFile[i]['geometry']]
    bandName = month
    rasterPath = path2021 + bandName
    rasterBand = rasterio.open(rasterPath)
    outImage, outTransform = mask(rasterBand, aoiGeom, crop = True)# crop=True)
    outMeta = rasterBand.meta
    outMeta.update({"driver": 'JP2OpenJPEG',
                    "height": outImage.shape[1],
                    "width": outImage.shape[2],
                    "transform": outTransform})

    outRaster = rasterio.open( d + '/' + str(i) + '.tif', "w", **outMeta) 
    outRaster.write(outImage)
    outRaster.close()