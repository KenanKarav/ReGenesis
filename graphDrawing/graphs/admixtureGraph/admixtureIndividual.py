
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
    def setid(self, id):
        self.ID = id

    def setname(self, name):
        self.Name = name

    def setphenotypedata(self, phenoValues):
        self.phenotypeData = phenoValues

    def setvisibility(self, visible):
        self.isVisible = visible

#############################Accessors##################################################
    def getpopratios(self):
        return self.populationRatios

    def getid(self):
        return self.ID

    def getname(self):
        return self.Name

    def getphenotypedata(self):
        return self.phenotypeData

    def getpopgroups(self):
        return self.populationGroups

    def getnumofancestors(self):
        return len(self.populationGroups)

    def getvisibility(self):
        return self.isVisible

    def getancestrydictionary(self):
        return self.ancestryDict

#############################Methods######################################################
    def buildancestrydictonary(self):
        numAncestors = len(self.populationRatios)
        for loop in range(0, numAncestors):
            key = loop
            self.ancestryDict.update({key, self.populationRatios[loop]})


