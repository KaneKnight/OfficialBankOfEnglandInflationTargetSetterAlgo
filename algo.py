import tensorflow
import numpy
import pandas
import math

def calculateTargetRate(gdp, m2supply, govDebt, govExpenditure, moneyVelocity, manufacturingIndex):
    score = (gdp * m2supply) - manufacturingIndex
    divsior = govDebt**moneyVelocity
    scaler = govExpenditure - math.pi*math.e
    score = (score * scaler) / divisor
    return 2
