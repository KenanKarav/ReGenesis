from pyforms import BaseWidget
from pyforms import start_app
from pyforms.controls import ControlMatplotlib
from matplotlib import pyplot as pplot
from matplotlib.figure import Figure
class SimpleExample(BaseWidget):
    def __init__(self):
        super(SimpleExample, self).__init__('ReGenesis')

        # Definition of the forms fields
        self._graph = ControlMatplotlib("plot")
        self.formset = [' ', (' ', '_graph', ' '), ' ']

        self.mainmenu = [
            {'New graphs': [
                {'PCA': self.__pcaEvent},
                '-',
                {'Admixture': self.__admixtureEvent},

            ]
            },
            {'Manage Graphs': [
                {'Save': self.__saveEvent},
                '-',
                {'Load': self.__loadEvent},
                '-',
                {'Export': self.__exportEvent}
            ]
            }
        ]






        X = [i for i in range(0,100,2)]
        Y = [i for i in range(0,150,3)]
        Z = [i for i in range(0,50)]

        pplot.scatter(X, Y, Z)

       # self._graph.value = pplot.figure()
       # self._graph.draw()

    def __admixtureEvent(self):
        x = 1

    def __pcaEvent(self):
        x = 1

    def __saveEvent(self):
        x = 1

    def __loadEvent(self):
        x = 1
    def __exportEvent(self):
        x = 1
##################################################################################################################
##################################################################################################################
##################################################################################################################

# Execute the applicatio
start_app(SimpleExample, geometry= (400,400,600,600))




