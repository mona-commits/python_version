 ''' Defining function gmm update weight '''
 
 def  ''' Defining function gmm update weight '''
 
 def gmmUpdateWeight(gmm,Vj,expn): # original one has ~ also in inputs

    gmm.accu = gmm.accu + expn# sum of activity eqn 17
    gmm.counter_accu = gmm.counter_accu + 1# lifespan eqn 17
    denumerator = (2 * pi) ** (-1 / 2) * np.power(Vj,(-1 / 2))
    pxn = np.multiply(denumerator, expn) # p(x|n)
    pn = np.divide(gmm.Np,sum(gmm.Np)) # p(n)
    pxnpn = np.multiply(pxn,pn) # p(x|n)p(n)
    if sum(pxnpn) == 0:
        # for stability purposes
        max(expn)
        pxnpn[max_expj_index] = pxnpn[max_expj_index] + 1
    gmm.weight = pxnpn / sum(pxnpn) # omega eqn 16
    return gmmgmm,Vj,expn): # original one has ~ also in inputs

    gmm.accu = gmm.accu + expn# sum of activity eqn 17
    gmm.counter_accu = gmm.counter_accu + 1# lifespan eqn 17
    denumerator = (2 * pi) ** (-1 / 2) * np.power(Vj,(-1 / 2))
    pxn = np.multiply(denumerator, expn) # p(x|n)
    pn = np.divide(gmm.Np,sum(gmm.Np)) # p(n)
    pxnpn = np.multiply(pxn,pn) # p(x|n)p(n)
    if sum(pxnpn) == 0:
        # for stability purposes
        max(expn)
        pxnpn[max_expj_index] = pxnpn[max_expj_index] + 1
    gmm.weight = pxnpn / sum(pxnpn) # omega eqn 16
    return gmm
