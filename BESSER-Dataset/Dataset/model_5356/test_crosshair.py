from python_code import p2_Copyright
from python_code import p2_Description
from python_code import p2_Feature
from python_code import p2_License
from python_code import p2_Vendor

def test_p2_Feature___init__():
    assert p2_Feature.__init__(p2_Feature('', p2_Feature=p2_Copyright(), p2_Feature2=p2_Description(), p2_Feature4=set(), p2_Feature6=p2_License(), p2_Feature8=p2_Vendor(), p2_Feature10=set()), '', p2_Feature=p2_Copyright(), p2_Feature2=p2_Description(), p2_Feature4=set(), p2_Feature6=p2_License(), p2_Feature8=p2_Vendor(), p2_Feature10=set()) == None


from python_code import p2_FeatureMetadata

def test_p2_FeatureMetadata___init__():
    assert p2_FeatureMetadata.__init__(p2_FeatureMetadata('', '\x00'), '\x00\x00', '') == None

