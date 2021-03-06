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
## Class pca_Frame
###########################################################################

class pca_Frame(wx.Dialog):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"PCA Creator", pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.Bind(wx.EVT_CLOSE, self.OnClose)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))
        self.SetBackgroundColour(wx.Colour(239, 239, 239))

        pca_ParentSizer = wx.BoxSizer(wx.VERTICAL)

        pcaBoxSizer_PcaImport = wx.BoxSizer(wx.HORIZONTAL)

        self.pca_label1 = wx.StaticText(self, wx.ID_ANY, u"Import PCA file", wx.DefaultPosition, wx.DefaultSize, 0)
        self.pca_label1.Wrap(-1)
        self.pca_label1.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))
        self.pca_label1.SetBackgroundColour(wx.Colour(240, 240, 240))

        pcaBoxSizer_PcaImport.Add(self.pca_label1, 0, wx.ALL, 5)

        self.pca_pcaImport = wx.FilePickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*",
                                               wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE)
        pcaBoxSizer_PcaImport.Add(self.pca_pcaImport, 0, wx.ALL, 5)

        pca_ParentSizer.Add(pcaBoxSizer_PcaImport, 1, wx.EXPAND, 5)

        pcaBoxSizer_PcaChoice = wx.BoxSizer(wx.HORIZONTAL)

        self.pca_label2 = wx.StaticText(self, wx.ID_ANY, u"Select PCA columns:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.pca_label2.Wrap(-1)
        self.pca_label2.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))
        self.pca_label2.SetBackgroundColour(wx.Colour(240, 240, 240))
        self.pca_label2.Enable(False)

        pcaBoxSizer_PcaChoice.Add(self.pca_label2, 0, wx.ALL, 5)

        pca_col1Choices = []
        self.pca_col1 = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, pca_col1Choices, 0)
        self.pca_col1.SetSelection(0)
        self.pca_col1.Enable(False)

        pcaBoxSizer_PcaChoice.Add(self.pca_col1, 0, wx.ALL, 5)

        pca_col2Choices = []
        self.pca_col2 = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, pca_col2Choices, 0)
        self.pca_col2.SetSelection(0)
        self.pca_col2.Enable(False)

        pcaBoxSizer_PcaChoice.Add(self.pca_col2, 0, wx.ALL, 5)

        pca_col3Choices = []
        self.pca_col3 = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, pca_col3Choices, 0)
        self.pca_col3.SetSelection(0)
        self.pca_col3.Enable(False)

        pcaBoxSizer_PcaChoice.Add(self.pca_col3, 0, wx.ALL, 5)

        pca_ParentSizer.Add(pcaBoxSizer_PcaChoice, 1, wx.EXPAND, 5)

        pcaBoxSizer_PhenoImport = wx.BoxSizer(wx.HORIZONTAL)

        self.pca_label3 = wx.StaticText(self, wx.ID_ANY, u"Import Phenotype file (optional):", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.pca_label3.Wrap(-1)
        self.pca_label3.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))
        self.pca_label3.SetBackgroundColour(wx.Colour(240, 240, 240))
        self.pca_label3.Enable(False)

        pcaBoxSizer_PhenoImport.Add(self.pca_label3, 0, wx.ALL, 5)

        self.pca_phenoImport = wx.FilePickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*",
                                                 wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE)
        self.pca_phenoImport.Enable(False)

        pcaBoxSizer_PhenoImport.Add(self.pca_phenoImport, 0, wx.ALL, 5)

        pca_ParentSizer.Add(pcaBoxSizer_PhenoImport, 1, wx.EXPAND, 5)

        pcaBoxSizer_phenoChoice = wx.BoxSizer(wx.HORIZONTAL)

        self.pca_label4 = wx.StaticText(self, wx.ID_ANY, u"Which column represents the grouping?", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.pca_label4.Wrap(-1)
        self.pca_label4.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))
        self.pca_label4.SetBackgroundColour(wx.Colour(240, 240, 240))
        self.pca_label4.Enable(False)

        pcaBoxSizer_phenoChoice.Add(self.pca_label4, 0, wx.ALL, 5)

        pca_phenoChoiceChoices = []
        self.pca_phenoChoice = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, pca_phenoChoiceChoices, 0)
        self.pca_phenoChoice.SetSelection(0)
        self.pca_phenoChoice.Enable(False)

        pcaBoxSizer_phenoChoice.Add(self.pca_phenoChoice, 0, wx.ALL, 5)

        pca_ParentSizer.Add(pcaBoxSizer_phenoChoice, 1, wx.EXPAND, 5)

        pcaBoxSizer_Buttons = wx.BoxSizer(wx.HORIZONTAL)

        self.pca_Confirm = wx.Button(self, wx.ID_ANY, u"Confirm", wx.DefaultPosition, wx.DefaultSize, 0)
        self.pca_Confirm.Enable(False)

        pcaBoxSizer_Buttons.Add(self.pca_Confirm, 0, wx.ALL | wx.ALIGN_BOTTOM, 5)

        self.pca_Reset = wx.Button(self, wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.DefaultSize, 0)
        pcaBoxSizer_Buttons.Add(self.pca_Reset, 0, wx.ALL | wx.ALIGN_BOTTOM, 5)

        self.pca_Cancel = wx.Button(self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0)
        pcaBoxSizer_Buttons.Add(self.pca_Cancel, 0, wx.ALL | wx.ALIGN_BOTTOM, 5)

        pca_ParentSizer.Add(pcaBoxSizer_Buttons, 1, wx.ALIGN_RIGHT, 5)

        self.SetSizer(pca_ParentSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.pca_pcaImport.Bind(wx.EVT_FILEPICKER_CHANGED, self.ImportPcaFile)
        self.pca_col1.Bind(wx.EVT_CHOICE, self.PcaChoiceChange)
        self.pca_col2.Bind(wx.EVT_CHOICE, self.PcaChoiceChange)
        self.pca_col3.Bind(wx.EVT_CHOICE, self.PcaChoiceChange)
        self.pca_phenoImport.Bind(wx.EVT_FILEPICKER_CHANGED, self.ImportPhenoFile)
        self.pca_Confirm.Bind(wx.EVT_BUTTON, self.Confirm)
        self.pca_Reset.Bind(wx.EVT_BUTTON, self.Reset)
        self.pca_Cancel.Bind(wx.EVT_BUTTON, self.Cancel)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def ImportPcaFile(self, event):
        event.Skip()

    def PcaChoiceChange(self, event):
        event.Skip()

    def ImportPhenoFile(self, event):
        event.Skip()

    def Confirm(self, event):
        event.Skip()

    def Reset(self, event):
        event.Skip()

    def Cancel(self, event):
        event.Skip()

    def OnClose(self, event):
        event.Skip()


