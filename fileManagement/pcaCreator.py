from fileManagement.pcaCreatorGUI import *

from fileManagement.fileImporter import fileImporter
from fileManagement.file import *

class pcaCreator(pca_Frame):

    def __init__(self, parent):
        pca_Frame.__init__(self, parent)
        self._isPheno = False
        self._parent = parent
        self.dimension = 2
        self.result = ""

        # the third PCA column selector is hidden because the 3D plotting functionality has not yet been implemented
        # majority of the code for the third pca column selector still exists and will be used when the program is expanded upon
        self.pca_col3.Hide()

    def ImportPcaFile( self, event ):
        """
        Import the PCA file

        Validate the file.
        Enable the column selector.
        Run the file importer.
        Populate the pca choice boxes with the column options.
        """

        #run the file validity checker
        self._pcaFilePath = self.pca_pcaImport.Path
        self._isValid = fileImporter.ValidateFile(fileImporter, 'PCA', self._pcaFilePath)
        if self._isValid == False:
            errDlg = wx.MessageDialog(parent=self, message="Please select a valid file type", caption="Invalid file chosen", style=wx.ICON_ERROR)
            val = errDlg.ShowModal()
            errDlg.Show()
            self.pca_pcaImport.Path = ''

        else:
            # enable the pcaColumn selector GUI
            self.pca_label2.Enable()
            self.pca_col1.Enable()
            self.pca_col2.Enable()
            self.pca_col3.Enable()

            # enable the phenotype file selector
            self.pca_label3.Enable()
            self.pca_phenoImport.Enable()

            # enable the confirm button
            self.pca_Confirm.Enable()

            # run the file importer
            self._pcaData = {}
            self._pcaData = fileImporter.ImportFile(fileImporter, self._pcaFilePath)

            # populate the pca choice boxes
            self._pcaNumCols = self.CountCols(self._pcaFilePath)

            for x in range(1, self._pcaNumCols-1):
                self.pca_col1.Append('Column ' + str(x))
                self.pca_col2.Append('Column ' + str(x))
                self.pca_col3.Append('Column ' + str(x))

            self.pca_col1.SetSelection(0)
            self.pca_col2.SetSelection(1)

    def ImportPhenoFile(self, event):
        """
        Import the phenotype file

        Validate the file.
        Enable the column selector.
        Run the file importer.
        Populate the phenotype choice boxes with the column options.
        """
        # run the file validity checker
        self._phenoFilePath = self.pca_phenoImport.Path
        self._isValid = fileImporter.ValidateFile(fileImporter, 'Phenotype', self._phenoFilePath)
        if self._isValid == False:
            errDlg = wx.MessageDialog(parent=self, message="Please select a valid file type",
                                      caption="Invalid file chosen", style=wx.ICON_ERROR)
            val = errDlg.ShowModal()
            errDlg.Show()
            self.pca_phenoImport.Path = ''

        else:
            #enable the pheno column selector
            self.pca_phenoChoice.Enable()
            self.pca_label4.Enable()

            # run the file importer
            self._phenoData = fileImporter.ImportFile(fileImporter, self._phenoFilePath)


            # populate the phenotype choice boxes
            self._phenoNumCols = self.CountCols(self._phenoFilePath)

            for x in range(1, self._phenoNumCols+1):
                self.pca_phenoChoice.Append('Column ' + str(x))

            self.pca_phenoChoice.SetSelection(0)

            self._isPheno = True

    def Cancel(self, event):
        """
        Close the window and enable the parent window.
        """

        self.result = "CANCEL"
        self._parent.Enable()
        self._parent.Show()
        self.Close()

    def Reset(self, event):
        """
        Reset the form to its original state.
        """

        self.pca_pcaImport.Path = ''
        self.pca_phenoImport.Path = ''

        self.pca_label2.Disable()
        self.pca_col1.Clear()
        self.pca_col1.Disable()

        self.pca_col2.Clear()
        self.pca_col2.Disable()

        self.pca_col3.Clear()
        self.pca_col3.Disable()

        self.pca_phenoChoice.Clear()
        self.pca_phenoChoice.Disable()

        self.pca_label3.Disable()
        self.pca_phenoImport.Disable()

        self.pca_label4.Disable()
        self.pca_Confirm.Disable()

        self._isPheno = False

    def Confirm(self, event):
        """
        User confirms selections.

        Extract PCA data information.
        Store PCA information in dictionary.
        Check if phenotype exists.
        Store pca data and phenotype data in the dictionary if it exists.
        """

        # extracting PCA data info
        self.result = "CONFIRM"
        self._numLines = self.FileLength(self._pcaFilePath)

        self._num1 = self.pca_col1.Selection +1
        self._num2 = self.pca_col2.Selection +1

        self._zVals = None
        if self.pca_col3.Selection >-1:
            self._num3 = self.pca_col3.Selection+1
            self._zVals = self.GetPcaCol(self._pcaFilePath, self._num3, self._numLines)
            self.dimension = 3
        self._xVals = self.GetPcaCol(self._pcaFilePath, self._num1, self._numLines)
        self._yVals = self.GetPcaCol(self._pcaFilePath, self._num2, self._numLines)

        self._pcaIDs = self.GetIDs(self._pcaFilePath, 0, self._numLines)

        self._pcaFile = File(self._pcaData['fileName'], self._pcaData['fileType'], self._pcaData['data'])

        self._dataDict = {
            'PcaFile' : self._pcaFile,
            'PcaIDs' : self._pcaIDs,
            'xLabel': "PCA "+str(self._num1),
            'yLabel': "PCA "+str(self._num2),
            'hasGrid': 1,
            'hasLabels': 1,
            'x' : self._xVals,
            'y' : self._yVals,
            'z' : self._zVals,
            'dimension' : self.dimension
        }
        if not self._isPheno:
            self._parent.Enable()
            self._parent.Show()
            self.Close()
        else:
            # retrieving IDs from PCA file
            self._pcaIDs = self.GetIDs(self._pcaFilePath, 0, self._numLines)

            # extracting the Pheno data
            self._num = self.pca_phenoChoice.Selection
            self._numLines = self.FileLength(self._phenoFilePath)

            tempID_1 = self.GetPhenoCol( self._phenoFilePath, 0, self._numLines)
            tempID_2 = self.GetPhenoCol(self._phenoFilePath, 1, self._numLines)
            self._phenoIDs = []

            for i in range(self._numLines):
                self._phenoIDs.append(tempID_1[i] + ':' + tempID_2[i])

            # retrieving data from chosen phenotype column and storing in list
            self._phenoCol = self.GetPhenoCol(self._phenoFilePath, self._num, self._numLines)


            #updating phenotype dictionary
            self._phenoFile = File(self._phenoData['fileName'], self._phenoData['fileType'], self._phenoData['data'])
            self._dataDict.update({
                'PhenoFile' : self._phenoFile,
                'PhenoIDs' : self._phenoIDs,
                'PhenoColumn' : self._phenoCol
            })
            self._parent.Enable()
            self._parent.Show()
            self.Close()

        # counting the columns
    def CountCols(self, filePath):
        self._file = open(filePath)
        self._file.readline()
        self._list = self._file.readline().split()
        self._file.close()
        return len(self._list)

    def GetPcaCol(self, filePath, colNum, numLines):
        self._realList = []
        file = open(filePath)
        file.readline()
        for i in range(numLines-1):
            tempList = file.readline().split()
            self._realList.append(float(tempList[colNum]))
        file.close()
        return self._realList

    def GetPhenoCol(self, filePath, colNum, numLines):
        self._realList = []
        file = open(filePath)
        for i in range(numLines):
            tempList = file.readline().split()
            self._realList.append(tempList[colNum])
        file.close()
        return self._realList

        # counting number of lines in file
    def FileLength(self, filePath):
        self._file = open(filePath)
        for i, line in enumerate(self._file):
            pass
        self._file.close()
        return i + 1

    def GetIDs(self, filePath, colNum, numLines):
        self._realList = []
        file = open(filePath)
        file.readline()
        for i in range(numLines-1):
            tempList = file.readline().split()
            self._realList.append(tempList[colNum])
        file.close()
        return self._realList

    # finds and stores each group from a list in a seperate list
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


