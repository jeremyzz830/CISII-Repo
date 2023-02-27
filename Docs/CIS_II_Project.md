<h1 align="center"> CIS II Project</h1>

- 2.24 A 5-8 page proposal

# [Update Logs] 

<u>Feb 01, 2023</u>

### Questions Regarding the LoopX

1. Is the connection between the navigation system and the teaching pendant fixed?
2. Is it possible to write some script on the windows environment of the Loop-X?
3. Can we directly save our file to the local driver and get access to it from the local environment?
4. Can the teaching pendant set up a public network, i.e. WAN, except for the local network?
5. Can the navigation system be customized? For example, adding some script.



### Possible Solutions

1. Script on Teaching Pendant
2. ssh to the teaching pendant
3. Script on the Navigation Platform and use a wireless stick to set up a private WAN
4. SanDisk Wireless Stick, need an app on my computer



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


class LandmarkDetectionInput()
class LandmarkDetectionOutput()
class RegiInput()
class RegiOutput()
```

no dependency between two functionality, we can use the data to test our code separately.

Modularize the call_synthex function to allow future substitution of syntheX

h5 viewer/h5py can open h5 file : Document all the structure of the h5 out

pack everything in a sole package so that we can pip install whatever we build

Sim2Real meaning training: 