import random


def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3
    balls of the same color were drawn in the first 3 draws.
    '''
    success = 0

    for x in range(numTrials):
        bag = [0, 0, 0, 0, 1, 1, 1, 1]
        pulled = []

        for i in range(3):
            pulled.append(bag.pop(random.randint(1, len(bag)-1)))

        if all(pulled):
            success += 1

    return success/float(numTrials)
