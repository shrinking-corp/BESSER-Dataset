from python_code import myDsl_EQL
from python_code import myDsl_simple_expression

def test_myDsl_EQL___init__():
    assert myDsl_EQL.__init__(myDsl_EQL('', myDsl_EQL=myDsl_simple_expression(), myDsl_EQL416=myDsl_simple_expression()), '', myDsl_EQL=myDsl_simple_expression(), myDsl_EQL416=myDsl_simple_expression()) == None


from python_code import myDsl_MUL
from python_code import myDsl_simple_expression

def test_myDsl_MUL___init__():
    assert myDsl_MUL.__init__(myDsl_MUL('', myDsl_MUL=myDsl_simple_expression(), myDsl_MUL391=myDsl_simple_expression()), '', myDsl_MUL=myDsl_simple_expression(), myDsl_MUL391=myDsl_simple_expression()) == None


from python_code import myDsl_REL
from python_code import myDsl_simple_expression

def test_myDsl_REL___init__():
    assert myDsl_REL.__init__(myDsl_REL('', myDsl_REL=myDsl_simple_expression(), myDsl_REL411=myDsl_simple_expression()), '', myDsl_REL=myDsl_simple_expression(), myDsl_REL411=myDsl_simple_expression()) == None


from python_code import myDsl_SHF
from python_code import myDsl_simple_expression

def test_myDsl_SHF___init__():
    assert myDsl_SHF.__init__(myDsl_SHF('', myDsl_SHF=myDsl_simple_expression(), myDsl_SHF406=myDsl_simple_expression()), '', myDsl_SHF=myDsl_simple_expression(), myDsl_SHF406=myDsl_simple_expression()) == None


from python_code import myDsl_alignment_specifier
from python_code import myDsl_constant_expression
from python_code import myDsl_declaration_specifiers
from python_code import myDsl_type_name

def test_myDsl_alignment_specifier___init__():
    assert myDsl_alignment_specifier.__init__(myDsl_alignment_specifier('', myDsl_alignment_specifier175=myDsl_type_name(), myDsl_alignment_specifier178=myDsl_constant_expression(), myDsl_alignment_specifier=myDsl_declaration_specifiers()), '', myDsl_alignment_specifier175=myDsl_type_name(), myDsl_alignment_specifier178=myDsl_constant_expression(), myDsl_alignment_specifier=myDsl_declaration_specifiers()) == None


from python_code import myDsl_assignment_expression
from python_code import myDsl_assignment_operator

def test_myDsl_assignment_operator___init__():
    assert myDsl_assignment_operator.__init__(myDsl_assignment_operator('', '', '\x00', '', '', '', '', '', '', '', myDsl_assignment_operator=myDsl_assignment_expression()), '', '', '\x00', '', '', '', '', '', '', '', myDsl_assignment_operator=myDsl_assignment_expression()) == None


from python_code import myDsl_booleanType

def test_myDsl_booleanType___init__():
    assert myDsl_booleanType.__init__(myDsl_booleanType('', '\x00'), '\x00\x00', '') == None


from python_code import myDsl_charType

def test_myDsl_charType___init__():
    assert myDsl_charType.__init__(myDsl_charType(''), '') == None


from python_code import myDsl_complexType

def test_myDsl_complexType___init__():
    assert myDsl_complexType.__init__(myDsl_complexType(''), '') == None


from python_code import myDsl_constant

def test_myDsl_constant___init__():
    assert myDsl_constant.__init__(myDsl_constant('', '', '\x00\x00'), '', '', '') == None


from python_code import myDsl_constant_expression
from python_code import myDsl_designator
from python_code import myDsl_designator_list
from python_code import myDsl_designator_list2

def test_myDsl_designator___init__():
    assert myDsl_designator.__init__(myDsl_designator('', myDsl_designator=myDsl_designator_list(), myDsl_designator294=myDsl_designator_list2(), myDsl_designator299=myDsl_constant_expression()), '', myDsl_designator=myDsl_designator_list(), myDsl_designator294=myDsl_designator_list2(), myDsl_designator299=myDsl_constant_expression()) == None


from python_code import myDsl_doubleType

def test_myDsl_doubleType___init__():
    assert myDsl_doubleType.__init__(myDsl_doubleType(''), '') == None


from python_code import myDsl_enumeration_constant
from python_code import myDsl_enumerator

