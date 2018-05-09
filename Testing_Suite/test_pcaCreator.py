import unittest
from fileManagement.pcaCreator import pcaCreator

class TestPCACreator(unittest.TestCase):

    def test_CountCols(self):
        # Test that it correctly counts the number of columns in a file
        self.assertEqual(pcaCreator.CountCols(self, "ExtraTestFiles/RandomFile.txt"), 3)
        self.assertEqual(pcaCreator.CountCols(self, "AdmixtureTestFiles/small.Q.5"), 5)
        self.assertEqual(pcaCreator.CountCols(self, "AdmixtureTestFiles/small.fam"), 6)
        self.assertEqual(pcaCreator.CountCols(self, "AdmixtureTestFiles/small.phe"), 6)
        self.assertEqual(pcaCreator.CountCols(self, "PCATestFiles/test_pca.pca.evec"), 12)

    def test_GetPcaCol(self):
        # Test that it correctly gets a column of data from a file, converts it to float data type and then appends it into a list to be returned
        # The first line in the file is skipped as those contain the eigen values.
        compareList = [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0]
        self.assertEqual(pcaCreator.GetPcaCol(self, "ExtraTestFiles/RandomFile.txt", 0, 15), compareList)
        self.assertEqual(pcaCreator.GetPcaCol(self, "PCATestFiles/test_pca.pca.evec", 3, 5), [0.0697, 0.0666, 0.0810, 0.0795])

    def test_GetPhenoCol(self):
        # Test that it correctly gets a column of data from a file then appends it into a list to be returned
        compareList = ['Kenan', 'Aimee', 'Dhevan', 'Regenesis', 'Professional', 'Practice']
        self.assertEqual(pcaCreator.GetPhenoCol(self, "ExtraTestFiles/RandomFile.txt", 1, 6), compareList)
        self.assertEqual(pcaCreator.GetPhenoCol(self, "AdmixtureTestFiles/small.Q.5", 2, 5), ['0.022254', '0.029752', '0.020280', '0.023803', '0.000010'])
        self.assertEqual(pcaCreator.GetPhenoCol(self, "AdmixtureTestFiles/small.phe", 1, 5), ['NA19916', 'NA19835', 'NA20282', 'NA19703', 'NA19901'])
        self.assertEqual(pcaCreator.GetPhenoCol(self, "PCATestFiles/test_pca.pca.evec", 0, 5),['#eigvals:', 'RYCS149:WITS149', 'RYCS2997:WITS2997', 'RYCS1122:WITS1122', 'RYCS1376:WITS1376'])
        self.assertEqual(pcaCreator.GetPhenoCol(self, "AdmixtureTestFiles/small.fam", 3, 5), ['0', '0', '0', '0', '0'])

    def test_GetIDs(self):
        # Test that it correctly gets the IDs in the first two columns, combines them into 1 string and then appends it into a list to be returned
        # The first line in the file is skipped as those contain the eigen values.
        compareList = ['RYCS149:WITS149', 'RYCS2997:WITS2997', 'RYCS1122:WITS1122', 'RYCS1376:WITS1376', 'RYCS446:WITS446']
        self.assertEqual(pcaCreator.GetIDs(self, "PCATestFiles/test_pca.pca.evec", 0, 6), compareList)

    def test_FindGroups(self):
        testList = ['Green', 'Green', 'Red', 'Blue', 'Green', 'Orange', 'Yellow', 'Blue', 'Red', 'Green', 'Yellow', 'Orange', 'Red', 'Red']
        self.assertEqual(pcaCreator.FindGroups(self, testList), ['Green', 'Red', 'Blue', 'Orange', 'Yellow'])

if __name__ == '__main__':
    unittest.main()