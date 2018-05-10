# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Apr 18 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class pcaGroupAppearance_Frame
###########################################################################

class pcaGroupAppearance_Frame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"PCA Plot Group Appearance", pos=wx.DefaultPosition,
                          size=wx.Size(327, 217), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        bSizer9 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText9 = wx.StaticText(self, wx.ID_ANY, u"Group name:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText9.Wrap(-1)
        bSizer9.Add(self.m_staticText9, 0, wx.ALL, 5)

        pca_GroupNameChoices = []
        self.pca_GroupName = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, pca_GroupNameChoices, 0)
        self.pca_GroupName.SetSelection(0)
        bSizer9.Add(self.pca_GroupName, 0, wx.ALL, 5)

        bSizer7.Add(bSizer9, 1, wx.EXPAND, 5)

        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText6 = wx.StaticText(self, wx.ID_ANY, u"Set group colour:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)
        bSizer8.Add(self.m_staticText6, 0, wx.ALL, 5)

        self.pca_GroupColour = wx.ColourPickerCtrl(self, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize,
                                                   wx.CLRP_DEFAULT_STYLE)
        bSizer8.Add(self.pca_GroupColour, 0, wx.ALL, 5)

        bSizer7.Add(bSizer8, 1, wx.EXPAND, 5)

        bSizer10 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText8 = wx.StaticText(self, wx.ID_ANY, u"Change group shape:", wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.m_staticText8.Wrap(-1)
        bSizer10.Add(self.m_staticText8, 0, wx.ALL, 5)

        pca_GroupShapeChoices = []
        self.pca_GroupShape = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, pca_GroupShapeChoices, 0)
        self.pca_GroupShape.SetSelection(0)
        bSizer10.Add(self.pca_GroupShape, 0, wx.ALL, 5)

        bSizer7.Add(bSizer10, 1, wx.EXPAND, 5)

        bSizer11 = wx.BoxSizer(wx.HORIZONTAL)

        self.pca_GroupCancel = wx.Button(self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer11.Add(self.pca_GroupCancel, 0, wx.ALL, 5)

        self.pca_GroupAccept = wx.Button(self, wx.ID_ANY, u"Accept Changes", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer11.Add(self.pca_GroupAccept, 0, wx.ALL, 5)

        bSizer7.Add(bSizer11, 1, wx.ALIGN_RIGHT, 5)

        self.SetSizer(bSizer7)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.pca_GroupName.Bind(wx.EVT_CHOICE, self.GroupChange)
        self.pca_GroupCancel.Bind(wx.EVT_BUTTON, self.CancelChanges)
        self.pca_GroupAccept.Bind(wx.EVT_BUTTON, self.AcceptChanges)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def GroupChange(self, event):
        event.Skip()

    def CancelChanges(self, event):
        event.Skip()

    def AcceptChanges(self, event):
        event.Skip()


