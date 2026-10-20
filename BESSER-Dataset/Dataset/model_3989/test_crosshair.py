from python_code import ExtendedAnnotationType
from python_code import xpdl2_ExtendedAttributeType
from python_code import xpdl2_ExtendedAttributesType

def test_xpdl2_ExtendedAttributeType___init__():
    assert xpdl2_ExtendedAttributeType.__init__(xpdl2_ExtendedAttributeType('', '', '', '', '', xpdl2_ExtendedAttributeType=xpdl2_ExtendedAttributesType(), xpdl2_ExtendedAttributeType9=ExtendedAnnotationType()), '', '', '', '', '', xpdl2_ExtendedAttributeType=xpdl2_ExtendedAttributesType(), xpdl2_ExtendedAttributeType9=ExtendedAnnotationType()) == None


from python_code import xpdl2_ExternalPackages

def test_xpdl2_ExternalPackages___init__():
    assert xpdl2_ExternalPackages.__init__(xpdl2_ExternalPackages(xpdl2_ExternalPackages=set()), xpdl2_ExternalPackages=set()) == None

def test_xpdl2_ExternalPackages_getExternalPackage():
    assert xpdl2_ExternalPackages.getExternalPackage(xpdl2_ExternalPackages(xpdl2_ExternalPackages=set()), 0) == None


from python_code import xpdl2_ScriptType

def test_xpdl2_ScriptType___init__():
    assert xpdl2_ScriptType.__init__(xpdl2_ScriptType('', '', '\x00\x00'), '', '', '') == None


from python_code import xpdl2_extensions_LoopDataRefType

def test_xpdl2_extensions_LoopDataRefType___init__():
    assert xpdl2_extensions_LoopDataRefType.__init__(xpdl2_extensions_LoopDataRefType('', '', '\x00\x00'), '', '', '') == None

