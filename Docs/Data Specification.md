<h1 align="center">Develop Log</h1>

This file documents all the necessary information about developing 

- Write ipynb file to read h5 file
- transform dicom image to numpy array and then write it to h5
- extract 2d landmarks from the output of synthex 
- write fcsv file



# Developed Features

- [x] image conversion from dicom to synthex required h5
- [x] 2D annotation result decoded from the resulting h5 of synthex
- [x] 3D landmarks conversion to the required format of xReg
- [x] image conversion from dicom to xReg required h5
- [x] scripts to call synthex to annotate and call xReg to get registration result



- [x] modularized classed to contain everything
- [ ] environment compatibility check
- [ ] integrate into a full pip package
- [ ] colab script to demonstrate
- [ ] performance analysis: frame rate
- [ ] x-ray image from loop-X comes with navigation info





## Write ipynb script to read h5 file

the virtual env has to be switched in advance to enable the package for reading h5, here are the steps of switching venv for jupyter notebook

1. Activate the virtual environment you want to use in your terminal. For example, if you are using Anaconda, you can activate your environment by running:

   ```
   conda activate myenv
   ```

2. Install the `ipykernel` package inside your virtual environment. This package provides the IPython kernel for Jupyter, which allows you to run code in the notebook using your virtual environment.

   ```
   pip install ipykernel
   ```

3. Next, you need to create a new kernel for your virtual environment. You can do this by running:

   ```
   python -m ipykernel install --user --name=myenv
   ```

   This will create a new kernel in Jupyter with the name `myenv`.

4. Now you can launch Jupyter Notebook by running the following command:

   ```
   jupyter notebook
   ```

   This will open the Jupyter Notebook interface in your web browser.

5. In Jupyter Notebook, you can switch to your virtual environment by selecting the kernel from the Kernel menu. To do this, go to the Kernel menu and select "Change kernel", then choose the kernel with the name of your virtual environment.



## Data Format

### SyntheX Data Format

The Hierarchical Data Format version 5 (HDF5), is **an open source file format that supports large, complex, heterogeneous data**. The HDF5 files use the suffix of h5.

