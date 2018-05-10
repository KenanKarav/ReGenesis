import unittest
from graphDrawing.graphs.pcaGraph.pcaGraph import pcaGraph

class TestPCAGraph(unittest.TestCase):

    def setUp(self):
        testDict = {'PcaFile': None, 'PcaIDs': ['ID1', 'ID2', 'ID3'], 'x': [0.33, 0.48, 0.58],
                    'y': [0.60, 0.22, 0.24], 'z': [0.07, 0.30, 0.18], 'dimension' : 3,
                    'PhenoFile': None, 'PhenoIDs': ['ID1', 'ID2', 'ID3'], 'PhenoColumn': ['Green', 'Blue', 'Green']}
        self.myGraph = pcaGraph(testDict)

    def test_FindPCAData(self):
        tempDict = self.myGraph.findPcaData()
        self.assertEqual({'Green':{'x':[0.33, 0.58], 'y':[0.60,0.24], 'z':[0.07,0.18]} , 'Blue' : {'x':[0.48],'y':[0.22],'z':[0.30]}}, tempDict)

if __name__ == '__main__':
    unittest.main()