import wx

from Test.pcaCreatorGUI import *

from fileManagement.fileImporter import fileImporter


class pcaCreator(MyFrame1):

    def __init__(self, parent):
        MyFrame1.__init__(self, parent)
        self._isPheno = False

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
            self._phenoData = fileImporter.ImportFile(fileImporter, self._phenoFilePath)

            # populate the phenotype choice boxes
            self._phenoNumCols = self.__countCols(self._phenoFilePath)

            for x in range(1, self._phenoNumCols):
                self.pca_phenoChoice.Append('Column ' + str(x))

            self.pca_phenoChoice.SetSelection(0)

            self._isPheno = True

    def Cancel(self, event):
        # close the window
        app.ExitMainLoop()

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
        '''
        self._numLines = self.__fileLength(self._pcaFilePath)

        self._num1 = self.pca_col1.Selection +1
        self._num2 = self.pca_col2.Selection +1

        self._zVals = None
        if self.pca_col3.Selection >-1:
            self._num3 = self.pca_col3.Selection+1
            self._zVals = self.__getCol('PCA',self._pcaFilePath, self._num3, self._numLines)

        self._xVals = self.__getCol('PCA',self._pcaFilePath, self._num1, self._numLines)
        self._yVals = self.__getCol('PCA',self._pcaFilePath, self._num2, self._numLines)
        if not self._isPheno:
            #return file object
            return self._xVals, self._yVals, self._zVals
        else:
            # retrieving IDs from PCA file
            self._pcaIDs = self.__getIDs(self._pcaFilePath, 0, self._numLines)

            # extracting the Pheno data
            self._num = self.pca_phenoChoice.Selection +1
            self._numLines = self.__fileLength(self._phenoFilePath)
            # put pheno data into a dictionary with key=ID and value=column
            # store all pca data IDs in a list, loop through checking for the position of the ID in the phenotype file
            # plot each group seperately

            tempID_1 = self.__getCol('Phenotype', self._phenoFilePath, 0, self._numLines)
            tempID_2 = self.__getCol('Phenotype', self._phenoFilePath, 1, self._numLines)
            self._phenoIDs = []

            for i in range(self._numLines):
                self._phenoIDs.append(tempID_1[i] + ':' + tempID_2[i])

            # retrieving data from chosen phenotype column and storing in list
            self._phenoData = self.__getCol('Phenotype', self._phenoFilePath, self._num - 1, self._numLines)
            self._phenoDict = {}
            for i in range(self._numLines):
                self._phenoDict.update({self._phenoIDs[i]: self._phenoData[i]})

            # determining how many different groups exist and storing groups in a list
            self._pcaGroups = self.__findGroups(self._phenoData)

            # looping through all the groups
            for numGroups in range(len(self._pcaGroups)):
                tempX = []
                tempY = []
                for numLines in range(len(self._pcaIDs)):
                    # if the ID from the pca file exists in the phenotype file
                    if self._pcaIDs[numLines] in self._phenoDict:
                        # if the key value matches the current group we are searching for..
                        if self._phenoDict.get(self._pcaIDs[numLines]) == self._pcaGroups[numGroups]:
                            tempX.append(self._xVals[numLines])
                            tempY.append(self._yVals[numLines])

        '''

        # counting the columns
    def __countCols(self, filePath):
        self._file = open(filePath)
        self._file.readline()
        self._list = self._file.readline().split()
        self._file.close()
        return len(self._list)

    def __getCol(self, fileType, filePath, colNum, numLines):
        self._realList = []
        file = open(filePath)
        if fileType == 'PCA':
            file.readline()
        for i in range(numLines-1):
            tempList = file.readline().split()
            self._realList.append(float(tempList[colNum]))
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
    # counting the columns
    '''
    def __countCols(self, filePath):
        self._file = open(filePath)
        self._file.readline()
        self._list = self._file.readline().split()
        self._file.close()
        return len(self._list)

    # counting number of lines in file
    def __fileLength(self, filePath):
        self._file = open(filePath)
        for i, line in enumerate(self._file):
            pass
        self._file.close()
        return i + 1

    # retrieving a column of text from a file and returning it as a list
    def __getCol(self, filePath, colNum, numLines):
        self._realList = []
        file = open(filePath)
        file.readline()
        for i in range(numLines - 1):
            tempList = file.readline().split()
            self._realList.append(float(tempList[colNum]))
        file.close()
        return self._realList

    def __getIDs(self, filePath, colNum, numLines):
        self._realList = []
        file = open(filePath)
        file.readline()
        for i in range(numLines - 1):
            tempList = file.readline().split()
            self._realList.append(tempList[colNum])
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

    def Test(self):
        print("POOP")
        self.importedData = self.dataDictionary
        pcaCreator().pcaFile.value = 'working'
        pcaCreator()._buttonConfirm.enabled = True
        print("Working??")
        print(self.importedData)
        #self._pcaFile.value = "POOP"

    def wait_for_event(e):
        while True:
            print('/tTHREAD: this is the thread speaking, we are waiting for the event to start')
            event_is_set = e.wait()
            print('/tTHREAD: Yaaaay we got a signal     :   %s',event_is_set)
            e.clear()

    def __buttonImportAction(self):

        # opens the fileImporter
        #self.Test()
        win = fileImporter()
        win.parent = pcaCreator()
        print('hi')
        #win.value = None
        win.show()
        #return None
        #time.sleep(4)
        #print("hello")
       # win.close()
       # while (win.value == None):
       #     pass
       # print(win.value)
       # win.close()
       # Data = win.buttonDoneAction()
       # win.close()

      #  self._pcaFile.value = Data


        
        if not self._phenoFile.enabled:
            self._pcaFilePath = self._pcaFile.value
            self._numCols = self.__countCols(self._pcaFilePath)

            for i in range(1, self._numCols - 1):
                self._pca1.add_item('PCA ' + str(i))
                self._pca2.add_item('PCA ' + str(i))

            self._pca1.enabled = True
            self._pca2.enabled = True
            self._pcaFile.enabled = False
            self._phenoFile.enabled = True

        else:
            if self._phenoFile.value == '':
                self._phenoCombo.enabled = True
                self._buttonDone.enabled = True
                self._phenoFile.enabled = False
                self._plotPheno = False
            else:
                self._phenoFilePath = self._phenoFile.value
                self._numCols = self.__countCols(self._phenoFilePath)

                for i in range(1, self._numCols + 1):
                    self._phenoCombo.add_item('Column ' + str(i))

                self._phenoCombo.enabled = True
                self._buttonDone.enabled = True
                self._phenoFile.enabled = False

                self._plotPheno = True
                

    # plotting graph from combo boxes
    def __buttonDoneAction(self):
        
        # extracting PCA data info
        tempList = self._pca1.value.split()
        self._num1 = int(tempList[1])

        tempList = self._pca2.value.split()
        self._num2 = int(tempList[1])

        self._numLines = self.__fileLength(self._pcaFilePath)
        self._xVals = self.__getCol(self._pcaFilePath, self._num1, self._numLines)
        self._yVals = self.__getCol(self._pcaFilePath, self._num2, self._numLines)
        if not self._plotPheno:
            # plotting the graph
            ##plt.clf()
            plt.scatter(self._xVals, self._yVals, color='r', s=1)

            plt.xlabel(self._pca1.value)
            plt.ylabel(self._pca2.value)
            plt.title('PCA Plot')

            plt.show()
        else:
            # retrieving IDs from PCA file
            self._pcaIDs = self.__getIDs(self._pcaFilePath, int('0'), self._numLines)

            # extracting the Pheno data
            tempList = self._phenoCombo.value.split()
            self._num = int(tempList[1])

            self._numLines = self.__fileLength(self._phenoFilePath)
            # put pheno data into a dictionary with key=ID and value=column
            # store all pca data IDs in a list, loop through checking for the position of the ID in the phenotype file
            # plot each group seperately

            tempID_1 = self.__getPhenoCol(self._phenoFilePath, int('0'), self._numLines)
            tempID_2 = self.__getPhenoCol(self._phenoFilePath, int('1'), self._numLines)
            self._phenoIDs = []

            for i in range(self._numLines):
                self._phenoIDs.append(tempID_1[i] + ':' + tempID_2[i])

            # retrieving data from chosen phenotype column and storing in list
            self._phenoData = self.__getPhenoCol(self._phenoFilePath, self._num - 1, self._numLines)
            self._phenoDict = {}
            for i in range(self._numLines):
                self._phenoDict.update({self._phenoIDs[i]: self._phenoData[i]})

            # determining how many different groups exist and storing groups in a list
            self._pcaGroups = self.__findGroups(self._phenoData)

            # looping through all the groups
            for numGroups in range(len(self._pcaGroups)):
                tempX = []
                tempY = []
                for numLines in range(len(self._pcaIDs)):
                    # if the ID from the pca file exists in the phenotype file
                    if self._pcaIDs[numLines] in self._phenoDict:
                        # if the key value matches the current group we are searching for..
                        if self._phenoDict.get(self._pcaIDs[numLines]) == self._pcaGroups[numGroups]:
                            tempX.append(self._xVals[numLines])
                            tempY.append(self._yVals[numLines])
                # plotting the graph
                if len(tempX) > 0:
                    ##plt.clf()
                    plt.scatter(tempX, tempY, label=self._pcaGroups[numGroups], s=1)

            # plotting the graph
            # plt.scatter(self._xVals, self._yVals, label='lolol I hope this works', color='r',s=1)

            plt.xlabel(self._pca1.value)
            plt.ylabel(self._pca2.value)
            plt.title('PCA Plot')
            plt.legend()

            plt.show()
            

     
    e = threading.Event()
    t = threading.Thread(name='test_thread', target=wait_for_event, args=(e,))
    t.start()

    while True:
        print('MAIN LOOP: still in the main loop..')
        time.sleep(4)
        print('MAIN LOOP: I just set the flag..')
        e.set()
        print('MAIN LOOP: now I\'m gonna do some processing')
        time.sleep(4)
        print('MAIN LOOP: ... more processing ...')
        time.sleep(4)
        print('MAIN LOOP: okay ready, soon we will repeat the loop..')
        time.sleep(2)
        print('DONE')
        '''

# Execute the application
#if __name__ == "__main__": pyforms.start_app(pcaCreator, geometry=(500,300,310,100))#, geometry=(500, 300, 100, 400))
# setting geometry: first two = x and y pos, second two = x and y size
app = wx.App(False)
frame = pcaCreator(None)
frame.Show(True)

app.MainLoop()