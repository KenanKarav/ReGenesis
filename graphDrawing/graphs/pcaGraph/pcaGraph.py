import  numpy as np
import random

class pcaGraph():

    def __init__(self, data):
        self.pcaFileData={}
        self.graphType = 'pca'
        self.groupColours = {}
        self.groupShapes = {}
        self.pcaSelectedGroups = []

        self.dimension = data['dimension']
        self.pcaIDs = data['PcaIDs']
        self.xVals = data['x']
        self.yVals = data['y']
        self.zVals = data['z']

        #updating data dictionary used for saving and loading
        self.pcaFileData.update({
            'dimension' : self.dimension,
            'PcaIDs' : self.pcaIDs,
            'x' : self.xVals,
            'y' : self.yVals,
            'z' : self.zVals
        })

        self.hasPheno = False
        if 'PhenoIDs' in data:
            # setting phenotype-related data
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

        #checking if shapes have been defined
        self.hasShapes = False
        if 'Shapes' in data:
            self.hasShapes = True
            self.groupShapes = data['Shapes']
        else:
            print('no defined shapes')



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

    def getShapes(self):
        return self.groupShapes

    def setColours(self, colourDict):
        self.groupColours = colourDict
        self.pcaFileData.update({
            'Colours': self.groupColours
        })

    def setShapes(self, shapeDict):
        self.groupShapes = shapeDict
        self.pcaFileData.update({
            'Shapes': self.groupShapes
        })

    def getGraphType(self):
        return self.graphType

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


                    if isNew:
                        # assigning a random colour to each group
                        if not self.hasColours:
                            print("NEW AND HAS NO DEFINED COLOURS")
                            rand = []
                            rand.append(random.random())
                            rand.append(random.random())
                            rand.append(random.random())
                            self.groupColours.update({
                                self.pcaGroups[numGroups]: rand
                            })

                            self.pcaFileData.update({
                                'Colours': self.groupColours
                            })

                        #assigning a random shape to each group
                        if not self.hasShapes:
                            print("NEW AND HAS NO DEFINED SHAPES")
                            # point, circle, square, triangle, diamond, cross, plus
                            availableShapes = ['.', 'o', 's', '^', 'D', 'x', '+']
                            rand = random.randint(0,6)
                            self.groupShapes.update({
                                self.pcaGroups[numGroups]: availableShapes[rand]
                            })

                            self.pcaFileData.update({
                                'Shapes': self.groupShapes
                            })

        else:
            # NO PHENOTYPE FILE
            self.pcaDataDict.update({
                "ungrouped" :  {'x': self.xVals,
                                'y': self.yVals,
                                'z': self.zVals}
            })
            self.pcaSelectedGroups = ['ungrouped']

            # assigning a random colour
            if isNew:

                if not self.hasColours:
                    print("NEW AND HAS NO DEFINED COLOUR")
                    rand = []
                    rand.append(random.random())
                    rand.append(random.random())
                    rand.append(random.random())
                    self.groupColours.update({
                        'ungrouped': rand
                    })

                    self.pcaFileData.update({
                        'Colours': self.groupColours
                    })

                if not self.hasShapes:
                    print("NEW AND HAS NO DEFINED SHAPES")
                    # point, circle, square, triangle, diamond, cross, plus
                    availableShapes = ['.', 'o', 's', '^', 'D', 'x', '+']
                    rand = random.randint(0, 6)
                    self.groupShapes.update({
                        'ungrouped' : availableShapes[rand]
                    })

                    self.pcaFileData.update({
                        'Shapes': self.groupShapes
                    })


        return self.pcaDataDict

