from python_code import ecdarText_ETBooleanLiteral

def test_ecdarText_ETBooleanLiteral___init__():
    assert ecdarText_ETBooleanLiteral.__init__(ecdarText_ETBooleanLiteral(''), '') == None


from python_code import ecdarText_ETExistsExpression
from python_code import ecdarText_ETExpression
from python_code import ecdarText_ETType

def test_ecdarText_ETExistsExpression___init__():
    assert ecdarText_ETExistsExpression.__init__(ecdarText_ETExistsExpression('', ecdarText_ETExistsExpression=ecdarText_ETType(), ecdarText_ETExistsExpression120=ecdarText_ETExpression()), '', ecdarText_ETExistsExpression=ecdarText_ETType(), ecdarText_ETExistsExpression120=ecdarText_ETExpression()) == None


from python_code import ecdarText_ETFieldDeclaration
from python_code import ecdarText_ETFieldID

def test_ecdarText_ETFieldID___init__():
    assert ecdarText_ETFieldID.__init__(ecdarText_ETFieldID('\x00\x00', '', ecdarText_ETFieldID=ecdarText_ETFieldDeclaration(), ecdarText_ETFieldID45=set()), '', '', ecdarText_ETFieldID=ecdarText_ETFieldDeclaration(), ecdarText_ETFieldID45=set()) == None


from python_code import ecdarText_ETExpression
from python_code import ecdarText_ETForallExpression
from python_code import ecdarText_ETType

def test_ecdarText_ETForallExpression___init__():
    assert ecdarText_ETForallExpression.__init__(ecdarText_ETForallExpression('', ecdarText_ETForallExpression=ecdarText_ETType(), ecdarText_ETForallExpression115=ecdarText_ETExpression()), '', ecdarText_ETForallExpression=ecdarText_ETType(), ecdarText_ETForallExpression115=ecdarText_ETExpression()) == None


from python_code import ecdarText_ETFile
from python_code import ecdarText_ETImport

def test_ecdarText_ETImport___init__():
    assert ecdarText_ETImport.__init__(ecdarText_ETImport('', ecdarText_ETImport=ecdarText_ETFile()), '', ecdarText_ETImport=ecdarText_ETFile()) == None


from python_code import ecdarText_ETNumberLiteral

def test_ecdarText_ETNumberLiteral___init__():
    assert ecdarText_ETNumberLiteral.__init__(ecdarText_ETNumberLiteral(0), 0) == None


from python_code import ecdarText_ETParameter
from python_code import ecdarText_ETSpecificationTemplate
from python_code import ecdarText_ETType

def test_ecdarText_ETParameter___init__():
    assert ecdarText_ETParameter.__init__(ecdarText_ETParameter('\x00\x00', '', ecdarText_ETParameter59=ecdarText_ETType(), ecdarText_ETParameter=ecdarText_ETSpecificationTemplate(), ecdarText_ETParameter62=set()), '', '', ecdarText_ETParameter59=ecdarText_ETType(), ecdarText_ETParameter=ecdarText_ETSpecificationTemplate(), ecdarText_ETParameter62=set()) == None


from python_code import ecdarText_ETFile
from python_code import ecdarText_ETSpecification
from python_code import ecdarText_ETSpecificationReference

def test_ecdarText_ETSpecification___init__():
    assert ecdarText_ETSpecification.__init__(ecdarText_ETSpecification('', ecdarText_ETSpecification=ecdarText_ETFile(), ecdarText_ETSpecification106=ecdarText_ETSpecificationReference()), '', ecdarText_ETSpecification=ecdarText_ETFile(), ecdarText_ETSpecification106=ecdarText_ETSpecificationReference()) == None


from python_code import ecdarText_ETExpression
from python_code import ecdarText_ETStructExpression

def test_ecdarText_ETStructExpression___init__():
    assert ecdarText_ETStructExpression.__init__(ecdarText_ETStructExpression('', ecdarText_ETStructExpression=ecdarText_ETExpression()), '', ecdarText_ETStructExpression=ecdarText_ETExpression()) == None


from python_code import ecdarText_ETTypeDeclaration
from python_code import ecdarText_ETTypeID
from python_code import ecdarText_ETTypeReference

def test_ecdarText_ETTypeID___init__():
    assert ecdarText_ETTypeID.__init__(ecdarText_ETTypeID('', ecdarText_ETTypeID=ecdarText_ETTypeDeclaration(), ecdarText_ETTypeID29=set(), ecdarText_ETTypeID89=ecdarText_ETTypeReference()), '', ecdarText_ETTypeID=ecdarText_ETTypeDeclaration(), ecdarText_ETTypeID29=set(), ecdarText_ETTypeID89=ecdarText_ETTypeReference()) == None


from python_code import ecdarText_ETType
from python_code import ecdarText_ETTypeModifiers

def test_ecdarText_ETTypeModifiers___init__():
    assert ecdarText_ETTypeModifiers.__init__(ecdarText_ETTypeModifiers(False, False, False, ecdarText_ETTypeModifiers=ecdarText_ETType()), False, False, False, ecdarText_ETTypeModifiers=ecdarText_ETType()) == None


from python_code import ecdarText_ETInitialiser
from python_code import ecdarText_ETVariableDeclaration
from python_code import ecdarText_ETVariableID

def test_ecdarText_ETVariableID___init__():
    assert ecdarText_ETVariableID.__init__(ecdarText_ETVariableID('\x00\x00', '', ecdarText_ETVariableID=ecdarText_ETVariableDeclaration(), ecdarText_ETVariableID16=set(), ecdarText_ETVariableID19=ecdarText_ETInitialiser()), '', '', ecdarText_ETVariableID=ecdarText_ETVariableDeclaration(), ecdarText_ETVariableID16=set(), ecdarText_ETVariableID19=ecdarText_ETInitialiser()) == None

