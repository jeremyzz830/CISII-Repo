<h1 align="center">Collaboration Documentation</h1>

<br></br>

[TOC]

> This documentation is created and maintained by:
>
> **Jiaming Zhang**,  Second Year Master's Student in Robotics
>
> **Zhangcong She**, Second Year Master's Student in Mechanical Engineering

This document states the duty distribution and interfaces between the work of Jiaming Zhang and Zhangcong She.

## Overview

Here is the overview of how our software is constructed.

![img](https://lh6.googleusercontent.com/NK8Cl69ZFYdTWo33SgYSsxmO14xq9yiiiYJ2AFIWYy2C-v2qq1H0ce_-uILbo5HGKFPx82LVoXkDUWyS9_QrsjFwDMYFxMvFEmvulyB_bwBORczSz38-6D62oJ2xTMnOZh8z40prd4K3sx9aZJCbtoJ2SQ=s2048)

To be specific, Jiaming Zhang is in charge of developing the Landmark Detector, and Zhangcong She is responsible for the development of Registration Solver. Both of the team members have contributed to the Registration 2D3D class.

## Jiaming Zhang

### Duty

- Mainly responsible for managing SyntheX section, basically includes:
  - Implement interfaces for each package for future development.
  - Make a user-friendly documentation for SyntheX
  - Desgin an abtract class for 2D landmark detection for future development




### Input

- X-ray image: in h5 format
- pytorch model checkpoint: in nn format



### Output

- 2D pixel coordinates of corresponding landmarks



## Zhangcong She

### Duty

-  Mainly Responsible for managing Intensity-based registration section:

- - Configure a proper environment for Compiling the existing functionalities of xReg.
  - Desgin an abtract class for registration solver for future development



### Input

- X-ray image: in h5 format
- Pixel coordinates for 2D landmarks
- CT Scan
- Preoperatively annotated 3D landmarks



### Output

- Video demonstrating the optimization process
- Projection matrix



## Joint Contribution

- Both of us are also responsible for pipeline design, mixed reality visualization part, including:

- - Design a pipeline to automatically swap data between Loop-X, SyntheX and 2D/3D Registration.
  - Implement a program to manage these packages and integrate them into a single executable application with a Graphics User Interface.
  - Develop an executable application on Hololens for projective visualization
