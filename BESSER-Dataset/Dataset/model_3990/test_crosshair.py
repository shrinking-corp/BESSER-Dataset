from python_code import ExtendedAnnotationType
from python_code import xpdl_ExtendedAttributeType
from python_code import xpdl_ExtendedAttributesType

def test_xpdl_ExtendedAttributeType___init__():
    assert xpdl_ExtendedAttributeType.__init__(xpdl_ExtendedAttributeType('', '', '', '', '', xpdl_ExtendedAttributeType9=ExtendedAnnotationType(), xpdl_ExtendedAttributeType=xpdl_ExtendedAttributesType()), '', '', '', '', '', xpdl_ExtendedAttributeType9=ExtendedAnnotationType(), xpdl_ExtendedAttributeType=xpdl_ExtendedAttributesType()) == None


from python_code import xpdl_ExternalPackages

def test_xpdl_ExternalPackages___init__():
    assert xpdl_ExternalPackages.__init__(xpdl_ExternalPackages(xpdl_ExternalPackages=set()), xpdl_ExternalPackages=set()) == None

def test_xpdl_ExternalPackages_getExternalPackage():
    assert xpdl_ExternalPackages.getExternalPackage(xpdl_ExternalPackages(xpdl_ExternalPackages=set()), 0) == None


from python_code import xpdl_ScriptType

def test_xpdl_ScriptType___init__():
    assert xpdl_ScriptType.__init__(xpdl_ScriptType('', '', '\x00\x00'), '', '', '') == None

