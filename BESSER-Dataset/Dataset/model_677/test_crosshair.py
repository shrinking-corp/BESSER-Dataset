from python_code import emof_MultiplicityElement

def test_emof_MultiplicityElement___init__():
    assert emof_MultiplicityElement.__init__(emof_MultiplicityElement('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import emof_Comment
from python_code import emof_NamedElement

def test_emof_NamedElement___init__():
    assert emof_NamedElement.__init__(emof_NamedElement('', emof_NamedElement=emof_Comment()), '', emof_NamedElement=emof_Comment()) == None


from python_code import emof_Element
from python_code import emof_Tag

def test_emof_Tag___init__():
    assert emof_Tag.__init__(emof_Tag('\x00\x00', '', Tag=emof_Element(), tag=set()), '', '', Tag=emof_Element(), tag=set()) == None

