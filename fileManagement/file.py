

from enum import Enum


FILETYPES = ["Admixture", "PCA", "Phenotype"]


def valid(filetype):

    if filetype in FILETYPES:
        return True

    return False


class File:

    def __init__(self, filename, filetype, data):
        self.fileName = filename
        if valid(filetype):
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

