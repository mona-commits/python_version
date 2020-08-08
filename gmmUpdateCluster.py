''' Defining function update cluster '''

def gmmUpdateCluster(gmm, x_ori, gmmwinner):
    gmm.TrackerC[gmmwinner,:] = gmm.TrackerC[gmmwinner,:] + (x_ori - gmm.TrackerC[gmmwinner,:]) / (gmm.Np[gmmwinner] + 1)# update the centroid of a cluster eqn 15
    gmm.TrackerS[gmmwinner,:] = gmm.TrackerS[gmmwinner,:] + (np.power(x_ori - gmm.TrackerC[gmmwinner,:]),2 - gmm.TrackerS[gmmwinner,:]) / (gmm.Np[gmmwinner] + 1)# update the variance of a cluster eqn 15
    gmm.Np[gmmwinner] = gmm.Np[gmmwinner] + 1# sup of a cluster eqn 15
    return gmm
