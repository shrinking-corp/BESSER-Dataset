from python_code import Data_Attribut
from python_code import Data_Classe

def test_Data_Attribut___init__():
    assert Data_Attribut.__init__(Data_Attribut('', False, '\x00\x00', Data_Attribut=Data_Classe(), Data_Attribut2=Data_Classe()), '', False, '', Data_Attribut=Data_Classe(), Data_Attribut2=Data_Classe()) == None


from python_code import Data_DeclarationType

def test_Data_DeclarationType___init__():
    assert Data_DeclarationType.__init__(Data_DeclarationType(''), '') == None

