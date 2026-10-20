from python_code import StatementWithNestedBlocks
from python_code import behavioral_actions_Block

def test_behavioral_actions_Block___init__():
    assert behavioral_actions_Block.__init__(behavioral_actions_Block(block=set(), owner=set(), nestedBlocks=StatementWithNestedBlocks()), block=set(), owner=set(), nestedBlocks=StatementWithNestedBlocks()) == None

def test_behavioral_actions_Block_getNamedValuesInScope():
    assert behavioral_actions_Block.getNamedValuesInScope(behavioral_actions_Block(block=set(), owner=set(), nestedBlocks=StatementWithNestedBlocks())) == None

def test_behavioral_actions_Block_getOutermostBlock():
    assert behavioral_actions_Block.getOutermostBlock(behavioral_actions_Block(block=set(), owner=set(), nestedBlocks=StatementWithNestedBlocks())) == None

def test_behavioral_actions_Block_getOwningClass():
    assert behavioral_actions_Block.getOwningClass(behavioral_actions_Block(block=set(), owner=set(), nestedBlocks=StatementWithNestedBlocks())) == None

def test_behavioral_actions_Block_localIsSideEffectFree():
    assert behavioral_actions_Block.localIsSideEffectFree(behavioral_actions_Block(block=set(), owner=set(), nestedBlocks=StatementWithNestedBlocks())) == None


from python_code import Expression
from python_code import Iterator
from python_code import behavioral_actions_Foreach

def test_behavioral_actions_Foreach___init__():
    assert behavioral_actions_Foreach.__init__(behavioral_actions_Foreach(True, behavioral_actions_Foreach=Expression(), boundToFor=Iterator()), False, behavioral_actions_Foreach=Expression(), boundToFor=Iterator()) == None


from python_code import behavioral_actions_IfElse

def test_behavioral_actions_IfElse___init__():
    assert behavioral_actions_IfElse.__init__(behavioral_actions_IfElse()) == None

def test_behavioral_actions_IfElse_getElseBlock():
    assert behavioral_actions_IfElse.getElseBlock(behavioral_actions_IfElse()) == None

def test_behavioral_actions_IfElse_getIfBlock():
    assert behavioral_actions_IfElse.getIfBlock(behavioral_actions_IfElse()) == None


from python_code import Association
from python_code import StatementWithNestedBlocks
from python_code import behavioral_actions_Block
from python_code import behavioral_actions_LinkManipulationStatement

def test_behavioral_actions_LinkManipulationStatement___init__():
    assert behavioral_actions_LinkManipulationStatement.__init__(behavioral_actions_LinkManipulationStatement(0, behavioral_actions_LinkManipulationStatement=Association(), behavioral_actions_LinkManipulationStatement9=set(), Statement=behavioral_actions_Block(block=set(), owner=set(), nestedBlocks=StatementWithNestedBlocks())), 0, behavioral_actions_LinkManipulationStatement=Association(), behavioral_actions_LinkManipulationStatement9=set(), Statement=behavioral_actions_Block(block=set(), owner=set(), nestedBlocks=StatementWithNestedBlocks())) == None


from python_code import Block
from python_code import behavioral_actions_Statement

def test_behavioral_actions_Statement___init__():
    assert behavioral_actions_Statement.__init__(behavioral_actions_Statement(statements=Block()), statements=Block()) == None

def test_behavioral_actions_Statement_getOutermostBlock():
    assert behavioral_actions_Statement.getOutermostBlock(behavioral_actions_Statement(statements=Block())) == None

def test_behavioral_actions_Statement_isSideEffectFree():
    assert behavioral_actions_Statement.isSideEffectFree(behavioral_actions_Statement(statements=Block())) == None

def test_behavioral_actions_Statement_getOwningClass():
    assert behavioral_actions_Statement.getOwningClass(behavioral_actions_Statement(statements=Block())) == None

def test_behavioral_actions_Statement_getNamedValuesInScope():
    assert behavioral_actions_Statement.getNamedValuesInScope(behavioral_actions_Statement(statements=Block())) == None

def test_behavioral_actions_Statement_isSideEffectFreeForBlock():
    assert behavioral_actions_Statement.isSideEffectFreeForBlock(behavioral_actions_Statement(statements=Block()), '') == None


from python_code import behavioral_actions_NamedValueDeclaration
from python_code import behavioral_actions_Variable

def test_behavioral_actions_Variable___init__():
    assert behavioral_actions_Variable.__init__(behavioral_actions_Variable(assignTo=set(), NamedValueWithOptionalInitExpression=behavioral_actions_NamedValueDeclaration()), assignTo=set(), NamedValueWithOptionalInitExpression=behavioral_actions_NamedValueDeclaration()) == None

def test_behavioral_actions_Variable_getCommonTypeOfAssignments():
    assert behavioral_actions_Variable.getCommonTypeOfAssignments(behavioral_actions_Variable(assignTo=set(), NamedValueWithOptionalInitExpression=behavioral_actions_NamedValueDeclaration())) == None


from python_code import behavioral_actions_WhileLoop

def test_behavioral_actions_WhileLoop___init__():
    assert behavioral_actions_WhileLoop.__init__(behavioral_actions_WhileLoop()) == None

def test_behavioral_actions_WhileLoop_getLoopBody():
    assert behavioral_actions_WhileLoop.getLoopBody(behavioral_actions_WhileLoop()) == None


