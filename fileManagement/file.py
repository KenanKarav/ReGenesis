

from enum import Enum


class FileType(Enum):
    Admixture = "Admixture"
    PCA = "PCA"
    Phenotype = "Phenotype"

    def valid(self, filetype):

        if filetype == self.Admixture or filetype == self.PCA or filetype == self.Phenotype:
            return True

        return False


class File:

    def __init__(self, filename, filetype, data):
        self.fileName = filename
        if FileType.valid(filetype):
            self.fileType = filetype
        else:
            raise ValueError("Invalid FileType found: %s" % filetype)
        self.Data = data

    def getfilename(self):
        return self.fileName

    def getfilename(self):
        return self.fileType

    def getdata(self):
        return self.Data

