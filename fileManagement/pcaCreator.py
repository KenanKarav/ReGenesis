from fileManagement.pcaCreatorGUI import *

from fileManagement.fileImporter import fileImporter
from fileManagement.file import *

class pcaCreator(MyFrame1):

    def __init__(self, parent):
        MyFrame1.__init__(self, parent)
        self._isPheno = False
        self._parent = parent
    def ImportPcaFile( self, event ):
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
            self._pcaNumCols = self.__countCols(self._pcaFilePath)

            for x in range(1, self._pcaNumCols-1):
                self.pca_col1.Append('Column ' + str(x))
                self.pca_col2.Append('Column ' + str(x))
                self.pca_col3.Append('Column ' + str(x))

            self.pca_col1.SetSelection(0)
            self.pca_col2.SetSelection(1)

    # ensuring that the same column cannot be chosen twice
    def PcaChoiceChange(self, event):
       '''
       num1 = self.pca_col1.Selection +1
        num2 = self.pca_col2.Selection +1
        num3 = self.pca_col3.Selection +1
        print(num1)
        print(num2)
        print(num3)
        self.pca_col1.Clear()
        self.pca_col2.Clear()
        self.pca_col3.Clear()
        for x in range(1, self._pcaNumCols - 1):
            if x != num2 and x != num3:
                self.pca_col1.Append('Column ' + str(x))
            if x != num1 and x != num3:
                self.pca_col2.Append('Column ' + str(x))
            if x != num1 and x != num2:
                self.pca_col3.Append('Column ' + str(x))
        self.pca_col1.SetSelection(num1-1)
        self.pca_col2.SetSelection(num2-1)
        self.pca_col3.SetSelection(num3-1)
        '''

    def ImportPhenoFile(self, event):
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
            #self._phenoData = {}
            self._phenoData = fileImporter.ImportFile(fileImporter, self._phenoFilePath)
            print(type(self._phenoData))

            # populate the phenotype choice boxes
            self._phenoNumCols = self.__countCols(self._phenoFilePath)

            for x in range(1, self._phenoNumCols+1):
                self.pca_phenoChoice.Append('Column ' + str(x))

            self.pca_phenoChoice.SetSelection(0)

            self._isPheno = True

    def Cancel(self, event):
        # close the window
        self._parent.Enable()
        self._parent.Show()
        self.Close()

    def Reset(self, event):
        #reset the form to its original state
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
        self.pca_label4.Disable()
        self.pca_Confirm.Disable()

        self._isPheno = False

    def Confirm(self, event):
        # extracting PCA data info
        self._numLines = self.__fileLength(self._pcaFilePath)

        self._num1 = self.pca_col1.Selection +1
        self._num2 = self.pca_col2.Selection +1

        self._zVals = None
        if self.pca_col3.Selection >-1:
            self._num3 = self.pca_col3.Selection+1
            self._zVals = self.__getPcaCol(self._pcaFilePath, self._num3, self._numLines)

        self._xVals = self.__getPcaCol(self._pcaFilePath, self._num1, self._numLines)
        self._yVals = self.__getPcaCol(self._pcaFilePath, self._num2, self._numLines)

        self._pcaIDs = self.__getIDs(self._pcaFilePath, 0, self._numLines)

        self._pcaFile = File(self._pcaData['fileName'], self._pcaData['fileType'], self._pcaData['data'])
        self._dataDict = {
            'PcaFile' : self._pcaFile,
            'PcaIDs' : self._pcaIDs,
            'x' : self._xVals,
            'y' : self._yVals,
            'z' : self._zVals

        }
        if not self._isPheno:
            #return file object
            return self._dataDict
        else:
            # retrieving IDs from PCA file
            self._pcaIDs = self.__getIDs(self._pcaFilePath, 0, self._numLines)

            # extracting the Pheno data
            self._num = self.pca_phenoChoice.Selection
            self._numLines = self.__fileLength(self._phenoFilePath)
            # put pheno data into a dictionary with key=ID and value=column
            # store all pca data IDs in a list, loop through checking for the position of the ID in the phenotype file
            # plot each group seperately

            tempID_1 = self.__getIDs( self._phenoFilePath, 0, self._numLines)
            tempID_2 = self.__getIDs(self._phenoFilePath, 1, self._numLines)
            self._phenoIDs = []

            for i in range(self._numLines-1):
                self._phenoIDs.append(tempID_1[i] + ':' + tempID_2[i])

            # retrieving data from chosen phenotype column and storing in list
            print(type(self._phenoData))
            self._phenoCol = self.__getPhenoCol(self._phenoFilePath, self._num, self._numLines)
            print(type(self._phenoData))


            self._phenoFile = File(self._phenoData['fileName'], self._phenoData['fileType'], self._phenoData['data'])
            self._dataDict.update({
                'PhenoFile' : self._phenoFile,
                'PhenoIDs' : self._phenoIDs,
                'PhenoColumn' : self._phenoCol
            })

            return  self._dataDict

        # counting the columns
    def __countCols(self, filePath):
        self._file = open(filePath)
        self._file.readline()
        self._list = self._file.readline().split()
        self._file.close()
        return len(self._list)

    def __getPcaCol(self, filePath, colNum, numLines):
        self._realList = []
        file = open(filePath)
        file.readline()
        for i in range(numLines-1):
            tempList = file.readline().split()
            self._realList.append(float(tempList[colNum]))
        file.close()
        return self._realList

    def __getPhenoCol(self, filePath, colNum, numLines):
        self._realList = []
        file = open(filePath)
        for i in range(numLines):
            tempList = file.readline().split()
            self._realList.append(tempList[colNum])
        file.close()
        return self._realList

        # counting number of lines in file
    def __fileLength(self, filePath):
        self._file = open(filePath)
        for i, line in enumerate(self._file):
            pass
        self._file.close()
        return i + 1

    def __getIDs(self, filePath, colNum, numLines):
        self._realList = []
        file = open(filePath)
        file.readline()
        for i in range(numLines-1):
            tempList = file.readline().split()
            self._realList.append(tempList[colNum])
        file.close()
        return self._realList

    # finds and stores each group from a list in a seperate list
    def __findGroups(self, dataList):
        groupList = []
        for i in range(len(dataList)):
            data = dataList[i]
            if data in groupList:
                pass
            else:
                groupList.append(data)
        return groupList


