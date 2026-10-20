from python_code import Articulo

def test_Articulo___init__():
    assert Articulo.__init__(Articulo(''), '') == None


from python_code import Instructor

def test_Instructor___init__():
    assert Instructor.__init__(Instructor('', asistencia65=set()), '', asistencia65=set()) == None


from python_code import usario

def test_usario___init__():
    assert usario.__init__(usario(''), '') == None

