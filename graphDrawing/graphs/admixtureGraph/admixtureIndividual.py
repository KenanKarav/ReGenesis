
class AdmixtureIndividual:

###############################Constructor#############################################
    def __init__(self, popRatios):
        self.populationRatios = popRatios #this should be a list/array [] of the ratios
        self.Name = ""
        self.isVisible = True
        self.phenotypeData = []
        self.receivedPheno = False
        self.populationGroups = []

##############################Mutators##################################################
    def setname(self, name):
        self.Name = name

    def setphenotypedata(self, phenoValues):
        self.phenotypeData = phenoValues

    def setvisibile(self, visibility):
        self.isVisible = visibility

#############################Accessors##################################################
    def getpopratios(self):
        return self.populationRatios

    def getname(self):
        return self.Name

    def getphenotypedata(self):
        return self.phenotypeData

    def getpopgroups(self):
        return self.populationGroups

    def getnumofancestors(self):
        return len(self.populationGroups)

    def getvisible(self):
        return self.isVisible