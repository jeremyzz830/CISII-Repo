<h1 align="center">SyntheX Tutorial</h1>
<br></br>

[TOC]

This file is used for introducing all the componnets of SyntheX in detail and how to use them.

# File Naming Rules

| Abbreviation       | Full Name                                                    |
| ------------------ | ------------------------------------------------------------ |
| spec               | specimen                                                     |
| Sim2Real           | Train on simulation dataset and apply on real data           |
| nmd_20 CT_1k_ds_4x | nmd is for New Mexico Decedent, 1k means it contains 1000 CT scans, ds_4x means dataset of 4x resolution |
| Sim2Sim            | ?                                                            |
| -str and -rg       |                                                              |
| ds-3x              | resolution?                                                  |



# Idea Mentioned in the Paper

[Here](https://arxiv.org/pdf/2206.06127.pdf) you can find the link to the paper on arXiv

On the task of **anatomical landmark detection** and **anatomy segmentation** of <u>hip X-ray</u>, Gao tested the most commonly used domain generalization tech, i.e., adaptation and randomization.

## Data

- 366 real X-ray with accurate annotation
- 6 high-resolution CT scans of lower-torso, from 6 cadaveric specimens, with manual annotation.
- The pose of the X-ray camera is accurately known from 2D/3D registration



## Generation of synthetic X-ray image

Using the derived pose of the camera to generate digital reconstructed radiographs (DRR)

The synthetic image and the real image only differ on realism.



## DRR Methods

3 DRR methods are tested, namely naiveDRR, xreg DRR and DeepDRR. They are refered as :

**naiveDRR -> naive**

**xreg DRR -> Heurinstic**

**DeepDRR -> Realistic**



## Domain Generalization

Generalization ---- Randomization + Adaptation

### Domain Randomization

drastically change the appearance of the training data to force the network find more robust associations between input and desired target.

Two levels: regular and strong

- Regular: Done in every iteration
  - Gaussian noise injection
  - Gamma Transform
  - Random Crop: Randomly crop the image to 90% of its original size.
- Strong
  - Inverting
  - Impluse/Pepper/Salt Noise injection
  - Affine transform: rotate and translate the original image a bit
  - Contrast
  - Blurring
  - Box corruption
  - Dropout
  - ...



### Domain Adaptation

Mitigate the difference between training domain and target domain.

CycleGAN and ADDA are used.



In conclusion, randomization aims to add "noise" to the training set, while adaptation works to minimize the domain gap by sampling from the target domain at training stage.



## Validation and Evaluation

Cross-validation is a resampling procedure used to evaluate machine learning models on a limited data sample.

### K fold cross validation

The procedure has a single parameter called k that refers to the number of groups that a given data sample is to be split into. As such, the procedure is often called k-fold cross-validation. When a specific value for k is chosen, it may be used in place of k in the reference to the model, such as k=10 becoming 10-fold cross-validation.

### Naming Rules

- Sim2Real: training set is ( labeled synthetic x-ray + pure synthetic x-ray ) , evaluated on the real x-ray 
- Real2Real; trained on the real image and evaluated on the real image
- Sim2Sim: trained and evaluated are both done on synthetic image



# Technical Approach

1. import the image and store it into the given h5 format
2. using that to get a prediction out of the model with given checkpoint
3. get the landmarks pixel coordinate out of the results

Once these steps are done. Try to substitute the first step with a direct import step ( instead of using h5 ).



# Checkpoint

Cong, the first author, says the main checkpoint is in Aug14/ds_4x/nmd_str
If you want different resolultions, they are in ds_3x and ds_8x
using yy_checkpoint_net_20.pt should be good enough.



# User Tutorial

## Case 1: 

**2D Landmark Detection on Real X-ray Image**

### Model Inference Results to File

We use the following script to write network model inference results to a h5 file:

```
# This example testing is performed on the controlled real data
RealDataH5=/data/hip_imaging/controlled_study/real.h5
RealLabelH5=/data/hip_imaging/controlled_study/real_label.h5

# Patient ID
PatID=1

# Inference result output h5
InferenceH5=/data/hip_imaging/controlled_study/sim2real_example/spec_${PatID}_sim2real.h5

# Network Checkpoint Model
ModelCheckpoint=/data/hip_imaging/controlled_study/sim2real_example/yy_check_net${PatID}_50.pt

python test_ensemble.py ${RealDataH5} ${RealLabelH5} ${InferenceH5}
--pats ${PatID}
--nets ${ModelCheckpoint}
```

This example command refers to 1 fold testing. We performed 6-fold training/testing by alternating the patient ID from 1 to 6 as leave-one-out. The patient IDs are updated accordingly.

### Export Detection Results to CSV Files

#### Landmark

```
# Patient ID
PatID=1

# Inference result output h5
InferenceH5=/data/hip_imaging/controlled_study/sim2real_example/spec_${PatID}_sim2real.h5

# Output Landmark CSV File
LandmarkCSV=/data/hip_imaging/controlled_study/sim2real_example/spec_${patID}_sim2real_lands.csv

python est_lands_csv.py ${InferenceH5}
nn-heats
--use-seg nn-segs
--pat ${PatID}
--out ${LandmarkCSV}
```

#### Segmentation

```
# Patient ID
PatID=1

RealLabelH5=/data/hip_imaging/controlled_study/real_label.h5

# Inference result output h5
InferenceH5=/data/hip_imaging/controlled_study/sim2real_example/spec_${PatID}_sim2real.h5

# Output Segmentation Dice CSV File
DiceCSV=/data/hip_imaging/controlled_study/sim2real_example/spec_${patID}_sim2real_dice.csv

python compute_actual_dice_on_test.py ${RealLabelH5} ${InferenceH5}
nn-segs
${DiceCSV}
${PatID}
```



# Questions

1. Do I need to write a [Read the Docs](https://docs.readthedocs.io/en/stable/tutorial/index.html) form documentation or just a tutorial is fine
2. We don't actually need all those files now that we have the checkpoints right?
3. The script that Dr Gao used to validate his model uses the data that is not contained in the folder
4. Inference.h5 is the result. Segmentation and other results can be retrieved from it?
5. What is our goal, a csv file containing the landmarks pixel coordinates?

