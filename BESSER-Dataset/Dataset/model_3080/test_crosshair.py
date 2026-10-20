from python_code import caltrop_ActionPattern

def test_caltrop_ActionPattern___init__():
    assert caltrop_ActionPattern.__init__(caltrop_ActionPattern()) == None

def test_caltrop_ActionPattern_getGuardExpression():
    assert caltrop_ActionPattern.getGuardExpression(caltrop_ActionPattern()) == None

def test_caltrop_ActionPattern_getPatternVariables():
    assert caltrop_ActionPattern.getPatternVariables(caltrop_ActionPattern()) == None


from python_code import caltrop_ConversionRelation
from python_code import caltrop_XExpression

def test_caltrop_ConversionRelation___init__():
    assert caltrop_ConversionRelation.__init__(caltrop_ConversionRelation('', caltrop_ConversionRelation=caltrop_XExpression(), caltrop_ConversionRelation74=caltrop_XExpression()), '', caltrop_ConversionRelation=caltrop_XExpression(), caltrop_ConversionRelation74=caltrop_XExpression()) == None


from python_code import caltrop_ExpressionChannelSelector

def test_caltrop_ExpressionChannelSelector___init__():
    assert caltrop_ExpressionChannelSelector.__init__(caltrop_ExpressionChannelSelector(False, caltrop_ExpressionChannelSelector=set()), False, caltrop_ExpressionChannelSelector=set()) == None


from python_code import caltrop_FireAction
from python_code import caltrop_InputPattern

def test_caltrop_InputPattern___init__():
    assert caltrop_InputPattern.__init__(caltrop_InputPattern('', caltrop_InputPattern=caltrop_FireAction()), '', caltrop_InputPattern=caltrop_FireAction()) == None


from python_code import caltrop_KeywordChannelSelector

def test_caltrop_KeywordChannelSelector___init__():
    assert caltrop_KeywordChannelSelector.__init__(caltrop_KeywordChannelSelector(''), '') == None


from python_code import caltrop_CaltropActorImpl
from python_code import caltrop_OutputAction
from python_code import caltrop_Transition
from python_code import caltrop_XExpression

def test_caltrop_OutputAction___init__():
    assert caltrop_OutputAction.__init__(caltrop_OutputAction(caltrop_OutputAction15=caltrop_XExpression(), caltrop_OutputAction18=set(), caltrop_OutputAction20=caltrop_XExpression(), caltrop_OutputAction23=caltrop_XExpression(), caltrop_OutputAction26=caltrop_XExpression(), caltrop_OutputAction60=caltrop_Transition(), caltrop_OutputAction=caltrop_CaltropActorImpl()), caltrop_OutputAction15=caltrop_XExpression(), caltrop_OutputAction18=set(), caltrop_OutputAction20=caltrop_XExpression(), caltrop_OutputAction23=caltrop_XExpression(), caltrop_OutputAction26=caltrop_XExpression(), caltrop_OutputAction60=caltrop_Transition(), caltrop_OutputAction=caltrop_CaltropActorImpl()) == None

def test_caltrop_OutputAction_getInputPatterns():
    assert caltrop_OutputAction.getInputPatterns(caltrop_OutputAction(caltrop_OutputAction15=caltrop_XExpression(), caltrop_OutputAction18=set(), caltrop_OutputAction20=caltrop_XExpression(), caltrop_OutputAction23=caltrop_XExpression(), caltrop_OutputAction26=caltrop_XExpression(), caltrop_OutputAction60=caltrop_Transition(), caltrop_OutputAction=caltrop_CaltropActorImpl())) == None


from python_code import caltrop_ChannelSelector
from python_code import caltrop_Port
from python_code import caltrop_PortPattern
from python_code import caltrop_XExpression

def test_caltrop_PortPattern___init__():
    assert caltrop_PortPattern.__init__(caltrop_PortPattern(caltrop_PortPattern=caltrop_XExpression(), caltrop_PortPattern31=caltrop_ChannelSelector(), caltrop_PortPattern33=caltrop_Port(), caltrop_PortPattern35=caltrop_XExpression()), caltrop_PortPattern=caltrop_XExpression(), caltrop_PortPattern31=caltrop_ChannelSelector(), caltrop_PortPattern33=caltrop_Port(), caltrop_PortPattern35=caltrop_XExpression()) == None

def test_caltrop_PortPattern_size():
    assert caltrop_PortPattern.size(caltrop_PortPattern(caltrop_PortPattern=caltrop_XExpression(), caltrop_PortPattern31=caltrop_ChannelSelector(), caltrop_PortPattern33=caltrop_Port(), caltrop_PortPattern35=caltrop_XExpression())) == None

