from graphDrawing.graphs.pcaGraph.pcaAppearanceGUI import *
from graphDrawing.graphs.pcaGraph.pcaGraph import pcaGraph as pcaGraph
import math
class PcaAppearance(pcaAppearance_Frame):

    def __init__(self, parent):
        pcaAppearance_Frame.__init__(self, parent)
        self._parent = parent
        self.result = ""

        self.groupNames
        self.groupColours
        self.groupShapes
        self.groupSizes
        self.title

        #load the title
        self.pca_Title.Clear()
        if not self.title=='':
            self.pca_Title.SetValue(self.title)

        #load all the groups into choice box
        self.pca_GroupName.Clear()
        if(len(self.groupNames)>0):
            for x in range(len(self.groupNames)):
                self.pca_GroupName.Append(self.groupNames[x])
            self.pca_GroupName.SetSelection(0)

        #find the colour of the first group
        colour = self.groupColours[self.groupNames[0]]

        r = math.floor(colour[0]*255)
        g = math.floor(colour[1]*255)
        b = math.floor(colour[2]*255)

        self.pca_GroupColour.SetColour((r, g, b))

        #load all available shapes into choice box
        self.pca_GroupShape.Clear()
        self.pca_GroupShape.Append("Point")
        self.pca_GroupShape.Append("Circle")
        self.pca_GroupShape.Append("Square")
        self.pca_GroupShape.Append("Triangle")
        self.pca_GroupShape.Append("Diamond")
        self.pca_GroupShape.Append("Cross")
        self.pca_GroupShape.Append("Plus")

        #find the shape of the first group
        shape = self.groupShapes[self.groupNames[0]]
        self.UpdateShapeDisplay(shape)

        #find the size of the first group
        if (len(self.groupSizes) >0):
            self.pca_GroupSize.SetValue(self.groupSizes[self.groupNames[0]])

    def GroupChange(self, event):

        groupNum = self.pca_GroupName.GetCurrentSelection()

        #set the colour of the new group
        colour = self.groupColours[self.groupNames[groupNum]]

        r = math.floor(colour[0] * 255)
        g = math.floor(colour[1] * 255)
        b = math.floor(colour[2] * 255)

        self.pca_GroupColour.SetColour((r, g, b))

        #set the shape of the new group
        shape = self.groupShapes[self.groupNames[groupNum]]
        self.UpdateShapeDisplay(shape)

        #set the size of the new group
        size = self.groupSizes[self.groupNames[groupNum]]
        self.pca_GroupSize.SetValue(size)

    def UpdateShapeDisplay(self, shape):
        if shape == '.':
            self.pca_GroupShape.SetSelection(0)
        elif shape == 'o':
            self.pca_GroupShape.SetSelection(1)
        elif shape == 's':
            self.pca_GroupShape.SetSelection(2)
        elif shape == '^':
            self.pca_GroupShape.SetSelection(3)
        elif shape == 'D':
            self.pca_GroupShape.SetSelection(4)
        elif shape == 'x':
            self.pca_GroupShape.SetSelection(5)
        elif shape == '+':
            self.pca_GroupShape.SetSelection(6)

    def GetColours(self):
        return self.groupColours

    def GetShapes(self):
        return self.groupShapes

    def GetTitle(self):
        return self.title

    def GetSize(self):
        return self.groupSizes

    def OnClose(self,event):
        self._parent.Enable()
        self.Destroy()

    def CancelChanges(self, event):
        self.result="CANCEL"
        self._parent.Enable()
        self._parent.Show()
        self.Close()

    def AcceptChanges(self, event):
        self.result="CONFIRM"
        # find the group being edited
        groupNum = self.pca_GroupName.GetCurrentSelection()

        #get the colour that the group is being set to
        c = self.pca_GroupColour.GetColour()
        newR = c[0]/255
        newG = c[1]/255
        newB = c[2]/255

        #set the new colour of the group
        self.groupColours[self.groupNames[groupNum]] = []
        self.groupColours[self.groupNames[groupNum]].append(newR)
        self.groupColours[self.groupNames[groupNum]].append(newG)
        self.groupColours[self.groupNames[groupNum]].append(newB)

        # get the shape that the group is being set to
        newShape=''
        numShape = self.pca_GroupShape.GetCurrentSelection()
        if numShape == 0:
            newShape = '.'
        elif numShape == 1:
            newShape = 'o'
        elif numShape == 2:
            newShape = 's'
        elif numShape == 3:
            newShape = '^'
        elif numShape == 4:
            newShape = 'D'
        elif numShape == 5:
            newShape = 'x'
        elif numShape == 6:
            newShape = '+'

        self.groupShapes[self.groupNames[groupNum]] = newShape

        #get the size that the group is being set to
        newSize = self.pca_GroupSize.GetValue()
        #set the new size of the group
        self.groupSizes[self.groupNames[groupNum]] = newSize

        #set the title of the graph
        self.title = self.pca_Title.GetValue()


        self._parent.Enable()
        self._parent.Show()
        self.Close()
