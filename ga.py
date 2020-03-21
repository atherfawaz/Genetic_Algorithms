# GENETIC ALGORITHMS
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import time
import copy
import cv2
import numpy
from random import seed
from random import randint, random
import random
from PIL import Image
img = Image.open('imageB.bmp').convert('LA')
img.save('greyscale.png')

# GLOBALS
FILE = 'imageB.bmp'
IMAGE = mpimg.imread(FILE)
plt.imshow(IMAGE)
IMAGE = cv2.resize(IMAGE,(20,28))
# plt.imsave('original_compressed.png', IMAGE)
ROWS = IMAGE.shape[0]
COLUMNS = IMAGE.shape[1]
DEPTH = IMAGE.shape[2]
POPULATION = []
NEW_POPULATION = []
POPULATION_SIZE = 100
GENETIC_IMAGE = np.random.randint(0, 255, size=(ROWS, COLUMNS, DEPTH))
GENERATIONS = 20000
UNFIT = []
THRESHOLD = 10  # set to 0 for no mismatch between images
seed(1)
# GLOBALS


class Population_Class:
    array = None
    difference = None

    def __init__(self, difference):
        self.array = np.random.randint(0, 255, size=(ROWS, COLUMNS, DEPTH))
        self.difference = difference

def fitness_function():
    for var in POPULATION:
        var.difference = np.sum(np.abs(np.subtract(var.array, IMAGE))).astype(int)

def cross_over(pic1, pic2):
    child = Population_Class(None)
    child.array[0:int(ROWS/2)][:][:] = pic1.array[0:int(ROWS/2)][:][:]
    child.array[int(ROWS/2) : ROWS][:][:] = pic2.array[int(ROWS/2):ROWS][:][:]
    return child

def mutate(pic):
    global ROWS 
    global COLUMNS
    for _ in range(0, 1):
        indexR = np.random.randint(0,ROWS)
        indexC = np.random.randint(0,COLUMNS)
        value = np.random.uniform(0, 255, 1)
        pic.array[indexR][indexC][:] = value
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
        
        GENETIC_IMAGE = POPULATION[0].array

        # print cost for this generation
        cost = POPULATION[0].difference
        if (current_generation % 100 == 0):
            print('Generation: ', current_generation)
            print("Cost: ", POPULATION[0].difference)
            # GENETIC_IMAGE = np.reshape(GENETIC_IMAGE, IMAGE.shape)
            plt.imsave('temp.bmp', GENETIC_IMAGE.astype(np.uint8))

        # selection; selecting top 20%
        for i in range(0, round((10/100) * POPULATION_SIZE)):
            NEW_POPULATION.append(POPULATION[i])

        # cross over; select 2 pictures from 50% of the fittest ones at random, 
        # then apply crossover to them, store both parents and children in new pop
        for i in range(0, round((30/100) * POPULATION_SIZE)):
            pic1 = random.choice(POPULATION[: int(POPULATION_SIZE/2)])
            pic2 = random.choice(POPULATION[: int(POPULATION_SIZE/2)])
            NEW_POPULATION.append(pic1)
            NEW_POPULATION.append(pic2)
            NEW_POPULATION.append(cross_over(pic1, pic2))

        # mutation; select 1 picture from all at random, then mutate some of its pixels
        for i in range(0, round((10/100) * POPULATION_SIZE)):
            NEW_POPULATION.append(mutate(random.choice(POPULATION[:])))

        # increment generation
        POPULATION = NEW_POPULATION
        current_generation += 1

    imgplot = plt.imshow(GENETIC_IMAGE)
    plt.imsave('foo.png', GENETIC_IMAGE)