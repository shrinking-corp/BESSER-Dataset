from python_code import sedml_curve
from python_code import sedml_listOfCurves

def test_sedml_curve___init__():
    assert sedml_curve.__init__(sedml_curve('', '', '', '', '', sedml_curve=sedml_listOfCurves()), '', '', '', '', '', sedml_curve=sedml_listOfCurves()) == None


from python_code import sedml_listOfCurves
from python_code import sedml_listOfOutputs
from python_code import sedml_plot2D

def test_sedml_plot2D___init__():
    assert sedml_plot2D.__init__(sedml_plot2D('', '\x00', sedml_plot2D=sedml_listOfOutputs(), sedml_plot2D28=sedml_listOfCurves()), '\x00\x00', '', sedml_plot2D=sedml_listOfOutputs(), sedml_plot2D28=sedml_listOfCurves()) == None


from python_code import sedml_listOfDataGenerators
from python_code import sedml_listOfModels
from python_code import sedml_listOfOutputs
from python_code import sedml_listOfSimulations
from python_code import sedml_listOfTasks
from python_code import sedml_sedML

def test_sedml_sedML___init__():
    assert sedml_sedML.__init__(sedml_sedML(0, 0, sedml_sedML=sedml_listOfSimulations(), sedml_sedML2=sedml_listOfModels(), sedml_sedML4=sedml_listOfTasks(), sedml_sedML6=sedml_listOfDataGenerators(), sedml_sedML8=sedml_listOfOutputs()), 0, 0, sedml_sedML=sedml_listOfSimulations(), sedml_sedML2=sedml_listOfModels(), sedml_sedML4=sedml_listOfTasks(), sedml_sedML6=sedml_listOfDataGenerators(), sedml_sedML8=sedml_listOfOutputs()) == None

