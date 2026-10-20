from python_code import FCORE_AttributeConstraint
from python_code import FCORE_AttributeConstraintConnection
from python_code import FCORE_FeatureModel

def test_FCORE_AttributeConstraint___init__():
    assert FCORE_AttributeConstraint.__init__(FCORE_AttributeConstraint('', target54=FCORE_AttributeConstraintConnection(), AttributeConstraint=FCORE_AttributeConstraintConnection(), FCORE_AttributeConstraint=FCORE_FeatureModel()), '', target54=FCORE_AttributeConstraintConnection(), AttributeConstraint=FCORE_AttributeConstraintConnection(), FCORE_AttributeConstraint=FCORE_FeatureModel()) == None


from python_code import FCORE_CardinalityConnection

def test_FCORE_CardinalityConnection___init__():
    assert FCORE_CardinalityConnection.__init__(FCORE_CardinalityConnection(0, 0), 0, 0) == None


from python_code import FCORE_FeatureGroup
from python_code import FCORE_FeatureModel
from python_code import FCORE_FeatureToGroupConnection
from python_code import FCORE_GroupToFeatureConnection

def test_FCORE_FeatureGroup___init__():
    assert FCORE_FeatureGroup.__init__(FCORE_FeatureGroup(0, 0, target47=FCORE_FeatureToGroupConnection(), source50=set(), FeatureGroup=FCORE_FeatureToGroupConnection(), FeatureGroup72=FCORE_GroupToFeatureConnection(), FCORE_FeatureGroup=FCORE_FeatureModel()), 0, 0, target47=FCORE_FeatureToGroupConnection(), source50=set(), FeatureGroup=FCORE_FeatureToGroupConnection(), FeatureGroup72=FCORE_GroupToFeatureConnection(), FCORE_FeatureGroup=FCORE_FeatureModel()) == None


from python_code import FCORE_FeatureModel
from python_code import FCORE_SingleFeatureConnection
from python_code import FCORE_SolitaryFeature

def test_FCORE_SolitaryFeature___init__():
    assert FCORE_SolitaryFeature.__init__(FCORE_SolitaryFeature(0, 0, target=FCORE_SingleFeatureConnection(), SolitaryFeature=FCORE_SingleFeatureConnection(), FCORE_SolitaryFeature=FCORE_FeatureModel()), 0, 0, target=FCORE_SingleFeatureConnection(), SolitaryFeature=FCORE_SingleFeatureConnection(), FCORE_SolitaryFeature=FCORE_FeatureModel()) == None

