''' Defining function gmm delete cluster '''

def gmmDeleteCluster(gmm):
    accu_e = np.divide(gmm.accu, gmm.counter_accu)
    delete_list = find(accu_e < abs(mean(accu_e) - 0.5 * std(accu_e)))
    ndelete_list = numel(delete_list)
    if gmm.k - ndelete_list < gmm.nClass:
        nClust = gmm.k - ndelete_list
        nKeep = gmm.nClass - nClust
        nNewDeleteList = ndelete_list - nKeep
        delete_list = delete_list[1:nNewDeleteList]
        ndelete_list = numel(delete_list)
    
    if isempty(delete_list) == 0:
        gmm.k = gmm.k - ndelete_list
        gmm.weight[delete_list] = []
        gmm.TrackerC[delete_list,:] = []
        gmm.TrackerS[delete_list,:] = []
        gmm.Np[delete_list] = []
        gmm.Ni[delete_list] = []
        gmm.Nc[delete_list,:] = []
        gmm.accu[delete_list] = []
        gmm.counter_accu[delete_list] = []
        accu_e[delete_list] = []

        if sum(gmm.weight) == 0:
            max(accu_e)
            gmm.weight[max_index] = gmm.weight[max_index] + 1
      
        gmm.weight = np.divide(gmm.weight,sum(gmm.weight))
        return gmm
