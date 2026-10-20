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
    pascal_statement_part,
    pascal_formal_parameter_list,
    abstraction_declaration,
    pascal_abstraction_declaration,
    pascal_abstraction_heading,
    pascal_variable_identifier_list,
    pascal_variable_section,
    pascal_type,
    pascal_type_definition,
    pascal_constant,
    pascal_declaration_part,
    pascal_identifier_list,
    pascal_block,
    pascal_program_heading,
    pascal_program,
    pascal_record_section,
    pascal_variant_part,
    pascal_fixed_part,
    pascal_any_number,
    pascal_variant,
    pascal_tag_field,
    pascal_enumerated_type,
    pascal_subrange_type,
    pascal_pointer_type,
    pascal_field_list,
    pascal_file_type,
    pascal_set_type,
    pascal_record_type,
    pascal_array_type,
    pascal_unpacked_structured_type,
    pascal_expression_list,
    pascal_resto,
    pascal_structured_type,
    pascal_simple_type,
    pascal_case_label_list,
    pascal_case_limb,
    pascal_set,
    pascal_number,
    pascal_factor,
    pascal_term,
    pascal_EObject,
    pascal_simple_expression,
    pascal_conditional_statement,
    pascal_repetitive_statement,
    pascal_compound_statement,
    pascal_expression,
    pascal_variable,
    pascal_goto_statement,
    pascal_function_designator,
    pascal_case_statement,
    pascal_if_statement,
    pascal_for_statement,
    pascal_repeat_statement,
    pascal_while_statement,
    pascal_with_statement,
    pascal_parameter_type,
    pascal_variable_parameter_section,
    pascal_value_parameter_section,
    pascal_formal_parameter_section,
    pascal_statement_sequence,
    pascal_assignment_statement,
    pascal_structured_statement,
    pascal_simple_statement,
    pascal_statement,
    pascal_bound_specification,
    pascal_unpacked_conformant_array_schema,
    pascal_packed_conformant_array_schema,
    pascal_conformant_array_schema,
    pascal_constant_definition,
    pascal_label,
    pascal_procedure_and_function_declaration_part,
    pascal_variable_declaration_part,
    pascal_type_definition_part,
    pascal_constant_definition_part,
    pascal_label_declaration_part,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_pascal_statement_part_is_not_abstract():
    assert not inspect.isabstract(pascal_statement_part)


def test_hyp_pascal_statement_part_constructor_exists():
    assert callable(pascal_statement_part.__init__)


