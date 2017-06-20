#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.1),
    on June 19, 2017, at 12:03
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
    text='In this experiment you will see two circular stimuli one after the other.\nYour task is to adjust the color of the second circle in a way that it resembles as musch as possible the color of the first one.\nYou can adjust the color by pressing the left and right arrow keys.\nSubmit your answer by pressing Space bar. \n\n\nTo start the experiment press any mouse button (needed for iohub) and then space. \n\n',
    font='Arial',
    pos=[0, 0], height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "all_trials"
all_trialsClock = core.Clock()
inducer_stimulus = visual.Polygon(
    win=win, name='inducer_stimulus',
    edges=90, size=(0.5, 0.5),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
Noise_patch = visual.ImageStim(
    win=win, name='Noise_patch',
    image='sin', mask='circle',
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
i = 1
from psychopy.iohub import launchHubServer, EventConstants

io=launchHubServer(experiment_code='key_evts', psychopy_monitor_name='default')
keyboard = io.devices.keyboard

increment=0
green = 0.5 # initial value of scaling factor

color=[1,green,0]

red = 0.5

blue = 0.5

green =0.5
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
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trials_R_reduced.xlsx'),
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
    
    # ------Prepare to start Routine "all_trials"-------
    t = 0
    all_trialsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    inducer_stimulus.setFillColor([red,green,blue])
    inducer_stimulus.setLineColor([red,green,blue])
    Noise_patch.setImage(noiseTexture)
    
    
    
    
    if i <=5:
     green = random()
     red =1
     blue = 0
    
    if i >5:
      blue = random()
      red=0
      green=1
    
    if i > 10:
     red = random
     blue=1
     green=0
    
    color= [red, green, blue]
    key_resp_3 = event.BuilderKeyResponse()
    
    
    stimulus_color = [red,green,blue]
    # keep track of which components have finished
    all_trialsComponents = [inducer_stimulus, Noise_patch, ISI, polygon, key_resp_3, Fixation_cross1, Fixation_cross2]
    for thisComponent in all_trialsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "all_trials"-------
    while continueRoutine:
        # get current time
        t = all_trialsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *inducer_stimulus* updates
        if t >= 2 and inducer_stimulus.status == NOT_STARTED:
            # keep track of start time/frame for later
            inducer_stimulus.tStart = t
            inducer_stimulus.frameNStart = frameN  # exact frame index
            inducer_stimulus.setAutoDraw(True)
        frameRemains = 2 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if inducer_stimulus.status == STARTED and t >= frameRemains:
            inducer_stimulus.setAutoDraw(False)
        
        # *Noise_patch* updates
        if t >= 2.5 and Noise_patch.status == NOT_STARTED:
            # keep track of start time/frame for later
            Noise_patch.tStart = t
            Noise_patch.frameNStart = frameN  # exact frame index
            Noise_patch.setAutoDraw(True)
        frameRemains = 2.5 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Noise_patch.status == STARTED and t >= frameRemains:
            Noise_patch.setAutoDraw(False)
        
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
         
        if i <=5:
        
         if green>1: green =1
         if green<0: green =0
        
         if 0 <= green <= 1:
        
        
                green += increment
                color = [1,green,0]
        
        
        if i >5:
        
         if blue>1: blue =1
         if blue<0: blue =0
         
         if 0 <= blue <= 1:
        
        
                blue += increment
                color = [0,1,blue]
        
        if i >10:
        
         if red>1: red =1
         if red<0: red =0
         
         if 0 <= red <= 1:
        
        
                red += increment
                color = [red,0,1]
        
        # *key_resp_3* updates
        if t >= 4 and key_resp_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_3.tStart = t
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_3.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if key_resp_3.keys == []:  # then this was the first keypress
                    key_resp_3.keys = theseKeys[0]  # just the first key pressed
                    key_resp_3.rt = key_resp_3.clock.getTime()
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
        for thisComponent in all_trialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "all_trials"-------
    for thisComponent in all_trialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('colorChosen', color)
    thisExp.addData('prop_red', green)
    
    
    i =i+1
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys=None
    trials.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        trials.addData('key_resp_3.rt', key_resp_3.rt)
    
    
    
    # the Routine "all_trials" was not non-slip safe, so reset the non-slip timer
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
