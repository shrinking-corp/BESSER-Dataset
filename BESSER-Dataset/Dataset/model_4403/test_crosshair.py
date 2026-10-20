from python_code import featureModel_FeatureGroup

def test_featureModel_FeatureGroup___init__():
    assert featureModel_FeatureGroup.__init__(featureModel_FeatureGroup(0, 0, '', featureModel_FeatureGroup=set()), 0, 0, '', featureModel_FeatureGroup=set()) == None


from python_code import featureModel_Project

def test_featureModel_Project___init__():
    assert featureModel_Project.__init__(featureModel_Project('', '', 0, False, False, featureModel_Project=set(), featureModel_Project15=set()), '', '', 0, False, False, featureModel_Project=set(), featureModel_Project15=set()) == None

