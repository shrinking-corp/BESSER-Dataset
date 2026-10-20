from python_code import xpand3_SyntaxElement

def test_xpand3_SyntaxElement___init__():
    assert xpand3_SyntaxElement.__init__(xpand3_SyntaxElement(0, 0, 0, ''), 0, 0, 0, '') == None


from python_code import declaration_xpand3_Identifier
from python_code import xpand3_File
from python_code import xpand3_declaration_AbstractAspect

def test_xpand3_declaration_AbstractAspect___init__():
    assert xpand3_declaration_AbstractAspect.__init__(xpand3_declaration_AbstractAspect(True, xpand3_declaration_AbstractAspect=declaration_xpand3_Identifier(), AbstractDeclaration=xpand3_File()), False, xpand3_declaration_AbstractAspect=declaration_xpand3_Identifier(), AbstractDeclaration=xpand3_File()) == None


from python_code import AbstractExpression
from python_code import declaration_xpand3_File
from python_code import xpand3_declaration_AbstractDeclaration

def test_xpand3_declaration_AbstractDeclaration___init__():
    assert xpand3_declaration_AbstractDeclaration.__init__(xpand3_declaration_AbstractDeclaration(False, xpand3_declaration_AbstractDeclaration131=set(), xpand3_declaration_AbstractDeclaration133=AbstractExpression(), xpand3_declaration_AbstractDeclaration=declaration_xpand3_File()), True, xpand3_declaration_AbstractDeclaration131=set(), xpand3_declaration_AbstractDeclaration133=AbstractExpression(), xpand3_declaration_AbstractDeclaration=declaration_xpand3_File()) == None


from python_code import AbstractExpression
from python_code import xpand3_File
from python_code import xpand3_declaration_Check

def test_xpand3_declaration_Check___init__():
    assert xpand3_declaration_Check.__init__(xpand3_declaration_Check(True, '\x01', xpand3_declaration_Check=AbstractExpression(), xpand3_declaration_Check152=AbstractExpression(), AbstractDeclaration=xpand3_File()), False, '', xpand3_declaration_Check=AbstractExpression(), xpand3_declaration_Check152=AbstractExpression(), AbstractDeclaration=xpand3_File()) == None


from python_code import AbstractExpression
from python_code import declaration_xpand3_Identifier
from python_code import xpand3_declaration_Extension

def test_xpand3_declaration_Extension___init__():
    assert xpand3_declaration_Extension.__init__(xpand3_declaration_Extension(False, xpand3_declaration_Extension141=declaration_xpand3_Identifier(), xpand3_declaration_Extension=AbstractExpression()), False, xpand3_declaration_Extension141=declaration_xpand3_Identifier(), xpand3_declaration_Extension=AbstractExpression()) == None


from python_code import AbstractExpression
from python_code import statement_xpand3_Identifier
from python_code import xpand3_declaration_Definition
from python_code import xpand3_declaration_DefinitionAspect
from python_code import xpand3_statement_AbstractStatementWithBody
from python_code import xpand3_statement_ExpandStatement

def test_xpand3_statement_ExpandStatement___init__():
    assert xpand3_statement_ExpandStatement.__init__(xpand3_statement_ExpandStatement(False, xpand3_statement_ExpandStatement=set(), xpand3_statement_ExpandStatement84=AbstractExpression(), xpand3_statement_ExpandStatement87=AbstractExpression(), xpand3_statement_ExpandStatement90=statement_xpand3_Identifier(), AbstractStatement=xpand3_statement_AbstractStatementWithBody(), AbstractStatement148=xpand3_declaration_DefinitionAspect(), AbstractStatement137=xpand3_declaration_Definition()), True, xpand3_statement_ExpandStatement=set(), xpand3_statement_ExpandStatement84=AbstractExpression(), xpand3_statement_ExpandStatement87=AbstractExpression(), xpand3_statement_ExpandStatement90=statement_xpand3_Identifier(), AbstractStatement=xpand3_statement_AbstractStatementWithBody(), AbstractStatement148=xpand3_declaration_DefinitionAspect(), AbstractStatement137=xpand3_declaration_Definition()) == None


from python_code import AbstractExpression
from python_code import statement_xpand3_Identifier
from python_code import xpand3_statement_FileStatement

def test_xpand3_statement_FileStatement___init__():
    assert xpand3_statement_FileStatement.__init__(xpand3_statement_FileStatement(False, xpand3_statement_FileStatement99=statement_xpand3_Identifier(), xpand3_statement_FileStatement=AbstractExpression()), False, xpand3_statement_FileStatement99=statement_xpand3_Identifier(), xpand3_statement_FileStatement=AbstractExpression()) == None


from python_code import AbstractExpression
from python_code import xpand3_statement_ProtectStatement

def test_xpand3_statement_ProtectStatement___init__():
    assert xpand3_statement_ProtectStatement.__init__(xpand3_statement_ProtectStatement(False, xpand3_statement_ProtectStatement=AbstractExpression(), xpand3_statement_ProtectStatement124=AbstractExpression(), xpand3_statement_ProtectStatement127=AbstractExpression()), False, xpand3_statement_ProtectStatement=AbstractExpression(), xpand3_statement_ProtectStatement124=AbstractExpression(), xpand3_statement_ProtectStatement127=AbstractExpression()) == None


from python_code import xpand3_declaration_Definition
from python_code import xpand3_declaration_DefinitionAspect
from python_code import xpand3_statement_AbstractStatementWithBody
from python_code import xpand3_statement_TextStatement

def test_xpand3_statement_TextStatement___init__():
    assert xpand3_statement_TextStatement.__init__(xpand3_statement_TextStatement('', False, AbstractStatement=xpand3_statement_AbstractStatementWithBody(), AbstractStatement148=xpand3_declaration_DefinitionAspect(), AbstractStatement137=xpand3_declaration_Definition()), '', False, AbstractStatement=xpand3_statement_AbstractStatementWithBody(), AbstractStatement148=xpand3_declaration_DefinitionAspect(), AbstractStatement137=xpand3_declaration_Definition()) == None

