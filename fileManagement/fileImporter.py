import pyforms
from pyforms            import BaseWidget
from pyforms.controls   import ControlButton
from pyforms.controls   import ControlFile

import os



class fileImporter(BaseWidget):

    def __init__(self):
        super(fileImporter,self).__init__('Import File')

        #Definitions of the form fields
        self._controlFile = ControlFile('Import File')
        self._buttonCancel = ControlButton('Cancel')
        self._buttonDone = ControlButton('Done')

        #Define the button actions
        self._buttonCancel.value = self.__buttonCancelAction
        self._buttonDone.value = self.buttonDoneAction

        #Define the organisation of the forms
        self.formset = [' ',' ',(' ','_controlFile',' '),'=',' ',(' ',' ',' ',' ','_buttonCancel','_buttonDone',' '),' ']

    #counting the columns
    def __countCols(self, filePath):
        self._file = open(filePath)
        self._file.readline()
        self._list = self._file.readline().split()
        self._file.close()
        return len(self._list)
    
    #counting number of lines in file
    def __fileLength(self, filePath):
        self._file = open(filePath)
        for i, line in enumerate(self._file):
            pass
        self._file.close()
        return i + 1

    #generating a list of lists from data in file
    #each sublist is a row in the file
    def __genDataList(self, filePath, length):
        self._file = open(filePath)
        dataList = []
        for i in range(0, length):
            tempList = self._file.readline().split()
            dataList.append(tempList)
        self._file.close()
        return dataList
    
    def __buttonCancelAction(self):
        self.close()

    def Test(self):
        return 'hi, I work'

    def buttonDoneAction(self):
        #extracting the data file name(incl. extension) from the path
        self._filePath = self._controlFile.value
        self._fileName = os.path.basename(self._filePath)

        #determining the file type
        self._isPca = self._fileName.find(".pca.evec")
        self._isAdmix = self._fileName.find(".Q.")
        self._isFam = self._fileName.find(".fam")
        self._isPheno = self._fileName.find(".phe")
        if self._isPca > -1:
            self._fileType = 'PCA'
        elif self._isAdmix > -1:
            self._fileType = 'Admixture'
        elif self._isFam > -1:
            self._fileType = 'Fam'
        elif self._isPheno > -1:
            self._fileType = 'Phenotype'
        else:
            raise ValueError('Invalid file type selected')
        
        #calculating file length
        self._length = self.__fileLength(self._filePath)

        #generating list of data from file
        self._dataList = self.__genDataList(self._filePath, self._length)

        #defining dictionary of data
        self.dataDictionary = {
            'fileName': self._fileName,
            'fileType': self._fileType,
            'data': self._dataList
            }
        pcaCreator.Test(self)
        fileImporter.value = self.dataDictionary
       # return self.dataDictionary


from fileManagement.pcaCreator import pcaCreator
#Execute the application
if __name__ == "__main__": pyforms.start_app(fileImporter, geometry=(500,300,400,100))
#setting geometry: first two = x and y pos, second two = x and y size

