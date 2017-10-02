#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.84.2),
    on Tue Jan 17 17:14:18 2017
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, gui, visual, core, data, event, logging, sound
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
expName = 'emoregulate'  # from the Builder filename that created this script
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
    size=[1024,768], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "initialize"
initializeClock = core.Clock()
parametersFile = u'parameters/param_%s%s.csv' %(expInfo['randomization'],expInfo['session'])

nTrials = 24
finalResp = [None]*nTrials #trials.nReps
finalRespRT = [None]*nTrials #trials.nReps
IAPSshown = [None]*nTrials #trials.nReps
IAPSshownTime = [None]*nTrials #trials.nReps
IAPSresponseTime = [None]*nTrials #trials.nReps
IAPSshownDuration = [None]*nTrials #trials.nReps
InstructionsShown = [None]*nTrials
IAPSstimClassDesc = [None]*nTrials
IAPSstimGroup = [None]*nTrials

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

# Initialize components for Routine "scannerTrigger"
scannerTriggerClock = core.Clock()
scannertrigger_fixation = visual.ImageStim(
    win=win, name='scannertrigger_fixation',units='pix', 
    image='instructions/fixation.png', mask=None,
    ori=0, pos=(0, 0), size=[1024,768],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_scannerTigger = visual.TextStim(win=win, name='text_scannerTigger',
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


# Initialize components for Routine "presentation"
presentationClock = core.Clock()


image_fixation_ISI = visual.ImageStim(
    win=win, name='image_fixation_ISI',units='pix', 
    image='instructions/fixation.png', mask=None,
    ori=0, pos=(0, 0), size=[1024,768],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
image_blank = visual.ImageStim(
    win=win, name='image_blank',units='pix', 
    image='instructions/blank.png', mask=None,
    ori=0, pos=(0, 0), size=[1024,768],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
instructions_pic = visual.ImageStim(
    win=win, name='instructions_pic',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1024,768],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
ISI_2 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_2')
image_IAPS = visual.ImageStim(
    win=win, name='image_IAPS',units='pix',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=[1024,1024],
    color=[1,1,1], colorSpace='rgb', opacity=.9, #IAPSOPACITY
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
debug_text2 = visual.TextStim(win=win, name='debug_text2',
    text='stimClassDesc',
    font='Arial',
    pos=(0, -2), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-7.0);
ISI_1 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_1')
# if int(expInfo['participant']) == 0:
#     debug_text2.color=u'white'
#     debug_text2.pos=(0, -.43)

# Initialize components for Routine "response"
responseClock = core.Clock()
rating_instructions = visual.ImageStim(
    win=win, name='rating_instructions',units='pix', 
    image='instructions/rating.png', mask=None,
    ori=0, pos=[0, .3], size=[1024,768],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
rating = visual.RatingScale(win=win, name='rating', markerColor='Grey', marker='triangle', markerStart=None, size=2.0, pos=[0.0, -0.4], choices=['1', '2', '3', '4', '5'], respKeys=['1','2','3','4','5'], tickHeight=-1, showAccept=False, scale=None)


# Initialize components for Routine "logData"
logDataClock = core.Clock()

fixation_final = visual.ImageStim(
    win=win, name='fixation_final',units='pix', 
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
image_end = visual.ImageStim(
    win=win, name='image_end',units='pix', 
    image='instructions/end.png', mask=None,
    ori=0, pos=(0, 0), size=[1024,768],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "initialize"-------
t = 0
initializeClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
win.mouseVisible = False
# keep track of which components have finished
initializeComponents = []
for thisComponent in initializeComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "initialize"-------
while continueRoutine:
    # get current time
    t = initializeClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in initializeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "initialize"-------
for thisComponent in initializeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "initialize" was not non-slip safe, so reset the non-slip timer
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
key_resp_begin = event.BuilderKeyResponse()
# keep track of which components have finished
readyComponents = [key_resp_begin, image_ready]
for thisComponent in readyComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "ready"-------
while continueRoutine:
    # get current time
    t = readyClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_begin* updates
    if t >= 0.0 and key_resp_begin.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_begin.tStart = t
        key_resp_begin.frameNStart = frameN  # exact frame index
        key_resp_begin.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_begin.status == STARTED:
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

# ------Prepare to start Routine "scannerTrigger"-------
t = 0
scannerTriggerClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
scanner_cue_key = event.BuilderKeyResponse()
# keep track of which components have finished
scannerTriggerComponents = [scanner_cue_key, scannertrigger_fixation, text_scannerTigger]
for thisComponent in scannerTriggerComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "scannerTrigger"-------
while continueRoutine:
    # get current time
    t = scannerTriggerClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *scanner_cue_key* updates
    if t >= 0.0 and scanner_cue_key.status == NOT_STARTED:
        # keep track of start time/frame for later
        scanner_cue_key.tStart = t
        scanner_cue_key.frameNStart = frameN  # exact frame index
        scanner_cue_key.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(scanner_cue_key.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if scanner_cue_key.status == STARTED:
        theseKeys = event.getKeys(keyList=['num_add', '+', 'equal'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            scanner_cue_key.keys.extend(theseKeys)  # storing all keys
            scanner_cue_key.rt.append(scanner_cue_key.clock.getTime())
            # a response ends the routine
            continueRoutine = False
    
    # *scannertrigger_fixation* updates
    if t >= 0.0 and scannertrigger_fixation.status == NOT_STARTED:
        # keep track of start time/frame for later
        scannertrigger_fixation.tStart = t
        scannertrigger_fixation.frameNStart = frameN  # exact frame index
        scannertrigger_fixation.setAutoDraw(True)
    
    # *text_scannerTigger* updates
    if t >= 0.0 and text_scannerTigger.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_scannerTigger.tStart = t
        text_scannerTigger.frameNStart = frameN  # exact frame index
        text_scannerTigger.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in scannerTriggerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "scannerTrigger"-------
for thisComponent in scannerTriggerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if scanner_cue_key.keys in ['', [], None]:  # No response was made
    scanner_cue_key.keys=None
thisExp.addData('scanner_cue_key.keys',scanner_cue_key.keys)
if scanner_cue_key.keys != None:  # we had a response
    thisExp.addData('scanner_cue_key.rt', scanner_cue_key.rt)
thisExp.nextEntry()
# the Routine "scannerTrigger" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "prescan"-------
t = 0
prescanClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(6.000000)
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
    frameRemains = 0.0 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
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
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(parametersFile),
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
    
    time_ISIA=float(ISIA)
    time_ISIB=float(ISIB)
    stime_instructions=time_ISIB
    stime_image_IAPS=time_ISIB+2
    ttime=time_ISIB+10+time_ISIA
    routineTimer.add(ttime)
    # update component parameters for each repeat
    
    
    debug_text2.setText(stimClassDesc)
    # keep track of which components have finished
    presentationComponents = [image_fixation_ISI, image_blank, instructions_pic, ISI_2, image_IAPS, debug_text2, ISI_1]
    for thisComponent in presentationComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "presentation"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = presentationClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        
        # *image_fixation_ISI* updates
        if t >= 0.0 and image_fixation_ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_fixation_ISI.tStart = t
            image_fixation_ISI.frameNStart = frameN  # exact frame index
            image_fixation_ISI.setAutoDraw(True)
        frameRemains = 0.0 + ttime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_fixation_ISI.status == STARTED and t >= frameRemains:
            image_fixation_ISI.setAutoDraw(False)
        
        # *image_blank* updates
        if t >= time_ISIB and image_blank.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_blank.tStart = t
            image_blank.frameNStart = frameN  # exact frame index
            image_blank.setAutoDraw(True)
        frameRemains = time_ISIB + 10 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_blank.status == STARTED and t >= frameRemains:
            image_blank.setAutoDraw(False)
        
        # *instructions_pic* updates
        if t >= time_ISIB and instructions_pic.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructions_pic.tStart = t
            instructions_pic.frameNStart = frameN  # exact frame index
            instructions_pic.setAutoDraw(True)
        frameRemains = time_ISIB + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if instructions_pic.status == STARTED and t >= frameRemains:
            instructions_pic.setAutoDraw(False)
        
        # *image_IAPS* updates
        if t >= (time_ISIB+2) and image_IAPS.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_IAPS.tStart = t
            image_IAPS.frameNStart = frameN  # exact frame index
            image_IAPS.setAutoDraw(True)
            IAPSshownTime[trials.thisIndex] = prescanClock.getTime()
        frameRemains = time_ISIB + 2 + 8- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_IAPS.status == STARTED and t >= frameRemains:
            image_IAPS.setAutoDraw(False)
        
        # *debug_text2* updates
        if t >= .5 and debug_text2.status == NOT_STARTED:
            # keep track of start time/frame for later
            debug_text2.tStart = t
            debug_text2.frameNStart = frameN  # exact frame index
            debug_text2.setAutoDraw(True)
        frameRemains = time_ISIB + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
        if debug_text2.status == STARTED and t >= frameRemains:
            debug_text2.setAutoDraw(False)
        
        # *ISI_2* period
        if t >= 0.0 and ISI_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI_2.tStart = t
            ISI_2.frameNStart = frameN  # exact frame index
            ISI_2.start(time_ISIB)
        elif ISI_2.status == STARTED:  # one frame should pass before updating params and completing
            # updating other components during *ISI_2*
            instructions_pic.setImage(instructions_image)
            image_IAPS.setImage(IAPS_image)
            debug_text2.setText(stimClassDesc)
            # component updates done
            ISI_2.complete()  # finish the static period
        # *ISI_1* period
        if t >= (time_ISIB+10) and ISI_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI_1.tStart = t
            ISI_1.frameNStart = frameN  # exact frame index
            ISI_1.start(time_ISIA)
            IAPSshownDuration[trials.thisIndex] = image_IAPS.tStart
        elif ISI_1.status == STARTED:  # one frame should pass before updating params and completing
            # updating other components during *ISI_1*
            IAPSshown[trials.thisIndex] = IAPS_image[8:-4]
            IAPSstimClassDesc[trials.thisIndex] = stimClassDesc
            IAPSstimGroup[trials.thisIndex] = stimClass
            InstructionsShown[trials.thisIndex] = instructions_image[13:-4]
            # component updates done
            ISI_1.complete()  # finish the static period
        
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
    
    
    # ------Prepare to start Routine "response"-------
    t = 0
    responseClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    rating.reset()
    event.clearEvents(eventType='keyboard')
    # keep track of which components have finished
    responseComponents = [rating, rating_instructions]
    for thisComponent in responseComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    IAPSresponseTime[trials.thisIndex] = prescanClock.getTime()
    # -------Start Routine "response"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = responseClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rating_instructions* updates
        if t >= 0.0 and rating_instructions.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating_instructions.tStart = t
            rating_instructions.frameNStart = frameN  # exact frame index
            rating_instructions.setAutoDraw(True)
        frameRemains = 0.0 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
        if rating_instructions.status == STARTED and t >= frameRemains:
            rating_instructions.setAutoDraw(False)
        # *rating* updates
        if t >= 0 and rating.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating.tStart = t
            rating.frameNStart = frameN  # exact frame index
            rating.setAutoDraw(True)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in responseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "response"-------
    for thisComponent in responseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    trials.addData('rating.response', rating.getRating())
    trials.addData('rating.rt', rating.getRT())
    trials.addData('rating.history', rating.getHistory())
    if rating.history[-1][0] is None:
        finalResp[trials.thisIndex] = -1
    else:
        finalResp[trials.thisIndex] = int(rating.history[-1][0])
    finalRespRT[trials.thisIndex] = rating.history[-1][1]
    print(trials.thisIndex, IAPSshown[trials.thisIndex], finalResp[trials.thisIndex])
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "logData"-------
t = 0
logDataClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
experimentEnd = prescanClock.getTime()
#exptInfo = u'participant %s session %s date %s\n\n' %(expInfo['participant'], expInfo['session'], expInfo['date'])
#f.write(expInfo['participant'])
# datafile = u'data/Data_%s_%s%s_%s_%s.txt' %(expInfo['participant'], expInfo['randomization'], expInfo['session'], expName, expInfo['date'])
datafile = u'data/sub-%s_task-%s_run-00%s_parm-%s%s_date-%s_events.tsv' %(expInfo['participant'], expName, expInfo['session'], expInfo['randomization'], expInfo['session'], expInfo['date'])
f = open(datafile,'w')
f.write(
    'onset' + '\t' + # stim_startTime
    'duration' + '\t' + 
    'trial' + '\t' + 
    'instructions' + '\t' + 
    'trial_type' + '\t' + # stim_classDesc
    'stim_groupID' + '\t' + 
    'stimulus' + '\t' + 
    'finalResp' + '\t' + 
    'finalResp_RT' + '\t' + 
    'respPeriod_startTime' + '\t' + 
    'subject' + '\t' + 
    'randomization' + '\t' + 
    'randomizationInput' + '\t' + 
    'parametersFile' + '\n')
for n in range(0,len(finalResp)):
    f.write(
        str(IAPSshownTime[n]) + '\t' + 
        str(8.000) + '\t' + #hardcoded duration, be careful
        str(n+1) + '\t' + 
        str(InstructionsShown[n]) + '\t' + 
        str(IAPSstimClassDesc[n]) + '\t' + 
        str(IAPSstimGroup[n]) + '\t' + 
        str(IAPSshown[n]) + '\t' + 
        str(finalResp[n]) + '\t' + 
        str(finalRespRT[n]) + '\t' + 
        str(IAPSresponseTime[n]) + '\t' + 
        expInfo['participant'] + '\t' + 
        parametersFile[17:-4] + '\t' + 
        expInfo['randomization'] + '\t' + 
        parametersFile + '\n')
f.write(
    str(experimentEnd+10.000) + '\t' + 
    str(10.000) + '\t' 
    'n/a' + '\t' + 
    'rest' + '\t' + 
    'rest' + '\t' + 
    'rest' + '\t' + 
    'rest' + '\t' + 
    'n/a' + '\t' + 
    'n/a' + '\t' + 
    'n/a' + '\t' + 
    expInfo['participant'] + '\t' + 
    parametersFile[17:-4] + '\t' + 
    expInfo['randomization'] + '\t' + 
    parametersFile + '\n')
f.close() # you can omit in most cases as the destructor will call it
# keep track of which components have finished
logDataComponents = [fixation_final]
for thisComponent in logDataComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "logData"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = logDataClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *fixation_final* updates
    if t >= 0.0 and fixation_final.status == NOT_STARTED:
        # keep track of start time/frame for later
        fixation_final.tStart = t
        fixation_final.frameNStart = frameN  # exact frame index
        fixation_final.setAutoDraw(True)
    frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if fixation_final.status == STARTED and t >= frameRemains:
        fixation_final.setAutoDraw(False)
    
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
endComponents = [image_end]
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_end* updates
    if t >= 0.0 and image_end.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_end.tStart = t
        image_end.frameNStart = frameN  # exact frame index
        image_end.setAutoDraw(True)
    frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if image_end.status == STARTED and t >= frameRemains:
        image_end.setAutoDraw(False)
    
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







# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
