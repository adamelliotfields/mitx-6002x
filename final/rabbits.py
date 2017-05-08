import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30


def rabbitGrowth():
    """
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up,
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    prob_new_rabbit = 1 - CURRENTRABBITPOP/MAXRABBITPOP
    num_new_rabbits = 0

    for i_rabbit in range(CURRENTRABBITPOP):
        if random.random() < prob_new_rabbit:
            num_new_rabbits += 1

    CURRENTRABBITPOP += num_new_rabbits
    CURRENTRABBITPOP = min(CURRENTRABBITPOP, MAXRABBITPOP)


def foxGrowth():
    """
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    num_new_foxes = 0
    for i_fox in range(CURRENTFOXPOP):
        if CURRENTRABBITPOP <= 10:
            eat_rabbit = False
        else:
            eat_rabbit = random.random() < CURRENTRABBITPOP/MAXRABBITPOP

        if eat_rabbit:
            CURRENTRABBITPOP -= 1
            if random.random() < 1/3:
                num_new_foxes += 1
        else:
            if random.random() < 0.1 and CURRENTFOXPOP > 10:
                num_new_foxes -= 1

    CURRENTFOXPOP += num_new_foxes


def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    rabbit_populations = []
    fox_populations = []

    for iStep in range(numSteps):
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)
        rabbitGrowth()
        foxGrowth()

    return (rabbit_populations, fox_populations)
