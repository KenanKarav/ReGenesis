from pyforms import BaseWidget
from pyforms import start_app
from pyforms.controls import ControlMatplotlib
from matplotlib import pyplot as pplot
from matplotlib.figure import Figure
class SimpleExample(BaseWidget):
    def __init__(self):
        super(SimpleExample, self).__init__('Simple example')

        # Definition of the forms fields
        self._graph = ControlMatplotlib("plot")
        self.formset = [' ', (' ', '_graph', ' '), ' ']

        X = [i for i in range(0,100,2)]
        Y = [i for i in range(0,150,3)]
        Z = [i for i in range(0,50)]

        pplot.scatter(X, Y, Z)

       # self._graph.value = pplot.figure()
       # self._graph.draw()



##################################################################################################################
##################################################################################################################
##################################################################################################################

# Execute the applicatio
start_app(SimpleExample)




