from fileManagement.admixCreatorGUI import *

from fileManagement.fileImporter import fileImporter
from fileManagement.file import *

class admixCreator(AdmixFrame):

    def __init__(self, parent):
        AdmixFrame.__init__(self, parent)
        self.__isPheno = False
        self._parent = parent
        self.result = ""

    def OnFileChange_ImportDataFile(self, event):
        #Validate Imported File
        self._admixFilePath = self.filePicker_DataFile.Path
        self._isValid = fileImporter.ValidateFile(fileImporter, 'Admixture', self._admixFilePath)
        if self._isValid == False:
            errorDialog = wx.MessageDialog(parent=self, message="Please select a valid file type", caption="Invalid file chosen", style=wx.ICON_ERROR)
            val = errorDialog.ShowModal()
            errorDialog.Show()
            self.filePicker_DataFile.Path = ''

        else:
            #Enable FAM File Picker
            self.filePicker_FamFile.Enable()
            self.lbl_ImportFamFile.Enable()

            #Run File Importer
            self._admixData = {}
            self._admixData = fileImporter.ImportFile(fileImporter, self._admixFilePath)

    def OnFileChange_ImportFamFile(self, event):
        #Validate Imported File
        self._famFilePath = self.filePicker_FamFile.Path
        self._isValid = fileImporter.ValidateFile(fileImporter, 'Fam', self._famFilePath)
        if self._isValid == False:
            errorDialog = wx.MessageDialog(parent=self, message="Please select a valid file type", caption="Invalid file chosen", style=wx.ICON_ERROR)
            val = errorDialog.ShowModal()
            errorDialog.Show()
            self.filePicker_FamFile.Path = ''

            #Incase the user chooses an invalid file after they have chosen a correct one
            self.lbl_ColumnRepresent.Disable()
            self.choiceBox_PheColumn.Clear()
            self.choiceBox_PheColumn.Disable()
            self.filePicker_PheFile.Disable()
            self.lbl_ImportPheFile.Disable()
            self.btn_Confirm.Disable()

        else:
            #Enable FAM File Picker
            self.filePicker_PheFile.Enable()
            self.lbl_ImportPheFile.Enable()
            self.btn_Confirm.Enable()

    def OnFileChange_ImportPhenoFile(self, event):
        #Validate Imported File
        self._pheFilePath = self.filePicker_PheFile.Path
        self._isValid = fileImporter.ValidateFile(fileImporter, 'Phenotype', self._pheFilePath)
        if self._isValid == False:
            errorDialog = wx.MessageDialog(parent=self, message="Please select a valid file type", caption="Invalid file chosen", style=wx.ICON_ERROR)
            val = errorDialog.ShowModal()
            errorDialog.Show()
            self.filePicker_PheFile.Path = ''

            # Incase the user chooses an invalid file after they have chosen a correct one
            self.lbl_ColumnRepresent.Disable()
            self.choiceBox_PheColumn.Clear()
            self.choiceBox_PheColumn.Disable()

        else:
            #Enable Phenotype Column Chooser
            self.choiceBox_PheColumn.Enable()
            self.lbl_ColumnRepresent.Enable()

            #Run File Importer
            self._phenoData = fileImporter.ImportFile(fileImporter, self._pheFilePath)
            #print(self._phenoData)

            #Populate Phenotype Choice Boxes
            self._phenoNumCols = self.CountCols(self._pheFilePath)

            for x in range(1, self._phenoNumCols+1):
                self.choiceBox_PheColumn.Append('Column ' + str(x))

            self.choiceBox_PheColumn.SetSelection(0)
            self.__isPheno = True

    def OnBtnClick_Cancel(self, event):
        self.result = "CANCEL"
        self._parent.Enable()
        self._parent.Show()
        self.Close()

    def OnBtnClick_Reset(self, event):
        #Clear All Text Fields
        self.filePicker_DataFile.Path = ''
        self.filePicker_FamFile.Path = ''
        self.filePicker_PheFile.Path = ''
        self.choiceBox_PheColumn.Clear()

        #Disable The Appropriate Components
        self.filePicker_FamFile.Disable()
        self.lbl_ImportFamFile.Disable()
        self.filePicker_PheFile.Disable()
        self.lbl_ImportPheFile.Disable()
        self.lbl_ColumnRepresent.Disable()
        self.btn_Confirm.Disable()

        self.__isPheno = False

    def OnBtnClick_Confirm(self, event):
        self.result = "CONFIRM"
        self._numLines = self.FileLength(self._admixFilePath)
        self._admixIDs = self.GetIDs(self._famFilePath, self._numLines)

        self._admixFile = File(self._admixData['fileName'], self._admixData['fileType'], self._admixData['data'])

        self._dataDict = {
            'AdmixFile': self._admixFile,
            'AdmixIDs': self._admixIDs
        }

        numColumns = self.CountCols(self._admixFilePath)
        # Count the amount of ancestries and update the data dictionary as required.
        for i in range(1, numColumns+1):
            ancestryKey = 'Ancestry'+str(i)
            self._dataDict.update({
                ancestryKey : self.GetAdmixColumn(self._admixFilePath,i,self._numLines)
            })


        if not self.__isPheno:
            self._parent.Enable()
            self._parent.Show()
            self.Close()

        else:
            #Retrieving Pheno Column Selection
            self._num = self.choiceBox_PheColumn.Selection
            self._numLines = self.FileLength(self._pheFilePath)
            # store all admix data IDs in a list, loop through checking for the position of the ID in the phenotype file
            # plot each group seperately
            self._phenoIDs= []
            self._phenoIDs = self.GetIDs(self._pheFilePath, self._numLines)

            # retrieving data from chosen phenotype column and storing in list
            print(type(self._phenoData))
            self._phenoCol = self.GetColumn(self._pheFilePath, self._num+1, self._numLines)
            print(type(self._phenoData))

            self._phenoFile = File(self._phenoData['fileName'], self._phenoData['fileType'], self._phenoData['data'])
            self._dataDict.update({
                'PhenoFile' : self._phenoFile,
                'PhenoIDs' : self._phenoIDs,
                'PhenoColumn' : self._phenoCol
            })
            self._parent.Enable()
            self._parent.Show()
            self.Close()

        self._parent.Enable()
        self._parent.Show()
        self.Close()


    """
    Count total number of columns
    """
    def CountCols(self, filePath):
        self._file = open(filePath)
        self._file.readline()
        self._list = self._file.readline().split()
        self._file.close()
        return len(self._list)

    """
    Get a single column of data and convert it to float data type
    """
    def GetAdmixColumn(self, filePath, colNum, numLines):
        self._realList = []
        file = open(filePath)
        for i in range(numLines):
            tempList = file.readline().split()
            self._realList.append(float(tempList[colNum-1]))
        file.close()
        return self._realList

    """
    Get a single column of data
    """
    def GetColumn(self, filePath, colNum, numLines):
        self._realList = []
        file = open(filePath)
        for i in range(numLines):
            tempList = file.readline().split()
            self._realList.append(tempList[colNum-1])
        file.close()
        return self._realList

    """
    counting number of lines in file
    """
    def FileLength(self, filePath):
        self._file = open(filePath)
        for i, line in enumerate(self._file):
            pass
        self._file.close()
        return i + 1


    """
    Get the IDs which are the first two columns in the Fam file
    """
    def GetIDs(self, filePath, numLines):
        self._realList = []
        file = open(filePath)
        for i in range(numLines):
            tempList = file.readline().split()
            self._realList.append(tempList[0]+':'+tempList[1])
        file.close()
        return self._realList
    """
    Finds and stores each group from a list in a separate list
    """
    def FindGroups(self, dataList):
        groupList = []
        for i in range(len(dataList)):
            data = dataList[i]
            if data in groupList:
                pass
            else:
                groupList.append(data)
        return groupList

    def OnClose(self,event):
        self._parent.Enable()
        self.Destroy()


