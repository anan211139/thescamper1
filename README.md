# Note Here
Firstly, we use QGIS to preprocess the data, then export the NVDI data into picture which each pixel store the value. In order to train the model, we classify the value into each class. After finished training the model, we try to use the python to preprocess the data instead of QGIS, but due to the limited of time we cannot finished it. The files we cannot finished in time (not use) are Clip_vector.py, NDVI_remove_cloud.ipynb.
# Varuna crop classification Hackathon
   We use the Catboost model to classify crops from the Sentinel-2 satellite. Initially, we explored data from QGIS software. The concept of the model is to use the time series of the median NDVI Index to analyze and classify the period of the planting cycle. 
# Data Data Acquisition
   The data filted from at most 15% percentage of the cloud in each day and then we split satellite images to small crops from vector data(.shp file).
# Preprocess
   NDVI_remove_cloud.ipynb - Calculated NDVI from band 4 and band NIR\
   Clip_vector.py - Crop Aoi to images\
   Preprocess.ipynb - The process is continued after we acquire the EVI value from each field in the picture.
   
   All data and preprocess file with details can be downloaded from here
   https://drive.google.com/drive/u/0/folders/1lvnMZit9gLAIJOdRBzxBo4DTGd4hIX8h
# Model
   Catboost.ipynb - Catboost model
