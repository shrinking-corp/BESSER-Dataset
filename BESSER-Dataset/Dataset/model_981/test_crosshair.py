from python_code import henshin_Annotation
from python_code import henshin_ModelElement

def test_henshin_Annotation___init__():
    assert henshin_Annotation.__init__(henshin_Annotation('', '\x00', henshin_Annotation=henshin_ModelElement()), '\x00\x00', '', henshin_Annotation=henshin_ModelElement()) == None


from python_code import henshin_GraphElement

def test_henshin_GraphElement___init__():
    assert henshin_GraphElement.__init__(henshin_GraphElement(''), '') == None

def test_henshin_GraphElement_getGraph():
    assert henshin_GraphElement.getGraph(henshin_GraphElement('')) == None


from python_code import henshin_IteratedUnit

def test_henshin_IteratedUnit___init__():
    assert henshin_IteratedUnit.__init__(henshin_IteratedUnit(''), '') == None


from python_code import henshin_NamedElement

def test_henshin_NamedElement___init__():
    assert henshin_NamedElement.__init__(henshin_NamedElement('', '\x00'), '\x00\x00', '') == None


from python_code import henshin_SequentialUnit

def test_henshin_SequentialUnit___init__():
    assert henshin_SequentialUnit.__init__(henshin_SequentialUnit(False, False), False, False) == None