Python provides [h5py](https://docs.h5py.org/en/stable/) lib to process h5 files. In Python, h5 file can be loaded as an iteratively nested dictionary. The basic structure is called dataset, dataset can be accessed by [...] method, for example:



example real.h5: Used as an input to syntheX from dicom images

``` python
├── '01'
│    └── 'projs' <HDF5 Dataset>
├── '02'
│    └── 'projs' <HDF5 Dataset>
├── '03'
│    └── 'projs' <HDF5 Dataset>
├── '04'
│    └── 'projs' <HDF5 Dataset>
├── '05'
│    └── 'projs' <HDF5 Dataset>
├── '06'
│    └── 'projs' <HDF5 Dataset>
└── 'land-names'
    ├── 'land-00' <HDF5 Dataset>
    ├── 'land-01' <HDF5 Dataset>
    ├── 'land-02' <HDF5 Dataset>
    ├── 'land-03' <HDF5 Dataset>
    ├── 'land-05' <HDF5 Dataset>
    ├── 'land-06' <HDF5 Dataset>
    ├── 'land-07' <HDF5 Dataset>
    ├── 'land-08' <HDF5 Dataset>
    ├── 'land-09' <HDF5 Dataset>
    ├── 'land-10' <HDF5 Dataset>
    ├── 'land-11' <HDF5 Dataset>
    ├── 'land-12' <HDF5 Dataset>
    ├── 'land-13' <HDF5 Dataset>
    └── 'num-lands' <HDF5 Dataset>

```






example real_label.h5: 

``` python
├── '01'
│   ├── 'gt-poses'
│   |     └──  ['000',['001'],['002']....]
│   |     |      └──  <HDF5 Dataset>
│   ├── 'lands'
│   |     └──  <HDF5 Dataset>
│   ├── 'segs'
│   |     └──  <HDF5 Dataset>
├── '02'
│    └── same as '01'
├── '03'
│   └── ...
├── '04'
│    └──  ...
├── '05'
│    └── ...
├── '06'
│    └──  ...
├── 'land-names'
│   ├── 'land-00' <HDF5 Dataset>
│   ├── 'land-01' <HDF5 Dataset>
│   ├── 'land-02' <HDF5 Dataset>
│   ├── 'land-03' <HDF5 Dataset>
│   ├── 'land-05' <HDF5 Dataset>
│   ├── 'land-06' <HDF5 Dataset>
│   ├── 'land-07' <HDF5 Dataset>
│   ├── 'land-08' <HDF5 Dataset>
│   ├── 'land-09' <HDF5 Dataset>
│   ├── 'land-10' <HDF5 Dataset>
│   ├── 'land-11' <HDF5 Dataset>
│   ├── 'land-12' <HDF5 Dataset>
│   ├── 'land-13' <HDF5 Dataset>
│   └──  'num-lands' <HDF5 Dataset>
└── 'proj-para'
    ├── 'extrinsic' <HDF5 Dataset>
    ├── 'intrinsic' <HDF5 Dataset>
    ├── 'num-cols' <HDF5 Dataset>
    ├── 'num-rows' <HDF5 Dataset>
    ├── 'pixel-col-spacing' <HDF5 Dataset>
    └── 'pixel-row-spacing' <HDF5 Dataset>

```



name of the landmarks:

```bash
['FH-l', 'FH-r', 'GSN-l', 'GSN-r', 'IOF-l', 'IOF-r', 'MOF-l', 'MOF-r', 'SPS-l', 'SPS-r', 'IPS-l', 'IPS-r', 'ASIS-l', 'ASIS-r']
```



### xReg Data Format

#### FCSV

'id' and 'associatedNodeID' are not necessary for xReg, it should be some labels that come from the landmark annotation process in 3DSlicer

```
# Markups fiducial file version = 5.0
# CoordinateSystem = LPS
# columns = id,x,y,z,ow,ox,oy,oz,vis,sel,lock,label,desc,associatedNodeID
,33.51913833618164,91.95581817626953,-614.0459594726562,0,0,0,1,1,1,1,SPS-r, , 
,32.69633865356445,113.62252807617188,-635.4973754882812,0,0,0,1,1,1,1,IPS-r, , 
,-16.04508399963379,162.6339874267578,-640.7818603515625,0,0,0,1,1,1,1,IOF-r, , 
,-23.665447235107422,173.18283081054688,-545.8438110351562,0,0,0,1,1,1,1,GSN-r, , 
,-30.927318572998047,190.9574432373047,-649.4568481445312,0,0,0,1,1,1,1,IT-r, , 
,10.974197387695312,124.45952606201172,-622.6507568359375,0,0,0,1,1,1,1,MOF-r, , 
,-59.7931022644043,81.35031127929688,-517.1331176757812,0,0,0,1,1,1,1,ASIS-r, , 
,-14.3635835647583,188.99717712402344,-591.510986328125,0,0,0,1,1,1,1,IS-r, , 
,43.9493408203125,90.42715454101562,-614.400146484375,0,0,0,1,1,1,1,SPS-l, , 
,43.29179763793945,116.68962097167969,-636.6901245117188,0,0,0,1,1,1,1,IPS-l, , 
,86.10452270507812,165.24656677246094,-641.2273559570312,0,0,0,1,1,1,1,IOF-l, , 
,102.52001953125,176.56101989746094,-548.27294921875,0,0,0,1,1,1,1,GSN-l, , 
,100.10421752929688,193.62289428710938,-652.7132568359375,0,0,0,1,1,1,1,IT-l, , 
,62.239341735839844,123.50407409667969,-623.759521484375,0,0,0,1,1,1,1,MOF-l, , 
,141.8777618408203,87.38057708740234,-525.8892822265625,0,0,0,1,1,1,1,ASIS-l, , 
,86.5421371459961,195.70928955078125,-594.8851928710938,0,0,0,1,1,1,1,IS-l, , 
```

Coordinate System tag is used to identify the

#### HDF5

example the input of xreg: example1_1_pd_003.h5

example1_1_pd_003.h5

```bash
.
├── 'num-projs'
│   └── <HDF5 Dataset>
├── 'proj-000'
│   ├── 'cam'
│   │   ├── 'cam-coord-frame-type'
│   │   │   └── <HDF5 Dataset>
│   │   ├── 'col-spacing'
│   │   │   └── <HDF5 Dataset>
│   │   ├── 'extrinsic'
│   │   │   └── <HDF5 Dataset>
│   │   ├── 'intrinsic'
│   │   │   └── <HDF5 Dataset>
│   │   ├── 'num-cols'
│   │   │   └── <HDF5 Dataset>
│   │   ├── 'num-rows'
│   │   │   └── <HDF5 Dataset>
│   │   └── 'row-spacing'
│   │       └── <HDF5 Dataset>
│   ├── 'img'
│   │   ├── 'dir-mat'
│   │   │   └── <HDF5 Dataset>
│   │   ├── 'origin'
│   │   │   └── <HDF5 Dataset>
│   │   ├── 'pixels'
│   │   │   └── <HDF5 Dataset>
│   │   └── 'spacing'
│   │       └── <HDF5 Dataset>
│   └── 'landmarks'
│       ├── 'GSN-l'
│       │   └── <HDF5 Dataset>
│       ├── ...
│       └── 'SPS-r'
│           └── <HDF5 Dataset>
├── 'proj-001'
│   └── # same as proj-000
└── 'proj-002'
    └── # same as proj-000
```

```python
Keys: <KeysViewHDF5 ['num-projs', 'proj-000', 'proj-001', 'proj-002']>
'proj-000' keys: <KeysViewHDF5 ['cam', 'img', 'landmarks']>
'cam' keys: <KeysViewHDF5 ['cam-coord-frame-type', 'col-spacing', 'extrinsic', 'intrinsic', 'num-cols', 'num-rows', 'row-spacing']>
'img' keys: <KeysViewHDF5 ['dir-mat', 'origin', 'pixels', 'spacing']>

```

