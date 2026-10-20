from python_code import featureModelMetamodel_ClonableSelection

def test_featureModelMetamodel_ClonableSelection___init__():
    assert featureModelMetamodel_ClonableSelection.__init__(featureModelMetamodel_ClonableSelection(''), '') == None


from python_code import featureModelMetamodel_Constraint
from python_code import featureModelMetamodel_FeatureModel

def test_featureModelMetamodel_Constraint___init__():
    assert featureModelMetamodel_Constraint.__init__(featureModelMetamodel_Constraint('', '', '\x00\x00', featureModelMetamodel_Constraint=featureModelMetamodel_FeatureModel()), '', '', '', featureModelMetamodel_Constraint=featureModelMetamodel_FeatureModel()) == None


from python_code import featureModelMetamodel_ClonableFeature
from python_code import featureModelMetamodel_Multiplicity_

def test_featureModelMetamodel_Multiplicity____init__():
    assert featureModelMetamodel_Multiplicity_.__init__(featureModelMetamodel_Multiplicity_('', '\x00', featureModelMetamodel_Multiplicity=featureModelMetamodel_ClonableFeature()), '\x00\x00', '', featureModelMetamodel_Multiplicity=featureModelMetamodel_ClonableFeature()) == None

