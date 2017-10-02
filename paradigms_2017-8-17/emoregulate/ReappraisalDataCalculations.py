# !/usr/local/bin/python
# coding: latin-1

import numpy as np

# -------------------------- Parameters --------------------------
IAPSmatrix = #row = IAPSshown, column = block. Col0 = a1, Col1 = a2, Col2 = a3, Col3 = a4 or b1,b2.b3,b4
stimClass = #row = instruction ('A' = attend, 'R' = Reappraise), column = block. Col1 = a2, Col2 = a3, Col3 = a4 or b1,b2.b3,b4
target = #row = target ('S' = self, 'O' = other, 'x' = no traget (stim is neural)), column = block. Col1 = a2, Col2 = a3, Col3 = a4 or b1,b2.b3,b4
valence = #row = valence ('N' = neutral, 'T' = threat, 'D' = disgust), column = block. Col1 = a2, Col2 = a3, Col3 = a4 or b1,b2.b3,b4
Resp =  selectedResp[:,0,:] #row = subject's rating, column = block. Col0 = a1, Col1 = a2, Col2 = a3, Col3 = a4 or b1,b2.b3,b4
RT = selectedResp[:,1,:] #row = response time (ms), column = block. Col0 = a1, Col1 = a2, Col2 = a3, Col3 = a4 or b1,b2.b3,b4
nBlocks = 4

# Stimuli related to response rating 
dResp = Resp-verdicalResp #difference between subject's rating and IAPS rating    
pdResp = dResp/verdicalResp #percent or normalized difference between subject's rating and IAPS rating


# -------------------------- matrix with all parameters --------------------------
summary = np.empty((nTrials+1, nBlocks, 6)) #trials x blocks x parameter
for i in range(nBlocks):
    summary[0][i][0] = 'dResp'
    summary[0][i][1] = 'pdResp'
    summary[0][i][2] = 'stimClass' # 'A' or 'R'
    summary[0][i][3] = 'target' # 'S', 'O', or 'x'
    summary[0][i][4] = 'valence' # 'N', 'D', or 'T'
    summary[0][i][5] = 'RT'
summary[1:][:][0] = dResp
summary[1:][:][1] = pdResp
summary[1:][:][2] = stimClass
summary[1:][:][3] = target
summary[1:][:][4] = valence
summary[1:][:][5] = RT


# ------ Lists of dResp and RT by each stimulus class, target, and valence ------

# create an empty list for each parameter
dRespAttend = [] 
RTAttend = []
dRespReapp = [] 
RTReapp = []
dRespSelf= [] 
RTSelf = []
dRespOther = [] 
RTOther = []
dRespNeutral = [] 
RTNeutral = []
dRespDisgust = [] 
RTDisgust = []
dRespThreat = [] 
RTThreat = []

# append values to respective lists based on parameters
for i in range(nBlocks):
    for j in range(1,nTrials+1):
        #stimClass lists
        if summary[j][i][2] == 'A': #stimClass is Attend
            dRespAttend.append(summary[j][i][0])
            RTAttend.append(summary[j][i][5])
        else: #stimClass is Reappraise
            dRespReapp.append(summary[j][i][0])
            RTReapp.append(summary[j][i][5])
        #target lists
        if summary[j][i][3] == 'S': #target is Self
            dRespSelf.append(summary[j][i][0])
            RTSelf.append(summary[j][i][5])
        elif summary[j][i][3] == 'O': #target is Other
            dRespOther.append(summary[j][i][0])
            RTOther.append(summary[j][i][5])
        else: #no target (target is 'x')
            continue
        #valence lists
        if summary[j][i][4] == 'N': #valence is Neutral
            dRespNeutral.append(summary[j][i][0])
            RTNeutral.append(summary[j][i][5])
        elif summary[j][i][4] == 'D': #valence is Disgust
            dRespDisgust.append(summary[j][i][0])
            RTDisgust.append(summary[j][i][5])
        else: #valence is Threat
            dRespThreat.append(summary[j][i][0])
            RTThreat.append(summary[j][i][5])
        


