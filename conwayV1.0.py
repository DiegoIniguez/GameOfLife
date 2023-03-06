"""
conway.py 
A simple Python/matplotlib implementation of Conway's Game of Life.

Edited by 0215625
Diego Alejandro Iñiguez Carvajal
"""

import sys, argparse
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import datetime

#Values
ON = 255
OFF = 0
vals = [ON, OFF]

#Create all figures as arrays
#STILL LIVES
block = np.array([[0,0,0,0],
                 [0,255,255,0],
                 [0,255,255,0],
                 [0,0,0,0]])

beehive = np.array([[0,0,0,0,0,0],
                 [0,0,255,255,0,0],
                 [0,255,0,0,255,0],
                 [0,0,255,255,0,0],
                 [0,0,0,0,0,0]])

loaf = np.array([[0,0,0,0,0,0],
                 [0,0,255,255,0,0],
                 [0,255,0,0,255,0],
                 [0,0,255,0,255,0],
                 [0,0,0,255,0,0],
                 [0,0,0,0,0,0]])

boat = np.array([[0,0,0,0,0],
                 [0,255,255,0,0],
                 [0,255,0,255,0],
                 [0,0,255,0,0],
                 [0,0,0,0,0]])

tub = np.array([[0,0,0,0,0],
                 [0,0,255,0,0],
                 [0,255,0,255,0],
                 [0,0,255,0,0],
                 [0,0,0,0,0]])

#OSCILATORS (REMEMBER TO REMOVE lines & columns)
blinker1 = np.array([[0,0,0],
                     [0,255,0],
                     [0,255,0],
                     [0,255,0],
                     [0,0,0]])

blinker2 = np.array([[0,0,0,0,0],
                    [0,255,255,255,0],
                    [0,0,0,0,0]])

toad1 = np.array([[0,0,0,0,0,0],
                  [0,0,0,255,0,0],
                  [0,255,0,0,255,0],
                  [0,255,0,0,255,0],
                  [0,0,255,0,0,0],
                  [0,0,0,0,0,0]])

toad2 = np.array([[0,0,0,0,0,0],
                  [0,0,255,255,255,0],
                  [0,255,255,255,0,0],
                  [0,0,0,0,0,0]])

beacon1 = np.array([[0,0,0,0,0,0],
                  [0,255,255,0,0,0],
                  [0,255,255,0,0,0],
                  [0,0,0,255,255,0],
                  [0,0,0,255,255,0],
                  [0,0,0,0,0,0]])

beacon2 = np.array([[0,0,0,0,0,0],
                  [0,255,255,0,0,0],
                  [0,255,255,0,0,0],
                  [0,0,0,255,255,0],
                  [0,0,0,255,255,0],
                  [0,0,0,0,0,0]])

#SPACESHIPS
glider1 = np.array([[0,0,0,0,0,0,0],
                  [0,0,0,255,0,0,0],
                  [0,0,0,0,255,0,0],
                  [0,0,255,255,255,0,0],
                  [0,0,0,0,0,0,0]])

glider2 = np.array([[0,0,0,0,0],
                  [0,255,0,255,0],
                  [0,0,255,0,0],
                  [0,0,255,0,0],
                  [0,0,0,0,0]])

glider3 = np.array([[0,0,0,0,0],
                  [0,0,0,255,0],
                  [0,255,0,255,0],
                  [0,0,255,255,0],
                  [0,0,0,0,0]])

glider4 = np.array([[0,0,0,0,0],
                  [0,255,0,0,0],
                  [0,0,255,255,0],
                  [0,255,255,0,0],
                  [0,0,0,0,0]])

lightweightSpaceship = np.array([[0,0,0,0,0,0,0],
                                [0,255,0,0,255,0,0],
                                [0,0,0,0,0,255,0],
                                [0,255,0,0,0,255,0],
                                [0,0,255,255,255,255,0],
                                [0,0,0,0,0,0,0]])

lightweightSpaceship2 = np.array([[0,0,0,0,0,0,0],
                                [0,0,0,255,255,0,0],
                                [0,255,255,0,255,255,0],
                                [0,255,255,255,255,0,0],
                                [0,0,255,255,0,0,0],
                                [0,0,0,0,0,0,0]])

lightweightSpaceship3 = np.array([[0,0,0,0,0,0,0],
                                [0,0,255,255,255,255,0],
                                [0,255,0,0,0,255,0],
                                [0,0,0,0,0,255,0],
                                [0,255,0,0,255,0,0],
                                [0,0,0,0,0,0,0]])

lightweightSpaceship4 = np.array([[0,0,0,0,0,0,0],
                                [0,0,255,255,0,0,0],
                                [0,255,255,255,255,0,0],
                                [0,255,255,0,255,255,0],
                                [0,0,0,255,255,0,0],
                                [0,0,0,0,0,0,0]])

def randomGrid(gridX, gridY):
    """returns a grid of X * Y random values"""
    return np.random.choice(vals, gridX*gridY, p=[0.2, 0.8]).reshape(gridX, gridY)


