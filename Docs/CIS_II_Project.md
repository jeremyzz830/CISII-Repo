<h1 align="center">Project Logs</h1>

> Print out the slides in a 6 page format
>
> A print version of the papers is also preferred

# [Update Logs] 

<u>Feb 01, 2023</u>

### Questions Regarding the Loop-X

1. Is the connection between the navigation system and the teaching pendant fixed?
2. Is it possible to write some script on the windows environment of the Loop-X?
3. Can we directly save our file to the local driver and get access to it from the local environment?
4. Can the teaching pendant set up a public network, i.e., WAN, except for the local network?
5. Can the navigation system be customized? For example, adding some script.



### Possible Solutions

1. Script on Teaching Pendant
2. ssh to the teaching pendant
3. Script on the Navigation Platform and use a wireless stick to set up a private WAN
4. SanDisk Wireless Stick, need an App on my computer



# [Update Comments] 

<u>Feb 09, 2023</u>

Print out a paper form handout for the Slides. Add Group Number

Deliverables matter! Don't be vague. [**Documentation**/Program/Design]

<u>Specification Review, Task Plan Review, Test Plan Documentation</u>

Milestones

Dependency: Need, Status, Followup, ContingencyPlan, Include Dates

Dependency includes software access, hardware access, other people, money

Timeline before 5.11



# [Update Log] 

<u>Feb 11, 2023</u>

What exactly are we going to document? SyntheX .....



# [Weekly Meeting] 

<u>Feb 13, 2023</u>

**What's the specific workflow?** - LoopX ->  SyntheX -> Registration by Grupp 

**Solutions to the data acquisition.**

1. SanDisk Wireless Stick, need an app on my computer

2. PACS

What role does SyntheX play in this whole process? - Preparing dataset for other models?



### Tasks TODO:

Make Slides and demonstrate to Ben before the presentation before the next meeting.

Make documentation and explain the whole pipeline for SnytheX. Integrate SytheX in a docker image.(Possibly)

IRB is not a dependency.

Find landmarks with SyntheX-made X-Ray images, then solve the 2D-3D registration based on what Robert Group has developed.



# [Update Log] 

<u>Feb 14, 2023</u>

Don't use the word "study". Use analyze instead.

Clearly state the name of the mentor who would provide the dependency.



# [Update Log]

<u>Feb 16, 2023</u>

Clearly statement of the allocation of duties.

Deliverable is not an activity, is a prototype, documentation, report, code repo, manuscript

What's my input and output, what's his input and output, and when should team members meet

the dependency is provided by who.



# [Update Log]

<u>Feb 23, 2023</u>

The communications of the specification of the interfaces between the group members



# [Weekly Meeting]

<u>Feb 27, 2023</u>

exact data format that are exchanging

a outline of python scripts

```python
def import_image()
	pass
def call_syntheX()
	return image, landmark
def call_xreg()
	pass

class data_container
class LandmarkDetectionInput()
class LandmarkDetectionOutput()
class RegiInput()
class RegiOutput()
```

We can use the data to test our code separately without dependency between two functionality.

Modularize the call_synthex function to allow future substitution of SyntheX

h5 viewer/h5py can open h5 file : Document all the structure of the h5 out

pack everything in a sole package so that we can pip-install whatever we build

Sim2Real meaning training on the simulation dataset ( input <u>synthetic image</u> + <u>labeled synthetic image</u> pairs )



# [Update Log]

Mar 02, 2023

One paper per member.

Documentation for the total workflow functionalities should be done now.

Figs mush come with proper citation right below where you use it.



# [Weekly Meeting]

Nifty file uses this for now. Don't modify all the data. Segmentation, a landmark in JSON format.

Intensity-based method can gain more control over the edge of the bone.



# [Update Log]

Mar 09 2023

Explain the terms before every presentation!!!

Better don't bring scripts. Memorize it!

To be clear and concise in the citation, especially in the report.



# [Update Log]

Mar 16 2023

Talk about how many milestones have been done.

Progress: 

Real-time integration for 2d3d registration

Implementation for submodules is done, which is our minimum deliverable, now the integration part is done either, and according to our timeline, we are wirting for the tutorials and documentations for others to use our software. We also on our way of trying to pack everything into a pip package so that everyone else can easily download it and use it.



# [Update Log]

Mar 27, 2023

- integrate into a full pip package:
  - method 1: instruction for installing the xReg aside
  - method 2: integrate the binary of xReg into a pipy work flow and make wheels of building it
- colab script to demonstrate how the code works, include one image
- loop-x image frame, navigation frame, ct and x-ray image frame : RAS/LAS

# [Update Log]
Apr 17, 2023

- fix all the bugs
- - can have xreg installed aside
- have a main script so that people can run the file from terminal, with --help functionality
- have a colab notebook with xreg installed so that people can run it online
- write a readme and add some interactive warning and errors if ct segmentation is not provided, give a direct link to the total segmentator would be perfect.


# [Update Log]

Apr 24, 2023

- command line tool, create a dir for the result, if not provided, create a folder with the image names
- a json file that contains camera parameters, errors, results
- emphasis for russ, installation and usage demo for the package, comparing to the old complicated way of doing the whole process.
- update readme file and the colab stuff
