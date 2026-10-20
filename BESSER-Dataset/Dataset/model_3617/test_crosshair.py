from python_code import profile_ContextToValueSet
from python_code import profile_ValueSetConstraints

def test_profile_ContextToValueSet___init__():
    assert profile_ContextToValueSet.__init__(profile_ContextToValueSet('', '\x00', profile_ContextToValueSet=profile_ValueSetConstraints()), '\x00\x00', '', profile_ContextToValueSet=profile_ValueSetConstraints()) == None

