from python_code import feature_HyBooleanAttribute

def test_feature_HyBooleanAttribute___init__():
    assert feature_HyBooleanAttribute.__init__(feature_HyBooleanAttribute(True), False) == None


from python_code import feature_HyFeatureChild
from python_code import feature_HyFeatureModel
from python_code import feature_HyGroup
from python_code import feature_HyGroupComposition

def test_feature_HyGroup___init__():
    assert feature_HyGroup.__init__(feature_HyGroup(HyGroup=feature_HyFeatureModel(), compositionOf=set(), childGroup=set(), HyGroup41=feature_HyGroupComposition(), feature_HyGroup=set(), groups=feature_HyFeatureModel(), HyGroup48=feature_HyFeatureChild()), HyGroup=feature_HyFeatureModel(), compositionOf=set(), childGroup=set(), HyGroup41=feature_HyGroupComposition(), feature_HyGroup=set(), groups=feature_HyFeatureModel(), HyGroup48=feature_HyFeatureChild()) == None

def test_feature_HyGroup_isOr():
    assert feature_HyGroup.isOr(feature_HyGroup(HyGroup=feature_HyFeatureModel(), compositionOf=set(), childGroup=set(), HyGroup41=feature_HyGroupComposition(), feature_HyGroup=set(), groups=feature_HyFeatureModel(), HyGroup48=feature_HyFeatureChild()), '\x00') == None

def test_feature_HyGroup_isAnd():
    assert feature_HyGroup.isAnd(feature_HyGroup(HyGroup=feature_HyFeatureModel(), compositionOf=set(), childGroup=set(), HyGroup41=feature_HyGroupComposition(), feature_HyGroup=set(), groups=feature_HyFeatureModel(), HyGroup48=feature_HyFeatureChild()), '\x00') == None

def test_feature_HyGroup_isAlternative():
    assert feature_HyGroup.isAlternative(feature_HyGroup(HyGroup=feature_HyFeatureModel(), compositionOf=set(), childGroup=set(), HyGroup41=feature_HyGroupComposition(), feature_HyGroup=set(), groups=feature_HyFeatureModel(), HyGroup48=feature_HyFeatureChild()), '\x00') == None


from python_code import feature_HyNumberAttribute

def test_feature_HyNumberAttribute___init__():
    assert feature_HyNumberAttribute.__init__(feature_HyNumberAttribute(0, 0, 0), 0, 0, 0) == None


from python_code import feature_HyStringAttribute

def test_feature_HyStringAttribute___init__():
    assert feature_HyStringAttribute.__init__(feature_HyStringAttribute(''), '') == None

