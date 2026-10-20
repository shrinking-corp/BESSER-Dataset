from python_code import alergia

def test_alergia___init__():
    assert alergia.__init__(alergia(0, '\x00'), 0, '\x00') == None


from python_code import especialidad

def test_especialidad___init__():
    assert especialidad.__init__(especialidad(0, '\x00', especialidad_doctor_04=set()), 0, '', especialidad_doctor_04=set()) == None


from python_code import tipoSeguro

def test_tipoSeguro___init__():
    assert tipoSeguro.__init__(tipoSeguro(0, '\x00', tipoSeguro_aseguradora_08=set()), 0, '', tipoSeguro_aseguradora_08=set()) == None

