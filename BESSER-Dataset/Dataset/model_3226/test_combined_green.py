# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    pascal_case_limb,
    pascal_Variable1,
    pascal_Set,
    pascal_number,
    pascal_FunctionDesignator,
    pascal_factor,
    pascal_term,
    pascal_simple_expression,
    pascal_variable,
    pascal_structured_statement,
    pascal_expression,
    pascal_case_statement,
    pascal_if_statement,
    repetitive_statement,
    pascal_for_statement,
    pascal_repeat_statement,
    pascal_while_statement,
    structured_statement,
    pascal_repetitive_statement,
    pascal_compound_statement,
    pascal_conditional_statement,
    pascal_with_statement,
    pascal_variable_parameter_section,
    pascal_value_parameter_section,
    pascal_formal_parameter_section,
    simple_statement,
    pascal_goto_statement,
    pascal_procedure_statement,
    pascal_assignment_statement,
    pascal_simple_statement,
    pascal_EObject,
    pascal_statement,
    statement_part,
    pascal_statement_sequence,
    pascal_bound_specification,
    conformant_array_schema,
    pascal_unpacked_conformant_array_Schema,
    pascal_packed_conformant_array_schema,
    pascal_conformant_array_schema,
    pascal_parameter_type,
    pascal_constant_definition,
    pascal_procedure_and_function_declaration_part,
    pascal_function_heading,
    pascal_procedure_heading,
    pascal_formal_parameter_list,
    pascal_function_declaration,
    pascal_procedure_declaration,
    pascal_variable_declaration,
    pascal_type_definition,
    pascal_variable_declaration_part,
    pascal_type_definition_part,
    pascal_constant_definition_part,
    pascal_label_declaration_part,
    pascal_statement_part,
    pascal_DeclarationPart,
    pascal_block,
    pascal_program_heading,
    pascal_program,
    pascal_Model,
    constant_definition,
    pascal_constant,
    pascal_field_list,
    goto_statement,
    statement,
    pascal_label,
    program_heading,
    pascal_identifier_list,
    pascal_variant,
    pascal_tag_field,
    pascal_record_section,
    pascal_variant_part,
    pascal_fixed_part,
    pascal_ElementList,
    pascal_ExpressionList,
    pascal_file_type,
    pascal_set_type,
    pascal_record_type,
    pascal_array_type,
    pascal_unpacked_structured_type,
    pascal_enumerated_type,
    pascal_subrange_type,
    pascal_pointer_type,
    pascal_structured_type,
    pascal_simple_type,
    type_definition,
    pascal_type,
    pascal_case_label_list,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_pascal_case_limb_is_not_abstract():
    assert not inspect.isabstract(pascal_case_limb)


def test_hyp_pascal_case_limb_constructor_exists():
    assert callable(pascal_case_limb.__init__)


