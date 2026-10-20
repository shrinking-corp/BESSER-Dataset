from python_code import myDsl_Conditional

def test_myDsl_Conditional___init__():
    assert myDsl_Conditional.__init__(myDsl_Conditional('', 0, 0), '\x00', 0, 0) == None


from python_code import myDsl_Define

def test_myDsl_Define___init__():
    assert myDsl_Define.__init__(myDsl_Define(''), '') == None


from python_code import myDsl_Expression
from python_code import myDsl_Model

def test_myDsl_Expression___init__():
    assert myDsl_Expression.__init__(myDsl_Expression(0, myDsl_Expression=myDsl_Model()), 0, myDsl_Expression=myDsl_Model()) == None


from python_code import myDsl_Lambda

def test_myDsl_Lambda___init__():
    assert myDsl_Lambda.__init__(myDsl_Lambda(''), '') == None


from python_code import myDsl_Operation

def test_myDsl_Operation___init__():
    assert myDsl_Operation.__init__(myDsl_Operation('', 0), '', 0) == None

