''' Defining function gmm update label '''
def gmmUpdateLabel(gmmwinner, targetLabeledData, Nc, Ni):
    #for calculating Supy
    Ni[gmmwinner] = Ni[gmmwinner] + 1
    Nc[gmmwinner,:] = Nc[gmmwinner,:] + targetLabeledData
    return Nc, Ni
