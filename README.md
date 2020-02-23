# xray-thc-data
x-ray microCT dataset from a thalamocortical section of mouse brain

# Dataset Description
This dataset consists of a 3D brain volume, generated via microCT, spanning from hypothalamus to cortex. The dataset has dimension 720x1420x5805 (z,y,x), with a 1.17um isotropic voxel volume. The brain areas available are Cortex, Striatum, TRN, VP, Zona Incerta, Internal Capsule, Hypothalamus, and Corpus Callosum. Human-annotated ground truth data are available for both brain area classification and samples for microstructure segmentation of 4 brain areas.

# Annotation Description
# Brain Area Classification
Brain area classification annotations are available for all brain areas. Complete human annotations of brain area are available for slices z = 109, 159, 209, 259, 309, 359, 409, 410, and 460. Thus, across each of these 9 slices, every pixel is labeled as belonging to one of the 8 brain areas mentioned in the dataset description. Interpolated annotations were computed and are made available for the slices between the 9 human-annotated slices.

# Microstructure Segmentation
Microstructure segmentation (of cell bodies, blood vessels, and myelinated axons) are available for 4 brain areas: Cortex, Striatum, TRN, and Zona Incerta. For each of these 4 brain areas, there is a 256x256x360 (x,y,z) volume for which slice z = 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, and 330 have been densely annotated.

# Data Access
Python notebooks for pulling down the data from BossDB, along with an instructional README, are provided in the "data_access_notebooks" directory.