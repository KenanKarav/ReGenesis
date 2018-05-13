##########################README#######################################################################################

##########################Installation#################################################################################

The following python packages need to be installed in order for ReGenesis to run:

Matplotlib
wxPython
Enum

These can easily be installed using pip3.
To install these packages open terminal and navigate to the directory where pip3.exe is installed.
To find where pip3.exe is installed simply search for it using your computer's search tool and open the file location
pf pip3.exe
Once within that directory in terminal type in the following commands to install the packages:

pip3 install matplotlib
pip3 install wxpython
pip3 install enum

Make sure to type each command separately and hit Enter after each line.

##########################Directory Guide##############################################################################

Ignore all the __init__.py files in every directory.

In the root directory:

- graphManager.py is main script that is to be run first in order to start the ReGenesis applciation.
    To run the application open terminal and type in: python3 graphManager.py
                                          or type in: py graphManager.py

- fileManagement directory: consists of python scripts that are responsible for extracting and storing of data from the
  relative files
    - admixCreator.py
    - admixCreatorGUI.py
    - file.py
    - fileImporter.py
    - fileManager.py
    - pcaCreator.py
    - pcaCreatorGUI.py

- graphDrawing directory: consists of python scripts that are responsible for interpreting processed data and plotting
  the respective graphs.
      - graphs directory: contains the directories for both the admixture and pca related scripts
            - admixtureGraph directory: contains the scripts that deal with storing processed admixture data about the graph,
              admixture individuals and admixture graph appearence options.
                    - admixtureAppearance.py (Not implemented for current ReGenesis build)
                    - admixtureGraph.py
                    - admixtureIndividual (Not implemented for current ReGenesis build)
             - pcaGraph directory: contains the scripts that deal with storing processed pca data about the graph,
               pca individuals and pca graph appearence options.
                    - pcaAppearence.py
                    - pcaGraph.py
                    - pcaIndividual (Not implemented for current ReGenesis build)
             graphRenderer.py (Not implemented for current ReGenesis build)

- Testing_Suite directory: stores all the unit test modules for majority of the scripts defined in the fileManagement
  and graphDrawing directories as well as the some sample data files that were utilised in the unit tests.
    - AdmixtureTestFiles directory: contains samples of data, fam and phenotype files for the admixture graph
    - ExtraTestFiles directory: contains standard text files that were used for unit testing.
    - PCATestFiles directory: contains samples of data and phenotype files for the pca graph
    - test_admixCreator.py
    - test_admixGraph.py
    - test_file.py
    - test_fileImporter.py
    - test_pcaCreator.py
    - test_pcaGraph.py