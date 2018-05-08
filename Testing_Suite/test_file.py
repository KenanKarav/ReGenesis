import unittest
from fileManagement.file import File

class TestFile(unittest.TestCase):

    def setUp(self):
        self.myFile1 = File('Dhev', 'Admixture', [1,2,3,4])
        self.myFile2 = File('Aimee', 'PCA', ['poop', 'oop' , 'pop', 'popo'])
        self.myFile3 = File('Kenan', 'Fam', [True,False,False,True])
        self.myFile4 = File('Regenesis', 'Phenotype', {"Key" : "Value"})


    def test_fileName(self):
        self.assertEqual(self.myFile1.getfilename(), 'Dhev')
        self.assertEqual(self.myFile2.getfilename(), 'Aimee')
        self.assertEqual(self.myFile3.getfilename(), 'Kenan')
        self.assertEqual(self.myFile4.getfilename(), 'Regenesis')

    def test_fileType(self):
        self.assertEqual(self.myFile1.getfiletype(), 'Admixture')
        self.assertEqual(self.myFile2.getfiletype(), 'PCA')
        self.assertEqual(self.myFile3.getfiletype(), 'Fam')
        self.assertEqual(self.myFile4.getfiletype(), 'Phenotype')

    def test_fileData(self):
        self.assertEqual(self.myFile1.getdata(), [1,2,3,4])
        self.assertEqual(self.myFile2.getdata(), ['poop', 'oop' , 'pop', 'popo'])
        self.assertEqual(self.myFile3.getdata(), [True,False,False,True])
        self.assertEqual(self.myFile4.getdata(), {"Key" : "Value"})

if __name__ == '__main__':
    unittest.main()