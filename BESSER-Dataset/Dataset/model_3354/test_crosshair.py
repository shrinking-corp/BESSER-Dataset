from python_code import Trmodel_Column
from python_code import Trmodel_Operation

def test_Trmodel_Column___init__():
    assert Trmodel_Column.__init__(Trmodel_Column('', '\x00', Trmodel_Column=Trmodel_Operation()), '\x00\x00', '', Trmodel_Column=Trmodel_Operation()) == None


from python_code import Trmodel_LoadModel
from python_code import Trmodel_loader

def test_Trmodel_LoadModel___init__():
    assert Trmodel_LoadModel.__init__(Trmodel_LoadModel('', Trmodel_LoadModel=Trmodel_loader()), '', Trmodel_LoadModel=Trmodel_loader()) == None


from python_code import Trmodel_Operation
from python_code import Trmodel_Table

def test_Trmodel_Table___init__():
    assert Trmodel_Table.__init__(Trmodel_Table('', Trmodel_Table=Trmodel_Operation()), '', Trmodel_Table=Trmodel_Operation()) == None


from python_code import Trmodel_Update

def test_Trmodel_Update___init__():
    assert Trmodel_Update.__init__(Trmodel_Update(''), '') == None

