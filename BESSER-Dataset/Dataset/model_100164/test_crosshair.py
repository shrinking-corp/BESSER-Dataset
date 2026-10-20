from python_code import plsql_declaration_NamedElement

def test_plsql_declaration_NamedElement___init__():
    assert plsql_declaration_NamedElement.__init__(plsql_declaration_NamedElement(''), '') == None


from python_code import plsql_statement_ExceptionSection

def test_plsql_statement_ExceptionSection___init__():
    assert plsql_statement_ExceptionSection.__init__(plsql_statement_ExceptionSection('', plsql_statement_ExceptionSection=set()), '', plsql_statement_ExceptionSection=set()) == None


from python_code import plsql_statement_InsertStatement

def test_plsql_statement_InsertStatement___init__():
    assert plsql_statement_InsertStatement.__init__(plsql_statement_InsertStatement('\x00\x00', '', plsql_statement_InsertStatement=set()), '', '', plsql_statement_InsertStatement=set()) == None


from python_code import plsql_declaration_FunctionDeclaration
from python_code import plsql_declaration_Package
from python_code import plsql_declaration_ProcedureDeclaration
from python_code import plsql_statement_BlockStatement
from python_code import plsql_statement_ExceptionSection
from python_code import plsql_statement_IfStatement
from python_code import plsql_statement_LoopStatement
from python_code import plsql_statement_RaiseStatement

def test_plsql_statement_RaiseStatement___init__():
    assert plsql_statement_RaiseStatement.__init__(plsql_statement_RaiseStatement('\x00\x00', Statement=plsql_statement_IfStatement(), Statement24=plsql_statement_BlockStatement(), Statement12=plsql_statement_IfStatement(), Statement119=plsql_declaration_ProcedureDeclaration(), Statement127=plsql_declaration_FunctionDeclaration(), Statement137=plsql_declaration_Package(), Statement54=plsql_statement_ExceptionSection('', plsql_statement_ExceptionSection=set()), Statement14=plsql_statement_LoopStatement()), '', Statement=plsql_statement_IfStatement(), Statement24=plsql_statement_BlockStatement(), Statement12=plsql_statement_IfStatement(), Statement119=plsql_declaration_ProcedureDeclaration(), Statement127=plsql_declaration_FunctionDeclaration(), Statement137=plsql_declaration_Package(), Statement54=plsql_statement_ExceptionSection('', plsql_statement_ExceptionSection=set()), Statement14=plsql_statement_LoopStatement()) == None


from python_code import plsql_type_Datatype
from python_code import plsql_type_TypedElement

def test_plsql_type_Datatype___init__():
    assert plsql_type_Datatype.__init__(plsql_type_Datatype('', 0, Type=plsql_type_TypedElement()), '', 0, Type=plsql_type_TypedElement()) == None


from python_code import plsql_type_IndirectType
from python_code import plsql_type_TypedElement

def test_plsql_type_IndirectType___init__():
    assert plsql_type_IndirectType.__init__(plsql_type_IndirectType('\x00\x00', False, False, 0, Type=plsql_type_TypedElement()), '', False, False, 0, Type=plsql_type_TypedElement()) == None

