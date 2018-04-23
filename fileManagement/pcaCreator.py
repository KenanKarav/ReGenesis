import matplotlib.pyplot as plt

import pyforms
from pyforms import BaseWidget
from pyforms.controls import ControlCombo
from pyforms.controls import ControlButton
from pyforms.controls import ControlLabel

from fileManagement.fileImporter import fileImporter


class pcaCreator(BaseWidget):

    def __init__(self):

        super(pcaCreator, self).__init__('PCA Creator')

        # definitions of the forms fields
        # PCA
        self._pcaLabel = ControlLabel('Import PCA file:')
        self._pcaButtonImport = ControlButton('Import')
        self._pcaFile = ControlLabel('')
        self._selectPCACols = ControlLabel('Select PCA columns:')
        self._pca1 = ControlCombo('')
        self._pca2 = ControlCombo('')
        self._pca3= ControlCombo('')

        # Phenotype
        self._phenoLabel = ControlLabel('Import phenotype file (optional):')
        self._phenoButtonImport = ControlButton('Import')
        self._phenoFile = ControlLabel('')
        self._selectPhenoCol = ControlCombo('Which column represents the grouping?')

        #bottom buttons
        self._buttonCancel = ControlButton('Cancel')
        self._buttonReset = ControlButton('Reset')
        self._buttonConfirm = ControlButton('Confirm')

        # Define the button actions
        self._pcaButtonImport.value = self.__buttonImportAction
        self._phenoButtonImport.value = self.__buttonImportAction

        self._buttonCancel.value = self.__buttonCancelAction
        self._buttonReset.value = self.__buttonResetAction
        self._buttonConfirm.value = self.__buttonDoneAction


        # Disabling elements
        self._selectPCACols.enabled = False
        self._pca1.enabled = False
        self._pca2.enabled = False
        self._pca3.enabled = False
        self._selectPhenoCol.enabled = False
        self._buttonConfirm.enabled = False


        # define the organisation of the forms
        self.formset = [' ',('_pcaLabel','_pcaButtonImport',' '),
                        '=',('_pcaFile',' '),
                        '=',('_selectPCACols',' '),
                        '=',('_pca1','_pca2','_pca3',' '),
                        '=','=','=','=','=',('_phenoLabel','||','_phenoButtonImport',' '),
                        '=',('_phenoFile',' '),
                        '=',('_selectPhenoCol',' '),
                        '=','=','=','=','=',('_buttonCancel','_buttonReset','_buttonConfirm',' '),
                        '=',' ']

    #closing the form
    def __buttonCancelAction(self):
        pass

    # reseting the form
    def __buttonResetAction(self):
        pass

        '''
        self._buttonDone.enabled = False
        self._pcaFile.enabled = True
        self._phenoFile.enabled = False
        self._pca1.enabled = False
        self._pca2.enabled = False
        self._phenoCombo.enabled = False

        self._pca1.clear()
        self._pca2.clear()
        self._phenoCombo.clear()

        self._pca1.value = ''
        self._pca2.value = ''
        self._phenoCombo.value = ''
        self._pcaFile.value = ''
        self._phenoFile.value = ''
        '''

    # counting the columns
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
        pass
        #self._pcaFile.value = fileImporter.dataDictionary[0]

    def __buttonImportAction(self):
        # opens the fileImporter
        win = fileImporter()
        win.parent = pcaCreator
        print('hi')
        win.value = None
        win.show()
       # while (win.value == None):
       #     pass
       # print(win.value)
       # win.close()
       # Data = win.buttonDoneAction()
       # win.close()

      #  self._pcaFile.value = Data


        '''
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
                '''

    # plotting graph from combo boxes
    def __buttonDoneAction(self):
        '''
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
            '''


# Execute the application
if __name__ == "__main__": pyforms.start_app(pcaCreator, geometry=(500,300,310,100))#, geometry=(500, 300, 100, 400))
# setting geometry: first two = x and y pos, second two = x and y size
