from python_code import scmodel_History

def test_scmodel_History___init__():
    assert scmodel_History.__init__(scmodel_History(True), False) == None


from python_code import scmodel_PseudoState

def test_scmodel_PseudoState___init__():
    assert scmodel_PseudoState.__init__(scmodel_PseudoState(''), '') == None

