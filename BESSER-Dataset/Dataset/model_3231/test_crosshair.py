from python_code import pascal_any_number
from python_code import pascal_number

def test_pascal_any_number___init__():
    assert pascal_any_number.__init__(pascal_any_number('', '\x00', pascal_any_number=pascal_number()), '\x00\x00', '', pascal_any_number=pascal_number()) == None

from python_code import pascal_goto_statement
from python_code import pascal_label
from python_code import pascal_label_declaration_part
from python_code import pascal_statement

def test_pascal_label___init__():
    assert pascal_label.__init__(pascal_label('', pascal_label=pascal_label_declaration_part(), pascal_label91=pascal_statement(), pascal_label108=pascal_goto_statement()), '', pascal_label=pascal_label_declaration_part(), pascal_label91=pascal_statement(), pascal_label108=pascal_goto_statement()) == None

from python_code import pascal_conformant_array_schema
from python_code import pascal_parameter_type
from python_code import pascal_unpacked_conformant_array_schema
from python_code import pascal_value_parameter_section
from python_code import pascal_variable_parameter_section

def test_pascal_parameter_type___init__():
    assert pascal_parameter_type.__init__(pascal_parameter_type('', pascal_parameter_type=pascal_value_parameter_section(), pascal_parameter_type72=pascal_variable_parameter_section(), pascal_parameter_type74=pascal_conformant_array_schema(), pascal_parameter_type86=pascal_unpacked_conformant_array_schema()), '', pascal_parameter_type=pascal_value_parameter_section(), pascal_parameter_type72=pascal_variable_parameter_section(), pascal_parameter_type74=pascal_conformant_array_schema(), pascal_parameter_type86=pascal_unpacked_conformant_array_schema()) == None

from python_code import pascal_field_list
from python_code import pascal_record_type
from python_code import pascal_unpacked_structured_type

def test_pascal_record_type___init__():
    assert pascal_record_type.__init__(pascal_record_type('', '\x00', pascal_record_type243=pascal_field_list(), pascal_record_type=pascal_unpacked_structured_type()), '\x00\x00', '', pascal_record_type243=pascal_field_list(), pascal_record_type=pascal_unpacked_structured_type()) == None

from python_code import pascal_structured_type
from python_code import pascal_type
from python_code import pascal_unpacked_structured_type

def test_pascal_structured_type___init__():
    assert pascal_structured_type.__init__(pascal_structured_type(True, pascal_structured_type=pascal_type(), pascal_structured_type227=pascal_unpacked_structured_type()), False, pascal_structured_type=pascal_type(), pascal_structured_type227=pascal_unpacked_structured_type()) == None

from python_code import pascal_term

def test_pascal_term___init__():
    assert pascal_term.__init__(pascal_term('', pascal_term=set()), '', pascal_term=set()) == None

from python_code import pascal_type
from python_code import pascal_type_definition
from python_code import pascal_type_definition_part

def test_pascal_type_definition___init__():
    assert pascal_type_definition.__init__(pascal_type_definition('', pascal_type_definition=pascal_type_definition_part(), pascal_type_definition28=pascal_type()), '', pascal_type_definition=pascal_type_definition_part(), pascal_type_definition28=pascal_type()) == None

from python_code import pascal_variable_identifier_list
from python_code import pascal_variable_section

def test_pascal_variable_identifier_list___init__():
    assert pascal_variable_identifier_list.__init__(pascal_variable_identifier_list('', pascal_variable_identifier_list=pascal_variable_section()), '', pascal_variable_identifier_list=pascal_variable_section()) == None

from python_code import pascal_statement
from python_code import pascal_structured_statement
from python_code import pascal_with_statement

def test_pascal_with_statement___init__():
    assert pascal_with_statement.__init__(pascal_with_statement('', '\x00', pascal_with_statement=pascal_structured_statement(), pascal_with_statement159=pascal_statement()), '\x00\x00', '', pascal_with_statement=pascal_structured_statement(), pascal_with_statement159=pascal_statement()) == None
