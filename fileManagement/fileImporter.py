import os

class fileImporter():

    def __init__(self):
        pass



        # counting number of lines in file
    def __fileLength(self, filePath):
        self._file = open(filePath)
        for i, line in enumerate(self._file):
            pass
        self._file.close()
        return i + 1

        # generating a list of lists from data in file
        # each sublist is a row in the file
    def __genDataList(self, filePath, length):
        self._file = open(filePath)
        dataList = []
        for i in range(0, length):
            tempList = self._file.readline().split()
            dataList.append(tempList)
        self._file.close()
        return dataList

    def ValidateFile(self, fileType, filePath):
        # extracting file name with extension
        self._fileName = os.path.basename(filePath)

        # determining the file type
        self._isPca = self._fileName.find(".evec")
        self._isAdmix = self._fileName.find(".Q.")
        self._isFam = self._fileName.find(".fam")
        self._isPheno = self._fileName.find(".phe")
        if self._isPca > -1:
            if fileType == 'PCA':
                self._fileType = fileType
                return True
            else:
                return False

        elif self._isAdmix > -1:
            if fileType == 'Admixture':
                self._fileType = fileType
                return True
            else:
                return False

        elif self._isFam > -1:
            if fileType == 'Fam':
                self._fileType = fileType
                return True
            else:
                return False

        elif self._isPheno > -1:
            if fileType == 'Phenotype':
                self._fileType = fileType
                return True
            else:
                return False

        else:
            return False

    def ImportFile(self, filePath):
        # calculating file length
        self._length = self.__fileLength(self, filePath)

        # generating list of data from file
        self._dataList = self.__genDataList(self, filePath, self._length)

        # defining dictionary of data
        self._dataDictionary = {
            'fileName': self._fileName,
            'fileType': self._fileType,
            'data': self._dataList
        }
        return self._dataDictionary