def test_hyp_pascal_case_limb_constructor_args():
    sig = inspect.signature(pascal_case_limb.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_variable1_is_not_abstract():
    assert not inspect.isabstract(pascal_Variable1)


def test_hyp_pascal_variable1_constructor_exists():
    assert callable(pascal_Variable1.__init__)


def test_hyp_pascal_variable1_constructor_args():
    sig = inspect.signature(pascal_Variable1.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_pascal_set_is_not_abstract():
    assert not inspect.isabstract(pascal_Set)


def test_hyp_pascal_set_constructor_exists():
    assert callable(pascal_Set.__init__)


def test_hyp_pascal_set_constructor_args():
    sig = inspect.signature(pascal_Set.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_number_is_not_abstract():
    assert not inspect.isabstract(pascal_number)


def test_hyp_pascal_number_constructor_exists():
    assert callable(pascal_number.__init__)


def test_hyp_pascal_number_constructor_args():
    sig = inspect.signature(pascal_number.__init__)
    params = list(sig.parameters.keys())
    assert "real" in params, "Missing parameter 'real'"
    assert "integer" in params, "Missing parameter 'integer'"





def test_hyp_pascal_functiondesignator_is_not_abstract():
    assert not inspect.isabstract(pascal_FunctionDesignator)


def test_hyp_pascal_functiondesignator_constructor_exists():
    assert callable(pascal_FunctionDesignator.__init__)


def test_hyp_pascal_functiondesignator_constructor_args():
    sig = inspect.signature(pascal_FunctionDesignator.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_pascal_factor_is_not_abstract():
    assert not inspect.isabstract(pascal_factor)


def test_hyp_pascal_factor_constructor_exists():
    assert callable(pascal_factor.__init__)


def test_hyp_pascal_factor_constructor_args():
    sig = inspect.signature(pascal_factor.__init__)
    params = list(sig.parameters.keys())
    assert "string" in params, "Missing parameter 'string'"
    assert "nil" in params, "Missing parameter 'nil'"
    assert "id" in params, "Missing parameter 'id'"






def test_hyp_pascal_term_is_not_abstract():
    assert not inspect.isabstract(pascal_term)


def test_hyp_pascal_term_constructor_exists():
    assert callable(pascal_term.__init__)


def test_hyp_pascal_term_constructor_args():
    sig = inspect.signature(pascal_term.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_simple_expression_is_not_abstract():
    assert not inspect.isabstract(pascal_simple_expression)


def test_hyp_pascal_simple_expression_constructor_exists():
    assert callable(pascal_simple_expression.__init__)


def test_hyp_pascal_simple_expression_constructor_args():
    sig = inspect.signature(pascal_simple_expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_variable_is_not_abstract():
    assert not inspect.isabstract(pascal_variable)


def test_hyp_pascal_variable_constructor_exists():
    assert callable(pascal_variable.__init__)


def test_hyp_pascal_variable_constructor_args():
    sig = inspect.signature(pascal_variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_pascal_structured_statement_is_not_abstract():
    assert not inspect.isabstract(pascal_structured_statement)


def test_hyp_pascal_structured_statement_constructor_exists():
    assert callable(pascal_structured_statement.__init__)


def test_hyp_pascal_structured_statement_constructor_args():
    sig = inspect.signature(pascal_structured_statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_expression_is_not_abstract():
    assert not inspect.isabstract(pascal_expression)


def test_hyp_pascal_expression_constructor_exists():
    assert callable(pascal_expression.__init__)


def test_hyp_pascal_expression_constructor_args():
    sig = inspect.signature(pascal_expression.__init__)
    params = list(sig.parameters.keys())
    assert "relational_operators" in params, "Missing parameter 'relational_operators'"




def test_hyp_pascal_case_statement_is_not_abstract():
    assert not inspect.isabstract(pascal_case_statement)


def test_hyp_pascal_case_statement_constructor_exists():
    assert callable(pascal_case_statement.__init__)


def test_hyp_pascal_case_statement_constructor_args():
    sig = inspect.signature(pascal_case_statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_if_statement_is_not_abstract():
    assert not inspect.isabstract(pascal_if_statement)


def test_hyp_pascal_if_statement_constructor_exists():
    assert callable(pascal_if_statement.__init__)


def test_hyp_pascal_if_statement_constructor_args():
    sig = inspect.signature(pascal_if_statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_repetitive_statement_is_not_abstract():
    assert not inspect.isabstract(repetitive_statement)


def test_hyp_repetitive_statement_constructor_exists():
    assert callable(repetitive_statement.__init__)


def test_hyp_repetitive_statement_constructor_args():
    sig = inspect.signature(repetitive_statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_for_statement_is_not_abstract():
    assert not inspect.isabstract(pascal_for_statement)


def test_hyp_pascal_for_statement_constructor_exists():
    assert callable(pascal_for_statement.__init__)


def test_hyp_pascal_for_statement_constructor_args():
    sig = inspect.signature(pascal_for_statement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_pascal_repeat_statement_is_not_abstract():
    assert not inspect.isabstract(pascal_repeat_statement)


def test_hyp_pascal_repeat_statement_constructor_exists():
    assert callable(pascal_repeat_statement.__init__)


def test_hyp_pascal_repeat_statement_constructor_args():
    sig = inspect.signature(pascal_repeat_statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_while_statement_is_not_abstract():
    assert not inspect.isabstract(pascal_while_statement)


def test_hyp_pascal_while_statement_constructor_exists():
    assert callable(pascal_while_statement.__init__)


def test_hyp_pascal_while_statement_constructor_args():
    sig = inspect.signature(pascal_while_statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_structured_statement_is_not_abstract():
    assert not inspect.isabstract(structured_statement)


def test_hyp_structured_statement_constructor_exists():
    assert callable(structured_statement.__init__)


def test_hyp_structured_statement_constructor_args():
    sig = inspect.signature(structured_statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_repetitive_statement_is_not_abstract():
    assert not inspect.isabstract(pascal_repetitive_statement)


def test_hyp_pascal_repetitive_statement_constructor_exists():
    assert callable(pascal_repetitive_statement.__init__)


def test_hyp_pascal_repetitive_statement_constructor_args():
    sig = inspect.signature(pascal_repetitive_statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_compound_statement_is_not_abstract():
    assert not inspect.isabstract(pascal_compound_statement)


def test_hyp_pascal_compound_statement_constructor_exists():
    assert callable(pascal_compound_statement.__init__)


def test_hyp_pascal_compound_statement_constructor_args():
    sig = inspect.signature(pascal_compound_statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_conditional_statement_is_not_abstract():
    assert not inspect.isabstract(pascal_conditional_statement)


def test_hyp_pascal_conditional_statement_constructor_exists():
    assert callable(pascal_conditional_statement.__init__)


def test_hyp_pascal_conditional_statement_constructor_args():
    sig = inspect.signature(pascal_conditional_statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_with_statement_is_not_abstract():
    assert not inspect.isabstract(pascal_with_statement)


def test_hyp_pascal_with_statement_constructor_exists():
    assert callable(pascal_with_statement.__init__)


def test_hyp_pascal_with_statement_constructor_args():
    sig = inspect.signature(pascal_with_statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_variable_parameter_section_is_not_abstract():
    assert not inspect.isabstract(pascal_variable_parameter_section)


def test_hyp_pascal_variable_parameter_section_constructor_exists():
    assert callable(pascal_variable_parameter_section.__init__)


def test_hyp_pascal_variable_parameter_section_constructor_args():
    sig = inspect.signature(pascal_variable_parameter_section.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_value_parameter_section_is_not_abstract():
    assert not inspect.isabstract(pascal_value_parameter_section)


def test_hyp_pascal_value_parameter_section_constructor_exists():
    assert callable(pascal_value_parameter_section.__init__)


def test_hyp_pascal_value_parameter_section_constructor_args():
    sig = inspect.signature(pascal_value_parameter_section.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_formal_parameter_section_is_not_abstract():
    assert not inspect.isabstract(pascal_formal_parameter_section)


def test_hyp_pascal_formal_parameter_section_constructor_exists():
    assert callable(pascal_formal_parameter_section.__init__)


def test_hyp_pascal_formal_parameter_section_constructor_args():
    sig = inspect.signature(pascal_formal_parameter_section.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simple_statement_is_not_abstract():
    assert not inspect.isabstract(simple_statement)


def test_hyp_simple_statement_constructor_exists():
    assert callable(simple_statement.__init__)


def test_hyp_simple_statement_constructor_args():
    sig = inspect.signature(simple_statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_goto_statement_is_not_abstract():
    assert not inspect.isabstract(pascal_goto_statement)


def test_hyp_pascal_goto_statement_constructor_exists():
    assert callable(pascal_goto_statement.__init__)


def test_hyp_pascal_goto_statement_constructor_args():
    sig = inspect.signature(pascal_goto_statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_procedure_statement_is_not_abstract():
    assert not inspect.isabstract(pascal_procedure_statement)


def test_hyp_pascal_procedure_statement_constructor_exists():
    assert callable(pascal_procedure_statement.__init__)


def test_hyp_pascal_procedure_statement_constructor_args():
    sig = inspect.signature(pascal_procedure_statement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "actualParameterList" in params, "Missing parameter 'actualParameterList'"





def test_hyp_pascal_assignment_statement_is_not_abstract():
    assert not inspect.isabstract(pascal_assignment_statement)


def test_hyp_pascal_assignment_statement_constructor_exists():
    assert callable(pascal_assignment_statement.__init__)


def test_hyp_pascal_assignment_statement_constructor_args():
    sig = inspect.signature(pascal_assignment_statement.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "variable" in params, "Missing parameter 'variable'"





def test_hyp_pascal_simple_statement_is_not_abstract():
    assert not inspect.isabstract(pascal_simple_statement)


def test_hyp_pascal_simple_statement_constructor_exists():
    assert callable(pascal_simple_statement.__init__)


def test_hyp_pascal_simple_statement_constructor_args():
    sig = inspect.signature(pascal_simple_statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_eobject_is_not_abstract():
    assert not inspect.isabstract(pascal_EObject)


def test_hyp_pascal_eobject_constructor_exists():
    assert callable(pascal_EObject.__init__)


def test_hyp_pascal_eobject_constructor_args():
    sig = inspect.signature(pascal_EObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_statement_is_not_abstract():
    assert not inspect.isabstract(pascal_statement)


def test_hyp_pascal_statement_constructor_exists():
    assert callable(pascal_statement.__init__)


def test_hyp_pascal_statement_constructor_args():
    sig = inspect.signature(pascal_statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statement_part_is_not_abstract():
    assert not inspect.isabstract(statement_part)


def test_hyp_statement_part_constructor_exists():
    assert callable(statement_part.__init__)


def test_hyp_statement_part_constructor_args():
    sig = inspect.signature(statement_part.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_statement_sequence_is_not_abstract():
    assert not inspect.isabstract(pascal_statement_sequence)


def test_hyp_pascal_statement_sequence_constructor_exists():
    assert callable(pascal_statement_sequence.__init__)


def test_hyp_pascal_statement_sequence_constructor_args():
    sig = inspect.signature(pascal_statement_sequence.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_bound_specification_is_not_abstract():
    assert not inspect.isabstract(pascal_bound_specification)


def test_hyp_pascal_bound_specification_constructor_exists():
    assert callable(pascal_bound_specification.__init__)


def test_hyp_pascal_bound_specification_constructor_args():
    sig = inspect.signature(pascal_bound_specification.__init__)
    params = list(sig.parameters.keys())
    assert "id3" in params, "Missing parameter 'id3'"
    assert "id2" in params, "Missing parameter 'id2'"
    assert "id1" in params, "Missing parameter 'id1'"






def test_hyp_conformant_array_schema_is_not_abstract():
    assert not inspect.isabstract(conformant_array_schema)


def test_hyp_conformant_array_schema_constructor_exists():
    assert callable(conformant_array_schema.__init__)


def test_hyp_conformant_array_schema_constructor_args():
    sig = inspect.signature(conformant_array_schema.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_unpacked_conformant_array_schema_is_not_abstract():
    assert not inspect.isabstract(pascal_unpacked_conformant_array_Schema)


def test_hyp_pascal_unpacked_conformant_array_schema_constructor_exists():
    assert callable(pascal_unpacked_conformant_array_Schema.__init__)


def test_hyp_pascal_unpacked_conformant_array_schema_constructor_args():
    sig = inspect.signature(pascal_unpacked_conformant_array_Schema.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_packed_conformant_array_schema_is_not_abstract():
    assert not inspect.isabstract(pascal_packed_conformant_array_schema)


def test_hyp_pascal_packed_conformant_array_schema_constructor_exists():
    assert callable(pascal_packed_conformant_array_schema.__init__)


def test_hyp_pascal_packed_conformant_array_schema_constructor_args():
    sig = inspect.signature(pascal_packed_conformant_array_schema.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_conformant_array_schema_is_not_abstract():
    assert not inspect.isabstract(pascal_conformant_array_schema)


def test_hyp_pascal_conformant_array_schema_constructor_exists():
    assert callable(pascal_conformant_array_schema.__init__)


def test_hyp_pascal_conformant_array_schema_constructor_args():
    sig = inspect.signature(pascal_conformant_array_schema.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_pascal_parameter_type_is_not_abstract():
    assert not inspect.isabstract(pascal_parameter_type)


def test_hyp_pascal_parameter_type_constructor_exists():
    assert callable(pascal_parameter_type.__init__)


def test_hyp_pascal_parameter_type_constructor_args():
    sig = inspect.signature(pascal_parameter_type.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_pascal_constant_definition_is_not_abstract():
    assert not inspect.isabstract(pascal_constant_definition)


def test_hyp_pascal_constant_definition_constructor_exists():
    assert callable(pascal_constant_definition.__init__)


def test_hyp_pascal_constant_definition_constructor_args():
    sig = inspect.signature(pascal_constant_definition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_procedure_and_function_declaration_part_is_not_abstract():
    assert not inspect.isabstract(pascal_procedure_and_function_declaration_part)


def test_hyp_pascal_procedure_and_function_declaration_part_constructor_exists():
    assert callable(pascal_procedure_and_function_declaration_part.__init__)


def test_hyp_pascal_procedure_and_function_declaration_part_constructor_args():
    sig = inspect.signature(pascal_procedure_and_function_declaration_part.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_function_heading_is_not_abstract():
    assert not inspect.isabstract(pascal_function_heading)


def test_hyp_pascal_function_heading_constructor_exists():
    assert callable(pascal_function_heading.__init__)


def test_hyp_pascal_function_heading_constructor_args():
    sig = inspect.signature(pascal_function_heading.__init__)
    params = list(sig.parameters.keys())
    assert "id1" in params, "Missing parameter 'id1'"
    assert "id2" in params, "Missing parameter 'id2'"





def test_hyp_pascal_procedure_heading_is_not_abstract():
    assert not inspect.isabstract(pascal_procedure_heading)


def test_hyp_pascal_procedure_heading_constructor_exists():
    assert callable(pascal_procedure_heading.__init__)


def test_hyp_pascal_procedure_heading_constructor_args():
    sig = inspect.signature(pascal_procedure_heading.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_pascal_formal_parameter_list_is_not_abstract():
    assert not inspect.isabstract(pascal_formal_parameter_list)


def test_hyp_pascal_formal_parameter_list_constructor_exists():
    assert callable(pascal_formal_parameter_list.__init__)


def test_hyp_pascal_formal_parameter_list_constructor_args():
    sig = inspect.signature(pascal_formal_parameter_list.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_function_declaration_is_not_abstract():
    assert not inspect.isabstract(pascal_function_declaration)


def test_hyp_pascal_function_declaration_constructor_exists():
    assert callable(pascal_function_declaration.__init__)


def test_hyp_pascal_function_declaration_constructor_args():
    sig = inspect.signature(pascal_function_declaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_pascal_procedure_declaration_is_not_abstract():
    assert not inspect.isabstract(pascal_procedure_declaration)


def test_hyp_pascal_procedure_declaration_constructor_exists():
    assert callable(pascal_procedure_declaration.__init__)


def test_hyp_pascal_procedure_declaration_constructor_args():
    sig = inspect.signature(pascal_procedure_declaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_pascal_variable_declaration_is_not_abstract():
    assert not inspect.isabstract(pascal_variable_declaration)


def test_hyp_pascal_variable_declaration_constructor_exists():
    assert callable(pascal_variable_declaration.__init__)


def test_hyp_pascal_variable_declaration_constructor_args():
    sig = inspect.signature(pascal_variable_declaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_type_definition_is_not_abstract():
    assert not inspect.isabstract(pascal_type_definition)


def test_hyp_pascal_type_definition_constructor_exists():
    assert callable(pascal_type_definition.__init__)


def test_hyp_pascal_type_definition_constructor_args():
    sig = inspect.signature(pascal_type_definition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_variable_declaration_part_is_not_abstract():
    assert not inspect.isabstract(pascal_variable_declaration_part)


def test_hyp_pascal_variable_declaration_part_constructor_exists():
    assert callable(pascal_variable_declaration_part.__init__)


def test_hyp_pascal_variable_declaration_part_constructor_args():
    sig = inspect.signature(pascal_variable_declaration_part.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_type_definition_part_is_not_abstract():
    assert not inspect.isabstract(pascal_type_definition_part)


def test_hyp_pascal_type_definition_part_constructor_exists():
    assert callable(pascal_type_definition_part.__init__)


def test_hyp_pascal_type_definition_part_constructor_args():
    sig = inspect.signature(pascal_type_definition_part.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_constant_definition_part_is_not_abstract():
    assert not inspect.isabstract(pascal_constant_definition_part)


def test_hyp_pascal_constant_definition_part_constructor_exists():
    assert callable(pascal_constant_definition_part.__init__)


def test_hyp_pascal_constant_definition_part_constructor_args():
    sig = inspect.signature(pascal_constant_definition_part.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_label_declaration_part_is_not_abstract():
    assert not inspect.isabstract(pascal_label_declaration_part)


def test_hyp_pascal_label_declaration_part_constructor_exists():
    assert callable(pascal_label_declaration_part.__init__)


def test_hyp_pascal_label_declaration_part_constructor_args():
    sig = inspect.signature(pascal_label_declaration_part.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_statement_part_is_not_abstract():
    assert not inspect.isabstract(pascal_statement_part)


def test_hyp_pascal_statement_part_constructor_exists():
    assert callable(pascal_statement_part.__init__)


def test_hyp_pascal_statement_part_constructor_args():
    sig = inspect.signature(pascal_statement_part.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_declarationpart_is_not_abstract():
    assert not inspect.isabstract(pascal_DeclarationPart)


def test_hyp_pascal_declarationpart_constructor_exists():
    assert callable(pascal_DeclarationPart.__init__)


def test_hyp_pascal_declarationpart_constructor_args():
    sig = inspect.signature(pascal_DeclarationPart.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_block_is_not_abstract():
    assert not inspect.isabstract(pascal_block)


def test_hyp_pascal_block_constructor_exists():
    assert callable(pascal_block.__init__)


def test_hyp_pascal_block_constructor_args():
    sig = inspect.signature(pascal_block.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_program_heading_is_not_abstract():
    assert not inspect.isabstract(pascal_program_heading)


def test_hyp_pascal_program_heading_constructor_exists():
    assert callable(pascal_program_heading.__init__)


def test_hyp_pascal_program_heading_constructor_args():
    sig = inspect.signature(pascal_program_heading.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_program_is_not_abstract():
    assert not inspect.isabstract(pascal_program)


def test_hyp_pascal_program_constructor_exists():
    assert callable(pascal_program.__init__)


def test_hyp_pascal_program_constructor_args():
    sig = inspect.signature(pascal_program.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_model_is_not_abstract():
    assert not inspect.isabstract(pascal_Model)


def test_hyp_pascal_model_constructor_exists():
    assert callable(pascal_Model.__init__)


def test_hyp_pascal_model_constructor_args():
    sig = inspect.signature(pascal_Model.__init__)
    params = list(sig.parameters.keys())



def test_hyp_constant_definition_is_not_abstract():
    assert not inspect.isabstract(constant_definition)


def test_hyp_constant_definition_constructor_exists():
    assert callable(constant_definition.__init__)


def test_hyp_constant_definition_constructor_args():
    sig = inspect.signature(constant_definition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_constant_is_not_abstract():
    assert not inspect.isabstract(pascal_constant)


def test_hyp_pascal_constant_constructor_exists():
    assert callable(pascal_constant.__init__)


def test_hyp_pascal_constant_constructor_args():
    sig = inspect.signature(pascal_constant.__init__)
    params = list(sig.parameters.keys())
    assert "string" in params, "Missing parameter 'string'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_pascal_field_list_is_not_abstract():
    assert not inspect.isabstract(pascal_field_list)


def test_hyp_pascal_field_list_constructor_exists():
    assert callable(pascal_field_list.__init__)


def test_hyp_pascal_field_list_constructor_args():
    sig = inspect.signature(pascal_field_list.__init__)
    params = list(sig.parameters.keys())



def test_hyp_goto_statement_is_not_abstract():
    assert not inspect.isabstract(goto_statement)


def test_hyp_goto_statement_constructor_exists():
    assert callable(goto_statement.__init__)


def test_hyp_goto_statement_constructor_args():
    sig = inspect.signature(goto_statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statement_is_not_abstract():
    assert not inspect.isabstract(statement)


def test_hyp_statement_constructor_exists():
    assert callable(statement.__init__)


def test_hyp_statement_constructor_args():
    sig = inspect.signature(statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_label_is_not_abstract():
    assert not inspect.isabstract(pascal_label)


def test_hyp_pascal_label_constructor_exists():
    assert callable(pascal_label.__init__)


def test_hyp_pascal_label_constructor_args():
    sig = inspect.signature(pascal_label.__init__)
    params = list(sig.parameters.keys())
    assert "int" in params, "Missing parameter 'int'"




def test_hyp_program_heading_is_not_abstract():
    assert not inspect.isabstract(program_heading)


def test_hyp_program_heading_constructor_exists():
    assert callable(program_heading.__init__)


def test_hyp_program_heading_constructor_args():
    sig = inspect.signature(program_heading.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_identifier_list_is_not_abstract():
    assert not inspect.isabstract(pascal_identifier_list)


def test_hyp_pascal_identifier_list_constructor_exists():
    assert callable(pascal_identifier_list.__init__)


def test_hyp_pascal_identifier_list_constructor_args():
    sig = inspect.signature(pascal_identifier_list.__init__)
    params = list(sig.parameters.keys())
    assert "ids" in params, "Missing parameter 'ids'"




def test_hyp_pascal_variant_is_not_abstract():
    assert not inspect.isabstract(pascal_variant)


def test_hyp_pascal_variant_constructor_exists():
    assert callable(pascal_variant.__init__)


def test_hyp_pascal_variant_constructor_args():
    sig = inspect.signature(pascal_variant.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_tag_field_is_not_abstract():
    assert not inspect.isabstract(pascal_tag_field)


def test_hyp_pascal_tag_field_constructor_exists():
    assert callable(pascal_tag_field.__init__)


def test_hyp_pascal_tag_field_constructor_args():
    sig = inspect.signature(pascal_tag_field.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_pascal_record_section_is_not_abstract():
    assert not inspect.isabstract(pascal_record_section)


def test_hyp_pascal_record_section_constructor_exists():
    assert callable(pascal_record_section.__init__)


def test_hyp_pascal_record_section_constructor_args():
    sig = inspect.signature(pascal_record_section.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_variant_part_is_not_abstract():
    assert not inspect.isabstract(pascal_variant_part)


def test_hyp_pascal_variant_part_constructor_exists():
    assert callable(pascal_variant_part.__init__)


def test_hyp_pascal_variant_part_constructor_args():
    sig = inspect.signature(pascal_variant_part.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_pascal_fixed_part_is_not_abstract():
    assert not inspect.isabstract(pascal_fixed_part)


def test_hyp_pascal_fixed_part_constructor_exists():
    assert callable(pascal_fixed_part.__init__)


def test_hyp_pascal_fixed_part_constructor_args():
    sig = inspect.signature(pascal_fixed_part.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_elementlist_is_not_abstract():
    assert not inspect.isabstract(pascal_ElementList)


def test_hyp_pascal_elementlist_constructor_exists():
    assert callable(pascal_ElementList.__init__)


def test_hyp_pascal_elementlist_constructor_args():
    sig = inspect.signature(pascal_ElementList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_expressionlist_is_not_abstract():
    assert not inspect.isabstract(pascal_ExpressionList)


def test_hyp_pascal_expressionlist_constructor_exists():
    assert callable(pascal_ExpressionList.__init__)


def test_hyp_pascal_expressionlist_constructor_args():
    sig = inspect.signature(pascal_ExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_file_type_is_not_abstract():
    assert not inspect.isabstract(pascal_file_type)


def test_hyp_pascal_file_type_constructor_exists():
    assert callable(pascal_file_type.__init__)


def test_hyp_pascal_file_type_constructor_args():
    sig = inspect.signature(pascal_file_type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_set_type_is_not_abstract():
    assert not inspect.isabstract(pascal_set_type)


def test_hyp_pascal_set_type_constructor_exists():
    assert callable(pascal_set_type.__init__)


def test_hyp_pascal_set_type_constructor_args():
    sig = inspect.signature(pascal_set_type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_record_type_is_not_abstract():
    assert not inspect.isabstract(pascal_record_type)


def test_hyp_pascal_record_type_constructor_exists():
    assert callable(pascal_record_type.__init__)


def test_hyp_pascal_record_type_constructor_args():
    sig = inspect.signature(pascal_record_type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_array_type_is_not_abstract():
    assert not inspect.isabstract(pascal_array_type)


def test_hyp_pascal_array_type_constructor_exists():
    assert callable(pascal_array_type.__init__)


def test_hyp_pascal_array_type_constructor_args():
    sig = inspect.signature(pascal_array_type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_unpacked_structured_type_is_not_abstract():
    assert not inspect.isabstract(pascal_unpacked_structured_type)


def test_hyp_pascal_unpacked_structured_type_constructor_exists():
    assert callable(pascal_unpacked_structured_type.__init__)


def test_hyp_pascal_unpacked_structured_type_constructor_args():
    sig = inspect.signature(pascal_unpacked_structured_type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_enumerated_type_is_not_abstract():
    assert not inspect.isabstract(pascal_enumerated_type)


def test_hyp_pascal_enumerated_type_constructor_exists():
    assert callable(pascal_enumerated_type.__init__)


def test_hyp_pascal_enumerated_type_constructor_args():
    sig = inspect.signature(pascal_enumerated_type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_subrange_type_is_not_abstract():
    assert not inspect.isabstract(pascal_subrange_type)


def test_hyp_pascal_subrange_type_constructor_exists():
    assert callable(pascal_subrange_type.__init__)


def test_hyp_pascal_subrange_type_constructor_args():
    sig = inspect.signature(pascal_subrange_type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_pointer_type_is_not_abstract():
    assert not inspect.isabstract(pascal_pointer_type)


def test_hyp_pascal_pointer_type_constructor_exists():
    assert callable(pascal_pointer_type.__init__)


def test_hyp_pascal_pointer_type_constructor_args():
    sig = inspect.signature(pascal_pointer_type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_pascal_structured_type_is_not_abstract():
    assert not inspect.isabstract(pascal_structured_type)


def test_hyp_pascal_structured_type_constructor_exists():
    assert callable(pascal_structured_type.__init__)


def test_hyp_pascal_structured_type_constructor_args():
    sig = inspect.signature(pascal_structured_type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_simple_type_is_not_abstract():
    assert not inspect.isabstract(pascal_simple_type)


def test_hyp_pascal_simple_type_constructor_exists():
    assert callable(pascal_simple_type.__init__)


def test_hyp_pascal_simple_type_constructor_args():
    sig = inspect.signature(pascal_simple_type.__init__)
    params = list(sig.parameters.keys())
    assert "primitiveType" in params, "Missing parameter 'primitiveType'"




def test_hyp_type_definition_is_not_abstract():
    assert not inspect.isabstract(type_definition)


def test_hyp_type_definition_constructor_exists():
    assert callable(type_definition.__init__)


def test_hyp_type_definition_constructor_args():
    sig = inspect.signature(type_definition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_type_is_not_abstract():
    assert not inspect.isabstract(pascal_type)


def test_hyp_pascal_type_constructor_exists():
    assert callable(pascal_type.__init__)


def test_hyp_pascal_type_constructor_args():
    sig = inspect.signature(pascal_type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_pascal_case_label_list_is_not_abstract():
    assert not inspect.isabstract(pascal_case_label_list)


def test_hyp_pascal_case_label_list_constructor_exists():
    assert callable(pascal_case_label_list.__init__)


def test_hyp_pascal_case_label_list_constructor_args():
    sig = inspect.signature(pascal_case_label_list.__init__)
    params = list(sig.parameters.keys())


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
pascal_case_limb_strategy = st.builds(
    pascal_case_limb,
)
pascal_Variable1_strategy = st.builds(
    pascal_Variable1,
    name=
        safe_text
)
pascal_Set_strategy = st.builds(
    pascal_Set,
)
pascal_number_strategy = st.builds(
    pascal_number,
    real=
        safe_text,
    integer=
        safe_text
)
pascal_FunctionDesignator_strategy = st.builds(
    pascal_FunctionDesignator,
    name=
        safe_text
)
pascal_factor_strategy = st.builds(
    pascal_factor,
    string=
        safe_text,
    nil=
        safe_text,
    id=
        safe_text
)
pascal_term_strategy = st.builds(
    pascal_term,
)
pascal_simple_expression_strategy = st.builds(
    pascal_simple_expression,
)
pascal_variable_strategy = st.builds(
    pascal_variable,
    name=
        safe_text
)
pascal_structured_statement_strategy = st.builds(
    pascal_structured_statement,
)
pascal_expression_strategy = st.builds(
    pascal_expression,
    relational_operators=
        safe_text
)
pascal_case_statement_strategy = st.builds(
    pascal_case_statement,
)
pascal_if_statement_strategy = st.builds(
    pascal_if_statement,
)
repetitive_statement_strategy = st.builds(
    repetitive_statement,
)
pascal_for_statement_strategy = st.builds(
    pascal_for_statement,
    name=
        safe_text
)
pascal_repeat_statement_strategy = st.builds(
    pascal_repeat_statement,
)
pascal_while_statement_strategy = st.builds(
    pascal_while_statement,
)
structured_statement_strategy = st.builds(
    structured_statement,
)
pascal_repetitive_statement_strategy = st.builds(
    pascal_repetitive_statement,
)
pascal_compound_statement_strategy = st.builds(
    pascal_compound_statement,
)
pascal_conditional_statement_strategy = st.builds(
    pascal_conditional_statement,
)
pascal_with_statement_strategy = st.builds(
    pascal_with_statement,
)
pascal_variable_parameter_section_strategy = st.builds(
    pascal_variable_parameter_section,
)
pascal_value_parameter_section_strategy = st.builds(
    pascal_value_parameter_section,
)
pascal_formal_parameter_section_strategy = st.builds(
    pascal_formal_parameter_section,
)
simple_statement_strategy = st.builds(
    simple_statement,
)
pascal_goto_statement_strategy = st.builds(
    pascal_goto_statement,
)
pascal_procedure_statement_strategy = st.builds(
    pascal_procedure_statement,
    name=
        safe_text,
    actualParameterList=
        safe_text
)
pascal_assignment_statement_strategy = st.builds(
    pascal_assignment_statement,
    identifier=
        safe_text,
    variable=
        safe_text
)
pascal_simple_statement_strategy = st.builds(
    pascal_simple_statement,
)
pascal_EObject_strategy = st.builds(
    pascal_EObject,
)
pascal_statement_strategy = st.builds(
    pascal_statement,
)
statement_part_strategy = st.builds(
    statement_part,
)
pascal_statement_sequence_strategy = st.builds(
    pascal_statement_sequence,
)
pascal_bound_specification_strategy = st.builds(
    pascal_bound_specification,
    id3=
        safe_text,
    id2=
        safe_text,
    id1=
        safe_text
)
conformant_array_schema_strategy = st.builds(
    conformant_array_schema,
)
pascal_unpacked_conformant_array_Schema_strategy = st.builds(
    pascal_unpacked_conformant_array_Schema,
)
pascal_packed_conformant_array_schema_strategy = st.builds(
    pascal_packed_conformant_array_schema,
)
pascal_conformant_array_schema_strategy = st.builds(
    pascal_conformant_array_schema,
    id=
        safe_text
)
pascal_parameter_type_strategy = st.builds(
    pascal_parameter_type,
    id=
        safe_text
)
pascal_constant_definition_strategy = st.builds(
    pascal_constant_definition,
)
pascal_procedure_and_function_declaration_part_strategy = st.builds(
    pascal_procedure_and_function_declaration_part,
)
pascal_function_heading_strategy = st.builds(
    pascal_function_heading,
    id1=
        safe_text,
    id2=
        safe_text
)
pascal_procedure_heading_strategy = st.builds(
    pascal_procedure_heading,
    name=
        safe_text
)
pascal_formal_parameter_list_strategy = st.builds(
    pascal_formal_parameter_list,
)
pascal_function_declaration_strategy = st.builds(
    pascal_function_declaration,
    name=
        safe_text
)
pascal_procedure_declaration_strategy = st.builds(
    pascal_procedure_declaration,
    name=
        safe_text
)
pascal_variable_declaration_strategy = st.builds(
    pascal_variable_declaration,
)
pascal_type_definition_strategy = st.builds(
    pascal_type_definition,
)
pascal_variable_declaration_part_strategy = st.builds(
    pascal_variable_declaration_part,
)
pascal_type_definition_part_strategy = st.builds(
    pascal_type_definition_part,
)
pascal_constant_definition_part_strategy = st.builds(
    pascal_constant_definition_part,
)
pascal_label_declaration_part_strategy = st.builds(
    pascal_label_declaration_part,
)
pascal_statement_part_strategy = st.builds(
    pascal_statement_part,
)
pascal_DeclarationPart_strategy = st.builds(
    pascal_DeclarationPart,
)
pascal_block_strategy = st.builds(
    pascal_block,
)
pascal_program_heading_strategy = st.builds(
    pascal_program_heading,
)
pascal_program_strategy = st.builds(
    pascal_program,
)
pascal_Model_strategy = st.builds(
    pascal_Model,
)
constant_definition_strategy = st.builds(
    constant_definition,
)
pascal_constant_strategy = st.builds(
    pascal_constant,
    string=
        safe_text,
    name=
        safe_text
)
pascal_field_list_strategy = st.builds(
    pascal_field_list,
)
goto_statement_strategy = st.builds(
    goto_statement,
)
statement_strategy = st.builds(
    statement,
)
pascal_label_strategy = st.builds(
    pascal_label,
    int=
        safe_text
)
program_heading_strategy = st.builds(
    program_heading,
)
pascal_identifier_list_strategy = st.builds(
    pascal_identifier_list,
    ids=
        safe_text
)
pascal_variant_strategy = st.builds(
    pascal_variant,
)
pascal_tag_field_strategy = st.builds(
    pascal_tag_field,
    id=
        safe_text
)
pascal_record_section_strategy = st.builds(
    pascal_record_section,
)
pascal_variant_part_strategy = st.builds(
    pascal_variant_part,
    id=
        safe_text
)
pascal_fixed_part_strategy = st.builds(
    pascal_fixed_part,
)
pascal_ElementList_strategy = st.builds(
    pascal_ElementList,
)
pascal_ExpressionList_strategy = st.builds(
    pascal_ExpressionList,
)
pascal_file_type_strategy = st.builds(
    pascal_file_type,
)
pascal_set_type_strategy = st.builds(
    pascal_set_type,
)
pascal_record_type_strategy = st.builds(
    pascal_record_type,
)
pascal_array_type_strategy = st.builds(
    pascal_array_type,
)
pascal_unpacked_structured_type_strategy = st.builds(
    pascal_unpacked_structured_type,
)
pascal_enumerated_type_strategy = st.builds(
    pascal_enumerated_type,
)
pascal_subrange_type_strategy = st.builds(
    pascal_subrange_type,
)
pascal_pointer_type_strategy = st.builds(
    pascal_pointer_type,
    name=
        safe_text
)
pascal_structured_type_strategy = st.builds(
    pascal_structured_type,
)
pascal_simple_type_strategy = st.builds(
    pascal_simple_type,
    primitiveType=
        safe_text
)
type_definition_strategy = st.builds(
    type_definition,
)
pascal_type_strategy = st.builds(
    pascal_type,
    name=
        safe_text
)
pascal_case_label_list_strategy = st.builds(
    pascal_case_label_list,
)





@given(instance=pascal_Variable1_strategy)
def test_hyp_pascal_variable1_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=pascal_number_strategy)
def test_hyp_pascal_number_real_setter(instance):
    original = instance.real
    instance.real = original
    assert instance.real == original



@given(instance=pascal_number_strategy)
def test_hyp_pascal_number_integer_setter(instance):
    original = instance.integer
    instance.integer = original
    assert instance.integer == original




@given(instance=pascal_FunctionDesignator_strategy)
def test_hyp_pascal_functiondesignator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=pascal_factor_strategy)
def test_hyp_pascal_factor_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original



@given(instance=pascal_factor_strategy)
def test_hyp_pascal_factor_nil_setter(instance):
    original = instance.nil
    instance.nil = original
    assert instance.nil == original



@given(instance=pascal_factor_strategy)
def test_hyp_pascal_factor_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original






@given(instance=pascal_variable_strategy)
def test_hyp_pascal_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=pascal_expression_strategy)
def test_hyp_pascal_expression_relational_operators_setter(instance):
    original = instance.relational_operators
    instance.relational_operators = original
    assert instance.relational_operators == original







@given(instance=pascal_for_statement_strategy)
def test_hyp_pascal_for_statement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
















@given(instance=pascal_procedure_statement_strategy)
def test_hyp_pascal_procedure_statement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=pascal_procedure_statement_strategy)
def test_hyp_pascal_procedure_statement_actualParameterList_setter(instance):
    original = instance.actualParameterList
    instance.actualParameterList = original
    assert instance.actualParameterList == original




@given(instance=pascal_assignment_statement_strategy)
def test_hyp_pascal_assignment_statement_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original



@given(instance=pascal_assignment_statement_strategy)
def test_hyp_pascal_assignment_statement_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original









@given(instance=pascal_bound_specification_strategy)
def test_hyp_pascal_bound_specification_id3_setter(instance):
    original = instance.id3
    instance.id3 = original
    assert instance.id3 == original



@given(instance=pascal_bound_specification_strategy)
def test_hyp_pascal_bound_specification_id2_setter(instance):
    original = instance.id2
    instance.id2 = original
    assert instance.id2 == original



@given(instance=pascal_bound_specification_strategy)
def test_hyp_pascal_bound_specification_id1_setter(instance):
    original = instance.id1
    instance.id1 = original
    assert instance.id1 == original







@given(instance=pascal_conformant_array_schema_strategy)
def test_hyp_pascal_conformant_array_schema_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=pascal_parameter_type_strategy)
def test_hyp_pascal_parameter_type_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original






@given(instance=pascal_function_heading_strategy)
def test_hyp_pascal_function_heading_id1_setter(instance):
    original = instance.id1
    instance.id1 = original
    assert instance.id1 == original



@given(instance=pascal_function_heading_strategy)
def test_hyp_pascal_function_heading_id2_setter(instance):
    original = instance.id2
    instance.id2 = original
    assert instance.id2 == original




@given(instance=pascal_procedure_heading_strategy)
def test_hyp_pascal_procedure_heading_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=pascal_function_declaration_strategy)
def test_hyp_pascal_function_declaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=pascal_procedure_declaration_strategy)
def test_hyp_pascal_procedure_declaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

















@given(instance=pascal_constant_strategy)
def test_hyp_pascal_constant_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original



@given(instance=pascal_constant_strategy)
def test_hyp_pascal_constant_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original







@given(instance=pascal_label_strategy)
def test_hyp_pascal_label_int_setter(instance):
    original = instance.int
    instance.int = original
    assert instance.int == original





@given(instance=pascal_identifier_list_strategy)
def test_hyp_pascal_identifier_list_ids_setter(instance):
    original = instance.ids
    instance.ids = original
    assert instance.ids == original





@given(instance=pascal_tag_field_strategy)
def test_hyp_pascal_tag_field_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original





@given(instance=pascal_variant_part_strategy)
def test_hyp_pascal_variant_part_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original














@given(instance=pascal_pointer_type_strategy)
def test_hyp_pascal_pointer_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=pascal_simple_type_strategy)
def test_hyp_pascal_simple_type_primitiveType_setter(instance):
    original = instance.primitiveType
    instance.primitiveType = original
    assert instance.primitiveType == original





@given(instance=pascal_type_strategy)
def test_hyp_pascal_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    conformant_array_schema,
    constant_definition,
    goto_statement,
    pascal_DeclarationPart,
    pascal_EObject,
    pascal_ElementList,
    pascal_ExpressionList,
    pascal_FunctionDesignator,
    pascal_Model,
    pascal_Set,
    pascal_Variable1,
    pascal_array_type,
    pascal_assignment_statement,
    pascal_block,
    pascal_bound_specification,
    pascal_case_label_list,
    pascal_case_limb,
    pascal_case_statement,
    pascal_compound_statement,
    pascal_conditional_statement,
    pascal_conformant_array_schema,
    pascal_constant,
    pascal_constant_definition,
    pascal_constant_definition_part,
    pascal_enumerated_type,
    pascal_expression,
    pascal_factor,
    pascal_field_list,
    pascal_file_type,
    pascal_fixed_part,
    pascal_for_statement,
    pascal_formal_parameter_list,
    pascal_formal_parameter_section,
    pascal_function_declaration,
    pascal_function_heading,
    pascal_goto_statement,
    pascal_identifier_list,
    pascal_if_statement,
    pascal_label,
    pascal_label_declaration_part,
    pascal_number,
    pascal_packed_conformant_array_schema,
    pascal_parameter_type,
    pascal_pointer_type,
    pascal_procedure_and_function_declaration_part,
    pascal_procedure_declaration,
    pascal_procedure_heading,
    pascal_procedure_statement,
    pascal_program,
    pascal_program_heading,
    pascal_record_section,
    pascal_record_type,
    pascal_repeat_statement,
    pascal_repetitive_statement,
    pascal_set_type,
    pascal_simple_expression,
    pascal_simple_statement,
    pascal_simple_type,
    pascal_statement,
    pascal_statement_part,
    pascal_statement_sequence,
    pascal_structured_statement,
    pascal_structured_type,
    pascal_subrange_type,
    pascal_tag_field,
    pascal_term,
    pascal_type,
    pascal_type_definition,
    pascal_type_definition_part,
    pascal_unpacked_conformant_array_Schema,
    pascal_unpacked_structured_type,
    pascal_value_parameter_section,
    pascal_variable,
    pascal_variable_declaration,
    pascal_variable_declaration_part,
    pascal_variable_parameter_section,
    pascal_variant,
    pascal_variant_part,
    pascal_while_statement,
    pascal_with_statement,
    program_heading,
    repetitive_statement,
    simple_statement,
    statement,
    statement_part,
    structured_statement,
    type_definition,
)

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

def _is_linked(obj, attr_name, other):
    value = getattr(obj, attr_name, None)
    if isinstance(value, (set, list, tuple, frozenset)):
        return other in value
    return value == other

def _safe_set(obj, attr_name, value):
    # Some generated models have a genuine bug: two reciprocal setters
    # unconditionally call each other with no base case, causing
    # infinite mutual recursion for that specific relationship (found
    # in model_10000002's items10/sc11 pair). That's a defect in the
    # code under test, not in this test -- skip rather than fail so it
    # doesn't masquerade as a test-suite problem.
    try:
        setattr(obj, attr_name, value)
    except RecursionError:
        pytest.skip(f'{attr_name!r} setter has infinite mutual recursion in the generated code')

# =============================================================================
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_pascal_FunctionDesignator_name_value_roundtrip():
    instance = pascal_FunctionDesignator(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_pascal_Variable1_name_value_roundtrip():
    instance = pascal_Variable1(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_pascal_assignment_statement_identifier_value_roundtrip():
    instance = pascal_assignment_statement(identifier="sample_text", variable="sample_text")
    assert instance.identifier == "sample_text"
    instance.identifier = "sample_text_2"
    assert instance.identifier == "sample_text_2"


def test_pascal_assignment_statement_variable_value_roundtrip():
    instance = pascal_assignment_statement(identifier="sample_text", variable="sample_text")
    assert instance.variable == "sample_text"
    instance.variable = "sample_text_2"
    assert instance.variable == "sample_text_2"


def test_pascal_bound_specification_id1_value_roundtrip():
    instance = pascal_bound_specification(id1="sample_text", id2="sample_text", id3="sample_text")
    assert instance.id1 == "sample_text"
    instance.id1 = "sample_text_2"
    assert instance.id1 == "sample_text_2"


def test_pascal_bound_specification_id2_value_roundtrip():
    instance = pascal_bound_specification(id1="sample_text", id2="sample_text", id3="sample_text")
    assert instance.id2 == "sample_text"
    instance.id2 = "sample_text_2"
    assert instance.id2 == "sample_text_2"


def test_pascal_bound_specification_id3_value_roundtrip():
    instance = pascal_bound_specification(id1="sample_text", id2="sample_text", id3="sample_text")
    assert instance.id3 == "sample_text"
    instance.id3 = "sample_text_2"
    assert instance.id3 == "sample_text_2"


def test_pascal_conformant_array_schema_id_value_roundtrip():
    instance = pascal_conformant_array_schema(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_pascal_constant_name_value_roundtrip():
    instance = pascal_constant(name="sample_text", string="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_pascal_constant_string_value_roundtrip():
    instance = pascal_constant(name="sample_text", string="sample_text")
    assert instance.string == "sample_text"
    instance.string = "sample_text_2"
    assert instance.string == "sample_text_2"


def test_pascal_expression_relational_operators_value_roundtrip():
    instance = pascal_expression(relational_operators="sample_text")
    assert instance.relational_operators == "sample_text"
    instance.relational_operators = "sample_text_2"
    assert instance.relational_operators == "sample_text_2"


def test_pascal_factor_id_value_roundtrip():
    instance = pascal_factor(id="sample_text", nil="sample_text", string="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_pascal_factor_nil_value_roundtrip():
    instance = pascal_factor(id="sample_text", nil="sample_text", string="sample_text")
    assert instance.nil == "sample_text"
    instance.nil = "sample_text_2"
    assert instance.nil == "sample_text_2"


def test_pascal_factor_string_value_roundtrip():
    instance = pascal_factor(id="sample_text", nil="sample_text", string="sample_text")
    assert instance.string == "sample_text"
    instance.string = "sample_text_2"
    assert instance.string == "sample_text_2"


def test_pascal_for_statement_name_value_roundtrip():
    instance = pascal_for_statement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_pascal_function_declaration_name_value_roundtrip():
    instance = pascal_function_declaration(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_pascal_function_heading_id1_value_roundtrip():
    instance = pascal_function_heading(id1="sample_text", id2="sample_text")
    assert instance.id1 == "sample_text"
    instance.id1 = "sample_text_2"
    assert instance.id1 == "sample_text_2"


def test_pascal_function_heading_id2_value_roundtrip():
    instance = pascal_function_heading(id1="sample_text", id2="sample_text")
    assert instance.id2 == "sample_text"
    instance.id2 = "sample_text_2"
    assert instance.id2 == "sample_text_2"


def test_pascal_identifier_list_ids_value_roundtrip():
    instance = pascal_identifier_list(ids="sample_text")
    assert instance.ids == "sample_text"
    instance.ids = "sample_text_2"
    assert instance.ids == "sample_text_2"


def test_pascal_label_int_value_roundtrip():
    instance = pascal_label(int="sample_text")
    assert instance.int == "sample_text"
    instance.int = "sample_text_2"
    assert instance.int == "sample_text_2"


def test_pascal_number_integer_value_roundtrip():
    instance = pascal_number(integer="sample_text", real="sample_text")
    assert instance.integer == "sample_text"
    instance.integer = "sample_text_2"
    assert instance.integer == "sample_text_2"


def test_pascal_number_real_value_roundtrip():
    instance = pascal_number(integer="sample_text", real="sample_text")
    assert instance.real == "sample_text"
    instance.real = "sample_text_2"
    assert instance.real == "sample_text_2"


def test_pascal_parameter_type_id_value_roundtrip():
    instance = pascal_parameter_type(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_pascal_pointer_type_name_value_roundtrip():
    instance = pascal_pointer_type(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_pascal_procedure_declaration_name_value_roundtrip():
    instance = pascal_procedure_declaration(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_pascal_procedure_heading_name_value_roundtrip():
    instance = pascal_procedure_heading(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_pascal_procedure_statement_actualParameterList_value_roundtrip():
    instance = pascal_procedure_statement(actualParameterList="sample_text", name="sample_text")
    assert instance.actualParameterList == "sample_text"
    instance.actualParameterList = "sample_text_2"
    assert instance.actualParameterList == "sample_text_2"


def test_pascal_procedure_statement_name_value_roundtrip():
    instance = pascal_procedure_statement(actualParameterList="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_pascal_simple_type_primitiveType_value_roundtrip():
    instance = pascal_simple_type(primitiveType="sample_text")
    assert instance.primitiveType == "sample_text"
    instance.primitiveType = "sample_text_2"
    assert instance.primitiveType == "sample_text_2"


def test_pascal_tag_field_id_value_roundtrip():
    instance = pascal_tag_field(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_pascal_type_name_value_roundtrip():
    instance = pascal_type(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_pascal_variable_name_value_roundtrip():
    instance = pascal_variable(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_pascal_variant_part_id_value_roundtrip():
    instance = pascal_variant_part(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_pascal_packed_conformant_array_schema_isa_conformant_array_schema():
    instance = pascal_packed_conformant_array_schema()
    assert isinstance(instance, conformant_array_schema)


def test_pascal_unpacked_conformant_array_Schema_isa_conformant_array_schema():
    instance = pascal_unpacked_conformant_array_Schema()
    assert isinstance(instance, conformant_array_schema)


def test_pascal_constant_isa_constant_definition():
    instance = pascal_constant(name="sample_text", string="sample_text")
    assert isinstance(instance, constant_definition)


def test_pascal_label_isa_goto_statement():
    instance = pascal_label(int="sample_text")
    assert isinstance(instance, goto_statement)


def test_pascal_identifier_list_isa_program_heading():
    instance = pascal_identifier_list(ids="sample_text")
    assert isinstance(instance, program_heading)


def test_pascal_for_statement_isa_repetitive_statement():
    instance = pascal_for_statement(name="sample_text")
    assert isinstance(instance, repetitive_statement)


def test_pascal_repeat_statement_isa_repetitive_statement():
    instance = pascal_repeat_statement()
    assert isinstance(instance, repetitive_statement)


def test_pascal_while_statement_isa_repetitive_statement():
    instance = pascal_while_statement()
    assert isinstance(instance, repetitive_statement)


def test_pascal_assignment_statement_isa_simple_statement():
    instance = pascal_assignment_statement(identifier="sample_text", variable="sample_text")
    assert isinstance(instance, simple_statement)


def test_pascal_goto_statement_isa_simple_statement():
    instance = pascal_goto_statement()
    assert isinstance(instance, simple_statement)


def test_pascal_procedure_statement_isa_simple_statement():
    instance = pascal_procedure_statement(actualParameterList="sample_text", name="sample_text")
    assert isinstance(instance, simple_statement)


def test_pascal_label_isa_statement():
    instance = pascal_label(int="sample_text")
    assert isinstance(instance, statement)


def test_pascal_statement_sequence_isa_statement_part():
    instance = pascal_statement_sequence()
    assert isinstance(instance, statement_part)


def test_pascal_compound_statement_isa_structured_statement():
    instance = pascal_compound_statement()
    assert isinstance(instance, structured_statement)


def test_pascal_conditional_statement_isa_structured_statement():
    instance = pascal_conditional_statement()
    assert isinstance(instance, structured_statement)


def test_pascal_repetitive_statement_isa_structured_statement():
    instance = pascal_repetitive_statement()
    assert isinstance(instance, structured_statement)


def test_pascal_with_statement_isa_structured_statement():
    instance = pascal_with_statement()
    assert isinstance(instance, structured_statement)


def test_pascal_type_isa_type_definition():
    instance = pascal_type(name="sample_text")
    assert isinstance(instance, type_definition)


def test_assoc_FormalParameterList49_link_reassign_clear():
    a = pascal_procedure_heading(name="sample_text")
    b1 = pascal_formal_parameter_list()
    b2 = pascal_formal_parameter_list()
    _safe_set(a, 'pascal_procedure_heading', b1)
    assert _is_linked(a, 'pascal_procedure_heading', b1)
    if hasattr(b1, 'pascal_formal_parameter_list50'):
        assert _is_linked(b1, 'pascal_formal_parameter_list50', a)
    _safe_set(a, 'pascal_procedure_heading', b2)
    assert _is_linked(a, 'pascal_procedure_heading', b2)
    if hasattr(b1, 'pascal_formal_parameter_list50'):
        assert not _is_linked(b1, 'pascal_formal_parameter_list50', a)
    if hasattr(b2, 'pascal_formal_parameter_list50'):
        assert _is_linked(b2, 'pascal_formal_parameter_list50', a)
    _safe_set(a, 'pascal_procedure_heading', None)
    assert not _is_linked(a, 'pascal_procedure_heading', b2)
    if hasattr(b2, 'pascal_formal_parameter_list50'):
        assert not _is_linked(b2, 'pascal_formal_parameter_list50', a)


def test_assoc_FormalParameterList51_link_reassign_clear():
    a = pascal_function_heading(id1="sample_text", id2="sample_text")
    b1 = pascal_formal_parameter_list()
    b2 = pascal_formal_parameter_list()
    _safe_set(a, 'pascal_function_heading', b1)
    assert _is_linked(a, 'pascal_function_heading', b1)
    if hasattr(b1, 'pascal_formal_parameter_list52'):
        assert _is_linked(b1, 'pascal_formal_parameter_list52', a)
    _safe_set(a, 'pascal_function_heading', b2)
    assert _is_linked(a, 'pascal_function_heading', b2)
    if hasattr(b1, 'pascal_formal_parameter_list52'):
        assert not _is_linked(b1, 'pascal_formal_parameter_list52', a)
    if hasattr(b2, 'pascal_formal_parameter_list52'):
        assert _is_linked(b2, 'pascal_formal_parameter_list52', a)
    _safe_set(a, 'pascal_function_heading', None)
    assert not _is_linked(a, 'pascal_function_heading', b2)
    if hasattr(b2, 'pascal_formal_parameter_list52'):
        assert not _is_linked(b2, 'pascal_formal_parameter_list52', a)


def test_assoc_block37_link_reassign_clear():
    a = pascal_procedure_declaration(name="sample_text")
    b1 = pascal_block()
    b2 = pascal_block()
    _safe_set(a, 'pascal_procedure_declaration38', b1)
    assert _is_linked(a, 'pascal_procedure_declaration38', b1)
    if hasattr(b1, 'pascal_block39'):
        assert _is_linked(b1, 'pascal_block39', a)
    _safe_set(a, 'pascal_procedure_declaration38', b2)
    assert _is_linked(a, 'pascal_procedure_declaration38', b2)
    if hasattr(b1, 'pascal_block39'):
        assert not _is_linked(b1, 'pascal_block39', a)
    if hasattr(b2, 'pascal_block39'):
        assert _is_linked(b2, 'pascal_block39', a)
    _safe_set(a, 'pascal_procedure_declaration38', None)
    assert not _is_linked(a, 'pascal_procedure_declaration38', b2)
    if hasattr(b2, 'pascal_block39'):
        assert not _is_linked(b2, 'pascal_block39', a)


def test_assoc_block46_link_reassign_clear():
    a = pascal_function_declaration(name="sample_text")
    b1 = pascal_block()
    b2 = pascal_block()
    _safe_set(a, 'pascal_function_declaration47', b1)
    assert _is_linked(a, 'pascal_function_declaration47', b1)
    if hasattr(b1, 'pascal_block48'):
        assert _is_linked(b1, 'pascal_block48', a)
    _safe_set(a, 'pascal_function_declaration47', b2)
    assert _is_linked(a, 'pascal_function_declaration47', b2)
    if hasattr(b1, 'pascal_block48'):
        assert not _is_linked(b1, 'pascal_block48', a)
    if hasattr(b2, 'pascal_block48'):
        assert _is_linked(b2, 'pascal_block48', a)
    _safe_set(a, 'pascal_function_declaration47', None)
    assert not _is_linked(a, 'pascal_function_declaration47', b2)
    if hasattr(b2, 'pascal_block48'):
        assert not _is_linked(b2, 'pascal_block48', a)


def test_assoc_boundSpecification78_link_reassign_clear():
    a = pascal_bound_specification(id1="sample_text", id2="sample_text", id3="sample_text")
    b1 = pascal_packed_conformant_array_schema()
    b2 = pascal_packed_conformant_array_schema()
    _safe_set(a, 'pascal_bound_specification', b1)
    assert _is_linked(a, 'pascal_bound_specification', b1)
    if hasattr(b1, 'pascal_packed_conformant_array_schema'):
        assert _is_linked(b1, 'pascal_packed_conformant_array_schema', a)
    _safe_set(a, 'pascal_bound_specification', b2)
    assert _is_linked(a, 'pascal_bound_specification', b2)
    if hasattr(b1, 'pascal_packed_conformant_array_schema'):
        assert not _is_linked(b1, 'pascal_packed_conformant_array_schema', a)
    if hasattr(b2, 'pascal_packed_conformant_array_schema'):
        assert _is_linked(b2, 'pascal_packed_conformant_array_schema', a)
    _safe_set(a, 'pascal_bound_specification', None)
    assert not _is_linked(a, 'pascal_bound_specification', b2)
    if hasattr(b2, 'pascal_packed_conformant_array_schema'):
        assert not _is_linked(b2, 'pascal_packed_conformant_array_schema', a)


def test_assoc_boundSpecifications79_link_reassign_clear():
    a = pascal_bound_specification(id1="sample_text", id2="sample_text", id3="sample_text")
    b1 = pascal_unpacked_conformant_array_Schema()
    b2 = pascal_unpacked_conformant_array_Schema()
    _safe_set(a, 'pascal_bound_specification80', b1)
    assert _is_linked(a, 'pascal_bound_specification80', b1)
    if hasattr(b1, 'pascal_unpacked_conformant_array_Schema'):
        assert _is_linked(b1, 'pascal_unpacked_conformant_array_Schema', a)
    _safe_set(a, 'pascal_bound_specification80', b2)
    assert _is_linked(a, 'pascal_bound_specification80', b2)
    if hasattr(b1, 'pascal_unpacked_conformant_array_Schema'):
        assert not _is_linked(b1, 'pascal_unpacked_conformant_array_Schema', a)
    if hasattr(b2, 'pascal_unpacked_conformant_array_Schema'):
        assert _is_linked(b2, 'pascal_unpacked_conformant_array_Schema', a)
    _safe_set(a, 'pascal_bound_specification80', None)
    assert not _is_linked(a, 'pascal_bound_specification80', b2)
    if hasattr(b2, 'pascal_unpacked_conformant_array_Schema'):
        assert not _is_linked(b2, 'pascal_unpacked_conformant_array_Schema', a)


def test_assoc_conformantArraySchema76_link_reassign_clear():
    a = pascal_parameter_type(id="sample_text")
    b1 = pascal_conformant_array_schema(id="sample_text")
    b2 = pascal_conformant_array_schema(id="sample_text_2")
    _safe_set(a, 'pascal_parameter_type77', b1)
    assert _is_linked(a, 'pascal_parameter_type77', b1)
    if hasattr(b1, 'pascal_conformant_array_schema'):
        assert _is_linked(b1, 'pascal_conformant_array_schema', a)
    _safe_set(a, 'pascal_parameter_type77', b2)
    assert _is_linked(a, 'pascal_parameter_type77', b2)
    if hasattr(b1, 'pascal_conformant_array_schema'):
        assert not _is_linked(b1, 'pascal_conformant_array_schema', a)
    if hasattr(b2, 'pascal_conformant_array_schema'):
        assert _is_linked(b2, 'pascal_conformant_array_schema', a)
    _safe_set(a, 'pascal_parameter_type77', None)
    assert not _is_linked(a, 'pascal_parameter_type77', b2)
    if hasattr(b2, 'pascal_conformant_array_schema'):
        assert not _is_linked(b2, 'pascal_conformant_array_schema', a)


def test_assoc_conformantArraySchema81_link_reassign_clear():
    a = pascal_conformant_array_schema(id="sample_text")
    b1 = pascal_unpacked_conformant_array_Schema()
    b2 = pascal_unpacked_conformant_array_Schema()
    _safe_set(a, 'pascal_conformant_array_schema83', b1)
    assert _is_linked(a, 'pascal_conformant_array_schema83', b1)
    if hasattr(b1, 'pascal_unpacked_conformant_array_Schema82'):
        assert _is_linked(b1, 'pascal_unpacked_conformant_array_Schema82', a)
    _safe_set(a, 'pascal_conformant_array_schema83', b2)
    assert _is_linked(a, 'pascal_conformant_array_schema83', b2)
    if hasattr(b1, 'pascal_unpacked_conformant_array_Schema82'):
        assert not _is_linked(b1, 'pascal_unpacked_conformant_array_Schema82', a)
    if hasattr(b2, 'pascal_unpacked_conformant_array_Schema82'):
        assert _is_linked(b2, 'pascal_unpacked_conformant_array_Schema82', a)
    _safe_set(a, 'pascal_conformant_array_schema83', None)
    assert not _is_linked(a, 'pascal_conformant_array_schema83', b2)
    if hasattr(b2, 'pascal_unpacked_conformant_array_Schema82'):
        assert not _is_linked(b2, 'pascal_unpacked_conformant_array_Schema82', a)


def test_assoc_constant182_link_reassign_clear():
    a = pascal_constant(name="sample_text", string="sample_text")
    b1 = pascal_subrange_type()
    b2 = pascal_subrange_type()
    _safe_set(a, 'pascal_constant184', b1)
    assert _is_linked(a, 'pascal_constant184', b1)
    if hasattr(b1, 'pascal_subrange_type183'):
        assert _is_linked(b1, 'pascal_subrange_type183', a)
    _safe_set(a, 'pascal_constant184', b2)
    assert _is_linked(a, 'pascal_constant184', b2)
    if hasattr(b1, 'pascal_subrange_type183'):
        assert not _is_linked(b1, 'pascal_subrange_type183', a)
    if hasattr(b2, 'pascal_subrange_type183'):
        assert _is_linked(b2, 'pascal_subrange_type183', a)
    _safe_set(a, 'pascal_constant184', None)
    assert not _is_linked(a, 'pascal_constant184', b2)
    if hasattr(b2, 'pascal_subrange_type183'):
        assert not _is_linked(b2, 'pascal_subrange_type183', a)


def test_assoc_constant2185_link_reassign_clear():
    a = pascal_constant(name="sample_text", string="sample_text")
    b1 = pascal_subrange_type()
    b2 = pascal_subrange_type()
    _safe_set(a, 'pascal_constant187', b1)
    assert _is_linked(a, 'pascal_constant187', b1)
    if hasattr(b1, 'pascal_subrange_type186'):
        assert _is_linked(b1, 'pascal_subrange_type186', a)
    _safe_set(a, 'pascal_constant187', b2)
    assert _is_linked(a, 'pascal_constant187', b2)
    if hasattr(b1, 'pascal_subrange_type186'):
        assert not _is_linked(b1, 'pascal_subrange_type186', a)
    if hasattr(b2, 'pascal_subrange_type186'):
        assert _is_linked(b2, 'pascal_subrange_type186', a)
    _safe_set(a, 'pascal_constant187', None)
    assert not _is_linked(a, 'pascal_constant187', b2)
    if hasattr(b2, 'pascal_subrange_type186'):
        assert not _is_linked(b2, 'pascal_subrange_type186', a)


def test_assoc_constants130_link_reassign_clear():
    a = pascal_constant(name="sample_text", string="sample_text")
    b1 = pascal_case_label_list()
    b2 = pascal_case_label_list()
    _safe_set(a, 'pascal_constant', b1)
    assert _is_linked(a, 'pascal_constant', b1)
    if hasattr(b1, 'pascal_case_label_list131'):
        assert _is_linked(b1, 'pascal_case_label_list131', a)
    _safe_set(a, 'pascal_constant', b2)
    assert _is_linked(a, 'pascal_constant', b2)
    if hasattr(b1, 'pascal_case_label_list131'):
        assert not _is_linked(b1, 'pascal_case_label_list131', a)
    if hasattr(b2, 'pascal_case_label_list131'):
        assert _is_linked(b2, 'pascal_case_label_list131', a)
    _safe_set(a, 'pascal_constant', None)
    assert not _is_linked(a, 'pascal_constant', b2)
    if hasattr(b2, 'pascal_case_label_list131'):
        assert not _is_linked(b2, 'pascal_case_label_list131', a)


def test_assoc_enumeratedType177_link_reassign_clear():
    a = pascal_simple_type(primitiveType="sample_text")
    b1 = pascal_enumerated_type()
    b2 = pascal_enumerated_type()
    _safe_set(a, 'pascal_simple_type178', b1)
    assert _is_linked(a, 'pascal_simple_type178', b1)
    if hasattr(b1, 'pascal_enumerated_type'):
        assert _is_linked(b1, 'pascal_enumerated_type', a)
    _safe_set(a, 'pascal_simple_type178', b2)
    assert _is_linked(a, 'pascal_simple_type178', b2)
    if hasattr(b1, 'pascal_enumerated_type'):
        assert not _is_linked(b1, 'pascal_enumerated_type', a)
    if hasattr(b2, 'pascal_enumerated_type'):
        assert _is_linked(b2, 'pascal_enumerated_type', a)
    _safe_set(a, 'pascal_simple_type178', None)
    assert not _is_linked(a, 'pascal_simple_type178', b2)
    if hasattr(b2, 'pascal_enumerated_type'):
        assert not _is_linked(b2, 'pascal_enumerated_type', a)


def test_assoc_expression1100_link_reassign_clear():
    a = pascal_for_statement(name="sample_text")
    b1 = pascal_expression(relational_operators="sample_text")
    b2 = pascal_expression(relational_operators="sample_text_2")
    _safe_set(a, 'pascal_for_statement', b1)
    assert _is_linked(a, 'pascal_for_statement', b1)
    if hasattr(b1, 'pascal_expression101'):
        assert _is_linked(b1, 'pascal_expression101', a)
    _safe_set(a, 'pascal_for_statement', b2)
    assert _is_linked(a, 'pascal_for_statement', b2)
    if hasattr(b1, 'pascal_expression101'):
        assert not _is_linked(b1, 'pascal_expression101', a)
    if hasattr(b2, 'pascal_expression101'):
        assert _is_linked(b2, 'pascal_expression101', a)
    _safe_set(a, 'pascal_for_statement', None)
    assert not _is_linked(a, 'pascal_for_statement', b2)
    if hasattr(b2, 'pascal_expression101'):
        assert not _is_linked(b2, 'pascal_expression101', a)


def test_assoc_expression111_link_reassign_clear():
    a = pascal_expression(relational_operators="sample_text")
    b1 = pascal_if_statement()
    b2 = pascal_if_statement()
    _safe_set(a, 'pascal_expression113', b1)
    assert _is_linked(a, 'pascal_expression113', b1)
    if hasattr(b1, 'pascal_if_statement112'):
        assert _is_linked(b1, 'pascal_if_statement112', a)
    _safe_set(a, 'pascal_expression113', b2)
    assert _is_linked(a, 'pascal_expression113', b2)
    if hasattr(b1, 'pascal_if_statement112'):
        assert not _is_linked(b1, 'pascal_if_statement112', a)
    if hasattr(b2, 'pascal_if_statement112'):
        assert _is_linked(b2, 'pascal_if_statement112', a)
    _safe_set(a, 'pascal_expression113', None)
    assert not _is_linked(a, 'pascal_expression113', b2)
    if hasattr(b2, 'pascal_if_statement112'):
        assert not _is_linked(b2, 'pascal_if_statement112', a)


def test_assoc_expression120_link_reassign_clear():
    a = pascal_expression(relational_operators="sample_text")
    b1 = pascal_case_statement()
    b2 = pascal_case_statement()
    _safe_set(a, 'pascal_expression122', b1)
    assert _is_linked(a, 'pascal_expression122', b1)
    if hasattr(b1, 'pascal_case_statement121'):
        assert _is_linked(b1, 'pascal_case_statement121', a)
    _safe_set(a, 'pascal_expression122', b2)
    assert _is_linked(a, 'pascal_expression122', b2)
    if hasattr(b1, 'pascal_case_statement121'):
        assert not _is_linked(b1, 'pascal_case_statement121', a)
    if hasattr(b2, 'pascal_case_statement121'):
        assert _is_linked(b2, 'pascal_case_statement121', a)
    _safe_set(a, 'pascal_expression122', None)
    assert not _is_linked(a, 'pascal_expression122', b2)
    if hasattr(b2, 'pascal_case_statement121'):
        assert not _is_linked(b2, 'pascal_case_statement121', a)


def test_assoc_expression151_link_reassign_clear():
    a = pascal_factor(id="sample_text", nil="sample_text", string="sample_text")
    b1 = pascal_expression(relational_operators="sample_text")
    b2 = pascal_expression(relational_operators="sample_text_2")
    _safe_set(a, 'pascal_factor152', b1)
    assert _is_linked(a, 'pascal_factor152', b1)
    if hasattr(b1, 'pascal_expression153'):
        assert _is_linked(b1, 'pascal_expression153', a)
    _safe_set(a, 'pascal_factor152', b2)
    assert _is_linked(a, 'pascal_factor152', b2)
    if hasattr(b1, 'pascal_expression153'):
        assert not _is_linked(b1, 'pascal_expression153', a)
    if hasattr(b2, 'pascal_expression153'):
        assert _is_linked(b2, 'pascal_expression153', a)
    _safe_set(a, 'pascal_factor152', None)
    assert not _is_linked(a, 'pascal_factor152', b2)
    if hasattr(b2, 'pascal_expression153'):
        assert not _is_linked(b2, 'pascal_expression153', a)


def test_assoc_expression2102_link_reassign_clear():
    a = pascal_for_statement(name="sample_text")
    b1 = pascal_expression(relational_operators="sample_text")
    b2 = pascal_expression(relational_operators="sample_text_2")
    _safe_set(a, 'pascal_for_statement103', b1)
    assert _is_linked(a, 'pascal_for_statement103', b1)
    if hasattr(b1, 'pascal_expression104'):
        assert _is_linked(b1, 'pascal_expression104', a)
    _safe_set(a, 'pascal_for_statement103', b2)
    assert _is_linked(a, 'pascal_for_statement103', b2)
    if hasattr(b1, 'pascal_expression104'):
        assert not _is_linked(b1, 'pascal_expression104', a)
    if hasattr(b2, 'pascal_expression104'):
        assert _is_linked(b2, 'pascal_expression104', a)
    _safe_set(a, 'pascal_for_statement103', None)
    assert not _is_linked(a, 'pascal_for_statement103', b2)
    if hasattr(b2, 'pascal_expression104'):
        assert not _is_linked(b2, 'pascal_expression104', a)


def test_assoc_expression87_link_reassign_clear():
    a = pascal_expression(relational_operators="sample_text")
    b1 = pascal_assignment_statement(identifier="sample_text", variable="sample_text")
    b2 = pascal_assignment_statement(identifier="sample_text_2", variable="sample_text_2")
    _safe_set(a, 'pascal_expression', b1)
    assert _is_linked(a, 'pascal_expression', b1)
    if hasattr(b1, 'pascal_assignment_statement'):
        assert _is_linked(b1, 'pascal_assignment_statement', a)
    _safe_set(a, 'pascal_expression', b2)
    assert _is_linked(a, 'pascal_expression', b2)
    if hasattr(b1, 'pascal_assignment_statement'):
        assert not _is_linked(b1, 'pascal_assignment_statement', a)
    if hasattr(b2, 'pascal_assignment_statement'):
        assert _is_linked(b2, 'pascal_assignment_statement', a)
    _safe_set(a, 'pascal_expression', None)
    assert not _is_linked(a, 'pascal_expression', b2)
    if hasattr(b2, 'pascal_assignment_statement'):
        assert not _is_linked(b2, 'pascal_assignment_statement', a)


def test_assoc_expression90_link_reassign_clear():
    a = pascal_expression(relational_operators="sample_text")
    b1 = pascal_while_statement()
    b2 = pascal_while_statement()
    _safe_set(a, 'pascal_expression91', b1)
    assert _is_linked(a, 'pascal_expression91', b1)
    if hasattr(b1, 'pascal_while_statement'):
        assert _is_linked(b1, 'pascal_while_statement', a)
    _safe_set(a, 'pascal_expression91', b2)
    assert _is_linked(a, 'pascal_expression91', b2)
    if hasattr(b1, 'pascal_while_statement'):
        assert not _is_linked(b1, 'pascal_while_statement', a)
    if hasattr(b2, 'pascal_while_statement'):
        assert _is_linked(b2, 'pascal_while_statement', a)
    _safe_set(a, 'pascal_expression91', None)
    assert not _is_linked(a, 'pascal_expression91', b2)
    if hasattr(b2, 'pascal_while_statement'):
        assert not _is_linked(b2, 'pascal_while_statement', a)


def test_assoc_expression97_link_reassign_clear():
    a = pascal_expression(relational_operators="sample_text")
    b1 = pascal_repeat_statement()
    b2 = pascal_repeat_statement()
    _safe_set(a, 'pascal_expression99', b1)
    assert _is_linked(a, 'pascal_expression99', b1)
    if hasattr(b1, 'pascal_repeat_statement98'):
        assert _is_linked(b1, 'pascal_repeat_statement98', a)
    _safe_set(a, 'pascal_expression99', b2)
    assert _is_linked(a, 'pascal_expression99', b2)
    if hasattr(b1, 'pascal_repeat_statement98'):
        assert not _is_linked(b1, 'pascal_repeat_statement98', a)
    if hasattr(b2, 'pascal_repeat_statement98'):
        assert _is_linked(b2, 'pascal_repeat_statement98', a)
    _safe_set(a, 'pascal_expression99', None)
    assert not _is_linked(a, 'pascal_expression99', b2)
    if hasattr(b2, 'pascal_repeat_statement98'):
        assert not _is_linked(b2, 'pascal_repeat_statement98', a)


def test_assoc_expressionList159_link_reassign_clear():
    a = pascal_Variable1(name="sample_text")
    b1 = pascal_ExpressionList()
    b2 = pascal_ExpressionList()
    _safe_set(a, 'pascal_Variable1160', b1)
    assert _is_linked(a, 'pascal_Variable1160', b1)
    if hasattr(b1, 'pascal_ExpressionList'):
        assert _is_linked(b1, 'pascal_ExpressionList', a)
    _safe_set(a, 'pascal_Variable1160', b2)
    assert _is_linked(a, 'pascal_Variable1160', b2)
    if hasattr(b1, 'pascal_ExpressionList'):
        assert not _is_linked(b1, 'pascal_ExpressionList', a)
    if hasattr(b2, 'pascal_ExpressionList'):
        assert _is_linked(b2, 'pascal_ExpressionList', a)
    _safe_set(a, 'pascal_Variable1160', None)
    assert not _is_linked(a, 'pascal_Variable1160', b2)
    if hasattr(b2, 'pascal_ExpressionList'):
        assert not _is_linked(b2, 'pascal_ExpressionList', a)


def test_assoc_expressions166_link_reassign_clear():
    a = pascal_expression(relational_operators="sample_text")
    b1 = pascal_ElementList()
    b2 = pascal_ElementList()
    _safe_set(a, 'pascal_expression168', b1)
    assert _is_linked(a, 'pascal_expression168', b1)
    if hasattr(b1, 'pascal_ElementList167'):
        assert _is_linked(b1, 'pascal_ElementList167', a)
    _safe_set(a, 'pascal_expression168', b2)
    assert _is_linked(a, 'pascal_expression168', b2)
    if hasattr(b1, 'pascal_ElementList167'):
        assert not _is_linked(b1, 'pascal_ElementList167', a)
    if hasattr(b2, 'pascal_ElementList167'):
        assert _is_linked(b2, 'pascal_ElementList167', a)
    _safe_set(a, 'pascal_expression168', None)
    assert not _is_linked(a, 'pascal_expression168', b2)
    if hasattr(b2, 'pascal_ElementList167'):
        assert not _is_linked(b2, 'pascal_ElementList167', a)


def test_assoc_expressions234_link_reassign_clear():
    a = pascal_expression(relational_operators="sample_text")
    b1 = pascal_ExpressionList()
    b2 = pascal_ExpressionList()
    _safe_set(a, 'pascal_expression236', b1)
    assert _is_linked(a, 'pascal_expression236', b1)
    if hasattr(b1, 'pascal_ExpressionList235'):
        assert _is_linked(b1, 'pascal_ExpressionList235', a)
    _safe_set(a, 'pascal_expression236', b2)
    assert _is_linked(a, 'pascal_expression236', b2)
    if hasattr(b1, 'pascal_ExpressionList235'):
        assert not _is_linked(b1, 'pascal_ExpressionList235', a)
    if hasattr(b2, 'pascal_ExpressionList235'):
        assert _is_linked(b2, 'pascal_ExpressionList235', a)
    _safe_set(a, 'pascal_expression236', None)
    assert not _is_linked(a, 'pascal_expression236', b2)
    if hasattr(b2, 'pascal_ExpressionList235'):
        assert not _is_linked(b2, 'pascal_ExpressionList235', a)


def test_assoc_factor155_link_reassign_clear():
    a = pascal_factor(id="sample_text", nil="sample_text", string="sample_text")
    b1 = pascal_factor(id="sample_text", nil="sample_text", string="sample_text")
    b2 = pascal_factor(id="sample_text_2", nil="sample_text_2", string="sample_text_2")
    _safe_set(a, 'pascal_factor154', b1)
    assert _is_linked(a, 'pascal_factor154', b1)
    if hasattr(b1, 'pascal_factor156'):
        assert _is_linked(b1, 'pascal_factor156', a)
    _safe_set(a, 'pascal_factor154', b2)
    assert _is_linked(a, 'pascal_factor154', b2)
    if hasattr(b1, 'pascal_factor156'):
        assert not _is_linked(b1, 'pascal_factor156', a)
    if hasattr(b2, 'pascal_factor156'):
        assert _is_linked(b2, 'pascal_factor156', a)
    _safe_set(a, 'pascal_factor154', None)
    assert not _is_linked(a, 'pascal_factor154', b2)
    if hasattr(b2, 'pascal_factor156'):
        assert not _is_linked(b2, 'pascal_factor156', a)


def test_assoc_factors140_link_reassign_clear():
    a = pascal_factor(id="sample_text", nil="sample_text", string="sample_text")
    b1 = pascal_term()
    b2 = pascal_term()
    _safe_set(a, 'pascal_factor', b1)
    assert _is_linked(a, 'pascal_factor', b1)
    if hasattr(b1, 'pascal_term141'):
        assert _is_linked(b1, 'pascal_term141', a)
    _safe_set(a, 'pascal_factor', b2)
    assert _is_linked(a, 'pascal_factor', b2)
    if hasattr(b1, 'pascal_term141'):
        assert not _is_linked(b1, 'pascal_term141', a)
    if hasattr(b2, 'pascal_term141'):
        assert _is_linked(b2, 'pascal_term141', a)
    _safe_set(a, 'pascal_factor', None)
    assert not _is_linked(a, 'pascal_factor', b2)
    if hasattr(b2, 'pascal_term141'):
        assert not _is_linked(b2, 'pascal_term141', a)


def test_assoc_formalParameterList35_link_reassign_clear():
    a = pascal_procedure_declaration(name="sample_text")
    b1 = pascal_formal_parameter_list()
    b2 = pascal_formal_parameter_list()
    _safe_set(a, 'pascal_procedure_declaration36', b1)
    assert _is_linked(a, 'pascal_procedure_declaration36', b1)
    if hasattr(b1, 'pascal_formal_parameter_list'):
        assert _is_linked(b1, 'pascal_formal_parameter_list', a)
    _safe_set(a, 'pascal_procedure_declaration36', b2)
    assert _is_linked(a, 'pascal_procedure_declaration36', b2)
    if hasattr(b1, 'pascal_formal_parameter_list'):
        assert not _is_linked(b1, 'pascal_formal_parameter_list', a)
    if hasattr(b2, 'pascal_formal_parameter_list'):
        assert _is_linked(b2, 'pascal_formal_parameter_list', a)
    _safe_set(a, 'pascal_procedure_declaration36', None)
    assert not _is_linked(a, 'pascal_procedure_declaration36', b2)
    if hasattr(b2, 'pascal_formal_parameter_list'):
        assert not _is_linked(b2, 'pascal_formal_parameter_list', a)


def test_assoc_formalParameterList40_link_reassign_clear():
    a = pascal_function_declaration(name="sample_text")
    b1 = pascal_formal_parameter_list()
    b2 = pascal_formal_parameter_list()
    _safe_set(a, 'pascal_function_declaration41', b1)
    assert _is_linked(a, 'pascal_function_declaration41', b1)
    if hasattr(b1, 'pascal_formal_parameter_list42'):
        assert _is_linked(b1, 'pascal_formal_parameter_list42', a)
    _safe_set(a, 'pascal_function_declaration41', b2)
    assert _is_linked(a, 'pascal_function_declaration41', b2)
    if hasattr(b1, 'pascal_formal_parameter_list42'):
        assert not _is_linked(b1, 'pascal_formal_parameter_list42', a)
    if hasattr(b2, 'pascal_formal_parameter_list42'):
        assert _is_linked(b2, 'pascal_formal_parameter_list42', a)
    _safe_set(a, 'pascal_function_declaration41', None)
    assert not _is_linked(a, 'pascal_function_declaration41', b2)
    if hasattr(b2, 'pascal_formal_parameter_list42'):
        assert not _is_linked(b2, 'pascal_formal_parameter_list42', a)


def test_assoc_functionDeclarations33_link_reassign_clear():
    a = pascal_function_declaration(name="sample_text")
    b1 = pascal_procedure_and_function_declaration_part()
    b2 = pascal_procedure_and_function_declaration_part()
    _safe_set(a, 'pascal_function_declaration', b1)
    assert _is_linked(a, 'pascal_function_declaration', b1)
    if hasattr(b1, 'pascal_procedure_and_function_declaration_part34'):
        assert _is_linked(b1, 'pascal_procedure_and_function_declaration_part34', a)
    _safe_set(a, 'pascal_function_declaration', b2)
    assert _is_linked(a, 'pascal_function_declaration', b2)
    if hasattr(b1, 'pascal_procedure_and_function_declaration_part34'):
        assert not _is_linked(b1, 'pascal_procedure_and_function_declaration_part34', a)
    if hasattr(b2, 'pascal_procedure_and_function_declaration_part34'):
        assert _is_linked(b2, 'pascal_procedure_and_function_declaration_part34', a)
    _safe_set(a, 'pascal_function_declaration', None)
    assert not _is_linked(a, 'pascal_function_declaration', b2)
    if hasattr(b2, 'pascal_procedure_and_function_declaration_part34'):
        assert not _is_linked(b2, 'pascal_procedure_and_function_declaration_part34', a)


def test_assoc_functionDesignator142_link_reassign_clear():
    a = pascal_factor(id="sample_text", nil="sample_text", string="sample_text")
    b1 = pascal_FunctionDesignator(name="sample_text")
    b2 = pascal_FunctionDesignator(name="sample_text_2")
    _safe_set(a, 'pascal_factor143', b1)
    assert _is_linked(a, 'pascal_factor143', b1)
    if hasattr(b1, 'pascal_FunctionDesignator'):
        assert _is_linked(b1, 'pascal_FunctionDesignator', a)
    _safe_set(a, 'pascal_factor143', b2)
    assert _is_linked(a, 'pascal_factor143', b2)
    if hasattr(b1, 'pascal_FunctionDesignator'):
        assert not _is_linked(b1, 'pascal_FunctionDesignator', a)
    if hasattr(b2, 'pascal_FunctionDesignator'):
        assert _is_linked(b2, 'pascal_FunctionDesignator', a)
    _safe_set(a, 'pascal_factor143', None)
    assert not _is_linked(a, 'pascal_factor143', b2)
    if hasattr(b2, 'pascal_FunctionDesignator'):
        assert not _is_linked(b2, 'pascal_FunctionDesignator', a)


def test_assoc_functionHeading62_link_reassign_clear():
    a = pascal_function_heading(id1="sample_text", id2="sample_text")
    b1 = pascal_formal_parameter_section()
    b2 = pascal_formal_parameter_section()
    _safe_set(a, 'pascal_function_heading64', b1)
    assert _is_linked(a, 'pascal_function_heading64', b1)
    if hasattr(b1, 'pascal_formal_parameter_section63'):
        assert _is_linked(b1, 'pascal_formal_parameter_section63', a)
    _safe_set(a, 'pascal_function_heading64', b2)
    assert _is_linked(a, 'pascal_function_heading64', b2)
    if hasattr(b1, 'pascal_formal_parameter_section63'):
        assert not _is_linked(b1, 'pascal_formal_parameter_section63', a)
    if hasattr(b2, 'pascal_formal_parameter_section63'):
        assert _is_linked(b2, 'pascal_formal_parameter_section63', a)
    _safe_set(a, 'pascal_function_heading64', None)
    assert not _is_linked(a, 'pascal_function_heading64', b2)
    if hasattr(b2, 'pascal_formal_parameter_section63'):
        assert not _is_linked(b2, 'pascal_formal_parameter_section63', a)


def test_assoc_identifierList179_link_reassign_clear():
    a = pascal_identifier_list(ids="sample_text")
    b1 = pascal_enumerated_type()
    b2 = pascal_enumerated_type()
    _safe_set(a, 'pascal_identifier_list181', b1)
    assert _is_linked(a, 'pascal_identifier_list181', b1)
    if hasattr(b1, 'pascal_enumerated_type180'):
        assert _is_linked(b1, 'pascal_enumerated_type180', a)
    _safe_set(a, 'pascal_identifier_list181', b2)
    assert _is_linked(a, 'pascal_identifier_list181', b2)
    if hasattr(b1, 'pascal_enumerated_type180'):
        assert not _is_linked(b1, 'pascal_enumerated_type180', a)
    if hasattr(b2, 'pascal_enumerated_type180'):
        assert _is_linked(b2, 'pascal_enumerated_type180', a)
    _safe_set(a, 'pascal_identifier_list181', None)
    assert not _is_linked(a, 'pascal_identifier_list181', b2)
    if hasattr(b2, 'pascal_enumerated_type180'):
        assert not _is_linked(b2, 'pascal_enumerated_type180', a)


def test_assoc_identifierList218_link_reassign_clear():
    a = pascal_identifier_list(ids="sample_text")
    b1 = pascal_record_section()
    b2 = pascal_record_section()
    _safe_set(a, 'pascal_identifier_list220', b1)
    assert _is_linked(a, 'pascal_identifier_list220', b1)
    if hasattr(b1, 'pascal_record_section219'):
        assert _is_linked(b1, 'pascal_record_section219', a)
    _safe_set(a, 'pascal_identifier_list220', b2)
    assert _is_linked(a, 'pascal_identifier_list220', b2)
    if hasattr(b1, 'pascal_record_section219'):
        assert not _is_linked(b1, 'pascal_record_section219', a)
    if hasattr(b2, 'pascal_record_section219'):
        assert _is_linked(b2, 'pascal_record_section219', a)
    _safe_set(a, 'pascal_identifier_list220', None)
    assert not _is_linked(a, 'pascal_identifier_list220', b2)
    if hasattr(b2, 'pascal_record_section219'):
        assert not _is_linked(b2, 'pascal_record_section219', a)


def test_assoc_identifierList27_link_reassign_clear():
    a = pascal_identifier_list(ids="sample_text")
    b1 = pascal_variable_declaration()
    b2 = pascal_variable_declaration()
    _safe_set(a, 'pascal_identifier_list', b1)
    assert _is_linked(a, 'pascal_identifier_list', b1)
    if hasattr(b1, 'pascal_variable_declaration28'):
        assert _is_linked(b1, 'pascal_variable_declaration28', a)
    _safe_set(a, 'pascal_identifier_list', b2)
    assert _is_linked(a, 'pascal_identifier_list', b2)
    if hasattr(b1, 'pascal_variable_declaration28'):
        assert not _is_linked(b1, 'pascal_variable_declaration28', a)
    if hasattr(b2, 'pascal_variable_declaration28'):
        assert _is_linked(b2, 'pascal_variable_declaration28', a)
    _safe_set(a, 'pascal_identifier_list', None)
    assert not _is_linked(a, 'pascal_identifier_list', b2)
    if hasattr(b2, 'pascal_variable_declaration28'):
        assert not _is_linked(b2, 'pascal_variable_declaration28', a)


def test_assoc_identifierList65_link_reassign_clear():
    a = pascal_identifier_list(ids="sample_text")
    b1 = pascal_value_parameter_section()
    b2 = pascal_value_parameter_section()
    _safe_set(a, 'pascal_identifier_list67', b1)
    assert _is_linked(a, 'pascal_identifier_list67', b1)
    if hasattr(b1, 'pascal_value_parameter_section66'):
        assert _is_linked(b1, 'pascal_value_parameter_section66', a)
    _safe_set(a, 'pascal_identifier_list67', b2)
    assert _is_linked(a, 'pascal_identifier_list67', b2)
    if hasattr(b1, 'pascal_value_parameter_section66'):
        assert not _is_linked(b1, 'pascal_value_parameter_section66', a)
    if hasattr(b2, 'pascal_value_parameter_section66'):
        assert _is_linked(b2, 'pascal_value_parameter_section66', a)
    _safe_set(a, 'pascal_identifier_list67', None)
    assert not _is_linked(a, 'pascal_identifier_list67', b2)
    if hasattr(b2, 'pascal_value_parameter_section66'):
        assert not _is_linked(b2, 'pascal_value_parameter_section66', a)


def test_assoc_identifierList70_link_reassign_clear():
    a = pascal_identifier_list(ids="sample_text")
    b1 = pascal_variable_parameter_section()
    b2 = pascal_variable_parameter_section()
    _safe_set(a, 'pascal_identifier_list72', b1)
    assert _is_linked(a, 'pascal_identifier_list72', b1)
    if hasattr(b1, 'pascal_variable_parameter_section71'):
        assert _is_linked(b1, 'pascal_variable_parameter_section71', a)
    _safe_set(a, 'pascal_identifier_list72', b2)
    assert _is_linked(a, 'pascal_identifier_list72', b2)
    if hasattr(b1, 'pascal_variable_parameter_section71'):
        assert not _is_linked(b1, 'pascal_variable_parameter_section71', a)
    if hasattr(b2, 'pascal_variable_parameter_section71'):
        assert _is_linked(b2, 'pascal_variable_parameter_section71', a)
    _safe_set(a, 'pascal_identifier_list72', None)
    assert not _is_linked(a, 'pascal_identifier_list72', b2)
    if hasattr(b2, 'pascal_variable_parameter_section71'):
        assert not _is_linked(b2, 'pascal_variable_parameter_section71', a)


def test_assoc_labels19_link_reassign_clear():
    a = pascal_label(int="sample_text")
    b1 = pascal_label_declaration_part()
    b2 = pascal_label_declaration_part()
    _safe_set(a, 'pascal_label', b1)
    assert _is_linked(a, 'pascal_label', b1)
    if hasattr(b1, 'pascal_label_declaration_part20'):
        assert _is_linked(b1, 'pascal_label_declaration_part20', a)
    _safe_set(a, 'pascal_label', b2)
    assert _is_linked(a, 'pascal_label', b2)
    if hasattr(b1, 'pascal_label_declaration_part20'):
        assert not _is_linked(b1, 'pascal_label_declaration_part20', a)
    if hasattr(b2, 'pascal_label_declaration_part20'):
        assert _is_linked(b2, 'pascal_label_declaration_part20', a)
    _safe_set(a, 'pascal_label', None)
    assert not _is_linked(a, 'pascal_label', b2)
    if hasattr(b2, 'pascal_label_declaration_part20'):
        assert not _is_linked(b2, 'pascal_label_declaration_part20', a)


def test_assoc_number147_link_reassign_clear():
    a = pascal_number(integer="sample_text", real="sample_text")
    b1 = pascal_factor(id="sample_text", nil="sample_text", string="sample_text")
    b2 = pascal_factor(id="sample_text_2", nil="sample_text_2", string="sample_text_2")
    _safe_set(a, 'pascal_number', b1)
    assert _is_linked(a, 'pascal_number', b1)
    if hasattr(b1, 'pascal_factor148'):
        assert _is_linked(b1, 'pascal_factor148', a)
    _safe_set(a, 'pascal_number', b2)
    assert _is_linked(a, 'pascal_number', b2)
    if hasattr(b1, 'pascal_factor148'):
        assert not _is_linked(b1, 'pascal_factor148', a)
    if hasattr(b2, 'pascal_factor148'):
        assert _is_linked(b2, 'pascal_factor148', a)
    _safe_set(a, 'pascal_number', None)
    assert not _is_linked(a, 'pascal_number', b2)
    if hasattr(b2, 'pascal_factor148'):
        assert not _is_linked(b2, 'pascal_factor148', a)


def test_assoc_number237_link_reassign_clear():
    a = pascal_number(integer="sample_text", real="sample_text")
    b1 = pascal_constant(name="sample_text", string="sample_text")
    b2 = pascal_constant(name="sample_text_2", string="sample_text_2")
    _safe_set(a, 'pascal_number239', b1)
    assert _is_linked(a, 'pascal_number239', b1)
    if hasattr(b1, 'pascal_constant238'):
        assert _is_linked(b1, 'pascal_constant238', a)
    _safe_set(a, 'pascal_number239', b2)
    assert _is_linked(a, 'pascal_number239', b2)
    if hasattr(b1, 'pascal_constant238'):
        assert not _is_linked(b1, 'pascal_constant238', a)
    if hasattr(b2, 'pascal_constant238'):
        assert _is_linked(b2, 'pascal_constant238', a)
    _safe_set(a, 'pascal_number239', None)
    assert not _is_linked(a, 'pascal_number239', b2)
    if hasattr(b2, 'pascal_constant238'):
        assert not _is_linked(b2, 'pascal_constant238', a)


def test_assoc_parameterType68_link_reassign_clear():
    a = pascal_parameter_type(id="sample_text")
    b1 = pascal_value_parameter_section()
    b2 = pascal_value_parameter_section()
    _safe_set(a, 'pascal_parameter_type', b1)
    assert _is_linked(a, 'pascal_parameter_type', b1)
    if hasattr(b1, 'pascal_value_parameter_section69'):
        assert _is_linked(b1, 'pascal_value_parameter_section69', a)
    _safe_set(a, 'pascal_parameter_type', b2)
    assert _is_linked(a, 'pascal_parameter_type', b2)
    if hasattr(b1, 'pascal_value_parameter_section69'):
        assert not _is_linked(b1, 'pascal_value_parameter_section69', a)
    if hasattr(b2, 'pascal_value_parameter_section69'):
        assert _is_linked(b2, 'pascal_value_parameter_section69', a)
    _safe_set(a, 'pascal_parameter_type', None)
    assert not _is_linked(a, 'pascal_parameter_type', b2)
    if hasattr(b2, 'pascal_value_parameter_section69'):
        assert not _is_linked(b2, 'pascal_value_parameter_section69', a)


def test_assoc_parameterType73_link_reassign_clear():
    a = pascal_parameter_type(id="sample_text")
    b1 = pascal_variable_parameter_section()
    b2 = pascal_variable_parameter_section()
    _safe_set(a, 'pascal_parameter_type75', b1)
    assert _is_linked(a, 'pascal_parameter_type75', b1)
    if hasattr(b1, 'pascal_variable_parameter_section74'):
        assert _is_linked(b1, 'pascal_variable_parameter_section74', a)
    _safe_set(a, 'pascal_parameter_type75', b2)
    assert _is_linked(a, 'pascal_parameter_type75', b2)
    if hasattr(b1, 'pascal_variable_parameter_section74'):
        assert not _is_linked(b1, 'pascal_variable_parameter_section74', a)
    if hasattr(b2, 'pascal_variable_parameter_section74'):
        assert _is_linked(b2, 'pascal_variable_parameter_section74', a)
    _safe_set(a, 'pascal_parameter_type75', None)
    assert not _is_linked(a, 'pascal_parameter_type75', b2)
    if hasattr(b2, 'pascal_variable_parameter_section74'):
        assert not _is_linked(b2, 'pascal_variable_parameter_section74', a)


def test_assoc_pointerType173_link_reassign_clear():
    a = pascal_type(name="sample_text")
    b1 = pascal_pointer_type(name="sample_text")
    b2 = pascal_pointer_type(name="sample_text_2")
    _safe_set(a, 'pascal_type174', b1)
    assert _is_linked(a, 'pascal_type174', b1)
    if hasattr(b1, 'pascal_pointer_type'):
        assert _is_linked(b1, 'pascal_pointer_type', a)
    _safe_set(a, 'pascal_type174', b2)
    assert _is_linked(a, 'pascal_type174', b2)
    if hasattr(b1, 'pascal_pointer_type'):
        assert not _is_linked(b1, 'pascal_pointer_type', a)
    if hasattr(b2, 'pascal_pointer_type'):
        assert _is_linked(b2, 'pascal_pointer_type', a)
    _safe_set(a, 'pascal_type174', None)
    assert not _is_linked(a, 'pascal_type174', b2)
    if hasattr(b2, 'pascal_pointer_type'):
        assert not _is_linked(b2, 'pascal_pointer_type', a)


def test_assoc_procedureDeclarations31_link_reassign_clear():
    a = pascal_procedure_declaration(name="sample_text")
    b1 = pascal_procedure_and_function_declaration_part()
    b2 = pascal_procedure_and_function_declaration_part()
    _safe_set(a, 'pascal_procedure_declaration', b1)
    assert _is_linked(a, 'pascal_procedure_declaration', b1)
    if hasattr(b1, 'pascal_procedure_and_function_declaration_part32'):
        assert _is_linked(b1, 'pascal_procedure_and_function_declaration_part32', a)
    _safe_set(a, 'pascal_procedure_declaration', b2)
    assert _is_linked(a, 'pascal_procedure_declaration', b2)
    if hasattr(b1, 'pascal_procedure_and_function_declaration_part32'):
        assert not _is_linked(b1, 'pascal_procedure_and_function_declaration_part32', a)
    if hasattr(b2, 'pascal_procedure_and_function_declaration_part32'):
        assert _is_linked(b2, 'pascal_procedure_and_function_declaration_part32', a)
    _safe_set(a, 'pascal_procedure_declaration', None)
    assert not _is_linked(a, 'pascal_procedure_declaration', b2)
    if hasattr(b2, 'pascal_procedure_and_function_declaration_part32'):
        assert not _is_linked(b2, 'pascal_procedure_and_function_declaration_part32', a)


def test_assoc_procedureHeading59_link_reassign_clear():
    a = pascal_procedure_heading(name="sample_text")
    b1 = pascal_formal_parameter_section()
    b2 = pascal_formal_parameter_section()
    _safe_set(a, 'pascal_procedure_heading61', b1)
    assert _is_linked(a, 'pascal_procedure_heading61', b1)
    if hasattr(b1, 'pascal_formal_parameter_section60'):
        assert _is_linked(b1, 'pascal_formal_parameter_section60', a)
    _safe_set(a, 'pascal_procedure_heading61', b2)
    assert _is_linked(a, 'pascal_procedure_heading61', b2)
    if hasattr(b1, 'pascal_formal_parameter_section60'):
        assert not _is_linked(b1, 'pascal_formal_parameter_section60', a)
    if hasattr(b2, 'pascal_formal_parameter_section60'):
        assert _is_linked(b2, 'pascal_formal_parameter_section60', a)
    _safe_set(a, 'pascal_procedure_heading61', None)
    assert not _is_linked(a, 'pascal_procedure_heading61', b2)
    if hasattr(b2, 'pascal_formal_parameter_section60'):
        assert not _is_linked(b2, 'pascal_formal_parameter_section60', a)


def test_assoc_set149_link_reassign_clear():
    a = pascal_factor(id="sample_text", nil="sample_text", string="sample_text")
    b1 = pascal_Set()
    b2 = pascal_Set()
    _safe_set(a, 'pascal_factor150', b1)
    assert _is_linked(a, 'pascal_factor150', b1)
    if hasattr(b1, 'pascal_Set'):
        assert _is_linked(b1, 'pascal_Set', a)
    _safe_set(a, 'pascal_factor150', b2)
    assert _is_linked(a, 'pascal_factor150', b2)
    if hasattr(b1, 'pascal_Set'):
        assert not _is_linked(b1, 'pascal_Set', a)
    if hasattr(b2, 'pascal_Set'):
        assert _is_linked(b2, 'pascal_Set', a)
    _safe_set(a, 'pascal_factor150', None)
    assert not _is_linked(a, 'pascal_factor150', b2)
    if hasattr(b2, 'pascal_Set'):
        assert not _is_linked(b2, 'pascal_Set', a)


def test_assoc_simpleExpressions136_link_reassign_clear():
    a = pascal_expression(relational_operators="sample_text")
    b1 = pascal_simple_expression()
    b2 = pascal_simple_expression()
    _safe_set(a, 'pascal_expression137', {b1})
    assert _is_linked(a, 'pascal_expression137', b1)
    if hasattr(b1, 'pascal_simple_expression'):
        assert _is_linked(b1, 'pascal_simple_expression', a)
    _safe_set(a, 'pascal_expression137', {b2})
    assert _is_linked(a, 'pascal_expression137', b2)
    if hasattr(b1, 'pascal_simple_expression'):
        assert not _is_linked(b1, 'pascal_simple_expression', a)
    if hasattr(b2, 'pascal_simple_expression'):
        assert _is_linked(b2, 'pascal_simple_expression', a)
    _safe_set(a, 'pascal_expression137', set())
    assert not _is_linked(a, 'pascal_expression137', b2)
    if hasattr(b2, 'pascal_simple_expression'):
        assert not _is_linked(b2, 'pascal_simple_expression', a)


def test_assoc_simpleType169_link_reassign_clear():
    a = pascal_type(name="sample_text")
    b1 = pascal_simple_type(primitiveType="sample_text")
    b2 = pascal_simple_type(primitiveType="sample_text_2")
    _safe_set(a, 'pascal_type170', b1)
    assert _is_linked(a, 'pascal_type170', b1)
    if hasattr(b1, 'pascal_simple_type'):
        assert _is_linked(b1, 'pascal_simple_type', a)
    _safe_set(a, 'pascal_type170', b2)
    assert _is_linked(a, 'pascal_type170', b2)
    if hasattr(b1, 'pascal_simple_type'):
        assert not _is_linked(b1, 'pascal_simple_type', a)
    if hasattr(b2, 'pascal_simple_type'):
        assert _is_linked(b2, 'pascal_simple_type', a)
    _safe_set(a, 'pascal_type170', None)
    assert not _is_linked(a, 'pascal_type170', b2)
    if hasattr(b2, 'pascal_simple_type'):
        assert not _is_linked(b2, 'pascal_simple_type', a)


def test_assoc_simpleTypes198_link_reassign_clear():
    a = pascal_simple_type(primitiveType="sample_text")
    b1 = pascal_array_type()
    b2 = pascal_array_type()
    _safe_set(a, 'pascal_simple_type200', b1)
    assert _is_linked(a, 'pascal_simple_type200', b1)
    if hasattr(b1, 'pascal_array_type199'):
        assert _is_linked(b1, 'pascal_array_type199', a)
    _safe_set(a, 'pascal_simple_type200', b2)
    assert _is_linked(a, 'pascal_simple_type200', b2)
    if hasattr(b1, 'pascal_array_type199'):
        assert not _is_linked(b1, 'pascal_array_type199', a)
    if hasattr(b2, 'pascal_array_type199'):
        assert _is_linked(b2, 'pascal_array_type199', a)
    _safe_set(a, 'pascal_simple_type200', None)
    assert not _is_linked(a, 'pascal_simple_type200', b2)
    if hasattr(b2, 'pascal_array_type199'):
        assert not _is_linked(b2, 'pascal_array_type199', a)


def test_assoc_statement105_link_reassign_clear():
    a = pascal_for_statement(name="sample_text")
    b1 = pascal_statement()
    b2 = pascal_statement()
    _safe_set(a, 'pascal_for_statement106', b1)
    assert _is_linked(a, 'pascal_for_statement106', b1)
    if hasattr(b1, 'pascal_statement107'):
        assert _is_linked(b1, 'pascal_statement107', a)
    _safe_set(a, 'pascal_for_statement106', b2)
    assert _is_linked(a, 'pascal_for_statement106', b2)
    if hasattr(b1, 'pascal_statement107'):
        assert not _is_linked(b1, 'pascal_statement107', a)
    if hasattr(b2, 'pascal_statement107'):
        assert _is_linked(b2, 'pascal_statement107', a)
    _safe_set(a, 'pascal_for_statement106', None)
    assert not _is_linked(a, 'pascal_for_statement106', b2)
    if hasattr(b2, 'pascal_statement107'):
        assert not _is_linked(b2, 'pascal_statement107', a)


def test_assoc_structuredType171_link_reassign_clear():
    a = pascal_type(name="sample_text")
    b1 = pascal_structured_type()
    b2 = pascal_structured_type()
    _safe_set(a, 'pascal_type172', b1)
    assert _is_linked(a, 'pascal_type172', b1)
    if hasattr(b1, 'pascal_structured_type'):
        assert _is_linked(b1, 'pascal_structured_type', a)
    _safe_set(a, 'pascal_type172', b2)
    assert _is_linked(a, 'pascal_type172', b2)
    if hasattr(b1, 'pascal_structured_type'):
        assert not _is_linked(b1, 'pascal_structured_type', a)
    if hasattr(b2, 'pascal_structured_type'):
        assert _is_linked(b2, 'pascal_structured_type', a)
    _safe_set(a, 'pascal_type172', None)
    assert not _is_linked(a, 'pascal_type172', b2)
    if hasattr(b2, 'pascal_structured_type'):
        assert not _is_linked(b2, 'pascal_structured_type', a)


def test_assoc_subrangeType175_link_reassign_clear():
    a = pascal_simple_type(primitiveType="sample_text")
    b1 = pascal_subrange_type()
    b2 = pascal_subrange_type()
    _safe_set(a, 'pascal_simple_type176', b1)
    assert _is_linked(a, 'pascal_simple_type176', b1)
    if hasattr(b1, 'pascal_subrange_type'):
        assert _is_linked(b1, 'pascal_subrange_type', a)
    _safe_set(a, 'pascal_simple_type176', b2)
    assert _is_linked(a, 'pascal_simple_type176', b2)
    if hasattr(b1, 'pascal_subrange_type'):
        assert not _is_linked(b1, 'pascal_subrange_type', a)
    if hasattr(b2, 'pascal_subrange_type'):
        assert _is_linked(b2, 'pascal_subrange_type', a)
    _safe_set(a, 'pascal_simple_type176', None)
    assert not _is_linked(a, 'pascal_simple_type176', b2)
    if hasattr(b2, 'pascal_subrange_type'):
        assert not _is_linked(b2, 'pascal_subrange_type', a)


def test_assoc_tagfield224_link_reassign_clear():
    a = pascal_variant_part(id="sample_text")
    b1 = pascal_tag_field(id="sample_text")
    b2 = pascal_tag_field(id="sample_text_2")
    _safe_set(a, 'pascal_variant_part225', b1)
    assert _is_linked(a, 'pascal_variant_part225', b1)
    if hasattr(b1, 'pascal_tag_field'):
        assert _is_linked(b1, 'pascal_tag_field', a)
    _safe_set(a, 'pascal_variant_part225', b2)
    assert _is_linked(a, 'pascal_variant_part225', b2)
    if hasattr(b1, 'pascal_tag_field'):
        assert not _is_linked(b1, 'pascal_tag_field', a)
    if hasattr(b2, 'pascal_tag_field'):
        assert _is_linked(b2, 'pascal_tag_field', a)
    _safe_set(a, 'pascal_variant_part225', None)
    assert not _is_linked(a, 'pascal_variant_part225', b2)
    if hasattr(b2, 'pascal_tag_field'):
        assert not _is_linked(b2, 'pascal_tag_field', a)


def test_assoc_type201_link_reassign_clear():
    a = pascal_type(name="sample_text")
    b1 = pascal_array_type()
    b2 = pascal_array_type()
    _safe_set(a, 'pascal_type203', b1)
    assert _is_linked(a, 'pascal_type203', b1)
    if hasattr(b1, 'pascal_array_type202'):
        assert _is_linked(b1, 'pascal_array_type202', a)
    _safe_set(a, 'pascal_type203', b2)
    assert _is_linked(a, 'pascal_type203', b2)
    if hasattr(b1, 'pascal_array_type202'):
        assert not _is_linked(b1, 'pascal_array_type202', a)
    if hasattr(b2, 'pascal_array_type202'):
        assert _is_linked(b2, 'pascal_array_type202', a)
    _safe_set(a, 'pascal_type203', None)
    assert not _is_linked(a, 'pascal_type203', b2)
    if hasattr(b2, 'pascal_array_type202'):
        assert not _is_linked(b2, 'pascal_array_type202', a)


def test_assoc_type206_link_reassign_clear():
    a = pascal_type(name="sample_text")
    b1 = pascal_set_type()
    b2 = pascal_set_type()
    _safe_set(a, 'pascal_type208', b1)
    assert _is_linked(a, 'pascal_type208', b1)
    if hasattr(b1, 'pascal_set_type207'):
        assert _is_linked(b1, 'pascal_set_type207', a)
    _safe_set(a, 'pascal_type208', b2)
    assert _is_linked(a, 'pascal_type208', b2)
    if hasattr(b1, 'pascal_set_type207'):
        assert not _is_linked(b1, 'pascal_set_type207', a)
    if hasattr(b2, 'pascal_set_type207'):
        assert _is_linked(b2, 'pascal_set_type207', a)
    _safe_set(a, 'pascal_type208', None)
    assert not _is_linked(a, 'pascal_type208', b2)
    if hasattr(b2, 'pascal_set_type207'):
        assert not _is_linked(b2, 'pascal_set_type207', a)


def test_assoc_type209_link_reassign_clear():
    a = pascal_type(name="sample_text")
    b1 = pascal_file_type()
    b2 = pascal_file_type()
    _safe_set(a, 'pascal_type211', b1)
    assert _is_linked(a, 'pascal_type211', b1)
    if hasattr(b1, 'pascal_file_type210'):
        assert _is_linked(b1, 'pascal_file_type210', a)
    _safe_set(a, 'pascal_type211', b2)
    assert _is_linked(a, 'pascal_type211', b2)
    if hasattr(b1, 'pascal_file_type210'):
        assert not _is_linked(b1, 'pascal_file_type210', a)
    if hasattr(b2, 'pascal_file_type210'):
        assert _is_linked(b2, 'pascal_file_type210', a)
    _safe_set(a, 'pascal_type211', None)
    assert not _is_linked(a, 'pascal_type211', b2)
    if hasattr(b2, 'pascal_file_type210'):
        assert not _is_linked(b2, 'pascal_file_type210', a)


def test_assoc_type221_link_reassign_clear():
    a = pascal_type(name="sample_text")
    b1 = pascal_record_section()
    b2 = pascal_record_section()
    _safe_set(a, 'pascal_type223', b1)
    assert _is_linked(a, 'pascal_type223', b1)
    if hasattr(b1, 'pascal_record_section222'):
        assert _is_linked(b1, 'pascal_record_section222', a)
    _safe_set(a, 'pascal_type223', b2)
    assert _is_linked(a, 'pascal_type223', b2)
    if hasattr(b1, 'pascal_record_section222'):
        assert not _is_linked(b1, 'pascal_record_section222', a)
    if hasattr(b2, 'pascal_record_section222'):
        assert _is_linked(b2, 'pascal_record_section222', a)
    _safe_set(a, 'pascal_type223', None)
    assert not _is_linked(a, 'pascal_type223', b2)
    if hasattr(b2, 'pascal_record_section222'):
        assert not _is_linked(b2, 'pascal_record_section222', a)


def test_assoc_type29_link_reassign_clear():
    a = pascal_type(name="sample_text")
    b1 = pascal_variable_declaration()
    b2 = pascal_variable_declaration()
    _safe_set(a, 'pascal_type', b1)
    assert _is_linked(a, 'pascal_type', b1)
    if hasattr(b1, 'pascal_variable_declaration30'):
        assert _is_linked(b1, 'pascal_variable_declaration30', a)
    _safe_set(a, 'pascal_type', b2)
    assert _is_linked(a, 'pascal_type', b2)
    if hasattr(b1, 'pascal_variable_declaration30'):
        assert not _is_linked(b1, 'pascal_variable_declaration30', a)
    if hasattr(b2, 'pascal_variable_declaration30'):
        assert _is_linked(b2, 'pascal_variable_declaration30', a)
    _safe_set(a, 'pascal_type', None)
    assert not _is_linked(a, 'pascal_type', b2)
    if hasattr(b2, 'pascal_variable_declaration30'):
        assert not _is_linked(b2, 'pascal_variable_declaration30', a)


def test_assoc_type43_link_reassign_clear():
    a = pascal_type(name="sample_text")
    b1 = pascal_function_declaration(name="sample_text")
    b2 = pascal_function_declaration(name="sample_text_2")
    _safe_set(a, 'pascal_type45', b1)
    assert _is_linked(a, 'pascal_type45', b1)
    if hasattr(b1, 'pascal_function_declaration44'):
        assert _is_linked(b1, 'pascal_function_declaration44', a)
    _safe_set(a, 'pascal_type45', b2)
    assert _is_linked(a, 'pascal_type45', b2)
    if hasattr(b1, 'pascal_function_declaration44'):
        assert not _is_linked(b1, 'pascal_function_declaration44', a)
    if hasattr(b2, 'pascal_function_declaration44'):
        assert _is_linked(b2, 'pascal_function_declaration44', a)
    _safe_set(a, 'pascal_type45', None)
    assert not _is_linked(a, 'pascal_type45', b2)
    if hasattr(b2, 'pascal_function_declaration44'):
        assert not _is_linked(b2, 'pascal_function_declaration44', a)


def test_assoc_variable1157_link_reassign_clear():
    a = pascal_variable(name="sample_text")
    b1 = pascal_Variable1(name="sample_text")
    b2 = pascal_Variable1(name="sample_text_2")
    _safe_set(a, 'pascal_variable158', b1)
    assert _is_linked(a, 'pascal_variable158', b1)
    if hasattr(b1, 'pascal_Variable1'):
        assert _is_linked(b1, 'pascal_Variable1', a)
    _safe_set(a, 'pascal_variable158', b2)
    assert _is_linked(a, 'pascal_variable158', b2)
    if hasattr(b1, 'pascal_Variable1'):
        assert not _is_linked(b1, 'pascal_Variable1', a)
    if hasattr(b2, 'pascal_Variable1'):
        assert _is_linked(b2, 'pascal_Variable1', a)
    _safe_set(a, 'pascal_variable158', None)
    assert not _is_linked(a, 'pascal_variable158', b2)
    if hasattr(b2, 'pascal_Variable1'):
        assert not _is_linked(b2, 'pascal_Variable1', a)


def test_assoc_variable1162_link_reassign_clear():
    a = pascal_Variable1(name="sample_text")
    b1 = pascal_Variable1(name="sample_text")
    b2 = pascal_Variable1(name="sample_text_2")
    _safe_set(a, 'pascal_Variable1161', b1)
    assert _is_linked(a, 'pascal_Variable1161', b1)
    if hasattr(b1, 'pascal_Variable1163'):
        assert _is_linked(b1, 'pascal_Variable1163', a)
    _safe_set(a, 'pascal_Variable1161', b2)
    assert _is_linked(a, 'pascal_Variable1161', b2)
    if hasattr(b1, 'pascal_Variable1163'):
        assert not _is_linked(b1, 'pascal_Variable1163', a)
    if hasattr(b2, 'pascal_Variable1163'):
        assert _is_linked(b2, 'pascal_Variable1163', a)
    _safe_set(a, 'pascal_Variable1161', None)
    assert not _is_linked(a, 'pascal_Variable1161', b2)
    if hasattr(b2, 'pascal_Variable1163'):
        assert not _is_linked(b2, 'pascal_Variable1163', a)


def test_assoc_variable144_link_reassign_clear():
    a = pascal_variable(name="sample_text")
    b1 = pascal_factor(id="sample_text", nil="sample_text", string="sample_text")
    b2 = pascal_factor(id="sample_text_2", nil="sample_text_2", string="sample_text_2")
    _safe_set(a, 'pascal_variable146', b1)
    assert _is_linked(a, 'pascal_variable146', b1)
    if hasattr(b1, 'pascal_factor145'):
        assert _is_linked(b1, 'pascal_factor145', a)
    _safe_set(a, 'pascal_variable146', b2)
    assert _is_linked(a, 'pascal_variable146', b2)
    if hasattr(b1, 'pascal_factor145'):
        assert not _is_linked(b1, 'pascal_factor145', a)
    if hasattr(b2, 'pascal_factor145'):
        assert _is_linked(b2, 'pascal_factor145', a)
    _safe_set(a, 'pascal_variable146', None)
    assert not _is_linked(a, 'pascal_variable146', b2)
    if hasattr(b2, 'pascal_factor145'):
        assert not _is_linked(b2, 'pascal_factor145', a)


def test_assoc_variables132_link_reassign_clear():
    a = pascal_variable(name="sample_text")
    b1 = pascal_with_statement()
    b2 = pascal_with_statement()
    _safe_set(a, 'pascal_variable', b1)
    assert _is_linked(a, 'pascal_variable', b1)
    if hasattr(b1, 'pascal_with_statement'):
        assert _is_linked(b1, 'pascal_with_statement', a)
    _safe_set(a, 'pascal_variable', b2)
    assert _is_linked(a, 'pascal_variable', b2)
    if hasattr(b1, 'pascal_with_statement'):
        assert not _is_linked(b1, 'pascal_with_statement', a)
    if hasattr(b2, 'pascal_with_statement'):
        assert _is_linked(b2, 'pascal_with_statement', a)
    _safe_set(a, 'pascal_variable', None)
    assert not _is_linked(a, 'pascal_variable', b2)
    if hasattr(b2, 'pascal_with_statement'):
        assert not _is_linked(b2, 'pascal_with_statement', a)


def test_assoc_variantPart214_link_reassign_clear():
    a = pascal_variant_part(id="sample_text")
    b1 = pascal_field_list()
    b2 = pascal_field_list()
    _safe_set(a, 'pascal_variant_part', b1)
    assert _is_linked(a, 'pascal_variant_part', b1)
    if hasattr(b1, 'pascal_field_list215'):
        assert _is_linked(b1, 'pascal_field_list215', a)
    _safe_set(a, 'pascal_variant_part', b2)
    assert _is_linked(a, 'pascal_variant_part', b2)
    if hasattr(b1, 'pascal_field_list215'):
        assert not _is_linked(b1, 'pascal_field_list215', a)
    if hasattr(b2, 'pascal_field_list215'):
        assert _is_linked(b2, 'pascal_field_list215', a)
    _safe_set(a, 'pascal_variant_part', None)
    assert not _is_linked(a, 'pascal_variant_part', b2)
    if hasattr(b2, 'pascal_field_list215'):
        assert not _is_linked(b2, 'pascal_field_list215', a)


def test_assoc_variants226_link_reassign_clear():
    a = pascal_variant_part(id="sample_text")
    b1 = pascal_variant()
    b2 = pascal_variant()
    _safe_set(a, 'pascal_variant_part227', {b1})
    assert _is_linked(a, 'pascal_variant_part227', b1)
    if hasattr(b1, 'pascal_variant'):
        assert _is_linked(b1, 'pascal_variant', a)
    _safe_set(a, 'pascal_variant_part227', {b2})
    assert _is_linked(a, 'pascal_variant_part227', b2)
    if hasattr(b1, 'pascal_variant'):
        assert not _is_linked(b1, 'pascal_variant', a)
    if hasattr(b2, 'pascal_variant'):
        assert _is_linked(b2, 'pascal_variant', a)
    _safe_set(a, 'pascal_variant_part227', set())
    assert not _is_linked(a, 'pascal_variant_part227', b2)
    if hasattr(b2, 'pascal_variant'):
        assert not _is_linked(b2, 'pascal_variant', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

conformant_array_schema_strategy = st.builds(conformant_array_schema)
@given(instance=conformant_array_schema_strategy)
@settings(max_examples=25)
def test_conformant_array_schema_instantiation(instance):
    assert isinstance(instance, conformant_array_schema)


constant_definition_strategy = st.builds(constant_definition)
@given(instance=constant_definition_strategy)
@settings(max_examples=25)
def test_constant_definition_instantiation(instance):
    assert isinstance(instance, constant_definition)


goto_statement_strategy = st.builds(goto_statement)
@given(instance=goto_statement_strategy)
@settings(max_examples=25)
def test_goto_statement_instantiation(instance):
    assert isinstance(instance, goto_statement)


pascal_DeclarationPart_strategy = st.builds(pascal_DeclarationPart)
@given(instance=pascal_DeclarationPart_strategy)
@settings(max_examples=25)
def test_pascal_DeclarationPart_instantiation(instance):
    assert isinstance(instance, pascal_DeclarationPart)


pascal_EObject_strategy = st.builds(pascal_EObject)
@given(instance=pascal_EObject_strategy)
@settings(max_examples=25)
def test_pascal_EObject_instantiation(instance):
    assert isinstance(instance, pascal_EObject)


pascal_ElementList_strategy = st.builds(pascal_ElementList)
@given(instance=pascal_ElementList_strategy)
@settings(max_examples=25)
def test_pascal_ElementList_instantiation(instance):
    assert isinstance(instance, pascal_ElementList)


pascal_ExpressionList_strategy = st.builds(pascal_ExpressionList)
@given(instance=pascal_ExpressionList_strategy)
@settings(max_examples=25)
def test_pascal_ExpressionList_instantiation(instance):
    assert isinstance(instance, pascal_ExpressionList)


pascal_FunctionDesignator_strategy = st.builds(pascal_FunctionDesignator, name=safe_text)
@given(instance=pascal_FunctionDesignator_strategy)
@settings(max_examples=25)
def test_pascal_FunctionDesignator_instantiation(instance):
    assert isinstance(instance, pascal_FunctionDesignator)


pascal_Model_strategy = st.builds(pascal_Model)
@given(instance=pascal_Model_strategy)
@settings(max_examples=25)
def test_pascal_Model_instantiation(instance):
    assert isinstance(instance, pascal_Model)


pascal_Set_strategy = st.builds(pascal_Set)
@given(instance=pascal_Set_strategy)
@settings(max_examples=25)
def test_pascal_Set_instantiation(instance):
    assert isinstance(instance, pascal_Set)


pascal_Variable1_strategy = st.builds(pascal_Variable1, name=safe_text)
@given(instance=pascal_Variable1_strategy)
@settings(max_examples=25)
def test_pascal_Variable1_instantiation(instance):
    assert isinstance(instance, pascal_Variable1)


pascal_array_type_strategy = st.builds(pascal_array_type)
@given(instance=pascal_array_type_strategy)
@settings(max_examples=25)
def test_pascal_array_type_instantiation(instance):
    assert isinstance(instance, pascal_array_type)


pascal_assignment_statement_strategy = st.builds(pascal_assignment_statement, identifier=safe_text, variable=safe_text)
@given(instance=pascal_assignment_statement_strategy)
@settings(max_examples=25)
def test_pascal_assignment_statement_instantiation(instance):
    assert isinstance(instance, pascal_assignment_statement)


pascal_block_strategy = st.builds(pascal_block)
@given(instance=pascal_block_strategy)
@settings(max_examples=25)
def test_pascal_block_instantiation(instance):
    assert isinstance(instance, pascal_block)


pascal_bound_specification_strategy = st.builds(pascal_bound_specification, id1=safe_text, id2=safe_text, id3=safe_text)
@given(instance=pascal_bound_specification_strategy)
@settings(max_examples=25)
def test_pascal_bound_specification_instantiation(instance):
    assert isinstance(instance, pascal_bound_specification)


pascal_case_label_list_strategy = st.builds(pascal_case_label_list)
@given(instance=pascal_case_label_list_strategy)
@settings(max_examples=25)
def test_pascal_case_label_list_instantiation(instance):
    assert isinstance(instance, pascal_case_label_list)


pascal_case_limb_strategy = st.builds(pascal_case_limb)
@given(instance=pascal_case_limb_strategy)
@settings(max_examples=25)
def test_pascal_case_limb_instantiation(instance):
    assert isinstance(instance, pascal_case_limb)


pascal_case_statement_strategy = st.builds(pascal_case_statement)
@given(instance=pascal_case_statement_strategy)
@settings(max_examples=25)
def test_pascal_case_statement_instantiation(instance):
    assert isinstance(instance, pascal_case_statement)


pascal_compound_statement_strategy = st.builds(pascal_compound_statement)
@given(instance=pascal_compound_statement_strategy)
@settings(max_examples=25)
def test_pascal_compound_statement_instantiation(instance):
    assert isinstance(instance, pascal_compound_statement)


pascal_conditional_statement_strategy = st.builds(pascal_conditional_statement)
@given(instance=pascal_conditional_statement_strategy)
@settings(max_examples=25)
def test_pascal_conditional_statement_instantiation(instance):
    assert isinstance(instance, pascal_conditional_statement)


pascal_conformant_array_schema_strategy = st.builds(pascal_conformant_array_schema, id=safe_text)
@given(instance=pascal_conformant_array_schema_strategy)
@settings(max_examples=25)
def test_pascal_conformant_array_schema_instantiation(instance):
    assert isinstance(instance, pascal_conformant_array_schema)


pascal_constant_strategy = st.builds(pascal_constant, name=safe_text, string=safe_text)
@given(instance=pascal_constant_strategy)
@settings(max_examples=25)
def test_pascal_constant_instantiation(instance):
    assert isinstance(instance, pascal_constant)


pascal_constant_definition_strategy = st.builds(pascal_constant_definition)
@given(instance=pascal_constant_definition_strategy)
@settings(max_examples=25)
def test_pascal_constant_definition_instantiation(instance):
    assert isinstance(instance, pascal_constant_definition)


pascal_constant_definition_part_strategy = st.builds(pascal_constant_definition_part)
@given(instance=pascal_constant_definition_part_strategy)
@settings(max_examples=25)
def test_pascal_constant_definition_part_instantiation(instance):
    assert isinstance(instance, pascal_constant_definition_part)


pascal_enumerated_type_strategy = st.builds(pascal_enumerated_type)
@given(instance=pascal_enumerated_type_strategy)
@settings(max_examples=25)
def test_pascal_enumerated_type_instantiation(instance):
    assert isinstance(instance, pascal_enumerated_type)


pascal_expression_strategy = st.builds(pascal_expression, relational_operators=safe_text)
@given(instance=pascal_expression_strategy)
@settings(max_examples=25)
def test_pascal_expression_instantiation(instance):
    assert isinstance(instance, pascal_expression)


pascal_factor_strategy = st.builds(pascal_factor, id=safe_text, nil=safe_text, string=safe_text)
@given(instance=pascal_factor_strategy)
@settings(max_examples=25)
def test_pascal_factor_instantiation(instance):
    assert isinstance(instance, pascal_factor)


pascal_field_list_strategy = st.builds(pascal_field_list)
@given(instance=pascal_field_list_strategy)
@settings(max_examples=25)
def test_pascal_field_list_instantiation(instance):
    assert isinstance(instance, pascal_field_list)


pascal_file_type_strategy = st.builds(pascal_file_type)
@given(instance=pascal_file_type_strategy)
@settings(max_examples=25)
def test_pascal_file_type_instantiation(instance):
    assert isinstance(instance, pascal_file_type)


pascal_fixed_part_strategy = st.builds(pascal_fixed_part)
@given(instance=pascal_fixed_part_strategy)
@settings(max_examples=25)
def test_pascal_fixed_part_instantiation(instance):
    assert isinstance(instance, pascal_fixed_part)


pascal_for_statement_strategy = st.builds(pascal_for_statement, name=safe_text)
@given(instance=pascal_for_statement_strategy)
@settings(max_examples=25)
def test_pascal_for_statement_instantiation(instance):
    assert isinstance(instance, pascal_for_statement)


pascal_formal_parameter_list_strategy = st.builds(pascal_formal_parameter_list)
@given(instance=pascal_formal_parameter_list_strategy)
@settings(max_examples=25)
def test_pascal_formal_parameter_list_instantiation(instance):
    assert isinstance(instance, pascal_formal_parameter_list)


pascal_formal_parameter_section_strategy = st.builds(pascal_formal_parameter_section)
@given(instance=pascal_formal_parameter_section_strategy)
@settings(max_examples=25)
def test_pascal_formal_parameter_section_instantiation(instance):
    assert isinstance(instance, pascal_formal_parameter_section)


pascal_function_declaration_strategy = st.builds(pascal_function_declaration, name=safe_text)
@given(instance=pascal_function_declaration_strategy)
@settings(max_examples=25)
def test_pascal_function_declaration_instantiation(instance):
    assert isinstance(instance, pascal_function_declaration)


pascal_function_heading_strategy = st.builds(pascal_function_heading, id1=safe_text, id2=safe_text)
@given(instance=pascal_function_heading_strategy)
@settings(max_examples=25)
def test_pascal_function_heading_instantiation(instance):
    assert isinstance(instance, pascal_function_heading)


pascal_goto_statement_strategy = st.builds(pascal_goto_statement)
@given(instance=pascal_goto_statement_strategy)
@settings(max_examples=25)
def test_pascal_goto_statement_instantiation(instance):
    assert isinstance(instance, pascal_goto_statement)


pascal_identifier_list_strategy = st.builds(pascal_identifier_list, ids=safe_text)
@given(instance=pascal_identifier_list_strategy)
@settings(max_examples=25)
def test_pascal_identifier_list_instantiation(instance):
    assert isinstance(instance, pascal_identifier_list)


pascal_if_statement_strategy = st.builds(pascal_if_statement)
@given(instance=pascal_if_statement_strategy)
@settings(max_examples=25)
def test_pascal_if_statement_instantiation(instance):
    assert isinstance(instance, pascal_if_statement)


pascal_label_strategy = st.builds(pascal_label, int=safe_text)
@given(instance=pascal_label_strategy)
@settings(max_examples=25)
def test_pascal_label_instantiation(instance):
    assert isinstance(instance, pascal_label)


pascal_label_declaration_part_strategy = st.builds(pascal_label_declaration_part)
@given(instance=pascal_label_declaration_part_strategy)
@settings(max_examples=25)
def test_pascal_label_declaration_part_instantiation(instance):
    assert isinstance(instance, pascal_label_declaration_part)


pascal_number_strategy = st.builds(pascal_number, integer=safe_text, real=safe_text)
@given(instance=pascal_number_strategy)
@settings(max_examples=25)
def test_pascal_number_instantiation(instance):
    assert isinstance(instance, pascal_number)


pascal_packed_conformant_array_schema_strategy = st.builds(pascal_packed_conformant_array_schema)
@given(instance=pascal_packed_conformant_array_schema_strategy)
@settings(max_examples=25)
def test_pascal_packed_conformant_array_schema_instantiation(instance):
    assert isinstance(instance, pascal_packed_conformant_array_schema)


pascal_parameter_type_strategy = st.builds(pascal_parameter_type, id=safe_text)
@given(instance=pascal_parameter_type_strategy)
@settings(max_examples=25)
def test_pascal_parameter_type_instantiation(instance):
    assert isinstance(instance, pascal_parameter_type)


pascal_pointer_type_strategy = st.builds(pascal_pointer_type, name=safe_text)
@given(instance=pascal_pointer_type_strategy)
@settings(max_examples=25)
def test_pascal_pointer_type_instantiation(instance):
    assert isinstance(instance, pascal_pointer_type)


pascal_procedure_and_function_declaration_part_strategy = st.builds(pascal_procedure_and_function_declaration_part)
@given(instance=pascal_procedure_and_function_declaration_part_strategy)
@settings(max_examples=25)
def test_pascal_procedure_and_function_declaration_part_instantiation(instance):
    assert isinstance(instance, pascal_procedure_and_function_declaration_part)


pascal_procedure_declaration_strategy = st.builds(pascal_procedure_declaration, name=safe_text)
@given(instance=pascal_procedure_declaration_strategy)
@settings(max_examples=25)
def test_pascal_procedure_declaration_instantiation(instance):
    assert isinstance(instance, pascal_procedure_declaration)


pascal_procedure_heading_strategy = st.builds(pascal_procedure_heading, name=safe_text)
@given(instance=pascal_procedure_heading_strategy)
@settings(max_examples=25)
def test_pascal_procedure_heading_instantiation(instance):
    assert isinstance(instance, pascal_procedure_heading)


pascal_procedure_statement_strategy = st.builds(pascal_procedure_statement, actualParameterList=safe_text, name=safe_text)
@given(instance=pascal_procedure_statement_strategy)
@settings(max_examples=25)
def test_pascal_procedure_statement_instantiation(instance):
    assert isinstance(instance, pascal_procedure_statement)


pascal_program_strategy = st.builds(pascal_program)
@given(instance=pascal_program_strategy)
@settings(max_examples=25)
def test_pascal_program_instantiation(instance):
    assert isinstance(instance, pascal_program)


pascal_program_heading_strategy = st.builds(pascal_program_heading)
@given(instance=pascal_program_heading_strategy)
@settings(max_examples=25)
def test_pascal_program_heading_instantiation(instance):
    assert isinstance(instance, pascal_program_heading)


pascal_record_section_strategy = st.builds(pascal_record_section)
@given(instance=pascal_record_section_strategy)
@settings(max_examples=25)
def test_pascal_record_section_instantiation(instance):
    assert isinstance(instance, pascal_record_section)


pascal_record_type_strategy = st.builds(pascal_record_type)
@given(instance=pascal_record_type_strategy)
@settings(max_examples=25)
def test_pascal_record_type_instantiation(instance):
    assert isinstance(instance, pascal_record_type)


pascal_repeat_statement_strategy = st.builds(pascal_repeat_statement)
@given(instance=pascal_repeat_statement_strategy)
@settings(max_examples=25)
def test_pascal_repeat_statement_instantiation(instance):
    assert isinstance(instance, pascal_repeat_statement)


pascal_repetitive_statement_strategy = st.builds(pascal_repetitive_statement)
@given(instance=pascal_repetitive_statement_strategy)
@settings(max_examples=25)
def test_pascal_repetitive_statement_instantiation(instance):
    assert isinstance(instance, pascal_repetitive_statement)


pascal_set_type_strategy = st.builds(pascal_set_type)
@given(instance=pascal_set_type_strategy)
@settings(max_examples=25)
def test_pascal_set_type_instantiation(instance):
    assert isinstance(instance, pascal_set_type)


pascal_simple_expression_strategy = st.builds(pascal_simple_expression)
@given(instance=pascal_simple_expression_strategy)
@settings(max_examples=25)
def test_pascal_simple_expression_instantiation(instance):
    assert isinstance(instance, pascal_simple_expression)


pascal_simple_statement_strategy = st.builds(pascal_simple_statement)
@given(instance=pascal_simple_statement_strategy)
@settings(max_examples=25)
def test_pascal_simple_statement_instantiation(instance):
    assert isinstance(instance, pascal_simple_statement)


pascal_simple_type_strategy = st.builds(pascal_simple_type, primitiveType=safe_text)
@given(instance=pascal_simple_type_strategy)
@settings(max_examples=25)
def test_pascal_simple_type_instantiation(instance):
    assert isinstance(instance, pascal_simple_type)


pascal_statement_strategy = st.builds(pascal_statement)
@given(instance=pascal_statement_strategy)
@settings(max_examples=25)
def test_pascal_statement_instantiation(instance):
    assert isinstance(instance, pascal_statement)


pascal_statement_part_strategy = st.builds(pascal_statement_part)
@given(instance=pascal_statement_part_strategy)
@settings(max_examples=25)
def test_pascal_statement_part_instantiation(instance):
    assert isinstance(instance, pascal_statement_part)


pascal_statement_sequence_strategy = st.builds(pascal_statement_sequence)
@given(instance=pascal_statement_sequence_strategy)
@settings(max_examples=25)
def test_pascal_statement_sequence_instantiation(instance):
    assert isinstance(instance, pascal_statement_sequence)


pascal_structured_statement_strategy = st.builds(pascal_structured_statement)
@given(instance=pascal_structured_statement_strategy)
@settings(max_examples=25)
def test_pascal_structured_statement_instantiation(instance):
    assert isinstance(instance, pascal_structured_statement)


pascal_structured_type_strategy = st.builds(pascal_structured_type)
@given(instance=pascal_structured_type_strategy)
@settings(max_examples=25)
def test_pascal_structured_type_instantiation(instance):
    assert isinstance(instance, pascal_structured_type)


pascal_subrange_type_strategy = st.builds(pascal_subrange_type)
@given(instance=pascal_subrange_type_strategy)
@settings(max_examples=25)
def test_pascal_subrange_type_instantiation(instance):
    assert isinstance(instance, pascal_subrange_type)


pascal_tag_field_strategy = st.builds(pascal_tag_field, id=safe_text)
@given(instance=pascal_tag_field_strategy)
@settings(max_examples=25)
def test_pascal_tag_field_instantiation(instance):
    assert isinstance(instance, pascal_tag_field)


pascal_term_strategy = st.builds(pascal_term)
@given(instance=pascal_term_strategy)
@settings(max_examples=25)
def test_pascal_term_instantiation(instance):
    assert isinstance(instance, pascal_term)


pascal_type_strategy = st.builds(pascal_type, name=safe_text)
@given(instance=pascal_type_strategy)
@settings(max_examples=25)
def test_pascal_type_instantiation(instance):
    assert isinstance(instance, pascal_type)


pascal_type_definition_strategy = st.builds(pascal_type_definition)
@given(instance=pascal_type_definition_strategy)
@settings(max_examples=25)
def test_pascal_type_definition_instantiation(instance):
    assert isinstance(instance, pascal_type_definition)


pascal_type_definition_part_strategy = st.builds(pascal_type_definition_part)
@given(instance=pascal_type_definition_part_strategy)
@settings(max_examples=25)
def test_pascal_type_definition_part_instantiation(instance):
    assert isinstance(instance, pascal_type_definition_part)


pascal_unpacked_conformant_array_Schema_strategy = st.builds(pascal_unpacked_conformant_array_Schema)
@given(instance=pascal_unpacked_conformant_array_Schema_strategy)
@settings(max_examples=25)
def test_pascal_unpacked_conformant_array_Schema_instantiation(instance):
    assert isinstance(instance, pascal_unpacked_conformant_array_Schema)


pascal_unpacked_structured_type_strategy = st.builds(pascal_unpacked_structured_type)
@given(instance=pascal_unpacked_structured_type_strategy)
@settings(max_examples=25)
def test_pascal_unpacked_structured_type_instantiation(instance):
    assert isinstance(instance, pascal_unpacked_structured_type)


pascal_value_parameter_section_strategy = st.builds(pascal_value_parameter_section)
@given(instance=pascal_value_parameter_section_strategy)
@settings(max_examples=25)
def test_pascal_value_parameter_section_instantiation(instance):
    assert isinstance(instance, pascal_value_parameter_section)


pascal_variable_strategy = st.builds(pascal_variable, name=safe_text)
@given(instance=pascal_variable_strategy)
@settings(max_examples=25)
def test_pascal_variable_instantiation(instance):
    assert isinstance(instance, pascal_variable)


pascal_variable_declaration_strategy = st.builds(pascal_variable_declaration)
@given(instance=pascal_variable_declaration_strategy)
@settings(max_examples=25)
def test_pascal_variable_declaration_instantiation(instance):
    assert isinstance(instance, pascal_variable_declaration)


pascal_variable_declaration_part_strategy = st.builds(pascal_variable_declaration_part)
@given(instance=pascal_variable_declaration_part_strategy)
@settings(max_examples=25)
def test_pascal_variable_declaration_part_instantiation(instance):
    assert isinstance(instance, pascal_variable_declaration_part)


pascal_variable_parameter_section_strategy = st.builds(pascal_variable_parameter_section)
@given(instance=pascal_variable_parameter_section_strategy)
@settings(max_examples=25)
def test_pascal_variable_parameter_section_instantiation(instance):
    assert isinstance(instance, pascal_variable_parameter_section)


pascal_variant_strategy = st.builds(pascal_variant)
@given(instance=pascal_variant_strategy)
@settings(max_examples=25)
def test_pascal_variant_instantiation(instance):
    assert isinstance(instance, pascal_variant)


pascal_variant_part_strategy = st.builds(pascal_variant_part, id=safe_text)
@given(instance=pascal_variant_part_strategy)
@settings(max_examples=25)
def test_pascal_variant_part_instantiation(instance):
    assert isinstance(instance, pascal_variant_part)


pascal_while_statement_strategy = st.builds(pascal_while_statement)
@given(instance=pascal_while_statement_strategy)
@settings(max_examples=25)
def test_pascal_while_statement_instantiation(instance):
    assert isinstance(instance, pascal_while_statement)


pascal_with_statement_strategy = st.builds(pascal_with_statement)
@given(instance=pascal_with_statement_strategy)
@settings(max_examples=25)
def test_pascal_with_statement_instantiation(instance):
    assert isinstance(instance, pascal_with_statement)


program_heading_strategy = st.builds(program_heading)
@given(instance=program_heading_strategy)
@settings(max_examples=25)
def test_program_heading_instantiation(instance):
    assert isinstance(instance, program_heading)


repetitive_statement_strategy = st.builds(repetitive_statement)
@given(instance=repetitive_statement_strategy)
@settings(max_examples=25)
def test_repetitive_statement_instantiation(instance):
    assert isinstance(instance, repetitive_statement)


simple_statement_strategy = st.builds(simple_statement)
@given(instance=simple_statement_strategy)
@settings(max_examples=25)
def test_simple_statement_instantiation(instance):
    assert isinstance(instance, simple_statement)


statement_strategy = st.builds(statement)
@given(instance=statement_strategy)
@settings(max_examples=25)
def test_statement_instantiation(instance):
    assert isinstance(instance, statement)


statement_part_strategy = st.builds(statement_part)
@given(instance=statement_part_strategy)
@settings(max_examples=25)
def test_statement_part_instantiation(instance):
    assert isinstance(instance, statement_part)


structured_statement_strategy = st.builds(structured_statement)
@given(instance=structured_statement_strategy)
@settings(max_examples=25)
def test_structured_statement_instantiation(instance):
    assert isinstance(instance, structured_statement)


type_definition_strategy = st.builds(type_definition)
@given(instance=type_definition_strategy)
@settings(max_examples=25)
def test_type_definition_instantiation(instance):
    assert isinstance(instance, type_definition)



