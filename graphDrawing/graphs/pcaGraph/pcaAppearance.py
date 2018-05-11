from graphDrawing.graphs.pcaGraph.pcaAppearanceGUI import *
from graphDrawing.graphs.pcaGraph.pcaGraph import pcaGraph as pcaGraph
import math
class PcaAppearance(pcaGroupAppearance_Frame):

    def __init__(self, parent):
        pcaGroupAppearance_Frame.__init__(self, parent)
        self._parent = parent
        self.result = ""

        self.groupNames
        self.groupColours


        #load all the groups into choice box
        self.pca_GroupName.Clear()
        if(len(self.groupNames)>0):
            for x in range(len(self.groupNames)):
                self.pca_GroupName.Append(self.groupNames[x])
            self.pca_GroupName.SetSelection(0)

        #find the current colour of the group
        colour = self.groupColours[self.groupNames[0]]

        r = math.floor(colour[0]*255)
        g = math.floor(colour[1]*255)
        b = math.floor(colour[2]*255)

        self.pca_GroupColour.SetColour((r, g, b))

        #load all available shapes into choice box
        self.pca_GroupShape.Clear()
        self.pca_GroupShape.Append("Default")
        self.pca_GroupShape.Append("Circle")
        self.pca_GroupShape.Append("Square")
        self.pca_GroupShape.Append("Triangle")
        self.pca_GroupShape.Append("Diamond")
        self.pca_GroupShape.Append("Cross")
        self.pca_GroupShape.Append("Plus")
        self.pca_GroupShape.SetSelection(0)

    def GroupChange(self, event):
        #set the colour of the new group
        groupNum = self.pca_GroupName.GetCurrentSelection()
        colour = self.groupColours[self.groupNames[groupNum]]

        r = math.floor(colour[0] * 255)
        g = math.floor(colour[1] * 255)
        b = math.floor(colour[2] * 255)

        self.pca_GroupColour.SetColour((r, g, b))

    def GetColours(self):
        return self.groupColours

    def CancelChanges(self, event):
        self.result="CANCEL"
        self._parent.Enable()
        self._parent.Show()
        self.Close()

    def AcceptChanges(self, event):
        self.result="CONFIRM"
        # find the group being edited
        groupNum = self.pca_GroupName.GetCurrentSelection()
       # print(groupNum)

        #get the colour of the group
        c = self.pca_GroupColour.GetColour()
        newR = c[0]/255
        newG = c[1]/255
        newB = c[2]/255

       # print(str(newR) + ', ' + str(newG) +', ' + str(newB))
        #set the new colour of the group
        self.groupColours[self.groupNames[groupNum]] = []
        self.groupColours[self.groupNames[groupNum]].append(newR)
        self.groupColours[self.groupNames[groupNum]].append(newG)
        self.groupColours[self.groupNames[groupNum]].append(newB)

        self._parent.Enable()
        self._parent.Show()
        self.Close()

