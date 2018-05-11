import  numpy as np
import random

class pcaGraph():

    def __init__(self, data):
        self.pcaFileData={}
        self.groupColours = {}

        self.dimension = data['dimension']
        self.pcaIDs = data['PcaIDs']
        self.xVals = data['x']
        self.yVals = data['y']
        self.zVals = data['z']

        self.pcaFileData.update({
            'dimension' : self.dimension,
            'PcaIDs' : self.pcaIDs,
            'x' : self.xVals,
            'y' : self.yVals,
            'z' : self.zVals
        })

        self.hasPheno = False
        if 'PhenoIDs' in data:
            self.hasPheno = True
            self.phenoIDs = data['PhenoIDs']
            self.phenoCol = data['PhenoColumn']

            self.pcaFileData.update({
                'PhenoIDs': self.phenoIDs,
                'PhenoColumn': self.phenoCol
            })

            self.pcaGroups = self.genListGroups(self.phenoCol)
            self.pcaSelectedGroups = []
            print("MADE GROUPS")
            self.phenoDict = {}

            for i in range(len(self.phenoCol)):
                self.phenoDict.update({self.phenoIDs[i]: self.phenoCol[i]})

            #checking if colours have been defined
            self.hasColours = False
            if 'Colours' in data:
                self.hasColours = True
                self.groupColours = data['Colours']
            else:
                print('no defined colours')

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

    def getGroups(self):
        return self.pcaSelectedGroups

    def getColours(self):
        return self.groupColours

    def setColours(self, colourDict):
        self.groupColours = colourDict
        self.pcaFileData.update({
            'Colours': self.groupColours
        })

    #returns the pca data received from the pcaCreator class
    def getSaveFileData(self):
        return self.pcaFileData

    def findPcaData(self, isNew):
        self.pcaDataDict = {}
        if self.hasPheno:
            # looping through all the groups
            self.pcaSelectedGroups = []
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
                    self.pcaDataDict.update({
                        self.pcaGroups[numGroups] : {'x': tempX,
                                                     'y': tempY,
                                                     'z': tempZ}
                    })
                    #adding to list of selected groups
                    self.pcaSelectedGroups.append(self.pcaGroups[numGroups])

                    #assigning a random colour to each group
                    if isNew and not self.hasColours:
                        print("NEW AND HAS NO DEFINED COLOURS")
                        #rand = np.random.rand(1, 3)
                        #print(type(rand))
                        rand = []
                        rand.append(random.random())
                        rand.append(random.random())
                        rand.append(random.random())
                        print(rand)
                        print(type(rand))
                        self.groupColours.update({
                            self.pcaGroups[numGroups]: rand
                        })

                        self.pcaFileData.update({
                            'Colours': self.groupColours
                        })


        else:
            self.pcaDataDict.update({
                "ungrouped" :  {'x': self.xVals,
                                'y': self.yVals,
                                'z': self.zVals}
            })
        print(self.pcaFileData)
        return self.pcaDataDict