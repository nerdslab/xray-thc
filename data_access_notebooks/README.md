# Example Code for Access and Manipulation of X-ray Microtomography data in BossDB
### "A three-dimensional X-ray microtomography dataset for characterizing heterogeneity across brain areas" (Prasad et al.)

This repository provides example Jupyter notebooks for access and visualization of the data described in the paper "A three-dimensional X-ray microtomography dataset for characterizing heterogeneity across brain areas". 

The paper introduces a 3D neuroanatomical dataset which encompasses both heterogeneous ROIs and diverse microstructures including: axons, cell bodies and blood vessels (vasculature). An in vitro sample was used in slice physiology and imaged with X-ray microCT. The overall dataset is 720x1420x5805 pixels, with a 1.17um isotropic voxel volume. Cutouts outside of this volume will return 0 values. _Note: Z slices containing tissue range from index 15-680. Beyond this, the volume is padded with mostly dark pixels. All raw images are type unit8, and all annotations are type uint64._

The dataset contains regions of cortex (CTX), zona incerta (ZI), ventral posterior thalamic nucleus (VP), thalamic reticular nucleus (TRN), striatum (STR), hypothalamus (HYP).

The notebooks below provide examples for how to access arbitrary cutouts of the data (images), key human-annotated Regions of Interest (ROIs), and pixel-level annotations that include labels for blood vessels, cell bodies, and white matter.  Finally, example workflows, compatible with the SABER project, are provided to deploy tools, such as segmentation algorithms, to the entire dataset.

## Requirements for Jupyter Notebooks
* Python 3.x (https://www.python.org/)
* Jupyter notebook (https://jupyter.org/)
You'll want to make sure these are installed if you plan to use the python API to access the data.

Required Python packages are listed in requirements.txt. Navigate to the folder you downloaded using your command line.
Using pip (https://docs.python.org/3/installing/index.html), you can install them with 
```bash
pip install -r requirements.txt
```

When using these notebooks, the data at https://bossdb.org/project/prasad2020 is accessed.

## Example notebooks
In the folder data_access, there are the following examples
* access of an arbitrary cutout of the raw data (raw_data_access.ipynb) including saving to numpy, hdf5, and tiff formats
* access of pixel annotations (annotation_access.ipynb)
* access of regions of interest (roi_access.ipynb)
* Joint pull of pixel annotations and raw data for training machine learning algorithms for cell body, vasculature, and white matter segmentation(training_data_access.ipynb)
* Pull low-resolution version of entire volume and ROIs for quick analysis (low_res_volume.ipynb)
* Pulling data masked using from the ROIs (e.g. display raw data from striatum) (mask_roi_example.ipynb)

To run these notebooks, please clone this repository (git clone: https://git-scm.com/docs/git-clone) and navigate to the folder using your command line.
If you have not installed the necessary packages, run the pip install line above. 
If using jupyter notebook, please run 
```bash
jupyter notebook
```
from your command line, then open a browser of your choice, and navigate to http://localhost:8888 and select the appropriate notebook. This will open in a new tab. 

## Docker Image (Optional)
You can also use Docker CE (https://docs.docker.com/install/linux/docker-ce). If you have docker installed, this method will require no additional installation of packages or software to your environment. This is very useful if you have any problems installing the above open source software tools with pip. Alternatively, if you have problems with conflicting software versions, this is a powerful approach.
To run using the docker container, navigate to the folder where you cloned this repository and run the following:
```bash
docker build -t xray_access .
docker run -p 8888:8888 -v $(pwd)/data:/home/jovyan/app/data -it xray_access
jovyan@761b7fd9f032:~/app$ jupyter notebook
```
Using a web browser, navigate to http://localhost:8888 after running these commands. 
As the notebook opened in a docker container, it may require a password, find the line 'token=' on your command line and copy the section after the equals sign as the security token for jupyter in your web browser. This should start the notebook

## Options for further processing (Optional)
Further processing tools and common workflow language processing pipelines for these data can be found at the SABER project: 
https://github.com/aplbrain/saber
https://github.com/aplbrain/saber/wiki/Example-workflow:-XBrain

## Troubleshooting
Errors installing Blosc. This can be particularly true with Windows 10
If you get an error message requiring “Build Tools for Visual Studio”, you must download visual studio. https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=16
Download and install (indicate C++ when prompted). After this, attempt to pip install blosc again. 

