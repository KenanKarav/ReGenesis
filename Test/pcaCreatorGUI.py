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
## Class MyFrame1
###########################################################################

class MyFrame1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"PCA Creator", pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))
        self.SetBackgroundColour(wx.Colour(239, 239, 239))

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.pca_label1 = wx.StaticText(self, wx.ID_ANY, u"Import PCA file", wx.DefaultPosition, wx.DefaultSize, 0)
        self.pca_label1.Wrap(-1)
        self.pca_label1.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))
        self.pca_label1.SetBackgroundColour(wx.Colour(240, 240, 240))

        bSizer2.Add(self.pca_label1, 0, wx.ALL, 5)

        self.pca_pcaImport = wx.FilePickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*",
                                               wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE)
        bSizer2.Add(self.pca_pcaImport, 0, wx.ALL, 5)

        bSizer1.Add(bSizer2, 1, wx.EXPAND, 5)

        bSizer3 = wx.BoxSizer(wx.HORIZONTAL)

        self.pca_label2 = wx.StaticText(self, wx.ID_ANY, u"Select PCA columns:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.pca_label2.Wrap(-1)
        self.pca_label2.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))
        self.pca_label2.SetBackgroundColour(wx.Colour(240, 240, 240))
        self.pca_label2.Enable(False)

        bSizer3.Add(self.pca_label2, 0, wx.ALL, 5)

        pca_col1Choices = []
        self.pca_col1 = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, pca_col1Choices, 0)
        self.pca_col1.SetSelection(0)
        self.pca_col1.Enable(False)

        bSizer3.Add(self.pca_col1, 0, wx.ALL, 5)

        pca_col2Choices = []
        self.pca_col2 = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, pca_col2Choices, 0)
        self.pca_col2.SetSelection(0)
        self.pca_col2.Enable(False)

        bSizer3.Add(self.pca_col2, 0, wx.ALL, 5)

        pca_col3Choices = []
        self.pca_col3 = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, pca_col3Choices, 0)
        self.pca_col3.SetSelection(0)
        self.pca_col3.Enable(False)

        bSizer3.Add(self.pca_col3, 0, wx.ALL, 5)

        bSizer1.Add(bSizer3, 1, wx.EXPAND, 5)

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.pca_label3 = wx.StaticText(self, wx.ID_ANY, u"Import Phenotype file (optional):", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.pca_label3.Wrap(-1)
        self.pca_label3.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))
        self.pca_label3.SetBackgroundColour(wx.Colour(240, 240, 240))
        self.pca_label3.Enable(False)

        bSizer4.Add(self.pca_label3, 0, wx.ALL, 5)

        self.pca_phenoImport = wx.FilePickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*",
                                                 wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE)
        self.pca_phenoImport.Enable(False)

        bSizer4.Add(self.pca_phenoImport, 0, wx.ALL, 5)

        bSizer1.Add(bSizer4, 1, wx.EXPAND, 5)

        bSizer5 = wx.BoxSizer(wx.HORIZONTAL)

        self.pca_label4 = wx.StaticText(self, wx.ID_ANY, u"Which column represents the grouping?", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.pca_label4.Wrap(-1)
        self.pca_label4.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))
        self.pca_label4.SetBackgroundColour(wx.Colour(240, 240, 240))
        self.pca_label4.Enable(False)

        bSizer5.Add(self.pca_label4, 0, wx.ALL, 5)

        pca_phenoChoiceChoices = []
        self.pca_phenoChoice = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, pca_phenoChoiceChoices, 0)
        self.pca_phenoChoice.SetSelection(0)
        self.pca_phenoChoice.Enable(False)

        bSizer5.Add(self.pca_phenoChoice, 0, wx.ALL, 5)

        bSizer1.Add(bSizer5, 1, wx.EXPAND, 5)

        bSizer6 = wx.BoxSizer(wx.HORIZONTAL)

        self.pca_Cancel = wx.Button(self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer6.Add(self.pca_Cancel, 0, wx.ALL | wx.ALIGN_BOTTOM, 5)

        self.pca_Reset = wx.Button(self, wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer6.Add(self.pca_Reset, 0, wx.ALL | wx.ALIGN_BOTTOM, 5)

        self.pca_Confirm = wx.Button(self, wx.ID_ANY, u"Confirm", wx.DefaultPosition, wx.DefaultSize, 0)
        self.pca_Confirm.Enable(False)

        bSizer6.Add(self.pca_Confirm, 0, wx.ALL | wx.ALIGN_BOTTOM, 5)

        bSizer1.Add(bSizer6, 1, wx.ALIGN_RIGHT, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.pca_pcaImport.Bind(wx.EVT_FILEPICKER_CHANGED, self.ImportPcaFile)
        self.pca_col1.Bind(wx.EVT_CHOICE, self.PcaChoiceChange)
        self.pca_col2.Bind(wx.EVT_CHOICE, self.PcaChoiceChange)
        self.pca_col3.Bind(wx.EVT_CHOICE, self.PcaChoiceChange)
        self.pca_phenoImport.Bind(wx.EVT_FILEPICKER_CHANGED, self.ImportPhenoFile)
        self.pca_Cancel.Bind(wx.EVT_BUTTON, self.Cancel)
        self.pca_Reset.Bind(wx.EVT_BUTTON, self.Reset)
        self.pca_Confirm.Bind(wx.EVT_BUTTON, self.Confirm)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def ImportPcaFile(self, event):
        event.Skip()

    def PcaChoiceChange(self, event):
        event.Skip()

    def ImportPhenoFile(self, event):
        event.Skip()

    def Cancel(self, event):
        event.Skip()

    def Reset(self, event):
        event.Skip()

    def Confirm(self, event):
        event.Skip()


