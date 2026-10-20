from python_code import stext_EntryPointSpec

def test_stext_EntryPointSpec___init__():
    assert stext_EntryPointSpec.__init__(stext_EntryPointSpec(''), '') == None


from python_code import stext_EventDefinition

def test_stext_EventDefinition___init__():
    assert stext_EventDefinition.__init__(stext_EventDefinition(''), '') == None


from python_code import stext_ExitPointSpec

def test_stext_ExitPointSpec___init__():
    assert stext_ExitPointSpec.__init__(stext_ExitPointSpec(''), '') == None


from python_code import stext_Import
from python_code import stext_ImportScope

def test_stext_Import___init__():
    assert stext_Import.__init__(stext_Import('', stext_Import=stext_ImportScope()), '', stext_Import=stext_ImportScope()) == None


from python_code import stext_Expression
from python_code import stext_TimeEventSpec

def test_stext_TimeEventSpec___init__():
    assert stext_TimeEventSpec.__init__(stext_TimeEventSpec('', '\x00', stext_TimeEventSpec=stext_Expression()), '\x00\x00', '', stext_TimeEventSpec=stext_Expression()) == None


from python_code import stext_Expression
from python_code import stext_VariableDefinition

def test_stext_VariableDefinition___init__():
    assert stext_VariableDefinition.__init__(stext_VariableDefinition(False, False, stext_VariableDefinition=stext_Expression()), False, False, stext_VariableDefinition=stext_Expression()) == None

