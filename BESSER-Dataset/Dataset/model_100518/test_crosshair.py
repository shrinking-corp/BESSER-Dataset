from python_code import schema_ActionLike

def test_schema_ActionLike___init__():
    assert schema_ActionLike.__init__(schema_ActionLike('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import schema_EFactory
from python_code import schema_EPackage
from python_code import schema_StorySchemaCatalog

def test_schema_StorySchemaCatalog___init__():
    assert schema_StorySchemaCatalog.__init__(schema_StorySchemaCatalog('', '', '', schema_StorySchemaCatalog4=set(), schema_StorySchemaCatalog=set(), schema_StorySchemaCatalog2=set(), schema_StorySchemaCatalog6=schema_EPackage(), schema_StorySchemaCatalog8=schema_EFactory()), '\x00', '', '', schema_StorySchemaCatalog4=set(), schema_StorySchemaCatalog=set(), schema_StorySchemaCatalog2=set(), schema_StorySchemaCatalog6=schema_EPackage(), schema_StorySchemaCatalog8=schema_EFactory()) == None

def test_schema_StorySchemaCatalog_createAction():
    assert schema_StorySchemaCatalog.createAction(schema_StorySchemaCatalog('\x00', '', '', schema_StorySchemaCatalog4=set(), schema_StorySchemaCatalog=set(), schema_StorySchemaCatalog2=set(), schema_StorySchemaCatalog6=schema_EPackage(), schema_StorySchemaCatalog8=schema_EFactory()), '') == None

