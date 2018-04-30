import numpy as np
import wx
import wx.lib.mixins.inspection as wit
from fileManagement.pcaCreator import pcaCreator as pcaCreator
from fileManagement.admixCreator import admixCreator as admixCreator
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
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.renderer = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,wx.TAB_TRAVERSAL)
        sizer.Add(self.renderer, 1, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(sizer)
        self.Layout()
        self.MenuBar = wx.MenuBar(0)
        self.Menu = wx.Menu()
        self.newPCA = wx.MenuItem(self.Menu, wx.ID_ANY, u"PCA Graph", wx.EmptyString, wx.ITEM_NORMAL)
        self.Menu.Append(self.newPCA)

        self.newAdmixture = wx.MenuItem(self.Menu, wx.ID_ANY, u"Admixture Graph", wx.EmptyString, wx.ITEM_NORMAL)
        self.Menu.Append(self.newAdmixture)

        self.MenuBar.Append(self.Menu, u"New Graph")

        self.SetMenuBar(self.MenuBar)

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_MENU, self.newPCAOnMenuSelection, id=self.newPCA.GetId())
        self.Bind(wx.EVT_MENU, self.newAdmixtureOnMenuSelection, id=self.newAdmixture.GetId())

    def __del__(self):
        pass

    def CreatePlot(self):
        self.figure = mpl.figure.Figure()  # figsize=(6, 4), dpi=100)
        self.axes = self.figure.add_subplot(111)
        x = np.arange(0, 6, .01)
        y = np.sin(x ** 2) * np.exp(-x)
        self.axes.plot(x, y)

        # Add it to the panel created in wxFormBuilder
        self.canvas = FigureCanvas(self.renderer, wx.ID_ANY, self.figure)
        self.toolbar = NavigationToolbar(self.canvas)
        self.toolbar.Realize()
        return
    # Virtual event handlers, overide them in your derived class
    def newPCAOnMenuSelection(self, event):
        self.child = pcaCreator(self)
        self.Disable()
        self.child.Show()


    def newAdmixtureOnMenuSelection(self, event):
        self.child = admixCreator(self)
        self.Disable()
        self.child.Show()

if __name__ == "__main__":
    app = wx.App(False)
    frame = graphManager(None)
    frame.CreatePlot()
    frame.Show()
    app.MainLoop()