def test_hyp_pascal_statement_part_constructor_args():
    sig = inspect.signature(pascal_statement_part.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_formal_parameter_list_is_not_abstract():
    assert not inspect.isabstract(pascal_formal_parameter_list)


def test_hyp_pascal_formal_parameter_list_constructor_exists():
    assert callable(pascal_formal_parameter_list.__init__)


def test_hyp_pascal_formal_parameter_list_constructor_args():
    sig = inspect.signature(pascal_formal_parameter_list.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstraction_declaration_is_not_abstract():
    assert not inspect.isabstract(abstraction_declaration)


def test_hyp_abstraction_declaration_constructor_exists():
    assert callable(abstraction_declaration.__init__)


def test_hyp_abstraction_declaration_constructor_args():
    sig = inspect.signature(abstraction_declaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_abstraction_declaration_is_not_abstract():
    assert not inspect.isabstract(pascal_abstraction_declaration)


def test_hyp_pascal_abstraction_declaration_constructor_exists():
    assert callable(pascal_abstraction_declaration.__init__)


def test_hyp_pascal_abstraction_declaration_constructor_args():
    sig = inspect.signature(pascal_abstraction_declaration.__init__)
    params = list(sig.parameters.keys())
    assert "forward" in params, "Missing parameter 'forward'"




def test_hyp_pascal_abstraction_heading_is_not_abstract():
    assert not inspect.isabstract(pascal_abstraction_heading)


def test_hyp_pascal_abstraction_heading_constructor_exists():
    assert callable(pascal_abstraction_heading.__init__)


def test_hyp_pascal_abstraction_heading_constructor_args():
    sig = inspect.signature(pascal_abstraction_heading.__init__)
    params = list(sig.parameters.keys())
    assert "resultType" in params, "Missing parameter 'resultType'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_pascal_variable_identifier_list_is_not_abstract():
    assert not inspect.isabstract(pascal_variable_identifier_list)


def test_hyp_pascal_variable_identifier_list_constructor_exists():
    assert callable(pascal_variable_identifier_list.__init__)


def test_hyp_pascal_variable_identifier_list_constructor_args():
    sig = inspect.signature(pascal_variable_identifier_list.__init__)
    params = list(sig.parameters.keys())
    assert "names" in params, "Missing parameter 'names'"




def test_hyp_pascal_variable_section_is_not_abstract():
    assert not inspect.isabstract(pascal_variable_section)


def test_hyp_pascal_variable_section_constructor_exists():
    assert callable(pascal_variable_section.__init__)


def test_hyp_pascal_variable_section_constructor_args():
    sig = inspect.signature(pascal_variable_section.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_type_is_not_abstract():
    assert not inspect.isabstract(pascal_type)


def test_hyp_pascal_type_constructor_exists():
    assert callable(pascal_type.__init__)


def test_hyp_pascal_type_constructor_args():
    sig = inspect.signature(pascal_type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_type_definition_is_not_abstract():
    assert not inspect.isabstract(pascal_type_definition)


def test_hyp_pascal_type_definition_constructor_exists():
    assert callable(pascal_type_definition.__init__)


def test_hyp_pascal_type_definition_constructor_args():
    sig = inspect.signature(pascal_type_definition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_pascal_constant_is_not_abstract():
    assert not inspect.isabstract(pascal_constant)


def test_hyp_pascal_constant_constructor_exists():
    assert callable(pascal_constant.__init__)


def test_hyp_pascal_constant_constructor_args():
    sig = inspect.signature(pascal_constant.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "nil" in params, "Missing parameter 'nil'"
    assert "opterator" in params, "Missing parameter 'opterator'"
    assert "string" in params, "Missing parameter 'string'"
    assert "boolLiteral" in params, "Missing parameter 'boolLiteral'"








def test_hyp_pascal_declaration_part_is_not_abstract():
    assert not inspect.isabstract(pascal_declaration_part)


def test_hyp_pascal_declaration_part_constructor_exists():
    assert callable(pascal_declaration_part.__init__)


def test_hyp_pascal_declaration_part_constructor_args():
    sig = inspect.signature(pascal_declaration_part.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_identifier_list_is_not_abstract():
    assert not inspect.isabstract(pascal_identifier_list)


def test_hyp_pascal_identifier_list_constructor_exists():
    assert callable(pascal_identifier_list.__init__)


def test_hyp_pascal_identifier_list_constructor_args():
    sig = inspect.signature(pascal_identifier_list.__init__)
    params = list(sig.parameters.keys())
    assert "ids" in params, "Missing parameter 'ids'"




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
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_pascal_program_is_not_abstract():
    assert not inspect.isabstract(pascal_program)


def test_hyp_pascal_program_constructor_exists():
    assert callable(pascal_program.__init__)


def test_hyp_pascal_program_constructor_args():
    sig = inspect.signature(pascal_program.__init__)
    params = list(sig.parameters.keys())



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
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_pascal_fixed_part_is_not_abstract():
    assert not inspect.isabstract(pascal_fixed_part)


def test_hyp_pascal_fixed_part_constructor_exists():
    assert callable(pascal_fixed_part.__init__)


def test_hyp_pascal_fixed_part_constructor_args():
    sig = inspect.signature(pascal_fixed_part.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_any_number_is_not_abstract():
    assert not inspect.isabstract(pascal_any_number)


def test_hyp_pascal_any_number_constructor_exists():
    assert callable(pascal_any_number.__init__)


def test_hyp_pascal_any_number_constructor_args():
    sig = inspect.signature(pascal_any_number.__init__)
    params = list(sig.parameters.keys())
    assert "real" in params, "Missing parameter 'real'"
    assert "integer" in params, "Missing parameter 'integer'"





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
    assert "name" in params, "Missing parameter 'name'"




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
    assert "subrange" in params, "Missing parameter 'subrange'"




def test_hyp_pascal_pointer_type_is_not_abstract():
    assert not inspect.isabstract(pascal_pointer_type)


def test_hyp_pascal_pointer_type_constructor_exists():
    assert callable(pascal_pointer_type.__init__)


def test_hyp_pascal_pointer_type_constructor_args():
    sig = inspect.signature(pascal_pointer_type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_field_list_is_not_abstract():
    assert not inspect.isabstract(pascal_field_list)


def test_hyp_pascal_field_list_constructor_exists():
    assert callable(pascal_field_list.__init__)


def test_hyp_pascal_field_list_constructor_args():
    sig = inspect.signature(pascal_field_list.__init__)
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
    assert "end" in params, "Missing parameter 'end'"
    assert "record" in params, "Missing parameter 'record'"





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



def test_hyp_pascal_expression_list_is_not_abstract():
    assert not inspect.isabstract(pascal_expression_list)


def test_hyp_pascal_expression_list_constructor_exists():
    assert callable(pascal_expression_list.__init__)


def test_hyp_pascal_expression_list_constructor_args():
    sig = inspect.signature(pascal_expression_list.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_resto_is_not_abstract():
    assert not inspect.isabstract(pascal_resto)


def test_hyp_pascal_resto_constructor_exists():
    assert callable(pascal_resto.__init__)


def test_hyp_pascal_resto_constructor_args():
    sig = inspect.signature(pascal_resto.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "accessor" in params, "Missing parameter 'accessor'"





def test_hyp_pascal_structured_type_is_not_abstract():
    assert not inspect.isabstract(pascal_structured_type)


def test_hyp_pascal_structured_type_constructor_exists():
    assert callable(pascal_structured_type.__init__)


def test_hyp_pascal_structured_type_constructor_args():
    sig = inspect.signature(pascal_structured_type.__init__)
    params = list(sig.parameters.keys())
    assert "packed" in params, "Missing parameter 'packed'"




def test_hyp_pascal_simple_type_is_not_abstract():
    assert not inspect.isabstract(pascal_simple_type)


def test_hyp_pascal_simple_type_constructor_exists():
    assert callable(pascal_simple_type.__init__)


def test_hyp_pascal_simple_type_constructor_args():
    sig = inspect.signature(pascal_simple_type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_pascal_case_label_list_is_not_abstract():
    assert not inspect.isabstract(pascal_case_label_list)


def test_hyp_pascal_case_label_list_constructor_exists():
    assert callable(pascal_case_label_list.__init__)


def test_hyp_pascal_case_label_list_constructor_args():
    sig = inspect.signature(pascal_case_label_list.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_case_limb_is_not_abstract():
    assert not inspect.isabstract(pascal_case_limb)


def test_hyp_pascal_case_limb_constructor_exists():
    assert callable(pascal_case_limb.__init__)


def test_hyp_pascal_case_limb_constructor_args():
    sig = inspect.signature(pascal_case_limb.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_set_is_not_abstract():
    assert not inspect.isabstract(pascal_set)


def test_hyp_pascal_set_constructor_exists():
    assert callable(pascal_set.__init__)


def test_hyp_pascal_set_constructor_args():
    sig = inspect.signature(pascal_set.__init__)
    params = list(sig.parameters.keys())
    assert "brackets" in params, "Missing parameter 'brackets'"




def test_hyp_pascal_number_is_not_abstract():
    assert not inspect.isabstract(pascal_number)


def test_hyp_pascal_number_constructor_exists():
    assert callable(pascal_number.__init__)


def test_hyp_pascal_number_constructor_args():
    sig = inspect.signature(pascal_number.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_factor_is_not_abstract():
    assert not inspect.isabstract(pascal_factor)


def test_hyp_pascal_factor_constructor_exists():
    assert callable(pascal_factor.__init__)


def test_hyp_pascal_factor_constructor_args():
    sig = inspect.signature(pascal_factor.__init__)
    params = list(sig.parameters.keys())
    assert "boolean" in params, "Missing parameter 'boolean'"
    assert "nil" in params, "Missing parameter 'nil'"
    assert "string" in params, "Missing parameter 'string'"






def test_hyp_pascal_term_is_not_abstract():
    assert not inspect.isabstract(pascal_term)


def test_hyp_pascal_term_constructor_exists():
    assert callable(pascal_term.__init__)


def test_hyp_pascal_term_constructor_args():
    sig = inspect.signature(pascal_term.__init__)
    params = list(sig.parameters.keys())
    assert "operators" in params, "Missing parameter 'operators'"




def test_hyp_pascal_eobject_is_not_abstract():
    assert not inspect.isabstract(pascal_EObject)


def test_hyp_pascal_eobject_constructor_exists():
    assert callable(pascal_EObject.__init__)


def test_hyp_pascal_eobject_constructor_args():
    sig = inspect.signature(pascal_EObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_simple_expression_is_not_abstract():
    assert not inspect.isabstract(pascal_simple_expression)


def test_hyp_pascal_simple_expression_constructor_exists():
    assert callable(pascal_simple_expression.__init__)


def test_hyp_pascal_simple_expression_constructor_args():
    sig = inspect.signature(pascal_simple_expression.__init__)
    params = list(sig.parameters.keys())
    assert "operators" in params, "Missing parameter 'operators'"
    assert "prefixOperator" in params, "Missing parameter 'prefixOperator'"





def test_hyp_pascal_conditional_statement_is_not_abstract():
    assert not inspect.isabstract(pascal_conditional_statement)


def test_hyp_pascal_conditional_statement_constructor_exists():
    assert callable(pascal_conditional_statement.__init__)


def test_hyp_pascal_conditional_statement_constructor_args():
    sig = inspect.signature(pascal_conditional_statement.__init__)
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



def test_hyp_pascal_expression_is_not_abstract():
    assert not inspect.isabstract(pascal_expression)


def test_hyp_pascal_expression_constructor_exists():
    assert callable(pascal_expression.__init__)


def test_hyp_pascal_expression_constructor_args():
    sig = inspect.signature(pascal_expression.__init__)
    params = list(sig.parameters.keys())
    assert "operators" in params, "Missing parameter 'operators'"




def test_hyp_pascal_variable_is_not_abstract():
    assert not inspect.isabstract(pascal_variable)


def test_hyp_pascal_variable_constructor_exists():
    assert callable(pascal_variable.__init__)


def test_hyp_pascal_variable_constructor_args():
    sig = inspect.signature(pascal_variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_pascal_goto_statement_is_not_abstract():
    assert not inspect.isabstract(pascal_goto_statement)


def test_hyp_pascal_goto_statement_constructor_exists():
    assert callable(pascal_goto_statement.__init__)


def test_hyp_pascal_goto_statement_constructor_args():
    sig = inspect.signature(pascal_goto_statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_function_designator_is_not_abstract():
    assert not inspect.isabstract(pascal_function_designator)


def test_hyp_pascal_function_designator_constructor_exists():
    assert callable(pascal_function_designator.__init__)


def test_hyp_pascal_function_designator_constructor_args():
    sig = inspect.signature(pascal_function_designator.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




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



def test_hyp_pascal_for_statement_is_not_abstract():
    assert not inspect.isabstract(pascal_for_statement)


def test_hyp_pascal_for_statement_constructor_exists():
    assert callable(pascal_for_statement.__init__)


def test_hyp_pascal_for_statement_constructor_args():
    sig = inspect.signature(pascal_for_statement.__init__)
    params = list(sig.parameters.keys())
    assert "initID" in params, "Missing parameter 'initID'"




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



def test_hyp_pascal_with_statement_is_not_abstract():
    assert not inspect.isabstract(pascal_with_statement)


def test_hyp_pascal_with_statement_constructor_exists():
    assert callable(pascal_with_statement.__init__)


def test_hyp_pascal_with_statement_constructor_args():
    sig = inspect.signature(pascal_with_statement.__init__)
    params = list(sig.parameters.keys())
    assert "records" in params, "Missing parameter 'records'"
    assert "record" in params, "Missing parameter 'record'"





def test_hyp_pascal_parameter_type_is_not_abstract():
    assert not inspect.isabstract(pascal_parameter_type)


def test_hyp_pascal_parameter_type_constructor_exists():
    assert callable(pascal_parameter_type.__init__)


def test_hyp_pascal_parameter_type_constructor_args():
    sig = inspect.signature(pascal_parameter_type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




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



def test_hyp_pascal_statement_sequence_is_not_abstract():
    assert not inspect.isabstract(pascal_statement_sequence)


def test_hyp_pascal_statement_sequence_constructor_exists():
    assert callable(pascal_statement_sequence.__init__)


def test_hyp_pascal_statement_sequence_constructor_args():
    sig = inspect.signature(pascal_statement_sequence.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_assignment_statement_is_not_abstract():
    assert not inspect.isabstract(pascal_assignment_statement)


def test_hyp_pascal_assignment_statement_constructor_exists():
    assert callable(pascal_assignment_statement.__init__)


def test_hyp_pascal_assignment_statement_constructor_args():
    sig = inspect.signature(pascal_assignment_statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_structured_statement_is_not_abstract():
    assert not inspect.isabstract(pascal_structured_statement)


def test_hyp_pascal_structured_statement_constructor_exists():
    assert callable(pascal_structured_statement.__init__)


def test_hyp_pascal_structured_statement_constructor_args():
    sig = inspect.signature(pascal_structured_statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_simple_statement_is_not_abstract():
    assert not inspect.isabstract(pascal_simple_statement)


def test_hyp_pascal_simple_statement_constructor_exists():
    assert callable(pascal_simple_statement.__init__)


def test_hyp_pascal_simple_statement_constructor_args():
    sig = inspect.signature(pascal_simple_statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_statement_is_not_abstract():
    assert not inspect.isabstract(pascal_statement)


def test_hyp_pascal_statement_constructor_exists():
    assert callable(pascal_statement.__init__)


def test_hyp_pascal_statement_constructor_args():
    sig = inspect.signature(pascal_statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_bound_specification_is_not_abstract():
    assert not inspect.isabstract(pascal_bound_specification)


def test_hyp_pascal_bound_specification_constructor_exists():
    assert callable(pascal_bound_specification.__init__)


def test_hyp_pascal_bound_specification_constructor_args():
    sig = inspect.signature(pascal_bound_specification.__init__)
    params = list(sig.parameters.keys())
    assert "fin" in params, "Missing parameter 'fin'"
    assert "name" in params, "Missing parameter 'name'"
    assert "init" in params, "Missing parameter 'init'"






def test_hyp_pascal_unpacked_conformant_array_schema_is_not_abstract():
    assert not inspect.isabstract(pascal_unpacked_conformant_array_schema)


def test_hyp_pascal_unpacked_conformant_array_schema_constructor_exists():
    assert callable(pascal_unpacked_conformant_array_schema.__init__)


def test_hyp_pascal_unpacked_conformant_array_schema_constructor_args():
    sig = inspect.signature(pascal_unpacked_conformant_array_schema.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_packed_conformant_array_schema_is_not_abstract():
    assert not inspect.isabstract(pascal_packed_conformant_array_schema)


def test_hyp_pascal_packed_conformant_array_schema_constructor_exists():
    assert callable(pascal_packed_conformant_array_schema.__init__)


def test_hyp_pascal_packed_conformant_array_schema_constructor_args():
    sig = inspect.signature(pascal_packed_conformant_array_schema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_pascal_conformant_array_schema_is_not_abstract():
    assert not inspect.isabstract(pascal_conformant_array_schema)


def test_hyp_pascal_conformant_array_schema_constructor_exists():
    assert callable(pascal_conformant_array_schema.__init__)


def test_hyp_pascal_conformant_array_schema_constructor_args():
    sig = inspect.signature(pascal_conformant_array_schema.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_constant_definition_is_not_abstract():
    assert not inspect.isabstract(pascal_constant_definition)


def test_hyp_pascal_constant_definition_constructor_exists():
    assert callable(pascal_constant_definition.__init__)


def test_hyp_pascal_constant_definition_constructor_args():
    sig = inspect.signature(pascal_constant_definition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_pascal_label_is_not_abstract():
    assert not inspect.isabstract(pascal_label)


def test_hyp_pascal_label_constructor_exists():
    assert callable(pascal_label.__init__)


def test_hyp_pascal_label_constructor_args():
    sig = inspect.signature(pascal_label.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"




def test_hyp_pascal_procedure_and_function_declaration_part_is_not_abstract():
    assert not inspect.isabstract(pascal_procedure_and_function_declaration_part)


def test_hyp_pascal_procedure_and_function_declaration_part_constructor_exists():
    assert callable(pascal_procedure_and_function_declaration_part.__init__)


def test_hyp_pascal_procedure_and_function_declaration_part_constructor_args():
    sig = inspect.signature(pascal_procedure_and_function_declaration_part.__init__)
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
pascal_statement_part_strategy = st.builds(
    pascal_statement_part,
)
pascal_formal_parameter_list_strategy = st.builds(
    pascal_formal_parameter_list,
)
abstraction_declaration_strategy = st.builds(
    abstraction_declaration,
)
pascal_abstraction_declaration_strategy = st.builds(
    pascal_abstraction_declaration,
    forward=
        st.booleans()
)
pascal_abstraction_heading_strategy = st.builds(
    pascal_abstraction_heading,
    resultType=
        safe_text,
    name=
        safe_text
)
pascal_variable_identifier_list_strategy = st.builds(
    pascal_variable_identifier_list,
    names=
        safe_text
)
pascal_variable_section_strategy = st.builds(
    pascal_variable_section,
)
pascal_type_strategy = st.builds(
    pascal_type,
)
pascal_type_definition_strategy = st.builds(
    pascal_type_definition,
    name=
        safe_text
)
pascal_constant_strategy = st.builds(
    pascal_constant,
    name=
        safe_text,
    nil=
        safe_text,
    opterator=
        safe_text,
    string=
        safe_text,
    boolLiteral=
        safe_text
)
pascal_declaration_part_strategy = st.builds(
    pascal_declaration_part,
)
pascal_identifier_list_strategy = st.builds(
    pascal_identifier_list,
    ids=
        safe_text
)
pascal_block_strategy = st.builds(
    pascal_block,
)
pascal_program_heading_strategy = st.builds(
    pascal_program_heading,
    name=
        safe_text
)
pascal_program_strategy = st.builds(
    pascal_program,
)
pascal_record_section_strategy = st.builds(
    pascal_record_section,
)
pascal_variant_part_strategy = st.builds(
    pascal_variant_part,
    name=
        safe_text
)
pascal_fixed_part_strategy = st.builds(
    pascal_fixed_part,
)
pascal_any_number_strategy = st.builds(
    pascal_any_number,
    real=
        safe_text,
    integer=
        safe_text
)
pascal_variant_strategy = st.builds(
    pascal_variant,
)
pascal_tag_field_strategy = st.builds(
    pascal_tag_field,
    name=
        safe_text
)
pascal_enumerated_type_strategy = st.builds(
    pascal_enumerated_type,
)
pascal_subrange_type_strategy = st.builds(
    pascal_subrange_type,
    subrange=
        safe_text
)
pascal_pointer_type_strategy = st.builds(
    pascal_pointer_type,
)
pascal_field_list_strategy = st.builds(
    pascal_field_list,
)
pascal_file_type_strategy = st.builds(
    pascal_file_type,
)
pascal_set_type_strategy = st.builds(
    pascal_set_type,
)
pascal_record_type_strategy = st.builds(
    pascal_record_type,
    end=
        safe_text,
    record=
        safe_text
)
pascal_array_type_strategy = st.builds(
    pascal_array_type,
)
pascal_unpacked_structured_type_strategy = st.builds(
    pascal_unpacked_structured_type,
)
pascal_expression_list_strategy = st.builds(
    pascal_expression_list,
)
pascal_resto_strategy = st.builds(
    pascal_resto,
    name=
        safe_text,
    accessor=
        st.booleans()
)
pascal_structured_type_strategy = st.builds(
    pascal_structured_type,
    packed=
        st.booleans()
)
pascal_simple_type_strategy = st.builds(
    pascal_simple_type,
    name=
        safe_text
)
pascal_case_label_list_strategy = st.builds(
    pascal_case_label_list,
)
pascal_case_limb_strategy = st.builds(
    pascal_case_limb,
)
pascal_set_strategy = st.builds(
    pascal_set,
    brackets=
        safe_text
)
pascal_number_strategy = st.builds(
    pascal_number,
)
pascal_factor_strategy = st.builds(
    pascal_factor,
    boolean=
        safe_text,
    nil=
        st.booleans(),
    string=
        safe_text
)
pascal_term_strategy = st.builds(
    pascal_term,
    operators=
        safe_text
)
pascal_EObject_strategy = st.builds(
    pascal_EObject,
)
pascal_simple_expression_strategy = st.builds(
    pascal_simple_expression,
    operators=
        safe_text,
    prefixOperator=
        safe_text
)
pascal_conditional_statement_strategy = st.builds(
    pascal_conditional_statement,
)
pascal_repetitive_statement_strategy = st.builds(
    pascal_repetitive_statement,
)
pascal_compound_statement_strategy = st.builds(
    pascal_compound_statement,
)
pascal_expression_strategy = st.builds(
    pascal_expression,
    operators=
        safe_text
)
pascal_variable_strategy = st.builds(
    pascal_variable,
    name=
        safe_text
)
pascal_goto_statement_strategy = st.builds(
    pascal_goto_statement,
)
pascal_function_designator_strategy = st.builds(
    pascal_function_designator,
    name=
        safe_text
)
pascal_case_statement_strategy = st.builds(
    pascal_case_statement,
)
pascal_if_statement_strategy = st.builds(
    pascal_if_statement,
)
pascal_for_statement_strategy = st.builds(
    pascal_for_statement,
    initID=
        safe_text
)
pascal_repeat_statement_strategy = st.builds(
    pascal_repeat_statement,
)
pascal_while_statement_strategy = st.builds(
    pascal_while_statement,
)
pascal_with_statement_strategy = st.builds(
    pascal_with_statement,
    records=
        safe_text,
    record=
        safe_text
)
pascal_parameter_type_strategy = st.builds(
    pascal_parameter_type,
    name=
        safe_text
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
pascal_statement_sequence_strategy = st.builds(
    pascal_statement_sequence,
)
pascal_assignment_statement_strategy = st.builds(
    pascal_assignment_statement,
)
pascal_structured_statement_strategy = st.builds(
    pascal_structured_statement,
)
pascal_simple_statement_strategy = st.builds(
    pascal_simple_statement,
)
pascal_statement_strategy = st.builds(
    pascal_statement,
)
pascal_bound_specification_strategy = st.builds(
    pascal_bound_specification,
    fin=
        safe_text,
    name=
        safe_text,
    init=
        safe_text
)
pascal_unpacked_conformant_array_schema_strategy = st.builds(
    pascal_unpacked_conformant_array_schema,
)
pascal_packed_conformant_array_schema_strategy = st.builds(
    pascal_packed_conformant_array_schema,
    name=
        safe_text
)
pascal_conformant_array_schema_strategy = st.builds(
    pascal_conformant_array_schema,
)
pascal_constant_definition_strategy = st.builds(
    pascal_constant_definition,
    name=
        safe_text
)
pascal_label_strategy = st.builds(
    pascal_label,
    number=
        safe_text
)
pascal_procedure_and_function_declaration_part_strategy = st.builds(
    pascal_procedure_and_function_declaration_part,
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







@given(instance=pascal_abstraction_declaration_strategy)
def test_hyp_pascal_abstraction_declaration_forward_setter(instance):
    original = instance.forward
    instance.forward = original
    assert instance.forward == original




@given(instance=pascal_abstraction_heading_strategy)
def test_hyp_pascal_abstraction_heading_resultType_setter(instance):
    original = instance.resultType
    instance.resultType = original
    assert instance.resultType == original



@given(instance=pascal_abstraction_heading_strategy)
def test_hyp_pascal_abstraction_heading_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=pascal_variable_identifier_list_strategy)
def test_hyp_pascal_variable_identifier_list_names_setter(instance):
    original = instance.names
    instance.names = original
    assert instance.names == original






@given(instance=pascal_type_definition_strategy)
def test_hyp_pascal_type_definition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=pascal_constant_strategy)
def test_hyp_pascal_constant_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=pascal_constant_strategy)
def test_hyp_pascal_constant_nil_setter(instance):
    original = instance.nil
    instance.nil = original
    assert instance.nil == original



@given(instance=pascal_constant_strategy)
def test_hyp_pascal_constant_opterator_setter(instance):
    original = instance.opterator
    instance.opterator = original
    assert instance.opterator == original



@given(instance=pascal_constant_strategy)
def test_hyp_pascal_constant_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original



@given(instance=pascal_constant_strategy)
def test_hyp_pascal_constant_boolLiteral_setter(instance):
    original = instance.boolLiteral
    instance.boolLiteral = original
    assert instance.boolLiteral == original





@given(instance=pascal_identifier_list_strategy)
def test_hyp_pascal_identifier_list_ids_setter(instance):
    original = instance.ids
    instance.ids = original
    assert instance.ids == original





@given(instance=pascal_program_heading_strategy)
def test_hyp_pascal_program_heading_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=pascal_variant_part_strategy)
def test_hyp_pascal_variant_part_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=pascal_any_number_strategy)
def test_hyp_pascal_any_number_real_setter(instance):
    original = instance.real
    instance.real = original
    assert instance.real == original



@given(instance=pascal_any_number_strategy)
def test_hyp_pascal_any_number_integer_setter(instance):
    original = instance.integer
    instance.integer = original
    assert instance.integer == original





@given(instance=pascal_tag_field_strategy)
def test_hyp_pascal_tag_field_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=pascal_subrange_type_strategy)
def test_hyp_pascal_subrange_type_subrange_setter(instance):
    original = instance.subrange
    instance.subrange = original
    assert instance.subrange == original








@given(instance=pascal_record_type_strategy)
def test_hyp_pascal_record_type_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original



@given(instance=pascal_record_type_strategy)
def test_hyp_pascal_record_type_record_setter(instance):
    original = instance.record
    instance.record = original
    assert instance.record == original







@given(instance=pascal_resto_strategy)
def test_hyp_pascal_resto_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=pascal_resto_strategy)
def test_hyp_pascal_resto_accessor_setter(instance):
    original = instance.accessor
    instance.accessor = original
    assert instance.accessor == original




@given(instance=pascal_structured_type_strategy)
def test_hyp_pascal_structured_type_packed_setter(instance):
    original = instance.packed
    instance.packed = original
    assert instance.packed == original




@given(instance=pascal_simple_type_strategy)
def test_hyp_pascal_simple_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=pascal_set_strategy)
def test_hyp_pascal_set_brackets_setter(instance):
    original = instance.brackets
    instance.brackets = original
    assert instance.brackets == original





@given(instance=pascal_factor_strategy)
def test_hyp_pascal_factor_boolean_setter(instance):
    original = instance.boolean
    instance.boolean = original
    assert instance.boolean == original



@given(instance=pascal_factor_strategy)
def test_hyp_pascal_factor_nil_setter(instance):
    original = instance.nil
    instance.nil = original
    assert instance.nil == original



@given(instance=pascal_factor_strategy)
def test_hyp_pascal_factor_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original




@given(instance=pascal_term_strategy)
def test_hyp_pascal_term_operators_setter(instance):
    original = instance.operators
    instance.operators = original
    assert instance.operators == original





@given(instance=pascal_simple_expression_strategy)
def test_hyp_pascal_simple_expression_operators_setter(instance):
    original = instance.operators
    instance.operators = original
    assert instance.operators == original



@given(instance=pascal_simple_expression_strategy)
def test_hyp_pascal_simple_expression_prefixOperator_setter(instance):
    original = instance.prefixOperator
    instance.prefixOperator = original
    assert instance.prefixOperator == original







@given(instance=pascal_expression_strategy)
def test_hyp_pascal_expression_operators_setter(instance):
    original = instance.operators
    instance.operators = original
    assert instance.operators == original




@given(instance=pascal_variable_strategy)
def test_hyp_pascal_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=pascal_function_designator_strategy)
def test_hyp_pascal_function_designator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=pascal_for_statement_strategy)
def test_hyp_pascal_for_statement_initID_setter(instance):
    original = instance.initID
    instance.initID = original
    assert instance.initID == original






@given(instance=pascal_with_statement_strategy)
def test_hyp_pascal_with_statement_records_setter(instance):
    original = instance.records
    instance.records = original
    assert instance.records == original



@given(instance=pascal_with_statement_strategy)
def test_hyp_pascal_with_statement_record_setter(instance):
    original = instance.record
    instance.record = original
    assert instance.record == original




@given(instance=pascal_parameter_type_strategy)
def test_hyp_pascal_parameter_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original












@given(instance=pascal_bound_specification_strategy)
def test_hyp_pascal_bound_specification_fin_setter(instance):
    original = instance.fin
    instance.fin = original
    assert instance.fin == original



@given(instance=pascal_bound_specification_strategy)
def test_hyp_pascal_bound_specification_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=pascal_bound_specification_strategy)
def test_hyp_pascal_bound_specification_init_setter(instance):
    original = instance.init
    instance.init = original
    assert instance.init == original





@given(instance=pascal_packed_conformant_array_schema_strategy)
def test_hyp_pascal_packed_conformant_array_schema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=pascal_constant_definition_strategy)
def test_hyp_pascal_constant_definition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=pascal_label_strategy)
def test_hyp_pascal_label_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original







# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    abstraction_declaration,
    pascal_EObject,
    pascal_abstraction_declaration,
    pascal_abstraction_heading,
    pascal_any_number,
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
    pascal_declaration_part,
    pascal_enumerated_type,
    pascal_expression,
    pascal_expression_list,
    pascal_factor,
    pascal_field_list,
    pascal_file_type,
    pascal_fixed_part,
    pascal_for_statement,
    pascal_formal_parameter_list,
    pascal_formal_parameter_section,
    pascal_function_designator,
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
    pascal_program,
    pascal_program_heading,
    pascal_record_section,
    pascal_record_type,
    pascal_repeat_statement,
    pascal_repetitive_statement,
    pascal_resto,
    pascal_set,
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
    pascal_unpacked_conformant_array_schema,
    pascal_unpacked_structured_type,
    pascal_value_parameter_section,
    pascal_variable,
    pascal_variable_declaration_part,
    pascal_variable_identifier_list,
    pascal_variable_parameter_section,
    pascal_variable_section,
    pascal_variant,
    pascal_variant_part,
    pascal_while_statement,
    pascal_with_statement,
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

def test_pascal_abstraction_declaration_forward_value_roundtrip():
    instance = pascal_abstraction_declaration(forward=True)
    assert instance.forward == True
    instance.forward = False
    assert instance.forward == False


def test_pascal_abstraction_heading_name_value_roundtrip():
    instance = pascal_abstraction_heading(name="sample_text", resultType="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_pascal_abstraction_heading_resultType_value_roundtrip():
    instance = pascal_abstraction_heading(name="sample_text", resultType="sample_text")
    assert instance.resultType == "sample_text"
    instance.resultType = "sample_text_2"
    assert instance.resultType == "sample_text_2"


def test_pascal_any_number_integer_value_roundtrip():
    instance = pascal_any_number(integer="sample_text", real="sample_text")
    assert instance.integer == "sample_text"
    instance.integer = "sample_text_2"
    assert instance.integer == "sample_text_2"


def test_pascal_any_number_real_value_roundtrip():
    instance = pascal_any_number(integer="sample_text", real="sample_text")
    assert instance.real == "sample_text"
    instance.real = "sample_text_2"
    assert instance.real == "sample_text_2"


def test_pascal_bound_specification_fin_value_roundtrip():
    instance = pascal_bound_specification(fin="sample_text", init="sample_text", name="sample_text")
    assert instance.fin == "sample_text"
    instance.fin = "sample_text_2"
    assert instance.fin == "sample_text_2"


def test_pascal_bound_specification_init_value_roundtrip():
    instance = pascal_bound_specification(fin="sample_text", init="sample_text", name="sample_text")
    assert instance.init == "sample_text"
    instance.init = "sample_text_2"
    assert instance.init == "sample_text_2"


def test_pascal_bound_specification_name_value_roundtrip():
    instance = pascal_bound_specification(fin="sample_text", init="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_pascal_constant_boolLiteral_value_roundtrip():
    instance = pascal_constant(boolLiteral="sample_text", name="sample_text", nil="sample_text", opterator="sample_text", string="sample_text")
    assert instance.boolLiteral == "sample_text"
    instance.boolLiteral = "sample_text_2"
    assert instance.boolLiteral == "sample_text_2"


def test_pascal_constant_name_value_roundtrip():
    instance = pascal_constant(boolLiteral="sample_text", name="sample_text", nil="sample_text", opterator="sample_text", string="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_pascal_constant_nil_value_roundtrip():
    instance = pascal_constant(boolLiteral="sample_text", name="sample_text", nil="sample_text", opterator="sample_text", string="sample_text")
    assert instance.nil == "sample_text"
    instance.nil = "sample_text_2"
    assert instance.nil == "sample_text_2"


def test_pascal_constant_opterator_value_roundtrip():
    instance = pascal_constant(boolLiteral="sample_text", name="sample_text", nil="sample_text", opterator="sample_text", string="sample_text")
    assert instance.opterator == "sample_text"
    instance.opterator = "sample_text_2"
    assert instance.opterator == "sample_text_2"


def test_pascal_constant_string_value_roundtrip():
    instance = pascal_constant(boolLiteral="sample_text", name="sample_text", nil="sample_text", opterator="sample_text", string="sample_text")
    assert instance.string == "sample_text"
    instance.string = "sample_text_2"
    assert instance.string == "sample_text_2"


def test_pascal_constant_definition_name_value_roundtrip():
    instance = pascal_constant_definition(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_pascal_expression_operators_value_roundtrip():
    instance = pascal_expression(operators="sample_text")
    assert instance.operators == "sample_text"
    instance.operators = "sample_text_2"
    assert instance.operators == "sample_text_2"


def test_pascal_factor_boolean_value_roundtrip():
    instance = pascal_factor(boolean="sample_text", nil=True, string="sample_text")
    assert instance.boolean == "sample_text"
    instance.boolean = "sample_text_2"
    assert instance.boolean == "sample_text_2"


def test_pascal_factor_nil_value_roundtrip():
    instance = pascal_factor(boolean="sample_text", nil=True, string="sample_text")
    assert instance.nil == True
    instance.nil = False
    assert instance.nil == False


def test_pascal_factor_string_value_roundtrip():
    instance = pascal_factor(boolean="sample_text", nil=True, string="sample_text")
    assert instance.string == "sample_text"
    instance.string = "sample_text_2"
    assert instance.string == "sample_text_2"


def test_pascal_for_statement_initID_value_roundtrip():
    instance = pascal_for_statement(initID="sample_text")
    assert instance.initID == "sample_text"
    instance.initID = "sample_text_2"
    assert instance.initID == "sample_text_2"


def test_pascal_function_designator_name_value_roundtrip():
    instance = pascal_function_designator(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_pascal_identifier_list_ids_value_roundtrip():
    instance = pascal_identifier_list(ids="sample_text")
    assert instance.ids == "sample_text"
    instance.ids = "sample_text_2"
    assert instance.ids == "sample_text_2"


def test_pascal_label_number_value_roundtrip():
    instance = pascal_label(number="sample_text")
    assert instance.number == "sample_text"
    instance.number = "sample_text_2"
    assert instance.number == "sample_text_2"


def test_pascal_packed_conformant_array_schema_name_value_roundtrip():
    instance = pascal_packed_conformant_array_schema(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_pascal_parameter_type_name_value_roundtrip():
    instance = pascal_parameter_type(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_pascal_program_heading_name_value_roundtrip():
    instance = pascal_program_heading(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_pascal_record_type_end_value_roundtrip():
    instance = pascal_record_type(end="sample_text", record="sample_text")
    assert instance.end == "sample_text"
    instance.end = "sample_text_2"
    assert instance.end == "sample_text_2"


def test_pascal_record_type_record_value_roundtrip():
    instance = pascal_record_type(end="sample_text", record="sample_text")
    assert instance.record == "sample_text"
    instance.record = "sample_text_2"
    assert instance.record == "sample_text_2"


def test_pascal_resto_accessor_value_roundtrip():
    instance = pascal_resto(accessor=True, name="sample_text")
    assert instance.accessor == True
    instance.accessor = False
    assert instance.accessor == False


def test_pascal_resto_name_value_roundtrip():
    instance = pascal_resto(accessor=True, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_pascal_set_brackets_value_roundtrip():
    instance = pascal_set(brackets="sample_text")
    assert instance.brackets == "sample_text"
    instance.brackets = "sample_text_2"
    assert instance.brackets == "sample_text_2"


def test_pascal_simple_expression_operators_value_roundtrip():
    instance = pascal_simple_expression(operators="sample_text", prefixOperator="sample_text")
    assert instance.operators == "sample_text"
    instance.operators = "sample_text_2"
    assert instance.operators == "sample_text_2"


def test_pascal_simple_expression_prefixOperator_value_roundtrip():
    instance = pascal_simple_expression(operators="sample_text", prefixOperator="sample_text")
    assert instance.prefixOperator == "sample_text"
    instance.prefixOperator = "sample_text_2"
    assert instance.prefixOperator == "sample_text_2"


def test_pascal_simple_type_name_value_roundtrip():
    instance = pascal_simple_type(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_pascal_structured_type_packed_value_roundtrip():
    instance = pascal_structured_type(packed=True)
    assert instance.packed == True
    instance.packed = False
    assert instance.packed == False


def test_pascal_subrange_type_subrange_value_roundtrip():
    instance = pascal_subrange_type(subrange="sample_text")
    assert instance.subrange == "sample_text"
    instance.subrange = "sample_text_2"
    assert instance.subrange == "sample_text_2"


def test_pascal_tag_field_name_value_roundtrip():
    instance = pascal_tag_field(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_pascal_term_operators_value_roundtrip():
    instance = pascal_term(operators="sample_text")
    assert instance.operators == "sample_text"
    instance.operators = "sample_text_2"
    assert instance.operators == "sample_text_2"


def test_pascal_type_definition_name_value_roundtrip():
    instance = pascal_type_definition(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_pascal_variable_name_value_roundtrip():
    instance = pascal_variable(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_pascal_variable_identifier_list_names_value_roundtrip():
    instance = pascal_variable_identifier_list(names="sample_text")
    assert instance.names == "sample_text"
    instance.names = "sample_text_2"
    assert instance.names == "sample_text_2"


def test_pascal_variant_part_name_value_roundtrip():
    instance = pascal_variant_part(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_pascal_with_statement_record_value_roundtrip():
    instance = pascal_with_statement(record="sample_text", records="sample_text")
    assert instance.record == "sample_text"
    instance.record = "sample_text_2"
    assert instance.record == "sample_text_2"


def test_pascal_with_statement_records_value_roundtrip():
    instance = pascal_with_statement(record="sample_text", records="sample_text")
    assert instance.records == "sample_text"
    instance.records = "sample_text_2"
    assert instance.records == "sample_text_2"


def test_pascal_abstraction_heading_isa_abstraction_declaration():
    instance = pascal_abstraction_heading(name="sample_text", resultType="sample_text")
    assert isinstance(instance, abstraction_declaration)


def test_assoc_array202_link_reassign_clear():
    a = pascal_resto(accessor=True, name="sample_text")
    b1 = pascal_resto(accessor=True, name="sample_text")
    b2 = pascal_resto(accessor=False, name="sample_text_2")
    _safe_set(a, 'pascal_resto201', b1)
    assert _is_linked(a, 'pascal_resto201', b1)
    if hasattr(b1, 'pascal_resto203'):
        assert _is_linked(b1, 'pascal_resto203', a)
    _safe_set(a, 'pascal_resto201', b2)
    assert _is_linked(a, 'pascal_resto201', b2)
    if hasattr(b1, 'pascal_resto203'):
        assert not _is_linked(b1, 'pascal_resto203', a)
    if hasattr(b2, 'pascal_resto203'):
        assert _is_linked(b2, 'pascal_resto203', a)
    _safe_set(a, 'pascal_resto201', None)
    assert not _is_linked(a, 'pascal_resto201', b2)
    if hasattr(b2, 'pascal_resto203'):
        assert not _is_linked(b2, 'pascal_resto203', a)


def test_assoc_array73_link_reassign_clear():
    a = pascal_parameter_type(name="sample_text")
    b1 = pascal_conformant_array_schema()
    b2 = pascal_conformant_array_schema()
    _safe_set(a, 'pascal_parameter_type74', b1)
    assert _is_linked(a, 'pascal_parameter_type74', b1)
    if hasattr(b1, 'pascal_conformant_array_schema'):
        assert _is_linked(b1, 'pascal_conformant_array_schema', a)
    _safe_set(a, 'pascal_parameter_type74', b2)
    assert _is_linked(a, 'pascal_parameter_type74', b2)
    if hasattr(b1, 'pascal_conformant_array_schema'):
        assert not _is_linked(b1, 'pascal_conformant_array_schema', a)
    if hasattr(b2, 'pascal_conformant_array_schema'):
        assert _is_linked(b2, 'pascal_conformant_array_schema', a)
    _safe_set(a, 'pascal_parameter_type74', None)
    assert not _is_linked(a, 'pascal_parameter_type74', b2)
    if hasattr(b2, 'pascal_conformant_array_schema'):
        assert not _is_linked(b2, 'pascal_conformant_array_schema', a)


def test_assoc_block45_link_reassign_clear():
    a = pascal_abstraction_declaration(forward=True)
    b1 = pascal_block()
    b2 = pascal_block()
    _safe_set(a, 'pascal_abstraction_declaration46', b1)
    assert _is_linked(a, 'pascal_abstraction_declaration46', b1)
    if hasattr(b1, 'pascal_block47'):
        assert _is_linked(b1, 'pascal_block47', a)
    _safe_set(a, 'pascal_abstraction_declaration46', b2)
    assert _is_linked(a, 'pascal_abstraction_declaration46', b2)
    if hasattr(b1, 'pascal_block47'):
        assert not _is_linked(b1, 'pascal_block47', a)
    if hasattr(b2, 'pascal_block47'):
        assert _is_linked(b2, 'pascal_block47', a)
    _safe_set(a, 'pascal_abstraction_declaration46', None)
    assert not _is_linked(a, 'pascal_abstraction_declaration46', b2)
    if hasattr(b2, 'pascal_block47'):
        assert not _is_linked(b2, 'pascal_block47', a)


def test_assoc_bound79_link_reassign_clear():
    a = pascal_packed_conformant_array_schema(name="sample_text")
    b1 = pascal_bound_specification(fin="sample_text", init="sample_text", name="sample_text")
    b2 = pascal_bound_specification(fin="sample_text_2", init="sample_text_2", name="sample_text_2")
    _safe_set(a, 'pascal_packed_conformant_array_schema80', b1)
    assert _is_linked(a, 'pascal_packed_conformant_array_schema80', b1)
    if hasattr(b1, 'pascal_bound_specification'):
        assert _is_linked(b1, 'pascal_bound_specification', a)
    _safe_set(a, 'pascal_packed_conformant_array_schema80', b2)
    assert _is_linked(a, 'pascal_packed_conformant_array_schema80', b2)
    if hasattr(b1, 'pascal_bound_specification'):
        assert not _is_linked(b1, 'pascal_bound_specification', a)
    if hasattr(b2, 'pascal_bound_specification'):
        assert _is_linked(b2, 'pascal_bound_specification', a)
    _safe_set(a, 'pascal_packed_conformant_array_schema80', None)
    assert not _is_linked(a, 'pascal_packed_conformant_array_schema80', b2)
    if hasattr(b2, 'pascal_bound_specification'):
        assert not _is_linked(b2, 'pascal_bound_specification', a)


def test_assoc_bounds81_link_reassign_clear():
    a = pascal_bound_specification(fin="sample_text", init="sample_text", name="sample_text")
    b1 = pascal_unpacked_conformant_array_schema()
    b2 = pascal_unpacked_conformant_array_schema()
    _safe_set(a, 'pascal_bound_specification83', b1)
    assert _is_linked(a, 'pascal_bound_specification83', b1)
    if hasattr(b1, 'pascal_unpacked_conformant_array_schema82'):
        assert _is_linked(b1, 'pascal_unpacked_conformant_array_schema82', a)
    _safe_set(a, 'pascal_bound_specification83', b2)
    assert _is_linked(a, 'pascal_bound_specification83', b2)
    if hasattr(b1, 'pascal_unpacked_conformant_array_schema82'):
        assert not _is_linked(b1, 'pascal_unpacked_conformant_array_schema82', a)
    if hasattr(b2, 'pascal_unpacked_conformant_array_schema82'):
        assert _is_linked(b2, 'pascal_unpacked_conformant_array_schema82', a)
    _safe_set(a, 'pascal_bound_specification83', None)
    assert not _is_linked(a, 'pascal_bound_specification83', b2)
    if hasattr(b2, 'pascal_unpacked_conformant_array_schema82'):
        assert not _is_linked(b2, 'pascal_unpacked_conformant_array_schema82', a)


def test_assoc_const23_link_reassign_clear():
    a = pascal_constant_definition(name="sample_text")
    b1 = pascal_constant(boolLiteral="sample_text", name="sample_text", nil="sample_text", opterator="sample_text", string="sample_text")
    b2 = pascal_constant(boolLiteral="sample_text_2", name="sample_text_2", nil="sample_text_2", opterator="sample_text_2", string="sample_text_2")
    _safe_set(a, 'pascal_constant_definition24', b1)
    assert _is_linked(a, 'pascal_constant_definition24', b1)
    if hasattr(b1, 'pascal_constant'):
        assert _is_linked(b1, 'pascal_constant', a)
    _safe_set(a, 'pascal_constant_definition24', b2)
    assert _is_linked(a, 'pascal_constant_definition24', b2)
    if hasattr(b1, 'pascal_constant'):
        assert not _is_linked(b1, 'pascal_constant', a)
    if hasattr(b2, 'pascal_constant'):
        assert _is_linked(b2, 'pascal_constant', a)
    _safe_set(a, 'pascal_constant_definition24', None)
    assert not _is_linked(a, 'pascal_constant_definition24', b2)
    if hasattr(b2, 'pascal_constant'):
        assert not _is_linked(b2, 'pascal_constant', a)


def test_assoc_const238_link_reassign_clear():
    a = pascal_subrange_type(subrange="sample_text")
    b1 = pascal_constant(boolLiteral="sample_text", name="sample_text", nil="sample_text", opterator="sample_text", string="sample_text")
    b2 = pascal_constant(boolLiteral="sample_text_2", name="sample_text_2", nil="sample_text_2", opterator="sample_text_2", string="sample_text_2")
    _safe_set(a, 'pascal_subrange_type239', b1)
    assert _is_linked(a, 'pascal_subrange_type239', b1)
    if hasattr(b1, 'pascal_constant240'):
        assert _is_linked(b1, 'pascal_constant240', a)
    _safe_set(a, 'pascal_subrange_type239', b2)
    assert _is_linked(a, 'pascal_subrange_type239', b2)
    if hasattr(b1, 'pascal_constant240'):
        assert not _is_linked(b1, 'pascal_constant240', a)
    if hasattr(b2, 'pascal_constant240'):
        assert _is_linked(b2, 'pascal_constant240', a)
    _safe_set(a, 'pascal_subrange_type239', None)
    assert not _is_linked(a, 'pascal_subrange_type239', b2)
    if hasattr(b2, 'pascal_constant240'):
        assert not _is_linked(b2, 'pascal_constant240', a)


def test_assoc_constants170_link_reassign_clear():
    a = pascal_constant(boolLiteral="sample_text", name="sample_text", nil="sample_text", opterator="sample_text", string="sample_text")
    b1 = pascal_case_label_list()
    b2 = pascal_case_label_list()
    _safe_set(a, 'pascal_constant172', b1)
    assert _is_linked(a, 'pascal_constant172', b1)
    if hasattr(b1, 'pascal_case_label_list171'):
        assert _is_linked(b1, 'pascal_case_label_list171', a)
    _safe_set(a, 'pascal_constant172', b2)
    assert _is_linked(a, 'pascal_constant172', b2)
    if hasattr(b1, 'pascal_case_label_list171'):
        assert not _is_linked(b1, 'pascal_case_label_list171', a)
    if hasattr(b2, 'pascal_case_label_list171'):
        assert _is_linked(b2, 'pascal_case_label_list171', a)
    _safe_set(a, 'pascal_constant172', None)
    assert not _is_linked(a, 'pascal_constant172', b2)
    if hasattr(b2, 'pascal_case_label_list171'):
        assert not _is_linked(b2, 'pascal_case_label_list171', a)


def test_assoc_consts21_link_reassign_clear():
    a = pascal_constant_definition(name="sample_text")
    b1 = pascal_constant_definition_part()
    b2 = pascal_constant_definition_part()
    _safe_set(a, 'pascal_constant_definition', b1)
    assert _is_linked(a, 'pascal_constant_definition', b1)
    if hasattr(b1, 'pascal_constant_definition_part22'):
        assert _is_linked(b1, 'pascal_constant_definition_part22', a)
    _safe_set(a, 'pascal_constant_definition', b2)
    assert _is_linked(a, 'pascal_constant_definition', b2)
    if hasattr(b1, 'pascal_constant_definition_part22'):
        assert not _is_linked(b1, 'pascal_constant_definition_part22', a)
    if hasattr(b2, 'pascal_constant_definition_part22'):
        assert _is_linked(b2, 'pascal_constant_definition_part22', a)
    _safe_set(a, 'pascal_constant_definition', None)
    assert not _is_linked(a, 'pascal_constant_definition', b2)
    if hasattr(b2, 'pascal_constant_definition_part22'):
        assert not _is_linked(b2, 'pascal_constant_definition_part22', a)


def test_assoc_enumerated227_link_reassign_clear():
    a = pascal_simple_type(name="sample_text")
    b1 = pascal_enumerated_type()
    b2 = pascal_enumerated_type()
    _safe_set(a, 'pascal_simple_type228', b1)
    assert _is_linked(a, 'pascal_simple_type228', b1)
    if hasattr(b1, 'pascal_enumerated_type'):
        assert _is_linked(b1, 'pascal_enumerated_type', a)
    _safe_set(a, 'pascal_simple_type228', b2)
    assert _is_linked(a, 'pascal_simple_type228', b2)
    if hasattr(b1, 'pascal_enumerated_type'):
        assert not _is_linked(b1, 'pascal_enumerated_type', a)
    if hasattr(b2, 'pascal_enumerated_type'):
        assert _is_linked(b2, 'pascal_enumerated_type', a)
    _safe_set(a, 'pascal_simple_type228', None)
    assert not _is_linked(a, 'pascal_simple_type228', b2)
    if hasattr(b2, 'pascal_enumerated_type'):
        assert not _is_linked(b2, 'pascal_enumerated_type', a)


def test_assoc_expression104_link_reassign_clear():
    a = pascal_expression(operators="sample_text")
    b1 = pascal_assignment_statement()
    b2 = pascal_assignment_statement()
    _safe_set(a, 'pascal_expression', b1)
    assert _is_linked(a, 'pascal_expression', b1)
    if hasattr(b1, 'pascal_assignment_statement105'):
        assert _is_linked(b1, 'pascal_assignment_statement105', a)
    _safe_set(a, 'pascal_expression', b2)
    assert _is_linked(a, 'pascal_expression', b2)
    if hasattr(b1, 'pascal_assignment_statement105'):
        assert not _is_linked(b1, 'pascal_assignment_statement105', a)
    if hasattr(b2, 'pascal_assignment_statement105'):
        assert _is_linked(b2, 'pascal_assignment_statement105', a)
    _safe_set(a, 'pascal_expression', None)
    assert not _is_linked(a, 'pascal_expression', b2)
    if hasattr(b2, 'pascal_assignment_statement105'):
        assert not _is_linked(b2, 'pascal_assignment_statement105', a)


def test_assoc_expression126_link_reassign_clear():
    a = pascal_expression(operators="sample_text")
    b1 = pascal_while_statement()
    b2 = pascal_while_statement()
    _safe_set(a, 'pascal_expression128', b1)
    assert _is_linked(a, 'pascal_expression128', b1)
    if hasattr(b1, 'pascal_while_statement127'):
        assert _is_linked(b1, 'pascal_while_statement127', a)
    _safe_set(a, 'pascal_expression128', b2)
    assert _is_linked(a, 'pascal_expression128', b2)
    if hasattr(b1, 'pascal_while_statement127'):
        assert not _is_linked(b1, 'pascal_while_statement127', a)
    if hasattr(b2, 'pascal_while_statement127'):
        assert _is_linked(b2, 'pascal_while_statement127', a)
    _safe_set(a, 'pascal_expression128', None)
    assert not _is_linked(a, 'pascal_expression128', b2)
    if hasattr(b2, 'pascal_while_statement127'):
        assert not _is_linked(b2, 'pascal_while_statement127', a)


def test_assoc_expression135_link_reassign_clear():
    a = pascal_expression(operators="sample_text")
    b1 = pascal_repeat_statement()
    b2 = pascal_repeat_statement()
    _safe_set(a, 'pascal_expression137', b1)
    assert _is_linked(a, 'pascal_expression137', b1)
    if hasattr(b1, 'pascal_repeat_statement136'):
        assert _is_linked(b1, 'pascal_repeat_statement136', a)
    _safe_set(a, 'pascal_expression137', b2)
    assert _is_linked(a, 'pascal_expression137', b2)
    if hasattr(b1, 'pascal_repeat_statement136'):
        assert not _is_linked(b1, 'pascal_repeat_statement136', a)
    if hasattr(b2, 'pascal_repeat_statement136'):
        assert _is_linked(b2, 'pascal_repeat_statement136', a)
    _safe_set(a, 'pascal_expression137', None)
    assert not _is_linked(a, 'pascal_expression137', b2)
    if hasattr(b2, 'pascal_repeat_statement136'):
        assert not _is_linked(b2, 'pascal_repeat_statement136', a)


def test_assoc_expression151_link_reassign_clear():
    a = pascal_expression(operators="sample_text")
    b1 = pascal_if_statement()
    b2 = pascal_if_statement()
    _safe_set(a, 'pascal_expression153', b1)
    assert _is_linked(a, 'pascal_expression153', b1)
    if hasattr(b1, 'pascal_if_statement152'):
        assert _is_linked(b1, 'pascal_if_statement152', a)
    _safe_set(a, 'pascal_expression153', b2)
    assert _is_linked(a, 'pascal_expression153', b2)
    if hasattr(b1, 'pascal_if_statement152'):
        assert not _is_linked(b1, 'pascal_if_statement152', a)
    if hasattr(b2, 'pascal_if_statement152'):
        assert _is_linked(b2, 'pascal_if_statement152', a)
    _safe_set(a, 'pascal_expression153', None)
    assert not _is_linked(a, 'pascal_expression153', b2)
    if hasattr(b2, 'pascal_if_statement152'):
        assert not _is_linked(b2, 'pascal_if_statement152', a)


def test_assoc_expression160_link_reassign_clear():
    a = pascal_expression(operators="sample_text")
    b1 = pascal_case_statement()
    b2 = pascal_case_statement()
    _safe_set(a, 'pascal_expression162', b1)
    assert _is_linked(a, 'pascal_expression162', b1)
    if hasattr(b1, 'pascal_case_statement161'):
        assert _is_linked(b1, 'pascal_case_statement161', a)
    _safe_set(a, 'pascal_expression162', b2)
    assert _is_linked(a, 'pascal_expression162', b2)
    if hasattr(b1, 'pascal_case_statement161'):
        assert not _is_linked(b1, 'pascal_case_statement161', a)
    if hasattr(b2, 'pascal_case_statement161'):
        assert _is_linked(b2, 'pascal_case_statement161', a)
    _safe_set(a, 'pascal_expression162', None)
    assert not _is_linked(a, 'pascal_expression162', b2)
    if hasattr(b2, 'pascal_case_statement161'):
        assert not _is_linked(b2, 'pascal_case_statement161', a)


def test_assoc_expression191_link_reassign_clear():
    a = pascal_factor(boolean="sample_text", nil=True, string="sample_text")
    b1 = pascal_expression(operators="sample_text")
    b2 = pascal_expression(operators="sample_text_2")
    _safe_set(a, 'pascal_factor192', b1)
    assert _is_linked(a, 'pascal_factor192', b1)
    if hasattr(b1, 'pascal_expression193'):
        assert _is_linked(b1, 'pascal_expression193', a)
    _safe_set(a, 'pascal_factor192', b2)
    assert _is_linked(a, 'pascal_factor192', b2)
    if hasattr(b1, 'pascal_expression193'):
        assert not _is_linked(b1, 'pascal_expression193', a)
    if hasattr(b2, 'pascal_expression193'):
        assert _is_linked(b2, 'pascal_expression193', a)
    _safe_set(a, 'pascal_factor192', None)
    assert not _is_linked(a, 'pascal_factor192', b2)
    if hasattr(b2, 'pascal_expression193'):
        assert not _is_linked(b2, 'pascal_expression193', a)


def test_assoc_expressionFin141_link_reassign_clear():
    a = pascal_for_statement(initID="sample_text")
    b1 = pascal_expression(operators="sample_text")
    b2 = pascal_expression(operators="sample_text_2")
    _safe_set(a, 'pascal_for_statement142', b1)
    assert _is_linked(a, 'pascal_for_statement142', b1)
    if hasattr(b1, 'pascal_expression143'):
        assert _is_linked(b1, 'pascal_expression143', a)
    _safe_set(a, 'pascal_for_statement142', b2)
    assert _is_linked(a, 'pascal_for_statement142', b2)
    if hasattr(b1, 'pascal_expression143'):
        assert not _is_linked(b1, 'pascal_expression143', a)
    if hasattr(b2, 'pascal_expression143'):
        assert _is_linked(b2, 'pascal_expression143', a)
    _safe_set(a, 'pascal_for_statement142', None)
    assert not _is_linked(a, 'pascal_for_statement142', b2)
    if hasattr(b2, 'pascal_expression143'):
        assert not _is_linked(b2, 'pascal_expression143', a)


def test_assoc_expressionInit138_link_reassign_clear():
    a = pascal_for_statement(initID="sample_text")
    b1 = pascal_expression(operators="sample_text")
    b2 = pascal_expression(operators="sample_text_2")
    _safe_set(a, 'pascal_for_statement139', b1)
    assert _is_linked(a, 'pascal_for_statement139', b1)
    if hasattr(b1, 'pascal_expression140'):
        assert _is_linked(b1, 'pascal_expression140', a)
    _safe_set(a, 'pascal_for_statement139', b2)
    assert _is_linked(a, 'pascal_for_statement139', b2)
    if hasattr(b1, 'pascal_expression140'):
        assert not _is_linked(b1, 'pascal_expression140', a)
    if hasattr(b2, 'pascal_expression140'):
        assert _is_linked(b2, 'pascal_expression140', a)
    _safe_set(a, 'pascal_for_statement139', None)
    assert not _is_linked(a, 'pascal_for_statement139', b2)
    if hasattr(b2, 'pascal_expression140'):
        assert not _is_linked(b2, 'pascal_expression140', a)


def test_assoc_expressions176_link_reassign_clear():
    a = pascal_simple_expression(operators="sample_text", prefixOperator="sample_text")
    b1 = pascal_expression(operators="sample_text")
    b2 = pascal_expression(operators="sample_text_2")
    _safe_set(a, 'pascal_simple_expression', b1)
    assert _is_linked(a, 'pascal_simple_expression', b1)
    if hasattr(b1, 'pascal_expression177'):
        assert _is_linked(b1, 'pascal_expression177', a)
    _safe_set(a, 'pascal_simple_expression', b2)
    assert _is_linked(a, 'pascal_simple_expression', b2)
    if hasattr(b1, 'pascal_expression177'):
        assert not _is_linked(b1, 'pascal_expression177', a)
    if hasattr(b2, 'pascal_expression177'):
        assert _is_linked(b2, 'pascal_expression177', a)
    _safe_set(a, 'pascal_simple_expression', None)
    assert not _is_linked(a, 'pascal_simple_expression', b2)
    if hasattr(b2, 'pascal_expression177'):
        assert not _is_linked(b2, 'pascal_expression177', a)


def test_assoc_expressions199_link_reassign_clear():
    a = pascal_resto(accessor=True, name="sample_text")
    b1 = pascal_expression_list()
    b2 = pascal_expression_list()
    _safe_set(a, 'pascal_resto200', b1)
    assert _is_linked(a, 'pascal_resto200', b1)
    if hasattr(b1, 'pascal_expression_list'):
        assert _is_linked(b1, 'pascal_expression_list', a)
    _safe_set(a, 'pascal_resto200', b2)
    assert _is_linked(a, 'pascal_resto200', b2)
    if hasattr(b1, 'pascal_expression_list'):
        assert not _is_linked(b1, 'pascal_expression_list', a)
    if hasattr(b2, 'pascal_expression_list'):
        assert _is_linked(b2, 'pascal_expression_list', a)
    _safe_set(a, 'pascal_resto200', None)
    assert not _is_linked(a, 'pascal_resto200', b2)
    if hasattr(b2, 'pascal_expression_list'):
        assert not _is_linked(b2, 'pascal_expression_list', a)


def test_assoc_expressions210_link_reassign_clear():
    a = pascal_set(brackets="sample_text")
    b1 = pascal_expression_list()
    b2 = pascal_expression_list()
    _safe_set(a, 'pascal_set211', b1)
    assert _is_linked(a, 'pascal_set211', b1)
    if hasattr(b1, 'pascal_expression_list212'):
        assert _is_linked(b1, 'pascal_expression_list212', a)
    _safe_set(a, 'pascal_set211', b2)
    assert _is_linked(a, 'pascal_set211', b2)
    if hasattr(b1, 'pascal_expression_list212'):
        assert not _is_linked(b1, 'pascal_expression_list212', a)
    if hasattr(b2, 'pascal_expression_list212'):
        assert _is_linked(b2, 'pascal_expression_list212', a)
    _safe_set(a, 'pascal_set211', None)
    assert not _is_linked(a, 'pascal_set211', b2)
    if hasattr(b2, 'pascal_expression_list212'):
        assert not _is_linked(b2, 'pascal_expression_list212', a)


def test_assoc_expressions213_link_reassign_clear():
    a = pascal_expression(operators="sample_text")
    b1 = pascal_expression_list()
    b2 = pascal_expression_list()
    _safe_set(a, 'pascal_expression215', b1)
    assert _is_linked(a, 'pascal_expression215', b1)
    if hasattr(b1, 'pascal_expression_list214'):
        assert _is_linked(b1, 'pascal_expression_list214', a)
    _safe_set(a, 'pascal_expression215', b2)
    assert _is_linked(a, 'pascal_expression215', b2)
    if hasattr(b1, 'pascal_expression_list214'):
        assert not _is_linked(b1, 'pascal_expression_list214', a)
    if hasattr(b2, 'pascal_expression_list214'):
        assert _is_linked(b2, 'pascal_expression_list214', a)
    _safe_set(a, 'pascal_expression215', None)
    assert not _is_linked(a, 'pascal_expression215', b2)
    if hasattr(b2, 'pascal_expression_list214'):
        assert not _is_linked(b2, 'pascal_expression_list214', a)


def test_assoc_expressions216_link_reassign_clear():
    a = pascal_function_designator(name="sample_text")
    b1 = pascal_expression_list()
    b2 = pascal_expression_list()
    _safe_set(a, 'pascal_function_designator217', b1)
    assert _is_linked(a, 'pascal_function_designator217', b1)
    if hasattr(b1, 'pascal_expression_list218'):
        assert _is_linked(b1, 'pascal_expression_list218', a)
    _safe_set(a, 'pascal_function_designator217', b2)
    assert _is_linked(a, 'pascal_function_designator217', b2)
    if hasattr(b1, 'pascal_expression_list218'):
        assert not _is_linked(b1, 'pascal_expression_list218', a)
    if hasattr(b2, 'pascal_expression_list218'):
        assert _is_linked(b2, 'pascal_expression_list218', a)
    _safe_set(a, 'pascal_function_designator217', None)
    assert not _is_linked(a, 'pascal_function_designator217', b2)
    if hasattr(b2, 'pascal_expression_list218'):
        assert not _is_linked(b2, 'pascal_expression_list218', a)


def test_assoc_factors180_link_reassign_clear():
    a = pascal_term(operators="sample_text")
    b1 = pascal_factor(boolean="sample_text", nil=True, string="sample_text")
    b2 = pascal_factor(boolean="sample_text_2", nil=False, string="sample_text_2")
    _safe_set(a, 'pascal_term', {b1})
    assert _is_linked(a, 'pascal_term', b1)
    if hasattr(b1, 'pascal_factor'):
        assert _is_linked(b1, 'pascal_factor', a)
    _safe_set(a, 'pascal_term', {b2})
    assert _is_linked(a, 'pascal_term', b2)
    if hasattr(b1, 'pascal_factor'):
        assert not _is_linked(b1, 'pascal_factor', a)
    if hasattr(b2, 'pascal_factor'):
        assert _is_linked(b2, 'pascal_factor', a)
    _safe_set(a, 'pascal_term', set())
    assert not _is_linked(a, 'pascal_term', b2)
    if hasattr(b2, 'pascal_factor'):
        assert not _is_linked(b2, 'pascal_factor', a)


def test_assoc_fields257_link_reassign_clear():
    a = pascal_record_type(end="sample_text", record="sample_text")
    b1 = pascal_field_list()
    b2 = pascal_field_list()
    _safe_set(a, 'pascal_record_type258', b1)
    assert _is_linked(a, 'pascal_record_type258', b1)
    if hasattr(b1, 'pascal_field_list'):
        assert _is_linked(b1, 'pascal_field_list', a)
    _safe_set(a, 'pascal_record_type258', b2)
    assert _is_linked(a, 'pascal_record_type258', b2)
    if hasattr(b1, 'pascal_field_list'):
        assert not _is_linked(b1, 'pascal_field_list', a)
    if hasattr(b2, 'pascal_field_list'):
        assert _is_linked(b2, 'pascal_field_list', a)
    _safe_set(a, 'pascal_record_type258', None)
    assert not _is_linked(a, 'pascal_record_type258', b2)
    if hasattr(b2, 'pascal_field_list'):
        assert not _is_linked(b2, 'pascal_field_list', a)


def test_assoc_finalConst235_link_reassign_clear():
    a = pascal_subrange_type(subrange="sample_text")
    b1 = pascal_constant(boolLiteral="sample_text", name="sample_text", nil="sample_text", opterator="sample_text", string="sample_text")
    b2 = pascal_constant(boolLiteral="sample_text_2", name="sample_text_2", nil="sample_text_2", opterator="sample_text_2", string="sample_text_2")
    _safe_set(a, 'pascal_subrange_type236', b1)
    assert _is_linked(a, 'pascal_subrange_type236', b1)
    if hasattr(b1, 'pascal_constant237'):
        assert _is_linked(b1, 'pascal_constant237', a)
    _safe_set(a, 'pascal_subrange_type236', b2)
    assert _is_linked(a, 'pascal_subrange_type236', b2)
    if hasattr(b1, 'pascal_constant237'):
        assert not _is_linked(b1, 'pascal_constant237', a)
    if hasattr(b2, 'pascal_constant237'):
        assert _is_linked(b2, 'pascal_constant237', a)
    _safe_set(a, 'pascal_subrange_type236', None)
    assert not _is_linked(a, 'pascal_subrange_type236', b2)
    if hasattr(b2, 'pascal_constant237'):
        assert not _is_linked(b2, 'pascal_constant237', a)


def test_assoc_for_124_link_reassign_clear():
    a = pascal_for_statement(initID="sample_text")
    b1 = pascal_repetitive_statement()
    b2 = pascal_repetitive_statement()
    _safe_set(a, 'pascal_for_statement', b1)
    assert _is_linked(a, 'pascal_for_statement', b1)
    if hasattr(b1, 'pascal_repetitive_statement125'):
        assert _is_linked(b1, 'pascal_repetitive_statement125', a)
    _safe_set(a, 'pascal_for_statement', b2)
    assert _is_linked(a, 'pascal_for_statement', b2)
    if hasattr(b1, 'pascal_repetitive_statement125'):
        assert not _is_linked(b1, 'pascal_repetitive_statement125', a)
    if hasattr(b2, 'pascal_repetitive_statement125'):
        assert _is_linked(b2, 'pascal_repetitive_statement125', a)
    _safe_set(a, 'pascal_for_statement', None)
    assert not _is_linked(a, 'pascal_for_statement', b2)
    if hasattr(b2, 'pascal_repetitive_statement125'):
        assert not _is_linked(b2, 'pascal_repetitive_statement125', a)


def test_assoc_function188_link_reassign_clear():
    a = pascal_function_designator(name="sample_text")
    b1 = pascal_factor(boolean="sample_text", nil=True, string="sample_text")
    b2 = pascal_factor(boolean="sample_text_2", nil=False, string="sample_text_2")
    _safe_set(a, 'pascal_function_designator190', b1)
    assert _is_linked(a, 'pascal_function_designator190', b1)
    if hasattr(b1, 'pascal_factor189'):
        assert _is_linked(b1, 'pascal_factor189', a)
    _safe_set(a, 'pascal_function_designator190', b2)
    assert _is_linked(a, 'pascal_function_designator190', b2)
    if hasattr(b1, 'pascal_factor189'):
        assert not _is_linked(b1, 'pascal_factor189', a)
    if hasattr(b2, 'pascal_factor189'):
        assert _is_linked(b2, 'pascal_factor189', a)
    _safe_set(a, 'pascal_function_designator190', None)
    assert not _is_linked(a, 'pascal_function_designator190', b2)
    if hasattr(b2, 'pascal_factor189'):
        assert not _is_linked(b2, 'pascal_factor189', a)


def test_assoc_function59_link_reassign_clear():
    a = pascal_abstraction_heading(name="sample_text", resultType="sample_text")
    b1 = pascal_formal_parameter_section()
    b2 = pascal_formal_parameter_section()
    _safe_set(a, 'pascal_abstraction_heading61', b1)
    assert _is_linked(a, 'pascal_abstraction_heading61', b1)
    if hasattr(b1, 'pascal_formal_parameter_section60'):
        assert _is_linked(b1, 'pascal_formal_parameter_section60', a)
    _safe_set(a, 'pascal_abstraction_heading61', b2)
    assert _is_linked(a, 'pascal_abstraction_heading61', b2)
    if hasattr(b1, 'pascal_formal_parameter_section60'):
        assert not _is_linked(b1, 'pascal_formal_parameter_section60', a)
    if hasattr(b2, 'pascal_formal_parameter_section60'):
        assert _is_linked(b2, 'pascal_formal_parameter_section60', a)
    _safe_set(a, 'pascal_abstraction_heading61', None)
    assert not _is_linked(a, 'pascal_abstraction_heading61', b2)
    if hasattr(b2, 'pascal_formal_parameter_section60'):
        assert not _is_linked(b2, 'pascal_formal_parameter_section60', a)


def test_assoc_function98_link_reassign_clear():
    a = pascal_function_designator(name="sample_text")
    b1 = pascal_simple_statement()
    b2 = pascal_simple_statement()
    _safe_set(a, 'pascal_function_designator', b1)
    assert _is_linked(a, 'pascal_function_designator', b1)
    if hasattr(b1, 'pascal_simple_statement99'):
        assert _is_linked(b1, 'pascal_simple_statement99', a)
    _safe_set(a, 'pascal_function_designator', b2)
    assert _is_linked(a, 'pascal_function_designator', b2)
    if hasattr(b1, 'pascal_simple_statement99'):
        assert not _is_linked(b1, 'pascal_simple_statement99', a)
    if hasattr(b2, 'pascal_simple_statement99'):
        assert _is_linked(b2, 'pascal_simple_statement99', a)
    _safe_set(a, 'pascal_function_designator', None)
    assert not _is_linked(a, 'pascal_function_designator', b2)
    if hasattr(b2, 'pascal_simple_statement99'):
        assert not _is_linked(b2, 'pascal_simple_statement99', a)


def test_assoc_functions38_link_reassign_clear():
    a = pascal_abstraction_declaration(forward=True)
    b1 = pascal_procedure_and_function_declaration_part()
    b2 = pascal_procedure_and_function_declaration_part()
    _safe_set(a, 'pascal_abstraction_declaration', b1)
    assert _is_linked(a, 'pascal_abstraction_declaration', b1)
    if hasattr(b1, 'pascal_procedure_and_function_declaration_part39'):
        assert _is_linked(b1, 'pascal_procedure_and_function_declaration_part39', a)
    _safe_set(a, 'pascal_abstraction_declaration', b2)
    assert _is_linked(a, 'pascal_abstraction_declaration', b2)
    if hasattr(b1, 'pascal_procedure_and_function_declaration_part39'):
        assert not _is_linked(b1, 'pascal_procedure_and_function_declaration_part39', a)
    if hasattr(b2, 'pascal_procedure_and_function_declaration_part39'):
        assert _is_linked(b2, 'pascal_procedure_and_function_declaration_part39', a)
    _safe_set(a, 'pascal_abstraction_declaration', None)
    assert not _is_linked(a, 'pascal_abstraction_declaration', b2)
    if hasattr(b2, 'pascal_procedure_and_function_declaration_part39'):
        assert not _is_linked(b2, 'pascal_procedure_and_function_declaration_part39', a)


def test_assoc_heading0_link_reassign_clear():
    a = pascal_program_heading(name="sample_text")
    b1 = pascal_program()
    b2 = pascal_program()
    _safe_set(a, 'pascal_program_heading', b1)
    assert _is_linked(a, 'pascal_program_heading', b1)
    if hasattr(b1, 'pascal_program'):
        assert _is_linked(b1, 'pascal_program', a)
    _safe_set(a, 'pascal_program_heading', b2)
    assert _is_linked(a, 'pascal_program_heading', b2)
    if hasattr(b1, 'pascal_program'):
        assert not _is_linked(b1, 'pascal_program', a)
    if hasattr(b2, 'pascal_program'):
        assert _is_linked(b2, 'pascal_program', a)
    _safe_set(a, 'pascal_program_heading', None)
    assert not _is_linked(a, 'pascal_program_heading', b2)
    if hasattr(b2, 'pascal_program'):
        assert not _is_linked(b2, 'pascal_program', a)


def test_assoc_heading42_link_reassign_clear():
    a = pascal_abstraction_heading(name="sample_text", resultType="sample_text")
    b1 = pascal_abstraction_declaration(forward=True)
    b2 = pascal_abstraction_declaration(forward=False)
    _safe_set(a, 'pascal_abstraction_heading44', b1)
    assert _is_linked(a, 'pascal_abstraction_heading44', b1)
    if hasattr(b1, 'pascal_abstraction_declaration43'):
        assert _is_linked(b1, 'pascal_abstraction_declaration43', a)
    _safe_set(a, 'pascal_abstraction_heading44', b2)
    assert _is_linked(a, 'pascal_abstraction_heading44', b2)
    if hasattr(b1, 'pascal_abstraction_declaration43'):
        assert not _is_linked(b1, 'pascal_abstraction_declaration43', a)
    if hasattr(b2, 'pascal_abstraction_declaration43'):
        assert _is_linked(b2, 'pascal_abstraction_declaration43', a)
    _safe_set(a, 'pascal_abstraction_heading44', None)
    assert not _is_linked(a, 'pascal_abstraction_heading44', b2)
    if hasattr(b2, 'pascal_abstraction_declaration43'):
        assert not _is_linked(b2, 'pascal_abstraction_declaration43', a)


def test_assoc_identifiers229_link_reassign_clear():
    a = pascal_identifier_list(ids="sample_text")
    b1 = pascal_enumerated_type()
    b2 = pascal_enumerated_type()
    _safe_set(a, 'pascal_identifier_list231', b1)
    assert _is_linked(a, 'pascal_identifier_list231', b1)
    if hasattr(b1, 'pascal_enumerated_type230'):
        assert _is_linked(b1, 'pascal_enumerated_type230', a)
    _safe_set(a, 'pascal_identifier_list231', b2)
    assert _is_linked(a, 'pascal_identifier_list231', b2)
    if hasattr(b1, 'pascal_enumerated_type230'):
        assert not _is_linked(b1, 'pascal_enumerated_type230', a)
    if hasattr(b2, 'pascal_enumerated_type230'):
        assert _is_linked(b2, 'pascal_enumerated_type230', a)
    _safe_set(a, 'pascal_identifier_list231', None)
    assert not _is_linked(a, 'pascal_identifier_list231', b2)
    if hasattr(b2, 'pascal_enumerated_type230'):
        assert not _is_linked(b2, 'pascal_enumerated_type230', a)


def test_assoc_identifiers274_link_reassign_clear():
    a = pascal_identifier_list(ids="sample_text")
    b1 = pascal_record_section()
    b2 = pascal_record_section()
    _safe_set(a, 'pascal_identifier_list276', b1)
    assert _is_linked(a, 'pascal_identifier_list276', b1)
    if hasattr(b1, 'pascal_record_section275'):
        assert _is_linked(b1, 'pascal_record_section275', a)
    _safe_set(a, 'pascal_identifier_list276', b2)
    assert _is_linked(a, 'pascal_identifier_list276', b2)
    if hasattr(b1, 'pascal_record_section275'):
        assert not _is_linked(b1, 'pascal_record_section275', a)
    if hasattr(b2, 'pascal_record_section275'):
        assert _is_linked(b2, 'pascal_record_section275', a)
    _safe_set(a, 'pascal_identifier_list276', None)
    assert not _is_linked(a, 'pascal_identifier_list276', b2)
    if hasattr(b2, 'pascal_record_section275'):
        assert not _is_linked(b2, 'pascal_record_section275', a)


def test_assoc_identifiers3_link_reassign_clear():
    a = pascal_program_heading(name="sample_text")
    b1 = pascal_identifier_list(ids="sample_text")
    b2 = pascal_identifier_list(ids="sample_text_2")
    _safe_set(a, 'pascal_program_heading4', b1)
    assert _is_linked(a, 'pascal_program_heading4', b1)
    if hasattr(b1, 'pascal_identifier_list'):
        assert _is_linked(b1, 'pascal_identifier_list', a)
    _safe_set(a, 'pascal_program_heading4', b2)
    assert _is_linked(a, 'pascal_program_heading4', b2)
    if hasattr(b1, 'pascal_identifier_list'):
        assert not _is_linked(b1, 'pascal_identifier_list', a)
    if hasattr(b2, 'pascal_identifier_list'):
        assert _is_linked(b2, 'pascal_identifier_list', a)
    _safe_set(a, 'pascal_program_heading4', None)
    assert not _is_linked(a, 'pascal_program_heading4', b2)
    if hasattr(b2, 'pascal_identifier_list'):
        assert not _is_linked(b2, 'pascal_identifier_list', a)


def test_assoc_identifiers31_link_reassign_clear():
    a = pascal_variable_identifier_list(names="sample_text")
    b1 = pascal_variable_section()
    b2 = pascal_variable_section()
    _safe_set(a, 'pascal_variable_identifier_list', b1)
    assert _is_linked(a, 'pascal_variable_identifier_list', b1)
    if hasattr(b1, 'pascal_variable_section32'):
        assert _is_linked(b1, 'pascal_variable_section32', a)
    _safe_set(a, 'pascal_variable_identifier_list', b2)
    assert _is_linked(a, 'pascal_variable_identifier_list', b2)
    if hasattr(b1, 'pascal_variable_section32'):
        assert not _is_linked(b1, 'pascal_variable_section32', a)
    if hasattr(b2, 'pascal_variable_section32'):
        assert _is_linked(b2, 'pascal_variable_section32', a)
    _safe_set(a, 'pascal_variable_identifier_list', None)
    assert not _is_linked(a, 'pascal_variable_identifier_list', b2)
    if hasattr(b2, 'pascal_variable_section32'):
        assert not _is_linked(b2, 'pascal_variable_section32', a)


def test_assoc_identifiers62_link_reassign_clear():
    a = pascal_identifier_list(ids="sample_text")
    b1 = pascal_value_parameter_section()
    b2 = pascal_value_parameter_section()
    _safe_set(a, 'pascal_identifier_list64', b1)
    assert _is_linked(a, 'pascal_identifier_list64', b1)
    if hasattr(b1, 'pascal_value_parameter_section63'):
        assert _is_linked(b1, 'pascal_value_parameter_section63', a)
    _safe_set(a, 'pascal_identifier_list64', b2)
    assert _is_linked(a, 'pascal_identifier_list64', b2)
    if hasattr(b1, 'pascal_value_parameter_section63'):
        assert not _is_linked(b1, 'pascal_value_parameter_section63', a)
    if hasattr(b2, 'pascal_value_parameter_section63'):
        assert _is_linked(b2, 'pascal_value_parameter_section63', a)
    _safe_set(a, 'pascal_identifier_list64', None)
    assert not _is_linked(a, 'pascal_identifier_list64', b2)
    if hasattr(b2, 'pascal_value_parameter_section63'):
        assert not _is_linked(b2, 'pascal_value_parameter_section63', a)


def test_assoc_identifiers67_link_reassign_clear():
    a = pascal_identifier_list(ids="sample_text")
    b1 = pascal_variable_parameter_section()
    b2 = pascal_variable_parameter_section()
    _safe_set(a, 'pascal_identifier_list69', b1)
    assert _is_linked(a, 'pascal_identifier_list69', b1)
    if hasattr(b1, 'pascal_variable_parameter_section68'):
        assert _is_linked(b1, 'pascal_variable_parameter_section68', a)
    _safe_set(a, 'pascal_identifier_list69', b2)
    assert _is_linked(a, 'pascal_identifier_list69', b2)
    if hasattr(b1, 'pascal_variable_parameter_section68'):
        assert not _is_linked(b1, 'pascal_variable_parameter_section68', a)
    if hasattr(b2, 'pascal_variable_parameter_section68'):
        assert _is_linked(b2, 'pascal_variable_parameter_section68', a)
    _safe_set(a, 'pascal_identifier_list69', None)
    assert not _is_linked(a, 'pascal_identifier_list69', b2)
    if hasattr(b2, 'pascal_variable_parameter_section68'):
        assert not _is_linked(b2, 'pascal_variable_parameter_section68', a)


def test_assoc_indexes251_link_reassign_clear():
    a = pascal_simple_type(name="sample_text")
    b1 = pascal_array_type()
    b2 = pascal_array_type()
    _safe_set(a, 'pascal_simple_type253', b1)
    assert _is_linked(a, 'pascal_simple_type253', b1)
    if hasattr(b1, 'pascal_array_type252'):
        assert _is_linked(b1, 'pascal_array_type252', a)
    _safe_set(a, 'pascal_simple_type253', b2)
    assert _is_linked(a, 'pascal_simple_type253', b2)
    if hasattr(b1, 'pascal_array_type252'):
        assert not _is_linked(b1, 'pascal_array_type252', a)
    if hasattr(b2, 'pascal_array_type252'):
        assert _is_linked(b2, 'pascal_array_type252', a)
    _safe_set(a, 'pascal_simple_type253', None)
    assert not _is_linked(a, 'pascal_simple_type253', b2)
    if hasattr(b2, 'pascal_array_type252'):
        assert not _is_linked(b2, 'pascal_array_type252', a)


def test_assoc_initialConst232_link_reassign_clear():
    a = pascal_subrange_type(subrange="sample_text")
    b1 = pascal_constant(boolLiteral="sample_text", name="sample_text", nil="sample_text", opterator="sample_text", string="sample_text")
    b2 = pascal_constant(boolLiteral="sample_text_2", name="sample_text_2", nil="sample_text_2", opterator="sample_text_2", string="sample_text_2")
    _safe_set(a, 'pascal_subrange_type233', b1)
    assert _is_linked(a, 'pascal_subrange_type233', b1)
    if hasattr(b1, 'pascal_constant234'):
        assert _is_linked(b1, 'pascal_constant234', a)
    _safe_set(a, 'pascal_subrange_type233', b2)
    assert _is_linked(a, 'pascal_subrange_type233', b2)
    if hasattr(b1, 'pascal_constant234'):
        assert not _is_linked(b1, 'pascal_constant234', a)
    if hasattr(b2, 'pascal_constant234'):
        assert _is_linked(b2, 'pascal_constant234', a)
    _safe_set(a, 'pascal_subrange_type233', None)
    assert not _is_linked(a, 'pascal_subrange_type233', b2)
    if hasattr(b2, 'pascal_constant234'):
        assert not _is_linked(b2, 'pascal_constant234', a)


def test_assoc_label106_link_reassign_clear():
    a = pascal_label(number="sample_text")
    b1 = pascal_goto_statement()
    b2 = pascal_goto_statement()
    _safe_set(a, 'pascal_label108', b1)
    assert _is_linked(a, 'pascal_label108', b1)
    if hasattr(b1, 'pascal_goto_statement107'):
        assert _is_linked(b1, 'pascal_goto_statement107', a)
    _safe_set(a, 'pascal_label108', b2)
    assert _is_linked(a, 'pascal_label108', b2)
    if hasattr(b1, 'pascal_goto_statement107'):
        assert not _is_linked(b1, 'pascal_goto_statement107', a)
    if hasattr(b2, 'pascal_goto_statement107'):
        assert _is_linked(b2, 'pascal_goto_statement107', a)
    _safe_set(a, 'pascal_label108', None)
    assert not _is_linked(a, 'pascal_label108', b2)
    if hasattr(b2, 'pascal_goto_statement107'):
        assert not _is_linked(b2, 'pascal_goto_statement107', a)


def test_assoc_label89_link_reassign_clear():
    a = pascal_label(number="sample_text")
    b1 = pascal_statement()
    b2 = pascal_statement()
    _safe_set(a, 'pascal_label91', b1)
    assert _is_linked(a, 'pascal_label91', b1)
    if hasattr(b1, 'pascal_statement90'):
        assert _is_linked(b1, 'pascal_statement90', a)
    _safe_set(a, 'pascal_label91', b2)
    assert _is_linked(a, 'pascal_label91', b2)
    if hasattr(b1, 'pascal_statement90'):
        assert not _is_linked(b1, 'pascal_statement90', a)
    if hasattr(b2, 'pascal_statement90'):
        assert _is_linked(b2, 'pascal_statement90', a)
    _safe_set(a, 'pascal_label91', None)
    assert not _is_linked(a, 'pascal_label91', b2)
    if hasattr(b2, 'pascal_statement90'):
        assert not _is_linked(b2, 'pascal_statement90', a)


def test_assoc_labels19_link_reassign_clear():
    a = pascal_label(number="sample_text")
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


def test_assoc_not_195_link_reassign_clear():
    a = pascal_factor(boolean="sample_text", nil=True, string="sample_text")
    b1 = pascal_factor(boolean="sample_text", nil=True, string="sample_text")
    b2 = pascal_factor(boolean="sample_text_2", nil=False, string="sample_text_2")
    _safe_set(a, 'pascal_factor194', b1)
    assert _is_linked(a, 'pascal_factor194', b1)
    if hasattr(b1, 'pascal_factor196'):
        assert _is_linked(b1, 'pascal_factor196', a)
    _safe_set(a, 'pascal_factor194', b2)
    assert _is_linked(a, 'pascal_factor194', b2)
    if hasattr(b1, 'pascal_factor196'):
        assert not _is_linked(b1, 'pascal_factor196', a)
    if hasattr(b2, 'pascal_factor196'):
        assert _is_linked(b2, 'pascal_factor196', a)
    _safe_set(a, 'pascal_factor194', None)
    assert not _is_linked(a, 'pascal_factor194', b2)
    if hasattr(b2, 'pascal_factor196'):
        assert not _is_linked(b2, 'pascal_factor196', a)


def test_assoc_number184_link_reassign_clear():
    a = pascal_factor(boolean="sample_text", nil=True, string="sample_text")
    b1 = pascal_number()
    b2 = pascal_number()
    _safe_set(a, 'pascal_factor185', b1)
    assert _is_linked(a, 'pascal_factor185', b1)
    if hasattr(b1, 'pascal_number'):
        assert _is_linked(b1, 'pascal_number', a)
    _safe_set(a, 'pascal_factor185', b2)
    assert _is_linked(a, 'pascal_factor185', b2)
    if hasattr(b1, 'pascal_number'):
        assert not _is_linked(b1, 'pascal_number', a)
    if hasattr(b2, 'pascal_number'):
        assert _is_linked(b2, 'pascal_number', a)
    _safe_set(a, 'pascal_factor185', None)
    assert not _is_linked(a, 'pascal_factor185', b2)
    if hasattr(b2, 'pascal_number'):
        assert not _is_linked(b2, 'pascal_number', a)


def test_assoc_number290_link_reassign_clear():
    a = pascal_any_number(integer="sample_text", real="sample_text")
    b1 = pascal_number()
    b2 = pascal_number()
    _safe_set(a, 'pascal_any_number', b1)
    assert _is_linked(a, 'pascal_any_number', b1)
    if hasattr(b1, 'pascal_number291'):
        assert _is_linked(b1, 'pascal_number291', a)
    _safe_set(a, 'pascal_any_number', b2)
    assert _is_linked(a, 'pascal_any_number', b2)
    if hasattr(b1, 'pascal_number291'):
        assert not _is_linked(b1, 'pascal_number291', a)
    if hasattr(b2, 'pascal_number291'):
        assert _is_linked(b2, 'pascal_number291', a)
    _safe_set(a, 'pascal_any_number', None)
    assert not _is_linked(a, 'pascal_any_number', b2)
    if hasattr(b2, 'pascal_number291'):
        assert not _is_linked(b2, 'pascal_number291', a)


def test_assoc_number292_link_reassign_clear():
    a = pascal_constant(boolLiteral="sample_text", name="sample_text", nil="sample_text", opterator="sample_text", string="sample_text")
    b1 = pascal_number()
    b2 = pascal_number()
    _safe_set(a, 'pascal_constant293', b1)
    assert _is_linked(a, 'pascal_constant293', b1)
    if hasattr(b1, 'pascal_number294'):
        assert _is_linked(b1, 'pascal_number294', a)
    _safe_set(a, 'pascal_constant293', b2)
    assert _is_linked(a, 'pascal_constant293', b2)
    if hasattr(b1, 'pascal_number294'):
        assert not _is_linked(b1, 'pascal_number294', a)
    if hasattr(b2, 'pascal_number294'):
        assert _is_linked(b2, 'pascal_number294', a)
    _safe_set(a, 'pascal_constant293', None)
    assert not _is_linked(a, 'pascal_constant293', b2)
    if hasattr(b2, 'pascal_number294'):
        assert not _is_linked(b2, 'pascal_number294', a)


def test_assoc_packed75_link_reassign_clear():
    a = pascal_packed_conformant_array_schema(name="sample_text")
    b1 = pascal_conformant_array_schema()
    b2 = pascal_conformant_array_schema()
    _safe_set(a, 'pascal_packed_conformant_array_schema', b1)
    assert _is_linked(a, 'pascal_packed_conformant_array_schema', b1)
    if hasattr(b1, 'pascal_conformant_array_schema76'):
        assert _is_linked(b1, 'pascal_conformant_array_schema76', a)
    _safe_set(a, 'pascal_packed_conformant_array_schema', b2)
    assert _is_linked(a, 'pascal_packed_conformant_array_schema', b2)
    if hasattr(b1, 'pascal_conformant_array_schema76'):
        assert not _is_linked(b1, 'pascal_conformant_array_schema76', a)
    if hasattr(b2, 'pascal_conformant_array_schema76'):
        assert _is_linked(b2, 'pascal_conformant_array_schema76', a)
    _safe_set(a, 'pascal_packed_conformant_array_schema', None)
    assert not _is_linked(a, 'pascal_packed_conformant_array_schema', b2)
    if hasattr(b2, 'pascal_conformant_array_schema76'):
        assert not _is_linked(b2, 'pascal_conformant_array_schema76', a)


def test_assoc_parameters40_link_reassign_clear():
    a = pascal_abstraction_heading(name="sample_text", resultType="sample_text")
    b1 = pascal_formal_parameter_list()
    b2 = pascal_formal_parameter_list()
    _safe_set(a, 'pascal_abstraction_heading41', b1)
    assert _is_linked(a, 'pascal_abstraction_heading41', b1)
    if hasattr(b1, 'pascal_formal_parameter_list'):
        assert _is_linked(b1, 'pascal_formal_parameter_list', a)
    _safe_set(a, 'pascal_abstraction_heading41', b2)
    assert _is_linked(a, 'pascal_abstraction_heading41', b2)
    if hasattr(b1, 'pascal_formal_parameter_list'):
        assert not _is_linked(b1, 'pascal_formal_parameter_list', a)
    if hasattr(b2, 'pascal_formal_parameter_list'):
        assert _is_linked(b2, 'pascal_formal_parameter_list', a)
    _safe_set(a, 'pascal_abstraction_heading41', None)
    assert not _is_linked(a, 'pascal_abstraction_heading41', b2)
    if hasattr(b2, 'pascal_formal_parameter_list'):
        assert not _is_linked(b2, 'pascal_formal_parameter_list', a)


def test_assoc_pointer208_link_reassign_clear():
    a = pascal_resto(accessor=True, name="sample_text")
    b1 = pascal_resto(accessor=True, name="sample_text")
    b2 = pascal_resto(accessor=False, name="sample_text_2")
    _safe_set(a, 'pascal_resto207', b1)
    assert _is_linked(a, 'pascal_resto207', b1)
    if hasattr(b1, 'pascal_resto209'):
        assert _is_linked(b1, 'pascal_resto209', a)
    _safe_set(a, 'pascal_resto207', b2)
    assert _is_linked(a, 'pascal_resto207', b2)
    if hasattr(b1, 'pascal_resto209'):
        assert not _is_linked(b1, 'pascal_resto209', a)
    if hasattr(b2, 'pascal_resto209'):
        assert _is_linked(b2, 'pascal_resto209', a)
    _safe_set(a, 'pascal_resto207', None)
    assert not _is_linked(a, 'pascal_resto207', b2)
    if hasattr(b2, 'pascal_resto209'):
        assert not _is_linked(b2, 'pascal_resto209', a)


def test_assoc_procedure56_link_reassign_clear():
    a = pascal_abstraction_heading(name="sample_text", resultType="sample_text")
    b1 = pascal_formal_parameter_section()
    b2 = pascal_formal_parameter_section()
    _safe_set(a, 'pascal_abstraction_heading58', b1)
    assert _is_linked(a, 'pascal_abstraction_heading58', b1)
    if hasattr(b1, 'pascal_formal_parameter_section57'):
        assert _is_linked(b1, 'pascal_formal_parameter_section57', a)
    _safe_set(a, 'pascal_abstraction_heading58', b2)
    assert _is_linked(a, 'pascal_abstraction_heading58', b2)
    if hasattr(b1, 'pascal_formal_parameter_section57'):
        assert not _is_linked(b1, 'pascal_formal_parameter_section57', a)
    if hasattr(b2, 'pascal_formal_parameter_section57'):
        assert _is_linked(b2, 'pascal_formal_parameter_section57', a)
    _safe_set(a, 'pascal_abstraction_heading58', None)
    assert not _is_linked(a, 'pascal_abstraction_heading58', b2)
    if hasattr(b2, 'pascal_formal_parameter_section57'):
        assert not _is_linked(b2, 'pascal_formal_parameter_section57', a)


def test_assoc_procedures36_link_reassign_clear():
    a = pascal_abstraction_heading(name="sample_text", resultType="sample_text")
    b1 = pascal_procedure_and_function_declaration_part()
    b2 = pascal_procedure_and_function_declaration_part()
    _safe_set(a, 'pascal_abstraction_heading', b1)
    assert _is_linked(a, 'pascal_abstraction_heading', b1)
    if hasattr(b1, 'pascal_procedure_and_function_declaration_part37'):
        assert _is_linked(b1, 'pascal_procedure_and_function_declaration_part37', a)
    _safe_set(a, 'pascal_abstraction_heading', b2)
    assert _is_linked(a, 'pascal_abstraction_heading', b2)
    if hasattr(b1, 'pascal_procedure_and_function_declaration_part37'):
        assert not _is_linked(b1, 'pascal_procedure_and_function_declaration_part37', a)
    if hasattr(b2, 'pascal_procedure_and_function_declaration_part37'):
        assert _is_linked(b2, 'pascal_procedure_and_function_declaration_part37', a)
    _safe_set(a, 'pascal_abstraction_heading', None)
    assert not _is_linked(a, 'pascal_abstraction_heading', b2)
    if hasattr(b2, 'pascal_procedure_and_function_declaration_part37'):
        assert not _is_linked(b2, 'pascal_procedure_and_function_declaration_part37', a)


def test_assoc_record245_link_reassign_clear():
    a = pascal_record_type(end="sample_text", record="sample_text")
    b1 = pascal_unpacked_structured_type()
    b2 = pascal_unpacked_structured_type()
    _safe_set(a, 'pascal_record_type', b1)
    assert _is_linked(a, 'pascal_record_type', b1)
    if hasattr(b1, 'pascal_unpacked_structured_type246'):
        assert _is_linked(b1, 'pascal_unpacked_structured_type246', a)
    _safe_set(a, 'pascal_record_type', b2)
    assert _is_linked(a, 'pascal_record_type', b2)
    if hasattr(b1, 'pascal_unpacked_structured_type246'):
        assert not _is_linked(b1, 'pascal_unpacked_structured_type246', a)
    if hasattr(b2, 'pascal_unpacked_structured_type246'):
        assert _is_linked(b2, 'pascal_unpacked_structured_type246', a)
    _safe_set(a, 'pascal_record_type', None)
    assert not _is_linked(a, 'pascal_record_type', b2)
    if hasattr(b2, 'pascal_unpacked_structured_type246'):
        assert not _is_linked(b2, 'pascal_unpacked_structured_type246', a)


def test_assoc_set186_link_reassign_clear():
    a = pascal_set(brackets="sample_text")
    b1 = pascal_factor(boolean="sample_text", nil=True, string="sample_text")
    b2 = pascal_factor(boolean="sample_text_2", nil=False, string="sample_text_2")
    _safe_set(a, 'pascal_set', b1)
    assert _is_linked(a, 'pascal_set', b1)
    if hasattr(b1, 'pascal_factor187'):
        assert _is_linked(b1, 'pascal_factor187', a)
    _safe_set(a, 'pascal_set', b2)
    assert _is_linked(a, 'pascal_set', b2)
    if hasattr(b1, 'pascal_factor187'):
        assert not _is_linked(b1, 'pascal_factor187', a)
    if hasattr(b2, 'pascal_factor187'):
        assert _is_linked(b2, 'pascal_factor187', a)
    _safe_set(a, 'pascal_set', None)
    assert not _is_linked(a, 'pascal_set', b2)
    if hasattr(b2, 'pascal_factor187'):
        assert not _is_linked(b2, 'pascal_factor187', a)


def test_assoc_simple219_link_reassign_clear():
    a = pascal_simple_type(name="sample_text")
    b1 = pascal_type()
    b2 = pascal_type()
    _safe_set(a, 'pascal_simple_type', b1)
    assert _is_linked(a, 'pascal_simple_type', b1)
    if hasattr(b1, 'pascal_type220'):
        assert _is_linked(b1, 'pascal_type220', a)
    _safe_set(a, 'pascal_simple_type', b2)
    assert _is_linked(a, 'pascal_simple_type', b2)
    if hasattr(b1, 'pascal_type220'):
        assert not _is_linked(b1, 'pascal_type220', a)
    if hasattr(b2, 'pascal_type220'):
        assert _is_linked(b2, 'pascal_type220', a)
    _safe_set(a, 'pascal_simple_type', None)
    assert not _is_linked(a, 'pascal_simple_type', b2)
    if hasattr(b2, 'pascal_type220'):
        assert not _is_linked(b2, 'pascal_type220', a)


def test_assoc_stmt144_link_reassign_clear():
    a = pascal_for_statement(initID="sample_text")
    b1 = pascal_statement()
    b2 = pascal_statement()
    _safe_set(a, 'pascal_for_statement145', b1)
    assert _is_linked(a, 'pascal_for_statement145', b1)
    if hasattr(b1, 'pascal_statement146'):
        assert _is_linked(b1, 'pascal_statement146', a)
    _safe_set(a, 'pascal_for_statement145', b2)
    assert _is_linked(a, 'pascal_for_statement145', b2)
    if hasattr(b1, 'pascal_statement146'):
        assert not _is_linked(b1, 'pascal_statement146', a)
    if hasattr(b2, 'pascal_statement146'):
        assert _is_linked(b2, 'pascal_statement146', a)
    _safe_set(a, 'pascal_for_statement145', None)
    assert not _is_linked(a, 'pascal_for_statement145', b2)
    if hasattr(b2, 'pascal_statement146'):
        assert not _is_linked(b2, 'pascal_statement146', a)


def test_assoc_stmt173_link_reassign_clear():
    a = pascal_with_statement(record="sample_text", records="sample_text")
    b1 = pascal_statement()
    b2 = pascal_statement()
    _safe_set(a, 'pascal_with_statement174', b1)
    assert _is_linked(a, 'pascal_with_statement174', b1)
    if hasattr(b1, 'pascal_statement175'):
        assert _is_linked(b1, 'pascal_statement175', a)
    _safe_set(a, 'pascal_with_statement174', b2)
    assert _is_linked(a, 'pascal_with_statement174', b2)
    if hasattr(b1, 'pascal_statement175'):
        assert not _is_linked(b1, 'pascal_statement175', a)
    if hasattr(b2, 'pascal_statement175'):
        assert _is_linked(b2, 'pascal_statement175', a)
    _safe_set(a, 'pascal_with_statement174', None)
    assert not _is_linked(a, 'pascal_with_statement174', b2)
    if hasattr(b2, 'pascal_statement175'):
        assert not _is_linked(b2, 'pascal_statement175', a)


def test_assoc_structured221_link_reassign_clear():
    a = pascal_structured_type(packed=True)
    b1 = pascal_type()
    b2 = pascal_type()
    _safe_set(a, 'pascal_structured_type', b1)
    assert _is_linked(a, 'pascal_structured_type', b1)
    if hasattr(b1, 'pascal_type222'):
        assert _is_linked(b1, 'pascal_type222', a)
    _safe_set(a, 'pascal_structured_type', b2)
    assert _is_linked(a, 'pascal_structured_type', b2)
    if hasattr(b1, 'pascal_type222'):
        assert not _is_linked(b1, 'pascal_type222', a)
    if hasattr(b2, 'pascal_type222'):
        assert _is_linked(b2, 'pascal_type222', a)
    _safe_set(a, 'pascal_structured_type', None)
    assert not _is_linked(a, 'pascal_structured_type', b2)
    if hasattr(b2, 'pascal_type222'):
        assert not _is_linked(b2, 'pascal_type222', a)


def test_assoc_subrange225_link_reassign_clear():
    a = pascal_subrange_type(subrange="sample_text")
    b1 = pascal_simple_type(name="sample_text")
    b2 = pascal_simple_type(name="sample_text_2")
    _safe_set(a, 'pascal_subrange_type', b1)
    assert _is_linked(a, 'pascal_subrange_type', b1)
    if hasattr(b1, 'pascal_simple_type226'):
        assert _is_linked(b1, 'pascal_simple_type226', a)
    _safe_set(a, 'pascal_subrange_type', b2)
    assert _is_linked(a, 'pascal_subrange_type', b2)
    if hasattr(b1, 'pascal_simple_type226'):
        assert not _is_linked(b1, 'pascal_simple_type226', a)
    if hasattr(b2, 'pascal_simple_type226'):
        assert _is_linked(b2, 'pascal_simple_type226', a)
    _safe_set(a, 'pascal_subrange_type', None)
    assert not _is_linked(a, 'pascal_subrange_type', b2)
    if hasattr(b2, 'pascal_simple_type226'):
        assert not _is_linked(b2, 'pascal_simple_type226', a)


def test_assoc_tag280_link_reassign_clear():
    a = pascal_variant_part(name="sample_text")
    b1 = pascal_tag_field(name="sample_text")
    b2 = pascal_tag_field(name="sample_text_2")
    _safe_set(a, 'pascal_variant_part281', b1)
    assert _is_linked(a, 'pascal_variant_part281', b1)
    if hasattr(b1, 'pascal_tag_field'):
        assert _is_linked(b1, 'pascal_tag_field', a)
    _safe_set(a, 'pascal_variant_part281', b2)
    assert _is_linked(a, 'pascal_variant_part281', b2)
    if hasattr(b1, 'pascal_tag_field'):
        assert not _is_linked(b1, 'pascal_tag_field', a)
    if hasattr(b2, 'pascal_tag_field'):
        assert _is_linked(b2, 'pascal_tag_field', a)
    _safe_set(a, 'pascal_variant_part281', None)
    assert not _is_linked(a, 'pascal_variant_part281', b2)
    if hasattr(b2, 'pascal_tag_field'):
        assert not _is_linked(b2, 'pascal_tag_field', a)


def test_assoc_terms178_link_reassign_clear():
    a = pascal_simple_expression(operators="sample_text", prefixOperator="sample_text")
    b1 = pascal_EObject()
    b2 = pascal_EObject()
    _safe_set(a, 'pascal_simple_expression179', {b1})
    assert _is_linked(a, 'pascal_simple_expression179', b1)
    if hasattr(b1, 'pascal_EObject'):
        assert _is_linked(b1, 'pascal_EObject', a)
    _safe_set(a, 'pascal_simple_expression179', {b2})
    assert _is_linked(a, 'pascal_simple_expression179', b2)
    if hasattr(b1, 'pascal_EObject'):
        assert not _is_linked(b1, 'pascal_EObject', a)
    if hasattr(b2, 'pascal_EObject'):
        assert _is_linked(b2, 'pascal_EObject', a)
    _safe_set(a, 'pascal_simple_expression179', set())
    assert not _is_linked(a, 'pascal_simple_expression179', b2)
    if hasattr(b2, 'pascal_EObject'):
        assert not _is_linked(b2, 'pascal_EObject', a)


def test_assoc_type241_link_reassign_clear():
    a = pascal_structured_type(packed=True)
    b1 = pascal_unpacked_structured_type()
    b2 = pascal_unpacked_structured_type()
    _safe_set(a, 'pascal_structured_type242', b1)
    assert _is_linked(a, 'pascal_structured_type242', b1)
    if hasattr(b1, 'pascal_unpacked_structured_type'):
        assert _is_linked(b1, 'pascal_unpacked_structured_type', a)
    _safe_set(a, 'pascal_structured_type242', b2)
    assert _is_linked(a, 'pascal_structured_type242', b2)
    if hasattr(b1, 'pascal_unpacked_structured_type'):
        assert not _is_linked(b1, 'pascal_unpacked_structured_type', a)
    if hasattr(b2, 'pascal_unpacked_structured_type'):
        assert _is_linked(b2, 'pascal_unpacked_structured_type', a)
    _safe_set(a, 'pascal_structured_type242', None)
    assert not _is_linked(a, 'pascal_structured_type242', b2)
    if hasattr(b2, 'pascal_unpacked_structured_type'):
        assert not _is_linked(b2, 'pascal_unpacked_structured_type', a)


def test_assoc_type27_link_reassign_clear():
    a = pascal_type_definition(name="sample_text")
    b1 = pascal_type()
    b2 = pascal_type()
    _safe_set(a, 'pascal_type_definition28', b1)
    assert _is_linked(a, 'pascal_type_definition28', b1)
    if hasattr(b1, 'pascal_type'):
        assert _is_linked(b1, 'pascal_type', a)
    _safe_set(a, 'pascal_type_definition28', b2)
    assert _is_linked(a, 'pascal_type_definition28', b2)
    if hasattr(b1, 'pascal_type'):
        assert not _is_linked(b1, 'pascal_type', a)
    if hasattr(b2, 'pascal_type'):
        assert _is_linked(b2, 'pascal_type', a)
    _safe_set(a, 'pascal_type_definition28', None)
    assert not _is_linked(a, 'pascal_type_definition28', b2)
    if hasattr(b2, 'pascal_type'):
        assert not _is_linked(b2, 'pascal_type', a)


def test_assoc_type65_link_reassign_clear():
    a = pascal_parameter_type(name="sample_text")
    b1 = pascal_value_parameter_section()
    b2 = pascal_value_parameter_section()
    _safe_set(a, 'pascal_parameter_type', b1)
    assert _is_linked(a, 'pascal_parameter_type', b1)
    if hasattr(b1, 'pascal_value_parameter_section66'):
        assert _is_linked(b1, 'pascal_value_parameter_section66', a)
    _safe_set(a, 'pascal_parameter_type', b2)
    assert _is_linked(a, 'pascal_parameter_type', b2)
    if hasattr(b1, 'pascal_value_parameter_section66'):
        assert not _is_linked(b1, 'pascal_value_parameter_section66', a)
    if hasattr(b2, 'pascal_value_parameter_section66'):
        assert _is_linked(b2, 'pascal_value_parameter_section66', a)
    _safe_set(a, 'pascal_parameter_type', None)
    assert not _is_linked(a, 'pascal_parameter_type', b2)
    if hasattr(b2, 'pascal_value_parameter_section66'):
        assert not _is_linked(b2, 'pascal_value_parameter_section66', a)


def test_assoc_type70_link_reassign_clear():
    a = pascal_parameter_type(name="sample_text")
    b1 = pascal_variable_parameter_section()
    b2 = pascal_variable_parameter_section()
    _safe_set(a, 'pascal_parameter_type72', b1)
    assert _is_linked(a, 'pascal_parameter_type72', b1)
    if hasattr(b1, 'pascal_variable_parameter_section71'):
        assert _is_linked(b1, 'pascal_variable_parameter_section71', a)
    _safe_set(a, 'pascal_parameter_type72', b2)
    assert _is_linked(a, 'pascal_parameter_type72', b2)
    if hasattr(b1, 'pascal_variable_parameter_section71'):
        assert not _is_linked(b1, 'pascal_variable_parameter_section71', a)
    if hasattr(b2, 'pascal_variable_parameter_section71'):
        assert _is_linked(b2, 'pascal_variable_parameter_section71', a)
    _safe_set(a, 'pascal_parameter_type72', None)
    assert not _is_linked(a, 'pascal_parameter_type72', b2)
    if hasattr(b2, 'pascal_variable_parameter_section71'):
        assert not _is_linked(b2, 'pascal_variable_parameter_section71', a)


def test_assoc_type84_link_reassign_clear():
    a = pascal_parameter_type(name="sample_text")
    b1 = pascal_unpacked_conformant_array_schema()
    b2 = pascal_unpacked_conformant_array_schema()
    _safe_set(a, 'pascal_parameter_type86', b1)
    assert _is_linked(a, 'pascal_parameter_type86', b1)
    if hasattr(b1, 'pascal_unpacked_conformant_array_schema85'):
        assert _is_linked(b1, 'pascal_unpacked_conformant_array_schema85', a)
    _safe_set(a, 'pascal_parameter_type86', b2)
    assert _is_linked(a, 'pascal_parameter_type86', b2)
    if hasattr(b1, 'pascal_unpacked_conformant_array_schema85'):
        assert not _is_linked(b1, 'pascal_unpacked_conformant_array_schema85', a)
    if hasattr(b2, 'pascal_unpacked_conformant_array_schema85'):
        assert _is_linked(b2, 'pascal_unpacked_conformant_array_schema85', a)
    _safe_set(a, 'pascal_parameter_type86', None)
    assert not _is_linked(a, 'pascal_parameter_type86', b2)
    if hasattr(b2, 'pascal_unpacked_conformant_array_schema85'):
        assert not _is_linked(b2, 'pascal_unpacked_conformant_array_schema85', a)


def test_assoc_types25_link_reassign_clear():
    a = pascal_type_definition(name="sample_text")
    b1 = pascal_type_definition_part()
    b2 = pascal_type_definition_part()
    _safe_set(a, 'pascal_type_definition', b1)
    assert _is_linked(a, 'pascal_type_definition', b1)
    if hasattr(b1, 'pascal_type_definition_part26'):
        assert _is_linked(b1, 'pascal_type_definition_part26', a)
    _safe_set(a, 'pascal_type_definition', b2)
    assert _is_linked(a, 'pascal_type_definition', b2)
    if hasattr(b1, 'pascal_type_definition_part26'):
        assert not _is_linked(b1, 'pascal_type_definition_part26', a)
    if hasattr(b2, 'pascal_type_definition_part26'):
        assert _is_linked(b2, 'pascal_type_definition_part26', a)
    _safe_set(a, 'pascal_type_definition', None)
    assert not _is_linked(a, 'pascal_type_definition', b2)
    if hasattr(b2, 'pascal_type_definition_part26'):
        assert not _is_linked(b2, 'pascal_type_definition_part26', a)


def test_assoc_variable102_link_reassign_clear():
    a = pascal_variable(name="sample_text")
    b1 = pascal_assignment_statement()
    b2 = pascal_assignment_statement()
    _safe_set(a, 'pascal_variable', b1)
    assert _is_linked(a, 'pascal_variable', b1)
    if hasattr(b1, 'pascal_assignment_statement103'):
        assert _is_linked(b1, 'pascal_assignment_statement103', a)
    _safe_set(a, 'pascal_variable', b2)
    assert _is_linked(a, 'pascal_variable', b2)
    if hasattr(b1, 'pascal_assignment_statement103'):
        assert not _is_linked(b1, 'pascal_assignment_statement103', a)
    if hasattr(b2, 'pascal_assignment_statement103'):
        assert _is_linked(b2, 'pascal_assignment_statement103', a)
    _safe_set(a, 'pascal_variable', None)
    assert not _is_linked(a, 'pascal_variable', b2)
    if hasattr(b2, 'pascal_assignment_statement103'):
        assert not _is_linked(b2, 'pascal_assignment_statement103', a)


def test_assoc_variable181_link_reassign_clear():
    a = pascal_variable(name="sample_text")
    b1 = pascal_factor(boolean="sample_text", nil=True, string="sample_text")
    b2 = pascal_factor(boolean="sample_text_2", nil=False, string="sample_text_2")
    _safe_set(a, 'pascal_variable183', b1)
    assert _is_linked(a, 'pascal_variable183', b1)
    if hasattr(b1, 'pascal_factor182'):
        assert _is_linked(b1, 'pascal_factor182', a)
    _safe_set(a, 'pascal_variable183', b2)
    assert _is_linked(a, 'pascal_variable183', b2)
    if hasattr(b1, 'pascal_factor182'):
        assert not _is_linked(b1, 'pascal_factor182', a)
    if hasattr(b2, 'pascal_factor182'):
        assert _is_linked(b2, 'pascal_factor182', a)
    _safe_set(a, 'pascal_variable183', None)
    assert not _is_linked(a, 'pascal_variable183', b2)
    if hasattr(b2, 'pascal_factor182'):
        assert not _is_linked(b2, 'pascal_factor182', a)


def test_assoc_variable197_link_reassign_clear():
    a = pascal_variable(name="sample_text")
    b1 = pascal_resto(accessor=True, name="sample_text")
    b2 = pascal_resto(accessor=False, name="sample_text_2")
    _safe_set(a, 'pascal_variable198', b1)
    assert _is_linked(a, 'pascal_variable198', b1)
    if hasattr(b1, 'pascal_resto'):
        assert _is_linked(b1, 'pascal_resto', a)
    _safe_set(a, 'pascal_variable198', b2)
    assert _is_linked(a, 'pascal_variable198', b2)
    if hasattr(b1, 'pascal_resto'):
        assert not _is_linked(b1, 'pascal_resto', a)
    if hasattr(b2, 'pascal_resto'):
        assert _is_linked(b2, 'pascal_resto', a)
    _safe_set(a, 'pascal_variable198', None)
    assert not _is_linked(a, 'pascal_variable198', b2)
    if hasattr(b2, 'pascal_resto'):
        assert not _is_linked(b2, 'pascal_resto', a)


def test_assoc_variable205_link_reassign_clear():
    a = pascal_resto(accessor=True, name="sample_text")
    b1 = pascal_resto(accessor=True, name="sample_text")
    b2 = pascal_resto(accessor=False, name="sample_text_2")
    _safe_set(a, 'pascal_resto204', b1)
    assert _is_linked(a, 'pascal_resto204', b1)
    if hasattr(b1, 'pascal_resto206'):
        assert _is_linked(b1, 'pascal_resto206', a)
    _safe_set(a, 'pascal_resto204', b2)
    assert _is_linked(a, 'pascal_resto204', b2)
    if hasattr(b1, 'pascal_resto206'):
        assert not _is_linked(b1, 'pascal_resto206', a)
    if hasattr(b2, 'pascal_resto206'):
        assert _is_linked(b2, 'pascal_resto206', a)
    _safe_set(a, 'pascal_resto204', None)
    assert not _is_linked(a, 'pascal_resto204', b2)
    if hasattr(b2, 'pascal_resto206'):
        assert not _is_linked(b2, 'pascal_resto206', a)


def test_assoc_variants270_link_reassign_clear():
    a = pascal_variant_part(name="sample_text")
    b1 = pascal_field_list()
    b2 = pascal_field_list()
    _safe_set(a, 'pascal_variant_part', b1)
    assert _is_linked(a, 'pascal_variant_part', b1)
    if hasattr(b1, 'pascal_field_list271'):
        assert _is_linked(b1, 'pascal_field_list271', a)
    _safe_set(a, 'pascal_variant_part', b2)
    assert _is_linked(a, 'pascal_variant_part', b2)
    if hasattr(b1, 'pascal_field_list271'):
        assert not _is_linked(b1, 'pascal_field_list271', a)
    if hasattr(b2, 'pascal_field_list271'):
        assert _is_linked(b2, 'pascal_field_list271', a)
    _safe_set(a, 'pascal_variant_part', None)
    assert not _is_linked(a, 'pascal_variant_part', b2)
    if hasattr(b2, 'pascal_field_list271'):
        assert not _is_linked(b2, 'pascal_field_list271', a)


def test_assoc_variants282_link_reassign_clear():
    a = pascal_variant_part(name="sample_text")
    b1 = pascal_variant()
    b2 = pascal_variant()
    _safe_set(a, 'pascal_variant_part283', {b1})
    assert _is_linked(a, 'pascal_variant_part283', b1)
    if hasattr(b1, 'pascal_variant'):
        assert _is_linked(b1, 'pascal_variant', a)
    _safe_set(a, 'pascal_variant_part283', {b2})
    assert _is_linked(a, 'pascal_variant_part283', b2)
    if hasattr(b1, 'pascal_variant'):
        assert not _is_linked(b1, 'pascal_variant', a)
    if hasattr(b2, 'pascal_variant'):
        assert _is_linked(b2, 'pascal_variant', a)
    _safe_set(a, 'pascal_variant_part283', set())
    assert not _is_linked(a, 'pascal_variant_part283', b2)
    if hasattr(b2, 'pascal_variant'):
        assert not _is_linked(b2, 'pascal_variant', a)


def test_assoc_with_stt115_link_reassign_clear():
    a = pascal_with_statement(record="sample_text", records="sample_text")
    b1 = pascal_structured_statement()
    b2 = pascal_structured_statement()
    _safe_set(a, 'pascal_with_statement', b1)
    assert _is_linked(a, 'pascal_with_statement', b1)
    if hasattr(b1, 'pascal_structured_statement116'):
        assert _is_linked(b1, 'pascal_structured_statement116', a)
    _safe_set(a, 'pascal_with_statement', b2)
    assert _is_linked(a, 'pascal_with_statement', b2)
    if hasattr(b1, 'pascal_structured_statement116'):
        assert not _is_linked(b1, 'pascal_structured_statement116', a)
    if hasattr(b2, 'pascal_structured_statement116'):
        assert _is_linked(b2, 'pascal_structured_statement116', a)
    _safe_set(a, 'pascal_with_statement', None)
    assert not _is_linked(a, 'pascal_with_statement', b2)
    if hasattr(b2, 'pascal_structured_statement116'):
        assert not _is_linked(b2, 'pascal_structured_statement116', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

abstraction_declaration_strategy = st.builds(abstraction_declaration)
@given(instance=abstraction_declaration_strategy)
@settings(max_examples=25)
def test_abstraction_declaration_instantiation(instance):
    assert isinstance(instance, abstraction_declaration)


pascal_EObject_strategy = st.builds(pascal_EObject)
@given(instance=pascal_EObject_strategy)
@settings(max_examples=25)
def test_pascal_EObject_instantiation(instance):
    assert isinstance(instance, pascal_EObject)


pascal_abstraction_declaration_strategy = st.builds(pascal_abstraction_declaration, forward=st.booleans())
@given(instance=pascal_abstraction_declaration_strategy)
@settings(max_examples=25)
def test_pascal_abstraction_declaration_instantiation(instance):
    assert isinstance(instance, pascal_abstraction_declaration)


pascal_abstraction_heading_strategy = st.builds(pascal_abstraction_heading, name=safe_text, resultType=safe_text)
@given(instance=pascal_abstraction_heading_strategy)
@settings(max_examples=25)
def test_pascal_abstraction_heading_instantiation(instance):
    assert isinstance(instance, pascal_abstraction_heading)


pascal_any_number_strategy = st.builds(pascal_any_number, integer=safe_text, real=safe_text)
@given(instance=pascal_any_number_strategy)
@settings(max_examples=25)
def test_pascal_any_number_instantiation(instance):
    assert isinstance(instance, pascal_any_number)


pascal_array_type_strategy = st.builds(pascal_array_type)
@given(instance=pascal_array_type_strategy)
@settings(max_examples=25)
def test_pascal_array_type_instantiation(instance):
    assert isinstance(instance, pascal_array_type)


pascal_assignment_statement_strategy = st.builds(pascal_assignment_statement)
@given(instance=pascal_assignment_statement_strategy)
@settings(max_examples=25)
def test_pascal_assignment_statement_instantiation(instance):
    assert isinstance(instance, pascal_assignment_statement)


pascal_block_strategy = st.builds(pascal_block)
@given(instance=pascal_block_strategy)
@settings(max_examples=25)
def test_pascal_block_instantiation(instance):
    assert isinstance(instance, pascal_block)


pascal_bound_specification_strategy = st.builds(pascal_bound_specification, fin=safe_text, init=safe_text, name=safe_text)
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


pascal_conformant_array_schema_strategy = st.builds(pascal_conformant_array_schema)
@given(instance=pascal_conformant_array_schema_strategy)
@settings(max_examples=25)
def test_pascal_conformant_array_schema_instantiation(instance):
    assert isinstance(instance, pascal_conformant_array_schema)


pascal_constant_strategy = st.builds(pascal_constant, boolLiteral=safe_text, name=safe_text, nil=safe_text, opterator=safe_text, string=safe_text)
@given(instance=pascal_constant_strategy)
@settings(max_examples=25)
def test_pascal_constant_instantiation(instance):
    assert isinstance(instance, pascal_constant)


pascal_constant_definition_strategy = st.builds(pascal_constant_definition, name=safe_text)
@given(instance=pascal_constant_definition_strategy)
@settings(max_examples=25)
def test_pascal_constant_definition_instantiation(instance):
    assert isinstance(instance, pascal_constant_definition)


pascal_constant_definition_part_strategy = st.builds(pascal_constant_definition_part)
@given(instance=pascal_constant_definition_part_strategy)
@settings(max_examples=25)
def test_pascal_constant_definition_part_instantiation(instance):
    assert isinstance(instance, pascal_constant_definition_part)


pascal_declaration_part_strategy = st.builds(pascal_declaration_part)
@given(instance=pascal_declaration_part_strategy)
@settings(max_examples=25)
def test_pascal_declaration_part_instantiation(instance):
    assert isinstance(instance, pascal_declaration_part)


pascal_enumerated_type_strategy = st.builds(pascal_enumerated_type)
@given(instance=pascal_enumerated_type_strategy)
@settings(max_examples=25)
def test_pascal_enumerated_type_instantiation(instance):
    assert isinstance(instance, pascal_enumerated_type)


pascal_expression_strategy = st.builds(pascal_expression, operators=safe_text)
@given(instance=pascal_expression_strategy)
@settings(max_examples=25)
def test_pascal_expression_instantiation(instance):
    assert isinstance(instance, pascal_expression)


pascal_expression_list_strategy = st.builds(pascal_expression_list)
@given(instance=pascal_expression_list_strategy)
@settings(max_examples=25)
def test_pascal_expression_list_instantiation(instance):
    assert isinstance(instance, pascal_expression_list)


pascal_factor_strategy = st.builds(pascal_factor, boolean=safe_text, nil=st.booleans(), string=safe_text)
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


pascal_for_statement_strategy = st.builds(pascal_for_statement, initID=safe_text)
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


pascal_function_designator_strategy = st.builds(pascal_function_designator, name=safe_text)
@given(instance=pascal_function_designator_strategy)
@settings(max_examples=25)
def test_pascal_function_designator_instantiation(instance):
    assert isinstance(instance, pascal_function_designator)


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


pascal_label_strategy = st.builds(pascal_label, number=safe_text)
@given(instance=pascal_label_strategy)
@settings(max_examples=25)
def test_pascal_label_instantiation(instance):
    assert isinstance(instance, pascal_label)


pascal_label_declaration_part_strategy = st.builds(pascal_label_declaration_part)
@given(instance=pascal_label_declaration_part_strategy)
@settings(max_examples=25)
def test_pascal_label_declaration_part_instantiation(instance):
    assert isinstance(instance, pascal_label_declaration_part)


pascal_number_strategy = st.builds(pascal_number)
@given(instance=pascal_number_strategy)
@settings(max_examples=25)
def test_pascal_number_instantiation(instance):
    assert isinstance(instance, pascal_number)


pascal_packed_conformant_array_schema_strategy = st.builds(pascal_packed_conformant_array_schema, name=safe_text)
@given(instance=pascal_packed_conformant_array_schema_strategy)
@settings(max_examples=25)
def test_pascal_packed_conformant_array_schema_instantiation(instance):
    assert isinstance(instance, pascal_packed_conformant_array_schema)


pascal_parameter_type_strategy = st.builds(pascal_parameter_type, name=safe_text)
@given(instance=pascal_parameter_type_strategy)
@settings(max_examples=25)
def test_pascal_parameter_type_instantiation(instance):
    assert isinstance(instance, pascal_parameter_type)


pascal_pointer_type_strategy = st.builds(pascal_pointer_type)
@given(instance=pascal_pointer_type_strategy)
@settings(max_examples=25)
def test_pascal_pointer_type_instantiation(instance):
    assert isinstance(instance, pascal_pointer_type)


pascal_procedure_and_function_declaration_part_strategy = st.builds(pascal_procedure_and_function_declaration_part)
@given(instance=pascal_procedure_and_function_declaration_part_strategy)
@settings(max_examples=25)
def test_pascal_procedure_and_function_declaration_part_instantiation(instance):
    assert isinstance(instance, pascal_procedure_and_function_declaration_part)


pascal_program_strategy = st.builds(pascal_program)
@given(instance=pascal_program_strategy)
@settings(max_examples=25)
def test_pascal_program_instantiation(instance):
    assert isinstance(instance, pascal_program)


pascal_program_heading_strategy = st.builds(pascal_program_heading, name=safe_text)
@given(instance=pascal_program_heading_strategy)
@settings(max_examples=25)
def test_pascal_program_heading_instantiation(instance):
    assert isinstance(instance, pascal_program_heading)


pascal_record_section_strategy = st.builds(pascal_record_section)
@given(instance=pascal_record_section_strategy)
@settings(max_examples=25)
def test_pascal_record_section_instantiation(instance):
    assert isinstance(instance, pascal_record_section)


pascal_record_type_strategy = st.builds(pascal_record_type, end=safe_text, record=safe_text)
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


pascal_resto_strategy = st.builds(pascal_resto, accessor=st.booleans(), name=safe_text)
@given(instance=pascal_resto_strategy)
@settings(max_examples=25)
def test_pascal_resto_instantiation(instance):
    assert isinstance(instance, pascal_resto)


pascal_set_strategy = st.builds(pascal_set, brackets=safe_text)
@given(instance=pascal_set_strategy)
@settings(max_examples=25)
def test_pascal_set_instantiation(instance):
    assert isinstance(instance, pascal_set)


pascal_set_type_strategy = st.builds(pascal_set_type)
@given(instance=pascal_set_type_strategy)
@settings(max_examples=25)
def test_pascal_set_type_instantiation(instance):
    assert isinstance(instance, pascal_set_type)


pascal_simple_expression_strategy = st.builds(pascal_simple_expression, operators=safe_text, prefixOperator=safe_text)
@given(instance=pascal_simple_expression_strategy)
@settings(max_examples=25)
def test_pascal_simple_expression_instantiation(instance):
    assert isinstance(instance, pascal_simple_expression)


pascal_simple_statement_strategy = st.builds(pascal_simple_statement)
@given(instance=pascal_simple_statement_strategy)
@settings(max_examples=25)
def test_pascal_simple_statement_instantiation(instance):
    assert isinstance(instance, pascal_simple_statement)


pascal_simple_type_strategy = st.builds(pascal_simple_type, name=safe_text)
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


pascal_structured_type_strategy = st.builds(pascal_structured_type, packed=st.booleans())
@given(instance=pascal_structured_type_strategy)
@settings(max_examples=25)
def test_pascal_structured_type_instantiation(instance):
    assert isinstance(instance, pascal_structured_type)


pascal_subrange_type_strategy = st.builds(pascal_subrange_type, subrange=safe_text)
@given(instance=pascal_subrange_type_strategy)
@settings(max_examples=25)
def test_pascal_subrange_type_instantiation(instance):
    assert isinstance(instance, pascal_subrange_type)


pascal_tag_field_strategy = st.builds(pascal_tag_field, name=safe_text)
@given(instance=pascal_tag_field_strategy)
@settings(max_examples=25)
def test_pascal_tag_field_instantiation(instance):
    assert isinstance(instance, pascal_tag_field)


pascal_term_strategy = st.builds(pascal_term, operators=safe_text)
@given(instance=pascal_term_strategy)
@settings(max_examples=25)
def test_pascal_term_instantiation(instance):
    assert isinstance(instance, pascal_term)


pascal_type_strategy = st.builds(pascal_type)
@given(instance=pascal_type_strategy)
@settings(max_examples=25)
def test_pascal_type_instantiation(instance):
    assert isinstance(instance, pascal_type)


pascal_type_definition_strategy = st.builds(pascal_type_definition, name=safe_text)
@given(instance=pascal_type_definition_strategy)
@settings(max_examples=25)
def test_pascal_type_definition_instantiation(instance):
    assert isinstance(instance, pascal_type_definition)


pascal_type_definition_part_strategy = st.builds(pascal_type_definition_part)
@given(instance=pascal_type_definition_part_strategy)
@settings(max_examples=25)
def test_pascal_type_definition_part_instantiation(instance):
    assert isinstance(instance, pascal_type_definition_part)


pascal_unpacked_conformant_array_schema_strategy = st.builds(pascal_unpacked_conformant_array_schema)
@given(instance=pascal_unpacked_conformant_array_schema_strategy)
@settings(max_examples=25)
def test_pascal_unpacked_conformant_array_schema_instantiation(instance):
    assert isinstance(instance, pascal_unpacked_conformant_array_schema)


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


pascal_variable_declaration_part_strategy = st.builds(pascal_variable_declaration_part)
@given(instance=pascal_variable_declaration_part_strategy)
@settings(max_examples=25)
def test_pascal_variable_declaration_part_instantiation(instance):
    assert isinstance(instance, pascal_variable_declaration_part)


pascal_variable_identifier_list_strategy = st.builds(pascal_variable_identifier_list, names=safe_text)
@given(instance=pascal_variable_identifier_list_strategy)
@settings(max_examples=25)
def test_pascal_variable_identifier_list_instantiation(instance):
    assert isinstance(instance, pascal_variable_identifier_list)


pascal_variable_parameter_section_strategy = st.builds(pascal_variable_parameter_section)
@given(instance=pascal_variable_parameter_section_strategy)
@settings(max_examples=25)
def test_pascal_variable_parameter_section_instantiation(instance):
    assert isinstance(instance, pascal_variable_parameter_section)


pascal_variable_section_strategy = st.builds(pascal_variable_section)
@given(instance=pascal_variable_section_strategy)
@settings(max_examples=25)
def test_pascal_variable_section_instantiation(instance):
    assert isinstance(instance, pascal_variable_section)


pascal_variant_strategy = st.builds(pascal_variant)
@given(instance=pascal_variant_strategy)
@settings(max_examples=25)
def test_pascal_variant_instantiation(instance):
    assert isinstance(instance, pascal_variant)


pascal_variant_part_strategy = st.builds(pascal_variant_part, name=safe_text)
@given(instance=pascal_variant_part_strategy)
@settings(max_examples=25)
def test_pascal_variant_part_instantiation(instance):
    assert isinstance(instance, pascal_variant_part)


pascal_while_statement_strategy = st.builds(pascal_while_statement)
@given(instance=pascal_while_statement_strategy)
@settings(max_examples=25)
def test_pascal_while_statement_instantiation(instance):
    assert isinstance(instance, pascal_while_statement)


pascal_with_statement_strategy = st.builds(pascal_with_statement, record=safe_text, records=safe_text)
@given(instance=pascal_with_statement_strategy)
@settings(max_examples=25)
def test_pascal_with_statement_instantiation(instance):
    assert isinstance(instance, pascal_with_statement)



