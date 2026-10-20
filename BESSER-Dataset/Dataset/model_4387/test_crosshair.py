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
    assert arduino_BooleanVariable.__init__(arduino_BooleanVariable(False, '\x00', arduino_BooleanVariable=arduino_BooleanVariableRef()), False, '\x00', arduino_BooleanVariable=arduino_BooleanVariableRef()) == None

def test_arduino_BooleanVariable_evaluate():
    assert arduino_BooleanVariable.evaluate(arduino_BooleanVariable(True, '', arduino_BooleanVariable=arduino_BooleanVariableRef())) == None


from python_code import arduino_Constant

def test_arduino_Constant___init__():
    assert arduino_Constant.__init__(arduino_Constant()) == None

def test_arduino_Constant_evaluate():
    assert arduino_Constant.evaluate(arduino_Constant()) == None


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
    assert arduino_Expression.__init__(arduino_Expression(arduino_Expression=arduino_BinaryExpression(), arduino_Expression20=arduino_BinaryExpression(), arduino_Expression30=arduino_UnaryExpression(), arduino_Expression28=arduino_Assignment()), arduino_Expression=arduino_BinaryExpression(), arduino_Expression20=arduino_BinaryExpression(), arduino_Expression30=arduino_UnaryExpression(), arduino_Expression28=arduino_Assignment()) == None

def test_arduino_Expression_evaluate():
    assert arduino_Expression.evaluate(arduino_Expression(arduino_Expression=arduino_BinaryExpression(), arduino_Expression20=arduino_BinaryExpression(), arduino_Expression30=arduino_UnaryExpression(), arduino_Expression28=arduino_Assignment())) == None


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


from python_code import arduino_Repeat

def test_arduino_Repeat___init__():
    assert arduino_Repeat.__init__(arduino_Repeat(''), '') == None

def test_arduino_Repeat_finalize():
    assert arduino_Repeat.finalize(arduino_Repeat('')) == None

def test_arduino_Repeat_execute():
    assert arduino_Repeat.execute(arduino_Repeat('')) == None

def test_arduino_Repeat_evaluate():
    assert arduino_Repeat.evaluate(arduino_Repeat('')) == None


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

def test_arduino_While_execute():
    assert arduino_While.execute(arduino_While(arduino_While=arduino_BooleanExpression())) == None

def test_arduino_While_evaluate():
    assert arduino_While.evaluate(arduino_While(arduino_While=arduino_BooleanExpression())) == None

