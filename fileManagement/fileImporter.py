import pyforms
from pyforms            import BaseWidget
from pyforms.controls   import ControlButton
from pyforms.controls   import ControlFile

import os

import numpy as np

import csv

class fileImporter(BaseWidget):

    def __init__(self):
        super(fileImporter,self).__init__('Input Files')
        
        #Definitions of the forms fields
        self._dataFile = ControlFile('Import Data File')
        self._famFile = ControlFile('Import Fam File(Admix only)')
        self._phenoFile = ControlFile('Import Phenotype File (optional)')
        self._buttonDone = ControlButton('Done')
        self._buttonImport = ControlButton('Import File')
        self._buttonRedo = ControlButton('Redo Importing')

        #disabling gui elements
        self._famFile.enabled = False
        self._phenoFile.enabled = False
        self._buttonDone.enabled = False

        #initialising booleans
        self._isDataImported = True
        self._isFamImported = False
        self._isPhenoImported = False
        
        #Define the button actions
        self._buttonImport.value = self.__buttonImportAction
        self._buttonDone.value = self.__buttonDoneAction
        self._buttonRedo.value = self.__buttonRedoAction

        #define the organisation of the forms
        self.formset = [' ',(' ', '_dataFile', ' '),'=',(' ', '_famFile', ' '),'=',(' ', '_phenoFile', ' '),'=','=','=',(' ','_buttonRedo','_buttonImport','_buttonDone',' '),' ']
    
    #counting the columns
    def __countCols(self, filePath):
        self._file = open(filePath)
        self._file.readline()
        self._list = self._file.readline().split()
        return len(self._list)
    
    #counting number of lines in file
    def __fileLength(self, filePath):
        self._file = open(filePath)
        for i, line in enumerate(self._file):
            pass
        return i + 1

    #generating a list of lists from data in file
    #each sublist is a row in the file
    def __genDataList(self, filePath, length):
        self._file = open(filePath)
        dataList = []
        for i in range(0, length):
            tempList = self._file.readline().split()
            dataList.append(tempList)
        return dataList

    def __buttonRedoAction(self):
        #disabling gui elements
        self._dataFile.enabled = True
        self._famFile.enabled = False
        self._phenoFile.enabled = False
        self._buttonDone.enabled = False
        self._buttonImport.enabled = True

        #initialising booleans
        self._isDataImported = True
        self._isFamImported = False
        self._isPhenoImported = False

        #clearing the fields
        self._dataFile.value = ''
        self._famFile.value = ''
        self._phenoFile.value = ''
    
    def __buttonImportAction(self):
        """Button action event"""
        if self._isDataImported:
            ##PCA OR ADMIX##
            #extracting the data file name(incl. extension) from the path
            self._fileDataPath = self._dataFile.value
            self._fileDataName = os.path.basename(self._fileDataPath)
            
            #string handling to check if the file chosen is valid (pca or admix)
            #only checking the file extension for now
            self._isPca = self._fileDataName.find(".pca.evec")
            self._isAdmix = self._fileDataName.find(".Q.")       
            if self._isPca > -1:
                #setting file type
                self._fileType = 'PCA'
                
                #opening the file
                self._pcaFile = open(self._fileDataPath)

                #calculating file length
                self._length = self.__fileLength(self._fileDataPath)

                #generating list of data
                self._dataList = self.__genDataList(self._fileDataPath, self._length)

                self._dataFile.enabled = False
                self._phenoFile.enabled = True
                self._isDataImported = False
                self._isPhenoImported = True

                #closing the file
                self._pcaFile.close()

                #defining dictionary of data
                self._dataDictionary = {
                    'fileName': self._fileDataName,
                    'fileType': self._fileType,
                    'data': self._dataList
                    }
                return self._dataDictionary
            
            elif self._isAdmix > -1:
                #setting file type
                self._fileType = 'Admixture'
                
                #opening the file
                self._admixFile = open(self._fileDataPath)

                #calculating file length
                self._length = self.__fileLength(self._fileDataPath)

                #generating list of data
                self._dataList = self.__genDataList(self._fileDataPath, self._length)

                self._dataFile.enabled = False
                self._isDataImported = False
                self._famFile.enabled = True
                self._isFamImported = True

                #closing the file
                self._admixFile.close()

                #defining dictionary of data
                self._dataDictionary = {
                    'fileName': self._fileDataName,
                    'fileType': self._fileType,
                    'data': self._dataList
                    }
                return self._dataDictionary
                
            else:
                #print('Invalid File Selected. Please select either an Admixture or PCA file.')
                self._dataFile.value=''
                
        elif self._isFamImported:
            ##FAM##
            #extracting the data file name(incl. extension) from the path
            self._fileFamPath = self._famFile.value
            self._fileFamName = os.path.basename(self._fileFamPath)

            #string handling to check if the file chosen is a fam type
            self._isFam = self._fileFamName.find(".fam")
            if self._isFam > -1:
                self._fileType = 'Fam'
                
                #opening the file
                self._FamFile = open(self._fileFamPath)

                #calculating file length
                self._length = self.__fileLength(self._fileFamPath)

                #generating list of data
                self._famDataList = self.__genDataList(self._fileFamPath, self._length)

                self._famFile.enabled = False
                self._phenoFile.enabled = True
                self._isPhenoImported = True
                self._isFamImported = False

                #closing the file
                self._FamFile.close()
                
                #defining dictionary of data
                self._dataDictionary = {
                    'fileName': self._fileFamName,
                    'fileType': self._fileType,
                    'data': self._dataList
                    }
                return self._dataDictionary
            else:
                #print('Invalid File Selected. Please select a Fam file.')
                self._famFile.value=''

        elif self._isPhenoImported:
            ##PHENOTYPE##
            #extracting the pheno file name(incl. extension) from the path
            self._filePhenoPath = self._phenoFile.value
            self._filePhenoName = os.path.basename(self._filePhenoPath)

            #string handling to check if the file chosen is a phenotype
            self._isPheno = self._filePhenoName.find(".phe")
            if self._isPheno > -1:
                #setting the file type
                self._fileType='Phenotype'
                
                #opening the file
                self._PhenoFile = open(self._filePhenoPath)

                #calculating file length
                self._length = self.__fileLength(self._filePhenoPath)

                #generating list of data
                self._phenoDataList = self.__genDataList(self._filePhenoPath, self._length)

                self._phenoFile.enabled = False
                self._buttonDone.enabled = True
                self._buttonImport.enabled = False

                #closing the file
                self._PhenoFile.close()
 
                #defining dictionary of data
                self._dataDictionary = {
                    'fileName': self._filePhenoName,
                    'fileType': self._fileType,
                    'data': self._dataList
                    }
                return self._dataDictionary
                
            elif self._phenoFile.value == '':
                #no phenotype file was chosen
                self._phenoFile.enabled = False
                self._buttonDone.enabled = True
                self._buttonImport.enabled = False
            else:
                #print('Invalid File Selected. Please select a Phenotype file.')
                self._phenoFile.value=''
        
    def __buttonDoneAction(self):
        """Button action event"""
        #this button will move to the next screen
        pass
        
        
        
#Execute the application
if __name__ == "__main__": pyforms.start_app(fileImporter, geometry=(500,300,600,300))
#setting geometry: first two = x and y pos, second two = x and y size
