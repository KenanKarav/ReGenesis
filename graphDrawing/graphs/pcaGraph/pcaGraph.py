class pcaGraph():

    def __init__(self, data):
        self.pcaIDs = data['PcaIDs']
        self.xVals = data['x']
        self.yVals = data['y']
        self.zVals = data['z']
        if data['PhenoIDs']:
            self.phenoIDs = data['PhenoIDs']
            self.phenoCol = data['PhenoColumn']
            self.pcaGroups = self.genListGroups(self.phenoCol)
            self.phenoDict = {}
            for i in range(len(self.phenoCol)):
                self.phenoDict.update({self.phenoIDs[i]: self.phenoCol[i]})

    def __init__(self):
        self.pcaIDs = []
        self.xVals = []
        self.yVals = []
        self.zVals = []
        self.phenoCol = []
        self.pcaGroups = []
        self.phenoDict = {}

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
                        tempZ.append(self.zVals[numLines])
            # plotting the graph
            if len(tempX) > 0:
                self.pcaGroupDict.update({
                    self.pcaGroups[numGroups] : {'x': tempX,
                                                 'y': tempY,
                                                 'z': tempZ}
                })