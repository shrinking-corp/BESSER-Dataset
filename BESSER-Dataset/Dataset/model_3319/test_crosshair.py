from python_code import java_Class_declaration

def test_java_Class_declaration___init__():
    assert java_Class_declaration.__init__(java_Class_declaration('', '', '', '', '', java_Class_declaration=set()), '', '', '', '\x00', '', java_Class_declaration=set()) == None


from python_code import java_Constructor_declaration
from python_code import java_Parameter_list
from python_code import java_Statement_block

def test_java_Constructor_declaration___init__():
    assert java_Constructor_declaration.__init__(java_Constructor_declaration('', '\x00', java_Constructor_declaration=java_Parameter_list(), java_Constructor_declaration24=java_Statement_block()), '\x00\x00', '', java_Constructor_declaration=java_Parameter_list(), java_Constructor_declaration24=java_Statement_block()) == None


from python_code import java_Compilation_unit
from python_code import java_Import_statement

def test_java_Import_statement___init__():
    assert java_Import_statement.__init__(java_Import_statement('', '\x00', java_Import_statement=java_Compilation_unit()), '\x00\x00', '', java_Import_statement=java_Compilation_unit()) == None


from python_code import java_Interface_declaration

def test_java_Interface_declaration___init__():
    assert java_Interface_declaration.__init__(java_Interface_declaration('', '', '', '', java_Interface_declaration=set()), '', '', '', '', java_Interface_declaration=set()) == None


from python_code import java_Compilation_unit
from python_code import java_Package_statement

def test_java_Package_statement___init__():
    assert java_Package_statement.__init__(java_Package_statement('', java_Package_statement=java_Compilation_unit()), '', java_Package_statement=java_Compilation_unit()) == None


from python_code import java_Method_call
from python_code import java_Parameter_list_method_call

def test_java_Parameter_list_method_call___init__():
    assert java_Parameter_list_method_call.__init__(java_Parameter_list_method_call('', '\x00', java_Parameter_list_method_call=java_Method_call()), '\x00\x00', '', java_Parameter_list_method_call=java_Method_call()) == None


from python_code import java_Return_Statement
from python_code import java_Return_value

def test_java_Return_value___init__():
    assert java_Return_value.__init__(java_Return_value('', java_Return_value=java_Return_Statement()), '', java_Return_value=java_Return_Statement()) == None


from python_code import java_Statement_block
from python_code import java_Static_initializer

def test_java_Static_initializer___init__():
    assert java_Static_initializer.__init__(java_Static_initializer('', java_Static_initializer=java_Statement_block()), '', java_Static_initializer=java_Statement_block()) == None


from python_code import java_Compilation_unit
from python_code import java_EObject
from python_code import java_Type_declaration

def test_java_Type_declaration___init__():
    assert java_Type_declaration.__init__(java_Type_declaration('', java_Type_declaration=java_Compilation_unit(), java_Type_declaration8=java_EObject()), '', java_Type_declaration=java_Compilation_unit(), java_Type_declaration8=java_EObject()) == None

