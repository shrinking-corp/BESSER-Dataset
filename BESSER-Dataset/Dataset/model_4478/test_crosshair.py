from python_code import kmLogo_Constant

def test_kmLogo_Constant___init__():
    assert kmLogo_Constant.__init__(kmLogo_Constant(0.0), 0.0) == None


from python_code import kmLogo_ProcCall
from python_code import kmLogo_ProcDeclaration

def test_kmLogo_ProcDeclaration___init__():
    assert kmLogo_ProcDeclaration.__init__(kmLogo_ProcDeclaration('', ProcDeclaration=kmLogo_ProcCall(), kmLogo_ProcDeclaration=set(), declaration=set(), kmLogo_ProcDeclaration20=set()), '', ProcDeclaration=kmLogo_ProcCall(), kmLogo_ProcDeclaration=set(), declaration=set(), kmLogo_ProcDeclaration20=set()) == None


from python_code import kmLogo_StackFrame
from python_code import kmLogo_Variable

def test_kmLogo_Variable___init__():
    assert kmLogo_Variable.__init__(kmLogo_Variable('\x00', 0.0, kmLogo_Variable=kmLogo_StackFrame()), '', 0.0, kmLogo_Variable=kmLogo_StackFrame()) == None

