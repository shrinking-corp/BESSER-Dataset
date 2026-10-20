from python_code import oclstdlib_Collection

def test_oclstdlib_Collection___init__():
    assert oclstdlib_Collection.__init__(oclstdlib_Collection('', '\x00'), '\x00\x00', '') == None

