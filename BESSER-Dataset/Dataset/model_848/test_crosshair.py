from python_code import occi_AnnotatedElement
from python_code import occi_Annotation

def test_occi_Annotation___init__():
    assert occi_Annotation.__init__(occi_Annotation('', '\x00', occi_Annotation=occi_AnnotatedElement()), '\x00\x00', '', occi_Annotation=occi_AnnotatedElement()) == None


from python_code import occi_Category

def test_occi_Category___init__():
    assert occi_Category.__init__(occi_Category('', '', '', '', '', occi_Category=set()), '', '', '', '\x00', '', occi_Category=set()) == None


from python_code import occi_Constraint
from python_code import occi_Type

def test_occi_Constraint___init__():
    assert occi_Constraint.__init__(occi_Constraint('', '', '\x00\x00', occi_Constraint=occi_Type()), '', '', '', occi_Constraint=occi_Type()) == None


from python_code import occi_EObjectType

def test_occi_EObjectType___init__():
    assert occi_EObjectType.__init__(occi_EObjectType(''), '') == None


from python_code import occi_NumericType

def test_occi_NumericType___init__():
    assert occi_NumericType.__init__(occi_NumericType('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import occi_StringType

def test_occi_StringType___init__():
    assert occi_StringType.__init__(occi_StringType('\x00\x00', '', '', ''), '', '', '', '') == None

