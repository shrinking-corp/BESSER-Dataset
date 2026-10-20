from python_code import sihuhu_NamedElement

def test_sihuhu_NamedElement___init__():
    assert sihuhu_NamedElement.__init__(sihuhu_NamedElement(''), '') == None


from python_code import sihuhu_Rail
from python_code import sihuhu_Signal

def test_sihuhu_Signal___init__():
    assert sihuhu_Signal.__init__(sihuhu_Signal(True, sihuhu_Signal=sihuhu_Rail(), sihuhu_Signal12=sihuhu_Rail(), sihuhu_Signal31=sihuhu_Rail()), False, sihuhu_Signal=sihuhu_Rail(), sihuhu_Signal12=sihuhu_Rail(), sihuhu_Signal31=sihuhu_Rail()) == None

