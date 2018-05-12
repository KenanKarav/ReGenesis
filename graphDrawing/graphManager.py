import numpy as np
import wx
import wx.lib.mixins.inspection as wit

import json

from fileManagement.pcaCreator import pcaCreator as pcaCreator
from fileManagement.admixCreator import admixCreator as admixCreator
from graphDrawing.graphs.pcaGraph.pcaGraph import pcaGraph as pcaGraph
from graphDrawing.graphs.admixtureGraph.admixtureGraph import admixtureGraph as admixGraph

from graphDrawing.graphs.pcaGraph.pcaAppearance import PcaAppearance as pcaAppearance


import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg as NavigationToolbar


MAXWIDTH = 925
BUTTONHEIGHT = 40
MAXHEIGHT = 650
FIGUREWIDTH = 9
FIGUREHEIGHT = 5.5
FIGUREDPI = 100
class graphManager(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"ReGenesis", pos=wx.DefaultPosition,
                          size=wx.Size(MAXWIDTH, MAXHEIGHT),
                          style=wx.DEFAULT_FRAME_STYLE & ~ (wx.RESIZE_BORDER |
                                                            wx.MAXIMIZE_BOX))
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.sizer = wx.BoxSizer(wx.VERTICAL)

        self.renderer = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.sizer.Add(self.renderer, 1, wx.EXPAND | wx.ALL, 5)


        # toolbar
        self.toolbar = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.toolbar.SetMinSize(wx.Size(1200, 40))
        self.toolbar.SetMaxSize(wx.Size(1200,40))
        self.toolbarSizer = wx.BoxSizer(wx.HORIZONTAL)

        # adding buttons
        self.homeButton = wx.Button(self.toolbar, wx.ID_ANY, u"Home", wx.DefaultPosition, wx.DefaultSize, 0)
        self.toolbarSizer.Add(self.homeButton, 0, wx.ALL, 5)

        self.backButton = wx.Button(self.toolbar, wx.ID_ANY, u"Undo", wx.DefaultPosition, wx.DefaultSize, 0)
        self.toolbarSizer.Add(self.backButton, 0, wx.ALL, 5)

        self.forwardButton = wx.Button(self.toolbar, wx.ID_ANY, u"Redo", wx.DefaultPosition, wx.DefaultSize, 0)
        self.toolbarSizer.Add(self.forwardButton, 0, wx.ALL, 5)

        self.panButton = wx.Button(self.toolbar, wx.ID_ANY, u"Pan", wx.DefaultPosition, wx.DefaultSize, 0)
        self.toolbarSizer.Add(self.panButton, 0, wx.ALL, 5)

        self.zoomButton = wx.Button(self.toolbar, wx.ID_ANY, u"Zoom", wx.DefaultPosition, wx.DefaultSize, 0)
        self.toolbarSizer.Add(self.zoomButton, 0, wx.ALL, 5)

        self.appearanceButton = wx.Button(self.toolbar, wx.ID_ANY, u"Edit Appearance", wx.DefaultPosition, wx.DefaultSize, 0)
        self.toolbarSizer.Add(self.appearanceButton, 0, wx.ALL, 5)

        self.saveButton = wx.Button(self.toolbar, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0)
        self.toolbarSizer.Add(self.saveButton, 0, wx.ALL, 5)

        self.loadButton = wx.Button(self.toolbar, wx.ID_ANY, u"Load", wx.DefaultPosition, wx.DefaultSize, 0)
        self.toolbarSizer.Add(self.loadButton, 0, wx.ALL, 5)

        self.exportButton = wx.Button(self.toolbar, wx.ID_ANY, u"Export", wx.DefaultPosition, wx.DefaultSize, 0)
        self.toolbarSizer.Add(self.exportButton, 0, wx.ALL, 5)



        self.toolbar.SetSizer(self.toolbarSizer)
        self.toolbar.Layout()
        self.toolbarSizer.Fit(self.toolbar)
        self.sizer.Add(self.toolbar, 1, wx.EXPAND | wx.ALL, 5)

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

        # Toolbar Events

        self.saveButton.Bind(wx.EVT_BUTTON, self.saveGraphOnMenuSelection)
        self.loadButton.Bind(wx.EVT_BUTTON, self.loadGraphOnMenuSelection)
        self.zoomButton.Bind(wx.EVT_BUTTON, self.onZoomButtonClick)
        self.appearanceButton.Bind(wx.EVT_BUTTON, self.onAppearanceButtonClick)

    def __del__(self):
        pass

    def createFigure(self):
        # checking if figure exists to avoid reinitializing
        if not hasattr(self, 'figure'):
            self.figure = mpl.figure.Figure(figsize=(FIGUREWIDTH, FIGUREHEIGHT), dpi=FIGUREDPI)

        else:
            self.figure.clf()

        # add subplot to newly created/cleared figure

        self.axes = self.figure.add_subplot(111)

    def showGraph(self):

        self.axes.legend()
        self.canvas = FigureCanvas(self.renderer, wx.ID_ANY, self.figure)

        if not hasattr(self, "navToolbar"):
            self.navToolbar = NavigationToolbar(self.canvas)
            self.navToolbar.Hide()

    def CreatePCAPlot(self, data):

        self.pca = pcaGraph(data)
        pcaData = self.pca.findPcaData()
        self.plotPcaData(pcaData)

    def CreateAdmixturePlot(self, data):

        self.admix = admixGraph(data)


    def plotPcaData(self, pcaData):
        pcaAppearance.groupNames = self.pca.getGroups()
        pcaAppearance.groupColours = self.pca.getColours()
        pcaAppearance.groupShapes = self.pca.getShapes()

        if not hasattr(self, 'figure'):
            self.figure = mpl.figure.Figure()  # figsize=(6, 4), dpi=100)
            self.axes = self.figure.add_subplot(111)
        else:
            self.figure.clf()
            self.axes = self.figure.add_subplot(111)
        # Add it to the panel created in wxFormBuilder

        self.createFigure()

        for group in pcaData:
            x = pcaData[group]['x']
            y = pcaData[group]['y']
            # getting the colours of the groups
            colourList = self.pca.getColours()
            # getting the shapes of the groups
            shapeList = self.pca.getShapes()

            # plotting the graph
            self.axes.scatter(x, y, label=group, s=10, color=colourList[group], marker=shapeList[group])

        self.showGraph()

        return


    def plotAdmixData(self, admixData):


        groups = list(admixData.keys())
        ancestryLabels = list(admixData[groups[0]].keys())
        individualCount = 0
        groupCenters = []

        # creating figure
        self.createFigure()

        fullRatios = []

        self.axes.set_xticklabels([])
        for group in admixData:

            ratios = []

            for ancestry in admixData[group]:
                anc = admixData[group][ancestry]
                ratios.append(anc)
            numAncestries = len(ratios)
            numIndividuals = len(ratios[0])

            # Normalising ratios so they add up to 1
            tempRatios = list(zip(*ratios))
            sums = list(map(sum, tempRatios))
            for ancestry in ratios:
                for i in range(len(ancestry)):
                    ancestry[i] /= sums[i]

            # storing values used for separating groups at presentation

            groupCenters.append(individualCount + (numIndividuals/2))
            individualCount += numIndividuals
            self.axes.axvline(individualCount, color='w')

            if len(fullRatios) > 0:
                for i in range(len(fullRatios)):
                    fullRatios[i].extend(ratios[i])
            else:
                fullRatios = ratios

        # plotting bars
        indexes = [i for i in range(individualCount)]
        self.axes.bar(indexes, fullRatios[0], 1, label=ancestryLabels[0])
        # barBottom keeps track of the current height of each bar so subsequent bars can be plotted above
        barBottom = [0 for i in range(individualCount)]
        for i in range(0, numAncestries - 1):

            # increasing height of barBottom
            barBottom = [x + y for x, y in zip(barBottom, fullRatios[i])]
            self.axes.bar(indexes, fullRatios[i + 1], 1, bottom=barBottom, label=ancestryLabels[i + 1])

        # setting labels for better readability
        self.axes.set_xticks(groupCenters)
        self.axes.set_xticklabels(groups)

        self.showGraph()

    # Event Handlers
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
        if self.child.result == "CANCEL":
            event.Skip()
        elif self.child.result == "CONFIRM":
            self.CreateAdmixturePlot(self.child._dataDict)

    def saveGraphOnMenuSelection(self, event):
        with wx.FileDialog(self, "Save Graph file", wildcard="Regenesis Graph File files (*.rgf)|*.rgf",
                           style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return  # the user changed their mind

            # save the current contents in the file
            pathname = fileDialog.GetPath()
            try:
                with open(pathname, 'w', encoding='utf-8') as file:
                    self.doSaveData(file)
            except IOError:
                wx.LogError("Cannot save current data in file '%s'." % pathname)

    def doSaveData(self, f):
        # find dictionary of values to plot
        pcaData = self.pca.getSaveFileData()
        json.dump(pcaData, f, ensure_ascii=False)
        f.close()

    def loadGraphOnMenuSelection(self, event):
        '''if self.contentNotSaved:
            if wx.MessageBox("Current content has not been saved! Proceed?", "Please confirm",
                             wx.ICON_QUESTION | wx.YES_NO, self) == wx.NO:
                return'''

            # otherwise ask the user what new file to open
        with wx.FileDialog(self, "Load Graph file", wildcard="Regenesis Graph File files (*.rgf)|*.rgf",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return  # the user changed their mind

            # Proceed loading the file chosen by the user
            pathname = fileDialog.GetPath()
            try:
                with open(pathname, 'r') as file:
                    self.doLoadData(file)
            except IOError:
                wx.LogError("Cannot open file '%s'." % file)

    def doLoadData(self,f):
        pcaData = json.load(f)
        self.CreatePCAPlot(pcaData)
        f.close()

    def exportGraphOnMenuSelection(self, event):
        print("export graph event")

    def onZoomButtonClick(self, event):

        self.navToolbar.zoom()

    def onAppearanceButtonClick(self, event):
        self.child = pcaAppearance(self)
        self.Disable()
        self.child.ShowModal()
        if self.child.result == "CANCEL":
            event.Skip()
        elif self.child.result == "CONFIRM":
            print("RE-PLOT GRAPH")

            #re-plotting the graph with the newly chosen colours
            newColours = self.child.GetColours()
            self.pca.setColours(newColours)

            #re-plotting the graph with the newly chosen shape
            newShapes = self.child.GetShapes()
            self.pca.setShapes(newShapes)

            pcaData = self.pca.findPcaData(False)
            self.plotPcaData(pcaData)
            #self.CreatePCAPlot(self.child._dataDict)

    def onHomeButtonClick(self, event):
        self.navToolbar.home()

    def onPanButtonClick(self, event):
        self.navToolbar.pan()

    def onConfigureButtonClick(self, event):
        self.navToolbar.configure_subplots()

    def onBackButtonClick(self, event):
        self.navToolbar.back()

    def onForwardButtonClick(self, event):
        self.navToolbar.forward()

    def onExportButtonClick(self, event):
        self.navToolbar.save_figure()
if __name__ == "__main__":
    app = wx.App(False)
    frame = graphManager(None)
    frame.Show()
    app.MainLoop()