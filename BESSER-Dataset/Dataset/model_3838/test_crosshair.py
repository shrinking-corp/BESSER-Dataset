from python_code import sql_NamedElement

def test_sql_NamedElement___init__():
    assert sql_NamedElement.__init__(sql_NamedElement(''), '') == None

