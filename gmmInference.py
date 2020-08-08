''' Defining GMMM inference '''

def gmmInference(gmm, x_ori):
    Vn =[] # volume
    expn = [] # activity
    nGmm = gmm.k # number of GMM

    for iGmm in range(1,nGmm):
        inverseVariance = np.divide(1,gmm.TrackerS[iGmm,:])    # 1/sigma
        clusterCentroid = gmm.TrackerC[iGmm,:]
        dist = np.multiply((x_ori - clusterCentroid),inverseVariance,(x_ori - clusterCentroid))
        inference, maxDistance = min(exp(-0.5 * dist))
        inference = expn(iGmm)   # gmm inference eqn 12
        gmm.TrackerS[iGmm, maxDistance] = Vn[iGmm]   # volume 
        return Vn, expn
