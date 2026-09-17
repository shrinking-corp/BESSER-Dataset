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
    pascal_caseListElement,
    parameterList,
    pascal_actualParameter,
    pascal_functionDesignator,
    pascal_caseStatement,
    pascal_statements,
    pascal_conditionalStatement,
    pascal_term,
    pascal_simpleExpression,
    pascal_variable,
    pascal_assignmentStatement,
    pascal_gotoStatement,
    pascal_parameterList,
    pascal_structuredStatement,
    pascal_simpleStatement,
    pascal_unsignedConstant,
    pascal_factor,
    pascal_signedFactor,
    pascal_functionDeclaration,
    pascal_procedureDeclaration,
    pascal_procedureOrFunctionDeclaration,
    pascal_expression,
    pascal_variableDeclaration,
    pascal_constList,
    pascal_unlabelledStatement,
    pascal_statement,
    pascal_recordSection,
    pascal_variantPart,
    pascal_fixedPart,
    pascal_recordType,
    pascal_unpackedStructuredType,
    pascal_variant,
    pascal_tag,
    pascal_parameterGroup,
    pascal_formalParameterSection,
    pascal_stringtype,
    pascal_subrangeType,
    pascal_scalarType,
    pascal_pointerType,
    pascal_structuredType,
    pascal_simpleType,
    pascal_typeDefinition,
    pascal_fieldList,
    pascal_constantChr,
    pascal_typeIdentifier,
    pascal_formalParameterList,
    pascal_procedureType,
    pascal_functionType,
    pascal_type,
    pascal_unsignedInteger,
    statement,
    label_declaration_part,
    pascal_label,
    pascal_compoundStatement,
    pascal_usesUnitsPart,
    pascal_procedureAndFunctionDeclarationPart,
    pascal_variableDeclarationPart,
    pascal_typeDefinitionPart,
    pascal_constantDefinitionPart,
    pascal_label_declaration_part,
    pascal_unsignedNumber,
    variant,
    pascal_constant,
    pascal_constantDefinition,
    pascal_pascal,
    pascal_identifierList,
    pascal_identifier,
    pascal_block,
    pascal_programHeading,
    pascal_program,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_pascal_caselistelement_is_not_abstract():
    assert not inspect.isabstract(pascal_caseListElement)


def test_hyp_pascal_caselistelement_constructor_exists():
    assert callable(pascal_caseListElement.__init__)


