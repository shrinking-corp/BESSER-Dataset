from python_code import afmmm_Enum

def test_afmmm_Enum___init__():
    assert afmmm_Enum.__init__(afmmm_Enum(''), '') == None


from python_code import afmmm_AttributedFeatureDiagram
from python_code import afmmm_Feature
from python_code import afmmm_Relation

def test_afmmm_Feature___init__():
    assert afmmm_Feature.__init__(afmmm_Feature('\x00', afmmm_Feature=afmmm_AttributedFeatureDiagram(), afmmm_Feature3=afmmm_AttributedFeatureDiagram(), afmmm_Feature9=set(), afmmm_Feature12=afmmm_Relation(), afmmm_Feature15=afmmm_Relation()), '', afmmm_Feature=afmmm_AttributedFeatureDiagram(), afmmm_Feature3=afmmm_AttributedFeatureDiagram(), afmmm_Feature9=set(), afmmm_Feature12=afmmm_Relation(), afmmm_Feature15=afmmm_Relation()) == None

