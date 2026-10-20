from python_code import r2_AD

def test_r2_AD___init__():
    assert r2_AD.__init__(r2_AD('\x00', r2_AD=set()), '', r2_AD=set()) == None


from python_code import r2_BL

def test_r2_BL___init__():
    assert r2_BL.__init__(r2_BL(''), '') == None


from python_code import r2_CS

def test_r2_CS___init__():
    assert r2_CS.__init__(r2_CS(''), '') == None


from python_code import r2_EN

def test_r2_EN___init__():
    assert r2_EN.__init__(r2_EN('', r2_EN=set()), '', r2_EN=set()) == None


from python_code import r2_II

def test_r2_II___init__():
    assert r2_II.__init__(r2_II('', '', '\x00\x00'), '', '', '') == None


from python_code import r2_IVLQTY
from python_code import r2_QTY

def test_r2_IVLQTY___init__():
    assert r2_IVLQTY.__init__(r2_IVLQTY('', '\x00', r2_IVLQTY=r2_QTY(), r2_IVLQTY32=r2_QTY()), '\x00\x00', '', r2_IVLQTY=r2_QTY(), r2_IVLQTY32=r2_QTY()) == None


from python_code import r2_XP

def test_r2_XP___init__():
    assert r2_XP.__init__(r2_XP(''), '') == None