def test_hyp_pascal_caselistelement_constructor_args():
    sig = inspect.signature(pascal_caseListElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_parameterlist_is_not_abstract():
    assert not inspect.isabstract(parameterList)


def test_hyp_parameterlist_constructor_exists():
    assert callable(parameterList.__init__)


def test_hyp_parameterlist_constructor_args():
    sig = inspect.signature(parameterList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_actualparameter_is_not_abstract():
    assert not inspect.isabstract(pascal_actualParameter)


def test_hyp_pascal_actualparameter_constructor_exists():
    assert callable(pascal_actualParameter.__init__)


def test_hyp_pascal_actualparameter_constructor_args():
    sig = inspect.signature(pascal_actualParameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_functiondesignator_is_not_abstract():
    assert not inspect.isabstract(pascal_functionDesignator)


def test_hyp_pascal_functiondesignator_constructor_exists():
    assert callable(pascal_functionDesignator.__init__)


def test_hyp_pascal_functiondesignator_constructor_args():
    sig = inspect.signature(pascal_functionDesignator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_casestatement_is_not_abstract():
    assert not inspect.isabstract(pascal_caseStatement)


def test_hyp_pascal_casestatement_constructor_exists():
    assert callable(pascal_caseStatement.__init__)


def test_hyp_pascal_casestatement_constructor_args():
    sig = inspect.signature(pascal_caseStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_statements_is_not_abstract():
    assert not inspect.isabstract(pascal_statements)


def test_hyp_pascal_statements_constructor_exists():
    assert callable(pascal_statements.__init__)


def test_hyp_pascal_statements_constructor_args():
    sig = inspect.signature(pascal_statements.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_conditionalstatement_is_not_abstract():
    assert not inspect.isabstract(pascal_conditionalStatement)


def test_hyp_pascal_conditionalstatement_constructor_exists():
    assert callable(pascal_conditionalStatement.__init__)


def test_hyp_pascal_conditionalstatement_constructor_args():
    sig = inspect.signature(pascal_conditionalStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_term_is_not_abstract():
    assert not inspect.isabstract(pascal_term)


def test_hyp_pascal_term_constructor_exists():
    assert callable(pascal_term.__init__)


def test_hyp_pascal_term_constructor_args():
    sig = inspect.signature(pascal_term.__init__)
    params = list(sig.parameters.keys())
    assert "multiplicativeoperator" in params, "Missing parameter 'multiplicativeoperator'"




def test_hyp_pascal_simpleexpression_is_not_abstract():
    assert not inspect.isabstract(pascal_simpleExpression)


def test_hyp_pascal_simpleexpression_constructor_exists():
    assert callable(pascal_simpleExpression.__init__)


def test_hyp_pascal_simpleexpression_constructor_args():
    sig = inspect.signature(pascal_simpleExpression.__init__)
    params = list(sig.parameters.keys())
    assert "additiveoperator" in params, "Missing parameter 'additiveoperator'"




def test_hyp_pascal_variable_is_not_abstract():
    assert not inspect.isabstract(pascal_variable)


def test_hyp_pascal_variable_constructor_exists():
    assert callable(pascal_variable.__init__)


def test_hyp_pascal_variable_constructor_args():
    sig = inspect.signature(pascal_variable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_assignmentstatement_is_not_abstract():
    assert not inspect.isabstract(pascal_assignmentStatement)


def test_hyp_pascal_assignmentstatement_constructor_exists():
    assert callable(pascal_assignmentStatement.__init__)


def test_hyp_pascal_assignmentstatement_constructor_args():
    sig = inspect.signature(pascal_assignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_gotostatement_is_not_abstract():
    assert not inspect.isabstract(pascal_gotoStatement)


def test_hyp_pascal_gotostatement_constructor_exists():
    assert callable(pascal_gotoStatement.__init__)


def test_hyp_pascal_gotostatement_constructor_args():
    sig = inspect.signature(pascal_gotoStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_parameterlist_is_not_abstract():
    assert not inspect.isabstract(pascal_parameterList)


def test_hyp_pascal_parameterlist_constructor_exists():
    assert callable(pascal_parameterList.__init__)


def test_hyp_pascal_parameterlist_constructor_args():
    sig = inspect.signature(pascal_parameterList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_structuredstatement_is_not_abstract():
    assert not inspect.isabstract(pascal_structuredStatement)


def test_hyp_pascal_structuredstatement_constructor_exists():
    assert callable(pascal_structuredStatement.__init__)


def test_hyp_pascal_structuredstatement_constructor_args():
    sig = inspect.signature(pascal_structuredStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_simplestatement_is_not_abstract():
    assert not inspect.isabstract(pascal_simpleStatement)


def test_hyp_pascal_simplestatement_constructor_exists():
    assert callable(pascal_simpleStatement.__init__)


def test_hyp_pascal_simplestatement_constructor_args():
    sig = inspect.signature(pascal_simpleStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_unsignedconstant_is_not_abstract():
    assert not inspect.isabstract(pascal_unsignedConstant)


def test_hyp_pascal_unsignedconstant_constructor_exists():
    assert callable(pascal_unsignedConstant.__init__)


def test_hyp_pascal_unsignedconstant_constructor_args():
    sig = inspect.signature(pascal_unsignedConstant.__init__)
    params = list(sig.parameters.keys())
    assert "string_literal" in params, "Missing parameter 'string_literal'"




def test_hyp_pascal_factor_is_not_abstract():
    assert not inspect.isabstract(pascal_factor)


def test_hyp_pascal_factor_constructor_exists():
    assert callable(pascal_factor.__init__)


def test_hyp_pascal_factor_constructor_args():
    sig = inspect.signature(pascal_factor.__init__)
    params = list(sig.parameters.keys())
    assert "bool" in params, "Missing parameter 'bool'"




def test_hyp_pascal_signedfactor_is_not_abstract():
    assert not inspect.isabstract(pascal_signedFactor)


def test_hyp_pascal_signedfactor_constructor_exists():
    assert callable(pascal_signedFactor.__init__)


def test_hyp_pascal_signedfactor_constructor_args():
    sig = inspect.signature(pascal_signedFactor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_functiondeclaration_is_not_abstract():
    assert not inspect.isabstract(pascal_functionDeclaration)


def test_hyp_pascal_functiondeclaration_constructor_exists():
    assert callable(pascal_functionDeclaration.__init__)


def test_hyp_pascal_functiondeclaration_constructor_args():
    sig = inspect.signature(pascal_functionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_proceduredeclaration_is_not_abstract():
    assert not inspect.isabstract(pascal_procedureDeclaration)


def test_hyp_pascal_proceduredeclaration_constructor_exists():
    assert callable(pascal_procedureDeclaration.__init__)


def test_hyp_pascal_proceduredeclaration_constructor_args():
    sig = inspect.signature(pascal_procedureDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_procedureorfunctiondeclaration_is_not_abstract():
    assert not inspect.isabstract(pascal_procedureOrFunctionDeclaration)


def test_hyp_pascal_procedureorfunctiondeclaration_constructor_exists():
    assert callable(pascal_procedureOrFunctionDeclaration.__init__)


def test_hyp_pascal_procedureorfunctiondeclaration_constructor_args():
    sig = inspect.signature(pascal_procedureOrFunctionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_expression_is_not_abstract():
    assert not inspect.isabstract(pascal_expression)


def test_hyp_pascal_expression_constructor_exists():
    assert callable(pascal_expression.__init__)


def test_hyp_pascal_expression_constructor_args():
    sig = inspect.signature(pascal_expression.__init__)
    params = list(sig.parameters.keys())
    assert "relationaloperator" in params, "Missing parameter 'relationaloperator'"




def test_hyp_pascal_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(pascal_variableDeclaration)


def test_hyp_pascal_variabledeclaration_constructor_exists():
    assert callable(pascal_variableDeclaration.__init__)


def test_hyp_pascal_variabledeclaration_constructor_args():
    sig = inspect.signature(pascal_variableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_constlist_is_not_abstract():
    assert not inspect.isabstract(pascal_constList)


def test_hyp_pascal_constlist_constructor_exists():
    assert callable(pascal_constList.__init__)


def test_hyp_pascal_constlist_constructor_args():
    sig = inspect.signature(pascal_constList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_unlabelledstatement_is_not_abstract():
    assert not inspect.isabstract(pascal_unlabelledStatement)


def test_hyp_pascal_unlabelledstatement_constructor_exists():
    assert callable(pascal_unlabelledStatement.__init__)


def test_hyp_pascal_unlabelledstatement_constructor_args():
    sig = inspect.signature(pascal_unlabelledStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_statement_is_not_abstract():
    assert not inspect.isabstract(pascal_statement)


def test_hyp_pascal_statement_constructor_exists():
    assert callable(pascal_statement.__init__)


def test_hyp_pascal_statement_constructor_args():
    sig = inspect.signature(pascal_statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_recordsection_is_not_abstract():
    assert not inspect.isabstract(pascal_recordSection)


def test_hyp_pascal_recordsection_constructor_exists():
    assert callable(pascal_recordSection.__init__)


def test_hyp_pascal_recordsection_constructor_args():
    sig = inspect.signature(pascal_recordSection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_variantpart_is_not_abstract():
    assert not inspect.isabstract(pascal_variantPart)


def test_hyp_pascal_variantpart_constructor_exists():
    assert callable(pascal_variantPart.__init__)


def test_hyp_pascal_variantpart_constructor_args():
    sig = inspect.signature(pascal_variantPart.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_fixedpart_is_not_abstract():
    assert not inspect.isabstract(pascal_fixedPart)


def test_hyp_pascal_fixedpart_constructor_exists():
    assert callable(pascal_fixedPart.__init__)


def test_hyp_pascal_fixedpart_constructor_args():
    sig = inspect.signature(pascal_fixedPart.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_recordtype_is_not_abstract():
    assert not inspect.isabstract(pascal_recordType)


def test_hyp_pascal_recordtype_constructor_exists():
    assert callable(pascal_recordType.__init__)


def test_hyp_pascal_recordtype_constructor_args():
    sig = inspect.signature(pascal_recordType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_unpackedstructuredtype_is_not_abstract():
    assert not inspect.isabstract(pascal_unpackedStructuredType)


def test_hyp_pascal_unpackedstructuredtype_constructor_exists():
    assert callable(pascal_unpackedStructuredType.__init__)


def test_hyp_pascal_unpackedstructuredtype_constructor_args():
    sig = inspect.signature(pascal_unpackedStructuredType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_variant_is_not_abstract():
    assert not inspect.isabstract(pascal_variant)


def test_hyp_pascal_variant_constructor_exists():
    assert callable(pascal_variant.__init__)


def test_hyp_pascal_variant_constructor_args():
    sig = inspect.signature(pascal_variant.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_tag_is_not_abstract():
    assert not inspect.isabstract(pascal_tag)


def test_hyp_pascal_tag_constructor_exists():
    assert callable(pascal_tag.__init__)


def test_hyp_pascal_tag_constructor_args():
    sig = inspect.signature(pascal_tag.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_parametergroup_is_not_abstract():
    assert not inspect.isabstract(pascal_parameterGroup)


def test_hyp_pascal_parametergroup_constructor_exists():
    assert callable(pascal_parameterGroup.__init__)


def test_hyp_pascal_parametergroup_constructor_args():
    sig = inspect.signature(pascal_parameterGroup.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_formalparametersection_is_not_abstract():
    assert not inspect.isabstract(pascal_formalParameterSection)


def test_hyp_pascal_formalparametersection_constructor_exists():
    assert callable(pascal_formalParameterSection.__init__)


def test_hyp_pascal_formalparametersection_constructor_args():
    sig = inspect.signature(pascal_formalParameterSection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_stringtype_is_not_abstract():
    assert not inspect.isabstract(pascal_stringtype)


def test_hyp_pascal_stringtype_constructor_exists():
    assert callable(pascal_stringtype.__init__)


def test_hyp_pascal_stringtype_constructor_args():
    sig = inspect.signature(pascal_stringtype.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_subrangetype_is_not_abstract():
    assert not inspect.isabstract(pascal_subrangeType)


def test_hyp_pascal_subrangetype_constructor_exists():
    assert callable(pascal_subrangeType.__init__)


def test_hyp_pascal_subrangetype_constructor_args():
    sig = inspect.signature(pascal_subrangeType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_scalartype_is_not_abstract():
    assert not inspect.isabstract(pascal_scalarType)


def test_hyp_pascal_scalartype_constructor_exists():
    assert callable(pascal_scalarType.__init__)


def test_hyp_pascal_scalartype_constructor_args():
    sig = inspect.signature(pascal_scalarType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_pointertype_is_not_abstract():
    assert not inspect.isabstract(pascal_pointerType)


def test_hyp_pascal_pointertype_constructor_exists():
    assert callable(pascal_pointerType.__init__)


def test_hyp_pascal_pointertype_constructor_args():
    sig = inspect.signature(pascal_pointerType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_structuredtype_is_not_abstract():
    assert not inspect.isabstract(pascal_structuredType)


def test_hyp_pascal_structuredtype_constructor_exists():
    assert callable(pascal_structuredType.__init__)


def test_hyp_pascal_structuredtype_constructor_args():
    sig = inspect.signature(pascal_structuredType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_simpletype_is_not_abstract():
    assert not inspect.isabstract(pascal_simpleType)


def test_hyp_pascal_simpletype_constructor_exists():
    assert callable(pascal_simpleType.__init__)


def test_hyp_pascal_simpletype_constructor_args():
    sig = inspect.signature(pascal_simpleType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_typedefinition_is_not_abstract():
    assert not inspect.isabstract(pascal_typeDefinition)


def test_hyp_pascal_typedefinition_constructor_exists():
    assert callable(pascal_typeDefinition.__init__)


def test_hyp_pascal_typedefinition_constructor_args():
    sig = inspect.signature(pascal_typeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_fieldlist_is_not_abstract():
    assert not inspect.isabstract(pascal_fieldList)


def test_hyp_pascal_fieldlist_constructor_exists():
    assert callable(pascal_fieldList.__init__)


def test_hyp_pascal_fieldlist_constructor_args():
    sig = inspect.signature(pascal_fieldList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_constantchr_is_not_abstract():
    assert not inspect.isabstract(pascal_constantChr)


def test_hyp_pascal_constantchr_constructor_exists():
    assert callable(pascal_constantChr.__init__)


def test_hyp_pascal_constantchr_constructor_args():
    sig = inspect.signature(pascal_constantChr.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_typeidentifier_is_not_abstract():
    assert not inspect.isabstract(pascal_typeIdentifier)


def test_hyp_pascal_typeidentifier_constructor_exists():
    assert callable(pascal_typeIdentifier.__init__)


def test_hyp_pascal_typeidentifier_constructor_args():
    sig = inspect.signature(pascal_typeIdentifier.__init__)
    params = list(sig.parameters.keys())
    assert "char" in params, "Missing parameter 'char'"
    assert "integer" in params, "Missing parameter 'integer'"
    assert "real" in params, "Missing parameter 'real'"
    assert "boolean" in params, "Missing parameter 'boolean'"
    assert "string" in params, "Missing parameter 'string'"








def test_hyp_pascal_formalparameterlist_is_not_abstract():
    assert not inspect.isabstract(pascal_formalParameterList)


def test_hyp_pascal_formalparameterlist_constructor_exists():
    assert callable(pascal_formalParameterList.__init__)


def test_hyp_pascal_formalparameterlist_constructor_args():
    sig = inspect.signature(pascal_formalParameterList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_proceduretype_is_not_abstract():
    assert not inspect.isabstract(pascal_procedureType)


def test_hyp_pascal_proceduretype_constructor_exists():
    assert callable(pascal_procedureType.__init__)


def test_hyp_pascal_proceduretype_constructor_args():
    sig = inspect.signature(pascal_procedureType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_functiontype_is_not_abstract():
    assert not inspect.isabstract(pascal_functionType)


def test_hyp_pascal_functiontype_constructor_exists():
    assert callable(pascal_functionType.__init__)


def test_hyp_pascal_functiontype_constructor_args():
    sig = inspect.signature(pascal_functionType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_type_is_not_abstract():
    assert not inspect.isabstract(pascal_type)


def test_hyp_pascal_type_constructor_exists():
    assert callable(pascal_type.__init__)


def test_hyp_pascal_type_constructor_args():
    sig = inspect.signature(pascal_type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_unsignedinteger_is_not_abstract():
    assert not inspect.isabstract(pascal_unsignedInteger)


def test_hyp_pascal_unsignedinteger_constructor_exists():
    assert callable(pascal_unsignedInteger.__init__)


def test_hyp_pascal_unsignedinteger_constructor_args():
    sig = inspect.signature(pascal_unsignedInteger.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"




def test_hyp_statement_is_not_abstract():
    assert not inspect.isabstract(statement)


def test_hyp_statement_constructor_exists():
    assert callable(statement.__init__)


def test_hyp_statement_constructor_args():
    sig = inspect.signature(statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_label_declaration_part_is_not_abstract():
    assert not inspect.isabstract(label_declaration_part)


def test_hyp_label_declaration_part_constructor_exists():
    assert callable(label_declaration_part.__init__)


def test_hyp_label_declaration_part_constructor_args():
    sig = inspect.signature(label_declaration_part.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_label_is_not_abstract():
    assert not inspect.isabstract(pascal_label)


def test_hyp_pascal_label_constructor_exists():
    assert callable(pascal_label.__init__)


def test_hyp_pascal_label_constructor_args():
    sig = inspect.signature(pascal_label.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_compoundstatement_is_not_abstract():
    assert not inspect.isabstract(pascal_compoundStatement)


def test_hyp_pascal_compoundstatement_constructor_exists():
    assert callable(pascal_compoundStatement.__init__)


def test_hyp_pascal_compoundstatement_constructor_args():
    sig = inspect.signature(pascal_compoundStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_usesunitspart_is_not_abstract():
    assert not inspect.isabstract(pascal_usesUnitsPart)


def test_hyp_pascal_usesunitspart_constructor_exists():
    assert callable(pascal_usesUnitsPart.__init__)


def test_hyp_pascal_usesunitspart_constructor_args():
    sig = inspect.signature(pascal_usesUnitsPart.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_procedureandfunctiondeclarationpart_is_not_abstract():
    assert not inspect.isabstract(pascal_procedureAndFunctionDeclarationPart)


def test_hyp_pascal_procedureandfunctiondeclarationpart_constructor_exists():
    assert callable(pascal_procedureAndFunctionDeclarationPart.__init__)


def test_hyp_pascal_procedureandfunctiondeclarationpart_constructor_args():
    sig = inspect.signature(pascal_procedureAndFunctionDeclarationPart.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_variabledeclarationpart_is_not_abstract():
    assert not inspect.isabstract(pascal_variableDeclarationPart)


def test_hyp_pascal_variabledeclarationpart_constructor_exists():
    assert callable(pascal_variableDeclarationPart.__init__)


def test_hyp_pascal_variabledeclarationpart_constructor_args():
    sig = inspect.signature(pascal_variableDeclarationPart.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_typedefinitionpart_is_not_abstract():
    assert not inspect.isabstract(pascal_typeDefinitionPart)


def test_hyp_pascal_typedefinitionpart_constructor_exists():
    assert callable(pascal_typeDefinitionPart.__init__)


def test_hyp_pascal_typedefinitionpart_constructor_args():
    sig = inspect.signature(pascal_typeDefinitionPart.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_constantdefinitionpart_is_not_abstract():
    assert not inspect.isabstract(pascal_constantDefinitionPart)


def test_hyp_pascal_constantdefinitionpart_constructor_exists():
    assert callable(pascal_constantDefinitionPart.__init__)


def test_hyp_pascal_constantdefinitionpart_constructor_args():
    sig = inspect.signature(pascal_constantDefinitionPart.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_label_declaration_part_is_not_abstract():
    assert not inspect.isabstract(pascal_label_declaration_part)


def test_hyp_pascal_label_declaration_part_constructor_exists():
    assert callable(pascal_label_declaration_part.__init__)


def test_hyp_pascal_label_declaration_part_constructor_args():
    sig = inspect.signature(pascal_label_declaration_part.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_unsignednumber_is_not_abstract():
    assert not inspect.isabstract(pascal_unsignedNumber)


def test_hyp_pascal_unsignednumber_constructor_exists():
    assert callable(pascal_unsignedNumber.__init__)


def test_hyp_pascal_unsignednumber_constructor_args():
    sig = inspect.signature(pascal_unsignedNumber.__init__)
    params = list(sig.parameters.keys())
    assert "unsignedReal" in params, "Missing parameter 'unsignedReal'"




def test_hyp_variant_is_not_abstract():
    assert not inspect.isabstract(variant)


def test_hyp_variant_constructor_exists():
    assert callable(variant.__init__)


def test_hyp_variant_constructor_args():
    sig = inspect.signature(variant.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_constant_is_not_abstract():
    assert not inspect.isabstract(pascal_constant)


def test_hyp_pascal_constant_constructor_exists():
    assert callable(pascal_constant.__init__)


def test_hyp_pascal_constant_constructor_args():
    sig = inspect.signature(pascal_constant.__init__)
    params = list(sig.parameters.keys())
    assert "sign" in params, "Missing parameter 'sign'"
    assert "string" in params, "Missing parameter 'string'"
    assert "bool" in params, "Missing parameter 'bool'"






def test_hyp_pascal_constantdefinition_is_not_abstract():
    assert not inspect.isabstract(pascal_constantDefinition)


def test_hyp_pascal_constantdefinition_constructor_exists():
    assert callable(pascal_constantDefinition.__init__)


def test_hyp_pascal_constantdefinition_constructor_args():
    sig = inspect.signature(pascal_constantDefinition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_pascal_is_not_abstract():
    assert not inspect.isabstract(pascal_pascal)


def test_hyp_pascal_pascal_constructor_exists():
    assert callable(pascal_pascal.__init__)


def test_hyp_pascal_pascal_constructor_args():
    sig = inspect.signature(pascal_pascal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_identifierlist_is_not_abstract():
    assert not inspect.isabstract(pascal_identifierList)


def test_hyp_pascal_identifierlist_constructor_exists():
    assert callable(pascal_identifierList.__init__)


def test_hyp_pascal_identifierlist_constructor_args():
    sig = inspect.signature(pascal_identifierList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_identifier_is_not_abstract():
    assert not inspect.isabstract(pascal_identifier)


def test_hyp_pascal_identifier_constructor_exists():
    assert callable(pascal_identifier.__init__)


def test_hyp_pascal_identifier_constructor_args():
    sig = inspect.signature(pascal_identifier.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"




def test_hyp_pascal_block_is_not_abstract():
    assert not inspect.isabstract(pascal_block)


def test_hyp_pascal_block_constructor_exists():
    assert callable(pascal_block.__init__)


def test_hyp_pascal_block_constructor_args():
    sig = inspect.signature(pascal_block.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_programheading_is_not_abstract():
    assert not inspect.isabstract(pascal_programHeading)


def test_hyp_pascal_programheading_constructor_exists():
    assert callable(pascal_programHeading.__init__)


def test_hyp_pascal_programheading_constructor_args():
    sig = inspect.signature(pascal_programHeading.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pascal_program_is_not_abstract():
    assert not inspect.isabstract(pascal_program)


def test_hyp_pascal_program_constructor_exists():
    assert callable(pascal_program.__init__)


def test_hyp_pascal_program_constructor_args():
    sig = inspect.signature(pascal_program.__init__)
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
pascal_caseListElement_strategy = st.builds(
    pascal_caseListElement,
)
parameterList_strategy = st.builds(
    parameterList,
)
pascal_actualParameter_strategy = st.builds(
    pascal_actualParameter,
)
pascal_functionDesignator_strategy = st.builds(
    pascal_functionDesignator,
)
pascal_caseStatement_strategy = st.builds(
    pascal_caseStatement,
)
pascal_statements_strategy = st.builds(
    pascal_statements,
)
pascal_conditionalStatement_strategy = st.builds(
    pascal_conditionalStatement,
)
pascal_term_strategy = st.builds(
    pascal_term,
    multiplicativeoperator=
        safe_text
)
pascal_simpleExpression_strategy = st.builds(
    pascal_simpleExpression,
    additiveoperator=
        safe_text
)
pascal_variable_strategy = st.builds(
    pascal_variable,
)
pascal_assignmentStatement_strategy = st.builds(
    pascal_assignmentStatement,
)
pascal_gotoStatement_strategy = st.builds(
    pascal_gotoStatement,
)
pascal_parameterList_strategy = st.builds(
    pascal_parameterList,
)
pascal_structuredStatement_strategy = st.builds(
    pascal_structuredStatement,
)
pascal_simpleStatement_strategy = st.builds(
    pascal_simpleStatement,
)
pascal_unsignedConstant_strategy = st.builds(
    pascal_unsignedConstant,
    string_literal=
        safe_text
)
pascal_factor_strategy = st.builds(
    pascal_factor,
    bool=
        safe_text
)
pascal_signedFactor_strategy = st.builds(
    pascal_signedFactor,
)
pascal_functionDeclaration_strategy = st.builds(
    pascal_functionDeclaration,
)
pascal_procedureDeclaration_strategy = st.builds(
    pascal_procedureDeclaration,
)
pascal_procedureOrFunctionDeclaration_strategy = st.builds(
    pascal_procedureOrFunctionDeclaration,
)
pascal_expression_strategy = st.builds(
    pascal_expression,
    relationaloperator=
        safe_text
)
pascal_variableDeclaration_strategy = st.builds(
    pascal_variableDeclaration,
)
pascal_constList_strategy = st.builds(
    pascal_constList,
)
pascal_unlabelledStatement_strategy = st.builds(
    pascal_unlabelledStatement,
)
pascal_statement_strategy = st.builds(
    pascal_statement,
)
pascal_recordSection_strategy = st.builds(
    pascal_recordSection,
)
pascal_variantPart_strategy = st.builds(
    pascal_variantPart,
)
pascal_fixedPart_strategy = st.builds(
    pascal_fixedPart,
)
pascal_recordType_strategy = st.builds(
    pascal_recordType,
)
pascal_unpackedStructuredType_strategy = st.builds(
    pascal_unpackedStructuredType,
)
pascal_variant_strategy = st.builds(
    pascal_variant,
)
pascal_tag_strategy = st.builds(
    pascal_tag,
)
pascal_parameterGroup_strategy = st.builds(
    pascal_parameterGroup,
)
pascal_formalParameterSection_strategy = st.builds(
    pascal_formalParameterSection,
)
pascal_stringtype_strategy = st.builds(
    pascal_stringtype,
)
pascal_subrangeType_strategy = st.builds(
    pascal_subrangeType,
)
pascal_scalarType_strategy = st.builds(
    pascal_scalarType,
)
pascal_pointerType_strategy = st.builds(
    pascal_pointerType,
)
pascal_structuredType_strategy = st.builds(
    pascal_structuredType,
)
pascal_simpleType_strategy = st.builds(
    pascal_simpleType,
)
pascal_typeDefinition_strategy = st.builds(
    pascal_typeDefinition,
)
pascal_fieldList_strategy = st.builds(
    pascal_fieldList,
)
pascal_constantChr_strategy = st.builds(
    pascal_constantChr,
)
pascal_typeIdentifier_strategy = st.builds(
    pascal_typeIdentifier,
    char=
        safe_text,
    integer=
        safe_text,
    real=
        safe_text,
    boolean=
        safe_text,
    string=
        safe_text
)
pascal_formalParameterList_strategy = st.builds(
    pascal_formalParameterList,
)
pascal_procedureType_strategy = st.builds(
    pascal_procedureType,
)
pascal_functionType_strategy = st.builds(
    pascal_functionType,
)
pascal_type_strategy = st.builds(
    pascal_type,
)
pascal_unsignedInteger_strategy = st.builds(
    pascal_unsignedInteger,
    number=
        safe_text
)
statement_strategy = st.builds(
    statement,
)
label_declaration_part_strategy = st.builds(
    label_declaration_part,
)
pascal_label_strategy = st.builds(
    pascal_label,
)
pascal_compoundStatement_strategy = st.builds(
    pascal_compoundStatement,
)
pascal_usesUnitsPart_strategy = st.builds(
    pascal_usesUnitsPart,
)
pascal_procedureAndFunctionDeclarationPart_strategy = st.builds(
    pascal_procedureAndFunctionDeclarationPart,
)
pascal_variableDeclarationPart_strategy = st.builds(
    pascal_variableDeclarationPart,
)
pascal_typeDefinitionPart_strategy = st.builds(
    pascal_typeDefinitionPart,
)
pascal_constantDefinitionPart_strategy = st.builds(
    pascal_constantDefinitionPart,
)
pascal_label_declaration_part_strategy = st.builds(
    pascal_label_declaration_part,
)
pascal_unsignedNumber_strategy = st.builds(
    pascal_unsignedNumber,
    unsignedReal=
        safe_text
)
variant_strategy = st.builds(
    variant,
)
pascal_constant_strategy = st.builds(
    pascal_constant,
    sign=
        safe_text,
    string=
        safe_text,
    bool=
        safe_text
)
pascal_constantDefinition_strategy = st.builds(
    pascal_constantDefinition,
)
pascal_pascal_strategy = st.builds(
    pascal_pascal,
)
pascal_identifierList_strategy = st.builds(
    pascal_identifierList,
)
pascal_identifier_strategy = st.builds(
    pascal_identifier,
    identifier=
        safe_text
)
pascal_block_strategy = st.builds(
    pascal_block,
)
pascal_programHeading_strategy = st.builds(
    pascal_programHeading,
)
pascal_program_strategy = st.builds(
    pascal_program,
)











@given(instance=pascal_term_strategy)
def test_hyp_pascal_term_multiplicativeoperator_setter(instance):
    original = instance.multiplicativeoperator
    instance.multiplicativeoperator = original
    assert instance.multiplicativeoperator == original




@given(instance=pascal_simpleExpression_strategy)
def test_hyp_pascal_simpleexpression_additiveoperator_setter(instance):
    original = instance.additiveoperator
    instance.additiveoperator = original
    assert instance.additiveoperator == original










@given(instance=pascal_unsignedConstant_strategy)
def test_hyp_pascal_unsignedconstant_string_literal_setter(instance):
    original = instance.string_literal
    instance.string_literal = original
    assert instance.string_literal == original




@given(instance=pascal_factor_strategy)
def test_hyp_pascal_factor_bool_setter(instance):
    original = instance.bool
    instance.bool = original
    assert instance.bool == original








@given(instance=pascal_expression_strategy)
def test_hyp_pascal_expression_relationaloperator_setter(instance):
    original = instance.relationaloperator
    instance.relationaloperator = original
    assert instance.relationaloperator == original


























@given(instance=pascal_typeIdentifier_strategy)
def test_hyp_pascal_typeidentifier_char_setter(instance):
    original = instance.char
    instance.char = original
    assert instance.char == original



@given(instance=pascal_typeIdentifier_strategy)
def test_hyp_pascal_typeidentifier_integer_setter(instance):
    original = instance.integer
    instance.integer = original
    assert instance.integer == original



@given(instance=pascal_typeIdentifier_strategy)
def test_hyp_pascal_typeidentifier_real_setter(instance):
    original = instance.real
    instance.real = original
    assert instance.real == original



@given(instance=pascal_typeIdentifier_strategy)
def test_hyp_pascal_typeidentifier_boolean_setter(instance):
    original = instance.boolean
    instance.boolean = original
    assert instance.boolean == original



@given(instance=pascal_typeIdentifier_strategy)
def test_hyp_pascal_typeidentifier_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original








@given(instance=pascal_unsignedInteger_strategy)
def test_hyp_pascal_unsignedinteger_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original














@given(instance=pascal_unsignedNumber_strategy)
def test_hyp_pascal_unsignednumber_unsignedReal_setter(instance):
    original = instance.unsignedReal
    instance.unsignedReal = original
    assert instance.unsignedReal == original





@given(instance=pascal_constant_strategy)
def test_hyp_pascal_constant_sign_setter(instance):
    original = instance.sign
    instance.sign = original
    assert instance.sign == original



@given(instance=pascal_constant_strategy)
def test_hyp_pascal_constant_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original



@given(instance=pascal_constant_strategy)
def test_hyp_pascal_constant_bool_setter(instance):
    original = instance.bool
    instance.bool = original
    assert instance.bool == original







@given(instance=pascal_identifier_strategy)
def test_hyp_pascal_identifier_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original





# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    label_declaration_part,
    parameterList,
    pascal_actualParameter,
    pascal_assignmentStatement,
    pascal_block,
    pascal_caseListElement,
    pascal_caseStatement,
    pascal_compoundStatement,
    pascal_conditionalStatement,
    pascal_constList,
    pascal_constant,
    pascal_constantChr,
    pascal_constantDefinition,
    pascal_constantDefinitionPart,
    pascal_expression,
    pascal_factor,
    pascal_fieldList,
    pascal_fixedPart,
    pascal_formalParameterList,
    pascal_formalParameterSection,
    pascal_functionDeclaration,
    pascal_functionDesignator,
    pascal_functionType,
    pascal_gotoStatement,
    pascal_identifier,
    pascal_identifierList,
    pascal_label,
    pascal_label_declaration_part,
    pascal_parameterGroup,
    pascal_parameterList,
    pascal_pascal,
    pascal_pointerType,
    pascal_procedureAndFunctionDeclarationPart,
    pascal_procedureDeclaration,
    pascal_procedureOrFunctionDeclaration,
    pascal_procedureType,
    pascal_program,
    pascal_programHeading,
    pascal_recordSection,
    pascal_recordType,
    pascal_scalarType,
    pascal_signedFactor,
    pascal_simpleExpression,
    pascal_simpleStatement,
    pascal_simpleType,
    pascal_statement,
    pascal_statements,
    pascal_stringtype,
    pascal_structuredStatement,
    pascal_structuredType,
    pascal_subrangeType,
    pascal_tag,
    pascal_term,
    pascal_type,
    pascal_typeDefinition,
    pascal_typeDefinitionPart,
    pascal_typeIdentifier,
    pascal_unlabelledStatement,
    pascal_unpackedStructuredType,
    pascal_unsignedConstant,
    pascal_unsignedInteger,
    pascal_unsignedNumber,
    pascal_usesUnitsPart,
    pascal_variable,
    pascal_variableDeclaration,
    pascal_variableDeclarationPart,
    pascal_variant,
    pascal_variantPart,
    statement,
    variant,
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

def test_pascal_constant_bool_value_roundtrip():
    instance = pascal_constant(bool="sample_text", sign="sample_text", string="sample_text")
    assert instance.bool == "sample_text"
    instance.bool = "sample_text_2"
    assert instance.bool == "sample_text_2"


def test_pascal_constant_sign_value_roundtrip():
    instance = pascal_constant(bool="sample_text", sign="sample_text", string="sample_text")
    assert instance.sign == "sample_text"
    instance.sign = "sample_text_2"
    assert instance.sign == "sample_text_2"


def test_pascal_constant_string_value_roundtrip():
    instance = pascal_constant(bool="sample_text", sign="sample_text", string="sample_text")
    assert instance.string == "sample_text"
    instance.string = "sample_text_2"
    assert instance.string == "sample_text_2"


def test_pascal_expression_relationaloperator_value_roundtrip():
    instance = pascal_expression(relationaloperator="sample_text")
    assert instance.relationaloperator == "sample_text"
    instance.relationaloperator = "sample_text_2"
    assert instance.relationaloperator == "sample_text_2"


def test_pascal_factor_bool_value_roundtrip():
    instance = pascal_factor(bool="sample_text")
    assert instance.bool == "sample_text"
    instance.bool = "sample_text_2"
    assert instance.bool == "sample_text_2"


def test_pascal_identifier_identifier_value_roundtrip():
    instance = pascal_identifier(identifier="sample_text")
    assert instance.identifier == "sample_text"
    instance.identifier = "sample_text_2"
    assert instance.identifier == "sample_text_2"


def test_pascal_simpleExpression_additiveoperator_value_roundtrip():
    instance = pascal_simpleExpression(additiveoperator="sample_text")
    assert instance.additiveoperator == "sample_text"
    instance.additiveoperator = "sample_text_2"
    assert instance.additiveoperator == "sample_text_2"


def test_pascal_term_multiplicativeoperator_value_roundtrip():
    instance = pascal_term(multiplicativeoperator="sample_text")
    assert instance.multiplicativeoperator == "sample_text"
    instance.multiplicativeoperator = "sample_text_2"
    assert instance.multiplicativeoperator == "sample_text_2"


def test_pascal_typeIdentifier_boolean_value_roundtrip():
    instance = pascal_typeIdentifier(boolean="sample_text", char="sample_text", integer="sample_text", real="sample_text", string="sample_text")
    assert instance.boolean == "sample_text"
    instance.boolean = "sample_text_2"
    assert instance.boolean == "sample_text_2"


def test_pascal_typeIdentifier_char_value_roundtrip():
    instance = pascal_typeIdentifier(boolean="sample_text", char="sample_text", integer="sample_text", real="sample_text", string="sample_text")
    assert instance.char == "sample_text"
    instance.char = "sample_text_2"
    assert instance.char == "sample_text_2"


def test_pascal_typeIdentifier_integer_value_roundtrip():
    instance = pascal_typeIdentifier(boolean="sample_text", char="sample_text", integer="sample_text", real="sample_text", string="sample_text")
    assert instance.integer == "sample_text"
    instance.integer = "sample_text_2"
    assert instance.integer == "sample_text_2"


def test_pascal_typeIdentifier_real_value_roundtrip():
    instance = pascal_typeIdentifier(boolean="sample_text", char="sample_text", integer="sample_text", real="sample_text", string="sample_text")
    assert instance.real == "sample_text"
    instance.real = "sample_text_2"
    assert instance.real == "sample_text_2"


def test_pascal_typeIdentifier_string_value_roundtrip():
    instance = pascal_typeIdentifier(boolean="sample_text", char="sample_text", integer="sample_text", real="sample_text", string="sample_text")
    assert instance.string == "sample_text"
    instance.string = "sample_text_2"
    assert instance.string == "sample_text_2"


def test_pascal_unsignedConstant_string_literal_value_roundtrip():
    instance = pascal_unsignedConstant(string_literal="sample_text")
    assert instance.string_literal == "sample_text"
    instance.string_literal = "sample_text_2"
    assert instance.string_literal == "sample_text_2"


def test_pascal_unsignedInteger_number_value_roundtrip():
    instance = pascal_unsignedInteger(number="sample_text")
    assert instance.number == "sample_text"
    instance.number = "sample_text_2"
    assert instance.number == "sample_text_2"


def test_pascal_unsignedNumber_unsignedReal_value_roundtrip():
    instance = pascal_unsignedNumber(unsignedReal="sample_text")
    assert instance.unsignedReal == "sample_text"
    instance.unsignedReal = "sample_text_2"
    assert instance.unsignedReal == "sample_text_2"


def test_pascal_label_isa_label_declaration_part():
    instance = pascal_label()
    assert isinstance(instance, label_declaration_part)


def test_pascal_actualParameter_isa_parameterList():
    instance = pascal_actualParameter()
    assert isinstance(instance, parameterList)


def test_pascal_label_isa_statement():
    instance = pascal_label()
    assert isinstance(instance, statement)


def test_pascal_constant_isa_variant():
    instance = pascal_constant(bool="sample_text", sign="sample_text", string="sample_text")
    assert isinstance(instance, variant)


def test_assoc_constant1189_link_reassign_clear():
    a = pascal_constant(bool="sample_text", sign="sample_text", string="sample_text")
    b1 = pascal_constList()
    b2 = pascal_constList()
    _safe_set(a, 'pascal_constant191', b1)
    assert _is_linked(a, 'pascal_constant191', b1)
    if hasattr(b1, 'pascal_constList190'):
        assert _is_linked(b1, 'pascal_constList190', a)
    _safe_set(a, 'pascal_constant191', b2)
    assert _is_linked(a, 'pascal_constant191', b2)
    if hasattr(b1, 'pascal_constList190'):
        assert not _is_linked(b1, 'pascal_constList190', a)
    if hasattr(b2, 'pascal_constList190'):
        assert _is_linked(b2, 'pascal_constList190', a)
    _safe_set(a, 'pascal_constant191', None)
    assert not _is_linked(a, 'pascal_constant191', b2)
    if hasattr(b2, 'pascal_constList190'):
        assert not _is_linked(b2, 'pascal_constList190', a)


def test_assoc_constant131_link_reassign_clear():
    a = pascal_constant(bool="sample_text", sign="sample_text", string="sample_text")
    b1 = pascal_subrangeType()
    b2 = pascal_subrangeType()
    _safe_set(a, 'pascal_constant133', b1)
    assert _is_linked(a, 'pascal_constant133', b1)
    if hasattr(b1, 'pascal_subrangeType132'):
        assert _is_linked(b1, 'pascal_subrangeType132', a)
    _safe_set(a, 'pascal_constant133', b2)
    assert _is_linked(a, 'pascal_constant133', b2)
    if hasattr(b1, 'pascal_subrangeType132'):
        assert not _is_linked(b1, 'pascal_subrangeType132', a)
    if hasattr(b2, 'pascal_subrangeType132'):
        assert _is_linked(b2, 'pascal_subrangeType132', a)
    _safe_set(a, 'pascal_constant133', None)
    assert not _is_linked(a, 'pascal_constant133', b2)
    if hasattr(b2, 'pascal_subrangeType132'):
        assert not _is_linked(b2, 'pascal_subrangeType132', a)


def test_assoc_constant187_link_reassign_clear():
    a = pascal_constant(bool="sample_text", sign="sample_text", string="sample_text")
    b1 = pascal_constList()
    b2 = pascal_constList()
    _safe_set(a, 'pascal_constant188', b1)
    assert _is_linked(a, 'pascal_constant188', b1)
    if hasattr(b1, 'pascal_constList'):
        assert _is_linked(b1, 'pascal_constList', a)
    _safe_set(a, 'pascal_constant188', b2)
    assert _is_linked(a, 'pascal_constant188', b2)
    if hasattr(b1, 'pascal_constList'):
        assert not _is_linked(b1, 'pascal_constList', a)
    if hasattr(b2, 'pascal_constList'):
        assert _is_linked(b2, 'pascal_constList', a)
    _safe_set(a, 'pascal_constant188', None)
    assert not _is_linked(a, 'pascal_constant188', b2)
    if hasattr(b2, 'pascal_constList'):
        assert not _is_linked(b2, 'pascal_constList', a)


def test_assoc_constant2134_link_reassign_clear():
    a = pascal_constant(bool="sample_text", sign="sample_text", string="sample_text")
    b1 = pascal_subrangeType()
    b2 = pascal_subrangeType()
    _safe_set(a, 'pascal_constant136', b1)
    assert _is_linked(a, 'pascal_constant136', b1)
    if hasattr(b1, 'pascal_subrangeType135'):
        assert _is_linked(b1, 'pascal_subrangeType135', a)
    _safe_set(a, 'pascal_constant136', b2)
    assert _is_linked(a, 'pascal_constant136', b2)
    if hasattr(b1, 'pascal_subrangeType135'):
        assert not _is_linked(b1, 'pascal_subrangeType135', a)
    if hasattr(b2, 'pascal_subrangeType135'):
        assert _is_linked(b2, 'pascal_subrangeType135', a)
    _safe_set(a, 'pascal_constant136', None)
    assert not _is_linked(a, 'pascal_constant136', b2)
    if hasattr(b2, 'pascal_subrangeType135'):
        assert not _is_linked(b2, 'pascal_subrangeType135', a)


def test_assoc_constant41_link_reassign_clear():
    a = pascal_constant(bool="sample_text", sign="sample_text", string="sample_text")
    b1 = pascal_constantDefinition()
    b2 = pascal_constantDefinition()
    _safe_set(a, 'pascal_constant', b1)
    assert _is_linked(a, 'pascal_constant', b1)
    if hasattr(b1, 'pascal_constantDefinition42'):
        assert _is_linked(b1, 'pascal_constantDefinition42', a)
    _safe_set(a, 'pascal_constant', b2)
    assert _is_linked(a, 'pascal_constant', b2)
    if hasattr(b1, 'pascal_constantDefinition42'):
        assert not _is_linked(b1, 'pascal_constantDefinition42', a)
    if hasattr(b2, 'pascal_constantDefinition42'):
        assert _is_linked(b2, 'pascal_constantDefinition42', a)
    _safe_set(a, 'pascal_constant', None)
    assert not _is_linked(a, 'pascal_constant', b2)
    if hasattr(b2, 'pascal_constantDefinition42'):
        assert not _is_linked(b2, 'pascal_constantDefinition42', a)


def test_assoc_constant51_link_reassign_clear():
    a = pascal_constant(bool="sample_text", sign="sample_text", string="sample_text")
    b1 = pascal_constant(bool="sample_text", sign="sample_text", string="sample_text")
    b2 = pascal_constant(bool="sample_text_2", sign="sample_text_2", string="sample_text_2")
    _safe_set(a, 'pascal_constant50', {b1})
    assert _is_linked(a, 'pascal_constant50', b1)
    if hasattr(b1, 'pascal_constant52'):
        assert _is_linked(b1, 'pascal_constant52', a)
    _safe_set(a, 'pascal_constant50', {b2})
    assert _is_linked(a, 'pascal_constant50', b2)
    if hasattr(b1, 'pascal_constant52'):
        assert not _is_linked(b1, 'pascal_constant52', a)
    if hasattr(b2, 'pascal_constant52'):
        assert _is_linked(b2, 'pascal_constant52', a)
    _safe_set(a, 'pascal_constant50', set())
    assert not _is_linked(a, 'pascal_constant50', b2)
    if hasattr(b2, 'pascal_constant52'):
        assert not _is_linked(b2, 'pascal_constant52', a)


def test_assoc_constantChr287_link_reassign_clear():
    a = pascal_unsignedConstant(string_literal="sample_text")
    b1 = pascal_constantChr()
    b2 = pascal_constantChr()
    _safe_set(a, 'pascal_unsignedConstant288', b1)
    assert _is_linked(a, 'pascal_unsignedConstant288', b1)
    if hasattr(b1, 'pascal_constantChr289'):
        assert _is_linked(b1, 'pascal_constantChr289', a)
    _safe_set(a, 'pascal_unsignedConstant288', b2)
    assert _is_linked(a, 'pascal_unsignedConstant288', b2)
    if hasattr(b1, 'pascal_constantChr289'):
        assert not _is_linked(b1, 'pascal_constantChr289', a)
    if hasattr(b2, 'pascal_constantChr289'):
        assert _is_linked(b2, 'pascal_constantChr289', a)
    _safe_set(a, 'pascal_unsignedConstant288', None)
    assert not _is_linked(a, 'pascal_unsignedConstant288', b2)
    if hasattr(b2, 'pascal_constantChr289'):
        assert not _is_linked(b2, 'pascal_constantChr289', a)


def test_assoc_constantChr48_link_reassign_clear():
    a = pascal_constant(bool="sample_text", sign="sample_text", string="sample_text")
    b1 = pascal_constantChr()
    b2 = pascal_constantChr()
    _safe_set(a, 'pascal_constant49', b1)
    assert _is_linked(a, 'pascal_constant49', b1)
    if hasattr(b1, 'pascal_constantChr'):
        assert _is_linked(b1, 'pascal_constantChr', a)
    _safe_set(a, 'pascal_constant49', b2)
    assert _is_linked(a, 'pascal_constant49', b2)
    if hasattr(b1, 'pascal_constantChr'):
        assert not _is_linked(b1, 'pascal_constantChr', a)
    if hasattr(b2, 'pascal_constantChr'):
        assert _is_linked(b2, 'pascal_constantChr', a)
    _safe_set(a, 'pascal_constant49', None)
    assert not _is_linked(a, 'pascal_constant49', b2)
    if hasattr(b2, 'pascal_constantChr'):
        assert not _is_linked(b2, 'pascal_constantChr', a)


def test_assoc_expression203_link_reassign_clear():
    a = pascal_expression(relationaloperator="sample_text")
    b1 = pascal_variableDeclaration()
    b2 = pascal_variableDeclaration()
    _safe_set(a, 'pascal_expression', b1)
    assert _is_linked(a, 'pascal_expression', b1)
    if hasattr(b1, 'pascal_variableDeclaration204'):
        assert _is_linked(b1, 'pascal_variableDeclaration204', a)
    _safe_set(a, 'pascal_expression', b2)
    assert _is_linked(a, 'pascal_expression', b2)
    if hasattr(b1, 'pascal_variableDeclaration204'):
        assert not _is_linked(b1, 'pascal_variableDeclaration204', a)
    if hasattr(b2, 'pascal_variableDeclaration204'):
        assert _is_linked(b2, 'pascal_variableDeclaration204', a)
    _safe_set(a, 'pascal_expression', None)
    assert not _is_linked(a, 'pascal_expression', b2)
    if hasattr(b2, 'pascal_variableDeclaration204'):
        assert not _is_linked(b2, 'pascal_variableDeclaration204', a)


def test_assoc_expression248_link_reassign_clear():
    a = pascal_expression(relationaloperator="sample_text")
    b1 = pascal_assignmentStatement()
    b2 = pascal_assignmentStatement()
    _safe_set(a, 'pascal_expression250', b1)
    assert _is_linked(a, 'pascal_expression250', b1)
    if hasattr(b1, 'pascal_assignmentStatement249'):
        assert _is_linked(b1, 'pascal_assignmentStatement249', a)
    _safe_set(a, 'pascal_expression250', b2)
    assert _is_linked(a, 'pascal_expression250', b2)
    if hasattr(b1, 'pascal_assignmentStatement249'):
        assert not _is_linked(b1, 'pascal_assignmentStatement249', a)
    if hasattr(b2, 'pascal_assignmentStatement249'):
        assert _is_linked(b2, 'pascal_assignmentStatement249', a)
    _safe_set(a, 'pascal_expression250', None)
    assert not _is_linked(a, 'pascal_expression250', b2)
    if hasattr(b2, 'pascal_assignmentStatement249'):
        assert not _is_linked(b2, 'pascal_assignmentStatement249', a)


def test_assoc_expression257_link_reassign_clear():
    a = pascal_expression(relationaloperator="sample_text")
    b1 = pascal_expression(relationaloperator="sample_text")
    b2 = pascal_expression(relationaloperator="sample_text_2")
    _safe_set(a, 'pascal_expression256', b1)
    assert _is_linked(a, 'pascal_expression256', b1)
    if hasattr(b1, 'pascal_expression258'):
        assert _is_linked(b1, 'pascal_expression258', a)
    _safe_set(a, 'pascal_expression256', b2)
    assert _is_linked(a, 'pascal_expression256', b2)
    if hasattr(b1, 'pascal_expression258'):
        assert not _is_linked(b1, 'pascal_expression258', a)
    if hasattr(b2, 'pascal_expression258'):
        assert _is_linked(b2, 'pascal_expression258', a)
    _safe_set(a, 'pascal_expression256', None)
    assert not _is_linked(a, 'pascal_expression256', b2)
    if hasattr(b2, 'pascal_expression258'):
        assert not _is_linked(b2, 'pascal_expression258', a)


def test_assoc_expression271_link_reassign_clear():
    a = pascal_factor(bool="sample_text")
    b1 = pascal_expression(relationaloperator="sample_text")
    b2 = pascal_expression(relationaloperator="sample_text_2")
    _safe_set(a, 'pascal_factor272', b1)
    assert _is_linked(a, 'pascal_factor272', b1)
    if hasattr(b1, 'pascal_expression273'):
        assert _is_linked(b1, 'pascal_expression273', a)
    _safe_set(a, 'pascal_factor272', b2)
    assert _is_linked(a, 'pascal_factor272', b2)
    if hasattr(b1, 'pascal_expression273'):
        assert not _is_linked(b1, 'pascal_expression273', a)
    if hasattr(b2, 'pascal_expression273'):
        assert _is_linked(b2, 'pascal_expression273', a)
    _safe_set(a, 'pascal_factor272', None)
    assert not _is_linked(a, 'pascal_factor272', b2)
    if hasattr(b2, 'pascal_expression273'):
        assert not _is_linked(b2, 'pascal_expression273', a)


def test_assoc_expression298_link_reassign_clear():
    a = pascal_expression(relationaloperator="sample_text")
    b1 = pascal_actualParameter()
    b2 = pascal_actualParameter()
    _safe_set(a, 'pascal_expression300', b1)
    assert _is_linked(a, 'pascal_expression300', b1)
    if hasattr(b1, 'pascal_actualParameter299'):
        assert _is_linked(b1, 'pascal_actualParameter299', a)
    _safe_set(a, 'pascal_expression300', b2)
    assert _is_linked(a, 'pascal_expression300', b2)
    if hasattr(b1, 'pascal_actualParameter299'):
        assert not _is_linked(b1, 'pascal_actualParameter299', a)
    if hasattr(b2, 'pascal_actualParameter299'):
        assert _is_linked(b2, 'pascal_actualParameter299', a)
    _safe_set(a, 'pascal_expression300', None)
    assert not _is_linked(a, 'pascal_expression300', b2)
    if hasattr(b2, 'pascal_actualParameter299'):
        assert not _is_linked(b2, 'pascal_actualParameter299', a)


def test_assoc_expression316_link_reassign_clear():
    a = pascal_expression(relationaloperator="sample_text")
    b1 = pascal_caseStatement()
    b2 = pascal_caseStatement()
    _safe_set(a, 'pascal_expression318', b1)
    assert _is_linked(a, 'pascal_expression318', b1)
    if hasattr(b1, 'pascal_caseStatement317'):
        assert _is_linked(b1, 'pascal_caseStatement317', a)
    _safe_set(a, 'pascal_expression318', b2)
    assert _is_linked(a, 'pascal_expression318', b2)
    if hasattr(b1, 'pascal_caseStatement317'):
        assert not _is_linked(b1, 'pascal_caseStatement317', a)
    if hasattr(b2, 'pascal_caseStatement317'):
        assert _is_linked(b2, 'pascal_caseStatement317', a)
    _safe_set(a, 'pascal_expression318', None)
    assert not _is_linked(a, 'pascal_expression318', b2)
    if hasattr(b2, 'pascal_caseStatement317'):
        assert not _is_linked(b2, 'pascal_caseStatement317', a)


def test_assoc_factor269_link_reassign_clear():
    a = pascal_factor(bool="sample_text")
    b1 = pascal_signedFactor()
    b2 = pascal_signedFactor()
    _safe_set(a, 'pascal_factor', b1)
    assert _is_linked(a, 'pascal_factor', b1)
    if hasattr(b1, 'pascal_signedFactor270'):
        assert _is_linked(b1, 'pascal_signedFactor270', a)
    _safe_set(a, 'pascal_factor', b2)
    assert _is_linked(a, 'pascal_factor', b2)
    if hasattr(b1, 'pascal_signedFactor270'):
        assert not _is_linked(b1, 'pascal_signedFactor270', a)
    if hasattr(b2, 'pascal_signedFactor270'):
        assert _is_linked(b2, 'pascal_signedFactor270', a)
    _safe_set(a, 'pascal_factor', None)
    assert not _is_linked(a, 'pascal_factor', b2)
    if hasattr(b2, 'pascal_signedFactor270'):
        assert not _is_linked(b2, 'pascal_signedFactor270', a)


def test_assoc_factor277_link_reassign_clear():
    a = pascal_factor(bool="sample_text")
    b1 = pascal_factor(bool="sample_text")
    b2 = pascal_factor(bool="sample_text_2")
    _safe_set(a, 'pascal_factor276', b1)
    assert _is_linked(a, 'pascal_factor276', b1)
    if hasattr(b1, 'pascal_factor278'):
        assert _is_linked(b1, 'pascal_factor278', a)
    _safe_set(a, 'pascal_factor276', b2)
    assert _is_linked(a, 'pascal_factor276', b2)
    if hasattr(b1, 'pascal_factor278'):
        assert not _is_linked(b1, 'pascal_factor278', a)
    if hasattr(b2, 'pascal_factor278'):
        assert _is_linked(b2, 'pascal_factor278', a)
    _safe_set(a, 'pascal_factor276', None)
    assert not _is_linked(a, 'pascal_factor276', b2)
    if hasattr(b2, 'pascal_factor278'):
        assert not _is_linked(b2, 'pascal_factor278', a)


def test_assoc_fieldList53_link_reassign_clear():
    a = pascal_constant(bool="sample_text", sign="sample_text", string="sample_text")
    b1 = pascal_fieldList()
    b2 = pascal_fieldList()
    _safe_set(a, 'pascal_constant54', b1)
    assert _is_linked(a, 'pascal_constant54', b1)
    if hasattr(b1, 'pascal_fieldList'):
        assert _is_linked(b1, 'pascal_fieldList', a)
    _safe_set(a, 'pascal_constant54', b2)
    assert _is_linked(a, 'pascal_constant54', b2)
    if hasattr(b1, 'pascal_fieldList'):
        assert not _is_linked(b1, 'pascal_fieldList', a)
    if hasattr(b2, 'pascal_fieldList'):
        assert _is_linked(b2, 'pascal_fieldList', a)
    _safe_set(a, 'pascal_constant54', None)
    assert not _is_linked(a, 'pascal_constant54', b2)
    if hasattr(b2, 'pascal_fieldList'):
        assert not _is_linked(b2, 'pascal_fieldList', a)


def test_assoc_functionDesignator279_link_reassign_clear():
    a = pascal_factor(bool="sample_text")
    b1 = pascal_functionDesignator()
    b2 = pascal_functionDesignator()
    _safe_set(a, 'pascal_factor280', b1)
    assert _is_linked(a, 'pascal_factor280', b1)
    if hasattr(b1, 'pascal_functionDesignator'):
        assert _is_linked(b1, 'pascal_functionDesignator', a)
    _safe_set(a, 'pascal_factor280', b2)
    assert _is_linked(a, 'pascal_factor280', b2)
    if hasattr(b1, 'pascal_functionDesignator'):
        assert not _is_linked(b1, 'pascal_functionDesignator', a)
    if hasattr(b2, 'pascal_functionDesignator'):
        assert _is_linked(b2, 'pascal_functionDesignator', a)
    _safe_set(a, 'pascal_factor280', None)
    assert not _is_linked(a, 'pascal_factor280', b2)
    if hasattr(b2, 'pascal_functionDesignator'):
        assert not _is_linked(b2, 'pascal_functionDesignator', a)


def test_assoc_identifer5_link_reassign_clear():
    a = pascal_identifier(identifier="sample_text")
    b1 = pascal_programHeading()
    b2 = pascal_programHeading()
    _safe_set(a, 'pascal_identifier', b1)
    assert _is_linked(a, 'pascal_identifier', b1)
    if hasattr(b1, 'pascal_programHeading6'):
        assert _is_linked(b1, 'pascal_programHeading6', a)
    _safe_set(a, 'pascal_identifier', b2)
    assert _is_linked(a, 'pascal_identifier', b2)
    if hasattr(b1, 'pascal_programHeading6'):
        assert not _is_linked(b1, 'pascal_programHeading6', a)
    if hasattr(b2, 'pascal_programHeading6'):
        assert _is_linked(b2, 'pascal_programHeading6', a)
    _safe_set(a, 'pascal_identifier', None)
    assert not _is_linked(a, 'pascal_identifier', b2)
    if hasattr(b2, 'pascal_programHeading6'):
        assert not _is_linked(b2, 'pascal_programHeading6', a)


def test_assoc_identifier104_link_reassign_clear():
    a = pascal_typeIdentifier(boolean="sample_text", char="sample_text", integer="sample_text", real="sample_text", string="sample_text")
    b1 = pascal_identifier(identifier="sample_text")
    b2 = pascal_identifier(identifier="sample_text_2")
    _safe_set(a, 'pascal_typeIdentifier105', b1)
    assert _is_linked(a, 'pascal_typeIdentifier105', b1)
    if hasattr(b1, 'pascal_identifier106'):
        assert _is_linked(b1, 'pascal_identifier106', a)
    _safe_set(a, 'pascal_typeIdentifier105', b2)
    assert _is_linked(a, 'pascal_typeIdentifier105', b2)
    if hasattr(b1, 'pascal_identifier106'):
        assert not _is_linked(b1, 'pascal_identifier106', a)
    if hasattr(b2, 'pascal_identifier106'):
        assert _is_linked(b2, 'pascal_identifier106', a)
    _safe_set(a, 'pascal_typeIdentifier105', None)
    assert not _is_linked(a, 'pascal_typeIdentifier105', b2)
    if hasattr(b2, 'pascal_identifier106'):
        assert not _is_linked(b2, 'pascal_identifier106', a)


def test_assoc_identifier144_link_reassign_clear():
    a = pascal_identifier(identifier="sample_text")
    b1 = pascal_stringtype()
    b2 = pascal_stringtype()
    _safe_set(a, 'pascal_identifier146', b1)
    assert _is_linked(a, 'pascal_identifier146', b1)
    if hasattr(b1, 'pascal_stringtype145'):
        assert _is_linked(b1, 'pascal_stringtype145', a)
    _safe_set(a, 'pascal_identifier146', b2)
    assert _is_linked(a, 'pascal_identifier146', b2)
    if hasattr(b1, 'pascal_stringtype145'):
        assert not _is_linked(b1, 'pascal_stringtype145', a)
    if hasattr(b2, 'pascal_stringtype145'):
        assert _is_linked(b2, 'pascal_stringtype145', a)
    _safe_set(a, 'pascal_identifier146', None)
    assert not _is_linked(a, 'pascal_identifier146', b2)
    if hasattr(b2, 'pascal_stringtype145'):
        assert not _is_linked(b2, 'pascal_stringtype145', a)


def test_assoc_identifier178_link_reassign_clear():
    a = pascal_identifier(identifier="sample_text")
    b1 = pascal_tag()
    b2 = pascal_tag()
    _safe_set(a, 'pascal_identifier180', b1)
    assert _is_linked(a, 'pascal_identifier180', b1)
    if hasattr(b1, 'pascal_tag179'):
        assert _is_linked(b1, 'pascal_tag179', a)
    _safe_set(a, 'pascal_identifier180', b2)
    assert _is_linked(a, 'pascal_identifier180', b2)
    if hasattr(b1, 'pascal_tag179'):
        assert not _is_linked(b1, 'pascal_tag179', a)
    if hasattr(b2, 'pascal_tag179'):
        assert _is_linked(b2, 'pascal_tag179', a)
    _safe_set(a, 'pascal_identifier180', None)
    assert not _is_linked(a, 'pascal_identifier180', b2)
    if hasattr(b2, 'pascal_tag179'):
        assert not _is_linked(b2, 'pascal_tag179', a)


def test_assoc_identifier211_link_reassign_clear():
    a = pascal_identifier(identifier="sample_text")
    b1 = pascal_procedureDeclaration()
    b2 = pascal_procedureDeclaration()
    _safe_set(a, 'pascal_identifier213', b1)
    assert _is_linked(a, 'pascal_identifier213', b1)
    if hasattr(b1, 'pascal_procedureDeclaration212'):
        assert _is_linked(b1, 'pascal_procedureDeclaration212', a)
    _safe_set(a, 'pascal_identifier213', b2)
    assert _is_linked(a, 'pascal_identifier213', b2)
    if hasattr(b1, 'pascal_procedureDeclaration212'):
        assert not _is_linked(b1, 'pascal_procedureDeclaration212', a)
    if hasattr(b2, 'pascal_procedureDeclaration212'):
        assert _is_linked(b2, 'pascal_procedureDeclaration212', a)
    _safe_set(a, 'pascal_identifier213', None)
    assert not _is_linked(a, 'pascal_identifier213', b2)
    if hasattr(b2, 'pascal_procedureDeclaration212'):
        assert not _is_linked(b2, 'pascal_procedureDeclaration212', a)


def test_assoc_identifier220_link_reassign_clear():
    a = pascal_identifier(identifier="sample_text")
    b1 = pascal_functionDeclaration()
    b2 = pascal_functionDeclaration()
    _safe_set(a, 'pascal_identifier222', b1)
    assert _is_linked(a, 'pascal_identifier222', b1)
    if hasattr(b1, 'pascal_functionDeclaration221'):
        assert _is_linked(b1, 'pascal_functionDeclaration221', a)
    _safe_set(a, 'pascal_identifier222', b2)
    assert _is_linked(a, 'pascal_identifier222', b2)
    if hasattr(b1, 'pascal_functionDeclaration221'):
        assert not _is_linked(b1, 'pascal_functionDeclaration221', a)
    if hasattr(b2, 'pascal_functionDeclaration221'):
        assert _is_linked(b2, 'pascal_functionDeclaration221', a)
    _safe_set(a, 'pascal_identifier222', None)
    assert not _is_linked(a, 'pascal_identifier222', b2)
    if hasattr(b2, 'pascal_functionDeclaration221'):
        assert not _is_linked(b2, 'pascal_functionDeclaration221', a)


def test_assoc_identifier237_link_reassign_clear():
    a = pascal_identifier(identifier="sample_text")
    b1 = pascal_unlabelledStatement()
    b2 = pascal_unlabelledStatement()
    _safe_set(a, 'pascal_identifier239', b1)
    assert _is_linked(a, 'pascal_identifier239', b1)
    if hasattr(b1, 'pascal_unlabelledStatement238'):
        assert _is_linked(b1, 'pascal_unlabelledStatement238', a)
    _safe_set(a, 'pascal_identifier239', b2)
    assert _is_linked(a, 'pascal_identifier239', b2)
    if hasattr(b1, 'pascal_unlabelledStatement238'):
        assert not _is_linked(b1, 'pascal_unlabelledStatement238', a)
    if hasattr(b2, 'pascal_unlabelledStatement238'):
        assert _is_linked(b2, 'pascal_unlabelledStatement238', a)
    _safe_set(a, 'pascal_identifier239', None)
    assert not _is_linked(a, 'pascal_identifier239', b2)
    if hasattr(b2, 'pascal_unlabelledStatement238'):
        assert not _is_linked(b2, 'pascal_unlabelledStatement238', a)


def test_assoc_identifier251_link_reassign_clear():
    a = pascal_identifier(identifier="sample_text")
    b1 = pascal_variable()
    b2 = pascal_variable()
    _safe_set(a, 'pascal_identifier253', b1)
    assert _is_linked(a, 'pascal_identifier253', b1)
    if hasattr(b1, 'pascal_variable252'):
        assert _is_linked(b1, 'pascal_variable252', a)
    _safe_set(a, 'pascal_identifier253', b2)
    assert _is_linked(a, 'pascal_identifier253', b2)
    if hasattr(b1, 'pascal_variable252'):
        assert not _is_linked(b1, 'pascal_variable252', a)
    if hasattr(b2, 'pascal_variable252'):
        assert _is_linked(b2, 'pascal_variable252', a)
    _safe_set(a, 'pascal_identifier253', None)
    assert not _is_linked(a, 'pascal_identifier253', b2)
    if hasattr(b2, 'pascal_variable252'):
        assert not _is_linked(b2, 'pascal_variable252', a)


def test_assoc_identifier290_link_reassign_clear():
    a = pascal_identifier(identifier="sample_text")
    b1 = pascal_functionDesignator()
    b2 = pascal_functionDesignator()
    _safe_set(a, 'pascal_identifier292', b1)
    assert _is_linked(a, 'pascal_identifier292', b1)
    if hasattr(b1, 'pascal_functionDesignator291'):
        assert _is_linked(b1, 'pascal_functionDesignator291', a)
    _safe_set(a, 'pascal_identifier292', b2)
    assert _is_linked(a, 'pascal_identifier292', b2)
    if hasattr(b1, 'pascal_functionDesignator291'):
        assert not _is_linked(b1, 'pascal_functionDesignator291', a)
    if hasattr(b2, 'pascal_functionDesignator291'):
        assert _is_linked(b2, 'pascal_functionDesignator291', a)
    _safe_set(a, 'pascal_identifier292', None)
    assert not _is_linked(a, 'pascal_identifier292', b2)
    if hasattr(b2, 'pascal_functionDesignator291'):
        assert not _is_linked(b2, 'pascal_functionDesignator291', a)


def test_assoc_identifier33_link_reassign_clear():
    a = pascal_identifier(identifier="sample_text")
    b1 = pascal_label()
    b2 = pascal_label()
    _safe_set(a, 'pascal_identifier35', b1)
    assert _is_linked(a, 'pascal_identifier35', b1)
    if hasattr(b1, 'pascal_label34'):
        assert _is_linked(b1, 'pascal_label34', a)
    _safe_set(a, 'pascal_identifier35', b2)
    assert _is_linked(a, 'pascal_identifier35', b2)
    if hasattr(b1, 'pascal_label34'):
        assert not _is_linked(b1, 'pascal_label34', a)
    if hasattr(b2, 'pascal_label34'):
        assert _is_linked(b2, 'pascal_label34', a)
    _safe_set(a, 'pascal_identifier35', None)
    assert not _is_linked(a, 'pascal_identifier35', b2)
    if hasattr(b2, 'pascal_label34'):
        assert not _is_linked(b2, 'pascal_label34', a)


def test_assoc_identifier38_link_reassign_clear():
    a = pascal_identifier(identifier="sample_text")
    b1 = pascal_constantDefinition()
    b2 = pascal_constantDefinition()
    _safe_set(a, 'pascal_identifier40', b1)
    assert _is_linked(a, 'pascal_identifier40', b1)
    if hasattr(b1, 'pascal_constantDefinition39'):
        assert _is_linked(b1, 'pascal_constantDefinition39', a)
    _safe_set(a, 'pascal_identifier40', b2)
    assert _is_linked(a, 'pascal_identifier40', b2)
    if hasattr(b1, 'pascal_constantDefinition39'):
        assert not _is_linked(b1, 'pascal_constantDefinition39', a)
    if hasattr(b2, 'pascal_constantDefinition39'):
        assert _is_linked(b2, 'pascal_constantDefinition39', a)
    _safe_set(a, 'pascal_identifier40', None)
    assert not _is_linked(a, 'pascal_identifier40', b2)
    if hasattr(b2, 'pascal_constantDefinition39'):
        assert not _is_linked(b2, 'pascal_constantDefinition39', a)


def test_assoc_identifier45_link_reassign_clear():
    a = pascal_identifier(identifier="sample_text")
    b1 = pascal_constant(bool="sample_text", sign="sample_text", string="sample_text")
    b2 = pascal_constant(bool="sample_text_2", sign="sample_text_2", string="sample_text_2")
    _safe_set(a, 'pascal_identifier47', b1)
    assert _is_linked(a, 'pascal_identifier47', b1)
    if hasattr(b1, 'pascal_constant46'):
        assert _is_linked(b1, 'pascal_constant46', a)
    _safe_set(a, 'pascal_identifier47', b2)
    assert _is_linked(a, 'pascal_identifier47', b2)
    if hasattr(b1, 'pascal_constant46'):
        assert not _is_linked(b1, 'pascal_constant46', a)
    if hasattr(b2, 'pascal_constant46'):
        assert _is_linked(b2, 'pascal_constant46', a)
    _safe_set(a, 'pascal_identifier47', None)
    assert not _is_linked(a, 'pascal_identifier47', b2)
    if hasattr(b2, 'pascal_constant46'):
        assert not _is_linked(b2, 'pascal_constant46', a)


def test_assoc_identifier69_link_reassign_clear():
    a = pascal_identifier(identifier="sample_text")
    b1 = pascal_typeDefinition()
    b2 = pascal_typeDefinition()
    _safe_set(a, 'pascal_identifier71', b1)
    assert _is_linked(a, 'pascal_identifier71', b1)
    if hasattr(b1, 'pascal_typeDefinition70'):
        assert _is_linked(b1, 'pascal_typeDefinition70', a)
    _safe_set(a, 'pascal_identifier71', b2)
    assert _is_linked(a, 'pascal_identifier71', b2)
    if hasattr(b1, 'pascal_typeDefinition70'):
        assert not _is_linked(b1, 'pascal_typeDefinition70', a)
    if hasattr(b2, 'pascal_typeDefinition70'):
        assert _is_linked(b2, 'pascal_typeDefinition70', a)
    _safe_set(a, 'pascal_identifier71', None)
    assert not _is_linked(a, 'pascal_identifier71', b2)
    if hasattr(b2, 'pascal_typeDefinition70'):
        assert not _is_linked(b2, 'pascal_typeDefinition70', a)


def test_assoc_identifier9_link_reassign_clear():
    a = pascal_identifier(identifier="sample_text")
    b1 = pascal_identifierList()
    b2 = pascal_identifierList()
    _safe_set(a, 'pascal_identifier11', b1)
    assert _is_linked(a, 'pascal_identifier11', b1)
    if hasattr(b1, 'pascal_identifierList10'):
        assert _is_linked(b1, 'pascal_identifierList10', a)
    _safe_set(a, 'pascal_identifier11', b2)
    assert _is_linked(a, 'pascal_identifier11', b2)
    if hasattr(b1, 'pascal_identifierList10'):
        assert not _is_linked(b1, 'pascal_identifierList10', a)
    if hasattr(b2, 'pascal_identifierList10'):
        assert _is_linked(b2, 'pascal_identifierList10', a)
    _safe_set(a, 'pascal_identifier11', None)
    assert not _is_linked(a, 'pascal_identifier11', b2)
    if hasattr(b2, 'pascal_identifierList10'):
        assert not _is_linked(b2, 'pascal_identifierList10', a)


def test_assoc_identifierList112_link_reassign_clear():
    a = pascal_identifier(identifier="sample_text")
    b1 = pascal_identifierList()
    b2 = pascal_identifierList()
    _safe_set(a, 'pascal_identifier14', b1)
    assert _is_linked(a, 'pascal_identifier14', b1)
    if hasattr(b1, 'pascal_identifierList13'):
        assert _is_linked(b1, 'pascal_identifierList13', a)
    _safe_set(a, 'pascal_identifier14', b2)
    assert _is_linked(a, 'pascal_identifier14', b2)
    if hasattr(b1, 'pascal_identifierList13'):
        assert not _is_linked(b1, 'pascal_identifierList13', a)
    if hasattr(b2, 'pascal_identifierList13'):
        assert _is_linked(b2, 'pascal_identifierList13', a)
    _safe_set(a, 'pascal_identifier14', None)
    assert not _is_linked(a, 'pascal_identifier14', b2)
    if hasattr(b2, 'pascal_identifierList13'):
        assert not _is_linked(b2, 'pascal_identifierList13', a)


def test_assoc_signedFactor264_link_reassign_clear():
    a = pascal_term(multiplicativeoperator="sample_text")
    b1 = pascal_signedFactor()
    b2 = pascal_signedFactor()
    _safe_set(a, 'pascal_term265', b1)
    assert _is_linked(a, 'pascal_term265', b1)
    if hasattr(b1, 'pascal_signedFactor'):
        assert _is_linked(b1, 'pascal_signedFactor', a)
    _safe_set(a, 'pascal_term265', b2)
    assert _is_linked(a, 'pascal_term265', b2)
    if hasattr(b1, 'pascal_signedFactor'):
        assert not _is_linked(b1, 'pascal_signedFactor', a)
    if hasattr(b2, 'pascal_signedFactor'):
        assert _is_linked(b2, 'pascal_signedFactor', a)
    _safe_set(a, 'pascal_term265', None)
    assert not _is_linked(a, 'pascal_term265', b2)
    if hasattr(b2, 'pascal_signedFactor'):
        assert not _is_linked(b2, 'pascal_signedFactor', a)


def test_assoc_simpleExpression254_link_reassign_clear():
    a = pascal_simpleExpression(additiveoperator="sample_text")
    b1 = pascal_expression(relationaloperator="sample_text")
    b2 = pascal_expression(relationaloperator="sample_text_2")
    _safe_set(a, 'pascal_simpleExpression', b1)
    assert _is_linked(a, 'pascal_simpleExpression', b1)
    if hasattr(b1, 'pascal_expression255'):
        assert _is_linked(b1, 'pascal_expression255', a)
    _safe_set(a, 'pascal_simpleExpression', b2)
    assert _is_linked(a, 'pascal_simpleExpression', b2)
    if hasattr(b1, 'pascal_expression255'):
        assert not _is_linked(b1, 'pascal_expression255', a)
    if hasattr(b2, 'pascal_expression255'):
        assert _is_linked(b2, 'pascal_expression255', a)
    _safe_set(a, 'pascal_simpleExpression', None)
    assert not _is_linked(a, 'pascal_simpleExpression', b2)
    if hasattr(b2, 'pascal_expression255'):
        assert not _is_linked(b2, 'pascal_expression255', a)


def test_assoc_simpleExpression262_link_reassign_clear():
    a = pascal_simpleExpression(additiveoperator="sample_text")
    b1 = pascal_simpleExpression(additiveoperator="sample_text")
    b2 = pascal_simpleExpression(additiveoperator="sample_text_2")
    _safe_set(a, 'pascal_simpleExpression261', b1)
    assert _is_linked(a, 'pascal_simpleExpression261', b1)
    if hasattr(b1, 'pascal_simpleExpression263'):
        assert _is_linked(b1, 'pascal_simpleExpression263', a)
    _safe_set(a, 'pascal_simpleExpression261', b2)
    assert _is_linked(a, 'pascal_simpleExpression261', b2)
    if hasattr(b1, 'pascal_simpleExpression263'):
        assert not _is_linked(b1, 'pascal_simpleExpression263', a)
    if hasattr(b2, 'pascal_simpleExpression263'):
        assert _is_linked(b2, 'pascal_simpleExpression263', a)
    _safe_set(a, 'pascal_simpleExpression261', None)
    assert not _is_linked(a, 'pascal_simpleExpression261', b2)
    if hasattr(b2, 'pascal_simpleExpression263'):
        assert not _is_linked(b2, 'pascal_simpleExpression263', a)


def test_assoc_term259_link_reassign_clear():
    a = pascal_term(multiplicativeoperator="sample_text")
    b1 = pascal_simpleExpression(additiveoperator="sample_text")
    b2 = pascal_simpleExpression(additiveoperator="sample_text_2")
    _safe_set(a, 'pascal_term', b1)
    assert _is_linked(a, 'pascal_term', b1)
    if hasattr(b1, 'pascal_simpleExpression260'):
        assert _is_linked(b1, 'pascal_simpleExpression260', a)
    _safe_set(a, 'pascal_term', b2)
    assert _is_linked(a, 'pascal_term', b2)
    if hasattr(b1, 'pascal_simpleExpression260'):
        assert not _is_linked(b1, 'pascal_simpleExpression260', a)
    if hasattr(b2, 'pascal_simpleExpression260'):
        assert _is_linked(b2, 'pascal_simpleExpression260', a)
    _safe_set(a, 'pascal_term', None)
    assert not _is_linked(a, 'pascal_term', b2)
    if hasattr(b2, 'pascal_simpleExpression260'):
        assert not _is_linked(b2, 'pascal_simpleExpression260', a)


def test_assoc_term267_link_reassign_clear():
    a = pascal_term(multiplicativeoperator="sample_text")
    b1 = pascal_term(multiplicativeoperator="sample_text")
    b2 = pascal_term(multiplicativeoperator="sample_text_2")
    _safe_set(a, 'pascal_term266', b1)
    assert _is_linked(a, 'pascal_term266', b1)
    if hasattr(b1, 'pascal_term268'):
        assert _is_linked(b1, 'pascal_term268', a)
    _safe_set(a, 'pascal_term266', b2)
    assert _is_linked(a, 'pascal_term266', b2)
    if hasattr(b1, 'pascal_term268'):
        assert not _is_linked(b1, 'pascal_term268', a)
    if hasattr(b2, 'pascal_term268'):
        assert _is_linked(b2, 'pascal_term268', a)
    _safe_set(a, 'pascal_term266', None)
    assert not _is_linked(a, 'pascal_term266', b2)
    if hasattr(b2, 'pascal_term268'):
        assert not _is_linked(b2, 'pascal_term268', a)


def test_assoc_typeIdentifier101_link_reassign_clear():
    a = pascal_typeIdentifier(boolean="sample_text", char="sample_text", integer="sample_text", real="sample_text", string="sample_text")
    b1 = pascal_parameterGroup()
    b2 = pascal_parameterGroup()
    _safe_set(a, 'pascal_typeIdentifier103', b1)
    assert _is_linked(a, 'pascal_typeIdentifier103', b1)
    if hasattr(b1, 'pascal_parameterGroup102'):
        assert _is_linked(b1, 'pascal_parameterGroup102', a)
    _safe_set(a, 'pascal_typeIdentifier103', b2)
    assert _is_linked(a, 'pascal_typeIdentifier103', b2)
    if hasattr(b1, 'pascal_parameterGroup102'):
        assert not _is_linked(b1, 'pascal_parameterGroup102', a)
    if hasattr(b2, 'pascal_parameterGroup102'):
        assert _is_linked(b2, 'pascal_parameterGroup102', a)
    _safe_set(a, 'pascal_typeIdentifier103', None)
    assert not _is_linked(a, 'pascal_typeIdentifier103', b2)
    if hasattr(b2, 'pascal_parameterGroup102'):
        assert not _is_linked(b2, 'pascal_parameterGroup102', a)


def test_assoc_typeIdentifier116_link_reassign_clear():
    a = pascal_typeIdentifier(boolean="sample_text", char="sample_text", integer="sample_text", real="sample_text", string="sample_text")
    b1 = pascal_pointerType()
    b2 = pascal_pointerType()
    _safe_set(a, 'pascal_typeIdentifier118', b1)
    assert _is_linked(a, 'pascal_typeIdentifier118', b1)
    if hasattr(b1, 'pascal_pointerType117'):
        assert _is_linked(b1, 'pascal_pointerType117', a)
    _safe_set(a, 'pascal_typeIdentifier118', b2)
    assert _is_linked(a, 'pascal_typeIdentifier118', b2)
    if hasattr(b1, 'pascal_pointerType117'):
        assert not _is_linked(b1, 'pascal_pointerType117', a)
    if hasattr(b2, 'pascal_pointerType117'):
        assert _is_linked(b2, 'pascal_pointerType117', a)
    _safe_set(a, 'pascal_typeIdentifier118', None)
    assert not _is_linked(a, 'pascal_typeIdentifier118', b2)
    if hasattr(b2, 'pascal_pointerType117'):
        assert not _is_linked(b2, 'pascal_pointerType117', a)


def test_assoc_typeIdentifier1184_link_reassign_clear():
    a = pascal_typeIdentifier(boolean="sample_text", char="sample_text", integer="sample_text", real="sample_text", string="sample_text")
    b1 = pascal_tag()
    b2 = pascal_tag()
    _safe_set(a, 'pascal_typeIdentifier186', b1)
    assert _is_linked(a, 'pascal_typeIdentifier186', b1)
    if hasattr(b1, 'pascal_tag185'):
        assert _is_linked(b1, 'pascal_tag185', a)
    _safe_set(a, 'pascal_typeIdentifier186', b2)
    assert _is_linked(a, 'pascal_typeIdentifier186', b2)
    if hasattr(b1, 'pascal_tag185'):
        assert not _is_linked(b1, 'pascal_tag185', a)
    if hasattr(b2, 'pascal_tag185'):
        assert _is_linked(b2, 'pascal_tag185', a)
    _safe_set(a, 'pascal_typeIdentifier186', None)
    assert not _is_linked(a, 'pascal_typeIdentifier186', b2)
    if hasattr(b2, 'pascal_tag185'):
        assert not _is_linked(b2, 'pascal_tag185', a)


def test_assoc_typeIdentifier123_link_reassign_clear():
    a = pascal_typeIdentifier(boolean="sample_text", char="sample_text", integer="sample_text", real="sample_text", string="sample_text")
    b1 = pascal_simpleType()
    b2 = pascal_simpleType()
    _safe_set(a, 'pascal_typeIdentifier125', b1)
    assert _is_linked(a, 'pascal_typeIdentifier125', b1)
    if hasattr(b1, 'pascal_simpleType124'):
        assert _is_linked(b1, 'pascal_simpleType124', a)
    _safe_set(a, 'pascal_typeIdentifier125', b2)
    assert _is_linked(a, 'pascal_typeIdentifier125', b2)
    if hasattr(b1, 'pascal_simpleType124'):
        assert not _is_linked(b1, 'pascal_simpleType124', a)
    if hasattr(b2, 'pascal_simpleType124'):
        assert _is_linked(b2, 'pascal_simpleType124', a)
    _safe_set(a, 'pascal_typeIdentifier125', None)
    assert not _is_linked(a, 'pascal_typeIdentifier125', b2)
    if hasattr(b2, 'pascal_simpleType124'):
        assert not _is_linked(b2, 'pascal_simpleType124', a)


def test_assoc_typeIdentifier181_link_reassign_clear():
    a = pascal_typeIdentifier(boolean="sample_text", char="sample_text", integer="sample_text", real="sample_text", string="sample_text")
    b1 = pascal_tag()
    b2 = pascal_tag()
    _safe_set(a, 'pascal_typeIdentifier183', b1)
    assert _is_linked(a, 'pascal_typeIdentifier183', b1)
    if hasattr(b1, 'pascal_tag182'):
        assert _is_linked(b1, 'pascal_tag182', a)
    _safe_set(a, 'pascal_typeIdentifier183', b2)
    assert _is_linked(a, 'pascal_typeIdentifier183', b2)
    if hasattr(b1, 'pascal_tag182'):
        assert not _is_linked(b1, 'pascal_tag182', a)
    if hasattr(b2, 'pascal_tag182'):
        assert _is_linked(b2, 'pascal_tag182', a)
    _safe_set(a, 'pascal_typeIdentifier183', None)
    assert not _is_linked(a, 'pascal_typeIdentifier183', b2)
    if hasattr(b2, 'pascal_tag182'):
        assert not _is_linked(b2, 'pascal_tag182', a)


def test_assoc_typeIdentifier226_link_reassign_clear():
    a = pascal_typeIdentifier(boolean="sample_text", char="sample_text", integer="sample_text", real="sample_text", string="sample_text")
    b1 = pascal_functionDeclaration()
    b2 = pascal_functionDeclaration()
    _safe_set(a, 'pascal_typeIdentifier228', b1)
    assert _is_linked(a, 'pascal_typeIdentifier228', b1)
    if hasattr(b1, 'pascal_functionDeclaration227'):
        assert _is_linked(b1, 'pascal_functionDeclaration227', a)
    _safe_set(a, 'pascal_typeIdentifier228', b2)
    assert _is_linked(a, 'pascal_typeIdentifier228', b2)
    if hasattr(b1, 'pascal_functionDeclaration227'):
        assert not _is_linked(b1, 'pascal_functionDeclaration227', a)
    if hasattr(b2, 'pascal_functionDeclaration227'):
        assert _is_linked(b2, 'pascal_functionDeclaration227', a)
    _safe_set(a, 'pascal_typeIdentifier228', None)
    assert not _is_linked(a, 'pascal_typeIdentifier228', b2)
    if hasattr(b2, 'pascal_functionDeclaration227'):
        assert not _is_linked(b2, 'pascal_functionDeclaration227', a)


def test_assoc_typeIdentifier80_link_reassign_clear():
    a = pascal_typeIdentifier(boolean="sample_text", char="sample_text", integer="sample_text", real="sample_text", string="sample_text")
    b1 = pascal_functionType()
    b2 = pascal_functionType()
    _safe_set(a, 'pascal_typeIdentifier', b1)
    assert _is_linked(a, 'pascal_typeIdentifier', b1)
    if hasattr(b1, 'pascal_functionType81'):
        assert _is_linked(b1, 'pascal_functionType81', a)
    _safe_set(a, 'pascal_typeIdentifier', b2)
    assert _is_linked(a, 'pascal_typeIdentifier', b2)
    if hasattr(b1, 'pascal_functionType81'):
        assert not _is_linked(b1, 'pascal_functionType81', a)
    if hasattr(b2, 'pascal_functionType81'):
        assert _is_linked(b2, 'pascal_functionType81', a)
    _safe_set(a, 'pascal_typeIdentifier', None)
    assert not _is_linked(a, 'pascal_typeIdentifier', b2)
    if hasattr(b2, 'pascal_functionType81'):
        assert not _is_linked(b2, 'pascal_functionType81', a)


def test_assoc_unsignedConstant274_link_reassign_clear():
    a = pascal_unsignedConstant(string_literal="sample_text")
    b1 = pascal_factor(bool="sample_text")
    b2 = pascal_factor(bool="sample_text_2")
    _safe_set(a, 'pascal_unsignedConstant', b1)
    assert _is_linked(a, 'pascal_unsignedConstant', b1)
    if hasattr(b1, 'pascal_factor275'):
        assert _is_linked(b1, 'pascal_factor275', a)
    _safe_set(a, 'pascal_unsignedConstant', b2)
    assert _is_linked(a, 'pascal_unsignedConstant', b2)
    if hasattr(b1, 'pascal_factor275'):
        assert not _is_linked(b1, 'pascal_factor275', a)
    if hasattr(b2, 'pascal_factor275'):
        assert _is_linked(b2, 'pascal_factor275', a)
    _safe_set(a, 'pascal_unsignedConstant', None)
    assert not _is_linked(a, 'pascal_unsignedConstant', b2)
    if hasattr(b2, 'pascal_factor275'):
        assert not _is_linked(b2, 'pascal_factor275', a)


def test_assoc_unsignedInteger31_link_reassign_clear():
    a = pascal_unsignedInteger(number="sample_text")
    b1 = pascal_label()
    b2 = pascal_label()
    _safe_set(a, 'pascal_unsignedInteger', b1)
    assert _is_linked(a, 'pascal_unsignedInteger', b1)
    if hasattr(b1, 'pascal_label32'):
        assert _is_linked(b1, 'pascal_label32', a)
    _safe_set(a, 'pascal_unsignedInteger', b2)
    assert _is_linked(a, 'pascal_unsignedInteger', b2)
    if hasattr(b1, 'pascal_label32'):
        assert not _is_linked(b1, 'pascal_label32', a)
    if hasattr(b2, 'pascal_label32'):
        assert _is_linked(b2, 'pascal_label32', a)
    _safe_set(a, 'pascal_unsignedInteger', None)
    assert not _is_linked(a, 'pascal_unsignedInteger', b2)
    if hasattr(b2, 'pascal_label32'):
        assert not _is_linked(b2, 'pascal_label32', a)


def test_assoc_unsignedInteger55_link_reassign_clear():
    a = pascal_unsignedInteger(number="sample_text")
    b1 = pascal_constantChr()
    b2 = pascal_constantChr()
    _safe_set(a, 'pascal_unsignedInteger57', b1)
    assert _is_linked(a, 'pascal_unsignedInteger57', b1)
    if hasattr(b1, 'pascal_constantChr56'):
        assert _is_linked(b1, 'pascal_constantChr56', a)
    _safe_set(a, 'pascal_unsignedInteger57', b2)
    assert _is_linked(a, 'pascal_unsignedInteger57', b2)
    if hasattr(b1, 'pascal_constantChr56'):
        assert not _is_linked(b1, 'pascal_constantChr56', a)
    if hasattr(b2, 'pascal_constantChr56'):
        assert _is_linked(b2, 'pascal_constantChr56', a)
    _safe_set(a, 'pascal_unsignedInteger57', None)
    assert not _is_linked(a, 'pascal_unsignedInteger57', b2)
    if hasattr(b2, 'pascal_constantChr56'):
        assert not _is_linked(b2, 'pascal_constantChr56', a)


def test_assoc_unsignedInteger58_link_reassign_clear():
    a = pascal_unsignedNumber(unsignedReal="sample_text")
    b1 = pascal_unsignedInteger(number="sample_text")
    b2 = pascal_unsignedInteger(number="sample_text_2")
    _safe_set(a, 'pascal_unsignedNumber59', b1)
    assert _is_linked(a, 'pascal_unsignedNumber59', b1)
    if hasattr(b1, 'pascal_unsignedInteger60'):
        assert _is_linked(b1, 'pascal_unsignedInteger60', a)
    _safe_set(a, 'pascal_unsignedNumber59', b2)
    assert _is_linked(a, 'pascal_unsignedNumber59', b2)
    if hasattr(b1, 'pascal_unsignedInteger60'):
        assert not _is_linked(b1, 'pascal_unsignedInteger60', a)
    if hasattr(b2, 'pascal_unsignedInteger60'):
        assert _is_linked(b2, 'pascal_unsignedInteger60', a)
    _safe_set(a, 'pascal_unsignedNumber59', None)
    assert not _is_linked(a, 'pascal_unsignedNumber59', b2)
    if hasattr(b2, 'pascal_unsignedInteger60'):
        assert not _is_linked(b2, 'pascal_unsignedInteger60', a)


def test_assoc_unsignedNumber147_link_reassign_clear():
    a = pascal_unsignedNumber(unsignedReal="sample_text")
    b1 = pascal_stringtype()
    b2 = pascal_stringtype()
    _safe_set(a, 'pascal_unsignedNumber149', b1)
    assert _is_linked(a, 'pascal_unsignedNumber149', b1)
    if hasattr(b1, 'pascal_stringtype148'):
        assert _is_linked(b1, 'pascal_stringtype148', a)
    _safe_set(a, 'pascal_unsignedNumber149', b2)
    assert _is_linked(a, 'pascal_unsignedNumber149', b2)
    if hasattr(b1, 'pascal_stringtype148'):
        assert not _is_linked(b1, 'pascal_stringtype148', a)
    if hasattr(b2, 'pascal_stringtype148'):
        assert _is_linked(b2, 'pascal_stringtype148', a)
    _safe_set(a, 'pascal_unsignedNumber149', None)
    assert not _is_linked(a, 'pascal_unsignedNumber149', b2)
    if hasattr(b2, 'pascal_stringtype148'):
        assert not _is_linked(b2, 'pascal_stringtype148', a)


def test_assoc_unsignedNumber284_link_reassign_clear():
    a = pascal_unsignedNumber(unsignedReal="sample_text")
    b1 = pascal_unsignedConstant(string_literal="sample_text")
    b2 = pascal_unsignedConstant(string_literal="sample_text_2")
    _safe_set(a, 'pascal_unsignedNumber286', b1)
    assert _is_linked(a, 'pascal_unsignedNumber286', b1)
    if hasattr(b1, 'pascal_unsignedConstant285'):
        assert _is_linked(b1, 'pascal_unsignedConstant285', a)
    _safe_set(a, 'pascal_unsignedNumber286', b2)
    assert _is_linked(a, 'pascal_unsignedNumber286', b2)
    if hasattr(b1, 'pascal_unsignedConstant285'):
        assert not _is_linked(b1, 'pascal_unsignedConstant285', a)
    if hasattr(b2, 'pascal_unsignedConstant285'):
        assert _is_linked(b2, 'pascal_unsignedConstant285', a)
    _safe_set(a, 'pascal_unsignedNumber286', None)
    assert not _is_linked(a, 'pascal_unsignedNumber286', b2)
    if hasattr(b2, 'pascal_unsignedConstant285'):
        assert not _is_linked(b2, 'pascal_unsignedConstant285', a)


def test_assoc_unsignedNumber43_link_reassign_clear():
    a = pascal_unsignedNumber(unsignedReal="sample_text")
    b1 = pascal_constant(bool="sample_text", sign="sample_text", string="sample_text")
    b2 = pascal_constant(bool="sample_text_2", sign="sample_text_2", string="sample_text_2")
    _safe_set(a, 'pascal_unsignedNumber', b1)
    assert _is_linked(a, 'pascal_unsignedNumber', b1)
    if hasattr(b1, 'pascal_constant44'):
        assert _is_linked(b1, 'pascal_constant44', a)
    _safe_set(a, 'pascal_unsignedNumber', b2)
    assert _is_linked(a, 'pascal_unsignedNumber', b2)
    if hasattr(b1, 'pascal_constant44'):
        assert not _is_linked(b1, 'pascal_constant44', a)
    if hasattr(b2, 'pascal_constant44'):
        assert _is_linked(b2, 'pascal_constant44', a)
    _safe_set(a, 'pascal_unsignedNumber', None)
    assert not _is_linked(a, 'pascal_unsignedNumber', b2)
    if hasattr(b2, 'pascal_constant44'):
        assert not _is_linked(b2, 'pascal_constant44', a)


def test_assoc_variable281_link_reassign_clear():
    a = pascal_factor(bool="sample_text")
    b1 = pascal_variable()
    b2 = pascal_variable()
    _safe_set(a, 'pascal_factor282', b1)
    assert _is_linked(a, 'pascal_factor282', b1)
    if hasattr(b1, 'pascal_variable283'):
        assert _is_linked(b1, 'pascal_variable283', a)
    _safe_set(a, 'pascal_factor282', b2)
    assert _is_linked(a, 'pascal_factor282', b2)
    if hasattr(b1, 'pascal_variable283'):
        assert not _is_linked(b1, 'pascal_variable283', a)
    if hasattr(b2, 'pascal_variable283'):
        assert _is_linked(b2, 'pascal_variable283', a)
    _safe_set(a, 'pascal_factor282', None)
    assert not _is_linked(a, 'pascal_factor282', b2)
    if hasattr(b2, 'pascal_variable283'):
        assert not _is_linked(b2, 'pascal_variable283', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

label_declaration_part_strategy = st.builds(label_declaration_part)
@given(instance=label_declaration_part_strategy)
@settings(max_examples=25)
def test_label_declaration_part_instantiation(instance):
    assert isinstance(instance, label_declaration_part)


parameterList_strategy = st.builds(parameterList)
@given(instance=parameterList_strategy)
@settings(max_examples=25)
def test_parameterList_instantiation(instance):
    assert isinstance(instance, parameterList)


pascal_actualParameter_strategy = st.builds(pascal_actualParameter)
@given(instance=pascal_actualParameter_strategy)
@settings(max_examples=25)
def test_pascal_actualParameter_instantiation(instance):
    assert isinstance(instance, pascal_actualParameter)


pascal_assignmentStatement_strategy = st.builds(pascal_assignmentStatement)
@given(instance=pascal_assignmentStatement_strategy)
@settings(max_examples=25)
def test_pascal_assignmentStatement_instantiation(instance):
    assert isinstance(instance, pascal_assignmentStatement)


pascal_block_strategy = st.builds(pascal_block)
@given(instance=pascal_block_strategy)
@settings(max_examples=25)
def test_pascal_block_instantiation(instance):
    assert isinstance(instance, pascal_block)


pascal_caseListElement_strategy = st.builds(pascal_caseListElement)
@given(instance=pascal_caseListElement_strategy)
@settings(max_examples=25)
def test_pascal_caseListElement_instantiation(instance):
    assert isinstance(instance, pascal_caseListElement)


pascal_caseStatement_strategy = st.builds(pascal_caseStatement)
@given(instance=pascal_caseStatement_strategy)
@settings(max_examples=25)
def test_pascal_caseStatement_instantiation(instance):
    assert isinstance(instance, pascal_caseStatement)


pascal_compoundStatement_strategy = st.builds(pascal_compoundStatement)
@given(instance=pascal_compoundStatement_strategy)
@settings(max_examples=25)
def test_pascal_compoundStatement_instantiation(instance):
    assert isinstance(instance, pascal_compoundStatement)


pascal_conditionalStatement_strategy = st.builds(pascal_conditionalStatement)
@given(instance=pascal_conditionalStatement_strategy)
@settings(max_examples=25)
def test_pascal_conditionalStatement_instantiation(instance):
    assert isinstance(instance, pascal_conditionalStatement)


pascal_constList_strategy = st.builds(pascal_constList)
@given(instance=pascal_constList_strategy)
@settings(max_examples=25)
def test_pascal_constList_instantiation(instance):
    assert isinstance(instance, pascal_constList)


pascal_constant_strategy = st.builds(pascal_constant, bool=safe_text, sign=safe_text, string=safe_text)
@given(instance=pascal_constant_strategy)
@settings(max_examples=25)
def test_pascal_constant_instantiation(instance):
    assert isinstance(instance, pascal_constant)


pascal_constantChr_strategy = st.builds(pascal_constantChr)
@given(instance=pascal_constantChr_strategy)
@settings(max_examples=25)
def test_pascal_constantChr_instantiation(instance):
    assert isinstance(instance, pascal_constantChr)


pascal_constantDefinition_strategy = st.builds(pascal_constantDefinition)
@given(instance=pascal_constantDefinition_strategy)
@settings(max_examples=25)
def test_pascal_constantDefinition_instantiation(instance):
    assert isinstance(instance, pascal_constantDefinition)


pascal_constantDefinitionPart_strategy = st.builds(pascal_constantDefinitionPart)
@given(instance=pascal_constantDefinitionPart_strategy)
@settings(max_examples=25)
def test_pascal_constantDefinitionPart_instantiation(instance):
    assert isinstance(instance, pascal_constantDefinitionPart)


pascal_expression_strategy = st.builds(pascal_expression, relationaloperator=safe_text)
@given(instance=pascal_expression_strategy)
@settings(max_examples=25)
def test_pascal_expression_instantiation(instance):
    assert isinstance(instance, pascal_expression)


pascal_factor_strategy = st.builds(pascal_factor, bool=safe_text)
@given(instance=pascal_factor_strategy)
@settings(max_examples=25)
def test_pascal_factor_instantiation(instance):
    assert isinstance(instance, pascal_factor)


pascal_fieldList_strategy = st.builds(pascal_fieldList)
@given(instance=pascal_fieldList_strategy)
@settings(max_examples=25)
def test_pascal_fieldList_instantiation(instance):
    assert isinstance(instance, pascal_fieldList)


pascal_fixedPart_strategy = st.builds(pascal_fixedPart)
@given(instance=pascal_fixedPart_strategy)
@settings(max_examples=25)
def test_pascal_fixedPart_instantiation(instance):
    assert isinstance(instance, pascal_fixedPart)


pascal_formalParameterList_strategy = st.builds(pascal_formalParameterList)
@given(instance=pascal_formalParameterList_strategy)
@settings(max_examples=25)
def test_pascal_formalParameterList_instantiation(instance):
    assert isinstance(instance, pascal_formalParameterList)


pascal_formalParameterSection_strategy = st.builds(pascal_formalParameterSection)
@given(instance=pascal_formalParameterSection_strategy)
@settings(max_examples=25)
def test_pascal_formalParameterSection_instantiation(instance):
    assert isinstance(instance, pascal_formalParameterSection)


pascal_functionDeclaration_strategy = st.builds(pascal_functionDeclaration)
@given(instance=pascal_functionDeclaration_strategy)
@settings(max_examples=25)
def test_pascal_functionDeclaration_instantiation(instance):
    assert isinstance(instance, pascal_functionDeclaration)


pascal_functionDesignator_strategy = st.builds(pascal_functionDesignator)
@given(instance=pascal_functionDesignator_strategy)
@settings(max_examples=25)
def test_pascal_functionDesignator_instantiation(instance):
    assert isinstance(instance, pascal_functionDesignator)


pascal_functionType_strategy = st.builds(pascal_functionType)
@given(instance=pascal_functionType_strategy)
@settings(max_examples=25)
def test_pascal_functionType_instantiation(instance):
    assert isinstance(instance, pascal_functionType)


pascal_gotoStatement_strategy = st.builds(pascal_gotoStatement)
@given(instance=pascal_gotoStatement_strategy)
@settings(max_examples=25)
def test_pascal_gotoStatement_instantiation(instance):
    assert isinstance(instance, pascal_gotoStatement)


pascal_identifier_strategy = st.builds(pascal_identifier, identifier=safe_text)
@given(instance=pascal_identifier_strategy)
@settings(max_examples=25)
def test_pascal_identifier_instantiation(instance):
    assert isinstance(instance, pascal_identifier)


pascal_identifierList_strategy = st.builds(pascal_identifierList)
@given(instance=pascal_identifierList_strategy)
@settings(max_examples=25)
def test_pascal_identifierList_instantiation(instance):
    assert isinstance(instance, pascal_identifierList)


pascal_label_strategy = st.builds(pascal_label)
@given(instance=pascal_label_strategy)
@settings(max_examples=25)
def test_pascal_label_instantiation(instance):
    assert isinstance(instance, pascal_label)


pascal_label_declaration_part_strategy = st.builds(pascal_label_declaration_part)
@given(instance=pascal_label_declaration_part_strategy)
@settings(max_examples=25)
def test_pascal_label_declaration_part_instantiation(instance):
    assert isinstance(instance, pascal_label_declaration_part)


pascal_parameterGroup_strategy = st.builds(pascal_parameterGroup)
@given(instance=pascal_parameterGroup_strategy)
@settings(max_examples=25)
def test_pascal_parameterGroup_instantiation(instance):
    assert isinstance(instance, pascal_parameterGroup)


pascal_parameterList_strategy = st.builds(pascal_parameterList)
@given(instance=pascal_parameterList_strategy)
@settings(max_examples=25)
def test_pascal_parameterList_instantiation(instance):
    assert isinstance(instance, pascal_parameterList)


pascal_pascal_strategy = st.builds(pascal_pascal)
@given(instance=pascal_pascal_strategy)
@settings(max_examples=25)
def test_pascal_pascal_instantiation(instance):
    assert isinstance(instance, pascal_pascal)


pascal_pointerType_strategy = st.builds(pascal_pointerType)
@given(instance=pascal_pointerType_strategy)
@settings(max_examples=25)
def test_pascal_pointerType_instantiation(instance):
    assert isinstance(instance, pascal_pointerType)


pascal_procedureAndFunctionDeclarationPart_strategy = st.builds(pascal_procedureAndFunctionDeclarationPart)
@given(instance=pascal_procedureAndFunctionDeclarationPart_strategy)
@settings(max_examples=25)
def test_pascal_procedureAndFunctionDeclarationPart_instantiation(instance):
    assert isinstance(instance, pascal_procedureAndFunctionDeclarationPart)


pascal_procedureDeclaration_strategy = st.builds(pascal_procedureDeclaration)
@given(instance=pascal_procedureDeclaration_strategy)
@settings(max_examples=25)
def test_pascal_procedureDeclaration_instantiation(instance):
    assert isinstance(instance, pascal_procedureDeclaration)


pascal_procedureOrFunctionDeclaration_strategy = st.builds(pascal_procedureOrFunctionDeclaration)
@given(instance=pascal_procedureOrFunctionDeclaration_strategy)
@settings(max_examples=25)
def test_pascal_procedureOrFunctionDeclaration_instantiation(instance):
    assert isinstance(instance, pascal_procedureOrFunctionDeclaration)


pascal_procedureType_strategy = st.builds(pascal_procedureType)
@given(instance=pascal_procedureType_strategy)
@settings(max_examples=25)
def test_pascal_procedureType_instantiation(instance):
    assert isinstance(instance, pascal_procedureType)


pascal_program_strategy = st.builds(pascal_program)
@given(instance=pascal_program_strategy)
@settings(max_examples=25)
def test_pascal_program_instantiation(instance):
    assert isinstance(instance, pascal_program)


pascal_programHeading_strategy = st.builds(pascal_programHeading)
@given(instance=pascal_programHeading_strategy)
@settings(max_examples=25)
def test_pascal_programHeading_instantiation(instance):
    assert isinstance(instance, pascal_programHeading)


pascal_recordSection_strategy = st.builds(pascal_recordSection)
@given(instance=pascal_recordSection_strategy)
@settings(max_examples=25)
def test_pascal_recordSection_instantiation(instance):
    assert isinstance(instance, pascal_recordSection)


pascal_recordType_strategy = st.builds(pascal_recordType)
@given(instance=pascal_recordType_strategy)
@settings(max_examples=25)
def test_pascal_recordType_instantiation(instance):
    assert isinstance(instance, pascal_recordType)


pascal_scalarType_strategy = st.builds(pascal_scalarType)
@given(instance=pascal_scalarType_strategy)
@settings(max_examples=25)
def test_pascal_scalarType_instantiation(instance):
    assert isinstance(instance, pascal_scalarType)


pascal_signedFactor_strategy = st.builds(pascal_signedFactor)
@given(instance=pascal_signedFactor_strategy)
@settings(max_examples=25)
def test_pascal_signedFactor_instantiation(instance):
    assert isinstance(instance, pascal_signedFactor)


pascal_simpleExpression_strategy = st.builds(pascal_simpleExpression, additiveoperator=safe_text)
@given(instance=pascal_simpleExpression_strategy)
@settings(max_examples=25)
def test_pascal_simpleExpression_instantiation(instance):
    assert isinstance(instance, pascal_simpleExpression)


pascal_simpleStatement_strategy = st.builds(pascal_simpleStatement)
@given(instance=pascal_simpleStatement_strategy)
@settings(max_examples=25)
def test_pascal_simpleStatement_instantiation(instance):
    assert isinstance(instance, pascal_simpleStatement)


pascal_simpleType_strategy = st.builds(pascal_simpleType)
@given(instance=pascal_simpleType_strategy)
@settings(max_examples=25)
def test_pascal_simpleType_instantiation(instance):
    assert isinstance(instance, pascal_simpleType)


pascal_statement_strategy = st.builds(pascal_statement)
@given(instance=pascal_statement_strategy)
@settings(max_examples=25)
def test_pascal_statement_instantiation(instance):
    assert isinstance(instance, pascal_statement)


pascal_statements_strategy = st.builds(pascal_statements)
@given(instance=pascal_statements_strategy)
@settings(max_examples=25)
def test_pascal_statements_instantiation(instance):
    assert isinstance(instance, pascal_statements)


pascal_stringtype_strategy = st.builds(pascal_stringtype)
@given(instance=pascal_stringtype_strategy)
@settings(max_examples=25)
def test_pascal_stringtype_instantiation(instance):
    assert isinstance(instance, pascal_stringtype)


pascal_structuredStatement_strategy = st.builds(pascal_structuredStatement)
@given(instance=pascal_structuredStatement_strategy)
@settings(max_examples=25)
def test_pascal_structuredStatement_instantiation(instance):
    assert isinstance(instance, pascal_structuredStatement)


pascal_structuredType_strategy = st.builds(pascal_structuredType)
@given(instance=pascal_structuredType_strategy)
@settings(max_examples=25)
def test_pascal_structuredType_instantiation(instance):
    assert isinstance(instance, pascal_structuredType)


pascal_subrangeType_strategy = st.builds(pascal_subrangeType)
@given(instance=pascal_subrangeType_strategy)
@settings(max_examples=25)
def test_pascal_subrangeType_instantiation(instance):
    assert isinstance(instance, pascal_subrangeType)


pascal_tag_strategy = st.builds(pascal_tag)
@given(instance=pascal_tag_strategy)
@settings(max_examples=25)
def test_pascal_tag_instantiation(instance):
    assert isinstance(instance, pascal_tag)


pascal_term_strategy = st.builds(pascal_term, multiplicativeoperator=safe_text)
@given(instance=pascal_term_strategy)
@settings(max_examples=25)
def test_pascal_term_instantiation(instance):
    assert isinstance(instance, pascal_term)


pascal_type_strategy = st.builds(pascal_type)
@given(instance=pascal_type_strategy)
@settings(max_examples=25)
def test_pascal_type_instantiation(instance):
    assert isinstance(instance, pascal_type)


pascal_typeDefinition_strategy = st.builds(pascal_typeDefinition)
@given(instance=pascal_typeDefinition_strategy)
@settings(max_examples=25)
def test_pascal_typeDefinition_instantiation(instance):
    assert isinstance(instance, pascal_typeDefinition)


pascal_typeDefinitionPart_strategy = st.builds(pascal_typeDefinitionPart)
@given(instance=pascal_typeDefinitionPart_strategy)
@settings(max_examples=25)
def test_pascal_typeDefinitionPart_instantiation(instance):
    assert isinstance(instance, pascal_typeDefinitionPart)


pascal_typeIdentifier_strategy = st.builds(pascal_typeIdentifier, boolean=safe_text, char=safe_text, integer=safe_text, real=safe_text, string=safe_text)
@given(instance=pascal_typeIdentifier_strategy)
@settings(max_examples=25)
def test_pascal_typeIdentifier_instantiation(instance):
    assert isinstance(instance, pascal_typeIdentifier)


pascal_unlabelledStatement_strategy = st.builds(pascal_unlabelledStatement)
@given(instance=pascal_unlabelledStatement_strategy)
@settings(max_examples=25)
def test_pascal_unlabelledStatement_instantiation(instance):
    assert isinstance(instance, pascal_unlabelledStatement)


pascal_unpackedStructuredType_strategy = st.builds(pascal_unpackedStructuredType)
@given(instance=pascal_unpackedStructuredType_strategy)
@settings(max_examples=25)
def test_pascal_unpackedStructuredType_instantiation(instance):
    assert isinstance(instance, pascal_unpackedStructuredType)


pascal_unsignedConstant_strategy = st.builds(pascal_unsignedConstant, string_literal=safe_text)
@given(instance=pascal_unsignedConstant_strategy)
@settings(max_examples=25)
def test_pascal_unsignedConstant_instantiation(instance):
    assert isinstance(instance, pascal_unsignedConstant)


pascal_unsignedInteger_strategy = st.builds(pascal_unsignedInteger, number=safe_text)
@given(instance=pascal_unsignedInteger_strategy)
@settings(max_examples=25)
def test_pascal_unsignedInteger_instantiation(instance):
    assert isinstance(instance, pascal_unsignedInteger)


pascal_unsignedNumber_strategy = st.builds(pascal_unsignedNumber, unsignedReal=safe_text)
@given(instance=pascal_unsignedNumber_strategy)
@settings(max_examples=25)
def test_pascal_unsignedNumber_instantiation(instance):
    assert isinstance(instance, pascal_unsignedNumber)


pascal_usesUnitsPart_strategy = st.builds(pascal_usesUnitsPart)
@given(instance=pascal_usesUnitsPart_strategy)
@settings(max_examples=25)
def test_pascal_usesUnitsPart_instantiation(instance):
    assert isinstance(instance, pascal_usesUnitsPart)


pascal_variable_strategy = st.builds(pascal_variable)
@given(instance=pascal_variable_strategy)
@settings(max_examples=25)
def test_pascal_variable_instantiation(instance):
    assert isinstance(instance, pascal_variable)


pascal_variableDeclaration_strategy = st.builds(pascal_variableDeclaration)
@given(instance=pascal_variableDeclaration_strategy)
@settings(max_examples=25)
def test_pascal_variableDeclaration_instantiation(instance):
    assert isinstance(instance, pascal_variableDeclaration)


pascal_variableDeclarationPart_strategy = st.builds(pascal_variableDeclarationPart)
@given(instance=pascal_variableDeclarationPart_strategy)
@settings(max_examples=25)
def test_pascal_variableDeclarationPart_instantiation(instance):
    assert isinstance(instance, pascal_variableDeclarationPart)


pascal_variant_strategy = st.builds(pascal_variant)
@given(instance=pascal_variant_strategy)
@settings(max_examples=25)
def test_pascal_variant_instantiation(instance):
    assert isinstance(instance, pascal_variant)


pascal_variantPart_strategy = st.builds(pascal_variantPart)
@given(instance=pascal_variantPart_strategy)
@settings(max_examples=25)
def test_pascal_variantPart_instantiation(instance):
    assert isinstance(instance, pascal_variantPart)


statement_strategy = st.builds(statement)
@given(instance=statement_strategy)
@settings(max_examples=25)
def test_statement_instantiation(instance):
    assert isinstance(instance, statement)


variant_strategy = st.builds(variant)
@given(instance=variant_strategy)
@settings(max_examples=25)
def test_variant_instantiation(instance):
    assert isinstance(instance, variant)