def test_myDsl_enumeration_constant___init__():
    assert myDsl_enumeration_constant.__init__(myDsl_enumeration_constant('', myDsl_enumeration_constant=myDsl_enumerator()), '', myDsl_enumeration_constant=myDsl_enumerator()) == None


from python_code import myDsl_floatType

def test_myDsl_floatType___init__():
    assert myDsl_floatType.__init__(myDsl_floatType('', '\x00'), '\x00\x00', '') == None


from python_code import myDsl_declaration_specifiers
from python_code import myDsl_function_specifier

def test_myDsl_function_specifier___init__():
    assert myDsl_function_specifier.__init__(myDsl_function_specifier('', '\x00', myDsl_function_specifier=myDsl_declaration_specifiers()), '\x00\x00', '', myDsl_function_specifier=myDsl_declaration_specifiers()) == None


from python_code import myDsl_assignment_expression
from python_code import myDsl_generic_assoc_list
from python_code import myDsl_generic_association
from python_code import myDsl_type_name

def test_myDsl_generic_association___init__():
    assert myDsl_generic_association.__init__(myDsl_generic_association('', myDsl_generic_association=myDsl_generic_assoc_list(), myDsl_generic_association12=myDsl_generic_assoc_list(), myDsl_generic_association14=myDsl_type_name(), myDsl_generic_association17=myDsl_assignment_expression()), '', myDsl_generic_association=myDsl_generic_assoc_list(), myDsl_generic_association12=myDsl_generic_assoc_list(), myDsl_generic_association14=myDsl_type_name(), myDsl_generic_association17=myDsl_assignment_expression()) == None


from python_code import myDsl_assignment_expression
from python_code import myDsl_generic_assoc_list
from python_code import myDsl_generic_selection

def test_myDsl_generic_selection___init__():
    assert myDsl_generic_selection.__init__(myDsl_generic_selection('', myDsl_generic_selection=myDsl_assignment_expression(), myDsl_generic_selection7=myDsl_generic_assoc_list()), '', myDsl_generic_selection=myDsl_assignment_expression(), myDsl_generic_selection7=myDsl_generic_assoc_list()) == None


from python_code import myDsl_imaginaryType

def test_myDsl_imaginaryType___init__():
    assert myDsl_imaginaryType.__init__(myDsl_imaginaryType(''), '') == None


from python_code import myDsl_intType

def test_myDsl_intType___init__():
    assert myDsl_intType.__init__(myDsl_intType('', '\x00'), '\x00\x00', '') == None


from python_code import myDsl_EObject
from python_code import myDsl_declaration
from python_code import myDsl_expression_statement
from python_code import myDsl_iteration_statement
from python_code import myDsl_statement

def test_myDsl_iteration_statement___init__():
    assert myDsl_iteration_statement.__init__(myDsl_iteration_statement('', '', '\x00\x00', myDsl_iteration_statement=myDsl_statement(), myDsl_iteration_statement342=myDsl_EObject(), myDsl_iteration_statement344=myDsl_statement(), myDsl_iteration_statement347=myDsl_expression_statement(), myDsl_iteration_statement350=myDsl_expression_statement(), myDsl_iteration_statement353=myDsl_declaration()), '', '', '', myDsl_iteration_statement=myDsl_statement(), myDsl_iteration_statement342=myDsl_EObject(), myDsl_iteration_statement344=myDsl_statement(), myDsl_iteration_statement347=myDsl_expression_statement(), myDsl_iteration_statement350=myDsl_expression_statement(), myDsl_iteration_statement353=myDsl_declaration()) == None


from python_code import myDsl_expression
from python_code import myDsl_jump_statement
from python_code import myDsl_statement

def test_myDsl_jump_statement___init__():
    assert myDsl_jump_statement.__init__(myDsl_jump_statement('', '', '', '', '', myDsl_jump_statement=myDsl_statement(), myDsl_jump_statement356=myDsl_expression()), '', '', '', '', '', myDsl_jump_statement=myDsl_statement(), myDsl_jump_statement356=myDsl_expression()) == None


from python_code import myDsl_constant_expression
from python_code import myDsl_labeled_statement
from python_code import myDsl_statement

