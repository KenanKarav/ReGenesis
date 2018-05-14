
class admixtureGraph():

        """
        Initialise admixture graph variables.
        """
        def __init__(self, data):
            self.admixIDs = data['AdmixIDs']
            self.ancestryDict = {}  # This will contain a Dict of lists
            self.numAncestries = 0
            self.graphType = 'admix'

            # check for n number of ancestries through iteration
            checkAncestry = True
            i = 1
            while (checkAncestry == True):
                ancestryKey = 'Ancestry' + str(i)

                if ancestryKey in data:
                    self.ancestryDict.update({ancestryKey:data[ancestryKey]})
                    i = i+1
                    self.numAncestries = self.numAncestries + 1
                else:
                    checkAncestry = False

            self.hasPheno = False
            # if there is phenotype data
            if 'PhenoIDs' in data:
                self.hasPheno = True
                self.phenoIDs = data['PhenoIDs']
                self.phenoCol = data['PhenoColumn']
                self.admixGroups = self.genGroupList(self.phenoCol)
                self.phenoDict = {}
                for i in range(len(self.phenoCol)):
                    self.phenoDict.update({self.phenoIDs[i]: self.phenoCol[i]})
                self.admixFileData = data

        """
        Generate list of unique groups
        """
        # Returns a list of containing each unique group
        def genGroupList(self, column):
            groupList = []
            for i in range(len(column)):
                data = column[i]
                if data in groupList:
                    pass
                else:
                    groupList.append(data)
            return groupList

        """
        Generate data dictionary that seprates each individual into their respective groups.
        """
        def genDataDictionary(self):
            tempDataDict = {}

            if self.hasPheno == True:
                # looping through all the groups
                for numGroups in range(len(self.admixGroups)):
                    tempAncestDict = {}
                    for numAncest in range(self.numAncestries):
                        ancestryKey = 'Ancestry' + str(numAncest+1)
                        tempList = []
                        for numLines in range(len(self.admixIDs)):
                            tempValue = None
                            # if the ID from the FAM file exists in the phenotype file
                            if self.admixIDs[numLines] in self.phenoIDs:
                                # if the key value matches the current group we are searching for..
                                if self.phenoDict.get(self.admixIDs[numLines]) == self.admixGroups[numGroups]:
                                    valueList = self.ancestryDict.get(ancestryKey)
                                    tempValue = valueList[numLines]
                                    tempList.append(tempValue)

                        tempAncestDict.update({ancestryKey : tempList})

                    tempDataDict.update({
                        self.admixGroups[numGroups]: tempAncestDict
                    })
                return tempDataDict
            else:

                tempDataDict = {'ungrouped' : self.ancestryDict}
                return tempDataDict


        # Accessors
        """
        Return admix IDs
        """
        def getAdmixIDs(self):
            return self.admixIDs
        """
        Return ancestry dictionary
        """
        def getAncestryDict(self):
            return self.ancestryDict
        """
        Return number of ancestries
        """
        def getNumAncestries(self):
            return self.numAncestries
        """
        Return dictionary with phenotype data
        """
        def getPhenoDict(self):
            return self.phenoDict
        """
        Return list of groups
        """
        def getGroupList(self):
            return self.admixGroups
        """
        Return data in dictionary in save-able format
        """
        def getSaveFileData(self):
            tempDict = self.admixFileData
            # Delete the file data types as they cannot be converted to a save-able format
            del tempDict ["AdmixFile"]
            if "PhenoFile" in tempDict:
                del tempDict["PhenoFile"]
            return tempDict
        """
        Return graph type
        """
        def getGraphType(self):
            return self.graphType


