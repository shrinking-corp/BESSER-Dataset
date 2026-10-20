from python_code import umlTransition_AnyReceiveEventRule

def test_umlTransition_AnyReceiveEventRule___init__():
    assert umlTransition_AnyReceiveEventRule.__init__(umlTransition_AnyReceiveEventRule(''), '') == None


from python_code import umlTransition_ChangeEventRule

def test_umlTransition_ChangeEventRule___init__():
    assert umlTransition_ChangeEventRule.__init__(umlTransition_ChangeEventRule(''), '') == None


from python_code import umlTransition_EffectRule
from python_code import umlTransition_TransitionRule

def test_umlTransition_EffectRule___init__():
    assert umlTransition_EffectRule.__init__(umlTransition_EffectRule('', '\x00', umlTransition_EffectRule=umlTransition_TransitionRule()), '\x00\x00', '', umlTransition_EffectRule=umlTransition_TransitionRule()) == None


from python_code import umlTransition_GuardRule
from python_code import umlTransition_TransitionRule

def test_umlTransition_GuardRule___init__():
    assert umlTransition_GuardRule.__init__(umlTransition_GuardRule('', umlTransition_GuardRule=umlTransition_TransitionRule()), '', umlTransition_GuardRule=umlTransition_TransitionRule()) == None


from python_code import umlTransition_TimeEventRule

def test_umlTransition_TimeEventRule___init__():
    assert umlTransition_TimeEventRule.__init__(umlTransition_TimeEventRule(''), '') == None

