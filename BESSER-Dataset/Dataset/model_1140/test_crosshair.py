from python_code import statemodel_Import
from python_code import statemodel_Model

def test_statemodel_Import___init__():
    assert statemodel_Import.__init__(statemodel_Import('', statemodel_Import=statemodel_Model()), '', statemodel_Import=statemodel_Model()) == None

