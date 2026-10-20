from python_code import BD_EsquemaBD
from python_code import BD_Tabla

def test_BD_Tabla___init__():
    assert BD_Tabla.__init__(BD_Tabla('', BD_Tabla=BD_EsquemaBD(), BD_Tabla2=set()), '', BD_Tabla=BD_EsquemaBD(), BD_Tabla2=set()) == None

