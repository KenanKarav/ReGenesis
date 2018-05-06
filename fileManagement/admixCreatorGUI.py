# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class AdmixFrame
###########################################################################

class AdmixFrame(wx.Dialog):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Admix Creator", pos=wx.DefaultPosition,
                          size=wx.Size(573, 286), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        bSizer3 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_ImportDataFile = wx.StaticText(self, wx.ID_ANY, u"Import Data File", wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        self.lbl_ImportDataFile.Wrap(-1)
        bSizer3.Add(self.lbl_ImportDataFile, 0, wx.ALL, 5)

        self.filePicker_DataFile = wx.FilePickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*",
                                                     wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE)
        bSizer3.Add(self.filePicker_DataFile, 0, wx.ALL, 5)

        bSizer2.Add(bSizer3, 0, wx.ALL, 0)

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_ImportFamFile = wx.StaticText(self, wx.ID_ANY, u"Import FAM File", wx.DefaultPosition, wx.DefaultSize,
                                               0)
        self.lbl_ImportFamFile.Wrap(-1)
        self.lbl_ImportFamFile.Enable(False)

        bSizer4.Add(self.lbl_ImportFamFile, 0, wx.ALL, 5)

        self.filePicker_FamFile = wx.FilePickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*",
                                                    wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE)
        self.filePicker_FamFile.Enable(False)

        bSizer4.Add(self.filePicker_FamFile, 0, wx.ALL, 5)

        bSizer2.Add(bSizer4, 0, wx.ALL, 0)

        bSizer5 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_ImportPheFile = wx.StaticText(self, wx.ID_ANY, u"Import Phenotype File (Optional)", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        self.lbl_ImportPheFile.Wrap(-1)
        self.lbl_ImportPheFile.Enable(False)

        bSizer5.Add(self.lbl_ImportPheFile, 0, wx.ALL, 5)

        self.filePicker_PheFile = wx.FilePickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*",
                                                    wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE)
        self.filePicker_PheFile.Enable(False)

        bSizer5.Add(self.filePicker_PheFile, 0, wx.ALL, 5)

        bSizer2.Add(bSizer5, 0, wx.ALL, 0)

        bSizer6 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_ColumnRepresent = wx.StaticText(self, wx.ID_ANY, u"Choose which column represents the phenotype data",
                                                 wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_ColumnRepresent.Wrap(-1)
        self.lbl_ColumnRepresent.Enable(False)

        bSizer6.Add(self.lbl_ColumnRepresent, 0, wx.ALL, 5)

        choiceBox_PheColumnChoices = []
        self.choiceBox_PheColumn = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                             choiceBox_PheColumnChoices, 0)
        self.choiceBox_PheColumn.SetSelection(0)
        self.choiceBox_PheColumn.Enable(False)

        bSizer6.Add(self.choiceBox_PheColumn, 0, wx.ALL, 5)

        bSizer2.Add(bSizer6, 1, wx.ALL | wx.EXPAND, 0)

        bSizer9 = wx.BoxSizer(wx.HORIZONTAL)

        self.btn_Confirm = wx.Button(self, wx.ID_ANY, u"Confirm", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btn_Confirm.Enable(False)

        bSizer9.Add(self.btn_Confirm, 0, wx.ALL, 5)

        self.btn_Reset = wx.Button(self, wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer9.Add(self.btn_Reset, 0, wx.ALL, 5)

        self.btn_Cancel = wx.Button(self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer9.Add(self.btn_Cancel, 0, wx.ALL, 5)

        bSizer2.Add(bSizer9, 0, wx.ALIGN_RIGHT | wx.ALL, 0)

        self.SetSizer(bSizer2)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.filePicker_DataFile.Bind(wx.EVT_FILEPICKER_CHANGED, self.OnFileChange_ImportDataFile)
        self.filePicker_FamFile.Bind(wx.EVT_FILEPICKER_CHANGED, self.OnFileChange_ImportFamFile)
        self.filePicker_PheFile.Bind(wx.EVT_FILEPICKER_CHANGED, self.OnFileChange_ImportPhenoFile)
        self.choiceBox_PheColumn.Bind(wx.EVT_CHOICE, self.OnChoice_PhenoColRep)
        self.btn_Confirm.Bind(wx.EVT_BUTTON, self.OnBtnClick_Confirm)
        self.btn_Reset.Bind(wx.EVT_BUTTON, self.OnBtnClick_Reset)
        self.btn_Cancel.Bind(wx.EVT_BUTTON, self.OnBtnClick_Cancel)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def OnFileChange_ImportDataFile(self, event):
        event.Skip()

    def OnFileChange_ImportFamFile(self, event):
        event.Skip()

    def OnFileChange_ImportPhenoFile(self, event):
        event.Skip()

    def OnChoice_PhenoColRep(self, event):
        event.Skip()

    def OnBtnClick_Confirm(self, event):
        event.Skip()

    def OnBtnClick_Reset(self, event):
        event.Skip()

    def OnBtnClick_Cancel(self, event):
        event.Skip()


