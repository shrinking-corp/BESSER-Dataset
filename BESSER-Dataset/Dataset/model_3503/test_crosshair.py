from python_code import delphi_MineID

def test_delphi_MineID___init__():
    assert delphi_MineID.__init__(delphi_MineID('', '\x00'), '\x00\x00', '') == None

from python_code import delphi_MultipleId

def test_delphi_MultipleId___init__():
    assert delphi_MultipleId.__init__(delphi_MultipleId(''), '') == None

from python_code import delphi_adOp

def test_delphi_adOp___init__():
    assert delphi_adOp.__init__(delphi_adOp(''), '') == None

from python_code import delphi_assignmentStmnt
from python_code import delphi_designator
from python_code import delphi_expression

def test_delphi_assignmentStmnt___init__():
    assert delphi_assignmentStmnt.__init__(delphi_assignmentStmnt('', delphi_assignmentStmnt=delphi_designator(), delphi_assignmentStmnt432=delphi_expression()), '', delphi_assignmentStmnt=delphi_designator(), delphi_assignmentStmnt432=delphi_expression()) == None

from python_code import delphi_classField
from python_code import delphi_classFieldList
from python_code import delphi_objFieldList

def test_delphi_classField___init__():
    assert delphi_classField.__init__(delphi_classField('', delphi_classField=delphi_classFieldList(), delphi_classField322=delphi_objFieldList()), '', delphi_classField=delphi_classFieldList(), delphi_classField322=delphi_objFieldList()) == None

from python_code import delphi_classMethod
from python_code import delphi_classMethodList
from python_code import delphi_methodList

def test_delphi_classMethod___init__():
    assert delphi_classMethod.__init__(delphi_classMethod('', delphi_classMethod=delphi_classMethodList(), delphi_classMethod327=delphi_methodList()), '', delphi_classMethod=delphi_classMethodList(), delphi_classMethod327=delphi_methodList()) == None

from python_code import delphi_classFieldList
from python_code import delphi_classHeritage
from python_code import delphi_classMethodList
from python_code import delphi_classPropertyList
from python_code import delphi_classType

def test_delphi_classType___init__():
    assert delphi_classType.__init__(delphi_classType('', delphi_classType314=delphi_classFieldList(), delphi_classType316=delphi_classMethodList(), delphi_classType318=delphi_classPropertyList(), delphi_classType=delphi_classHeritage()), '', delphi_classType314=delphi_classFieldList(), delphi_classType316=delphi_classMethodList(), delphi_classType318=delphi_classPropertyList(), delphi_classType=delphi_classHeritage()) == None

from python_code import delphi_constExpr
from python_code import delphi_constSection
from python_code import delphi_constantDecl
from python_code import delphi_ident
from python_code import delphi_typeId
from python_code import delphi_typedConstant

def test_delphi_constantDecl___init__():
    assert delphi_constantDecl.__init__(delphi_constantDecl('', delphi_constantDecl60=delphi_constExpr(), delphi_constantDecl63=delphi_typeId(), delphi_constantDecl=delphi_constSection(), delphi_constantDecl57=delphi_ident(), delphi_constantDecl65=delphi_typedConstant()), '', delphi_constantDecl60=delphi_constExpr(), delphi_constantDecl63=delphi_typeId(), delphi_constantDecl=delphi_constSection(), delphi_constantDecl57=delphi_ident(), delphi_constantDecl65=delphi_typedConstant()) == None

from python_code import delphi_designator
from python_code import delphi_exprList
from python_code import delphi_expression
from python_code import delphi_factor
from python_code import delphi_multExp
from python_code import delphi_setConstructor
from python_code import delphi_typeId

def test_delphi_factor___init__():
    assert delphi_factor.__init__(delphi_factor('', '\x00', delphi_factor=delphi_designator(), delphi_factor167=delphi_exprList(), delphi_factor169=delphi_expression(), delphi_factor171=delphi_expression(), delphi_factor174=delphi_setConstructor(), delphi_factor176=delphi_typeId(), delphi_factor428=delphi_multExp()), '\x00\x00', '', delphi_factor=delphi_designator(), delphi_factor167=delphi_exprList(), delphi_factor169=delphi_expression(), delphi_factor171=delphi_expression(), delphi_factor174=delphi_setConstructor(), delphi_factor176=delphi_typeId(), delphi_factor428=delphi_multExp()) == None

from python_code import delphi_fieldDecl
from python_code import delphi_fieldList
from python_code import delphi_identList
from python_code import delphi_type

