from python_code import Make_Comment

def test_Make_Comment___init__():
    assert Make_Comment.__init__(Make_Comment(''), '') == None


from python_code import Make_Element

def test_Make_Element___init__():
    assert Make_Element.__init__(Make_Element(''), '') == None


from python_code import Make_FileDep
from python_code import Make_Rule

def test_Make_FileDep___init__():
    assert Make_FileDep.__init__(Make_FileDep('', Dependency=Make_Rule()), '', Dependency=Make_Rule()) == None


from python_code import Comment
from python_code import Make_Macro
from python_code import Make_Makefile

def test_Make_Macro___init__():
    assert Make_Macro.__init__(Make_Macro('\x00\x00', Element=Make_Makefile('', Make_Makefile2=set(), Make_Makefile=Comment())), '', Element=Make_Makefile('', Make_Makefile2=set(), Make_Makefile=Comment())) == None


from python_code import Comment
from python_code import Make_Makefile

def test_Make_Makefile___init__():
    assert Make_Makefile.__init__(Make_Makefile('', Make_Makefile2=set(), Make_Makefile=Comment()), '', Make_Makefile2=set(), Make_Makefile=Comment()) == None


from python_code import Make_ShellLine
from python_code import Rule

def test_Make_ShellLine___init__():
    assert Make_ShellLine.__init__(Make_ShellLine('', '\x00', shellLines=Rule()), '\x00\x00', '', shellLines=Rule()) == None