from python_code import behavioral_design_AbstractAction

def test_behavioral_design_AbstractAction___init__():
    assert behavioral_design_AbstractAction.__init__(behavioral_design_AbstractAction(False, False), False, False) == None


from python_code import behavioral_design_AbstractStatusValue

def test_behavioral_design_AbstractStatusValue___init__():
    assert behavioral_design_AbstractStatusValue.__init__(behavioral_design_AbstractStatusValue(False, False, False), False, False, False) == None


from python_code import behavioral_design_AbstractStatusVariable

def test_behavioral_design_AbstractStatusVariable___init__():
    assert behavioral_design_AbstractStatusVariable.__init__(behavioral_design_AbstractStatusVariable(False, False, behavioral_design_AbstractStatusVariable=set()), False, False, behavioral_design_AbstractStatusVariable=set()) == None


from python_code import SapClass
from python_code import behavioral_status_and_action_old_SAMAction

def test_behavioral_status_and_action_old_SAMAction___init__():
    assert behavioral_status_and_action_old_SAMAction.__init__(behavioral_status_and_action_old_SAMAction('\x00\x00', False, samAction=set(), samActions=SapClass()), '', True, samAction=set(), samActions=SapClass()) == None


from python_code import SapClass
from python_code import behavioral_status_and_action_old_SAMDerivator

def test_behavioral_status_and_action_old_SAMDerivator___init__():
    assert behavioral_status_and_action_old_SAMDerivator.__init__(behavioral_status_and_action_old_SAMDerivator('', samDerivators=SapClass(), samDerivator=set()), '', samDerivators=SapClass(), samDerivator=set()) == None


from python_code import SAMStatusSchema
from python_code import behavioral_status_and_action_old_SAMOperator

def test_behavioral_status_and_action_old_SAMOperator___init__():
    assert behavioral_status_and_action_old_SAMOperator.__init__(behavioral_status_and_action_old_SAMOperator('', samOperators=SAMStatusSchema(), samOperators68=set(), samTargetOperators=set(), samSourceOperators=set(), samSchemaOperators=set()), '', samOperators=SAMStatusSchema(), samOperators68=set(), samTargetOperators=set(), samSourceOperators=set(), samSchemaOperators=set()) == None


from python_code import SAMSchemaVariable
from python_code import behavioral_status_and_action_old_SAMSchemaValue

def test_behavioral_status_and_action_old_SAMSchemaValue___init__():
    assert behavioral_status_and_action_old_SAMSchemaValue.__init__(behavioral_status_and_action_old_SAMSchemaValue(False, False, samSchemaValues=SAMSchemaVariable(), samTargetSchemaValues=set(), samTargetSchemaValues91=set(), samSourceSchemaValues=set(), samSchemaValues96=set(), samSchemaValues99=set()), False, False, samSchemaValues=SAMSchemaVariable(), samTargetSchemaValues=set(), samTargetSchemaValues91=set(), samSourceSchemaValues=set(), samSchemaValues96=set(), samSchemaValues99=set()) == None


from python_code import SAMStatusSchema
from python_code import SAMStatusVariable
from python_code import behavioral_status_and_action_old_SAMSchemaVariable

def test_behavioral_status_and_action_old_SAMSchemaVariable___init__():
    assert behavioral_status_and_action_old_SAMSchemaVariable.__init__(behavioral_status_and_action_old_SAMSchemaVariable(False, samSchemaVariables=SAMStatusSchema(), samSchemaVariable=set(), samSchemaVariables80=SAMStatusVariable(), samSourceSchemaVariables=set(), samTargetSchemaVariable=set()), True, samSchemaVariables=SAMStatusSchema(), samSchemaVariable=set(), samSchemaVariables80=SAMStatusVariable(), samSourceSchemaVariables=set(), samTargetSchemaVariable=set()) == None


from python_code import SapClass
from python_code import behavioral_status_and_action_old_SAMStatusSchema

def test_behavioral_status_and_action_old_SAMStatusSchema___init__():
    assert behavioral_status_and_action_old_SAMStatusSchema.__init__(behavioral_status_and_action_old_SAMStatusSchema('', samStatusSchema=SapClass(), samStatusSchema56=set(), samStatusSchema58=set(), samStatusSchema61=set(), samStatusSchema64=set()), '', samStatusSchema=SapClass(), samStatusSchema56=set(), samStatusSchema58=set(), samStatusSchema61=set(), samStatusSchema64=set()) == None


from python_code import SAMStatusVariable
from python_code import behavioral_status_and_action_old_SAMStatusValue

def test_behavioral_status_and_action_old_SAMStatusValue___init__():
    assert behavioral_status_and_action_old_SAMStatusValue.__init__(behavioral_status_and_action_old_SAMStatusValue('', samStatusValues=SAMStatusVariable()), '', samStatusValues=SAMStatusVariable()) == None


from python_code import SapClass
from python_code import behavioral_status_and_action_old_SAMStatusVariable

def test_behavioral_status_and_action_old_SAMStatusVariable___init__():
    assert behavioral_status_and_action_old_SAMStatusVariable.__init__(behavioral_status_and_action_old_SAMStatusVariable('', False, samStatusVariables=SapClass(), samStatusVariable=set(), samSchemaValue=set()), '', True, samStatusVariables=SapClass(), samStatusVariable=set(), samSchemaValue=set()) == None

