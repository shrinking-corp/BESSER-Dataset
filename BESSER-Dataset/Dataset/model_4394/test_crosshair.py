from python_code import arduino_ArduinoCommunicationModule

def test_arduino_ArduinoCommunicationModule___init__():
    assert arduino_ArduinoCommunicationModule.__init__(arduino_ArduinoCommunicationModule()) == None

def test_arduino_ArduinoCommunicationModule_push():
    assert arduino_ArduinoCommunicationModule.push(arduino_ArduinoCommunicationModule()) == None


from python_code import arduino_BinaryBooleanExpression

def test_arduino_BinaryBooleanExpression___init__():
    assert arduino_BinaryBooleanExpression.__init__(arduino_BinaryBooleanExpression(''), '') == None

def test_arduino_BinaryBooleanExpression_evaluate():
    assert arduino_BinaryBooleanExpression.evaluate(arduino_BinaryBooleanExpression('')) == None


from python_code import arduino_BinaryIntegerExpression

def test_arduino_BinaryIntegerExpression___init__():
    assert arduino_BinaryIntegerExpression.__init__(arduino_BinaryIntegerExpression(''), '') == None

def test_arduino_BinaryIntegerExpression_evaluate():
    assert arduino_BinaryIntegerExpression.evaluate(arduino_BinaryIntegerExpression('')) == None


from python_code import arduino_BooleanConstant

def test_arduino_BooleanConstant___init__():
    assert arduino_BooleanConstant.__init__(arduino_BooleanConstant(True), False) == None

def test_arduino_BooleanConstant_evaluate():
    assert arduino_BooleanConstant.evaluate(arduino_BooleanConstant(False)) == None


from python_code import arduino_BooleanModuleGet

def test_arduino_BooleanModuleGet___init__():
    assert arduino_BooleanModuleGet.__init__(arduino_BooleanModuleGet()) == None

def test_arduino_BooleanModuleGet_evaluate():
    assert arduino_BooleanModuleGet.evaluate(arduino_BooleanModuleGet()) == None


from python_code import arduino_BooleanVariable
from python_code import arduino_BooleanVariableRef

def test_arduino_BooleanVariable___init__():
    assert arduino_BooleanVariable.__init__(arduino_BooleanVariable('', False, arduino_BooleanVariable=arduino_BooleanVariableRef()), '', False, arduino_BooleanVariable=arduino_BooleanVariableRef()) == None

def test_arduino_BooleanVariable_evaluate():
    assert arduino_BooleanVariable.evaluate(arduino_BooleanVariable('', False, arduino_BooleanVariable=arduino_BooleanVariableRef())) == None


from python_code import arduino_Constant

def test_arduino_Constant___init__():
    assert arduino_Constant.__init__(arduino_Constant()) == None

def test_arduino_Constant_evaluate():
    assert arduino_Constant.evaluate(arduino_Constant()) == None


from python_code import arduino_Block
from python_code import arduino_Control

def test_arduino_Control___init__():
    assert arduino_Control.__init__(arduino_Control(arduino_Control=arduino_Block()), arduino_Control=arduino_Block()) == None

def test_arduino_Control_execute():
    assert arduino_Control.execute(arduino_Control(arduino_Control=arduino_Block())) == None

def test_arduino_Control_evaluate():
    assert arduino_Control.evaluate(arduino_Control(arduino_Control=arduino_Block())) == None


from python_code import arduino_Delay

def test_arduino_Delay___init__():
    assert arduino_Delay.__init__(arduino_Delay('', 0), '', 0) == None

def test_arduino_Delay_execute():
    assert arduino_Delay.execute(arduino_Delay('', 0)) == None


from python_code import arduino_Assignment
from python_code import arduino_BinaryExpression
from python_code import arduino_Expression
from python_code import arduino_UnaryExpression

def test_arduino_Expression___init__():
    assert arduino_Expression.__init__(arduino_Expression(arduino_Expression=arduino_BinaryExpression(), arduino_Expression18=arduino_BinaryExpression(), arduino_Expression26=arduino_Assignment(), arduino_Expression28=arduino_UnaryExpression()), arduino_Expression=arduino_BinaryExpression(), arduino_Expression18=arduino_BinaryExpression(), arduino_Expression26=arduino_Assignment(), arduino_Expression28=arduino_UnaryExpression()) == None

def test_arduino_Expression_evaluate():
    assert arduino_Expression.evaluate(arduino_Expression(arduino_Expression=arduino_BinaryExpression(), arduino_Expression18=arduino_BinaryExpression(), arduino_Expression26=arduino_Assignment(), arduino_Expression28=arduino_UnaryExpression())) == None


from python_code import arduino_Block
from python_code import arduino_BooleanExpression
from python_code import arduino_If

def test_arduino_If___init__():
    assert arduino_If.__init__(arduino_If(arduino_If=arduino_BooleanExpression(), arduino_If23=arduino_Block()), arduino_If=arduino_BooleanExpression(), arduino_If23=arduino_Block()) == None

def test_arduino_If_evaluate():
    assert arduino_If.evaluate(arduino_If(arduino_If=arduino_BooleanExpression(), arduino_If23=arduino_Block())) == None


from python_code import arduino_Block
from python_code import arduino_Instruction

def test_arduino_Instruction___init__():
    assert arduino_Instruction.__init__(arduino_Instruction(arduino_Instruction=arduino_Block()), arduino_Instruction=arduino_Block()) == None

def test_arduino_Instruction_execute():
    assert arduino_Instruction.execute(arduino_Instruction(arduino_Instruction=arduino_Block())) == None

