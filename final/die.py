import random
import pylab


# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std


# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]

    def roll(self):
        return random.choice(self.possibleVals)


# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values, numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if title is not None:
        pylab.title(title)
    pylab.show()


# Implement this -- Coding Part 2 of 2


def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated to 3 decimal places
    """

    longest_runs = []

    for x in range(numTrials):

        rolls = [die.roll() for x in range(numRolls)]

        run = 0
        longest = 0

        for i in range(len(rolls)):
            if i == 0:
                run += 1
                longest += 1
            else:
                if rolls[i] == rolls[i-1]:
                    run += 1
                    if run > longest:
                        longest = run
                else:
                    run = 1

        longest_runs.append(longest)

    makeHistogram(longest_runs, 10, 'Longest Run', 'Frequency', 'Frequency of Longest Consecutive Dice Rolls')

    return sum(longest_runs)/len(longest_runs)


# One test case
print(getAverage(Die([1, 2, 3, 4, 5, 6, 6, 6, 7]), 1, 1000))
