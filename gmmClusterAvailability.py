''' Defining function cluster availability '''

import math
import numpy as np
def gmmClusterAvailability(gmm, gmmWinner):
    nGmm = gmm.k

    sigmaWinner = math.sqrt(gmm.TrackerS[gmmWinner,:])   # Assuming the matrix is in the form of a numpy array
    miu_plus_sigma_winner = gmm.TrackerC[gmmWinner,:] + sigmaWinner  # Assuming the matrix is in the form of a numpy array
    miu_mins_sigma_winner = gmm.TrackerC[gmmWinner, :] - sigmaWinner # Assuming the matrix is in the form of a numpy array

    totalProportion = length(gmm.TrackerC[gmmWinner,:]) * (gmm.k - 1)
    numInside = 0

    # count how many centers inside the winning cluster
    for iGmm in range(1,nGMM):
        if iGmm != gmmWinner:
            center = gmm.TrackerC[iGmm,:]
            lessThanSigma = center < miu_plus_sigma_winner
            moreThanSigma = center > miu_mins_sigma_winner
            insideWinner = np.multiply(lessThanSigma,moreThanSigma)
            numInside = numInside + sum(insideWinner)
    numOutside = abs(totalProportion - numInside)
    rho = numOutside / totalProportion  # eqn 14
    if rho == 0:
        rho = 0.1    # minimum vigilance parameter
    return rho
