from python_code import kmLogo_Constant

def test_kmLogo_Constant___init__():
    assert kmLogo_Constant.__init__(kmLogo_Constant(''), '') == None


from python_code import kmLogo_ProcCall
from python_code import kmLogo_ProcDeclaration

def test_kmLogo_ProcDeclaration___init__():
    assert kmLogo_ProcDeclaration.__init__(kmLogo_ProcDeclaration('', ProcDeclaration=kmLogo_ProcCall(), kmLogo_ProcDeclaration=set(), declaration=set(), kmLogo_ProcDeclaration18=set()), '', ProcDeclaration=kmLogo_ProcCall(), kmLogo_ProcDeclaration=set(), declaration=set(), kmLogo_ProcDeclaration18=set()) == None

