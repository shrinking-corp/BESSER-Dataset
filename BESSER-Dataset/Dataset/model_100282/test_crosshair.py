from python_code import highlevelnets_common_IEntityIdentifiable

def test_highlevelnets_common_IEntityIdentifiable___init__():
    assert highlevelnets_common_IEntityIdentifiable.__init__(highlevelnets_common_IEntityIdentifiable(''), '') == None


from python_code import highlevelnets_common_INetElement

def test_highlevelnets_common_INetElement___init__():
    assert highlevelnets_common_INetElement.__init__(highlevelnets_common_INetElement('', '\x00'), '\x00\x00', '') == None


from python_code import Arc
from python_code import NPNDiagramNetSystem
from python_code import highlevelnets_npndiagrams_NPNSymbolArcSN

def test_highlevelnets_npndiagrams_NPNSymbolArcSN___init__():
    assert highlevelnets_npndiagrams_NPNSymbolArcSN.__init__(highlevelnets_npndiagrams_NPNSymbolArcSN('', arcs142=NPNDiagramNetSystem(), highlevelnets_npndiagrams_NPNSymbolArcSN=Arc()), '\x00', arcs142=NPNDiagramNetSystem(), highlevelnets_npndiagrams_NPNSymbolArcSN=Arc()) == None


from python_code import NPNDiagramNetSystem
from python_code import Node
from python_code import highlevelnets_npndiagrams_NPNSymbolNodeSN

def test_highlevelnets_npndiagrams_NPNSymbolNodeSN___init__():
    assert highlevelnets_npndiagrams_NPNSymbolNodeSN.__init__(highlevelnets_npndiagrams_NPNSymbolNodeSN('', highlevelnets_npndiagrams_NPNSymbolNodeSN=Node(), nodes137=NPNDiagramNetSystem()), '\x00', highlevelnets_npndiagrams_NPNSymbolNodeSN=Node(), nodes137=NPNDiagramNetSystem()) == None


from python_code import highlevelnets_npnets_Synchronization

def test_highlevelnets_npnets_Synchronization___init__():
    assert highlevelnets_npnets_Synchronization.__init__(highlevelnets_npnets_Synchronization('\x00\x00', '', synchronization=set()), '', '', synchronization=set()) == None


from python_code import Variable
from python_code import highlevelnets_tokenexpressions_Monom

def test_highlevelnets_tokenexpressions_Monom___init__():
    assert highlevelnets_tokenexpressions_Monom.__init__(highlevelnets_tokenexpressions_Monom('', highlevelnets_tokenexpressions_Monom=Variable()), '', highlevelnets_tokenexpressions_Monom=Variable()) == None


from python_code import Token
from python_code import Variable
from python_code import highlevelnets_tokenexpressions_MonomConstant

def test_highlevelnets_tokenexpressions_MonomConstant___init__():
    assert highlevelnets_tokenexpressions_MonomConstant.__init__(highlevelnets_tokenexpressions_MonomConstant('', highlevelnets_tokenexpressions_MonomConstant=Variable(), highlevelnets_tokenexpressions_MonomConstant51=Token()), '\x00', highlevelnets_tokenexpressions_MonomConstant=Variable(), highlevelnets_tokenexpressions_MonomConstant51=Token()) == None


from python_code import Token
from python_code import highlevelnets_tokenexpressions_TokenWeight

def test_highlevelnets_tokenexpressions_TokenWeight___init__():
    assert highlevelnets_tokenexpressions_TokenWeight.__init__(highlevelnets_tokenexpressions_TokenWeight('', highlevelnets_tokenexpressions_TokenWeight=Token()), '\x00', highlevelnets_tokenexpressions_TokenWeight=Token()) == None


from python_code import ContextVariable
from python_code import highlevelnets_tokenexpressions_Variable

def test_highlevelnets_tokenexpressions_Variable___init__():
    assert highlevelnets_tokenexpressions_Variable.__init__(highlevelnets_tokenexpressions_Variable('', variables=ContextVariable()), '', variables=ContextVariable()) == None


from python_code import highlevelnets_tokentypes_Token

def test_highlevelnets_tokentypes_Token___init__():
    assert highlevelnets_tokentypes_Token.__init__(highlevelnets_tokentypes_Token(highlevelnets_tokentypes_Token=set()), highlevelnets_tokentypes_Token=set()) == None

def test_highlevelnets_tokentypes_Token_getType():
    assert highlevelnets_tokentypes_Token.getType(highlevelnets_tokentypes_Token(highlevelnets_tokentypes_Token=set())) == None


from python_code import highlevelnets_tokentypes_TokenAttribute

def test_highlevelnets_tokentypes_TokenAttribute___init__():
    assert highlevelnets_tokentypes_TokenAttribute.__init__(highlevelnets_tokentypes_TokenAttribute('', '', '\x00\x00'), '', '', '') == None


from python_code import HighLevelPetriNet
from python_code import highlevelnets_tokentypes_TokenTypeElementNet

def test_highlevelnets_tokentypes_TokenTypeElementNet___init__():
    assert highlevelnets_tokentypes_TokenTypeElementNet.__init__(highlevelnets_tokentypes_TokenTypeElementNet(type10=set(), highlevelnets_tokentypes_TokenTypeElementNet=HighLevelPetriNet(), type14=set()), type10=set(), highlevelnets_tokentypes_TokenTypeElementNet=HighLevelPetriNet(), type14=set()) == None

def test_highlevelnets_tokentypes_TokenTypeElementNet_getInstanceByID():
    assert highlevelnets_tokentypes_TokenTypeElementNet.getInstanceByID(highlevelnets_tokentypes_TokenTypeElementNet(type10=set(), highlevelnets_tokentypes_TokenTypeElementNet=HighLevelPetriNet(), type14=set()), 0) == None

def test_highlevelnets_tokentypes_TokenTypeElementNet_createInstance():
    assert highlevelnets_tokentypes_TokenTypeElementNet.createInstance(highlevelnets_tokentypes_TokenTypeElementNet(type10=set(), highlevelnets_tokentypes_TokenTypeElementNet=HighLevelPetriNet(), type14=set())) == None