def test_myDsl_labeled_statement___init__():
    assert myDsl_labeled_statement.__init__(myDsl_labeled_statement('', '', '\x00\x00', myDsl_labeled_statement=myDsl_statement(), myDsl_labeled_statement316=myDsl_statement(), myDsl_labeled_statement319=myDsl_constant_expression()), '', '', '', myDsl_labeled_statement=myDsl_statement(), myDsl_labeled_statement316=myDsl_statement(), myDsl_labeled_statement319=myDsl_constant_expression()) == None


from python_code import myDsl_longType

def test_myDsl_longType___init__():
    assert myDsl_longType.__init__(myDsl_longType(''), '') == None


from python_code import myDsl_selection_statement
from python_code import myDsl_simple_expression
from python_code import myDsl_statement

def test_myDsl_selection_statement___init__():
    assert myDsl_selection_statement.__init__(myDsl_selection_statement('', '', '\x00\x00', myDsl_selection_statement333=myDsl_simple_expression(), myDsl_selection_statement=myDsl_statement(), myDsl_selection_statement336=myDsl_statement(), myDsl_selection_statement339=myDsl_statement()), '', '', '', myDsl_selection_statement333=myDsl_simple_expression(), myDsl_selection_statement=myDsl_statement(), myDsl_selection_statement336=myDsl_statement(), myDsl_selection_statement339=myDsl_statement()) == None


from python_code import myDsl_shortType

def test_myDsl_shortType___init__():
    assert myDsl_shortType.__init__(myDsl_shortType(''), '') == None


from python_code import myDsl_signedType

def test_myDsl_signedType___init__():
    assert myDsl_signedType.__init__(myDsl_signedType(''), '') == None


from python_code import myDsl_constant_expression
from python_code import myDsl_declaration
from python_code import myDsl_static_assert_declaration
from python_code import myDsl_struct_declaration

def test_myDsl_static_assert_declaration___init__():
    assert myDsl_static_assert_declaration.__init__(myDsl_static_assert_declaration('', '\x00', myDsl_static_assert_declaration=myDsl_declaration(), myDsl_static_assert_declaration128=myDsl_struct_declaration(), myDsl_static_assert_declaration302=myDsl_constant_expression()), '\x00\x00', '', myDsl_static_assert_declaration=myDsl_declaration(), myDsl_static_assert_declaration128=myDsl_struct_declaration(), myDsl_static_assert_declaration302=myDsl_constant_expression()) == None


from python_code import myDsl_declaration_specifiers
from python_code import myDsl_storage_class_specifier

def test_myDsl_storage_class_specifier___init__():
    assert myDsl_storage_class_specifier.__init__(myDsl_storage_class_specifier('', '', '', '', '', '', myDsl_storage_class_specifier=myDsl_declaration_specifiers()), '', '', '', '', '\x00', '', myDsl_storage_class_specifier=myDsl_declaration_specifiers()) == None


from python_code import myDsl_stringType
from python_code import myDsl_string_nova

def test_myDsl_string_nova___init__():
    assert myDsl_string_nova.__init__(myDsl_string_nova('', '\x00', myDsl_string_nova=myDsl_stringType()), '\x00\x00', '', myDsl_string_nova=myDsl_stringType()) == None


from python_code import myDsl_declaration_specifiers
from python_code import myDsl_type_qualifier
from python_code import myDsl_type_qualifier_list
from python_code import myDsl_type_qualifier_list2

def test_myDsl_type_qualifier___init__():
    assert myDsl_type_qualifier.__init__(myDsl_type_qualifier('\x00\x00', '', '', '', myDsl_type_qualifier=myDsl_declaration_specifiers(), myDsl_type_qualifier209=myDsl_type_qualifier_list(), myDsl_type_qualifier214=myDsl_type_qualifier_list2()), '', '', '', '', myDsl_type_qualifier=myDsl_declaration_specifiers(), myDsl_type_qualifier209=myDsl_type_qualifier_list(), myDsl_type_qualifier214=myDsl_type_qualifier_list2()) == None


from python_code import myDsl_unsignedType

def test_myDsl_unsignedType___init__():
    assert myDsl_unsignedType.__init__(myDsl_unsignedType(''), '') == None


from python_code import myDsl_variableRef

def test_myDsl_variableRef___init__():
    assert myDsl_variableRef.__init__(myDsl_variableRef(''), '') == None


from python_code import myDsl_voidType

def test_myDsl_voidType___init__():
    assert myDsl_voidType.__init__(myDsl_voidType(''), '') == None

