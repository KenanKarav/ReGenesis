import unittest
from fileManagement.admixCreator import admixCreator

class TestAdmixCreator(unittest.TestCase):

    def test_CountCols(self):
        # Test that it correctly counts the number of columns in a file
        self.assertEqual(admixCreator.CountCols(self, "ExtraTestFiles/RandomFile.txt"), 3)
        self.assertEqual(admixCreator.CountCols(self, "AdmixtureTestFiles/small.Q.5"), 5)
        self.assertEqual(admixCreator.CountCols(self, "AdmixtureTestFiles/small.fam"), 6)
        self.assertEqual(admixCreator.CountCols(self, "AdmixtureTestFiles/small.phe"), 6)
        self.assertEqual(admixCreator.CountCols(self, "PCATestFiles/test_pca.pca.evec"), 12)

    def test_GetAdmixColumn(self):
        # Test that it correctly gets a column of data from a file, converts it to float data type and then appends it into a list to be returned
        compareList = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0]
        self.assertEqual(admixCreator.GetAdmixColumn(self, "ExtraTestFiles/RandomFile.txt", 1, 15), compareList)
        self.assertEqual(admixCreator.GetAdmixColumn(self, "AdmixtureTestFiles/small.Q.5", 3, 5), [0.022254, 0.029752, 0.020280, 0.023803, 0.000010])

    def test_GetColumn(self):
        # Test that it correctly gets a column of data from a file then appends it into a list to be returned
        compareList = ['Kenan', 'Aimee', 'Dhevan', 'Regenesis', 'Professional', 'Practice']
        self.assertEqual(admixCreator.GetColumn(self, "ExtraTestFiles/RandomFile.txt", 2, 6), compareList)
        self.assertEqual(admixCreator.GetColumn(self, "AdmixtureTestFiles/small.Q.5", 3, 5), ['0.022254', '0.029752', '0.020280', '0.023803', '0.000010'])
        self.assertEqual(admixCreator.GetColumn(self, "AdmixtureTestFiles/small.phe", 2, 5), ['NA19916', 'NA19835', 'NA20282', 'NA19703', 'NA19901'])
        self.assertEqual(admixCreator.GetColumn(self, "PCATestFiles/test_pca.pca.evec", 1, 5), ['#eigvals:', 'RYCS149:WITS149', 'RYCS2997:WITS2997', 'RYCS1122:WITS1122', 'RYCS1376:WITS1376'])
        self.assertEqual(admixCreator.GetColumn(self, "AdmixtureTestFiles/small.fam", 4, 5), ['0', '0', '0', '0', '0'])

    def test_GetIDs(self):
        # Test that it correctly gets the IDs in the first two columns, combines them into 1 string and then appends it into a list to be returned
        compareList = ['2431:NA19916', '2424:NA19835', '2469:NA20282', '2368:NA19703', '2425:NA19901']
        self.assertEqual(admixCreator.GetIDs(self, "AdmixtureTestFiles/small.fam", 5), compareList)
        self.assertEqual(admixCreator.GetIDs(self, "AdmixtureTestFiles/small.phe", 5), compareList)

    def test_FindGroups(self):
        testList = ['Green', 'Green', 'Red', 'Blue', 'Green', 'Orange', 'Yellow', 'Blue', 'Red', 'Green', 'Yellow', 'Orange', 'Red', 'Red']
        self.assertEqual(admixCreator.FindGroups(self, testList), ['Green', 'Red', 'Blue', 'Orange', 'Yellow'])

if __name__ == '__main__':
    unittest.main()