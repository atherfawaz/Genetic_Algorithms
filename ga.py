# GENETIC ALGORITHMS
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy

# GLOBALS
FILE = 'imageB.bmp'
IMAGE = mpimg.imread(FILE)
ROWS = IMAGE.shape[0]
COLUMNS = IMAGE.shape[1]
DEPTH = IMAGE.shape[2]
DIFFERENCE_MATRIX = numpy.zeros((ROWS, COLUMNS, DEPTH))
GENETIC_IMAGE = numpy.random.randint(0, 255, size=(ROWS, COLUMNS, DEPTH))
GENERATIONS = 1000
UNFIT = []
THRESHOLD = 0  # set to 0 for no mismatch between images
# GLOBALS


# Point class to keep track of the coordinates of the unfit population
class Coordinate:
    x = None
    y = None
    z = None
    difference = None

    def __init__(self, x, y, z, difference):
        self.x = x
        self.y = y
        self.z = z
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

# O(n^3)


def fitness_function():
    global UNFIT
    global DIFFERENCE_MATRIX
    UNFIT = []
    for i in range(0, ROWS):
        for j in range(0, COLUMNS):
            for k in range(0, DEPTH):
                difference = IMAGE[i][j][k] - GENETIC_IMAGE[i][j][k]
                DIFFERENCE_MATRIX[i][j][k] = difference
                if (abs(difference) > THRESHOLD):
                    # perhaps keepting the unfit population
                    # in an array can help us
                    UNFIT.append(Coordinate(i, j, k, difference))


def cross_over():
    global UNFIT
    global GENETIC_IMAGE
    # select only 20% good boys
    select = int(0.8 * UNFIT.__len__)
    for i in range(0, select):
        specimen_a = random.randint(0, select)
        specimen_b = random.randint(0, select)
        # swap genes (depths) 0 and 1 with 2 and 3
        # checked tuple swap but apparently this is a syntax error
        # didn't look further
        GENETIC_IMAGE[UNFIT[specimen_a].x][UNFIT[specimen_a].y][0], GENETIC_IMAGE[UNFIT[specimen_a].x][UNFIT[specimen_a].y][1] = GENETIC_IMAGE[UNFIT[specimen_b].x][UNFIT[specimen_b].y][2]), GENETIC_IMAGE[UNFIT[specimen_b].x][UNFIT[specimen_b].y][3])

def mutate():
    dummy = None

if __name__ == "__main__":
    # display image
    # plt.show()
    current_generation=0
    # call an O(n^3) loop once to set up the differences
    fitness_function()
    while (current_generation < GENERATIONS):
        # gauge current picture
        optimized_fitness()
        # selection
        UNFIT.sort(key=lambda Coordinate: Coordinate.difference, reverse = True)
        # cross over
        cross_over()
        # mutation
        mutate()
        #increment generation
        current_generation += 1
