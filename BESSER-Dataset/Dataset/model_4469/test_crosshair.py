from python_code import logoASM_Constant

def test_logoASM_Constant___init__():
    assert logoASM_Constant.__init__(logoASM_Constant(0), 0) == None


from python_code import logoASM_ProcCall
from python_code import logoASM_ProcDeclaration

def test_logoASM_ProcDeclaration___init__():
    assert logoASM_ProcDeclaration.__init__(logoASM_ProcDeclaration('', logoASM_ProcDeclaration=logoASM_ProcCall(), logoASM_ProcDeclaration17=set(), logoASM_ProcDeclaration19=set()), '', logoASM_ProcDeclaration=logoASM_ProcCall(), logoASM_ProcDeclaration17=set(), logoASM_ProcDeclaration19=set()) == None

