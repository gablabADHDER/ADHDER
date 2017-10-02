#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.84.2),
    on Wed Sep 27 12:37:19 2017
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'WMLoc'  # from the Builder filename that created this script
expInfo = {u'randomization': u'', u'session': u'', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/pyData_%s_%s%s_%s_%s' %(expInfo['participant'], expInfo['randomization'], expInfo['session'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/Users/schuyler/Dropbox (MIT)/GABLAB/ADHDER/Paradigms_2017-8-17/wmloc/WorkingMemory.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1280, 800), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "initalize"
initalizeClock = core.Clock()
if u'%s' %(expInfo['randomization']) == 'demo':
    parametersFile = u'parameters/blocks_demo.csv'
    runRandomization = 'debug'
    nBlocks = 2 #debug
else:
    nBlocks = 8 #debug
nTrials = 18 #debug

if u'%s' %(expInfo['randomization']) == 'a' and u'%s' %(expInfo['session']) == '1':
    parametersFile = u'parameters/blocks_runAa.csv'
    runRandomization = 'A'
if u'%s' %(expInfo['randomization']) == 'a' and u'%s' %(expInfo['session']) == '2':
    parametersFile = u'parameters/blocks_runBa.csv'
    runRandomization = 'B'

if u'%s' %(expInfo['randomization']) == 'b' and u'%s' %(expInfo['session']) == '1':
    parametersFile = u'parameters/blocks_runBb.csv'
    runRandomization = 'B'
if u'%s' %(expInfo['randomization']) == 'b' and u'%s' %(expInfo['session']) == '2':
    parametersFile = u'parameters/blocks_runAb.csv'
    runRandomization = 'A'

parametersFile_runs = [[None]*nTrials, [None]*nTrials, [None]*nTrials, [None]*nTrials, [None]*nTrials, [None]*nTrials, [None]*nTrials, [None]*nTrials]
targetShown = [[None]*nTrials, [None]*nTrials, [None]*nTrials, [None]*nTrials, [None]*nTrials, [None]*nTrials, [None]*nTrials, [None]*nTrials]
finalResp = np.zeros((nTrials,3,nBlocks))
verdicalResp = np.empty((nTrials,nBlocks))

# Initialize components for Routine "blank"
blankClock = core.Clock()

# Initialize components for Routine "ready"
readyClock = core.Clock()
image_ready = visual.ImageStim(
    win=win, name='image_ready',units='pix', 
    image='instructions/ready.png', mask=None,
    ori=0, pos=(0, 0), size=[1024,768],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "scanner_trigger"
scanner_triggerClock = core.Clock()
image_fixation_scanner = visual.ImageStim(
    win=win, name='image_fixation_scanner',units='pix', 
    image='instructions/fixation.png', mask=None,
    ori=0, pos=(0, 0), size=[1024,768],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text = visual.TextStim(win=win, name='text',
    text='(scanner warming up)',
    font='Arial',
    pos=(0, -.1), height=.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "prescan"
prescanClock = core.Clock()
fixation_prescan = visual.ImageStim(
    win=win, name='fixation_prescan',units='pix', 
    image='instructions/fixation.png', mask=None,
    ori=0, pos=(0, 0), size=[1024,768],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "trial_instr"
trial_instrClock = core.Clock()
image_fixation = visual.ImageStim(
    win=win, name='image_fixation',units='pix', 
    image='instructions/fixation.png', mask=None,
    ori=0, pos=(0, 0), size=[1024,768],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
trial_instructions_image1 = visual.ImageStim(
    win=win, name='trial_instructions_image1',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=[1024,768],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
trial_instructions_image2 = visual.ImageStim(
    win=win, name='trial_instructions_image2',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=[1024,768],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
trial_instructions_image3 = visual.ImageStim(
    win=win, name='trial_instructions_image3',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=[1024,768],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
trial_instructions_image4 = visual.ImageStim(
    win=win, name='trial_instructions_image4',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=[1024,768],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
trial_instructions_image5 = visual.ImageStim(
    win=win, name='trial_instructions_image5',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=[1024,768],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
trial_instructions_image6 = visual.ImageStim(
    win=win, name='trial_instructions_image6',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=[1024,768],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
ITI_static = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ITI_static')

# Initialize components for Routine "countdown"
countdownClock = core.Clock()
begin6 = visual.ImageStim(
    win=win, name='begin6',units='pix', 
    image='instructions/begin6.png', mask=None,
    ori=0, pos=(0, 0), size=[1024,768],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
begin5 = visual.ImageStim(
    win=win, name='begin5',units='pix', 
    image='instructions/begin5.png', mask=None,
    ori=0, pos=(0, 0), size=[1024,768],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
begin4 = visual.ImageStim(
    win=win, name='begin4',units='pix', 
    image='instructions/begin4.png', mask=None,
    ori=0, pos=(0, 0), size=[1024,768],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
begin3 = visual.ImageStim(
    win=win, name='begin3',units='pix', 
    image='instructions/begin3.png', mask=None,
    ori=0, pos=(0, 0), size=[1024,768],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
begin2 = visual.ImageStim(
    win=win, name='begin2',units='pix', 
    image='instructions/begin2.png', mask=None,
    ori=0, pos=(0, 0), size=[1024,768],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
begin1 = visual.ImageStim(
    win=win, name='begin1',units='pix', 
    image='instructions/begin1.png', mask=None,
    ori=0, pos=(0, 0), size=[1024,768],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)

# Initialize components for Routine "fixation_pre"
fixation_preClock = core.Clock()
fixation_image_pre = visual.ImageStim(
    win=win, name='fixation_image_pre',units='pix', 
    image='instructions/fixation.png', mask=None,
    ori=0, pos=(0, 0), size=[1024,768],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "presenation"
presenationClock = core.Clock()
fixation_image = visual.ImageStim(
    win=win, name='fixation_image',units='pix', 
    image='instructions/fixation.png', mask=None,
    ori=0, pos=(0, 0), size=[1024,768],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
target = visual.ImageStim(
    win=win, name='target',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=[1024,768],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)


# Initialize components for Routine "logData"
logDataClock = core.Clock()

export_fixation = visual.ImageStim(
    win=win, name='export_fixation',units='pix', 
    image='instructions/fixation.png', mask=None,
    ori=0, pos=(0, 0), size=[1024,768],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "finalFixation"
finalFixationClock = core.Clock()
final_fixation = visual.ImageStim(
    win=win, name='final_fixation',units='pix', 
    image='instructions/fixation.png', mask=None,
    ori=0, pos=(0, 0), size=[1024,768],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "end"
endClock = core.Clock()
end_image = visual.ImageStim(
    win=win, name='end_image',units='pix', 
    image='instructions/end.png', mask=None,
    ori=0, pos=(0, 0), size=[1024,768],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "initalize"-------
t = 0
initalizeClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat

# keep track of which components have finished
initalizeComponents = []
for thisComponent in initalizeComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "initalize"-------
while continueRoutine:
    # get current time
    t = initalizeClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in initalizeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "initalize"-------
for thisComponent in initalizeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "initalize" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "blank"-------
t = 0
blankClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()
# keep track of which components have finished
blankComponents = [key_resp_2]
for thisComponent in blankComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "blank"-------
while continueRoutine:
    # get current time
    t = blankClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['equal'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "blank"-------
for thisComponent in blankComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "blank" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ready"-------
t = 0
readyClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_ready = event.BuilderKeyResponse()
# keep track of which components have finished
readyComponents = [image_ready, key_resp_ready]
for thisComponent in readyComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "ready"-------
while continueRoutine:
    # get current time
    t = readyClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_ready* updates
    if t >= 0.0 and image_ready.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_ready.tStart = t
        image_ready.frameNStart = frameN  # exact frame index
        image_ready.setAutoDraw(True)
    
    # *key_resp_ready* updates
    if t >= 0.0 and key_resp_ready.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_ready.tStart = t
        key_resp_ready.frameNStart = frameN  # exact frame index
        key_resp_ready.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_ready.status == STARTED:
        theseKeys = event.getKeys(keyList=['1'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in readyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ready"-------
for thisComponent in readyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "ready" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "scanner_trigger"-------
t = 0
scanner_triggerClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_scanner_trigger = event.BuilderKeyResponse()
# keep track of which components have finished
scanner_triggerComponents = [key_resp_scanner_trigger, image_fixation_scanner, text]
for thisComponent in scanner_triggerComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "scanner_trigger"-------
while continueRoutine:
    # get current time
    t = scanner_triggerClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_scanner_trigger* updates
    if t >= 0.0 and key_resp_scanner_trigger.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_scanner_trigger.tStart = t
        key_resp_scanner_trigger.frameNStart = frameN  # exact frame index
        key_resp_scanner_trigger.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_scanner_trigger.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_scanner_trigger.status == STARTED:
        theseKeys = event.getKeys(keyList=['num_add', '+', 'equal'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_scanner_trigger.keys.extend(theseKeys)  # storing all keys
            key_resp_scanner_trigger.rt.append(key_resp_scanner_trigger.clock.getTime())
            # a response ends the routine
            continueRoutine = False
    
    # *image_fixation_scanner* updates
    if t >= 0.0 and image_fixation_scanner.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_fixation_scanner.tStart = t
        image_fixation_scanner.frameNStart = frameN  # exact frame index
        image_fixation_scanner.setAutoDraw(True)
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in scanner_triggerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "scanner_trigger"-------
for thisComponent in scanner_triggerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_scanner_trigger.keys in ['', [], None]:  # No response was made
    key_resp_scanner_trigger.keys=None
thisExp.addData('key_resp_scanner_trigger.keys',key_resp_scanner_trigger.keys)
if key_resp_scanner_trigger.keys != None:  # we had a response
    thisExp.addData('key_resp_scanner_trigger.rt', key_resp_scanner_trigger.rt)
thisExp.nextEntry()
# the Routine "scanner_trigger" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "prescan"-------
t = 0
prescanClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(4.000000)
# update component parameters for each repeat
# keep track of which components have finished
prescanComponents = [fixation_prescan]
for thisComponent in prescanComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "prescan"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = prescanClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fixation_prescan* updates
    if t >= 0.0 and fixation_prescan.status == NOT_STARTED:
        # keep track of start time/frame for later
        fixation_prescan.tStart = t
        fixation_prescan.frameNStart = frameN  # exact frame index
        fixation_prescan.setAutoDraw(True)
    frameRemains = 0.0 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if fixation_prescan.status == STARTED and t >= frameRemains:
        fixation_prescan.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in prescanComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "prescan"-------
for thisComponent in prescanComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
blocks = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(parametersFile),
    seed=None, name='blocks')
thisExp.addLoop(blocks)  # add the loop to the experiment
thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock.keys():
        exec(paramName + '= thisBlock.' + paramName)

for thisBlock in blocks:
    currentLoop = blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock.keys():
            exec(paramName + '= thisBlock.' + paramName)
    
    # ------Prepare to start Routine "trial_instr"-------
    t = 0
    trial_instrClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    trial_instrComponents = [image_fixation, trial_instructions_image1, trial_instructions_image2, trial_instructions_image3, trial_instructions_image4, trial_instructions_image5, trial_instructions_image6, ITI_static]
    for thisComponent in trial_instrComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial_instr"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial_instrClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_fixation* updates
        if t >= 0.0 and image_fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_fixation.tStart = t
            image_fixation.frameNStart = frameN  # exact frame index
            image_fixation.setAutoDraw(True)
        frameRemains = 0.0 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_fixation.status == STARTED and t >= frameRemains:
            image_fixation.setAutoDraw(False)
        
        # *trial_instructions_image1* updates
        if t >= 4 and trial_instructions_image1.status == NOT_STARTED:
            # keep track of start time/frame for later
            trial_instructions_image1.tStart = t
            trial_instructions_image1.frameNStart = frameN  # exact frame index
            trial_instructions_image1.setAutoDraw(True)
        frameRemains = 4 + .55- win.monitorFramePeriod * 0.75  # most of one frame period left
        if trial_instructions_image1.status == STARTED and t >= frameRemains:
            trial_instructions_image1.setAutoDraw(False)
        
        # *trial_instructions_image2* updates
        if t >= 4.5 and trial_instructions_image2.status == NOT_STARTED:
            # keep track of start time/frame for later
            trial_instructions_image2.tStart = t
            trial_instructions_image2.frameNStart = frameN  # exact frame index
            trial_instructions_image2.setAutoDraw(True)
        frameRemains = 4.5 + .55- win.monitorFramePeriod * 0.75  # most of one frame period left
        if trial_instructions_image2.status == STARTED and t >= frameRemains:
            trial_instructions_image2.setAutoDraw(False)
        
        # *trial_instructions_image3* updates
        if t >= 5 and trial_instructions_image3.status == NOT_STARTED:
            # keep track of start time/frame for later
            trial_instructions_image3.tStart = t
            trial_instructions_image3.frameNStart = frameN  # exact frame index
            trial_instructions_image3.setAutoDraw(True)
        frameRemains = 5 + .55- win.monitorFramePeriod * 0.75  # most of one frame period left
        if trial_instructions_image3.status == STARTED and t >= frameRemains:
            trial_instructions_image3.setAutoDraw(False)
        
        # *trial_instructions_image4* updates
        if t >= 5.5 and trial_instructions_image4.status == NOT_STARTED:
            # keep track of start time/frame for later
            trial_instructions_image4.tStart = t
            trial_instructions_image4.frameNStart = frameN  # exact frame index
            trial_instructions_image4.setAutoDraw(True)
        frameRemains = 5.5 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if trial_instructions_image4.status == STARTED and t >= frameRemains:
            trial_instructions_image4.setAutoDraw(False)
        
        # *trial_instructions_image5* updates
        if t >= 6 and trial_instructions_image5.status == NOT_STARTED:
            # keep track of start time/frame for later
            trial_instructions_image5.tStart = t
            trial_instructions_image5.frameNStart = frameN  # exact frame index
            trial_instructions_image5.setAutoDraw(True)
        frameRemains = 6 + .3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if trial_instructions_image5.status == STARTED and t >= frameRemains:
            trial_instructions_image5.setAutoDraw(False)
        
        # *trial_instructions_image6* updates
        if t >= 6.6 and trial_instructions_image6.status == NOT_STARTED:
            # keep track of start time/frame for later
            trial_instructions_image6.tStart = t
            trial_instructions_image6.frameNStart = frameN  # exact frame index
            trial_instructions_image6.setAutoDraw(True)
        frameRemains = 6.6 + 3.4- win.monitorFramePeriod * 0.75  # most of one frame period left
        if trial_instructions_image6.status == STARTED and t >= frameRemains:
            trial_instructions_image6.setAutoDraw(False)
        # *ITI_static* period
        if t >= 0.0 and ITI_static.status == NOT_STARTED:
            # keep track of start time/frame for later
            ITI_static.tStart = t
            ITI_static.frameNStart = frameN  # exact frame index
            ITI_static.start(4)
        elif ITI_static.status == STARTED:  # one frame should pass before updating params and completing
            # updating other components during *ITI_static*
            trial_instructions_image1.setImage(instructions_image1)
            trial_instructions_image2.setImage(instructions_image2)
            trial_instructions_image3.setImage(instructions_image3)
            trial_instructions_image4.setImage(instructions_image4)
            trial_instructions_image5.setImage(instructions_image5)
            trial_instructions_image6.setImage(instructions_image5)
            # component updates done
            ITI_static.complete()  # finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_instrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_instr"-------
    for thisComponent in trial_instrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "countdown"-------
    t = 0
    countdownClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    countdownComponents = [begin6, begin5, begin4, begin3, begin2, begin1]
    for thisComponent in countdownComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "countdown"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = countdownClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *begin6* updates
        if t >= 0.0 and begin6.status == NOT_STARTED:
            # keep track of start time/frame for later
            begin6.tStart = t
            begin6.frameNStart = frameN  # exact frame index
            begin6.setAutoDraw(True)
        frameRemains = 0.0 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
        if begin6.status == STARTED and t >= frameRemains:
            begin6.setAutoDraw(False)
        
        # *begin5* updates
        if t >= 1 and begin5.status == NOT_STARTED:
            # keep track of start time/frame for later
            begin5.tStart = t
            begin5.frameNStart = frameN  # exact frame index
            begin5.setAutoDraw(True)
        frameRemains = 6 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if begin5.status == STARTED and t >= frameRemains:
            begin5.setAutoDraw(False)
        
        # *begin4* updates
        if t >= 2 and begin4.status == NOT_STARTED:
            # keep track of start time/frame for later
            begin4.tStart = t
            begin4.frameNStart = frameN  # exact frame index
            begin4.setAutoDraw(True)
        frameRemains = 6 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if begin4.status == STARTED and t >= frameRemains:
            begin4.setAutoDraw(False)
        
        # *begin3* updates
        if t >= 3 and begin3.status == NOT_STARTED:
            # keep track of start time/frame for later
            begin3.tStart = t
            begin3.frameNStart = frameN  # exact frame index
            begin3.setAutoDraw(True)
        frameRemains = 6 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if begin3.status == STARTED and t >= frameRemains:
            begin3.setAutoDraw(False)
        
        # *begin2* updates
        if t >= 4 and begin2.status == NOT_STARTED:
            # keep track of start time/frame for later
            begin2.tStart = t
            begin2.frameNStart = frameN  # exact frame index
            begin2.setAutoDraw(True)
        frameRemains = 6 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if begin2.status == STARTED and t >= frameRemains:
            begin2.setAutoDraw(False)
        
        # *begin1* updates
        if t >= 5 and begin1.status == NOT_STARTED:
            # keep track of start time/frame for later
            begin1.tStart = t
            begin1.frameNStart = frameN  # exact frame index
            begin1.setAutoDraw(True)
        frameRemains = 6 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if begin1.status == STARTED and t >= frameRemains:
            begin1.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in countdownComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "countdown"-------
    for thisComponent in countdownComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "fixation_pre"-------
    t = 0
    fixation_preClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixation_preComponents = [fixation_image_pre]
    for thisComponent in fixation_preComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "fixation_pre"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixation_preClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_image_pre* updates
        if t >= 0.0 and fixation_image_pre.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_image_pre.tStart = t
            fixation_image_pre.frameNStart = frameN  # exact frame index
            fixation_image_pre.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_image_pre.status == STARTED and t >= frameRemains:
            fixation_image_pre.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixation_preComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation_pre"-------
    for thisComponent in fixation_preComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(stim_lists),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial.keys():
                exec(paramName + '= thisTrial.' + paramName)
        
        # ------Prepare to start Routine "presenation"-------
        t = 0
        presenationClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        target.setImage(target_image)
        rating = event.BuilderKeyResponse()
        finalResp[trials.thisIndex, 2, blocks.thisIndex] = prescanClock.getTime()
        # keep track of which components have finished
        presenationComponents = [fixation_image, target, rating]
        for thisComponent in presenationComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "presenation"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = presenationClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_image* updates
            if t >= 0.0 and fixation_image.status == NOT_STARTED:
                # keep track of start time/frame for later
                fixation_image.tStart = t
                fixation_image.frameNStart = frameN  # exact frame index
                fixation_image.setAutoDraw(True)
            frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
            if fixation_image.status == STARTED and t >= frameRemains:
                fixation_image.setAutoDraw(False)
            
            # *target* updates
            if t >= 0.0 and target.status == NOT_STARTED:
                # keep track of start time/frame for later
                target.tStart = t
                target.frameNStart = frameN  # exact frame index
                target.setAutoDraw(True)
            frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if target.status == STARTED and t >= frameRemains:
                target.setAutoDraw(False)
            
            # *rating* updates
            if t >= 0.0 and rating.status == NOT_STARTED:
                # keep track of start time/frame for later
                rating.tStart = t
                rating.frameNStart = frameN  # exact frame index
                rating.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(rating.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
            if rating.status == STARTED and t >= frameRemains:
                rating.status = STOPPED
            if rating.status == STARTED:
                theseKeys = event.getKeys(keyList=['1'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    rating.keys.extend(theseKeys)  # storing all keys
                    rating.rt.append(rating.clock.getTime())
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in presenationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "presenation"-------
        for thisComponent in presenationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if rating.keys in ['', [], None]:  # No response was made
            rating.keys=None
        trials.addData('rating.keys',rating.keys)
        if rating.keys != None:  # we had a response
            trials.addData('rating.rt', rating.rt)
        targetShown[blocks.thisIndex][trials.thisIndex] = target_image[8]
        verdicalResp[trials.thisIndex, blocks.thisIndex] = verdical_response
        parametersFile_runs[blocks.thisIndex][trials.thisIndex] = stim_lists
        if rating.keys is not None:
            finalResp[trials.thisIndex, 0, blocks.thisIndex] = int(rating.keys[0])
            finalResp[trials.thisIndex, 1, blocks.thisIndex] = rating.rt[0]
        
        #if verdicalResp[trials.thisIndex, blocks.thisIndex] == finalResp[trials.thisIndex, 0, blocks.thisIndex]:
        #    score = 'Correct'
        #else:
        #    score = 'Incorrect'
        #print(blocks.thisIndex, trials.thisIndex, finalResp[trials.thisIndex, 0, blocks.thisIndex], finalResp[trials.thisIndex, 1, blocks.thisIndex], finalResp[trials.thisIndex, 2, blocks.thisIndex], score)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials'
    
# completed 1 repeats of 'blocks'


# ------Prepare to start Routine "logData"-------
t = 0
logDataClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat

# keep track of which components have finished
logDataComponents = [export_fixation]
for thisComponent in logDataComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "logData"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = logDataClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *export_fixation* updates
    if t >= 0.0 and export_fixation.status == NOT_STARTED:
        # keep track of start time/frame for later
        export_fixation.tStart = t
        export_fixation.frameNStart = frameN  # exact frame index
        export_fixation.setAutoDraw(True)
    frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if export_fixation.status == STARTED and t >= frameRemains:
        export_fixation.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in logDataComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "logData"-------
for thisComponent in logDataComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


# ------Prepare to start Routine "finalFixation"-------
t = 0
finalFixationClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(6.000000)
# update component parameters for each repeat
# keep track of which components have finished
finalFixationComponents = [final_fixation]
for thisComponent in finalFixationComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "finalFixation"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = finalFixationClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *final_fixation* updates
    if t >= 0.0 and final_fixation.status == NOT_STARTED:
        # keep track of start time/frame for later
        final_fixation.tStart = t
        final_fixation.frameNStart = frameN  # exact frame index
        final_fixation.setAutoDraw(True)
    frameRemains = 0.0 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if final_fixation.status == STARTED and t >= frameRemains:
        final_fixation.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in finalFixationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "finalFixation"-------
for thisComponent in finalFixationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [end_image]
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_image* updates
    if t >= 0.0 and end_image.status == NOT_STARTED:
        # keep track of start time/frame for later
        end_image.tStart = t
        end_image.frameNStart = frameN  # exact frame index
        end_image.setAutoDraw(True)
    frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if end_image.status == STARTED and t >= frameRemains:
        end_image.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


dim = finalResp.shape
datafile = u'data/Data_%s_%s%s_RandCon%s_%s_%s.txt' %(expInfo['participant'], expInfo['randomization'], expInfo['session'], runRandomization, expName, expInfo['date'])
f = open(datafile,'w')
f.write(
    'block' + '\t' + 
    'trial' + '\t' + 
    'stimulus' + '\t' + 
    'verdicalResp' + '\t' + 
    'firstResp' + '\t' + 
    'firstResp_RT' + '\t' + 
    'trial_startTime' + '\t' + 
    'subject' + '\t' + 
    'randomization' + '\t' + 
    'randomizationInput' + '\t' + 
    'parametersFile_trials' + '\t' + 
    'parametersFile_blocks' + '\n')
for n in range(0,dim[2]): #blocks
    for m in range(0,dim[0]): #trials
        f.write(
            str(n+1) + '\t' + 
            str(m+1) + '\t' + 
            str(targetShown[n][m]) + '\t' + 
            str(verdicalResp[m,n]) + '\t' + 
            str(finalResp[m,0,n]) + '\t' + 
            str(finalResp[m,1,n]) + '\t' + 
            str(finalResp[m,2,n]) + '\t' + 
            expInfo['participant'] + '\t' + 
            parametersFile_runs[n][m][23:-4] + '\t' + 
            expInfo['randomization'] + '\t' + 
            parametersFile_runs[n][m] + '\t' + 
            parametersFile + '\n')
f.close()
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
