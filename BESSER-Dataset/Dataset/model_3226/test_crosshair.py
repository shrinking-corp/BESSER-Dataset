from python_code import pascal_bound_specification
from python_code import pascal_packed_conformant_array_schema
from python_code import pascal_unpacked_conformant_array_Schema

def test_pascal_bound_specification___init__():
    assert pascal_bound_specification.__init__(pascal_bound_specification('', '', '\x00\x00', pascal_bound_specification=pascal_packed_conformant_array_schema(), pascal_bound_specification80=pascal_unpacked_conformant_array_Schema()), '', '', '', pascal_bound_specification=pascal_packed_conformant_array_schema(), pascal_bound_specification80=pascal_unpacked_conformant_array_Schema()) == None


from python_code import pascal_formal_parameter_list
from python_code import pascal_formal_parameter_section
from python_code import pascal_function_heading

def test_pascal_function_heading___init__():
    assert pascal_function_heading.__init__(pascal_function_heading('', '\x00', pascal_function_heading=pascal_formal_parameter_list(), pascal_function_heading64=pascal_formal_parameter_section()), '\x00\x00', '', pascal_function_heading=pascal_formal_parameter_list(), pascal_function_heading64=pascal_formal_parameter_section()) == None


from python_code import pascal_enumerated_type
from python_code import pascal_identifier_list
from python_code import pascal_record_section
from python_code import pascal_value_parameter_section
from python_code import pascal_variable_declaration
from python_code import pascal_variable_parameter_section

def test_pascal_identifier_list___init__():
    assert pascal_identifier_list.__init__(pascal_identifier_list('', pascal_identifier_list=pascal_variable_declaration(), pascal_identifier_list67=pascal_value_parameter_section(), pascal_identifier_list72=pascal_variable_parameter_section(), pascal_identifier_list181=pascal_enumerated_type(), pascal_identifier_list220=pascal_record_section()), '', pascal_identifier_list=pascal_variable_declaration(), pascal_identifier_list67=pascal_value_parameter_section(), pascal_identifier_list72=pascal_variable_parameter_section(), pascal_identifier_list181=pascal_enumerated_type(), pascal_identifier_list220=pascal_record_section()) == None


from python_code import pascal_label
from python_code import pascal_label_declaration_part

def test_pascal_label___init__():
    assert pascal_label.__init__(pascal_label('', pascal_label=pascal_label_declaration_part()), '', pascal_label=pascal_label_declaration_part()) == None


from python_code import pascal_block
from python_code import pascal_formal_parameter_list
from python_code import pascal_procedure_and_function_declaration_part
from python_code import pascal_procedure_declaration

def test_pascal_procedure_declaration___init__():
    assert pascal_procedure_declaration.__init__(pascal_procedure_declaration('', pascal_procedure_declaration=pascal_procedure_and_function_declaration_part(), pascal_procedure_declaration36=pascal_formal_parameter_list(), pascal_procedure_declaration38=pascal_block()), '', pascal_procedure_declaration=pascal_procedure_and_function_declaration_part(), pascal_procedure_declaration36=pascal_formal_parameter_list(), pascal_procedure_declaration38=pascal_block()) == None


from python_code import pascal_formal_parameter_list
from python_code import pascal_formal_parameter_section
from python_code import pascal_procedure_heading

def test_pascal_procedure_heading___init__():
    assert pascal_procedure_heading.__init__(pascal_procedure_heading('', pascal_procedure_heading=pascal_formal_parameter_list(), pascal_procedure_heading61=pascal_formal_parameter_section()), '', pascal_procedure_heading=pascal_formal_parameter_list(), pascal_procedure_heading61=pascal_formal_parameter_section()) == None


from python_code import pascal_procedure_statement

def test_pascal_procedure_statement___init__():
    assert pascal_procedure_statement.__init__(pascal_procedure_statement('', '\x00'), '\x00\x00', '') == None

