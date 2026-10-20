from python_code import lib_LibSys
from python_code import lib_Library

def test_lib_Library___init__():
    assert lib_Library.__init__(lib_Library('', '', lib_Library=set(), lib_Library2=set(), lib_Library7=lib_LibSys()), '', '', lib_Library=set(), lib_Library2=set(), lib_Library7=lib_LibSys()) == None

