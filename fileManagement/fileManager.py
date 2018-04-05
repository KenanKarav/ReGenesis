from fileManagement.file import File


class FileManager:

    def __init__(self):
        self.files = list < File > []

    def listfiles(self):

        filenames = [file.getfilename() for file in self.files]
        return filenames

    def findfile(self, filename):

        for file in self.files:
            if filename == file.getfilename():
                return file

        return "%s File Not Found" % filename

    def getfiledata(self, filename):

        file = self.findfile(filename)
        return file.getfiledata()

    def addfile(self, file):

        self.files.__add__(file)

