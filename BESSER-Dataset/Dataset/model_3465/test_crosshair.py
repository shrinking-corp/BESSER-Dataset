from python_code import featureModel_Constraint
from python_code import featureModel_Constraints

def test_featureModel_Constraint___init__():
    assert featureModel_Constraint.__init__(featureModel_Constraint('', '\x00', featureModel_Constraint=featureModel_Constraints()), '\x00\x00', '', featureModel_Constraint=featureModel_Constraints()) == None


from python_code import featureModel_Feature
from python_code import featureModel_FeatureModel

def test_featureModel_Feature___init__():
    assert featureModel_Feature.__init__(featureModel_Feature('', featureModel_Feature=featureModel_FeatureModel(), featureModel_Feature6=set()), '', featureModel_Feature=featureModel_FeatureModel(), featureModel_Feature6=set()) == None


from python_code import featureModel_PropFormula
from python_code import featureModel_Proposition

def test_featureModel_Proposition___init__():
    assert featureModel_Proposition.__init__(featureModel_Proposition('', '\x00', featureModel_Proposition=featureModel_PropFormula(), featureModel_Proposition13=featureModel_PropFormula()), '\x00\x00', '', featureModel_Proposition=featureModel_PropFormula(), featureModel_Proposition13=featureModel_PropFormula()) == None

