#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 10:38:12 2017

@author: schuyler
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.2),
    on Wed Sep 20 11:47:06 2017
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
expName = 'emoloc'  # from the Builder filename that created this script
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
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[640, 400], fullscr=False, screen=0,
    allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "initalization"
initalizationClock = core.Clock()
if u'%s' %(expInfo['randomization']) == 'demo':
    parametersFile = u'parameters/blocks_demo.csv'
    runRandomization = 'debug'

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

nBlocks = 12
nTrials = 6
stimShown = [[None]*nTrials, [None]*nTrials, [None]*nTrials, [None]*nTrials, [None]*nTrials, [None]*nTrials, [None]*nTrials, [None]*nTrials, [None]*nTrials, [None]*nTrials, [None]*nTrials, [None]*nTrials]
parametersFile_runs = [[None]*nTrials, [None]*nTrials, [None]*nTrials, [None]*nTrials, [None]*nTrials, [None]*nTrials, [None]*nTrials, [None]*nTrials, [None]*nTrials, [None]*nTrials, [None]*nTrials, [None]*nTrials]
selectedResp = np.zeros((nTrials,3,nBlocks)) #0= key response, 1= RT 2= Time since start of scan to start of trials
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
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "scanner_cue"
scanner_cueClock = core.Clock()
image_fixation = visual.ImageStim(
    win=win, name='image_fixation',units='pix', 
    image='instructions/fixation.png', mask=None,
    ori=0, pos=(0, 0), size=[1024,768],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_scannertrigger = visual.TextStim(win=win, name='text_scannertrigger',
    text='(scanner warming up)',
    font='Arial',
    pos=(0, -.1), height=0.06, wrapWidth=None, ori=0, 
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

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instructions_image = visual.ImageStim(
    win=win, name='instructions_image',units='pix', 
    image='instructions/attend.png', mask=None,
    ori=0, pos=(0, 0), size=[1024,768],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "presentation"
presentationClock = core.Clock()
fixation_image = visual.ImageStim(
    win=win, name='fixation_image',units='pix', 
    image='instructions/fixation.png', mask=None,
    ori=0, pos=(0, 0), size=[1024,768],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
targetImage = visual.ImageStim(
    win=win, name='targetImage',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=[1024,1024],
    color=[1,1,1], colorSpace='rgb', opacity=.9,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)


# Initialize components for Routine "ITI"
ITIClock = core.Clock()
fixation3_image = visual.ImageStim(
    win=win, name='fixation3_image',units='pix', 
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

# ------Prepare to start Routine "initalization"-------
t = 0
initalizationClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat

# keep track of which components have finished
initalizationComponents = []
for thisComponent in initalizationComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "initalization"-------
while continueRoutine:
    # get current time
    t = initalizationClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in initalizationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "initalization"-------
for thisComponent in initalizationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "initalization" was not non-slip safe, so reset the non-slip timer
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
readyComponents = [key_resp_ready, image_ready]
for thisComponent in readyComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "ready"-------
while continueRoutine:
    # get current time
    t = readyClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
    
    # *image_ready* updates
    if t >= 0.0 and image_ready.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_ready.tStart = t
        image_ready.frameNStart = frameN  # exact frame index
        image_ready.setAutoDraw(True)
    
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

# ------Prepare to start Routine "scanner_cue"-------
t = 0
scanner_cueClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_scannercue = event.BuilderKeyResponse()
# keep track of which components have finished
scanner_cueComponents = [key_resp_scannercue, image_fixation, text_scannertrigger]
for thisComponent in scanner_cueComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "scanner_cue"-------
while continueRoutine:
    # get current time
    t = scanner_cueClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_scannercue* updates
    if t >= 0.0 and key_resp_scannercue.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_scannercue.tStart = t
        key_resp_scannercue.frameNStart = frameN  # exact frame index
        key_resp_scannercue.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_scannercue.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_scannercue.status == STARTED:
        theseKeys = event.getKeys(keyList=['num_add', '+', 'equal'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_scannercue.keys.extend(theseKeys)  # storing all keys
            key_resp_scannercue.rt.append(key_resp_scannercue.clock.getTime())
            # a response ends the routine
            continueRoutine = False
    
    # *image_fixation* updates
    if t >= 0.0 and image_fixation.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_fixation.tStart = t
        image_fixation.frameNStart = frameN  # exact frame index
        image_fixation.setAutoDraw(True)
    
    # *text_scannertrigger* updates
    if t >= 0.0 and text_scannertrigger.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_scannertrigger.tStart = t
        text_scannertrigger.frameNStart = frameN  # exact frame index
        text_scannertrigger.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in scanner_cueComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "scanner_cue"-------
for thisComponent in scanner_cueComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_scannercue.keys in ['', [], None]:  # No response was made
    key_resp_scannercue.keys=None
thisExp.addData('key_resp_scannercue.keys',key_resp_scannercue.keys)
if key_resp_scannercue.keys != None:  # we had a response
    thisExp.addData('key_resp_scannercue.rt', key_resp_scannercue.rt)
thisExp.nextEntry()
# the Routine "scanner_cue" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "prescan"-------
t = 0
prescanClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(8.000000)
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
    frameRemains = 0.0 + 8- win.monitorFramePeriod * 0.75  # most of one frame period left
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
    
    # ------Prepare to start Routine "instructions"-------
    t = 0
    instructionsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    instructionsComponents = [instructions_image]
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "instructions"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = instructionsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructions_image* updates
        if t >= 0.0 and instructions_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructions_image.tStart = t
            instructions_image.frameNStart = frameN  # exact frame index
            instructions_image.setAutoDraw(True)
        frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if instructions_image.status == STARTED and t >= frameRemains:
            instructions_image.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instructions"-------
    for thisComponent in instructionsComponents:
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
        
        # ------Prepare to start Routine "presentation"-------
        t = 0
        presentationClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        key_resp_1back = event.BuilderKeyResponse()
        targetImage.setImage(target_image)
        selectedResp[trials.thisIndex, 2, blocks.thisIndex] = prescanClock.getTime()
        # keep track of which components have finished
        presentationComponents = [key_resp_1back, fixation_image, targetImage]
        for thisComponent in presentationComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "presentation"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = presentationClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *key_resp_1back* updates
            if t >= 0.0 and key_resp_1back.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_1back.tStart = t
                key_resp_1back.frameNStart = frameN  # exact frame index
                key_resp_1back.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(key_resp_1back.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = 0.0 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
            if key_resp_1back.status == STARTED and t >= frameRemains:
                key_resp_1back.status = STOPPED
            if key_resp_1back.status == STARTED:
                theseKeys = event.getKeys(keyList=['1'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    key_resp_1back.keys.extend(theseKeys)  # storing all keys
                    key_resp_1back.rt.append(key_resp_1back.clock.getTime())
            
            # *fixation_image* updates
            if t >= 3 and fixation_image.status == NOT_STARTED:
                # keep track of start time/frame for later
                fixation_image.tStart = t
                fixation_image.frameNStart = frameN  # exact frame index
                fixation_image.setAutoDraw(True)
            frameRemains = 3 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
            if fixation_image.status == STARTED and t >= frameRemains:
                fixation_image.setAutoDraw(False)
            
            # *targetImage* updates
            if t >= 0 and targetImage.status == NOT_STARTED:
                # keep track of start time/frame for later
                targetImage.tStart = t
                targetImage.frameNStart = frameN  # exact frame index
                targetImage.setAutoDraw(True)
            frameRemains = 0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
            if targetImage.status == STARTED and t >= frameRemains:
                targetImage.setAutoDraw(False)
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in presentationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "presentation"-------
        for thisComponent in presentationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_1back.keys in ['', [], None]:  # No response was made
            key_resp_1back.keys=None
        trials.addData('key_resp_1back.keys',key_resp_1back.keys)
        if key_resp_1back.keys != None:  # we had a response
            trials.addData('key_resp_1back.rt', key_resp_1back.rt)
        if key_resp_1back.keys is not None:
            selectedResp[trials.thisIndex, 0, blocks.thisIndex] = int(key_resp_1back.keys[0])
            selectedResp[trials.thisIndex, 1, blocks.thisIndex] = key_resp_1back.rt[0]
        stimShown[blocks.thisIndex][trials.thisIndex] = target_image[8:-4]
        parametersFile_runs[blocks.thisIndex][trials.thisIndex] = stim_lists
        verdicalResp[trials.thisIndex,blocks.thisIndex] = verdical_response
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials'
    
    
    # ------Prepare to start Routine "ITI"-------
    t = 0
    ITIClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(12.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ITIComponents = [fixation3_image]
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ITI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ITIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation3_image* updates
        if t >= 0.0 and fixation3_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation3_image.tStart = t
            fixation3_image.frameNStart = frameN  # exact frame index
            fixation3_image.setAutoDraw(True)
        frameRemains = 0.0 + 12- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation3_image.status == STARTED and t >= frameRemains:
            fixation3_image.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ITI"-------
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
# completed 1 repeats of 'blocks'


# ------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
experimentEnd = prescanClock.getTime()
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
dim = selectedResp.shape
# datafile = u'data/Data_%s_%s%s_RandCon%s_%s_%s.txt' %(expInfo['participant'], expInfo['randomization'], expInfo['session'], runRandomization, expName, expInfo['date'])
datafile = u'data/sub-%s_task-%s_run-00%s_parm-%s%s_date-%s_events.tsv' %(expInfo['participant'], expName, expInfo['session'], expInfo['randomization'], expInfo['session'], expInfo['date'])
f = open(datafile,'w')
f.write(
    'onset' + '\t' + # trial_startTime
    'duration' + '\t' + # trial_startTime
    'block' + '\t' + 
    'trial' + '\t' + 
    'stimulus' + '\t' + 
    'verdicalResp' + '\t' + 
    'firstResp' + '\t' + 
    'firstResp_RT' + '\t' + 
    'subject' + '\t' + 
    'randomization' + '\t' + 
    'randomizationInput' + '\t' + 
    'parametersFile_trials' + '\t' + 
    'parametersFile_blocks' + '\n')
for n in range(0,dim[2]): # blocks
    for m in range(0,dim[0]): # trials
        f.write(
            str(selectedResp[m,2,n]) + '\t' + 
            str(3.000) + '\t' + # Hardcoded report of presentation time, be careful
            str(n+1) + '\t' + 
            str(m+1) + '\t' + 
            str(stimShown[n][m]) + '\t' + 
            str(verdicalResp[m,n]) + '\t' + 
            str(selectedResp[m,0,n]) + '\t' + 
            str(selectedResp[m,1,n]) + '\t' + 
            expInfo['participant'] + '\t' + 
            parametersFile_runs[n][m][23:-4] + '\t' + 
            expInfo['randomization'] + '\t' + 
            parametersFile_runs[n][m] + '\t' + 
            parametersFile + '\n')
f.write(str(experimentEnd) + '\t' + str(2) + '\n')
f.close()


blocktype = ['neutral','negative']*int(nBlocks/2)
datafile = u'data/sub-%s_task-%s_run-00%s_param-%s%s_param-GLM_date-%s_events.tsv' %(expInfo['participant'], expName, expInfo['session'], expInfo['randomization'], expInfo['session'], expInfo['date'])
f = open(datafile,'w')
f.write(
    'onset' + '\t' + # trial_startTime
    'duration' + '\t' + # trial_startTime
    'trial_type' + '\n')
for n in range(0,dim[2]): # blocks
        f.write(
            str(selectedResp[0, 2, n] - 2) + '\t' + 
            str(2.000) + '\t' + 
            'instructions' + '\n' + 
            str(selectedResp[0,2,n]) + '\t' + 
            str(dim[0]*(3.000+1.000)) + '\t' + # Hardcoded report of presentation time, be careful
            str(blocktype[n]) + '\n'
            )
f.write(str(experimentEnd) + '\t' + str(2) + '\t' + 'instructions' + '\n')
f.close()

datafile = u'data/subCOMBINED-%s_task-%s_run-00%s_parm-%s%s_date-%s_events.tsv' %(expInfo['participant'], expName, expInfo['session'], expInfo['randomization'], expInfo['session'], expInfo['date'])
f = open(datafile,'w')
f.write(
    'onset' + '\t' + # trial_startTime
    'duration' + '\t' + # trial_startTime
    'trial_type' + '\t' + 
    'block' + '\t' + 
    'trial' + '\t' + 
    'stimulus' + '\t' + 
    'verdicalResp' + '\t' + 
    'firstResp' + '\t' + 
    'firstResp_RT' + '\t' + 
    'subject' + '\t' + 
    'randomization' + '\t' + 
    'randomizationInput' + '\t' + 
    'parametersFile_trials' + '\t' + 
    'parametersFile_blocks' + '\n')
for n in range(0,dim[2]): # blocks
    for m in range(0,dim[0]): # trials
#        if n%2:
#            trialType = blocktype[1]
#        else:
#            trialType = blocktype[0]
        f.write(
            str(selectedResp[m,2,n]) + '\t' + 
            str(3.000) + '\t' + # Hardcoded report of presentation time, be careful
            str(blocktype[n] + '_stim') + '\t' + 
            str(n+1) + '\t' + 
            str(m+1) + '\t' + 
            str(stimShown[n][m]) + '\t' + 
            str(verdicalResp[m,n]) + '\t' + 
            str(selectedResp[m,0,n]) + '\t' + 
            str(selectedResp[m,1,n]) + '\t' + 
            expInfo['participant'] + '\t' + 
            parametersFile_runs[n][m][23:-4] + '\t' + 
            expInfo['randomization'] + '\t' + 
            parametersFile_runs[n][m] + '\t' + 
            parametersFile + '\n')
for n in range(0,dim[2]): # blocks
        f.write(
            str(selectedResp[0, 2, n] - 2) + '\t' + 
            str(2.000) + '\t' + 
            'instructions' + '\t' + 
            str(n+1) + '\t' + 
            'n/a' + '\t' + 
            'n/a' + '\t' + 
            'n/a' + '\t' + 
            'n/a' + '\t' + 
            'n/a' + '\t' + 
            expInfo['participant'] + '\t' + 
            parametersFile_runs[n][0][23:-4] + '\t' + 
            expInfo['randomization'] + '\t' + 
            parametersFile_runs[n][0] + '\t' + 
            parametersFile + '\n' + 
            str(selectedResp[0,2,n]) + '\t' + 
            str(dim[0]*(3.000+1.000)) + '\t' + # Hardcoded report of presentation time, be careful
            str(blocktype[n] + '_block') + '\t' +
            str(n+1) + '\t' + 
            'n/a' + '\t' + 
            'n/a' + '\t' + 
            'n/a' + '\t' + 
            'n/a' + '\t' + 
            'n/a' + '\t' + 
            expInfo['participant'] + '\t' + 
            parametersFile_runs[n][0][23:-4] + '\t' + 
            expInfo['randomization'] + '\t' + 
            parametersFile_runs[n][0] + '\t' + 
            parametersFile + '\n'
            )
f.write(str(experimentEnd) + '\t' + str(2) + '\t' + 'instructions' + '\n')
f.close()



# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
