import csv

totalOLPct = []
totalDLPct = []
numDefLine = 0
def threeGapCalc():
    global totalDLPct
    hole2 = (totalDLPct[0] + totalDLPct[1]) / 2.0
    totalDLPct.insert(1, hole2)
def fourGapCalc():
    global totalDLPct
    hole2 = (totalDLPct[0] + totalDLPct[1]) / 2.0
    totalDLPct.insert(1, hole2)
    hole5 = (totalDLPct[2] + totalDLPct[3]) / 2.0
    totalDLPct.insert(4, hole5)
def marginDL(stopPct, posRun):
    natDL = 25.4189
    stopPercent = []
    runPercent = []
    totalPct = []
    for stop in stopPct:
        stopPercent.append(float(stop[:len(stop) - 1]))
    for run in posRun:
        runPercent.append(float(run[:len(run) - 1]))
    for index, baseStop in enumerate(stopPercent):
        if index == 0 or index == len(stopPercent) - 1:
            stopPercent[index] = baseStop * 4.189189189
        else:
            stopPercent[index] = baseStop * 3.32908224
        totalPct.append(stopPercent[index] + runPercent[index] - natDL)
    global totalDLPct
    totalDLPct = totalPct
    if numDefLine == 3:
        threeGapCalc()
    if numDefLine == 4:
        fourGapCalc()

    print totalDLPct

def marginOL(inside, outside):
    insideT = 32.2
    outsideT = 48.4
    insideG = 37.2
    outsideG = 39.6
    leftC = 35.1
    rightC = 36.5
    insidePct = []
    outsidePct = []
    totalPct = []
    for ins in inside:
        insidePct.append(float(ins[:len(ins) - 1]))
    for out in outside:
        outsidePct.append(float(out[:len(out) - 1]))
    hole1 = outsidePct[0] - outsideT
    totalPct.append(-hole1)
    hole2 = (outsidePct[1] - outsideG) + (insidePct[0] - insideT)
    hole2 = hole2 / -2.0
    totalPct.append(hole2)
    hole3 = (outsidePct[2] - leftC) + (insidePct[1] - insideG)
    hole3 = hole3 / -2.0
    totalPct.append(hole3)
    hole4 = (insidePct[3] - insideG) + (insidePct[2] - rightC)
    hole4 = hole4 / -2.0
    totalPct.append(hole4)
    hole5 = (outsidePct[3] - outsideG) + (insidePct[4] - insideT)
    hole5 = hole5 / -2.0
    totalPct.append(hole5)
    hole6 = outsidePct[4] - outsideT
    totalPct.append(-hole6)
    global totalOLPct
    totalOLPct = totalPct
    print totalOLPct

def matchPlayers(oLine):
    num = 0
    playerNames = []
    insidePcts = []
    outsidePcts = []
    playerInsidePct = []
    playerOutsidePct = []
    with open('NCAA OL Report.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            num += 1
            if num >= 5 and num < 10:
                playerNames.append(row[12])
                insidePcts.append(row[27])
                outsidePcts.append(row[28])
    for x in range(0, 5):
        for index, name in enumerate(playerNames):
            if name == oLine[x]:
                playerInsidePct.append(insidePcts[index])
                playerOutsidePct.append(outsidePcts[index])
    marginOL(playerInsidePct, playerOutsidePct)
    print playerInsidePct
    print playerOutsidePct

def dmatchPlayers(dLine):
    num = 0
    playerNames = []
    runPcts = []
    stopPcts = []
    playerRunPct = []
    playerStopPct = []
    with open('NCAA Def Front 7 Report.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            num += 1
            if num >= 5 and num < 9:
                playerNames.append(row[5])
                runPcts.append(row[16])
                stopPcts.append(row[21])
    for x in range(0, 3):
        for index, name in enumerate(playerNames):
            if name == dLine[x]:
                playerRunPct.append(runPcts[index])
                playerStopPct.append(stopPcts[index])
    marginDL(playerStopPct, playerRunPct)
    print playerRunPct
    print playerStopPct

def compareLines():
    comparedNum = []
    if numDefLine == 3:
        comparedNum.append(totalOLPct[0] - totalDLPct[0])
        comparedNum.append(totalOLPct[1] - totalDLPct[1])
        comparedNum.append(totalOLPct[2] - totalDLPct[2])
        comparedNum.append(totalOLPct[3] - totalDLPct[2])
        comparedNum.append(totalOLPct[4] - totalDLPct[3])
        comparedNum.append(totalOLPct[5] - totalDLPct[3])
    if numDefLine == 4:
        comparedNum.append(totalOLPct[0] - totalDLPct[0])
        comparedNum.append(totalOLPct[1] - totalDLPct[1])
        comparedNum.append(totalOLPct[2] - totalDLPct[1])
        comparedNum.append(totalOLPct[3] - totalDLPct[2])
        comparedNum.append(totalOLPct[4] - totalDLPct[3])
        comparedNum.append(totalOLPct[5] - totalDLPct[4])
    print comparedNum

num = 0
offense = raw_input("What school's offensive line?")
defense = raw_input("What school's defense line?")
linemen = raw_input("What defense does this school run?")
numDefLine = int(linemen[:1])
schools = []
starters = []
depthChart = []
LTindex = 0
LGindex = 0
OCindex = 0
RGindex = 0
RTindex = 0
index = 0
filename = str(offense) + ' Depth Chart.csv'
with open(filename) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if row[0] == 'LT':
            LTindex = index
        if row[0] == 'LG':
            LGindex = index
        if row[0] == 'OC':
            OCindex = index
        if row[0] == 'RG':
            RGindex = index
        if row[0] == 'RT':
            RTindex = index
        index += 1
        depthChart.append(row)
    starters.append(depthChart[LTindex + 2])
    starters.append(depthChart[LGindex + 2])
    starters.append(depthChart[OCindex + 2])
    starters.append(depthChart[RGindex + 2])
    starters.append(depthChart[RTindex + 2])
    print(starters)

for index, name in enumerate(starters):
    last, first, x = str(name).split(" ", 2)
    starters[index] = last[2:] + " " + first
print starters
matchPlayers(starters)

dstarters = []
ddepthChart = []
DEindex = 0
DTindex = 0
DE2index = 0
DT2index = 0

dindex = 0
filename = str(defense) + ' Depth Chart.csv'
first = True
firstDT = True
with open(filename) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if row[0] == 'DE' and first:
            DEindex = dindex
            first = False
        elif row[0] == 'DE' and first is False:
            DE2index = dindex
        if numDefLine == 3 and row[0] == 'NT':
            DTindex = dindex
        if numDefLine == 4 and row[0] == 'DT' and firstDT:
            DTindex = dindex
            firstDT = False
        if numDefLine == 4 and row[0] == 'DT' and firstDT is False:
            DT2index = dindex

        dindex += 1
        ddepthChart.append(row)
    dstarters.append(ddepthChart[DEindex + 2])
    dstarters.append(ddepthChart[DTindex + 2])
    dstarters.append(ddepthChart[DT2index + 2])
    if ddepthChart[DEindex + 2] == ddepthChart[DE2index + 2]:
        dstarters.append(ddepthChart[DE2index + 4])
    else:
        dstarters.append(ddepthChart[DE2index + 2])



for index, name in enumerate(dstarters):
    last, first, x = str(name).split(" ", 2)
    dstarters[index] = last[2:] + " " + first
print dstarters
dmatchPlayers(dstarters)
compareLines()


