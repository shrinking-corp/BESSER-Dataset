from python_code import sxfm_CardinalizedElement

def test_sxfm_CardinalizedElement___init__():
    assert sxfm_CardinalizedElement.__init__(sxfm_CardinalizedElement(0, 0), 0, 0) == None


from python_code import sxfm_Constraint
from python_code import sxfm_ConstraintsSet
from python_code import sxfm_Or

def test_sxfm_Constraint___init__():
    assert sxfm_Constraint.__init__(sxfm_Constraint(0, sxfm_Constraint15=sxfm_ConstraintsSet(), sxfm_Constraint=sxfm_Or()), 0, sxfm_Constraint15=sxfm_ConstraintsSet(), sxfm_Constraint=sxfm_Or()) == None


from python_code import sxfm_Data
from python_code import sxfm_MetadataSet

def test_sxfm_Data___init__():
    assert sxfm_Data.__init__(sxfm_Data('', '\x00', sxfm_Data=sxfm_MetadataSet()), '\x00\x00', '', sxfm_Data=sxfm_MetadataSet()) == None


from python_code import sxfm_ConstraintsSet
from python_code import sxfm_FeatureModel
from python_code import sxfm_FeatureTree
from python_code import sxfm_MetadataSet

def test_sxfm_FeatureModel___init__():
    assert sxfm_FeatureModel.__init__(sxfm_FeatureModel('', sxfm_FeatureModel10=set(), sxfm_FeatureModel=sxfm_ConstraintsSet(), sxfm_FeatureModel6=sxfm_FeatureTree(), sxfm_FeatureModel8=sxfm_MetadataSet()), '', sxfm_FeatureModel10=set(), sxfm_FeatureModel=sxfm_ConstraintsSet(), sxfm_FeatureModel6=sxfm_FeatureTree(), sxfm_FeatureModel8=sxfm_MetadataSet()) == None

