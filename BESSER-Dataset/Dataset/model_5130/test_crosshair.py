from python_code import caracteristica_Acao
from python_code import caracteristica_AcaoLogico

def test_caracteristica_AcaoLogico___init__():
    assert caracteristica_AcaoLogico.__init__(caracteristica_AcaoLogico('', caracteristica_AcaoLogico=caracteristica_Acao(), caracteristica_AcaoLogico73=caracteristica_Acao()), '', caracteristica_AcaoLogico=caracteristica_Acao(), caracteristica_AcaoLogico73=caracteristica_Acao()) == None


from python_code import caracteristica_AtributoProduto
from python_code import caracteristica_CaracteristicaProduto

def test_caracteristica_AtributoProduto___init__():
    assert caracteristica_AtributoProduto.__init__(caracteristica_AtributoProduto('', '\x00', AtributoProduto=caracteristica_CaracteristicaProduto(), atributoProduto=caracteristica_CaracteristicaProduto()), '\x00\x00', '', AtributoProduto=caracteristica_CaracteristicaProduto(), atributoProduto=caracteristica_CaracteristicaProduto()) == None


from python_code import caracteristica_Evento
from python_code import caracteristica_EventoLogico

def test_caracteristica_EventoLogico___init__():
    assert caracteristica_EventoLogico.__init__(caracteristica_EventoLogico('', caracteristica_EventoLogico=caracteristica_Evento(), caracteristica_EventoLogico67=caracteristica_Evento()), '', caracteristica_EventoLogico=caracteristica_Evento(), caracteristica_EventoLogico67=caracteristica_Evento()) == None


from python_code import caracteristica_Antecedente
from python_code import caracteristica_ExpressaoLogica

def test_caracteristica_ExpressaoLogica___init__():
    assert caracteristica_ExpressaoLogica.__init__(caracteristica_ExpressaoLogica('', caracteristica_ExpressaoLogica=caracteristica_Antecedente(), caracteristica_ExpressaoLogica81=caracteristica_Antecedente()), '', caracteristica_ExpressaoLogica=caracteristica_Antecedente(), caracteristica_ExpressaoLogica81=caracteristica_Antecedente()) == None


from python_code import caracteristica_ElementoCaracteristico
from python_code import caracteristica_InconsistenciaRegraAdaptacao
from python_code import caracteristica_LiteralAcao

def test_caracteristica_LiteralAcao___init__():
    assert caracteristica_LiteralAcao.__init__(caracteristica_LiteralAcao('', caracteristica_LiteralAcao=caracteristica_ElementoCaracteristico(), caracteristica_LiteralAcao111=caracteristica_InconsistenciaRegraAdaptacao()), '', caracteristica_LiteralAcao=caracteristica_ElementoCaracteristico(), caracteristica_LiteralAcao111=caracteristica_InconsistenciaRegraAdaptacao()) == None


from python_code import caracteristica_ElementoCaracteristico
from python_code import caracteristica_LiteralComposicao

def test_caracteristica_LiteralComposicao___init__():
    assert caracteristica_LiteralComposicao.__init__(caracteristica_LiteralComposicao('', caracteristica_LiteralComposicao=caracteristica_ElementoCaracteristico()), '', caracteristica_LiteralComposicao=caracteristica_ElementoCaracteristico()) == None


from python_code import caracteristica_Caracteristica
from python_code import caracteristica_Variacao
from python_code import caracteristica_Variante

def test_caracteristica_Variacao___init__():
    assert caracteristica_Variacao.__init__(caracteristica_Variacao('\x00\x00', '', Variacao=caracteristica_Caracteristica(), variacaoPai=set(), variacoes=caracteristica_Caracteristica(), Variacao34=caracteristica_Variante()), '', '', Variacao=caracteristica_Caracteristica(), variacaoPai=set(), variacoes=caracteristica_Caracteristica(), Variacao34=caracteristica_Variante()) == None


from python_code import caracteristica_VariacaoDois

def test_caracteristica_VariacaoDois___init__():
    assert caracteristica_VariacaoDois.__init__(caracteristica_VariacaoDois('', '', '\x00\x00'), '', '', '') == None


from python_code import caracteristica_VariacaoDoisProduto

def test_caracteristica_VariacaoDoisProduto___init__():
    assert caracteristica_VariacaoDoisProduto.__init__(caracteristica_VariacaoDoisProduto(''), '') == None

