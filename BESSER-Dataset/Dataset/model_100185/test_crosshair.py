from python_code import sql_SqlProvides

def test_sql_SqlProvides___init__():
    assert sql_SqlProvides.__init__(sql_SqlProvides('\x00', '', '', '', '', '', '', '', '', '', '\x00'), '', '', '', '', '', '', '', '', '', '', '') == None

