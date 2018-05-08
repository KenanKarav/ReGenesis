import unittest
from fileManagement.fileImporter import fileImporter
import os

class TestFileImporter(unittest.TestCase):

    def test_FileLength(self):
        # Test the file lengths of a textfile of random words, a PCA file and an admixture file

        self.assertEqual(fileImporter.FileLength(self, "ExtraTestFiles/RandomFile.txt"), 15)
        self.assertEqual(fileImporter.FileLength(self, "PCATestFiles/test_pca.pca.evec"), 684)
        self.assertEqual(fileImporter.FileLength(self, "AdmixtureTestFiles/small.Q.5"), 1197)


    def test_GenDataList(self):
        # Test first and last line of each file is correctly read and appended into a list

        dataList = fileImporter.GenDataList(self, "ExtraTestFiles/RandomFile.txt" , 15)
        self.assertEqual(dataList[0], ['1', 'Kenan', 'Green'])
        self.assertEqual(dataList[14], ['15', 'Potato', 'Gold'])

        dataList = fileImporter.GenDataList(self, "PCATestFiles/test_pca.pca.evec", 684)
        self.assertEqual(dataList[0], ['#eigvals:', '66.890', '6.188', '4.056', '2.156', '1.929', '1.924', '1.913', '1.910', '1.901', '1.890'])
        self.assertEqual(dataList[683], ['NA19323:NA19323', '-0.0185', '-0.0189', '-0.0025', '0.0538', '0.0011', '0.0007', '0.0035', '-0.0043', '-0.0031', '0.0018', 'Control'])

        dataList = fileImporter.GenDataList(self, "AdmixtureTestFiles/small.Q.5", 1197)
        self.assertEqual(dataList[0], ['0.113654', '0.862588', '0.022254', '0.000010', '0.001494'])
        self.assertEqual(dataList[1196], ['0.000010', '0.972970', '0.003395', '0.023616', '0.000010'])

    def test_ValidateFile(self):
        # Test that the files are correctly validated as True

        self.assertTrue(fileImporter.ValidateFile(self, 'Admixture', "AdmixtureTestFiles/small.Q.5"))
        self.assertTrue(fileImporter.ValidateFile(self, 'Fam', "AdmixtureTestFiles/small.fam"))
        self.assertTrue(fileImporter.ValidateFile(self, 'Phenotype', "AdmixtureTestFiles/small.phe"))
        self.assertTrue(fileImporter.ValidateFile(self, 'PCA', "PCATestFiles/test_pca.pca.evec"))

        # Test that the files are correctly validated as False

        self.assertFalse(fileImporter.ValidateFile(self, 'Admixture', "AdmixtureTestFiles/small.fam"))
        self.assertFalse(fileImporter.ValidateFile(self, 'Fam', "PCATestFiles/test_pca.pca.evec"))
        self.assertFalse(fileImporter.ValidateFile(self, 'Phenotype', "AdmixtureTestFiles/small.Q.5"))
        self.assertFalse(fileImporter.ValidateFile(self, 'PCA', "AdmixtureTestFiles/small.phe"))

    def test_ImportFile(self):
        # Test that a file is correctly imported and its relevant data is stored correctly in a dictionary

        dataDict = fileImporter.ImportFile(fileImporter, "AdmixtureTestFiles/small.Q.5")
        dataList = fileImporter.GenDataList(fileImporter, "AdmixtureTestFiles/small.Q.5", 1197)
        self.assertEqual(dataDict, {'fileName':'small.Q.5', 'fileType':'Admixture', 'data':dataList})

        dataDict = fileImporter.ImportFile(fileImporter, "AdmixtureTestFiles/small.fam")
        dataList = fileImporter.GenDataList(fileImporter, "AdmixtureTestFiles/small.fam", 1197)
        self.assertEqual(dataDict, {'fileName':'small.fam', 'fileType':'Fam', 'data':dataList})

        dataDict = fileImporter.ImportFile(fileImporter, "AdmixtureTestFiles/small.phe")
        dataList = fileImporter.GenDataList(fileImporter, "AdmixtureTestFiles/small.phe", 1197)
        self.assertEqual(dataDict, {'fileName':'small.phe', 'fileType':"Phenotype", 'data':dataList})

        dataDict = fileImporter.ImportFile(fileImporter, "PCATestFiles/test_pca.pca.evec")
        dataList = fileImporter.GenDataList(fileImporter, "PCATestFiles/test_pca.pca.evec", 684)
        self.assertEqual(dataDict, {'fileName':'test_pca.pca.evec', 'fileType':'PCA', 'data':dataList})

if __name__ == '__main__':
    unittest.main()