def test_arduino_Instruction_finalize():
    assert arduino_Instruction.finalize(arduino_Instruction(arduino_Instruction=arduino_Block())) == None


from python_code import arduino_IntegerConstant

def test_arduino_IntegerConstant___init__():
    assert arduino_IntegerConstant.__init__(arduino_IntegerConstant(0), 0) == None

def test_arduino_IntegerConstant_evaluate():
    assert arduino_IntegerConstant.evaluate(arduino_IntegerConstant(0)) == None


from python_code import arduino_IntegerModuleGet

def test_arduino_IntegerModuleGet___init__():
    assert arduino_IntegerModuleGet.__init__(arduino_IntegerModuleGet()) == None

def test_arduino_IntegerModuleGet_evaluate():
    assert arduino_IntegerModuleGet.evaluate(arduino_IntegerModuleGet()) == None


from python_code import arduino_IntegerVariable
from python_code import arduino_IntegerVariableRef

def test_arduino_IntegerVariable___init__():
    assert arduino_IntegerVariable.__init__(arduino_IntegerVariable(0, '\x00', arduino_IntegerVariable=arduino_IntegerVariableRef()), 0, '\x00', arduino_IntegerVariable=arduino_IntegerVariableRef()) == None

def test_arduino_IntegerVariable_evaluate():
    assert arduino_IntegerVariable.evaluate(arduino_IntegerVariable(0, '', arduino_IntegerVariable=arduino_IntegerVariableRef())) == None


from python_code import arduino_LED

def test_arduino_LED___init__():
    assert arduino_LED.__init__(arduino_LED(''), '') == None


from python_code import arduino_ModuleAssignment

def test_arduino_ModuleAssignment___init__():
    assert arduino_ModuleAssignment.__init__(arduino_ModuleAssignment()) == None

def test_arduino_ModuleAssignment_execute():
    assert arduino_ModuleAssignment.execute(arduino_ModuleAssignment()) == None


from python_code import arduino_Module
from python_code import arduino_ModuleInstruction

def test_arduino_ModuleInstruction___init__():
    assert arduino_ModuleInstruction.__init__(arduino_ModuleInstruction(arduino_ModuleInstruction=arduino_Module()), arduino_ModuleInstruction=arduino_Module()) == None

def test_arduino_ModuleInstruction_execute():
    assert arduino_ModuleInstruction.execute(arduino_ModuleInstruction(arduino_ModuleInstruction=arduino_Module())) == None


from python_code import arduino_NamedElement

def test_arduino_NamedElement___init__():
    assert arduino_NamedElement.__init__(arduino_NamedElement(''), '') == None


from python_code import arduino_Pin

def test_arduino_Pin___init__():
    assert arduino_Pin.__init__(arduino_Pin(''), '') == None


from python_code import arduino_Board
from python_code import arduino_Project
from python_code import arduino_Sketch

def test_arduino_Project___init__():
    assert arduino_Project.__init__(arduino_Project(project=set(), project10=set(), Project=arduino_Board(), Project4=arduino_Sketch()), project=set(), project10=set(), Project=arduino_Board(), Project4=arduino_Sketch()) == None

def test_arduino_Project_initializeModel():
    assert arduino_Project.initializeModel(arduino_Project(project=set(), project10=set(), Project=arduino_Board(), Project4=arduino_Sketch()), 0) == None


from python_code import arduino_PushButton

def test_arduino_PushButton___init__():
    assert arduino_PushButton.__init__(arduino_PushButton(True), False) == None

def test_arduino_PushButton_toggle():
    assert arduino_PushButton.toggle(arduino_PushButton(False)) == None


from python_code import arduino_Repeat

def test_arduino_Repeat___init__():
    assert arduino_Repeat.__init__(arduino_Repeat(0, '\x00'), 0, '\x00') == None

def test_arduino_Repeat_evaluate():
    assert arduino_Repeat.evaluate(arduino_Repeat(0, '')) == None

def test_arduino_Repeat_finalize():
    assert arduino_Repeat.finalize(arduino_Repeat(0, '')) == None


from python_code import arduino_UnaryBooleanExpression

def test_arduino_UnaryBooleanExpression___init__():
    assert arduino_UnaryBooleanExpression.__init__(arduino_UnaryBooleanExpression(''), '') == None


from python_code import arduino_UnaryIntegerExpression

def test_arduino_UnaryIntegerExpression___init__():
    assert arduino_UnaryIntegerExpression.__init__(arduino_UnaryIntegerExpression(''), '') == None


from python_code import arduino_Utilities

def test_arduino_Utilities___init__():
    assert arduino_Utilities.__init__(arduino_Utilities()) == None

def test_arduino_Utilities_execute():
    assert arduino_Utilities.execute(arduino_Utilities()) == None


from python_code import arduino_VariableRef

def test_arduino_VariableRef___init__():
    assert arduino_VariableRef.__init__(arduino_VariableRef()) == None

def test_arduino_VariableRef_evaluate():
    assert arduino_VariableRef.evaluate(arduino_VariableRef()) == None


from python_code import arduino_BooleanExpression
from python_code import arduino_While

def test_arduino_While___init__():
    assert arduino_While.__init__(arduino_While(arduino_While=arduino_BooleanExpression()), arduino_While=arduino_BooleanExpression()) == None

def test_arduino_While_evaluate():
    assert arduino_While.evaluate(arduino_While(arduino_While=arduino_BooleanExpression())) == None

