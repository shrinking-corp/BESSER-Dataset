from python_code import opf_Item
from python_code import opf_Manifest

def test_opf_Item___init__():
    assert opf_Item.__init__(opf_Item('', '', '', '', '', '', '', '', False, '', False, '', opf_Item=opf_Manifest()), '', '', '', '', '', '', '', '', False, '', False, '', opf_Item=opf_Manifest()) == None


from python_code import opf_Meta
from python_code import opf_Metadata

def test_opf_Meta___init__():
    assert opf_Meta.__init__(opf_Meta('', '\x00', opf_Meta=opf_Metadata()), '\x00\x00', '', opf_Meta=opf_Metadata()) == None


from python_code import opf_Guide
from python_code import opf_Reference

def test_opf_Reference___init__():
    assert opf_Reference.__init__(opf_Reference('', '', '\x00\x00', opf_Reference=opf_Guide()), '', '', '', opf_Reference=opf_Guide()) == None

