from python_code import BaseEntity

def test_BaseEntity___init__():
    assert BaseEntity.__init__(BaseEntity('', False, '', '', '', ''), '', False, '', '', '\x00', '') == None

