import numpy as np
import wx
import wx.lib.mixins.inspection as wit
from fileManagement.pcaCreator import pcaCreator as pcaCreator
from fileManagement.admixCreator import admixCreator as admixCreator
from graphDrawing.graphs.pcaGraph.pcaGraph import pcaGraph as pcaGraph
if 'phoenix' in wx.PlatformInfo:
    import wx.lib.agw.aui as aui
else:
    import wx.aui as aui

import matplotlib as mpl
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg as NavigationToolbar




class graphManager(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"ReGenesis", pos=wx.DefaultPosition,
                          size=wx.Size(650, 550), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.renderer = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,wx.TAB_TRAVERSAL)
        self.sizer.Add(self.renderer, 1, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(self.sizer)
        self.Layout()
        self.MenuBar = wx.MenuBar(0)

        #new graph menu options
        self.newGraph = wx.Menu()
        self.newPCA = wx.MenuItem(self.newGraph, wx.ID_ANY, u"PCA Graph", wx.EmptyString, wx.ITEM_NORMAL)
        self.newGraph.Append(self.newPCA)

        self.newAdmixture = wx.MenuItem(self.newGraph, wx.ID_ANY, u"Admixture Graph", wx.EmptyString, wx.ITEM_NORMAL)
        self.newGraph.Append(self.newAdmixture)

        self.MenuBar.Append(self.newGraph, u"New Graph")


        #Manage Graphs Menu
        self.manageGraphs = wx.Menu()

        self.saveGraph = wx.MenuItem(self.manageGraphs, wx.ID_ANY, u"Save", wx.EmptyString, wx.ITEM_NORMAL)
        self.manageGraphs.Append(self.saveGraph)

        self.loadGraph = wx.MenuItem(self.manageGraphs, wx.ID_ANY, u"Load", wx.EmptyString, wx.ITEM_NORMAL)
        self.manageGraphs.Append(self.loadGraph)

        self.exportGraph = wx.MenuItem(self.manageGraphs, wx.ID_ANY, u"Export", wx.EmptyString, wx.ITEM_NORMAL)
        self.manageGraphs.Append(self.exportGraph)

        self.MenuBar.Append(self.manageGraphs, u"Manage Graphs")

        self.SetMenuBar(self.MenuBar)

        self.Centre(wx.BOTH)

        # Connect Events
        # New graph events
        self.Bind(wx.EVT_MENU, self.newPCAOnMenuSelection, id=self.newPCA.GetId())
        self.Bind(wx.EVT_MENU, self.newAdmixtureOnMenuSelection, id=self.newAdmixture.GetId())

        # Manage graph events
        self.Bind(wx.EVT_MENU, self.saveGraphOnMenuSelection, id=self.saveGraph.GetId())
        self.Bind(wx.EVT_MENU, self.loadGraphOnMenuSelection, id=self.loadGraph.GetId())
        self.Bind(wx.EVT_MENU, self.exportGraphOnMenuSelection, id=self.exportGraph.GetId())




    def __del__(self):
        pass

    def CreatePCAPlot(self, data):

        pca = pcaGraph(data)
        pcaGroups = pca.findGroupData()
        if not hasattr(self, 'figure'):
            self.figure = mpl.figure.Figure()  # figsize=(6, 4), dpi=100)
            self.axes = self.figure.add_subplot(111)
        else:
            self.figure.clf()
            self.axes = self.figure.add_subplot(111)
        # Add it to the panel created in wxFormBuilder


        if pca.dimension == 2:
            x = []
            y = []

            for group in pcaGroups:
                x = pcaGroups[group]['x']
                y = pcaGroups[group]['y']

                self.axes.scatter(x, y, label=group, s=2)
        self.canvas = FigureCanvas(self.renderer, wx.ID_ANY, self.figure)

        self.toolbar = NavigationToolbar(self.canvas)
        return

    # Virtual event handlers, overide them in your derived class
    def newPCAOnMenuSelection(self, event):
        self.child = pcaCreator(self)
        self.Disable()
        self.child.ShowModal()
        if self.child.result == "CANCEL":
            event.Skip()
        elif self.child.result == "CONFIRM":
            self.CreatePCAPlot(self.child._dataDict)
    def newAdmixtureOnMenuSelection(self, event):
        self.child = admixCreator(self)
        self.Disable()
        self.child.ShowModal()

    def saveGraphOnMenuSelection(self, event):
        print("save graph event")

    def loadGraphOnMenuSelection(self, event):
        print("load graph event")

    def exportGraphOnMenuSelection(self, event):
        print("export graph event")


if __name__ == "__main__":
    app = wx.App(False)
    frame = graphManager(None)
    #frame.CreatePlot()
    frame.Show()
    app.MainLoop()