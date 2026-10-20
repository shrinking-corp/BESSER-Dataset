from python_code import Articulo

def test_Articulo___init__():
    assert Articulo.__init__(Articulo(''), '') == None


from python_code import Clase

def test_Clase___init__():
    assert Clase.__init__(Clase('\x00\x00', '', asistencia65=set()), '', '', asistencia65=set()) == None


from python_code import Cliente1

def test_Cliente1___init__():
    assert Cliente1.__init__(Cliente1('', '', '\x00', '', '', '', asistencia60=set(), Cliente_inscripcion_068=set()), '', '', '', '', '', '', asistencia60=set(), Cliente_inscripcion_068=set()) == None


from python_code import Instructor

def test_Instructor___init__():
    assert Instructor.__init__(Instructor('', asistencia63=set()), '', asistencia63=set()) == None


from python_code import usario

def test_usario___init__():
    assert usario.__init__(usario(''), '') == None

