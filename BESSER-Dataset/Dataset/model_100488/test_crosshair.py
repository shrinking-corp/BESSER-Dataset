from python_code import Dependency
from python_code import UMLMetamodelFragment_Stereotype

def test_UMLMetamodelFragment_Stereotype___init__():
    assert UMLMetamodelFragment_Stereotype.__init__(UMLMetamodelFragment_Stereotype('', stereotype=Dependency()), '', stereotype=Dependency()) == None

