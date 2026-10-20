from python_code import caracteristica_Atributo
from python_code import caracteristica_Caracteristica

def test_caracteristica_Atributo___init__():
    assert caracteristica_Atributo.__init__(caracteristica_Atributo('', Atributo=caracteristica_Caracteristica(), atributo=caracteristica_Caracteristica()), '', Atributo=caracteristica_Caracteristica(), atributo=caracteristica_Caracteristica()) == None


from python_code import caracteristica_CaracteristicaRaiz
from python_code import caracteristica_LPS

def test_caracteristica_LPS___init__():
    assert caracteristica_LPS.__init__(caracteristica_LPS('\x00', caracteristica_LPS=set(), caracteristica_LPS13=caracteristica_CaracteristicaRaiz()), '', caracteristica_LPS=set(), caracteristica_LPS13=caracteristica_CaracteristicaRaiz()) == None


from python_code import caracteristica_Caracteristica
from python_code import caracteristica_Variacao
from python_code import caracteristica_Variante

def test_caracteristica_Variacao___init__():
    assert caracteristica_Variacao.__init__(caracteristica_Variacao('\x00\x00', '', Variacao=caracteristica_Caracteristica(), variacaoPai=set(), variacoes=caracteristica_Caracteristica(), Variacao18=caracteristica_Variante()), '', '', Variacao=caracteristica_Caracteristica(), variacaoPai=set(), variacoes=caracteristica_Caracteristica(), Variacao18=caracteristica_Variante()) == None


from python_code import caracteristica_VariacaoDois

def test_caracteristica_VariacaoDois___init__():
    assert caracteristica_VariacaoDois.__init__(caracteristica_VariacaoDois('', '', '\x00\x00'), '', '', '') == None

