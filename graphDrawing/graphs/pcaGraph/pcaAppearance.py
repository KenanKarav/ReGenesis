from graphDrawing.graphs.pcaGraph.pcaAppearanceGUI import *
from graphDrawing.graphs.pcaGraph.pcaGraph import pcaGraph as pcaGraph


class PcaAppearance(pcaGroupAppearance_Frame):

    def __init__(self, parent):
        pcaGroupAppearance_Frame.__init__(self, parent)
        self._parent = parent
        self.result = ""

        #load all the groups into choice box
        self.groupNames = pcaGraph.pcaGroups
        if(len(self.groupNames>0)):
            for x in range(len(self.groupNames)):
                self.pca_GroupName.Append(self.groupNames[x])

        #find the current colour of the group

        #load all available shapes into choice box
        self.pca_GroupShape.Append("Circle")
        self.pca_GroupShape.Append("Square")
        self.pca_GroupShape.Append("Triangle")
        self.pca_GroupShape.Append("Diamond")
        self.pca_GroupShape.Append("Cross")
        self.pca_GroupShape.Append("Plus")

    def GroupChange(self, event):
        pass

    def CancelChanges(self, event):
        self._parent.Enable()
        self._parent.Show()
        self.Close()

    def AcceptChanges(self, event):
        #set the colour

        pass

