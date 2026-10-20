from python_code import model_ModelObject

def test_model_ModelObject___init__():
    assert model_ModelObject.__init__(model_ModelObject('', '', '', '', model_ModelObject=set()), '', '', '', '', model_ModelObject=set()) == None


from python_code import PhysicalTable
from python_code import model_physical_PhysicalColumn

def test_model_physical_PhysicalColumn___init__():
    assert model_physical_PhysicalColumn.__init__(model_physical_PhysicalColumn('', '', 0, 0, 0, 0, '', False, 0, '', columns=PhysicalTable()), '', '', 0, 0, 0, 0, '', False, 0, '', columns=PhysicalTable()) == None


from python_code import PhysicalModel
from python_code import PhysicalTable
from python_code import model_physical_PhysicalForeignKey

def test_model_physical_PhysicalForeignKey___init__():
    assert model_physical_PhysicalForeignKey.__init__(model_physical_PhysicalForeignKey('', '', model_physical_PhysicalForeignKey=PhysicalTable(), model_physical_PhysicalForeignKey43=set(), model_physical_PhysicalForeignKey46=PhysicalTable(), model_physical_PhysicalForeignKey49=set(), foreignKeys=PhysicalModel()), '', '', model_physical_PhysicalForeignKey=PhysicalTable(), model_physical_PhysicalForeignKey43=set(), model_physical_PhysicalForeignKey46=PhysicalTable(), model_physical_PhysicalForeignKey49=set(), foreignKeys=PhysicalModel()) == None


from python_code import model_physical_PhysicalModel
from python_code import physical_model_Model

def test_model_physical_PhysicalModel___init__():
    assert model_physical_PhysicalModel.__init__(model_physical_PhysicalModel('', '', '\x00', '', physicalModels=physical_model_Model(), model=set(), model25=set(), model27=set()), '', '', '', '', physicalModels=physical_model_Model(), model=set(), model25=set(), model27=set()) == None


from python_code import PhysicalModel
from python_code import model_physical_PhysicalTable

def test_model_physical_PhysicalTable___init__():
    assert model_physical_PhysicalTable.__init__(model_physical_PhysicalTable('\x00\x00', '', tables=PhysicalModel(), table=set()), '', '', tables=PhysicalModel(), table=set()) == None

