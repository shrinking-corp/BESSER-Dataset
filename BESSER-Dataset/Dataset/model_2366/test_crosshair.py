from python_code import sql_Annotation
from python_code import sql_ModelElement

def test_sql_Annotation___init__():
    assert sql_Annotation.__init__(sql_Annotation('', Annotation=sql_ModelElement(), ownedAnnotations=sql_ModelElement()), '', Annotation=sql_ModelElement(), ownedAnnotations=sql_ModelElement()) == None


from python_code import sql_Column
from python_code import sql_Key
from python_code import sql_Table

def test_sql_Column___init__():
    assert sql_Column.__init__(sql_Column('\x00\x00', '', ownedColumns=sql_Table(), column=set(), Column11=sql_Key(), Column=sql_Table()), '', '', ownedColumns=sql_Table(), column=set(), Column11=sql_Key(), Column=sql_Table()) == None


from python_code import sql_Event
from python_code import sql_ForeignKey

def test_sql_Event___init__():
    assert sql_Event.__init__(sql_Event('', '\x00', ownedEvents=sql_ForeignKey(), Event=sql_ForeignKey()), '\x00\x00', '', ownedEvents=sql_ForeignKey(), Event=sql_ForeignKey()) == None


from python_code import sql_NamedElement

def test_sql_NamedElement___init__():
    assert sql_NamedElement.__init__(sql_NamedElement(''), '') == None

