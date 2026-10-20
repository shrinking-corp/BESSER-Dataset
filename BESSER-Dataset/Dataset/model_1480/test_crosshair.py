from python_code import graphmodel_Entity

def test_graphmodel_Entity___init__():
    assert graphmodel_Entity.__init__(graphmodel_Entity('', '', '', '', '', '', '\x00', '', '', '', '', '', '', ''), '', '', '', '', '', '', '', '', '\x00', '', '', '', '', '') == None


from python_code import graphmodel_ModellingType

def test_graphmodel_ModellingType___init__():
    assert graphmodel_ModellingType.__init__(graphmodel_ModellingType(''), '') == None

