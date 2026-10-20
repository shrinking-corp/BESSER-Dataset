from python_code import jcl_commons_CommentableElement

def test_jcl_commons_CommentableElement___init__():
    assert jcl_commons_CommentableElement.__init__(jcl_commons_CommentableElement(''), '') == None


from python_code import jcl_commons_NamedElement

def test_jcl_commons_NamedElement___init__():
    assert jcl_commons_NamedElement.__init__(jcl_commons_NamedElement(''), '') == None


from python_code import jcl_commons_PhraseableElement

def test_jcl_commons_PhraseableElement___init__():
    assert jcl_commons_PhraseableElement.__init__(jcl_commons_PhraseableElement(True), False) == None


from python_code import jcl_commons_ProcedureStepElement

def test_jcl_commons_ProcedureStepElement___init__():
    assert jcl_commons_ProcedureStepElement.__init__(jcl_commons_ProcedureStepElement(''), '') == None


from python_code import jcl_literals_IntegerLiteral

def test_jcl_literals_IntegerLiteral___init__():
    assert jcl_literals_IntegerLiteral.__init__(jcl_literals_IntegerLiteral(0), 0) == None


from python_code import jcl_containers_JobUnit
from python_code import jcl_literals_SpecialLiteral
from python_code import jcl_parameters_AccountInfo

def test_jcl_literals_SpecialLiteral___init__():
    assert jcl_literals_SpecialLiteral.__init__(jcl_literals_SpecialLiteral('', Literal=jcl_parameters_AccountInfo(), Literal15=jcl_containers_JobUnit()), '', Literal=jcl_parameters_AccountInfo(), Literal15=jcl_containers_JobUnit()) == None


from python_code import jcl_containers_JobUnit
from python_code import jcl_literals_StringLiteral
from python_code import jcl_parameters_AccountInfo

def test_jcl_literals_StringLiteral___init__():
    assert jcl_literals_StringLiteral.__init__(jcl_literals_StringLiteral('', Literal=jcl_parameters_AccountInfo(), Literal15=jcl_containers_JobUnit()), '', Literal=jcl_parameters_AccountInfo(), Literal15=jcl_containers_JobUnit()) == None


from python_code import jcl_parameters_AddressSpace

def test_jcl_parameters_AddressSpace___init__():
    assert jcl_parameters_AddressSpace.__init__(jcl_parameters_AddressSpace(''), '') == None


from python_code import jcl_parameters_Argument

def test_jcl_parameters_Argument___init__():
    assert jcl_parameters_Argument.__init__(jcl_parameters_Argument(''), '') == None


from python_code import jcl_containers_JobUnit
from python_code import jcl_parameters_Bytes
from python_code import jcl_statements_Statement

def test_jcl_parameters_Bytes___init__():
    assert jcl_parameters_Bytes.__init__(jcl_parameters_Bytes(0, Parameter12=jcl_containers_JobUnit(), Parameter=jcl_statements_Statement()), 0, Parameter12=jcl_containers_JobUnit(), Parameter=jcl_statements_Statement()) == None


from python_code import jcl_containers_JobUnit
from python_code import jcl_parameters_DatasetName
from python_code import jcl_statements_Statement

def test_jcl_parameters_DatasetName___init__():
    assert jcl_parameters_DatasetName.__init__(jcl_parameters_DatasetName('', Parameter12=jcl_containers_JobUnit(), Parameter=jcl_statements_Statement()), '', Parameter12=jcl_containers_JobUnit(), Parameter=jcl_statements_Statement()) == None


from python_code import jcl_containers_JobUnit
from python_code import jcl_parameters_Display
from python_code import jcl_statements_Statement

def test_jcl_parameters_Display___init__():
    assert jcl_parameters_Display.__init__(jcl_parameters_Display('', Parameter12=jcl_containers_JobUnit(), Parameter=jcl_statements_Statement()), '', Parameter12=jcl_containers_JobUnit(), Parameter=jcl_statements_Statement()) == None


from python_code import jcl_containers_JobUnit
from python_code import jcl_parameters_JobClass
from python_code import jcl_statements_Statement

def test_jcl_parameters_JobClass___init__():
    assert jcl_parameters_JobClass.__init__(jcl_parameters_JobClass(0, Parameter12=jcl_containers_JobUnit(), Parameter=jcl_statements_Statement()), 0, Parameter12=jcl_containers_JobUnit(), Parameter=jcl_statements_Statement()) == None


from python_code import jcl_containers_JobUnit
from python_code import jcl_parameters_MessageClass
from python_code import jcl_statements_Statement

def test_jcl_parameters_MessageClass___init__():
    assert jcl_parameters_MessageClass.__init__(jcl_parameters_MessageClass('', Parameter12=jcl_containers_JobUnit(), Parameter=jcl_statements_Statement()), '', Parameter12=jcl_containers_JobUnit(), Parameter=jcl_statements_Statement()) == None


from python_code import jcl_containers_JobUnit
from python_code import jcl_parameters_MessageLevel
from python_code import jcl_statements_Statement

