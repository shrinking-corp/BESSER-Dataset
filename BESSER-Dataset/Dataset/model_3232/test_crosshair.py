from python_code import pascal_abstraction_declaration
from python_code import pascal_abstraction_heading
from python_code import pascal_formal_parameter_list
from python_code import pascal_formal_parameter_section

def test_pascal_abstraction_heading___init__():
    assert pascal_abstraction_heading.__init__(pascal_abstraction_heading('', '\x00', pascal_abstraction_heading=pascal_formal_parameter_list(), pascal_abstraction_heading72=pascal_abstraction_declaration(), pascal_abstraction_heading84=pascal_formal_parameter_section(), pascal_abstraction_heading87=pascal_formal_parameter_section()), '\x00\x00', '', pascal_abstraction_heading=pascal_formal_parameter_list(), pascal_abstraction_heading72=pascal_abstraction_declaration(), pascal_abstraction_heading84=pascal_formal_parameter_section(), pascal_abstraction_heading87=pascal_formal_parameter_section()) == None


from python_code import pascal_any_number
from python_code import pascal_number

def test_pascal_any_number___init__():
    assert pascal_any_number.__init__(pascal_any_number('', '\x00', pascal_any_number=pascal_number()), '\x00\x00', '', pascal_any_number=pascal_number()) == None


from python_code import pascal_identifier_list
from python_code import pascal_record_section
from python_code import pascal_value_parameter_section
from python_code import pascal_variable_parameter_section

def test_pascal_identifier_list___init__():
    assert pascal_identifier_list.__init__(pascal_identifier_list('', pascal_identifier_list94=pascal_variable_parameter_section(), pascal_identifier_list128=pascal_record_section(), pascal_identifier_list=pascal_value_parameter_section()), '', pascal_identifier_list94=pascal_variable_parameter_section(), pascal_identifier_list128=pascal_record_section(), pascal_identifier_list=pascal_value_parameter_section()) == None


from python_code import pascal_label
from python_code import pascal_label_declaration
from python_code import pascal_statement

def test_pascal_label___init__():
    assert pascal_label.__init__(pascal_label('', pascal_label=pascal_statement(), pascal_label102=pascal_label_declaration()), '', pascal_label=pascal_statement(), pascal_label102=pascal_label_declaration()) == None


from python_code import pascal_parameter_type
from python_code import pascal_value_parameter_section
from python_code import pascal_variable_parameter_section

def test_pascal_parameter_type___init__():
    assert pascal_parameter_type.__init__(pascal_parameter_type('', pascal_parameter_type=pascal_value_parameter_section(), pascal_parameter_type97=pascal_variable_parameter_section()), '', pascal_parameter_type=pascal_value_parameter_section(), pascal_parameter_type97=pascal_variable_parameter_section()) == None


from python_code import pascal_program
from python_code import pascal_program_heading_block

def test_pascal_program_heading_block___init__():
    assert pascal_program_heading_block.__init__(pascal_program_heading_block('', pascal_program_heading_block=pascal_program()), '', pascal_program_heading_block=pascal_program()) == None


from python_code import pascal_field_list
from python_code import pascal_record_type
from python_code import pascal_unpacked_structured_type

def test_pascal_record_type___init__():
    assert pascal_record_type.__init__(pascal_record_type('', '\x00', pascal_record_type=pascal_unpacked_structured_type(), pascal_record_type123=pascal_field_list()), '\x00\x00', '', pascal_record_type=pascal_unpacked_structured_type(), pascal_record_type123=pascal_field_list()) == None


from python_code import pascal_simple_type
from python_code import pascal_type

def test_pascal_simple_type___init__():
    assert pascal_simple_type.__init__(pascal_simple_type('', pascal_simple_type=pascal_type()), '', pascal_simple_type=pascal_type()) == None


from python_code import pascal_term

def test_pascal_term___init__():
    assert pascal_term.__init__(pascal_term('', pascal_term=set()), '', pascal_term=set()) == None


from python_code import pascal_type
from python_code import pascal_type_definition
from python_code import pascal_type_definition_part

def test_pascal_type_definition___init__():
    assert pascal_type_definition.__init__(pascal_type_definition('', pascal_type_definition=pascal_type_definition_part(), pascal_type_definition113=pascal_type()), '', pascal_type_definition=pascal_type_definition_part(), pascal_type_definition113=pascal_type()) == None


from python_code import pascal_variable_identifier_list
from python_code import pascal_variable_section

def test_pascal_variable_identifier_list___init__():
    assert pascal_variable_identifier_list.__init__(pascal_variable_identifier_list('', pascal_variable_identifier_list=pascal_variable_section()), '', pascal_variable_identifier_list=pascal_variable_section()) == None

