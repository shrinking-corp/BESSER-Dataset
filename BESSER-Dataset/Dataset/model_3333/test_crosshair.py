from python_code import jdtmm_JDTMember
from python_code import jdtmm_JDTTypeParameter

def test_jdtmm_JDTMember___init__():
    assert jdtmm_JDTMember.__init__(jdtmm_JDTMember('', '', declaringMember=set(), jdtmm_JDTMember=set(), JDTMember=jdtmm_JDTTypeParameter()), '', '', declaringMember=set(), jdtmm_JDTMember=set(), JDTMember=jdtmm_JDTTypeParameter()) == None


from python_code import jdtmm_JDTOpaqueBody

def test_jdtmm_JDTOpaqueBody___init__():
    assert jdtmm_JDTOpaqueBody.__init__(jdtmm_JDTOpaqueBody(''), '') == None