def test_jcl_parameters_MessageLevel___init__():
    assert jcl_parameters_MessageLevel.__init__(jcl_parameters_MessageLevel(0, 0, Parameter12=jcl_containers_JobUnit(), Parameter=jcl_statements_Statement()), 0, 0, Parameter12=jcl_containers_JobUnit(), Parameter=jcl_statements_Statement()) == None


from python_code import jcl_parameters_Other

def test_jcl_parameters_Other___init__():
    assert jcl_parameters_Other.__init__(jcl_parameters_Other(''), '') == None


from python_code import jcl_containers_JobUnit
from python_code import jcl_parameters_Password
from python_code import jcl_statements_Statement

def test_jcl_parameters_Password___init__():
    assert jcl_parameters_Password.__init__(jcl_parameters_Password('', '\x00', Parameter12=jcl_containers_JobUnit(), Parameter=jcl_statements_Statement()), '\x00\x00', '', Parameter12=jcl_containers_JobUnit(), Parameter=jcl_statements_Statement()) == None


from python_code import jcl_containers_JobUnit
from python_code import jcl_parameters_Priority
from python_code import jcl_statements_Statement

def test_jcl_parameters_Priority___init__():
    assert jcl_parameters_Priority.__init__(jcl_parameters_Priority(0, Parameter12=jcl_containers_JobUnit(), Parameter=jcl_statements_Statement()), 0, Parameter12=jcl_containers_JobUnit(), Parameter=jcl_statements_Statement()) == None


from python_code import jcl_containers_JobUnit
from python_code import jcl_parameters_TypeRun
from python_code import jcl_statements_Statement

def test_jcl_parameters_TypeRun___init__():
    assert jcl_parameters_TypeRun.__init__(jcl_parameters_TypeRun('', Parameter12=jcl_containers_JobUnit(), Parameter=jcl_statements_Statement()), '', Parameter12=jcl_containers_JobUnit(), Parameter=jcl_statements_Statement()) == None


from python_code import jcl_containers_JobUnit
from python_code import jcl_parameters_UserID
from python_code import jcl_statements_Statement

def test_jcl_parameters_UserID___init__():
    assert jcl_parameters_UserID.__init__(jcl_parameters_UserID('', Parameter12=jcl_containers_JobUnit(), Parameter=jcl_statements_Statement()), '', Parameter12=jcl_containers_JobUnit(), Parameter=jcl_statements_Statement()) == None


from python_code import jcl_procedures_Procedure

def test_jcl_procedures_Procedure___init__():
    assert jcl_procedures_Procedure.__init__(jcl_procedures_Procedure(''), '') == None


from python_code import Expression
from python_code import jcl_statements_Command
from python_code import jcl_statements_Condition
from python_code import jcl_statements_StatementContainer

def test_jcl_statements_Command___init__():
    assert jcl_statements_Command.__init__(jcl_statements_Command('', Statement6=jcl_statements_Condition('', '', jcl_statements_Condition=set(), jcl_statements_Condition8=Expression()), Statement=jcl_statements_StatementContainer()), '', Statement6=jcl_statements_Condition('', '', jcl_statements_Condition=set(), jcl_statements_Condition8=Expression()), Statement=jcl_statements_StatementContainer()) == None


from python_code import Expression
from python_code import jcl_statements_Condition

def test_jcl_statements_Condition___init__():
    assert jcl_statements_Condition.__init__(jcl_statements_Condition('', '', jcl_statements_Condition=set(), jcl_statements_Condition8=Expression()), '', '', jcl_statements_Condition=set(), jcl_statements_Condition8=Expression()) == None


from python_code import EndControl
from python_code import Expression
from python_code import jcl_statements_Condition
from python_code import jcl_statements_Control
from python_code import jcl_statements_StatementContainer

def test_jcl_statements_Control___init__():
    assert jcl_statements_Control.__init__(jcl_statements_Control('', jcl_statements_Control=EndControl(), Statement6=jcl_statements_Condition('', '', jcl_statements_Condition=set(), jcl_statements_Condition8=Expression()), Statement=jcl_statements_StatementContainer()), '', jcl_statements_Control=EndControl(), Statement6=jcl_statements_Condition('', '', jcl_statements_Condition=set(), jcl_statements_Condition8=Expression()), Statement=jcl_statements_StatementContainer()) == None


from python_code import jcl_statements_ExecuteProcedure

def test_jcl_statements_ExecuteProcedure___init__():
    assert jcl_statements_ExecuteProcedure.__init__(jcl_statements_ExecuteProcedure(''), '') == None


from python_code import jcl_statements_ExecuteProgram

def test_jcl_statements_ExecuteProgram___init__():
    assert jcl_statements_ExecuteProgram.__init__(jcl_statements_ExecuteProgram(''), '') == None


from python_code import jcl_waters_Water

def test_jcl_waters_Water___init__():
    assert jcl_waters_Water.__init__(jcl_waters_Water(''), '') == None

