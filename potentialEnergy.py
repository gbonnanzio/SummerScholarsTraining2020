#! Program Files (x86)/PythonDownload/python
import matplotlib.pyplot as plt
import numpy as np
import math
import os

def determinePE(xPos,yPos,zPos):
    
    nAtoms = len(xData)
    allR = []
    allPE = []
    totalPE = 0
    totalR = 0

    for i in range(nAtoms):
        for j in range(i+1,nAtoms):
            #only execute if two different atoms
            #positions
            x1 = xPos[i]
            x2 = xPos[j]
            y1 = yPos[i]
            y2 = yPos[j]
            z1 = zPos[i]
            z2 = zPos[j]
 
            #difference in pos
            diffX = x2-x1
            diffY = y2-y1
            diffZ = z2-z1

            #find r
            r = math.sqrt((diffX**2)+(diffY**2)+(diffZ**2))
            totalR = totalR + r

            #constants
            Ar_diam = 142.0 #nm
            #from White 1999
            eps = 1.0 #125.0*(8.6173*10**-5) #eV
            sigma = 0.3345 #nm

            rCorrected = r*sigma
            sigOverR = sigma/rCorrected
            tempPE = 4.0*eps*((sigOverR**12)-(sigOverR**6))
            
            #add to total potential
            totalPE = totalPE + tempPE
        
        avgPE = totalPE/(nAtoms-1)
        allPE.append(avgPE)
        avgR = totalR/(nAtoms-1)
        allR.append(avgR)

    return allPE,allR
    

def main():
    #specify where the text file is located
    filePath = open('/Users/gbonn/Summer_Research_2020/lammps_tut/allCoords.txt',r)
    xData = []
    yData = []
    zData = []
    
    timeStep = 0
    for lineNum, line in enumerate(filePath):
        testLine = lineNum%502
        while(testLine != 0 and testLine!=1)):
            lineList = line.split()
            xData.append(float(lineList[1]))
            yData.append(float(lineList[2]))
            zData.append(float(lineList[3]))
        if(xData != ""):
            determinePE(xData,yData,zData)

            


    


    timeStep = []
    potentialEnergy = []
    #calculate and keep track of potential energy for each time step
    for fileName in textFiles:
        tempFile = filePath + fileName
        tempPE = determinePE(tempFile)
        timeStep.append(float(fileName[:7]))
        potentialEnergy.append(tempPE)
        #stringPE = str(determinePE(tempFile)) 
        #print("At time step " + fileName[:7] + " potential energy equals " + stringPE + " eV.")
    
    #plot potential energy at each time step
    plt.plot(timeStep,potentialEnergy)
    plt.xlabel('Time Step')
    plt.ylabel('Potential Energy (eV)')
    plt.show()

#run functions    
main()


