from python_code import stext_EntryPointSpec

def test_stext_EntryPointSpec___init__():
    assert stext_EntryPointSpec.__init__(stext_EntryPointSpec(''), '') == None


from python_code import stext_ExitPointSpec

def test_stext_ExitPointSpec___init__():
    assert stext_ExitPointSpec.__init__(stext_ExitPointSpec(''), '') == None


from python_code import stext_Expression
from python_code import stext_TimeEventSpec

def test_stext_TimeEventSpec___init__():
    assert stext_TimeEventSpec.__init__(stext_TimeEventSpec('', '\x00', stext_TimeEventSpec=stext_Expression()), '\x00\x00', '', stext_TimeEventSpec=stext_Expression()) == None

