
# CC BY-NC-SA 4.0 License
# Copyright (c) 2019 Mahardhika Pratama Andri Ashfahani Mohamad Abdul Hady

''' Defining function AGMMID in Python '''

def AGMMID(gmm, input, nInput, NetworkBias2, EvaluationWindow, nLabeledData, k, mode):
    # for infinite delay scenario
    # GMM inference #1
    gmm.counter = gmm.counter + 1
    Vn, expn = gmmInference(gmm, input)

    # update gmm weight
    gmm = gmmUpdateWeight(gmm, Vn, expn, nInput)
    ignore_var3, gmmwinner = max(gmm.weight)
    gmm.gmmwinner = gmmwinner

    # examine space availability
    if gmm.k > 1:
        gmm.rho = gmmClusterAvailability(gmm, gmmwinner)    # evaluate the cluster eqn 14
    elif gmm.k == 1:
        gmm.rho = 0.1
    

    # cluster growing or update
    kappa = 1.2 * exp(-NetworkBias2) + 0.8
    gmm.Threshold1 = exp(-nInput * kappa / ((4 - 2 * exp(-nInput / 20)))) # right hand side term of eqn 12
    condition1 = expn(gmmwinner) < gmm.Threshold1 # indicate uncovered input region eqn 12
    condition2 = Vn(gmmwinner) >= gmm.rho * (sum(Vn) - Vn(gmmwinner)) # vigilance test eqn 13
    condition3 = gmm.counter > 10 # wait until stable
    condition4 = gmm.counter != EvaluationWindow # this is for deleting a cluster, no creation of cluster in this time
    if condition1 and condition2 and condition3 and condition4 and mode(5) == 1 and k >= nLabeledData:
        # create clusters
        grow_cluster = 1
        gmm = gmmCreateCluster(gmm, input, nInput)
    else:
        # update the winning clusters
        grow_cluster = 0
        gmm = gmmUpdateCluster(gmm, input, gmmwinner)
    

    # delete cluster
    if ((gmm.counter)%(EvaluationWindow) == 0 and gmm.k > gmm.nClass and grow_cluster == 0):
        gmm = gmmDeleteCluster(gmm)
        ignore_var4, gmmwinner = max(gmm.weight)
        gmm.gmmwinner = gmmwinner
    return gmm
