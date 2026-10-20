from python_code import jDOQL_FromClause
from python_code import jDOQL_SingleStringJDOQL

def test_jDOQL_FromClause___init__():
    assert jDOQL_FromClause.__init__(jDOQL_FromClause('', False, jDOQL_FromClause=jDOQL_SingleStringJDOQL()), '', False, jDOQL_FromClause=jDOQL_SingleStringJDOQL()) == None


from python_code import jDOQL_ImportClause
from python_code import jDOQL_SingleStringJDOQL
from python_code import jDOQL_Subquery

def test_jDOQL_ImportClause___init__():
    assert jDOQL_ImportClause.__init__(jDOQL_ImportClause('', jDOQL_ImportClause=jDOQL_SingleStringJDOQL(), jDOQL_ImportClause31=jDOQL_Subquery()), '', jDOQL_ImportClause=jDOQL_SingleStringJDOQL(), jDOQL_ImportClause31=jDOQL_Subquery()) == None


from python_code import jDOQL_ParameterDeclaration
from python_code import jDOQL_ParametersClause

def test_jDOQL_ParameterDeclaration___init__():
    assert jDOQL_ParameterDeclaration.__init__(jDOQL_ParameterDeclaration('', '\x00', jDOQL_ParameterDeclaration=jDOQL_ParametersClause()), '\x00\x00', '', jDOQL_ParameterDeclaration=jDOQL_ParametersClause()) == None


from python_code import jDOQL_ResultClause

def test_jDOQL_ResultClause___init__():
    assert jDOQL_ResultClause.__init__(jDOQL_ResultClause(False, jDOQL_ResultClause=set()), False, jDOQL_ResultClause=set()) == None


from python_code import jDOQL_VariableDeclaration
from python_code import jDOQL_VariablesClause

def test_jDOQL_VariableDeclaration___init__():
    assert jDOQL_VariableDeclaration.__init__(jDOQL_VariableDeclaration('', '\x00', jDOQL_VariableDeclaration=jDOQL_VariablesClause()), '\x00\x00', '', jDOQL_VariableDeclaration=jDOQL_VariablesClause()) == None

