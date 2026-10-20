from python_code import oracle_DatabaseModuleExtensibleProperty

def test_oracle_DatabaseModuleExtensibleProperty___init__():
    assert oracle_DatabaseModuleExtensibleProperty.__init__(oracle_DatabaseModuleExtensibleProperty('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import oracle_OracleIndexProperty

def test_oracle_OracleIndexProperty___init__():
    assert oracle_OracleIndexProperty.__init__(oracle_OracleIndexProperty(True), False) == None


from python_code import oracle_OracleModuleProperty

def test_oracle_OracleModuleProperty___init__():
    assert oracle_OracleModuleProperty.__init__(oracle_OracleModuleProperty(''), '') == None


from python_code import oracle_OracleSequenceProperty

def test_oracle_OracleSequenceProperty___init__():
    assert oracle_OracleSequenceProperty.__init__(oracle_OracleSequenceProperty(''), '') == None


from python_code import oracle_OracleTableProperty

def test_oracle_OracleTableProperty___init__():
    assert oracle_OracleTableProperty.__init__(oracle_OracleTableProperty('', '\x00'), '\x00\x00', '') == None


from python_code import oracle_OracleUser
from python_code import oracle_OracleUserResourceData

def test_oracle_OracleUser___init__():
    assert oracle_OracleUser.__init__(oracle_OracleUser('', '', '', False, '', '', oracle_OracleUser=oracle_OracleUserResourceData(), oracle_OracleUser7=set()), '', '', '', True, '', '', oracle_OracleUser=oracle_OracleUserResourceData(), oracle_OracleUser7=set()) == None


from python_code import oracle_OracleViewProperty

def test_oracle_OracleViewProperty___init__():
    assert oracle_OracleViewProperty.__init__(oracle_OracleViewProperty(''), '') == None


from python_code import oracle_SequenceResourceData

def test_oracle_SequenceResourceData___init__():
    assert oracle_SequenceResourceData.__init__(oracle_SequenceResourceData('', '', '', '', '\x00', False, '', False, False), '', '', '', '', '', False, '', False, False) == None


from python_code import oracle_OracleSpaceResourceData
from python_code import oracle_TableSpace

def test_oracle_TableSpace___init__():
    assert oracle_TableSpace.__init__(oracle_TableSpace('', '', '', '', '', '', '', oracle_TableSpace=oracle_OracleSpaceResourceData()), '', '\x00', '', '', '', '', '', oracle_TableSpace=oracle_OracleSpaceResourceData()) == None


from python_code import oracle_OracleSpaceResourceData
from python_code import oracle_TableSpaceRelation

def test_oracle_TableSpaceRelation___init__():
    assert oracle_TableSpaceRelation.__init__(oracle_TableSpaceRelation('', '\x00', oracle_TableSpaceRelation=oracle_OracleSpaceResourceData()), '\x00\x00', '', oracle_TableSpaceRelation=oracle_OracleSpaceResourceData()) == None


from python_code import oracle_TriggerResourceData

def test_oracle_TriggerResourceData___init__():
    assert oracle_TriggerResourceData.__init__(oracle_TriggerResourceData(''), '') == None

