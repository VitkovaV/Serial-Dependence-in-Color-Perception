#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.1),
    on June 14, 2017, at 23:12
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
expName = 'OneStepFurther1'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'E:\\SCAN\\Summer Semester\\Experiment\\OneStepFurther1.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1536, 864), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "start"
startClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='In this task you can change the color(its red component) of a square by pressing left or right arrow, and then go to a next trial by pressing SPACE.\n\n\npress any mouse button (needed for iohub) and then space to start\n\n\n',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial_red"
trial_redClock = core.Clock()
polygon_2 = visual.Polygon(
    win=win, name='polygon_2',
    edges=90, size=(0.5, 0.5),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
Noise_patch1 = visual.ImageStim(
    win=win, name='Noise_patch1',
    image='sin', mask=u'circle',
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
polygon = visual.Polygon(
    win=win, name='polygon',
    edges=90, size=[0.5, 0.5],
    ori=0, pos=[0, 0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)

from psychopy.iohub import launchHubServer, EventConstants

io=launchHubServer(experiment_code='key_evts', psychopy_monitor_name='default')
keyboard = io.devices.keyboard

increment=0
green = 0.5 # initial value of scaling factor

color=[1,green,0]

red = 0.5

blue = 0.5
noiseTexture = np.random.rand(256,256) * 2 - 1
Fixation_cross1 = visual.TextStim(win=win, name='Fixation_cross1',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-8.0);
Fixation_cross2 = visual.TextStim(win=win, name='Fixation_cross2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-9.0);

# Initialize components for Routine "trial_blue"
trial_blueClock = core.Clock()
polygon_3 = visual.Polygon(
    win=win, name='polygon_3',
    edges=90, size=(0.5, 0.5),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
Noise_patch2 = visual.ImageStim(
    win=win, name='Noise_patch2',
    image=noiseTexture, mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
polygon_4 = visual.Polygon(
    win=win, name='polygon_4',
    edges=90, size=(0.5, 0.5),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)


# Initialize components for Routine "trial_green"
trial_greenClock = core.Clock()
polygon_5 = visual.Polygon(
    win=win, name='polygon_5',
    edges=90, size=(0.5, 0.5),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
Noise_patch3 = visual.ImageStim(
    win=win, name='Noise_patch3',
    image=noiseTexture, mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
polygon_6 = visual.Polygon(
    win=win, name='polygon_6',
    edges=90, size=(0.5, 0.5),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)


# Initialize components for Routine "end"
endClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='This is the end of the experiment.',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "start"-------
t = 0
startClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()
# keep track of which components have finished
startComponents = [text, key_resp_2]
for thisComponent in startComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "start"-------
while continueRoutine:
    # get current time
    t = startClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
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
    for thisComponent in startComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "start"-------
for thisComponent in startComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Stimuli-red.xlsx'),
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
    
    # ------Prepare to start Routine "trial_red"-------
    t = 0
    trial_redClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    polygon_2.setFillColor(stimulus_color)
    polygon_2.setLineColor(stimulus_color)
    Noise_patch1.setImage(noiseTexture)
    color= [1,green,0]
    green = 0.5
    key_resp_3 = event.BuilderKeyResponse()
    
    
    # keep track of which components have finished
    trial_redComponents = [polygon_2, Noise_patch1, ISI, polygon, key_resp_3, Fixation_cross1, Fixation_cross2]
    for thisComponent in trial_redComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial_red"-------
    while continueRoutine:
        # get current time
        t = trial_redClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_2* updates
        if t >= 2 and polygon_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_2.tStart = t
            polygon_2.frameNStart = frameN  # exact frame index
            polygon_2.setAutoDraw(True)
        frameRemains = 2 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if polygon_2.status == STARTED and t >= frameRemains:
            polygon_2.setAutoDraw(False)
        
        # *Noise_patch1* updates
        if t >= 2.5 and Noise_patch1.status == NOT_STARTED:
            # keep track of start time/frame for later
            Noise_patch1.tStart = t
            Noise_patch1.frameNStart = frameN  # exact frame index
            Noise_patch1.setAutoDraw(True)
        frameRemains = 2.5 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Noise_patch1.status == STARTED and t >= frameRemains:
            Noise_patch1.setAutoDraw(False)
        
        # *polygon* updates
        if t >= 3.75 and polygon.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon.tStart = t
            polygon.frameNStart = frameN  # exact frame index
            polygon.setAutoDraw(True)
        if polygon.status == STARTED:  # only update if drawing
            polygon.setFillColor(color, log=False)
            polygon.setLineColor(color, log=False)
        for event_io in keyboard.getEvents():
                if event_io.type == EventConstants.KEYBOARD_PRESS:
                # a key has been pressed. This is reported only once, so set the value 
                # of the scaling factor to be used until the key is released:
                    if event_io.key == u'right':
                        increment = 0.05 # make it 1% of screen half-width longer
                    elif event_io.key == u'left':
                        increment = -0.05 # make 1% shorter
                if event_io.type == EventConstants.KEYBOARD_RELEASE:
                # the key is no longer being pressed, so stop changing the size:
                    increment = 0
        
            # regardless of what key is/isn't pressed, apply the current
            # scaling factor on every screen refresh
        
        
        #if red <= 0:
         #  if event_io.key == u'left':
          #   increment = 0
           #elif event_io.key== u'right':
            # red += increment
         # color = [red, 0, 1]
        
        #if red >= 1:
         #  if event_io.key == u'right':
        #     increment = 0
         #  if event_io.key == u'left':
         #    red += increment
        if green>1: green =1
        if green<0: green =0
        
        if 0 <= green <= 1:
        
        
        
                green += increment
                color = [1,green,0]
        
        # *key_resp_3* updates
        if t >= 4 and key_resp_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_3.tStart = t
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key_resp_3.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        
        
        # *Fixation_cross1* updates
        if t >= 0.0 and Fixation_cross1.status == NOT_STARTED:
            # keep track of start time/frame for later
            Fixation_cross1.tStart = t
            Fixation_cross1.frameNStart = frameN  # exact frame index
            Fixation_cross1.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Fixation_cross1.status == STARTED and t >= frameRemains:
            Fixation_cross1.setAutoDraw(False)
        
        # *Fixation_cross2* updates
        if t >= 3.5 and Fixation_cross2.status == NOT_STARTED:
            # keep track of start time/frame for later
            Fixation_cross2.tStart = t
            Fixation_cross2.frameNStart = frameN  # exact frame index
            Fixation_cross2.setAutoDraw(True)
        frameRemains = 3.5 + 0.25- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Fixation_cross2.status == STARTED and t >= frameRemains:
            Fixation_cross2.setAutoDraw(False)
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(0.5)
        elif ISI.status == STARTED:  # one frame should pass before updating params and completing
            ISI.complete()  # finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_redComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_red"-------
    for thisComponent in trial_redComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('colorChosen', color)
    thisExp.addData('prop_red', green)
    
    
    
    # the Routine "trial_red" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials.saveAsText(filename + 'trials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Stimuli-blue.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2.keys():
        exec(paramName + '= thisTrial_2.' + paramName)

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2.keys():
            exec(paramName + '= thisTrial_2.' + paramName)
    
    # ------Prepare to start Routine "trial_blue"-------
    t = 0
    trial_blueClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    polygon_3.setFillColor(stimulus_color)
    polygon_3.setLineColor(stimulus_color)
    key_resp_4 = event.BuilderKeyResponse()
    color= [red,0,1]
    red = 0.5
    # keep track of which components have finished
    trial_blueComponents = [polygon_3, Noise_patch2, polygon_4, key_resp_4]
    for thisComponent in trial_blueComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial_blue"-------
    while continueRoutine:
        # get current time
        t = trial_blueClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_3* updates
        if t >= 1 and polygon_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_3.tStart = t
            polygon_3.frameNStart = frameN  # exact frame index
            polygon_3.setAutoDraw(True)
        frameRemains = 1 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if polygon_3.status == STARTED and t >= frameRemains:
            polygon_3.setAutoDraw(False)
        
        # *Noise_patch2* updates
        if t >= 2.5 and Noise_patch2.status == NOT_STARTED:
            # keep track of start time/frame for later
            Noise_patch2.tStart = t
            Noise_patch2.frameNStart = frameN  # exact frame index
            Noise_patch2.setAutoDraw(True)
        frameRemains = 2.5 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Noise_patch2.status == STARTED and t >= frameRemains:
            Noise_patch2.setAutoDraw(False)
        
        # *polygon_4* updates
        if t >= 3 and polygon_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_4.tStart = t
            polygon_4.frameNStart = frameN  # exact frame index
            polygon_4.setAutoDraw(True)
        if polygon_4.status == STARTED:  # only update if drawing
            polygon_4.setFillColor(color, log=False)
            polygon_4.setLineColor(color, log=False)
        
        # *key_resp_4* updates
        if t >= 3.5 and key_resp_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_4.tStart = t
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_4.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_4.keys = theseKeys[-1]  # just the last key pressed
                key_resp_4.rt = key_resp_4.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        for event_io in keyboard.getEvents():
                if event_io.type == EventConstants.KEYBOARD_PRESS:
                # a key has been pressed. This is reported only once, so set the value 
                # of the scaling factor to be used until the key is released:
                    if event_io.key == u'right':
                        increment = 0.05 # make it 1% of screen half-width longer
                    elif event_io.key == u'left':
                        increment = -0.05 # make 1% shorter
                if event_io.type == EventConstants.KEYBOARD_RELEASE:
                # the key is no longer being pressed, so stop changing the size:
                    increment = 0
        
            # regardless of what key is/isn't pressed, apply the current
            # scaling factor on every screen refresh
        
        
        #if red <= 0:
         #  if event_io.key == u'left':
          #   increment = 0
           #elif event_io.key== u'right':
            # red += increment
         # color = [red, 0, 1]
        
        #if red >= 1:
         #  if event_io.key == u'right':
        #     increment = 0
         #  if event_io.key == u'left':
         #    red += increment
        
        if 0 <= red <= 1:
        
        
        
                red += increment
                color = [red,0,1]
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_blueComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_blue"-------
    for thisComponent in trial_blueComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys=None
    trials_2.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        trials_2.addData('key_resp_4.rt', key_resp_4.rt)
    thisExp.addData('colorChosen', color)
    thisExp.addData('prop_red', red)
    # the Routine "trial_blue" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_2'

# get names of stimulus parameters
if trials_2.trialList in ([], [None], None):
    params = []
else:
    params = trials_2.trialList[0].keys()
# save data for this loop
trials_2.saveAsExcel(filename + '.xlsx', sheetName='trials_2',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials_2.saveAsText(filename + 'trials_2.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Stimuli-green.xlsx'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3.keys():
        exec(paramName + '= thisTrial_3.' + paramName)

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3.keys():
            exec(paramName + '= thisTrial_3.' + paramName)
    
    # ------Prepare to start Routine "trial_green"-------
    t = 0
    trial_greenClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    polygon_5.setFillColor(stimulus_color)
    polygon_5.setLineColor(stimulus_color)
    key_resp_5 = event.BuilderKeyResponse()
    color= [0,1,blue]
    blue = 0.5
    # keep track of which components have finished
    trial_greenComponents = [polygon_5, Noise_patch3, polygon_6, key_resp_5]
    for thisComponent in trial_greenComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial_green"-------
    while continueRoutine:
        # get current time
        t = trial_greenClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_5* updates
        if t >= 1 and polygon_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_5.tStart = t
            polygon_5.frameNStart = frameN  # exact frame index
            polygon_5.setAutoDraw(True)
        frameRemains = 1 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if polygon_5.status == STARTED and t >= frameRemains:
            polygon_5.setAutoDraw(False)
        
        # *Noise_patch3* updates
        if t >= 2.5 and Noise_patch3.status == NOT_STARTED:
            # keep track of start time/frame for later
            Noise_patch3.tStart = t
            Noise_patch3.frameNStart = frameN  # exact frame index
            Noise_patch3.setAutoDraw(True)
        frameRemains = 2.5 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Noise_patch3.status == STARTED and t >= frameRemains:
            Noise_patch3.setAutoDraw(False)
        
        # *polygon_6* updates
        if t >= 3 and polygon_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_6.tStart = t
            polygon_6.frameNStart = frameN  # exact frame index
            polygon_6.setAutoDraw(True)
        if polygon_6.status == STARTED:  # only update if drawing
            polygon_6.setFillColor(color, log=False)
            polygon_6.setLineColor(color, log=False)
        
        # *key_resp_5* updates
        if t >= 3.5 and key_resp_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_5.tStart = t
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_5.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_5.keys = theseKeys[-1]  # just the last key pressed
                key_resp_5.rt = key_resp_5.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        for event_io in keyboard.getEvents():
                if event_io.type == EventConstants.KEYBOARD_PRESS:
                # a key has been pressed. This is reported only once, so set the value 
                # of the scaling factor to be used until the key is released:
                    if event_io.key == u'right':
                        increment = 0.05 # make it 1% of screen half-width longer
                    elif event_io.key == u'left':
                        increment = -0.05 # make 1% shorter
                if event_io.type == EventConstants.KEYBOARD_RELEASE:
                # the key is no longer being pressed, so stop changing the size:
                    increment = 0
        
            # regardless of what key is/isn't pressed, apply the current
            # scaling factor on every screen refresh
        
        
        #if red <= 0:
         #  if event_io.key == u'left':
          #   increment = 0
           #elif event_io.key== u'right':
            # red += increment
         # color = [red, 0, 1]
        
        #if red >= 1:
         #  if event_io.key == u'right':
        #     increment = 0
         #  if event_io.key == u'left':
         #    red += increment
        
        if 0 <= blue <= 1:
        
        
        
                blue += increment
                color = [0,1,blue]
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_greenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_green"-------
    for thisComponent in trial_greenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys=None
    trials_3.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        trials_3.addData('key_resp_5.rt', key_resp_5.rt)
    thisExp.addData('colorChosen', color)
    thisExp.addData('prop_red', blue)
    # the Routine "trial_green" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_3'

# get names of stimulus parameters
if trials_3.trialList in ([], [None], None):
    params = []
else:
    params = trials_3.trialList[0].keys()
# save data for this loop
trials_3.saveAsExcel(filename + '.xlsx', sheetName='trials_3',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials_3.saveAsText(filename + 'trials_3.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [text_2]
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_2.status == STARTED and t >= frameRemains:
        text_2.setAutoDraw(False)
    
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
