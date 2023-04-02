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



- [ ] modularized classed to contain everything
- [ ] environment compatibility check
- [ ] integrate into a full pip package
- [ ] colab script to demonstrate
- [ ] performance analysis: frame rate
- [ ] x-ray image from loop-X comes with navigation info





## Write ipynb file to read h5 file

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



## Data format

### HDF5 Data format

The Hierarchical Data Format version 5 (HDF5), is **an open source file format that supports large, complex, heterogeneous data**. The HDF5 files use the suffix of h5.

Python provides [h5py](https://docs.h5py.org/en/stable/) lib to process h5 files. In Python, h5 file can be loaded as an iteratively nested dictionary. The basic structure is called dataset, dataset can be accessed by [...] method, for example:

```python
```





example real.h5: Used as an input to syntheX from dicom images

```python
keys:['01', '02', '03', '04', '05', '06', 'land-names']:
   "01"--> 'projs'--> <HDF5 dataset "projs": shape (111, 360, 360), type "<f4">
   "02"--> 'projs'--> <HDF5 dataset "projs": shape (103, 360, 360), type "<f4">
   "03"--> 'projs'--> <HDF5 dataset "projs": shape (24, 360, 360), type "<f4">
   "04"--> 'projs'--> <HDF5 dataset "projs": shape (48, 360, 360), type "<f4">
   "05"--> 'projs'--> <HDF5 dataset "projs": shape (55, 360, 360), type "<f4">
   "06"--> 'projs'--> <HDF5 dataset "projs": shape (24, 360, 360), type "<f4">
   "land-names" keys --> ['land-00', 'land-01', 'land-02', 'land-03', 'land-04', 'land-05', 'land-06', 'land-07', 'land-08', 'land-09', 'land-10', 'land-11', 'land-    12', 'land-13', 'num-lands']>:
      'num-lands'--> 14
      'land-00'--> FH-l
       ...
```
example real_label.h5: 
```python
keys:['01', '02', '03', '04', '05', '06', 'land-names', 'proj-params']
  "01" keys: ['gt-poses', 'lands', 'segs']>
      'gt-poses'--> ['000', '001', '002', '003', '004', '005', '006', '007', '008', '009', '010', '011', '012', '013', '014', '015', '016', '017', '018', '019', '020',                      '021', '022', '023', '024', '025', '026', '027', '028', '029', '030', '031', '032', '033', '034', '035', '036', '037', '038', '039', '040', '041',                      '042', '043', '044', '045', '046', '047', '048', '049', '050', '051', '052', '053', '054', '055', '056', '057', '058', '059', '060', '061', '062',                      '063', '064', '065', '066', '067', '068', '069', '070', '071', '072', '073', '074', '075', '076', '077', '078', '079', '080', '081', '082',                            '083', '084', '085', '086', '087', '088', '089', '090', '091', '092', '093', '094', '095', '096', '097', '098', '099', '100', '101', '102', '103',                      '104', '105', '106', '107', '108', '109', '110']
      "gt-poses"--> <HDF5 dataset "000": shape (4, 4), type "<f4">
      'lands' --><HDF5 dataset "lands": shape (111, 2, 14), type "<f4">
      'segs' --><HDF5 dataset "segs": shape (111, 360, 360), type "|u1">
      ...
```





name of the landmarks:

```bash
['FH-l', 'FH-r', 'GSN-l', 'GSN-r', 'IOF-l', 'IOF-r', 'MOF-l', 'MOF-r', 'SPS-l', 'SPS-r', 'IPS-l', 'IPS-r', 'ASIS-l', 'ASIS-r']
```









### xReg Data Format

#### FCSV

'id' and 'associatedNodeID' are not necessary for xReg, it should be some labels that come from the landmark annotation process in 3DSlicer

```

```

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



<ul id="myUL">  <li><span class="caret">example1_1_pd_003.h5</span>    <ul class="nested">      <li>'num-proj'</li>      <li>'proj-000'</li>      <li><span class="caret">'proj-001'</span>        <ul class="nested">          <li>Black Tea</li>          <li>White Tea</li>          <li><span class="caret">Green Tea</span>            <ul class="nested">              <li>Sencha</li>              <li>Gyokuro</li>              <li>Matcha</li>              <li>Pi Lo Chun</li>            </ul>          </li>        </ul>      </li>    </ul>  </li></ul>

```python
Keys: <KeysViewHDF5 ['num-projs', 'proj-000', 'proj-001', 'proj-002']>
'proj-000' keys: <KeysViewHDF5 ['cam', 'img', 'landmarks']>
'cam' keys: <KeysViewHDF5 ['cam-coord-frame-type', 'col-spacing', 'extrinsic', 'intrinsic', 'num-cols', 'num-rows', 'row-spacing']>
'img' keys: <KeysViewHDF5 ['dir-mat', 'origin', 'pixels', 'spacing']>

```