def update(frameNum, img, grid, gridX, gridY, gens):

    if frameNum >= gens:
        exit()
    newGrid = grid.copy()

    for i in range(gridX):
        for j in range(gridY):
            neighbors = (grid[i, (j-1)%gridY] + grid[i, (j+1)%gridY] +
                         grid[(i-1)%gridX, j] + grid[(i+1)%gridX, j] +
                         grid[(i-1)%gridX, (j-1)%gridY] + grid[(i-1)%gridX, (j+1)%gridY] +
                         grid[(i+1)%gridX, (j-1)%gridY] + grid[(i+1)%gridX, (j+1)%gridY])
            neighbors=neighbors/255
            # apply Conway's rules
            if grid[i, j]  == ON and (neighbors == 2 or neighbors == 3):
                    newGrid[i, j] = ON
            elif grid[i, j]  == OFF and neighbors == 3:
                    newGrid[i, j] = ON
            else:
                 newGrid[i, j] = OFF

    img.set_data(newGrid)
    grid[:] = newGrid[:]

    blockCounter = 0 
    beehiveCounter = 0
    loafCounter = 0
    boatCounter = 0
    tubCounter = 0
    blinkerCounter = 0
    toadCounter = 0
    beaconCounter = 0
    gliderCounter = 0
    spaceshipCounter = 0
    totalItems = 0;

    for i in range(gridX):
        for j in range(gridY):
             if i+4 <=gridX and j+4 <=gridY and (newGrid[i:i+4, j:j+4] == block).all():
                    blockCounter+=1
                    totalItems+=1

             if i+5 <=gridX and j+6 <=gridY and (newGrid[i:i+5, j:j+6] == beehive).all():
                    beehiveCounter+=1
                    totalItems+=1

             if i+5 <=gridX and j+5 <=gridY and (newGrid[i:i+5, j:j+5] == glider3).all():
                    gliderCounter+=1
                    totalItems+=1

             if i+5 <=gridX and j+7 <=gridY and (newGrid[i:i+5, j:j+7] == glider1).all():
                    gliderCounter+=1
                    totalItems+=1

             if i+5 <=gridX and j+5 <=gridY and (newGrid[i:i+5, j:j+5] == glider2).all():
                    gliderCounter+=1
                    totalItems+=1

             if i+5 <=gridX and j+5 <=gridY and (newGrid[i:i+5, j:j+5] == glider4).all():
                    gliderCounter+=1
                    totalItems+=1

             if i+6 <=gridX and j+6 <=gridY and (newGrid[i:i+6, j:j+6] == loaf).all():
                    loafCounter+=1
                    totalItems+=1

             if i+5 <=gridX and j+5 <=gridY and (newGrid[i:i+5, j:j+5] == boat).all():
                    boatCounter+=1
                    totalItems+=1

             if i+5 <=gridX and j+5 <=gridY and (newGrid[i:i+5, j:j+5] == tub).all():
                    tubCounter+=1
                    totalItems+=1

             if i+5 <=gridX and j+3 <=gridY and (newGrid[i:i+5, j:j+3] == blinker1).all():
                    blinkerCounter+=1
                    totalItems+=1

             if i+3 <=gridX and j+5 <=gridY and (newGrid[i:i+3, j:j+5] == blinker2).all():
                    blinkerCounter+=1
                    totalItems+=1

             if i+6 <=gridX and j+6 <=gridY and (newGrid[i:i+6, j:j+6] == toad1).all():
                    toadCounter+=1
                    totalItems+=1

             if i+4 <=gridX and j+6 <=gridY and (newGrid[i:i+4, j:j+6] == toad2).all():
                    toadCounter+=1
                    totalItems+=1

             if i+6 <=gridX and j+6 <=gridY and (newGrid[i:i+6, j:j+6] == beacon1).all():
                    beaconCounter+=1
                    totalItems+=1

             if i+6 <=gridX and j+6 <=gridY and (newGrid[i:i+6, j:j+6] == beacon2).all():
                    beaconCounter+=1
                    totalItems+=1

             if i+6 <=gridX and j+7 <=gridY and (newGrid[i:i+6, j:j+7] == lightweightSpaceship).all():
                    spaceshipCounter+=1
                    totalItems+=1

             if i+6 <=gridX and j+7 <=gridY and (newGrid[i:i+6, j:j+7] == lightweightSpaceship2).all():
                    spaceshipCounter+=1
                    totalItems+=1

             if i+6 <=gridX and j+7 <=gridY and(newGrid[i:i+6, j:j+7] == lightweightSpaceship3).all():
                    spaceshipCounter+=1
                    totalItems+=1

             if i+6 <=gridX and j+7 <=gridY and (newGrid[i:i+6, j:j+7] == lightweightSpaceship4).all():
                    spaceshipCounter+=1
                    totalItems+=1

    print("Iteracion", frameNum, "Total agents:", totalItems)

    outputinfo(blockCounter, beehiveCounter, loafCounter, boatCounter, tubCounter, blinkerCounter, toadCounter, beaconCounter, gliderCounter, spaceshipCounter, gridX, gridY, frameNum)
  
    return img, 

