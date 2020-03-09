# GENETIC ALGORITHMS
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy
from random import seed
from random import randint, random

# GLOBALS
FILE = 'image.png'
IMAGE = mpimg.imread(FILE)
ROWS = IMAGE.shape[0]
COLUMNS = IMAGE.shape[1]
DEPTH = 1
POPULATION = []
POPULATION_SIZE = 100
GENETIC_IMAGE = numpy.random.randint(0, 255, size=(ROWS, COLUMNS, DEPTH))
GENERATIONS = 1000
UNFIT = []
THRESHOLD = 10  # set to 0 for no mismatch between images
seed(1)
# GLOBALS


# Point class to keep track of the coordinates of the unfit population
class Population_Class:
    array = None
    difference = None

    def __init__(self, difference):
        self.array = numpy.random.randint(0, 255, size=(ROWS, COLUMNS, DEPTH))
        self.difference = difference

# Operates on a list
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
    global_difference = 0
    for var in POPULATION:
        global_difference = 0
        for i in range(0, ROWS):
            for j in range(0, COLUMNS):
                difference = var.array[i][j][0] - IMAGE[i][j][0]
                global_difference += abs(difference)
        var.difference = global_difference


def cross_over():
    global UNFIT
    global GENETIC_IMAGE
    # select only 20% good boys
    select = int((0.8 * len(UNFIT)))
    for i in range(0, select):
        specimen_a = randint(0, select)
        specimen_b = randint(0, select)
        # swap genes (depths) 0 and 1 with 2 and 3
        # tuple swapping
        GENETIC_IMAGE[UNFIT[specimen_a].x][UNFIT[specimen_a].y][0], GENETIC_IMAGE[UNFIT[specimen_a].x][UNFIT[specimen_a]
                                                                                                       .y][1] = GENETIC_IMAGE[UNFIT[specimen_b].x][UNFIT[specimen_b].y][2], GENETIC_IMAGE[UNFIT[specimen_b].x][UNFIT[specimen_b].y][3]

def mutate():
    dummy = None

def generate_population():
    global POPULATION
    seed(1)
    for i in range(0, POPULATION_SIZE):
        POPULATION.append(Population_Class(None))

if __name__ == "__main__":
    generate_population()
    # call an O(n^3) loop once to set up the differences
    # fitness_function()
    current_generation = 0
    while (current_generation < GENERATIONS):
        # gauge current picture
        fitness_function()
        # selection
        POPULATION.sort(key=lambda Population_Class: Population_Class.difference, reverse=True)
        # cross over
        cross_over()
        # mutation
        mutate()
        # increment generation
        current_generation += 1
        print('Generation: ', current_generation)
        #imgplot = plt.imshow(GENETIC_IMAGE)
        #plt.show() 
