def gmmClusterAvailability(gmm, gmmWinner):
    nGmm = gmm.k

    sigmaWinner = sqrt(gmm.TrackerS(gmmWinner, mslice[:]))
    miu_plus_sigma_winner = gmm.TrackerC(gmmWinner, mslice[:]) + sigmaWinner
    miu_mins_sigma_winner = gmm.TrackerC(gmmWinner, mslice[:]) - sigmaWinner

    totalProportion = length(gmm.TrackerC(gmmWinner, mslice[:])) * (gmm.k - 1)
    numInside = 0

    # count how many centers inside the winning cluster
    for iGmm in mslice[1:nGmm]:
        if iGmm != gmmWinner:
            center = gmm.TrackerC(iGmm, mslice[:])
            lessThanSigma = center < miu_plus_sigma_winner
            moreThanSigma = center > miu_mins_sigma_winner
            insideWinner = lessThanSigma *elmul* moreThanSigma
            numInside = numInside + sum(insideWinner)
        end
    end

    numOutside = abs(totalProportion - numInside)
    rho = numOutside / totalProportion# eqn 14
    if rho == 0:
        rho = 0.1    # minimum vigilance parameter
