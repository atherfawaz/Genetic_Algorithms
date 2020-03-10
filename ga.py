# GENETIC ALGORITHMS
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import time
import copy
from random import seed
from random import randint, random
import random

# GLOBALS
FILE = 'new.png'
IMAGE = mpimg.imread(FILE)
#IMAGE = cv2.resize(IMAGE,(20,28))
ROWS = IMAGE.shape[0]
COLUMNS = IMAGE.shape[1]
#DEPTH = 1
POPULATION = []
NEW_POPULATION = []
POPULATION_SIZE = 100
GENETIC_IMAGE = np.random.randint(0, 255, size=(ROWS, COLUMNS))
GENERATIONS = 1000
UNFIT = []
THRESHOLD = 10  # set to 0 for no mismatch between images
seed(1)
# GLOBALS


class Population_Class:
    array = None
    difference = None

    def __init__(self, difference):
        self.array = np.random.randint(0, 255, size=(ROWS, COLUMNS))
        self.difference = difference

def optimized_fitness():
    global UNFIT
    for var in UNFIT:
        difference = IMAGE[var.x][var.y][var.z] - \
            GENETIC_IMAGE[var.x][var.y][var.z]
        var.difference = difference  # debtable if we should update the array here
        if (abs(difference) < THRESHOLD):
            # remove this element if it is at its correct value
            UNFIT.remove(var)

def fitness_function():
    for var in POPULATION:
        var.difference = np.sum(np.abs(np.subtract(var.array, IMAGE)))

def cross_over(pic1, pic2):
    child = Population_Class(None)    
    child.array[0:int(ROWS/2)][0:int(COLUMNS)] = pic1.array[int(ROWS/2):ROWS][0:int(COLUMNS)]
    child.array[int(ROWS/2) : ROWS][0:int(COLUMNS)] = pic2.array[0:int(ROWS/2)][0:int(COLUMNS)]
    return child

def mutate(pic):
    global ROWS 
    global COLUMNS
    for _ in range(0, 50):
        indexR = np.random.randint(0,ROWS)
        indexC = np.random.randint(0,COLUMNS)
        value = np.random.uniform(0, 255, 1)
        pic.array[indexR][indexC] = value
    return pic

def generate_population():
    global POPULATION
    for _ in range(0, POPULATION_SIZE):
        POPULATION.append(Population_Class(None))


if __name__ == "__main__":
    generate_population()
    current_generation = 1
    while (current_generation <= GENERATIONS):
        NEW_POPULATION = []
        # gauge current picture
        fitness_function()

        POPULATION.sort(key=lambda Population_Class: Population_Class.difference, reverse=False)

        if (POPULATION[0].difference <= THRESHOLD):
            GENETIC_IMAGE = POPULATION[0].array
            break
        
        #GENETIC_IMAGE = POPULATION[0].array

        # print cost for this generation
        cost = POPULATION[0].difference
        if (current_generation % 50 == 0):
            print('Generation: ', current_generation)
            print("Cost: ", POPULATION[0].difference)
            #imgplot = plt.imshow(GENETIC_IMAGE)
            #plt.show()
            #time.sleep(1)
            #plt.close()

        # selection; selecting top 20%
        for i in range(0, round((20/100) * POPULATION_SIZE)):
            NEW_POPULATION.append(POPULATION[i])

        # cross over; select 2 pictures from 60% of the fittest ones at random, then apply crossover to them
        for i in range(0, round((60/100) * POPULATION_SIZE)):
            pic1 = random.choice(POPULATION[: int(POPULATION_SIZE/2)])
            pic2 = random.choice(POPULATION[: int(POPULATION_SIZE/2)])
            NEW_POPULATION.append(cross_over(pic1, pic2))

#        for i in range(0, round((60/100) * POPULATION_SIZE)):
#            NEW_POPULATION[counter] = POPULATION[counter]

        # mutation; select 1 picture from 50% of the fittest one at random, then mutate some of its pixels
        for i in range(0, round((20/100) * POPULATION_SIZE)):
            NEW_POPULATION.append(mutate(random.choice(POPULATION[: int(POPULATION_SIZE/2)])))

        # increment generation
        POPULATION = copy.deepcopy(NEW_POPULATION)
        current_generation += 1
