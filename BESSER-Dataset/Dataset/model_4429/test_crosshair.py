from python_code import arduino_Bumper_Pressionado

def test_arduino_Bumper_Pressionado___init__():
    assert arduino_Bumper_Pressionado.__init__(arduino_Bumper_Pressionado(''), '') == None


from python_code import arduino_Cabeca_Modificavel

def test_arduino_Cabeca_Modificavel___init__():
    assert arduino_Cabeca_Modificavel.__init__(arduino_Cabeca_Modificavel(0), 0) == None


from python_code import arduino_Centrar

def test_arduino_Centrar___init__():
    assert arduino_Centrar.__init__(arduino_Centrar(''), '') == None


from python_code import arduino_Corpo

def test_arduino_Corpo___init__():
    assert arduino_Corpo.__init__(arduino_Corpo(True), False) == None


from python_code import arduino_Corpo_Modificavel

def test_arduino_Corpo_Modificavel___init__():
    assert arduino_Corpo_Modificavel.__init__(arduino_Corpo_Modificavel(0, False), 0, False) == None


from python_code import arduino_Desligar_Cor

def test_arduino_Desligar_Cor___init__():
    assert arduino_Desligar_Cor.__init__(arduino_Desligar_Cor(''), '') == None


from python_code import arduino_Desligar_Cores

def test_arduino_Desligar_Cores___init__():
    assert arduino_Desligar_Cores.__init__(arduino_Desligar_Cores(''), '') == None


from python_code import arduino_Desligar_Intermitencia

def test_arduino_Desligar_Intermitencia___init__():
    assert arduino_Desligar_Intermitencia.__init__(arduino_Desligar_Intermitencia(''), '') == None


from python_code import arduino_Desligar_LED_Verde

def test_arduino_Desligar_LED_Verde___init__():
    assert arduino_Desligar_LED_Verde.__init__(arduino_Desligar_LED_Verde(''), '') == None


from python_code import arduino_Distancia_Infra_Vermelhos

def test_arduino_Distancia_Infra_Vermelhos___init__():
    assert arduino_Distancia_Infra_Vermelhos.__init__(arduino_Distancia_Infra_Vermelhos(0), 0) == None


from python_code import arduino_Fim

def test_arduino_Fim___init__():
    assert arduino_Fim.__init__(arduino_Fim(''), '') == None


from python_code import arduino_Acao
from python_code import arduino_If

def test_arduino_If___init__():
    assert arduino_If.__init__(arduino_If('', arduino_If=arduino_Acao()), '', arduino_If=arduino_Acao()) == None


from python_code import arduino_Inicio

def test_arduino_Inicio___init__():
    assert arduino_Inicio.__init__(arduino_Inicio('', False), '', False) == None


from python_code import arduino_Ligar_Azul

def test_arduino_Ligar_Azul___init__():
    assert arduino_Ligar_Azul.__init__(arduino_Ligar_Azul(''), '') == None


from python_code import arduino_Ligar_Cores_Arco_Iris

def test_arduino_Ligar_Cores_Arco_Iris___init__():
    assert arduino_Ligar_Cores_Arco_Iris.__init__(arduino_Ligar_Cores_Arco_Iris(''), '') == None


from python_code import arduino_Ligar_Cores_Policia

def test_arduino_Ligar_Cores_Policia___init__():
    assert arduino_Ligar_Cores_Policia.__init__(arduino_Ligar_Cores_Policia(''), '') == None


from python_code import arduino_Ligar_Intermitencia

def test_arduino_Ligar_Intermitencia___init__():
    assert arduino_Ligar_Intermitencia.__init__(arduino_Ligar_Intermitencia(''), '') == None


from python_code import arduino_Ligar_LED_Verde

def test_arduino_Ligar_LED_Verde___init__():
    assert arduino_Ligar_LED_Verde.__init__(arduino_Ligar_LED_Verde(''), '') == None


from python_code import arduino_Ligar_Verde

def test_arduino_Ligar_Verde___init__():
    assert arduino_Ligar_Verde.__init__(arduino_Ligar_Verde(''), '') == None


from python_code import arduino_Ligar_Vermelho

def test_arduino_Ligar_Vermelho___init__():
    assert arduino_Ligar_Vermelho.__init__(arduino_Ligar_Vermelho(''), '') == None


from python_code import arduino_Mover_Aleatoriamente

def test_arduino_Mover_Aleatoriamente___init__():
    assert arduino_Mover_Aleatoriamente.__init__(arduino_Mover_Aleatoriamente(''), '') == None


from python_code import arduino_Mover_Frente

def test_arduino_Mover_Frente___init__():
    assert arduino_Mover_Frente.__init__(arduino_Mover_Frente(''), '') == None


from python_code import arduino_Mover_Tras

def test_arduino_Mover_Tras___init__():
    assert arduino_Mover_Tras.__init__(arduino_Mover_Tras(''), '') == None


from python_code import arduino_Parar

def test_arduino_Parar___init__():
    assert arduino_Parar.__init__(arduino_Parar(''), '') == None


from python_code import arduino_Robo

def test_arduino_Robo___init__():
    assert arduino_Robo.__init__(arduino_Robo('', arduino_Robo=set(), arduino_Robo2=set(), arduino_Robo4=set()), '', arduino_Robo=set(), arduino_Robo2=set(), arduino_Robo4=set()) == None


from python_code import arduino_Virar_45_Drt

def test_arduino_Virar_45_Drt___init__():
    assert arduino_Virar_45_Drt.__init__(arduino_Virar_45_Drt(''), '') == None


from python_code import arduino_Virar_45_Esq

def test_arduino_Virar_45_Esq___init__():
    assert arduino_Virar_45_Esq.__init__(arduino_Virar_45_Esq(''), '') == None


from python_code import arduino_Virar_Direita

def test_arduino_Virar_Direita___init__():
    assert arduino_Virar_Direita.__init__(arduino_Virar_Direita(''), '') == None


from python_code import arduino_Virar_Esquerda

def test_arduino_Virar_Esquerda___init__():
    assert arduino_Virar_Esquerda.__init__(arduino_Virar_Esquerda(''), '') == None


from python_code import arduino_Virar_Max_Drt

def test_arduino_Virar_Max_Drt___init__():
    assert arduino_Virar_Max_Drt.__init__(arduino_Virar_Max_Drt(''), '') == None


from python_code import arduino_Virar_Max_Esq

def test_arduino_Virar_Max_Esq___init__():
    assert arduino_Virar_Max_Esq.__init__(arduino_Virar_Max_Esq(''), '') == None


from python_code import arduino_Acao
from python_code import arduino_While

def test_arduino_While___init__():
    assert arduino_While.__init__(arduino_While('', arduino_While=arduino_Acao()), '', arduino_While=arduino_Acao()) == None

