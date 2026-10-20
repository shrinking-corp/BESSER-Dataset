from python_code import myDsl_Api
from python_code import myDsl_ApiNome

def test_myDsl_ApiNome___init__():
    assert myDsl_ApiNome.__init__(myDsl_ApiNome('', myDsl_ApiNome=myDsl_Api()), '', myDsl_ApiNome=myDsl_Api()) == None


from python_code import myDsl_Associacao
from python_code import myDsl_Atributo

def test_myDsl_Associacao___init__():
    assert myDsl_Associacao.__init__(myDsl_Associacao('', myDsl_Associacao=myDsl_Atributo()), '', myDsl_Associacao=myDsl_Atributo()) == None


from python_code import myDsl_Atributo
from python_code import myDsl_AtributoTipo

def test_myDsl_AtributoTipo___init__():
    assert myDsl_AtributoTipo.__init__(myDsl_AtributoTipo('', '', '\x00\x00', myDsl_AtributoTipo=myDsl_Atributo()), '', '', '', myDsl_AtributoTipo=myDsl_Atributo()) == None


from python_code import myDsl_Entidade
from python_code import myDsl_Nome

def test_myDsl_Nome___init__():
    assert myDsl_Nome.__init__(myDsl_Nome('', myDsl_Nome=myDsl_Entidade()), '', myDsl_Nome=myDsl_Entidade()) == None


from python_code import myDsl_Atributo
from python_code import myDsl_Nome_Atributo

def test_myDsl_Nome_Atributo___init__():
    assert myDsl_Nome_Atributo.__init__(myDsl_Nome_Atributo('', myDsl_Nome_Atributo=myDsl_Atributo()), '', myDsl_Nome_Atributo=myDsl_Atributo()) == None


from python_code import myDsl_Operacao
from python_code import myDsl_OperacaoCascada

def test_myDsl_OperacaoCascada___init__():
    assert myDsl_OperacaoCascada.__init__(myDsl_OperacaoCascada('', myDsl_OperacaoCascada=myDsl_Operacao(), myDsl_OperacaoCascada33=myDsl_Operacao()), '', myDsl_OperacaoCascada=myDsl_Operacao(), myDsl_OperacaoCascada33=myDsl_Operacao()) == None

