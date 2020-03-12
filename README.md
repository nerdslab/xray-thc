# Thalamocortical sample imaged with X-ray microCT
A three-dimensional X-ray microtomography thalamocortical dataset for characterizing brain heterogeneity: [Paper](http://bossdb.org/project/prasad2020), [Data](http://bossdb.org/project/prasad2020)

# Dataset Description
This dataset consists of a 3D brain volume, generated via microCT, spanning from hypothalamus to cortex. The dataset has dimension 720x1420x5805 (z,y,x), with a 1.17um isotropic voxel volume. The brain areas available are Cortex, Striatum, TRN, VP, Zona Incerta, Internal Capsule, Hypothalamus, and Corpus Callosum. Human-annotated ground truth data are available for both brain area classification and samples for microstructure segmentation of 4 brain areas.

<!---
![Raw Image Example Slice (z = 309)](https://github.com/nerdslab/xray-thc-data/blob/master/images/309_Raw-Data.png)
--->

Relevant notebooks:
1. [Pulling down raw data](https://github.com/nerdslab/xray-thc-data/blob/master/data_access_notebooks/raw_data_access.ipynb)

# Annotation Description
# Brain Area Classification
Brain area classification annotations are available for all brain areas. Complete human annotations of brain area are available for slices z = 109, 159, 209, 259, 309, 359, 409, 410, and 460. Thus, across each of these 9 slices, every pixel is labeled as belonging to one of the 8 brain areas mentioned in the dataset description. Interpolated annotations were computed and are made available for the slices between the human-annotated ones.

Brain areas were annotated with the following values: Clear Label = 0, Cortex = 1, Striatum = 2, TRN = 3, VP = 4, Zona Incerta = 5, Internal Capsule = 6, Hypothalamus = 7, Corpus Callosum = 8.

<!---
![Brain Area Annotation Sample](https://github.com/nerdslab/xray-thc-data/blob/master/images/Brain-Area-Annos.PNG)
--->

Relevant notebooks:
1. [Pulling down area-level annotations](https://github.com/nerdslab/xray-thc-data/blob/master/data_access_notebooks/roi_access.ipynb)
2. [Pulling down raw data only from ROI of choice](https://github.com/nerdslab/xray-thc-data/blob/master/data_access_notebooks/mask_roi_example.ipynb)

# Microstructure Segmentation
Microstructure segmentation (of cell bodies, blood vessels, and myelinated axons) are available for 4 regions of interest: Cortex, Striatum, Thalamus (mostly VP and some TRN), and Zona Incerta. For each of these 4 regions, there is a 256x256x360 (x,y,z) volume available for which slice z (0 indexed) = 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, and 330 have been densely annotated.

Microstructures were annotated with the following values: background = 0, cells = 1, blood vessels = 2, myelinated axons = 3.

<!---
![Microstructure Annotation Regions](https://github.com/nerdslab/xray-thc-data/blob/master/images/Microstructure-Annos.png)
--->

Relevant notebooks (please check requirements [here](https://github.com/nerdslab/xray-thc-data/tree/master/data_access_notebooks) before use):
1. [Pulling down pixel-level annotations](https://github.com/nerdslab/xray-thc-data/blob/master/data_access_notebooks/annotation_access.ipynb)
2. [Pulling down raw data and pixel-level annotations jointly](https://github.com/nerdslab/xray-thc-data/blob/master/data_access_notebooks/training_data_access.ipynb)

# Data Access
Python notebooks for pulling down the data from BossDB, along with an instructional README, are provided in the "data_access_notebooks" directory.