def test_delphi_fieldDecl___init__():
    assert delphi_fieldDecl.__init__(delphi_fieldDecl('', delphi_fieldDecl=delphi_fieldList(), delphi_fieldDecl121=delphi_identList(), delphi_fieldDecl124=delphi_type()), '', delphi_fieldDecl=delphi_fieldList(), delphi_fieldDecl121=delphi_identList(), delphi_fieldDecl124=delphi_type()) == None

from python_code import delphi_gotoStmnt

def test_delphi_gotoStmnt___init__():
    assert delphi_gotoStmnt.__init__(delphi_gotoStmnt(''), '') == None

from python_code import delphi_labelDeclSection

def test_delphi_labelDeclSection___init__():
    assert delphi_labelDeclSection.__init__(delphi_labelDeclSection(''), '') == None

from python_code import delphi_mulOp
from python_code import delphi_multExp

def test_delphi_mulOp___init__():
    assert delphi_mulOp.__init__(delphi_mulOp('', delphi_mulOp=delphi_multExp()), '', delphi_mulOp=delphi_multExp()) == None

from python_code import delphi_raiseStmt

def test_delphi_raiseStmt___init__():
    assert delphi_raiseStmt.__init__(delphi_raiseStmt('', '\x00'), '\x00\x00', '') == None

from python_code import delphi_relExp
from python_code import delphi_relOp

def test_delphi_relOp___init__():
    assert delphi_relOp.__init__(delphi_relOp('', delphi_relOp=delphi_relExp()), '', delphi_relOp=delphi_relExp()) == None

from python_code import delphi_caseSelector
from python_code import delphi_exceptionBlock
from python_code import delphi_ifStmt
from python_code import delphi_loopStmt
from python_code import delphi_statement
from python_code import delphi_stmtList
from python_code import delphi_unlabelledStatement
from python_code import delphi_withStmt

def test_delphi_statement___init__():
    assert delphi_statement.__init__(delphi_statement('', delphi_statement=delphi_stmtList(), delphi_statement203=delphi_unlabelledStatement(), delphi_statement211=delphi_ifStmt(), delphi_statement214=delphi_ifStmt(), delphi_statement234=delphi_loopStmt(), delphi_statement226=delphi_caseSelector(), delphi_statement262=delphi_exceptionBlock(), delphi_statement246=delphi_withStmt()), '', delphi_statement=delphi_stmtList(), delphi_statement203=delphi_unlabelledStatement(), delphi_statement211=delphi_ifStmt(), delphi_statement214=delphi_ifStmt(), delphi_statement234=delphi_loopStmt(), delphi_statement226=delphi_caseSelector(), delphi_statement262=delphi_exceptionBlock(), delphi_statement246=delphi_withStmt()) == None

from python_code import delphi_strucType

def test_delphi_strucType___init__():
    assert delphi_strucType.__init__(delphi_strucType(''), '') == None

from python_code import delphi_ident
from python_code import delphi_restrictedType
from python_code import delphi_type
from python_code import delphi_typeDecl
from python_code import delphi_typeSection

def test_delphi_typeDecl___init__():
    assert delphi_typeDecl.__init__(delphi_typeDecl('', delphi_typeDecl68=delphi_ident(), delphi_typeDecl71=delphi_type(), delphi_typeDecl73=delphi_restrictedType(), delphi_typeDecl=delphi_typeSection()), '', delphi_typeDecl68=delphi_ident(), delphi_typeDecl71=delphi_type(), delphi_typeDecl73=delphi_restrictedType(), delphi_typeDecl=delphi_typeSection()) == None

from python_code import delphi_implementationSection
from python_code import delphi_initSection
from python_code import delphi_interfaceSection
from python_code import delphi_unit

def test_delphi_unit___init__():
    assert delphi_unit.__init__(delphi_unit('', delphi_unit=delphi_interfaceSection(), delphi_unit8=delphi_implementationSection(), delphi_unit10=delphi_initSection()), '', delphi_unit=delphi_interfaceSection(), delphi_unit8=delphi_implementationSection(), delphi_unit10=delphi_initSection()) == None

from python_code import delphi_qualId
from python_code import delphi_typeId
from python_code import delphi_unitId

def test_delphi_unitId___init__():
    assert delphi_unitId.__init__(delphi_unitId('', delphi_unitId=delphi_qualId(), delphi_unitId401=delphi_typeId()), '', delphi_unitId=delphi_qualId(), delphi_unitId401=delphi_typeId()) == None
