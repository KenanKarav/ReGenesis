import unittest
from graphDrawing.graphs.admixtureGraph.admixtureGraph import admixtureGraph

class TestAdmixGraph(unittest.TestCase):

    def setUp(self):
        testDict = {'AdmixFile' : None, 'AdmixIDs' : ['ID1', 'ID2', 'ID3'], 'Ancestry1' : [0.33, 0.48, 0.58], 'Ancestry2' : [0.60, 0.22, 0.24], 'Ancestry3' : [0.07, 0.30, 0.18]
                    , 'PhenoFile' : None, 'PhenoIDs' : ['ID1', 'ID2', 'ID3'], 'PhenoColumn' : ['Green', 'Blue', 'Green']}
        self.myGraph = admixtureGraph(testDict)

    def test_GetAdmixIDs(self):
        self.assertEqual(self.myGraph.getAdmixIDs(),  ['ID1', 'ID2', 'ID3'])

    def test_GetAncestry(self):
        tempDict = self.myGraph.getAncestryDict()
        self.assertEqual(tempDict, {'Ancestry1' : [0.33, 0.48, 0.58], 'Ancestry2' : [0.60, 0.22, 0.24], 'Ancestry3' : [0.07, 0.30, 0.18]})

    def test_GetNumAncestries(self):
        self.assertEqual(self.myGraph.getNumAncestries(), 3)

    def test_GetPhenoDict(self):
        tempDict = self.myGraph.getPhenoDict()
        self.assertEqual(tempDict, {'ID1' : 'Green','ID2' : 'Blue', 'ID3' : 'Green'})

    def  test_GetGroupList(self):
        self.assertEqual(self.myGraph.getGroupList(),['Green', 'Blue'])

    def test_GenGroupDictionary(self):
        tempDict = self.myGraph.genDataDictionary()
        self.assertEqual(self.myGraph.genDataDictionary(),{'Green':{'Ancestry1':[0.33, 0.58], 'Ancestry2':[0.60,0.24], 'Ancestry3':[0.07,0.18]} , 'Blue' : {'Ancestry1':[0.48],'Ancestry2':[0.22],'Ancestry3':[0.30]}})


if __name__ == '__main__':
    unittest.main()
