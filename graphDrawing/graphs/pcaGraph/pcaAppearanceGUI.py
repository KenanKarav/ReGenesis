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
## Class pcaAppearance_Frame
###########################################################################

class pcaAppearance_Frame(wx.Dialog):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Edit PCA Plot Appearance", pos=wx.DefaultPosition,
                          size=wx.Size(325, 439), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.Bind(wx.EVT_CLOSE, self.OnClose)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.SetBackgroundColour(wx.Colour(240, 240, 240))

        parentPcaSizer = wx.BoxSizer(wx.VERTICAL)

        self.pcaAppearLabel_GeneralAppearance = wx.StaticText(self, wx.ID_ANY, u"General Appearance:",
                                                              wx.DefaultPosition, wx.DefaultSize, 0)
        self.pcaAppearLabel_GeneralAppearance.Wrap(-1)
        self.pcaAppearLabel_GeneralAppearance.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))

        parentPcaSizer.Add(self.pcaAppearLabel_GeneralAppearance, 0, wx.ALL, 5)

        childPcaSizer_Title = wx.BoxSizer(wx.HORIZONTAL)

        self.pcaAppearLabel_Title = wx.StaticText(self, wx.ID_ANY, u"Title:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.pcaAppearLabel_Title.Wrap(-1)
        self.pcaAppearLabel_Title.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))

        childPcaSizer_Title.Add(self.pcaAppearLabel_Title, 0, wx.ALL, 5)

        self.pca_Title = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(250, -1), 0)
        childPcaSizer_Title.Add(self.pca_Title, 0, wx.ALL, 5)

        parentPcaSizer.Add(childPcaSizer_Title, 1, wx.EXPAND, 5)

        self.pcaCheckBox_ShowGrid = wx.CheckBox(self, wx.ID_ANY, u"Show Grid", wx.DefaultPosition, wx.DefaultSize, 0)
        self.pcaCheckBox_ShowGrid.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))

        parentPcaSizer.Add(self.pcaCheckBox_ShowGrid, 0, wx.ALL, 5)

        self.pcaCheckBox_showAxesLabels = wx.CheckBox(self, wx.ID_ANY, u"Show Axes Labels", wx.DefaultPosition,
                                                      wx.DefaultSize, 0)
        self.pcaCheckBox_showAxesLabels.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))

        parentPcaSizer.Add(self.pcaCheckBox_showAxesLabels, 0, wx.ALL, 5)

        parentPcaSizer.Add((0, 5), 1, wx.EXPAND, 5)

        self.pcaAppearLabel_Group = wx.StaticText(self, wx.ID_ANY, u"Group Appearance:", wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
        self.pcaAppearLabel_Group.Wrap(-1)
        self.pcaAppearLabel_Group.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))

        parentPcaSizer.Add(self.pcaAppearLabel_Group, 0, wx.ALL, 5)

        childPcaGroupSizer_Name = wx.BoxSizer(wx.HORIZONTAL)

        self.pcaGroupLabel_Name = wx.StaticText(self, wx.ID_ANY, u"Group name:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.pcaGroupLabel_Name.Wrap(-1)
        self.pcaGroupLabel_Name.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))

        childPcaGroupSizer_Name.Add(self.pcaGroupLabel_Name, 0, wx.ALL, 5)

        pca_GroupNameChoices = []
        self.pca_GroupName = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, pca_GroupNameChoices, 0)
        self.pca_GroupName.SetSelection(0)
        childPcaGroupSizer_Name.Add(self.pca_GroupName, 0, wx.ALL, 5)

        parentPcaSizer.Add(childPcaGroupSizer_Name, 1, wx.EXPAND, 5)

        childPcaGroupSizer_Colour = wx.BoxSizer(wx.HORIZONTAL)

        self.pcaGroupLabel_Colour = wx.StaticText(self, wx.ID_ANY, u"Set group colour:", wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
        self.pcaGroupLabel_Colour.Wrap(-1)
        self.pcaGroupLabel_Colour.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))

        childPcaGroupSizer_Colour.Add(self.pcaGroupLabel_Colour, 0, wx.ALL, 5)

        self.pca_GroupColour = wx.ColourPickerCtrl(self, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize,
                                                   wx.CLRP_DEFAULT_STYLE)
        childPcaGroupSizer_Colour.Add(self.pca_GroupColour, 0, wx.ALL, 5)

        parentPcaSizer.Add(childPcaGroupSizer_Colour, 1, wx.EXPAND, 5)

        childPcaGroupSizer_Shape = wx.BoxSizer(wx.HORIZONTAL)

        self.pcaGroupLabel_Shape = wx.StaticText(self, wx.ID_ANY, u"Set group shape:", wx.DefaultPosition,
                                                 wx.DefaultSize, 0)
        self.pcaGroupLabel_Shape.Wrap(-1)
        self.pcaGroupLabel_Shape.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))

        childPcaGroupSizer_Shape.Add(self.pcaGroupLabel_Shape, 0, wx.ALL, 5)

        pca_GroupShapeChoices = []
        self.pca_GroupShape = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, pca_GroupShapeChoices, 0)
        self.pca_GroupShape.SetSelection(0)
        childPcaGroupSizer_Shape.Add(self.pca_GroupShape, 0, wx.ALL, 5)

        parentPcaSizer.Add(childPcaGroupSizer_Shape, 1, wx.EXPAND, 5)

        bSizer7 = wx.BoxSizer(wx.HORIZONTAL)

        self.pcaGroupLabel_Size = wx.StaticText(self, wx.ID_ANY, u"Set group size:", wx.DefaultPosition, wx.DefaultSize,
                                                0)
        self.pcaGroupLabel_Size.Wrap(-1)
        self.pcaGroupLabel_Size.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))

        bSizer7.Add(self.pcaGroupLabel_Size, 0, wx.ALL, 5)

        self.pca_GroupSize = wx.SpinCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                         wx.SP_ARROW_KEYS, 2, 36, 14)
        self.pca_GroupSize.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))

        bSizer7.Add(self.pca_GroupSize, 0, wx.ALL, 5)

        parentPcaSizer.Add(bSizer7, 1, wx.EXPAND, 5)

        parentPcaSizer.Add((0, 0), 1, wx.EXPAND, 5)

        childPcaGroupSizer_Buttons = wx.BoxSizer(wx.HORIZONTAL)

        self.pca_GroupAccept = wx.Button(self, wx.ID_ANY, u"Accept Changes", wx.DefaultPosition, wx.DefaultSize, 0)
        childPcaGroupSizer_Buttons.Add(self.pca_GroupAccept, 0, wx.ALL, 5)

        self.pca_GroupCancel = wx.Button(self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0)
        childPcaGroupSizer_Buttons.Add(self.pca_GroupCancel, 0, wx.ALL, 5)

        parentPcaSizer.Add(childPcaGroupSizer_Buttons, 1, wx.ALIGN_RIGHT, 5)

        self.SetSizer(parentPcaSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.pca_GroupName.Bind(wx.EVT_CHOICE, self.GroupChange)
        self.pca_GroupAccept.Bind(wx.EVT_BUTTON, self.AcceptChanges)
        self.pca_GroupCancel.Bind(wx.EVT_BUTTON, self.CancelChanges)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def GroupChange(self, event):
        event.Skip()

    def AcceptChanges(self, event):
        event.Skip()

    def CancelChanges(self, event):
        event.Skip()

    def OnClose(self, event):
        event.Skip()
