from python_code import sparql_BLANK_NODE_LABEL

def test_sparql_BLANK_NODE_LABEL___init__():
    assert sparql_BLANK_NODE_LABEL.__init__(sparql_BLANK_NODE_LABEL(''), '') == None


from python_code import sparql_DECIMAL

def test_sparql_DECIMAL___init__():
    assert sparql_DECIMAL.__init__(sparql_DECIMAL(''), '') == None


from python_code import sparql_DOUBLE

def test_sparql_DOUBLE___init__():
    assert sparql_DOUBLE.__init__(sparql_DOUBLE(''), '') == None


from python_code import sparql_INTEGER
from python_code import sparql_LimitClause
from python_code import sparql_OffsetClause

def test_sparql_INTEGER___init__():
    assert sparql_INTEGER.__init__(sparql_INTEGER('', sparql_INTEGER=sparql_LimitClause(), sparql_INTEGER71=sparql_OffsetClause()), '', sparql_INTEGER=sparql_LimitClause(), sparql_INTEGER71=sparql_OffsetClause()) == None


from python_code import sparql_BaseDecl
from python_code import sparql_IRI_REF
from python_code import sparql_PrefixDecl

def test_sparql_IRI_REF___init__():
    assert sparql_IRI_REF.__init__(sparql_IRI_REF('', sparql_IRI_REF=sparql_BaseDecl(), sparql_IRI_REF13=sparql_PrefixDecl()), '', sparql_IRI_REF=sparql_BaseDecl(), sparql_IRI_REF13=sparql_PrefixDecl()) == None


from python_code import sparql_LANGTAG

def test_sparql_LANGTAG___init__():
    assert sparql_LANGTAG.__init__(sparql_LANGTAG(''), '') == None


from python_code import sparql_LocatedElement

def test_sparql_LocatedElement___init__():
    assert sparql_LocatedElement.__init__(sparql_LocatedElement('', '', '\x00\x00'), '', '', '') == None


from python_code import sparql_PNAME_NS
from python_code import sparql_PrefixDecl

def test_sparql_PNAME_NS___init__():
    assert sparql_PNAME_NS.__init__(sparql_PNAME_NS('', sparql_PNAME_NS=sparql_PrefixDecl()), '', sparql_PNAME_NS=sparql_PrefixDecl()) == None


from python_code import sparql_PNAME_LN
from python_code import sparql_PN_LOCAL

def test_sparql_PN_LOCAL___init__():
    assert sparql_PN_LOCAL.__init__(sparql_PN_LOCAL('', sparql_PN_LOCAL=sparql_PNAME_LN()), '', sparql_PN_LOCAL=sparql_PNAME_LN()) == None


from python_code import sparql_PN_PREFIX

def test_sparql_PN_PREFIX___init__():
    assert sparql_PN_PREFIX.__init__(sparql_PN_PREFIX(''), '') == None


from python_code import sparql_STRING_LITERAL1

def test_sparql_STRING_LITERAL1___init__():
    assert sparql_STRING_LITERAL1.__init__(sparql_STRING_LITERAL1(''), '') == None


from python_code import sparql_STRING_LITERAL2

def test_sparql_STRING_LITERAL2___init__():
    assert sparql_STRING_LITERAL2.__init__(sparql_STRING_LITERAL2(''), '') == None


from python_code import sparql_STRING_LITERAL_LONG1

def test_sparql_STRING_LITERAL_LONG1___init__():
    assert sparql_STRING_LITERAL_LONG1.__init__(sparql_STRING_LITERAL_LONG1(''), '') == None


from python_code import sparql_STRING_LITERAL_LONG2

def test_sparql_STRING_LITERAL_LONG2___init__():
    assert sparql_STRING_LITERAL_LONG2.__init__(sparql_STRING_LITERAL_LONG2(''), '') == None


from python_code import sparql_VAR1
from python_code import sparql_VAR2
from python_code import sparql_VARNAME

def test_sparql_VARNAME___init__():
    assert sparql_VARNAME.__init__(sparql_VARNAME('', sparql_VARNAME=sparql_VAR1(), sparql_VARNAME237=sparql_VAR2()), '', sparql_VARNAME=sparql_VAR1(), sparql_VARNAME237=sparql_VAR2()) == None


from python_code import sparql_BoundBuiltInCallNE
from python_code import sparql_SelectQuery
from python_code import sparql_SomeVariablesNE
from python_code import sparql_Var

def test_sparql_Var___init__():
    assert sparql_Var.__init__(sparql_Var('', sparql_Var=sparql_SelectQuery(), sparql_Var73=sparql_SomeVariablesNE(), sparql_Var137=sparql_BoundBuiltInCallNE()), '', sparql_Var=sparql_SelectQuery(), sparql_Var73=sparql_SomeVariablesNE(), sparql_Var137=sparql_BoundBuiltInCallNE()) == None


from python_code import sparql_VerbANE

def test_sparql_VerbANE___init__():
    assert sparql_VerbANE.__init__(sparql_VerbANE(''), '') == None


from python_code import sparql_ANON
from python_code import sparql_NotInList
from python_code import sparql_WS

def test_sparql_WS___init__():
    assert sparql_WS.__init__(sparql_WS('', sparql_WS=sparql_NotInList(), sparql_WS242=sparql_ANON()), '', sparql_WS=sparql_NotInList(), sparql_WS242=sparql_ANON()) == None