def outputinfo(blockCounter, beehiveCounter, loafCounter, boatCounter, tubCounter, blinkerCounter, toadCounter, beaconCounter, gliderCounter,spaceshipCounter, gridX, gridY, frameNum):
     totalFigures = blockCounter + beehiveCounter + loafCounter + boatCounter + tubCounter + blinkerCounter + toadCounter + beaconCounter + gliderCounter + spaceshipCounter
     if totalFigures > 0:
       blockPercentage = (100 * blockCounter) / totalFigures
       beehivePercentage = (100 * beehiveCounter) / totalFigures
       loafPercentage = (100 * loafCounter) / totalFigures
       boatPercentage = (100 * boatCounter) / totalFigures
       tubPercentage = (100 * tubCounter) / totalFigures
       blinkerPercentage = (100 * blinkerCounter) / totalFigures
       toadPercentage = (100 * toadCounter) / totalFigures
       beaconPercentage = (100 * beaconCounter) / totalFigures
       gliderPercentage = (100 * gliderCounter) / totalFigures
       spaceshipPercentage = (100 * spaceshipCounter) / totalFigures

     else:
       blockPercentage = 0
       beehivePercentage = 0
       loafPercentage = 0
       boatPercentage = 0
       tubPercentage = 0
       blinkerPercentage = 0
       toadPercentage = 0
       beaconPercentage = 0
       gliderPercentage = 0
       spaceshipPercentage = 0
           
     today = datetime.datetime.now()

     with open("output.txt", "a") as file:         
          file.write("Simulation: at "+ str(today) +"\n")
          file.write("Universe Size  " + str(gridX) + "x" + str(gridY)+ "\n")
          file.write("Iteration:     " + str(frameNum+1) + "\n")
          file.write("      Count       Percentage   " + "\n")
          file.write("Blocks:        " + str(blockCounter) + "   " + str(blockPercentage)+"%" + "\n")
          file.write("Beehives:      " + str(beehiveCounter) + "   " + str(beehivePercentage)+"%" +"\n")
          file.write("Loafs:         " + str(loafCounter) + "   " + str(loafPercentage)+"%"+"\n")
          file.write("Boats:         " + str(boatCounter) + "   " + str(boatPercentage)+"%"+"\n")
          file.write("Tubs:          " + str(tubCounter) + "    " +str(tubPercentage)+"%"+"\n")
          file.write("Blinkers:      " + str(blinkerCounter) + "   " +str(blinkerPercentage)+"%"+"\n")
          file.write("Toads:         " + str(toadCounter) + "    " +str(toadPercentage)+"%"+"\n")
          file.write("Beacons:       " + str(beaconCounter) + "    " +str(beaconPercentage)+"%"+"\n")
          file.write("Gliders:       " + str(gliderCounter) + "    " +str(gliderPercentage)+"%"+"\n")
          file.write("Spaceships: " + str(spaceshipCounter) + "    " + str(spaceshipPercentage) +"%"+"\n")
          file.write("Total Configurations: " + str(totalFigures) + "\n")
          file.write(""+ "\n")
          

def addGlider(i, j, grid):
    """adds a glider with top left cell at (i, j)"""
    glider = np.array([[0,    0, 255], 
                       [255,  0, 255], 
                       [0,  255, 255]])
    
    glider1 = np.array([[0,0,0,0,0,0,0],
                        [0,0,0,255,0,0,0],
                        [0,0,0,0,255,0,0],
                        [0,0,255,255,255,0,0],
                        [0,0,0,0,0,0,0]])
    
    grid[i:i+5, j:j+7] = glider1

def addCell(i,j, grid):
     cell = np.array([255])

     grid[i, j] = cell

def main():
    # Command line args are in sys.argv[1], sys.argv[2] ..
    # sys.argv[0] is the script name itself and can be ignored
    # parse arguments
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life system.py.")

    # TODO: add arguments
    
    updateInterval = 50

    grid = np.array([])

    with open("input.txt", "r") as File:
        array = []
        width = File.readline()
        width = int(width)
        gens = int(File.readline().strip())
        lines=File.read().splitlines()

        for line in lines:
            positions = line.split()
            for position in positions:
                 thisposition=position.split()
                 array.append(thisposition)
    Xalive=[]
    Yalive=[]


    ##grid = randomGrid(gridX, gridY)
    grid = np.zeros(width*width).reshape(width, width)
    
    for i in range(0, len(array)):
          thisnumber=int(array[i][0])
          if i%2 == 0:
               Xalive.append(int(array[i][0])) 
          else:
               Yalive.append(int(array[i][0]))
    

    for i, j in zip(Xalive,Yalive):
        addCell(i, j, grid)

    addGlider(4,4,grid)
    addGlider(14,14,grid)

    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, width, width, gens),
                                  frames = gens,
                                  interval=updateInterval,
                                  save_count=50, repeat=False)

    plt.show()


# call main
if __name__ == '__main__':
    main()
