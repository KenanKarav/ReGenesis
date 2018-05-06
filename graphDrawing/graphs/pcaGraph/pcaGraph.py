class pcaGraph():

    def __init__(self, data):
        self.dimension = data['dimension']
        self.pcaIDs = data['PcaIDs']
        self.xVals = data['x']
        self.yVals = data['y']
        self.zVals = data['z']
        if data['PhenoIDs']:
            self.phenoIDs = data['PhenoIDs']
            self.phenoCol = data['PhenoColumn']
            self.pcaGroups = self.genListGroups(self.phenoCol)
            self.phenoDict = {}
            for i in range(len(self.phenoCol)-1):
                self.phenoDict.update({self.phenoIDs[i]: self.phenoCol[i]})


    # finds and stores each group from a list in a seperate list
    def genListGroups(self, column):
        groupList = []
        for i in range(len(column)):
            data = column[i]
            if data in groupList:
                pass
            else:
                groupList.append(data)
        return groupList

    def findGroupData(self):
        self.pcaGroupDict = {}
        # looping through all the groups
        for numGroups in range(len(self.pcaGroups)):
            tempX = []
            tempY = []
            tempZ = []
            for numLines in range(len(self.pcaIDs)):
                # if the ID from the pca file exists in the phenotype file
                if self.pcaIDs[numLines] in self.phenoDict:
                    # if the key value matches the current group we are searching for..
                    if self.phenoDict.get(self.pcaIDs[numLines]) == self.pcaGroups[numGroups]:
                        tempX.append(self.xVals[numLines])
                        tempY.append(self.yVals[numLines])
                        if self.dimension == 3:
                            tempZ.append(self.zVals[numLines])
            # plotting the graph
            if len(tempX) > 0:
                self.pcaGroupDict.update({
                    self.pcaGroups[numGroups] : {'x': tempX,
                                                 'y': tempY,
                                                 'z': tempZ}
                })
        return self.pcaGroupDict