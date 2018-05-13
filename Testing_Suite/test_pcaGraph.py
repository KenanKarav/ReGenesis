import unittest
from graphDrawing.graphs.pcaGraph.pcaGraph import pcaGraph

class TestPCAGraph(unittest.TestCase):

    def setUp(self):
        # Test Graph with pheno data
        testDict = {'PcaFile': None, 'PcaIDs': ['ID1', 'ID2', 'ID3'],
                    'xLabel' : 'PCA labelX', 'yLabel' : 'PCA LabelY', 'hasGrid' : False, 'hasLabels' : True,
                    'x': [0.33, 0.48, 0.58], 'y': [0.60, 0.22, 0.24], 'z': [0.07, 0.30, 0.18], 'dimension' : 3,
                    'PhenoFile': None, 'PhenoIDs': ['ID1', 'ID2', 'ID3'], 'PhenoColumn': ['Green', 'Blue', 'Green']}
        self.myGraph = pcaGraph(testDict)

        #Test Graph without pheno data
        testDict = {'PcaFile': None, 'PcaIDs': ['ID1', 'ID2', 'ID3'],
                    'xLabel' : 'PCA labelX', 'yLabel' : 'PCA LabelY', 'hasGrid' : False, 'hasLabels' : True,
                    'x': [0.33, 0.48, 0.58], 'y': [0.60, 0.22, 0.24], 'z': [0.07, 0.30, 0.18], 'dimension' : 3}
        self.myGraph2 = pcaGraph(testDict)

    def test_FindPCAData(self):
        tempDict = self.myGraph.findPcaData(False)
        self.assertEqual({'Green':{'x':[0.33, 0.58], 'y':[0.60,0.24], 'z':[0.07,0.18]} , 'Blue' : {'x':[0.48],'y':[0.22],'z':[0.30]}}, tempDict)

        tempDict = self.myGraph2.findPcaData(False)
        self.assertEqual({'ungrouped' : {'x': [0.33, 0.48, 0.58], 'y': [0.60, 0.22, 0.24], 'z': [0.07, 0.30, 0.18]}}, tempDict)

    def test_GetSaveFileData(self):
        tempDict = self.myGraph.getSaveFileData()
        self.assertEqual(tempDict, {
            'dimension' : 3,
            'PcaIDs' : ['ID1', 'ID2', 'ID3'],
            'xLabel' : 'PCA labelX',
            'yLabel' : 'PCA LabelY',
            'hasGrid' : False,
            'hasLabels' : True,
            'x' : [0.33, 0.48, 0.58],
            'y' : [0.60, 0.22, 0.24],
            'z' : [0.07, 0.30, 0.18],
            'PhenoIDs': ['ID1', 'ID2', 'ID3'],
            'PhenoColumn': ['Green', 'Blue', 'Green']
        })

        tempDict = self.myGraph2.getSaveFileData()
        self.assertEqual(tempDict, {
            'dimension' : 3,
            'PcaIDs' : ['ID1', 'ID2', 'ID3'],
            'xLabel' : 'PCA labelX',
            'yLabel' : 'PCA LabelY',
            'hasGrid' : False,
            'hasLabels' : True,
            'x' : [0.33, 0.48, 0.58],
            'y' : [0.60, 0.22, 0.24],
            'z' : [0.07, 0.30, 0.18],
        })

    def test_GetHasGrid(self):
        self.assertEqual(self.myGraph.getHasGrid(), False)
        self.assertEqual(self.myGraph2.getHasGrid(), False)

        self.myGraph.setHasGrid(True)
        self.myGraph2.setHasGrid(True)

        self.assertEqual(self.myGraph.getHasGrid(), True)
        self.assertEqual(self.myGraph2.getHasGrid(), True)

    def test_GetHasLabels(self):
        self.assertEqual(self.myGraph.getHasLabels(), True)
        self.assertEqual(self.myGraph2.getHasLabels(), True)

        self.myGraph.setHasLabels(False)
        self.myGraph2.setHasLabels(False)

        self.assertEqual(self.myGraph.getHasLabels(), False)
        self.assertEqual(self.myGraph2.getHasLabels(), False)

if __name__ == '__main__':
    unittest.main()