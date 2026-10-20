from python_code import henshin_DescribedElement

def test_henshin_DescribedElement___init__():
    assert henshin_DescribedElement.__init__(henshin_DescribedElement(''), '') == None


from python_code import henshin_GraphElement

def test_henshin_GraphElement___init__():
    assert henshin_GraphElement.__init__(henshin_GraphElement()) == None

def test_henshin_GraphElement_getGraph():
    assert henshin_GraphElement.getGraph(henshin_GraphElement()) == None


from python_code import henshin_NamedElement

def test_henshin_NamedElement___init__():
    assert henshin_NamedElement.__init__(henshin_NamedElement(''), '') == None

