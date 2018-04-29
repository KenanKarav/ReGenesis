
class AdmixtureIndividual:

###############################Constructor#############################################
    def __init__(self, popRatios):
        self.populationRatios = popRatios #this should be a list/array [] of the ratios
        self.ID = ""
        self.Name = ""
        self.isVisible = True
        self.phenotypeData = []
        self.receivedPheno = False
        self.populationGroups = []
        self.ancestryDict = {}


##############################Mutators##################################################
    def setId(self, id):
        self.ID = id

    def setName(self, name):
        self.Name = name

    def setPhenotypedata(self, phenoValues):
        self.phenotypeData = phenoValues

    def setVisibility(self, visible):
        self.isVisible = visible

#############################Accessors##################################################
    def getPopRatios(self):
        return self.populationRatios

    def getID(self):
        return self.ID

    def getName(self):
        return self.Name

    def getPhenotypeData(self):
        return self.phenotypeData

    def getPopGroups(self):
        return self.populationGroups

    def getNumOfAncestors(self):
        return len(self.populationGroups)

    def getVisibility(self):
        return self.isVisible

    def getAncestryDictionary(self):
        return self.ancestryDict

#############################Methods######################################################
    def buildAncestryDictonary(self):
        numAncestors = len(self.populationRatios)
        for loop in range(0, numAncestors):
            key = loop
            self.ancestryDict.update({key, self.populationRatios[loop]})


