from python_code import selflet_Abilities
from python_code import selflet_Ability
from python_code import selflet_Methods

def test_selflet_Ability___init__():
    assert selflet_Ability.__init__(selflet_Ability('', '\x00', selflet_Ability=selflet_Abilities(), selflet_Ability2=selflet_Methods()), '\x00\x00', '', selflet_Ability=selflet_Abilities(), selflet_Ability2=selflet_Methods()) == None


from python_code import selflet_AbilityState
from python_code import selflet_Action
from python_code import selflet_Actions

def test_selflet_Action___init__():
    assert selflet_Action.__init__(selflet_Action('', selflet_Action=selflet_Actions(), selflet_Action65=selflet_AbilityState()), '', selflet_Action=selflet_Actions(), selflet_Action65=selflet_AbilityState()) == None


from python_code import selflet_CPUUtilization

def test_selflet_CPUUtilization___init__():
    assert selflet_CPUUtilization.__init__(selflet_CPUUtilization('', '\x00'), '\x00\x00', '') == None


from python_code import selflet_Condition
from python_code import selflet_Conditions

def test_selflet_Condition___init__():
    assert selflet_Condition.__init__(selflet_Condition('', selflet_Condition=selflet_Conditions()), '', selflet_Condition=selflet_Conditions()) == None


from python_code import selflet_Method
from python_code import selflet_Methods

def test_selflet_Method___init__():
    assert selflet_Method.__init__(selflet_Method('', '\x00', selflet_Method=selflet_Methods()), '\x00\x00', '', selflet_Method=selflet_Methods()) == None


from python_code import selflet_Input
from python_code import selflet_Output
from python_code import selflet_Parameter

def test_selflet_Parameter___init__():
    assert selflet_Parameter.__init__(selflet_Parameter('', '\x00', selflet_Parameter=selflet_Input(), selflet_Parameter11=selflet_Output()), '\x00\x00', '', selflet_Parameter=selflet_Input(), selflet_Parameter11=selflet_Output()) == None


from python_code import selflet_Rule
from python_code import selflet_Rules

def test_selflet_Rule___init__():
    assert selflet_Rule.__init__(selflet_Rule('', selflet_Rule=selflet_Rules()), '', selflet_Rule=selflet_Rules()) == None


from python_code import selflet_GeneralKnowledge
from python_code import selflet_SelfLetProperty
from python_code import selflet_TypeKnowledge

def test_selflet_SelfLetProperty___init__():
    assert selflet_SelfLetProperty.__init__(selflet_SelfLetProperty('', '', '\x00\x00', selflet_SelfLetProperty=selflet_GeneralKnowledge(), selflet_SelfLetProperty57=selflet_TypeKnowledge()), '', '', '', selflet_SelfLetProperty=selflet_GeneralKnowledge(), selflet_SelfLetProperty57=selflet_TypeKnowledge()) == None

