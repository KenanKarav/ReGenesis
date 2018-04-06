from enum import Enum

#############Temporary Enum Classes - We may want to make these separate classes ? #############
class Colour(Enum):
    Green = 1
    Blue = 2
    Red = 3
    Orange = 4
    Yellow = 5
    Purple = 6

class Shape(Enum):
    Circle = 1
    Cross = 2
    Trinagle = 3
    Square = 4
    Pentagon = 5
    Hexagon = 6
###############################################################################################

class PCAIndividual:

    def __init__(self, positiondata, name):
        self.positionData = positiondata
        self.Name = name
        self.phenotypeData = []
        self.Shape = Shape(1)
        self.Colour = Colour(1)
        self.isVisible = True
        self.populationGroups = []

########################Mutators##############################################################
    def setname(self, name):
        self.Name = name

    def setphenotypedata(self, phenoData):
        self.phenotypeData = phenoData

    def setshape(self, shapeNum):
        self.Shape = shapeNum

    def setcolour(self, colourNum):
        self.Colour = colourNum

    def setVisibility(self, visible):
        self.isVisible = visible

    def setPopGroups(self, groups):
        self.populationGroups = groups

#######################Accessors#############################################################
    def getname(self):
        return self.Name

    def getphenotypedata(self):
        return self.phenotypeData

    def getshape(self):
        return self.Shape

    def getcolour(self):
        return self.Colour

    def getvisibility(self):
        return self.isVisible

    def getpopgroups(self):
        return self.populationGroups