
class admixtureGraph():

        def __init__(self):
            self.admixIDs = []
            self.ancestryDict = {}  # This will contain a Dict of lists
            self.numAncestries = 0
            self.phenoCol = []
            self.admixGroups = []
            self.phenoDict = {}
            self.admixGroupDict = {}



        def __init__(self, data):
            self.admixIDs = [data['AdmixIDs']]

            self.ancestryDict = {}  # This will contain a Dict of lists
            self.numAncestries = 0

            # check for n number of ancestries through iteration
            checkAncestry = True
            i = 1
            while (checkAncestry == True):
                ancestryKey = 'Ancestry' + str(i)

                if data[ancestryKey]:
                    self.ancestryDict.update({ancestryKey:[data[ancestryKey]]})
                    i = i+1
                    self.numAncestries = self.numAncestries + 1
                else:
                    checkAncestry = False

            # if there is phenotype data
            if data['PhenoIDs']:
                self.phenoIDs = data['PhenoIDs']
                self.phenoCol = data['PhenoColumn']
                self.admixGroups = self.getGroupList(self.phenoCol)
                self.phenoDict = {}
                for i in range(len(self.phenoCol)):
                    self.phenoDict.update({self.phenoIDs[i]: self.phenoCol[i]})
                self.admixGroupDict = {}

        def getGroupList(self, column):
            groupList = []
            for i in range(len(column)):
                data = column[i]
                if data in groupList:
                    pass
                else:
                    groupList.append(data)
            return groupList

        def genGroupDictionary(self):

            # looping through all the groups
            for numGroups in range(len(self.admixGroups)):
                tempAncestDict = {}
                for numAncest in range(self.numAncestries):
                    ancestryKey = 'Ancestry' + str(numAncest+1)
                    tempList = []
                    for numLines in range(len(self.admixIDs)):
                        tempValue = None
                        # if the ID from the FAM file exists in the phenotype file
                        if self.admixIDs[numLines] in self.phenoDict:
                            # if the key value matches the current group we are searching for..
                            if self.phenoDict.get(self.admixIDs[numLines]) == self.admixGroups[numGroups]:
                                tempValue = self.ancestryDict.get(ancestryKey)[numLines]
                                tempList.append(tempValue)

                    tempAncestDict.update({ancestryKey : tempList})

                self.admixGroupDict.update({
                    self.admixGroups[numGroups]: tempAncestDict
                })

        def getGroupList(self):
            return self.admixGroups

        def getGroupDictionary(self):
            return self.admixGroupDict

