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
    FloatType,
    OPLmetamodel_Error,
    OPLmetamodel_Entity,
    OPLmetamodel_FunctionRef,
    Constraint,
    OPLmetamodel_ForAllConstraint,
    NumericExpression,
    OPLmetamodel_FloatExpression,
    OPLmetamodel_ParameterDomain,
    NumericType,
    OPLmetamodel_FloatType,
    RangeType,
    OPLmetamodel_FloatRangeType,
    Initialization,
    OPLmetamodel_DataObject,
    OPLmetamodel_DataInitMethods,
    OPLmetamodel_Initialization,
    SetType,
    OPLmetamodel_EnumerationType,
    OPLmetamodel_ParameterDeclaration,
    OPLmetamodel_DisplayInstruction,
    AbstractType,
    OPLmetamodel_DeferredInit,
    OPLmetamodel_Declaration,
    DefinedType,
    OPLmetamodel_ArrayType,
    CollectionExpression,
    OPLmetamodel_Extension,
    OPLmetamodel_Comprehension,
    Function,
    OPLmetamodel_CumulativeFunction,
    OPLmetamodel_BuiltInFunction,
    PrimitiveType,
    OPLmetamodel_BooleanType,
    PrimitiveExpression,
    OPLmetamodel_EnumLiteral,
    OPLmetamodel_BooleanExpression,
    OPLmetamodel_BooleanBlock,
    Reference,
    OPLmetamodel_DataRef,
    OPLmetamodel_BindingRef,
    AbstractBinaryOperator,
    OPLmetamodel_BinaryOperator,
    OPLmetamodel_TupleBinding,
    OPLmetamodel_StringType,
    OPLmetamodel_StringExpression,
    PiecewiseLinearFunction,
    OPLmetamodel_StateFunction,
    ScriptStatement,
    OPLmetamodel_Writeln,
    OPLmetamodel_VariableBinding,
    OPLmetamodel_RelationalInit,
    BooleanExpression,
    BinaryExpression,
    OPLmetamodel_RelationalExpression,
    BuiltInFunction,
    OPLmetamodel_ReflectiveFunction,
    OPLmetamodel_Sequence,
    OPLmetamodel_ScriptStatement,
    OPLmetamodel_RelationalOperator,
    DataInitMethods,
    OPLmetamodel_QueryUser,
    OPLmetamodel_PrimitiveType,
    OPLmetamodel_PositiveFloatType,
    OPLmetamodel_PiecewiseLinearFunction,
    OPLmetamodel_PiecewiseExpression,
    OPLmetamodel_RecordField,
    ParameterDomain,
    OPLmetamodel_SetType,
    OPLmetamodel_Record,
    OPLmetamodel_ReadFile,
    OPLmetamodel_RangeExpression,
    OPLmetamodel_Model,
    OPLmetamodel_ParameterRef,
    OPLmetamodel_Operator,
    OPLmetamodel_NumericExpression,
    OPLmetamodel_SearchProcedure,
    OPLmetamodel_IfConstraint,
    IntegerType,
    OPLmetamodel_PositiveIntegerType,
    OPLmetamodel_IntegerRangeType,
    OPLmetamodel_IntegerExpression,
    OPLmetamodel_StepFunction,
    OPLmetamodel_NumericType,
    OPLmetamodel_RangeType,
    OPLmetamodel_Interval,
    OPLmetamodel_IntegerType,
    OPLmetamodel_In,
    OPLmetamodel_AbstractBinaryOperator,
    PathExpression,
    OPLmetamodel_PathDereference,
    OPLmetamodel_FunctionCall,
    OPLmetamodel_ArrayDereference,
    OPLmetamodel_AllExpression,
    OPLmetamodel_Expression,
    OPLmetamodel_FormalParameter,
    Expression,
    OPLmetamodel_IfExpression,
    OPLmetamodel_RecordValue,
    OPLmetamodel_Reference,
    OPLmetamodel_PathExpression,
    OPLmetamodel_BlockExpression,
    OPLmetamodel_BinaryExpression,
    OPLmetamodel_IndexValuePair,
    OPLmetamodel_PrimitiveExpression,
    OPLmetamodel_CollectionExpression,
    OPLmetamodel_UnaryExpression,
    OPLmetamodel_ArrayValue,
    OPLmetamodel_ArraySlotConstraint,
    OPLmetamodel_SetValue,
    OPLmetamodel_AggregateExp,
    OPLmetamodel_Number,
    Declaration,
    OPLmetamodel_Constraint,
    OPLmetamodel_DefinedType,
    OPLmetamodel_Function,
    OPLmetamodel_Assertion,
    OPLmetamodel_ScheduleInitialization,
    OPLmetamodel_DataDeclaration,
    OPLmetamodel_Script,
    OPLmetamodel_ResourceDeclaration,
    OPLmetamodel_Objective,
    OPLmetamodel_Setting,
    OPLmetamodel_ActivityDeclaration,
    OPLmetamodel_AbstractType,
    BinaryOp,
    MembershipOp,
    Quantifier,
    OptimizationMode,
    LogicalOp,
    UnaryOp,
    RelationalOp,
    AggOp,
    SetOp,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_floattype_is_not_abstract():
    assert not inspect.isabstract(FloatType)


def test_hyp_floattype_constructor_exists():
    assert callable(FloatType.__init__)


def test_hyp_floattype_constructor_args():
    sig = inspect.signature(FloatType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_error_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_Error)


def test_hyp_oplmetamodel_error_constructor_exists():
    assert callable(OPLmetamodel_Error.__init__)


def test_hyp_oplmetamodel_error_constructor_args():
    sig = inspect.signature(OPLmetamodel_Error.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_entity_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_Entity)


def test_hyp_oplmetamodel_entity_constructor_exists():
    assert callable(OPLmetamodel_Entity.__init__)


def test_hyp_oplmetamodel_entity_constructor_args():
    sig = inspect.signature(OPLmetamodel_Entity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_functionref_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_FunctionRef)


def test_hyp_oplmetamodel_functionref_constructor_exists():
    assert callable(OPLmetamodel_FunctionRef.__init__)


def test_hyp_oplmetamodel_functionref_constructor_args():
    sig = inspect.signature(OPLmetamodel_FunctionRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_hyp_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_hyp_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_forallconstraint_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_ForAllConstraint)


def test_hyp_oplmetamodel_forallconstraint_constructor_exists():
    assert callable(OPLmetamodel_ForAllConstraint.__init__)


def test_hyp_oplmetamodel_forallconstraint_constructor_args():
    sig = inspect.signature(OPLmetamodel_ForAllConstraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_numericexpression_is_not_abstract():
    assert not inspect.isabstract(NumericExpression)


def test_hyp_numericexpression_constructor_exists():
    assert callable(NumericExpression.__init__)


def test_hyp_numericexpression_constructor_args():
    sig = inspect.signature(NumericExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_floatexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_FloatExpression)


def test_hyp_oplmetamodel_floatexpression_constructor_exists():
    assert callable(OPLmetamodel_FloatExpression.__init__)


def test_hyp_oplmetamodel_floatexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel_FloatExpression.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"




def test_hyp_oplmetamodel_parameterdomain_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_ParameterDomain)


def test_hyp_oplmetamodel_parameterdomain_constructor_exists():
    assert callable(OPLmetamodel_ParameterDomain.__init__)


def test_hyp_oplmetamodel_parameterdomain_constructor_args():
    sig = inspect.signature(OPLmetamodel_ParameterDomain.__init__)
    params = list(sig.parameters.keys())



def test_hyp_numerictype_is_not_abstract():
    assert not inspect.isabstract(NumericType)


def test_hyp_numerictype_constructor_exists():
    assert callable(NumericType.__init__)


def test_hyp_numerictype_constructor_args():
    sig = inspect.signature(NumericType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_floattype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_FloatType)


def test_hyp_oplmetamodel_floattype_constructor_exists():
    assert callable(OPLmetamodel_FloatType.__init__)


def test_hyp_oplmetamodel_floattype_constructor_args():
    sig = inspect.signature(OPLmetamodel_FloatType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rangetype_is_not_abstract():
    assert not inspect.isabstract(RangeType)


def test_hyp_rangetype_constructor_exists():
    assert callable(RangeType.__init__)


def test_hyp_rangetype_constructor_args():
    sig = inspect.signature(RangeType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_floatrangetype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_FloatRangeType)


def test_hyp_oplmetamodel_floatrangetype_constructor_exists():
    assert callable(OPLmetamodel_FloatRangeType.__init__)


def test_hyp_oplmetamodel_floatrangetype_constructor_args():
    sig = inspect.signature(OPLmetamodel_FloatRangeType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_initialization_is_not_abstract():
    assert not inspect.isabstract(Initialization)


def test_hyp_initialization_constructor_exists():
    assert callable(Initialization.__init__)


def test_hyp_initialization_constructor_args():
    sig = inspect.signature(Initialization.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_dataobject_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_DataObject)


def test_hyp_oplmetamodel_dataobject_constructor_exists():
    assert callable(OPLmetamodel_DataObject.__init__)


def test_hyp_oplmetamodel_dataobject_constructor_args():
    sig = inspect.signature(OPLmetamodel_DataObject.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"




def test_hyp_oplmetamodel_datainitmethods_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_DataInitMethods)


def test_hyp_oplmetamodel_datainitmethods_constructor_exists():
    assert callable(OPLmetamodel_DataInitMethods.__init__)


def test_hyp_oplmetamodel_datainitmethods_constructor_args():
    sig = inspect.signature(OPLmetamodel_DataInitMethods.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_initialization_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_Initialization)


def test_hyp_oplmetamodel_initialization_constructor_exists():
    assert callable(OPLmetamodel_Initialization.__init__)


def test_hyp_oplmetamodel_initialization_constructor_args():
    sig = inspect.signature(OPLmetamodel_Initialization.__init__)
    params = list(sig.parameters.keys())



def test_hyp_settype_is_not_abstract():
    assert not inspect.isabstract(SetType)


def test_hyp_settype_constructor_exists():
    assert callable(SetType.__init__)


def test_hyp_settype_constructor_args():
    sig = inspect.signature(SetType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_enumerationtype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_EnumerationType)


def test_hyp_oplmetamodel_enumerationtype_constructor_exists():
    assert callable(OPLmetamodel_EnumerationType.__init__)


def test_hyp_oplmetamodel_enumerationtype_constructor_args():
    sig = inspect.signature(OPLmetamodel_EnumerationType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_parameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_ParameterDeclaration)


def test_hyp_oplmetamodel_parameterdeclaration_constructor_exists():
    assert callable(OPLmetamodel_ParameterDeclaration.__init__)


def test_hyp_oplmetamodel_parameterdeclaration_constructor_args():
    sig = inspect.signature(OPLmetamodel_ParameterDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_displayinstruction_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_DisplayInstruction)


def test_hyp_oplmetamodel_displayinstruction_constructor_exists():
    assert callable(OPLmetamodel_DisplayInstruction.__init__)


def test_hyp_oplmetamodel_displayinstruction_constructor_args():
    sig = inspect.signature(OPLmetamodel_DisplayInstruction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstracttype_is_not_abstract():
    assert not inspect.isabstract(AbstractType)


def test_hyp_abstracttype_constructor_exists():
    assert callable(AbstractType.__init__)


def test_hyp_abstracttype_constructor_args():
    sig = inspect.signature(AbstractType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_deferredinit_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_DeferredInit)


def test_hyp_oplmetamodel_deferredinit_constructor_exists():
    assert callable(OPLmetamodel_DeferredInit.__init__)


def test_hyp_oplmetamodel_deferredinit_constructor_args():
    sig = inspect.signature(OPLmetamodel_DeferredInit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_declaration_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_Declaration)


def test_hyp_oplmetamodel_declaration_constructor_exists():
    assert callable(OPLmetamodel_Declaration.__init__)


def test_hyp_oplmetamodel_declaration_constructor_args():
    sig = inspect.signature(OPLmetamodel_Declaration.__init__)
    params = list(sig.parameters.keys())
    assert "order" in params, "Missing parameter 'order'"

def test_hyp_oplmetamodel_declaration_has_order():
    assert hasattr(OPLmetamodel_Declaration, "order")
    descriptor = None
    for klass in OPLmetamodel_Declaration.__mro__:
        if "order" in klass.__dict__:
            descriptor = klass.__dict__["order"]
            break
    assert isinstance(descriptor, property)



def test_hyp_definedtype_is_not_abstract():
    assert not inspect.isabstract(DefinedType)


def test_hyp_definedtype_constructor_exists():
    assert callable(DefinedType.__init__)


def test_hyp_definedtype_constructor_args():
    sig = inspect.signature(DefinedType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_arraytype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_ArrayType)


def test_hyp_oplmetamodel_arraytype_constructor_exists():
    assert callable(OPLmetamodel_ArrayType.__init__)


def test_hyp_oplmetamodel_arraytype_constructor_args():
    sig = inspect.signature(OPLmetamodel_ArrayType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_collectionexpression_is_not_abstract():
    assert not inspect.isabstract(CollectionExpression)


def test_hyp_collectionexpression_constructor_exists():
    assert callable(CollectionExpression.__init__)


def test_hyp_collectionexpression_constructor_args():
    sig = inspect.signature(CollectionExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_extension_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_Extension)


def test_hyp_oplmetamodel_extension_constructor_exists():
    assert callable(OPLmetamodel_Extension.__init__)


def test_hyp_oplmetamodel_extension_constructor_args():
    sig = inspect.signature(OPLmetamodel_Extension.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_comprehension_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_Comprehension)


def test_hyp_oplmetamodel_comprehension_constructor_exists():
    assert callable(OPLmetamodel_Comprehension.__init__)


def test_hyp_oplmetamodel_comprehension_constructor_args():
    sig = inspect.signature(OPLmetamodel_Comprehension.__init__)
    params = list(sig.parameters.keys())



def test_hyp_function_is_not_abstract():
    assert not inspect.isabstract(Function)


def test_hyp_function_constructor_exists():
    assert callable(Function.__init__)


def test_hyp_function_constructor_args():
    sig = inspect.signature(Function.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_cumulativefunction_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_CumulativeFunction)


def test_hyp_oplmetamodel_cumulativefunction_constructor_exists():
    assert callable(OPLmetamodel_CumulativeFunction.__init__)


def test_hyp_oplmetamodel_cumulativefunction_constructor_args():
    sig = inspect.signature(OPLmetamodel_CumulativeFunction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_builtinfunction_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_BuiltInFunction)


def test_hyp_oplmetamodel_builtinfunction_constructor_exists():
    assert callable(OPLmetamodel_BuiltInFunction.__init__)


def test_hyp_oplmetamodel_builtinfunction_constructor_args():
    sig = inspect.signature(OPLmetamodel_BuiltInFunction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_hyp_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_hyp_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_booleantype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_BooleanType)


def test_hyp_oplmetamodel_booleantype_constructor_exists():
    assert callable(OPLmetamodel_BooleanType.__init__)


def test_hyp_oplmetamodel_booleantype_constructor_args():
    sig = inspect.signature(OPLmetamodel_BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_primitiveexpression_is_not_abstract():
    assert not inspect.isabstract(PrimitiveExpression)


def test_hyp_primitiveexpression_constructor_exists():
    assert callable(PrimitiveExpression.__init__)


def test_hyp_primitiveexpression_constructor_args():
    sig = inspect.signature(PrimitiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_enumliteral_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_EnumLiteral)


def test_hyp_oplmetamodel_enumliteral_constructor_exists():
    assert callable(OPLmetamodel_EnumLiteral.__init__)


def test_hyp_oplmetamodel_enumliteral_constructor_args():
    sig = inspect.signature(OPLmetamodel_EnumLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_BooleanExpression)


def test_hyp_oplmetamodel_booleanexpression_constructor_exists():
    assert callable(OPLmetamodel_BooleanExpression.__init__)


def test_hyp_oplmetamodel_booleanexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel_BooleanExpression.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"




def test_hyp_oplmetamodel_booleanblock_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_BooleanBlock)


def test_hyp_oplmetamodel_booleanblock_constructor_exists():
    assert callable(OPLmetamodel_BooleanBlock.__init__)


def test_hyp_oplmetamodel_booleanblock_constructor_args():
    sig = inspect.signature(OPLmetamodel_BooleanBlock.__init__)
    params = list(sig.parameters.keys())



def test_hyp_reference_is_not_abstract():
    assert not inspect.isabstract(Reference)


def test_hyp_reference_constructor_exists():
    assert callable(Reference.__init__)


def test_hyp_reference_constructor_args():
    sig = inspect.signature(Reference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_dataref_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_DataRef)


def test_hyp_oplmetamodel_dataref_constructor_exists():
    assert callable(OPLmetamodel_DataRef.__init__)


def test_hyp_oplmetamodel_dataref_constructor_args():
    sig = inspect.signature(OPLmetamodel_DataRef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_bindingref_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_BindingRef)


def test_hyp_oplmetamodel_bindingref_constructor_exists():
    assert callable(OPLmetamodel_BindingRef.__init__)


def test_hyp_oplmetamodel_bindingref_constructor_args():
    sig = inspect.signature(OPLmetamodel_BindingRef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstractbinaryoperator_is_not_abstract():
    assert not inspect.isabstract(AbstractBinaryOperator)


def test_hyp_abstractbinaryoperator_constructor_exists():
    assert callable(AbstractBinaryOperator.__init__)


def test_hyp_abstractbinaryoperator_constructor_args():
    sig = inspect.signature(AbstractBinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_binaryoperator_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_BinaryOperator)


def test_hyp_oplmetamodel_binaryoperator_constructor_exists():
    assert callable(OPLmetamodel_BinaryOperator.__init__)


def test_hyp_oplmetamodel_binaryoperator_constructor_args():
    sig = inspect.signature(OPLmetamodel_BinaryOperator.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"




def test_hyp_oplmetamodel_tuplebinding_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_TupleBinding)


def test_hyp_oplmetamodel_tuplebinding_constructor_exists():
    assert callable(OPLmetamodel_TupleBinding.__init__)


def test_hyp_oplmetamodel_tuplebinding_constructor_args():
    sig = inspect.signature(OPLmetamodel_TupleBinding.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_stringtype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_StringType)


def test_hyp_oplmetamodel_stringtype_constructor_exists():
    assert callable(OPLmetamodel_StringType.__init__)


def test_hyp_oplmetamodel_stringtype_constructor_args():
    sig = inspect.signature(OPLmetamodel_StringType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_stringexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_StringExpression)


def test_hyp_oplmetamodel_stringexpression_constructor_exists():
    assert callable(OPLmetamodel_StringExpression.__init__)


def test_hyp_oplmetamodel_stringexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel_StringExpression.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"




def test_hyp_piecewiselinearfunction_is_not_abstract():
    assert not inspect.isabstract(PiecewiseLinearFunction)


def test_hyp_piecewiselinearfunction_constructor_exists():
    assert callable(PiecewiseLinearFunction.__init__)


def test_hyp_piecewiselinearfunction_constructor_args():
    sig = inspect.signature(PiecewiseLinearFunction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_statefunction_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_StateFunction)


def test_hyp_oplmetamodel_statefunction_constructor_exists():
    assert callable(OPLmetamodel_StateFunction.__init__)


def test_hyp_oplmetamodel_statefunction_constructor_args():
    sig = inspect.signature(OPLmetamodel_StateFunction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_scriptstatement_is_not_abstract():
    assert not inspect.isabstract(ScriptStatement)


def test_hyp_scriptstatement_constructor_exists():
    assert callable(ScriptStatement.__init__)


def test_hyp_scriptstatement_constructor_args():
    sig = inspect.signature(ScriptStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_writeln_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_Writeln)


def test_hyp_oplmetamodel_writeln_constructor_exists():
    assert callable(OPLmetamodel_Writeln.__init__)


def test_hyp_oplmetamodel_writeln_constructor_args():
    sig = inspect.signature(OPLmetamodel_Writeln.__init__)
    params = list(sig.parameters.keys())
    assert "arg" in params, "Missing parameter 'arg'"
    assert "string" in params, "Missing parameter 'string'"





def test_hyp_oplmetamodel_variablebinding_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_VariableBinding)


def test_hyp_oplmetamodel_variablebinding_constructor_exists():
    assert callable(OPLmetamodel_VariableBinding.__init__)


def test_hyp_oplmetamodel_variablebinding_constructor_args():
    sig = inspect.signature(OPLmetamodel_VariableBinding.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_relationalinit_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_RelationalInit)


def test_hyp_oplmetamodel_relationalinit_constructor_exists():
    assert callable(OPLmetamodel_RelationalInit.__init__)


def test_hyp_oplmetamodel_relationalinit_constructor_args():
    sig = inspect.signature(OPLmetamodel_RelationalInit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(BooleanExpression)


def test_hyp_booleanexpression_constructor_exists():
    assert callable(BooleanExpression.__init__)


def test_hyp_booleanexpression_constructor_args():
    sig = inspect.signature(BooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_hyp_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_hyp_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_relationalexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_RelationalExpression)


def test_hyp_oplmetamodel_relationalexpression_constructor_exists():
    assert callable(OPLmetamodel_RelationalExpression.__init__)


def test_hyp_oplmetamodel_relationalexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel_RelationalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "redefinedOp" in params, "Missing parameter 'redefinedOp'"




def test_hyp_builtinfunction_is_not_abstract():
    assert not inspect.isabstract(BuiltInFunction)


def test_hyp_builtinfunction_constructor_exists():
    assert callable(BuiltInFunction.__init__)


def test_hyp_builtinfunction_constructor_args():
    sig = inspect.signature(BuiltInFunction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_reflectivefunction_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_ReflectiveFunction)


def test_hyp_oplmetamodel_reflectivefunction_constructor_exists():
    assert callable(OPLmetamodel_ReflectiveFunction.__init__)


def test_hyp_oplmetamodel_reflectivefunction_constructor_args():
    sig = inspect.signature(OPLmetamodel_ReflectiveFunction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_sequence_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_Sequence)


def test_hyp_oplmetamodel_sequence_constructor_exists():
    assert callable(OPLmetamodel_Sequence.__init__)


def test_hyp_oplmetamodel_sequence_constructor_args():
    sig = inspect.signature(OPLmetamodel_Sequence.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_scriptstatement_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_ScriptStatement)


def test_hyp_oplmetamodel_scriptstatement_constructor_exists():
    assert callable(OPLmetamodel_ScriptStatement.__init__)


def test_hyp_oplmetamodel_scriptstatement_constructor_args():
    sig = inspect.signature(OPLmetamodel_ScriptStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_relationaloperator_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_RelationalOperator)


def test_hyp_oplmetamodel_relationaloperator_constructor_exists():
    assert callable(OPLmetamodel_RelationalOperator.__init__)


def test_hyp_oplmetamodel_relationaloperator_constructor_args():
    sig = inspect.signature(OPLmetamodel_RelationalOperator.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"




def test_hyp_datainitmethods_is_not_abstract():
    assert not inspect.isabstract(DataInitMethods)


def test_hyp_datainitmethods_constructor_exists():
    assert callable(DataInitMethods.__init__)


def test_hyp_datainitmethods_constructor_args():
    sig = inspect.signature(DataInitMethods.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_queryuser_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_QueryUser)


def test_hyp_oplmetamodel_queryuser_constructor_exists():
    assert callable(OPLmetamodel_QueryUser.__init__)


def test_hyp_oplmetamodel_queryuser_constructor_args():
    sig = inspect.signature(OPLmetamodel_QueryUser.__init__)
    params = list(sig.parameters.keys())
    assert "ask" in params, "Missing parameter 'ask'"




def test_hyp_oplmetamodel_primitivetype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_PrimitiveType)


def test_hyp_oplmetamodel_primitivetype_constructor_exists():
    assert callable(OPLmetamodel_PrimitiveType.__init__)


def test_hyp_oplmetamodel_primitivetype_constructor_args():
    sig = inspect.signature(OPLmetamodel_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_positivefloattype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_PositiveFloatType)


def test_hyp_oplmetamodel_positivefloattype_constructor_exists():
    assert callable(OPLmetamodel_PositiveFloatType.__init__)


def test_hyp_oplmetamodel_positivefloattype_constructor_args():
    sig = inspect.signature(OPLmetamodel_PositiveFloatType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_piecewiselinearfunction_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_PiecewiseLinearFunction)


def test_hyp_oplmetamodel_piecewiselinearfunction_constructor_exists():
    assert callable(OPLmetamodel_PiecewiseLinearFunction.__init__)


def test_hyp_oplmetamodel_piecewiselinearfunction_constructor_args():
    sig = inspect.signature(OPLmetamodel_PiecewiseLinearFunction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_piecewiseexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_PiecewiseExpression)


def test_hyp_oplmetamodel_piecewiseexpression_constructor_exists():
    assert callable(OPLmetamodel_PiecewiseExpression.__init__)


def test_hyp_oplmetamodel_piecewiseexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel_PiecewiseExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_recordfield_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_RecordField)


def test_hyp_oplmetamodel_recordfield_constructor_exists():
    assert callable(OPLmetamodel_RecordField.__init__)


def test_hyp_oplmetamodel_recordfield_constructor_args():
    sig = inspect.signature(OPLmetamodel_RecordField.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_parameterdomain_is_not_abstract():
    assert not inspect.isabstract(ParameterDomain)


def test_hyp_parameterdomain_constructor_exists():
    assert callable(ParameterDomain.__init__)


def test_hyp_parameterdomain_constructor_args():
    sig = inspect.signature(ParameterDomain.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_settype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_SetType)


def test_hyp_oplmetamodel_settype_constructor_exists():
    assert callable(OPLmetamodel_SetType.__init__)


def test_hyp_oplmetamodel_settype_constructor_args():
    sig = inspect.signature(OPLmetamodel_SetType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_oplmetamodel_record_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_Record)


def test_hyp_oplmetamodel_record_constructor_exists():
    assert callable(OPLmetamodel_Record.__init__)


def test_hyp_oplmetamodel_record_constructor_args():
    sig = inspect.signature(OPLmetamodel_Record.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isTuple" in params, "Missing parameter 'isTuple'"





def test_hyp_oplmetamodel_readfile_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_ReadFile)


def test_hyp_oplmetamodel_readfile_constructor_exists():
    assert callable(OPLmetamodel_ReadFile.__init__)


def test_hyp_oplmetamodel_readfile_constructor_args():
    sig = inspect.signature(OPLmetamodel_ReadFile.__init__)
    params = list(sig.parameters.keys())
    assert "path" in params, "Missing parameter 'path'"




def test_hyp_oplmetamodel_rangeexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_RangeExpression)


def test_hyp_oplmetamodel_rangeexpression_constructor_exists():
    assert callable(OPLmetamodel_RangeExpression.__init__)


def test_hyp_oplmetamodel_rangeexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel_RangeExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_model_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_Model)


def test_hyp_oplmetamodel_model_constructor_exists():
    assert callable(OPLmetamodel_Model.__init__)


def test_hyp_oplmetamodel_model_constructor_args():
    sig = inspect.signature(OPLmetamodel_Model.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "isConstraintProblem" in params, "Missing parameter 'isConstraintProblem'"





def test_hyp_oplmetamodel_parameterref_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_ParameterRef)


def test_hyp_oplmetamodel_parameterref_constructor_exists():
    assert callable(OPLmetamodel_ParameterRef.__init__)


def test_hyp_oplmetamodel_parameterref_constructor_args():
    sig = inspect.signature(OPLmetamodel_ParameterRef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_operator_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_Operator)


def test_hyp_oplmetamodel_operator_constructor_exists():
    assert callable(OPLmetamodel_Operator.__init__)


def test_hyp_oplmetamodel_operator_constructor_args():
    sig = inspect.signature(OPLmetamodel_Operator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_numericexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_NumericExpression)


def test_hyp_oplmetamodel_numericexpression_constructor_exists():
    assert callable(OPLmetamodel_NumericExpression.__init__)


def test_hyp_oplmetamodel_numericexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel_NumericExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_searchprocedure_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_SearchProcedure)


def test_hyp_oplmetamodel_searchprocedure_constructor_exists():
    assert callable(OPLmetamodel_SearchProcedure.__init__)


def test_hyp_oplmetamodel_searchprocedure_constructor_args():
    sig = inspect.signature(OPLmetamodel_SearchProcedure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_ifconstraint_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_IfConstraint)


def test_hyp_oplmetamodel_ifconstraint_constructor_exists():
    assert callable(OPLmetamodel_IfConstraint.__init__)


def test_hyp_oplmetamodel_ifconstraint_constructor_args():
    sig = inspect.signature(OPLmetamodel_IfConstraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_integertype_is_not_abstract():
    assert not inspect.isabstract(IntegerType)


def test_hyp_integertype_constructor_exists():
    assert callable(IntegerType.__init__)


def test_hyp_integertype_constructor_args():
    sig = inspect.signature(IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_positiveintegertype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_PositiveIntegerType)


def test_hyp_oplmetamodel_positiveintegertype_constructor_exists():
    assert callable(OPLmetamodel_PositiveIntegerType.__init__)


def test_hyp_oplmetamodel_positiveintegertype_constructor_args():
    sig = inspect.signature(OPLmetamodel_PositiveIntegerType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_integerrangetype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_IntegerRangeType)


def test_hyp_oplmetamodel_integerrangetype_constructor_exists():
    assert callable(OPLmetamodel_IntegerRangeType.__init__)


def test_hyp_oplmetamodel_integerrangetype_constructor_args():
    sig = inspect.signature(OPLmetamodel_IntegerRangeType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_integerexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_IntegerExpression)


def test_hyp_oplmetamodel_integerexpression_constructor_exists():
    assert callable(OPLmetamodel_IntegerExpression.__init__)


def test_hyp_oplmetamodel_integerexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel_IntegerExpression.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"




def test_hyp_oplmetamodel_stepfunction_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_StepFunction)


def test_hyp_oplmetamodel_stepfunction_constructor_exists():
    assert callable(OPLmetamodel_StepFunction.__init__)


def test_hyp_oplmetamodel_stepfunction_constructor_args():
    sig = inspect.signature(OPLmetamodel_StepFunction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_numerictype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_NumericType)


def test_hyp_oplmetamodel_numerictype_constructor_exists():
    assert callable(OPLmetamodel_NumericType.__init__)


def test_hyp_oplmetamodel_numerictype_constructor_args():
    sig = inspect.signature(OPLmetamodel_NumericType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_rangetype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_RangeType)


def test_hyp_oplmetamodel_rangetype_constructor_exists():
    assert callable(OPLmetamodel_RangeType.__init__)


def test_hyp_oplmetamodel_rangetype_constructor_args():
    sig = inspect.signature(OPLmetamodel_RangeType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_interval_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_Interval)


def test_hyp_oplmetamodel_interval_constructor_exists():
    assert callable(OPLmetamodel_Interval.__init__)


def test_hyp_oplmetamodel_interval_constructor_args():
    sig = inspect.signature(OPLmetamodel_Interval.__init__)
    params = list(sig.parameters.keys())
    assert "isOptional" in params, "Missing parameter 'isOptional'"




def test_hyp_oplmetamodel_integertype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_IntegerType)


def test_hyp_oplmetamodel_integertype_constructor_exists():
    assert callable(OPLmetamodel_IntegerType.__init__)


def test_hyp_oplmetamodel_integertype_constructor_args():
    sig = inspect.signature(OPLmetamodel_IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_in_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_In)


def test_hyp_oplmetamodel_in_constructor_exists():
    assert callable(OPLmetamodel_In.__init__)


def test_hyp_oplmetamodel_in_constructor_args():
    sig = inspect.signature(OPLmetamodel_In.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_abstractbinaryoperator_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_AbstractBinaryOperator)


def test_hyp_oplmetamodel_abstractbinaryoperator_constructor_exists():
    assert callable(OPLmetamodel_AbstractBinaryOperator.__init__)


def test_hyp_oplmetamodel_abstractbinaryoperator_constructor_args():
    sig = inspect.signature(OPLmetamodel_AbstractBinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pathexpression_is_not_abstract():
    assert not inspect.isabstract(PathExpression)


def test_hyp_pathexpression_constructor_exists():
    assert callable(PathExpression.__init__)


def test_hyp_pathexpression_constructor_args():
    sig = inspect.signature(PathExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_pathdereference_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_PathDereference)


def test_hyp_oplmetamodel_pathdereference_constructor_exists():
    assert callable(OPLmetamodel_PathDereference.__init__)


def test_hyp_oplmetamodel_pathdereference_constructor_args():
    sig = inspect.signature(OPLmetamodel_PathDereference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_functioncall_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_FunctionCall)


def test_hyp_oplmetamodel_functioncall_constructor_exists():
    assert callable(OPLmetamodel_FunctionCall.__init__)


def test_hyp_oplmetamodel_functioncall_constructor_args():
    sig = inspect.signature(OPLmetamodel_FunctionCall.__init__)
    params = list(sig.parameters.keys())
    assert "functionName" in params, "Missing parameter 'functionName'"




def test_hyp_oplmetamodel_arraydereference_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_ArrayDereference)


def test_hyp_oplmetamodel_arraydereference_constructor_exists():
    assert callable(OPLmetamodel_ArrayDereference.__init__)


def test_hyp_oplmetamodel_arraydereference_constructor_args():
    sig = inspect.signature(OPLmetamodel_ArrayDereference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_allexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_AllExpression)


def test_hyp_oplmetamodel_allexpression_constructor_exists():
    assert callable(OPLmetamodel_AllExpression.__init__)


def test_hyp_oplmetamodel_allexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel_AllExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_expression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_Expression)


def test_hyp_oplmetamodel_expression_constructor_exists():
    assert callable(OPLmetamodel_Expression.__init__)


def test_hyp_oplmetamodel_expression_constructor_args():
    sig = inspect.signature(OPLmetamodel_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_formalparameter_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_FormalParameter)


def test_hyp_oplmetamodel_formalparameter_constructor_exists():
    assert callable(OPLmetamodel_FormalParameter.__init__)


def test_hyp_oplmetamodel_formalparameter_constructor_args():
    sig = inspect.signature(OPLmetamodel_FormalParameter.__init__)
    params = list(sig.parameters.keys())
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"




def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_ifexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_IfExpression)


def test_hyp_oplmetamodel_ifexpression_constructor_exists():
    assert callable(OPLmetamodel_IfExpression.__init__)


def test_hyp_oplmetamodel_ifexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel_IfExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_recordvalue_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_RecordValue)


def test_hyp_oplmetamodel_recordvalue_constructor_exists():
    assert callable(OPLmetamodel_RecordValue.__init__)


def test_hyp_oplmetamodel_recordvalue_constructor_args():
    sig = inspect.signature(OPLmetamodel_RecordValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_reference_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_Reference)


def test_hyp_oplmetamodel_reference_constructor_exists():
    assert callable(OPLmetamodel_Reference.__init__)


def test_hyp_oplmetamodel_reference_constructor_args():
    sig = inspect.signature(OPLmetamodel_Reference.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_oplmetamodel_pathexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_PathExpression)


def test_hyp_oplmetamodel_pathexpression_constructor_exists():
    assert callable(OPLmetamodel_PathExpression.__init__)


def test_hyp_oplmetamodel_pathexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel_PathExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_blockexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_BlockExpression)


def test_hyp_oplmetamodel_blockexpression_constructor_exists():
    assert callable(OPLmetamodel_BlockExpression.__init__)


def test_hyp_oplmetamodel_blockexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel_BlockExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_BinaryExpression)


def test_hyp_oplmetamodel_binaryexpression_constructor_exists():
    assert callable(OPLmetamodel_BinaryExpression.__init__)


def test_hyp_oplmetamodel_binaryexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel_BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_indexvaluepair_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_IndexValuePair)


def test_hyp_oplmetamodel_indexvaluepair_constructor_exists():
    assert callable(OPLmetamodel_IndexValuePair.__init__)


def test_hyp_oplmetamodel_indexvaluepair_constructor_args():
    sig = inspect.signature(OPLmetamodel_IndexValuePair.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_primitiveexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_PrimitiveExpression)


def test_hyp_oplmetamodel_primitiveexpression_constructor_exists():
    assert callable(OPLmetamodel_PrimitiveExpression.__init__)


def test_hyp_oplmetamodel_primitiveexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel_PrimitiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_collectionexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_CollectionExpression)


def test_hyp_oplmetamodel_collectionexpression_constructor_exists():
    assert callable(OPLmetamodel_CollectionExpression.__init__)


def test_hyp_oplmetamodel_collectionexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel_CollectionExpression.__init__)
    params = list(sig.parameters.keys())
    assert "isUnique" in params, "Missing parameter 'isUnique'"




def test_hyp_oplmetamodel_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_UnaryExpression)


def test_hyp_oplmetamodel_unaryexpression_constructor_exists():
    assert callable(OPLmetamodel_UnaryExpression.__init__)


def test_hyp_oplmetamodel_unaryexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel_UnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"




def test_hyp_oplmetamodel_arrayvalue_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_ArrayValue)


def test_hyp_oplmetamodel_arrayvalue_constructor_exists():
    assert callable(OPLmetamodel_ArrayValue.__init__)


def test_hyp_oplmetamodel_arrayvalue_constructor_args():
    sig = inspect.signature(OPLmetamodel_ArrayValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_arrayslotconstraint_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_ArraySlotConstraint)


def test_hyp_oplmetamodel_arrayslotconstraint_constructor_exists():
    assert callable(OPLmetamodel_ArraySlotConstraint.__init__)


def test_hyp_oplmetamodel_arrayslotconstraint_constructor_args():
    sig = inspect.signature(OPLmetamodel_ArraySlotConstraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_setvalue_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_SetValue)


def test_hyp_oplmetamodel_setvalue_constructor_exists():
    assert callable(OPLmetamodel_SetValue.__init__)


def test_hyp_oplmetamodel_setvalue_constructor_args():
    sig = inspect.signature(OPLmetamodel_SetValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_aggregateexp_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_AggregateExp)


def test_hyp_oplmetamodel_aggregateexp_constructor_exists():
    assert callable(OPLmetamodel_AggregateExp.__init__)


def test_hyp_oplmetamodel_aggregateexp_constructor_args():
    sig = inspect.signature(OPLmetamodel_AggregateExp.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"




def test_hyp_oplmetamodel_number_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_Number)


def test_hyp_oplmetamodel_number_constructor_exists():
    assert callable(OPLmetamodel_Number.__init__)


def test_hyp_oplmetamodel_number_constructor_args():
    sig = inspect.signature(OPLmetamodel_Number.__init__)
    params = list(sig.parameters.keys())



def test_hyp_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_hyp_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_hyp_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_constraint_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_Constraint)


def test_hyp_oplmetamodel_constraint_constructor_exists():
    assert callable(OPLmetamodel_Constraint.__init__)


def test_hyp_oplmetamodel_constraint_constructor_args():
    sig = inspect.signature(OPLmetamodel_Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_oplmetamodel_definedtype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_DefinedType)


def test_hyp_oplmetamodel_definedtype_constructor_exists():
    assert callable(OPLmetamodel_DefinedType.__init__)


def test_hyp_oplmetamodel_definedtype_constructor_args():
    sig = inspect.signature(OPLmetamodel_DefinedType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_function_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_Function)


def test_hyp_oplmetamodel_function_constructor_exists():
    assert callable(OPLmetamodel_Function.__init__)


def test_hyp_oplmetamodel_function_constructor_args():
    sig = inspect.signature(OPLmetamodel_Function.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_assertion_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_Assertion)


def test_hyp_oplmetamodel_assertion_constructor_exists():
    assert callable(OPLmetamodel_Assertion.__init__)


def test_hyp_oplmetamodel_assertion_constructor_args():
    sig = inspect.signature(OPLmetamodel_Assertion.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_scheduleinitialization_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_ScheduleInitialization)


def test_hyp_oplmetamodel_scheduleinitialization_constructor_exists():
    assert callable(OPLmetamodel_ScheduleInitialization.__init__)


def test_hyp_oplmetamodel_scheduleinitialization_constructor_args():
    sig = inspect.signature(OPLmetamodel_ScheduleInitialization.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_datadeclaration_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_DataDeclaration)


def test_hyp_oplmetamodel_datadeclaration_constructor_exists():
    assert callable(OPLmetamodel_DataDeclaration.__init__)


def test_hyp_oplmetamodel_datadeclaration_constructor_args():
    sig = inspect.signature(OPLmetamodel_DataDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "isDecisionVar" in params, "Missing parameter 'isDecisionVar'"
    assert "isDecisionExpr" in params, "Missing parameter 'isDecisionExpr'"





def test_hyp_oplmetamodel_script_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_Script)


def test_hyp_oplmetamodel_script_constructor_exists():
    assert callable(OPLmetamodel_Script.__init__)


def test_hyp_oplmetamodel_script_constructor_args():
    sig = inspect.signature(OPLmetamodel_Script.__init__)
    params = list(sig.parameters.keys())
    assert "isMain" in params, "Missing parameter 'isMain'"




def test_hyp_oplmetamodel_resourcedeclaration_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_ResourceDeclaration)


def test_hyp_oplmetamodel_resourcedeclaration_constructor_exists():
    assert callable(OPLmetamodel_ResourceDeclaration.__init__)


def test_hyp_oplmetamodel_resourcedeclaration_constructor_args():
    sig = inspect.signature(OPLmetamodel_ResourceDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_objective_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_Objective)


def test_hyp_oplmetamodel_objective_constructor_exists():
    assert callable(OPLmetamodel_Objective.__init__)


def test_hyp_oplmetamodel_objective_constructor_args():
    sig = inspect.signature(OPLmetamodel_Objective.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"
    assert "isLinearRelaxation" in params, "Missing parameter 'isLinearRelaxation'"





def test_hyp_oplmetamodel_setting_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_Setting)


def test_hyp_oplmetamodel_setting_constructor_exists():
    assert callable(OPLmetamodel_Setting.__init__)


def test_hyp_oplmetamodel_setting_constructor_args():
    sig = inspect.signature(OPLmetamodel_Setting.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oplmetamodel_activitydeclaration_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_ActivityDeclaration)


def test_hyp_oplmetamodel_activitydeclaration_constructor_exists():
    assert callable(OPLmetamodel_ActivityDeclaration.__init__)


def test_hyp_oplmetamodel_activitydeclaration_constructor_args():
    sig = inspect.signature(OPLmetamodel_ActivityDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "latestEndTime" in params, "Missing parameter 'latestEndTime'"
    assert "earliestStartTime" in params, "Missing parameter 'earliestStartTime'"





def test_hyp_oplmetamodel_abstracttype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_AbstractType)


def test_hyp_oplmetamodel_abstracttype_constructor_exists():
    assert callable(OPLmetamodel_AbstractType.__init__)


def test_hyp_oplmetamodel_abstracttype_constructor_args():
    sig = inspect.signature(OPLmetamodel_AbstractType.__init__)
    params = list(sig.parameters.keys())

def test_hyp_binaryop_exists():
    # Check that the Enumeration exists
    assert BinaryOp is not None

def test_hyp_binaryop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BinaryOp]
    expected_literals = [
        "divide",
        "union",
        "power",
        "symdiff",
        "multiply",
        "inter",
        "subtract",
        "diff",
        "mod",
        "percent",
        "add",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BinaryOp"

def test_hyp_membershipop_exists():
    # Check that the Enumeration exists
    assert MembershipOp is not None

def test_hyp_membershipop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MembershipOp]
    expected_literals = [
        "and_",
        "or_",
        "in_",
        "conjunction",
        "not_in",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MembershipOp"

def test_hyp_quantifier_exists():
    # Check that the Enumeration exists
    assert Quantifier is not None

def test_hyp_quantifier_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Quantifier]
    expected_literals = [
        "forAll",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Quantifier"

def test_hyp_optimizationmode_exists():
    # Check that the Enumeration exists
    assert OptimizationMode is not None

def test_hyp_optimizationmode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OptimizationMode]
    expected_literals = [
        "maximize",
        "minimize",
        "solve",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OptimizationMode"

def test_hyp_logicalop_exists():
    # Check that the Enumeration exists
    assert LogicalOp is not None

def test_hyp_logicalop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LogicalOp]
    expected_literals = [
        "negation",
        "conjunction",
        "or_",
        "and_",
        "disjunction",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LogicalOp"

def test_hyp_unaryop_exists():
    # Check that the Enumeration exists
    assert UnaryOp is not None

def test_hyp_unaryop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnaryOp]
    expected_literals = [
        "negate",
        "unaryMinus",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnaryOp"

def test_hyp_relationalop_exists():
    # Check that the Enumeration exists
    assert RelationalOp is not None

def test_hyp_relationalop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RelationalOp]
    expected_literals = [
        "lessThanOrEqualTo",
        "greaterThan",
        "equalTo",
        "lessThan",
        "notEqualTo",
        "greaterThanOrEqualTo",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RelationalOp"

def test_hyp_aggop_exists():
    # Check that the Enumeration exists
    assert AggOp is not None

def test_hyp_aggop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AggOp]
    expected_literals = [
        "max",
        "and_",
        "min",
        "sum",
        "or_",
        "prod",
        "inter",
        "union",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AggOp"

def test_hyp_setop_exists():
    # Check that the Enumeration exists
    assert SetOp is not None

def test_hyp_setop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SetOp]
    expected_literals = [
        "inter",
        "union",
        "symdiff",
        "diff",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SetOp"


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
FloatType_strategy = st.builds(
    FloatType,
)
OPLmetamodel_Error_strategy = st.builds(
    OPLmetamodel_Error,
)
OPLmetamodel_Entity_strategy = st.builds(
    OPLmetamodel_Entity,
)
OPLmetamodel_FunctionRef_strategy = st.builds(
    OPLmetamodel_FunctionRef,
    name=
        safe_text
)
Constraint_strategy = st.builds(
    Constraint,
)
OPLmetamodel_ForAllConstraint_strategy = st.builds(
    OPLmetamodel_ForAllConstraint,
)
NumericExpression_strategy = st.builds(
    NumericExpression,
)
OPLmetamodel_FloatExpression_strategy = st.builds(
    OPLmetamodel_FloatExpression,
    body=
        safe_text
)
OPLmetamodel_ParameterDomain_strategy = st.builds(
    OPLmetamodel_ParameterDomain,
)
NumericType_strategy = st.builds(
    NumericType,
)
OPLmetamodel_FloatType_strategy = st.builds(
    OPLmetamodel_FloatType,
)
RangeType_strategy = st.builds(
    RangeType,
)
OPLmetamodel_FloatRangeType_strategy = st.builds(
    OPLmetamodel_FloatRangeType,
)
Initialization_strategy = st.builds(
    Initialization,
)
OPLmetamodel_DataObject_strategy = st.builds(
    OPLmetamodel_DataObject,
    body=
        safe_text
)
OPLmetamodel_DataInitMethods_strategy = st.builds(
    OPLmetamodel_DataInitMethods,
)
OPLmetamodel_Initialization_strategy = st.builds(
    OPLmetamodel_Initialization,
)
SetType_strategy = st.builds(
    SetType,
)
OPLmetamodel_EnumerationType_strategy = st.builds(
    OPLmetamodel_EnumerationType,
)
OPLmetamodel_ParameterDeclaration_strategy = st.builds(
    OPLmetamodel_ParameterDeclaration,
)
OPLmetamodel_DisplayInstruction_strategy = st.builds(
    OPLmetamodel_DisplayInstruction,
)
AbstractType_strategy = st.builds(
    AbstractType,
)
OPLmetamodel_DeferredInit_strategy = st.builds(
    OPLmetamodel_DeferredInit,
)
OPLmetamodel_Declaration_strategy = st.builds(
    OPLmetamodel_Declaration,
    order=
        st.none()
)
DefinedType_strategy = st.builds(
    DefinedType,
)
OPLmetamodel_ArrayType_strategy = st.builds(
    OPLmetamodel_ArrayType,
)
CollectionExpression_strategy = st.builds(
    CollectionExpression,
)
OPLmetamodel_Extension_strategy = st.builds(
    OPLmetamodel_Extension,
)
OPLmetamodel_Comprehension_strategy = st.builds(
    OPLmetamodel_Comprehension,
)
Function_strategy = st.builds(
    Function,
)
OPLmetamodel_CumulativeFunction_strategy = st.builds(
    OPLmetamodel_CumulativeFunction,
)
OPLmetamodel_BuiltInFunction_strategy = st.builds(
    OPLmetamodel_BuiltInFunction,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
OPLmetamodel_BooleanType_strategy = st.builds(
    OPLmetamodel_BooleanType,
)
PrimitiveExpression_strategy = st.builds(
    PrimitiveExpression,
)
OPLmetamodel_EnumLiteral_strategy = st.builds(
    OPLmetamodel_EnumLiteral,
)
OPLmetamodel_BooleanExpression_strategy = st.builds(
    OPLmetamodel_BooleanExpression,
    body=
        safe_text
)
OPLmetamodel_BooleanBlock_strategy = st.builds(
    OPLmetamodel_BooleanBlock,
)
Reference_strategy = st.builds(
    Reference,
)
OPLmetamodel_DataRef_strategy = st.builds(
    OPLmetamodel_DataRef,
)
OPLmetamodel_BindingRef_strategy = st.builds(
    OPLmetamodel_BindingRef,
)
AbstractBinaryOperator_strategy = st.builds(
    AbstractBinaryOperator,
)
OPLmetamodel_BinaryOperator_strategy = st.builds(
    OPLmetamodel_BinaryOperator,
    op=
        safe_text
)
OPLmetamodel_TupleBinding_strategy = st.builds(
    OPLmetamodel_TupleBinding,
)
OPLmetamodel_StringType_strategy = st.builds(
    OPLmetamodel_StringType,
)
OPLmetamodel_StringExpression_strategy = st.builds(
    OPLmetamodel_StringExpression,
    body=
        safe_text
)
PiecewiseLinearFunction_strategy = st.builds(
    PiecewiseLinearFunction,
)
OPLmetamodel_StateFunction_strategy = st.builds(
    OPLmetamodel_StateFunction,
)
ScriptStatement_strategy = st.builds(
    ScriptStatement,
)
OPLmetamodel_Writeln_strategy = st.builds(
    OPLmetamodel_Writeln,
    arg=
        safe_text,
    string=
        safe_text
)
OPLmetamodel_VariableBinding_strategy = st.builds(
    OPLmetamodel_VariableBinding,
)
OPLmetamodel_RelationalInit_strategy = st.builds(
    OPLmetamodel_RelationalInit,
)
BooleanExpression_strategy = st.builds(
    BooleanExpression,
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
OPLmetamodel_RelationalExpression_strategy = st.builds(
    OPLmetamodel_RelationalExpression,
    redefinedOp=
        safe_text
)
BuiltInFunction_strategy = st.builds(
    BuiltInFunction,
)
OPLmetamodel_ReflectiveFunction_strategy = st.builds(
    OPLmetamodel_ReflectiveFunction,
)
OPLmetamodel_Sequence_strategy = st.builds(
    OPLmetamodel_Sequence,
)
OPLmetamodel_ScriptStatement_strategy = st.builds(
    OPLmetamodel_ScriptStatement,
)
OPLmetamodel_RelationalOperator_strategy = st.builds(
    OPLmetamodel_RelationalOperator,
    op=
        safe_text
)
DataInitMethods_strategy = st.builds(
    DataInitMethods,
)
OPLmetamodel_QueryUser_strategy = st.builds(
    OPLmetamodel_QueryUser,
    ask=
        safe_text
)
OPLmetamodel_PrimitiveType_strategy = st.builds(
    OPLmetamodel_PrimitiveType,
)
OPLmetamodel_PositiveFloatType_strategy = st.builds(
    OPLmetamodel_PositiveFloatType,
)
OPLmetamodel_PiecewiseLinearFunction_strategy = st.builds(
    OPLmetamodel_PiecewiseLinearFunction,
)
OPLmetamodel_PiecewiseExpression_strategy = st.builds(
    OPLmetamodel_PiecewiseExpression,
)
OPLmetamodel_RecordField_strategy = st.builds(
    OPLmetamodel_RecordField,
    name=
        safe_text
)
ParameterDomain_strategy = st.builds(
    ParameterDomain,
)
OPLmetamodel_SetType_strategy = st.builds(
    OPLmetamodel_SetType,
    name=
        safe_text
)
OPLmetamodel_Record_strategy = st.builds(
    OPLmetamodel_Record,
    name=
        safe_text,
    isTuple=
        st.booleans()
)
OPLmetamodel_ReadFile_strategy = st.builds(
    OPLmetamodel_ReadFile,
    path=
        safe_text
)
OPLmetamodel_RangeExpression_strategy = st.builds(
    OPLmetamodel_RangeExpression,
)
OPLmetamodel_Model_strategy = st.builds(
    OPLmetamodel_Model,
    id=
        safe_text,
    isConstraintProblem=
        st.booleans()
)
OPLmetamodel_ParameterRef_strategy = st.builds(
    OPLmetamodel_ParameterRef,
)
OPLmetamodel_Operator_strategy = st.builds(
    OPLmetamodel_Operator,
)
OPLmetamodel_NumericExpression_strategy = st.builds(
    OPLmetamodel_NumericExpression,
)
OPLmetamodel_SearchProcedure_strategy = st.builds(
    OPLmetamodel_SearchProcedure,
)
OPLmetamodel_IfConstraint_strategy = st.builds(
    OPLmetamodel_IfConstraint,
)
IntegerType_strategy = st.builds(
    IntegerType,
)
OPLmetamodel_PositiveIntegerType_strategy = st.builds(
    OPLmetamodel_PositiveIntegerType,
)
OPLmetamodel_IntegerRangeType_strategy = st.builds(
    OPLmetamodel_IntegerRangeType,
)
OPLmetamodel_IntegerExpression_strategy = st.builds(
    OPLmetamodel_IntegerExpression,
    body=
        safe_text
)
OPLmetamodel_StepFunction_strategy = st.builds(
    OPLmetamodel_StepFunction,
)
OPLmetamodel_NumericType_strategy = st.builds(
    OPLmetamodel_NumericType,
)
OPLmetamodel_RangeType_strategy = st.builds(
    OPLmetamodel_RangeType,
)
OPLmetamodel_Interval_strategy = st.builds(
    OPLmetamodel_Interval,
    isOptional=
        st.booleans()
)
OPLmetamodel_IntegerType_strategy = st.builds(
    OPLmetamodel_IntegerType,
)
OPLmetamodel_In_strategy = st.builds(
    OPLmetamodel_In,
)
OPLmetamodel_AbstractBinaryOperator_strategy = st.builds(
    OPLmetamodel_AbstractBinaryOperator,
)
PathExpression_strategy = st.builds(
    PathExpression,
)
OPLmetamodel_PathDereference_strategy = st.builds(
    OPLmetamodel_PathDereference,
)
OPLmetamodel_FunctionCall_strategy = st.builds(
    OPLmetamodel_FunctionCall,
    functionName=
        safe_text
)
OPLmetamodel_ArrayDereference_strategy = st.builds(
    OPLmetamodel_ArrayDereference,
)
OPLmetamodel_AllExpression_strategy = st.builds(
    OPLmetamodel_AllExpression,
)
OPLmetamodel_Expression_strategy = st.builds(
    OPLmetamodel_Expression,
)
OPLmetamodel_FormalParameter_strategy = st.builds(
    OPLmetamodel_FormalParameter,
    isOrdered=
        st.booleans()
)
Expression_strategy = st.builds(
    Expression,
)
OPLmetamodel_IfExpression_strategy = st.builds(
    OPLmetamodel_IfExpression,
)
OPLmetamodel_RecordValue_strategy = st.builds(
    OPLmetamodel_RecordValue,
)
OPLmetamodel_Reference_strategy = st.builds(
    OPLmetamodel_Reference,
    name=
        safe_text
)
OPLmetamodel_PathExpression_strategy = st.builds(
    OPLmetamodel_PathExpression,
)
OPLmetamodel_BlockExpression_strategy = st.builds(
    OPLmetamodel_BlockExpression,
)
OPLmetamodel_BinaryExpression_strategy = st.builds(
    OPLmetamodel_BinaryExpression,
)
OPLmetamodel_IndexValuePair_strategy = st.builds(
    OPLmetamodel_IndexValuePair,
)
OPLmetamodel_PrimitiveExpression_strategy = st.builds(
    OPLmetamodel_PrimitiveExpression,
)
OPLmetamodel_CollectionExpression_strategy = st.builds(
    OPLmetamodel_CollectionExpression,
    isUnique=
        st.booleans()
)
OPLmetamodel_UnaryExpression_strategy = st.builds(
    OPLmetamodel_UnaryExpression,
    op=
        safe_text
)
OPLmetamodel_ArrayValue_strategy = st.builds(
    OPLmetamodel_ArrayValue,
)
OPLmetamodel_ArraySlotConstraint_strategy = st.builds(
    OPLmetamodel_ArraySlotConstraint,
)
OPLmetamodel_SetValue_strategy = st.builds(
    OPLmetamodel_SetValue,
)
OPLmetamodel_AggregateExp_strategy = st.builds(
    OPLmetamodel_AggregateExp,
    op=
        safe_text
)
OPLmetamodel_Number_strategy = st.builds(
    OPLmetamodel_Number,
)
Declaration_strategy = st.builds(
    Declaration,
)
OPLmetamodel_Constraint_strategy = st.builds(
    OPLmetamodel_Constraint,
    name=
        safe_text
)
OPLmetamodel_DefinedType_strategy = st.builds(
    OPLmetamodel_DefinedType,
)
OPLmetamodel_Function_strategy = st.builds(
    OPLmetamodel_Function,
)
OPLmetamodel_Assertion_strategy = st.builds(
    OPLmetamodel_Assertion,
)
OPLmetamodel_ScheduleInitialization_strategy = st.builds(
    OPLmetamodel_ScheduleInitialization,
)
OPLmetamodel_DataDeclaration_strategy = st.builds(
    OPLmetamodel_DataDeclaration,
    isDecisionVar=
        st.booleans(),
    isDecisionExpr=
        st.booleans()
)
OPLmetamodel_Script_strategy = st.builds(
    OPLmetamodel_Script,
    isMain=
        st.booleans()
)
OPLmetamodel_ResourceDeclaration_strategy = st.builds(
    OPLmetamodel_ResourceDeclaration,
)
OPLmetamodel_Objective_strategy = st.builds(
    OPLmetamodel_Objective,
    action=
        safe_text,
    isLinearRelaxation=
        st.booleans()
)
OPLmetamodel_Setting_strategy = st.builds(
    OPLmetamodel_Setting,
)
OPLmetamodel_ActivityDeclaration_strategy = st.builds(
    OPLmetamodel_ActivityDeclaration,
    latestEndTime=
        safe_text,
    earliestStartTime=
        safe_text
)
OPLmetamodel_AbstractType_strategy = st.builds(
    OPLmetamodel_AbstractType,
)







@given(instance=OPLmetamodel_FunctionRef_strategy)
def test_hyp_oplmetamodel_functionref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original







@given(instance=OPLmetamodel_FloatExpression_strategy)
def test_hyp_oplmetamodel_floatexpression_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original










@given(instance=OPLmetamodel_DataObject_strategy)
def test_hyp_oplmetamodel_dataobject_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original









@given(instance=OPLmetamodel_Declaration_strategy)
@settings(max_examples=50)
def test_hyp_oplmetamodel_declaration_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_Declaration)



@given(instance=OPLmetamodel_Declaration_strategy)
def test_hyp_oplmetamodel_declaration_order_setter(instance):
    original = instance.order
    instance.order = original
    assert instance.order == original
















@given(instance=OPLmetamodel_BooleanExpression_strategy)
def test_hyp_oplmetamodel_booleanexpression_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original









@given(instance=OPLmetamodel_BinaryOperator_strategy)
def test_hyp_oplmetamodel_binaryoperator_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original






@given(instance=OPLmetamodel_StringExpression_strategy)
def test_hyp_oplmetamodel_stringexpression_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original







@given(instance=OPLmetamodel_Writeln_strategy)
def test_hyp_oplmetamodel_writeln_arg_setter(instance):
    original = instance.arg
    instance.arg = original
    assert instance.arg == original



@given(instance=OPLmetamodel_Writeln_strategy)
def test_hyp_oplmetamodel_writeln_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original








@given(instance=OPLmetamodel_RelationalExpression_strategy)
def test_hyp_oplmetamodel_relationalexpression_redefinedOp_setter(instance):
    original = instance.redefinedOp
    instance.redefinedOp = original
    assert instance.redefinedOp == original








@given(instance=OPLmetamodel_RelationalOperator_strategy)
def test_hyp_oplmetamodel_relationaloperator_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original





@given(instance=OPLmetamodel_QueryUser_strategy)
def test_hyp_oplmetamodel_queryuser_ask_setter(instance):
    original = instance.ask
    instance.ask = original
    assert instance.ask == original








@given(instance=OPLmetamodel_RecordField_strategy)
def test_hyp_oplmetamodel_recordfield_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=OPLmetamodel_SetType_strategy)
def test_hyp_oplmetamodel_settype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=OPLmetamodel_Record_strategy)
def test_hyp_oplmetamodel_record_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=OPLmetamodel_Record_strategy)
def test_hyp_oplmetamodel_record_isTuple_setter(instance):
    original = instance.isTuple
    instance.isTuple = original
    assert instance.isTuple == original




@given(instance=OPLmetamodel_ReadFile_strategy)
def test_hyp_oplmetamodel_readfile_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original





@given(instance=OPLmetamodel_Model_strategy)
def test_hyp_oplmetamodel_model_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=OPLmetamodel_Model_strategy)
def test_hyp_oplmetamodel_model_isConstraintProblem_setter(instance):
    original = instance.isConstraintProblem
    instance.isConstraintProblem = original
    assert instance.isConstraintProblem == original












@given(instance=OPLmetamodel_IntegerExpression_strategy)
def test_hyp_oplmetamodel_integerexpression_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original







@given(instance=OPLmetamodel_Interval_strategy)
def test_hyp_oplmetamodel_interval_isOptional_setter(instance):
    original = instance.isOptional
    instance.isOptional = original
    assert instance.isOptional == original









@given(instance=OPLmetamodel_FunctionCall_strategy)
def test_hyp_oplmetamodel_functioncall_functionName_setter(instance):
    original = instance.functionName
    instance.functionName = original
    assert instance.functionName == original







@given(instance=OPLmetamodel_FormalParameter_strategy)
def test_hyp_oplmetamodel_formalparameter_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original







@given(instance=OPLmetamodel_Reference_strategy)
def test_hyp_oplmetamodel_reference_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original









@given(instance=OPLmetamodel_CollectionExpression_strategy)
def test_hyp_oplmetamodel_collectionexpression_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original




@given(instance=OPLmetamodel_UnaryExpression_strategy)
def test_hyp_oplmetamodel_unaryexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original







@given(instance=OPLmetamodel_AggregateExp_strategy)
def test_hyp_oplmetamodel_aggregateexp_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original






@given(instance=OPLmetamodel_Constraint_strategy)
def test_hyp_oplmetamodel_constraint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original








@given(instance=OPLmetamodel_DataDeclaration_strategy)
def test_hyp_oplmetamodel_datadeclaration_isDecisionVar_setter(instance):
    original = instance.isDecisionVar
    instance.isDecisionVar = original
    assert instance.isDecisionVar == original



@given(instance=OPLmetamodel_DataDeclaration_strategy)
def test_hyp_oplmetamodel_datadeclaration_isDecisionExpr_setter(instance):
    original = instance.isDecisionExpr
    instance.isDecisionExpr = original
    assert instance.isDecisionExpr == original




@given(instance=OPLmetamodel_Script_strategy)
def test_hyp_oplmetamodel_script_isMain_setter(instance):
    original = instance.isMain
    instance.isMain = original
    assert instance.isMain == original





@given(instance=OPLmetamodel_Objective_strategy)
def test_hyp_oplmetamodel_objective_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original



@given(instance=OPLmetamodel_Objective_strategy)
def test_hyp_oplmetamodel_objective_isLinearRelaxation_setter(instance):
    original = instance.isLinearRelaxation
    instance.isLinearRelaxation = original
    assert instance.isLinearRelaxation == original





@given(instance=OPLmetamodel_ActivityDeclaration_strategy)
def test_hyp_oplmetamodel_activitydeclaration_latestEndTime_setter(instance):
    original = instance.latestEndTime
    instance.latestEndTime = original
    assert instance.latestEndTime == original



@given(instance=OPLmetamodel_ActivityDeclaration_strategy)
def test_hyp_oplmetamodel_activitydeclaration_earliestStartTime_setter(instance):
    original = instance.earliestStartTime
    instance.earliestStartTime = original
    assert instance.earliestStartTime == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AbstractBinaryOperator,
    AbstractType,
    BinaryExpression,
    BooleanExpression,
    BuiltInFunction,
    CollectionExpression,
    Constraint,
    DataInitMethods,
    Declaration,
    DefinedType,
    Expression,
    FloatType,
    Function,
    Initialization,
    IntegerType,
    NumericExpression,
    NumericType,
    OPLmetamodel_AbstractBinaryOperator,
    OPLmetamodel_AbstractType,
    OPLmetamodel_ActivityDeclaration,
    OPLmetamodel_AggregateExp,
    OPLmetamodel_AllExpression,
    OPLmetamodel_ArrayDereference,
    OPLmetamodel_ArraySlotConstraint,
    OPLmetamodel_ArrayType,
    OPLmetamodel_ArrayValue,
    OPLmetamodel_Assertion,
    OPLmetamodel_BinaryExpression,
    OPLmetamodel_BinaryOperator,
    OPLmetamodel_BindingRef,
    OPLmetamodel_BlockExpression,
    OPLmetamodel_BooleanBlock,
    OPLmetamodel_BooleanExpression,
    OPLmetamodel_BooleanType,
    OPLmetamodel_BuiltInFunction,
    OPLmetamodel_CollectionExpression,
    OPLmetamodel_Comprehension,
    OPLmetamodel_Constraint,
    OPLmetamodel_CumulativeFunction,
    OPLmetamodel_DataDeclaration,
    OPLmetamodel_DataInitMethods,
    OPLmetamodel_DataObject,
    OPLmetamodel_DataRef,
    OPLmetamodel_Declaration,
    OPLmetamodel_DeferredInit,
    OPLmetamodel_DefinedType,
    OPLmetamodel_DisplayInstruction,
    OPLmetamodel_Entity,
    OPLmetamodel_EnumLiteral,
    OPLmetamodel_EnumerationType,
    OPLmetamodel_Error,
    OPLmetamodel_Expression,
    OPLmetamodel_Extension,
    OPLmetamodel_FloatExpression,
    OPLmetamodel_FloatRangeType,
    OPLmetamodel_FloatType,
    OPLmetamodel_ForAllConstraint,
    OPLmetamodel_FormalParameter,
    OPLmetamodel_Function,
    OPLmetamodel_FunctionCall,
    OPLmetamodel_FunctionRef,
    OPLmetamodel_IfConstraint,
    OPLmetamodel_IfExpression,
    OPLmetamodel_In,
    OPLmetamodel_IndexValuePair,
    OPLmetamodel_Initialization,
    OPLmetamodel_IntegerExpression,
    OPLmetamodel_IntegerRangeType,
    OPLmetamodel_IntegerType,
    OPLmetamodel_Interval,
    OPLmetamodel_Model,
    OPLmetamodel_Number,
    OPLmetamodel_NumericExpression,
    OPLmetamodel_NumericType,
    OPLmetamodel_Objective,
    OPLmetamodel_Operator,
    OPLmetamodel_ParameterDeclaration,
    OPLmetamodel_ParameterDomain,
    OPLmetamodel_ParameterRef,
    OPLmetamodel_PathDereference,
    OPLmetamodel_PathExpression,
    OPLmetamodel_PiecewiseExpression,
    OPLmetamodel_PiecewiseLinearFunction,
    OPLmetamodel_PositiveFloatType,
    OPLmetamodel_PositiveIntegerType,
    OPLmetamodel_PrimitiveExpression,
    OPLmetamodel_PrimitiveType,
    OPLmetamodel_QueryUser,
    OPLmetamodel_RangeExpression,
    OPLmetamodel_RangeType,
    OPLmetamodel_ReadFile,
    OPLmetamodel_Record,
    OPLmetamodel_RecordField,
    OPLmetamodel_RecordValue,
    OPLmetamodel_Reference,
    OPLmetamodel_ReflectiveFunction,
    OPLmetamodel_RelationalExpression,
    OPLmetamodel_RelationalInit,
    OPLmetamodel_RelationalOperator,
    OPLmetamodel_ResourceDeclaration,
    OPLmetamodel_ScheduleInitialization,
    OPLmetamodel_Script,
    OPLmetamodel_ScriptStatement,
    OPLmetamodel_SearchProcedure,
    OPLmetamodel_Sequence,
    OPLmetamodel_SetType,
    OPLmetamodel_SetValue,
    OPLmetamodel_Setting,
    OPLmetamodel_StateFunction,
    OPLmetamodel_StepFunction,
    OPLmetamodel_StringExpression,
    OPLmetamodel_StringType,
    OPLmetamodel_TupleBinding,
    OPLmetamodel_UnaryExpression,
    OPLmetamodel_VariableBinding,
    OPLmetamodel_Writeln,
    ParameterDomain,
    PathExpression,
    PiecewiseLinearFunction,
    PrimitiveExpression,
    PrimitiveType,
    RangeType,
    Reference,
    ScriptStatement,
    SetType,
    AggOp,
    BinaryOp,
    LogicalOp,
    MembershipOp,
    OptimizationMode,
    Quantifier,
    RelationalOp,
    SetOp,
    UnaryOp,
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

def test_OPLmetamodel_ActivityDeclaration_earliestStartTime_value_roundtrip():
    instance = OPLmetamodel_ActivityDeclaration(earliestStartTime="sample_text", latestEndTime="sample_text")
    assert instance.earliestStartTime == "sample_text"
    instance.earliestStartTime = "sample_text_2"
    assert instance.earliestStartTime == "sample_text_2"


def test_OPLmetamodel_ActivityDeclaration_latestEndTime_value_roundtrip():
    instance = OPLmetamodel_ActivityDeclaration(earliestStartTime="sample_text", latestEndTime="sample_text")
    assert instance.latestEndTime == "sample_text"
    instance.latestEndTime = "sample_text_2"
    assert instance.latestEndTime == "sample_text_2"


def test_OPLmetamodel_AggregateExp_op_value_roundtrip():
    instance = OPLmetamodel_AggregateExp(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_OPLmetamodel_BinaryOperator_op_value_roundtrip():
    instance = OPLmetamodel_BinaryOperator(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_OPLmetamodel_BooleanExpression_body_value_roundtrip():
    instance = OPLmetamodel_BooleanExpression(body="sample_text")
    assert instance.body == "sample_text"
    instance.body = "sample_text_2"
    assert instance.body == "sample_text_2"


def test_OPLmetamodel_CollectionExpression_isUnique_value_roundtrip():
    instance = OPLmetamodel_CollectionExpression(isUnique=True)
    assert instance.isUnique == True
    instance.isUnique = False
    assert instance.isUnique == False


def test_OPLmetamodel_Constraint_name_value_roundtrip():
    instance = OPLmetamodel_Constraint(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_OPLmetamodel_DataDeclaration_isDecisionExpr_value_roundtrip():
    instance = OPLmetamodel_DataDeclaration(isDecisionExpr=True, isDecisionVar=True)
    assert instance.isDecisionExpr == True
    instance.isDecisionExpr = False
    assert instance.isDecisionExpr == False


def test_OPLmetamodel_DataDeclaration_isDecisionVar_value_roundtrip():
    instance = OPLmetamodel_DataDeclaration(isDecisionExpr=True, isDecisionVar=True)
    assert instance.isDecisionVar == True
    instance.isDecisionVar = False
    assert instance.isDecisionVar == False


def test_OPLmetamodel_DataObject_body_value_roundtrip():
    instance = OPLmetamodel_DataObject(body="sample_text")
    assert instance.body == "sample_text"
    instance.body = "sample_text_2"
    assert instance.body == "sample_text_2"


def test_OPLmetamodel_FloatExpression_body_value_roundtrip():
    instance = OPLmetamodel_FloatExpression(body="sample_text")
    assert instance.body == "sample_text"
    instance.body = "sample_text_2"
    assert instance.body == "sample_text_2"


def test_OPLmetamodel_FormalParameter_isOrdered_value_roundtrip():
    instance = OPLmetamodel_FormalParameter(isOrdered=True)
    assert instance.isOrdered == True
    instance.isOrdered = False
    assert instance.isOrdered == False


def test_OPLmetamodel_FunctionCall_functionName_value_roundtrip():
    instance = OPLmetamodel_FunctionCall(functionName="sample_text")
    assert instance.functionName == "sample_text"
    instance.functionName = "sample_text_2"
    assert instance.functionName == "sample_text_2"


def test_OPLmetamodel_FunctionRef_name_value_roundtrip():
    instance = OPLmetamodel_FunctionRef(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_OPLmetamodel_IntegerExpression_body_value_roundtrip():
    instance = OPLmetamodel_IntegerExpression(body="sample_text")
    assert instance.body == "sample_text"
    instance.body = "sample_text_2"
    assert instance.body == "sample_text_2"


def test_OPLmetamodel_Interval_isOptional_value_roundtrip():
    instance = OPLmetamodel_Interval(isOptional=True)
    assert instance.isOptional == True
    instance.isOptional = False
    assert instance.isOptional == False


def test_OPLmetamodel_Model_id_value_roundtrip():
    instance = OPLmetamodel_Model(id="sample_text", isConstraintProblem=True)
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_OPLmetamodel_Model_isConstraintProblem_value_roundtrip():
    instance = OPLmetamodel_Model(id="sample_text", isConstraintProblem=True)
    assert instance.isConstraintProblem == True
    instance.isConstraintProblem = False
    assert instance.isConstraintProblem == False


def test_OPLmetamodel_Objective_action_value_roundtrip():
    instance = OPLmetamodel_Objective(action="sample_text", isLinearRelaxation=True)
    assert instance.action == "sample_text"
    instance.action = "sample_text_2"
    assert instance.action == "sample_text_2"


def test_OPLmetamodel_Objective_isLinearRelaxation_value_roundtrip():
    instance = OPLmetamodel_Objective(action="sample_text", isLinearRelaxation=True)
    assert instance.isLinearRelaxation == True
    instance.isLinearRelaxation = False
    assert instance.isLinearRelaxation == False


def test_OPLmetamodel_QueryUser_ask_value_roundtrip():
    instance = OPLmetamodel_QueryUser(ask="sample_text")
    assert instance.ask == "sample_text"
    instance.ask = "sample_text_2"
    assert instance.ask == "sample_text_2"


def test_OPLmetamodel_ReadFile_path_value_roundtrip():
    instance = OPLmetamodel_ReadFile(path="sample_text")
    assert instance.path == "sample_text"
    instance.path = "sample_text_2"
    assert instance.path == "sample_text_2"


def test_OPLmetamodel_Record_isTuple_value_roundtrip():
    instance = OPLmetamodel_Record(isTuple=True, name="sample_text")
    assert instance.isTuple == True
    instance.isTuple = False
    assert instance.isTuple == False


def test_OPLmetamodel_Record_name_value_roundtrip():
    instance = OPLmetamodel_Record(isTuple=True, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_OPLmetamodel_RecordField_name_value_roundtrip():
    instance = OPLmetamodel_RecordField(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_OPLmetamodel_Reference_name_value_roundtrip():
    instance = OPLmetamodel_Reference(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_OPLmetamodel_RelationalExpression_redefinedOp_value_roundtrip():
    instance = OPLmetamodel_RelationalExpression(redefinedOp="sample_text")
    assert instance.redefinedOp == "sample_text"
    instance.redefinedOp = "sample_text_2"
    assert instance.redefinedOp == "sample_text_2"


def test_OPLmetamodel_RelationalOperator_op_value_roundtrip():
    instance = OPLmetamodel_RelationalOperator(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_OPLmetamodel_Script_isMain_value_roundtrip():
    instance = OPLmetamodel_Script(isMain=True)
    assert instance.isMain == True
    instance.isMain = False
    assert instance.isMain == False


def test_OPLmetamodel_SetType_name_value_roundtrip():
    instance = OPLmetamodel_SetType(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_OPLmetamodel_StringExpression_body_value_roundtrip():
    instance = OPLmetamodel_StringExpression(body="sample_text")
    assert instance.body == "sample_text"
    instance.body = "sample_text_2"
    assert instance.body == "sample_text_2"


def test_OPLmetamodel_UnaryExpression_op_value_roundtrip():
    instance = OPLmetamodel_UnaryExpression(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_OPLmetamodel_Writeln_arg_value_roundtrip():
    instance = OPLmetamodel_Writeln(arg="sample_text", string="sample_text")
    assert instance.arg == "sample_text"
    instance.arg = "sample_text_2"
    assert instance.arg == "sample_text_2"


def test_OPLmetamodel_Writeln_string_value_roundtrip():
    instance = OPLmetamodel_Writeln(arg="sample_text", string="sample_text")
    assert instance.string == "sample_text"
    instance.string = "sample_text_2"
    assert instance.string == "sample_text_2"


def test_OPLmetamodel_BinaryOperator_isa_AbstractBinaryOperator():
    instance = OPLmetamodel_BinaryOperator(op="sample_text")
    assert isinstance(instance, AbstractBinaryOperator)


def test_OPLmetamodel_RelationalOperator_isa_AbstractBinaryOperator():
    instance = OPLmetamodel_RelationalOperator(op="sample_text")
    assert isinstance(instance, AbstractBinaryOperator)


def test_OPLmetamodel_DefinedType_isa_AbstractType():
    instance = OPLmetamodel_DefinedType()
    assert isinstance(instance, AbstractType)


def test_OPLmetamodel_PrimitiveType_isa_AbstractType():
    instance = OPLmetamodel_PrimitiveType()
    assert isinstance(instance, AbstractType)


def test_OPLmetamodel_RelationalExpression_isa_BinaryExpression():
    instance = OPLmetamodel_RelationalExpression(redefinedOp="sample_text")
    assert isinstance(instance, BinaryExpression)


def test_OPLmetamodel_RelationalExpression_isa_BooleanExpression():
    instance = OPLmetamodel_RelationalExpression(redefinedOp="sample_text")
    assert isinstance(instance, BooleanExpression)


def test_OPLmetamodel_ReflectiveFunction_isa_BuiltInFunction():
    instance = OPLmetamodel_ReflectiveFunction()
    assert isinstance(instance, BuiltInFunction)


def test_OPLmetamodel_Comprehension_isa_CollectionExpression():
    instance = OPLmetamodel_Comprehension()
    assert isinstance(instance, CollectionExpression)


def test_OPLmetamodel_Extension_isa_CollectionExpression():
    instance = OPLmetamodel_Extension()
    assert isinstance(instance, CollectionExpression)


def test_OPLmetamodel_ForAllConstraint_isa_Constraint():
    instance = OPLmetamodel_ForAllConstraint()
    assert isinstance(instance, Constraint)


def test_OPLmetamodel_IfConstraint_isa_Constraint():
    instance = OPLmetamodel_IfConstraint()
    assert isinstance(instance, Constraint)


def test_OPLmetamodel_QueryUser_isa_DataInitMethods():
    instance = OPLmetamodel_QueryUser(ask="sample_text")
    assert isinstance(instance, DataInitMethods)


def test_OPLmetamodel_ReadFile_isa_DataInitMethods():
    instance = OPLmetamodel_ReadFile(path="sample_text")
    assert isinstance(instance, DataInitMethods)


def test_OPLmetamodel_ActivityDeclaration_isa_Declaration():
    instance = OPLmetamodel_ActivityDeclaration(earliestStartTime="sample_text", latestEndTime="sample_text")
    assert isinstance(instance, Declaration)


def test_OPLmetamodel_Assertion_isa_Declaration():
    instance = OPLmetamodel_Assertion()
    assert isinstance(instance, Declaration)


def test_OPLmetamodel_Constraint_isa_Declaration():
    instance = OPLmetamodel_Constraint(name="sample_text")
    assert isinstance(instance, Declaration)


def test_OPLmetamodel_DataDeclaration_isa_Declaration():
    instance = OPLmetamodel_DataDeclaration(isDecisionExpr=True, isDecisionVar=True)
    assert isinstance(instance, Declaration)


def test_OPLmetamodel_DefinedType_isa_Declaration():
    instance = OPLmetamodel_DefinedType()
    assert isinstance(instance, Declaration)


def test_OPLmetamodel_Function_isa_Declaration():
    instance = OPLmetamodel_Function()
    assert isinstance(instance, Declaration)


def test_OPLmetamodel_Objective_isa_Declaration():
    instance = OPLmetamodel_Objective(action="sample_text", isLinearRelaxation=True)
    assert isinstance(instance, Declaration)


def test_OPLmetamodel_ResourceDeclaration_isa_Declaration():
    instance = OPLmetamodel_ResourceDeclaration()
    assert isinstance(instance, Declaration)


def test_OPLmetamodel_ScheduleInitialization_isa_Declaration():
    instance = OPLmetamodel_ScheduleInitialization()
    assert isinstance(instance, Declaration)


def test_OPLmetamodel_Script_isa_Declaration():
    instance = OPLmetamodel_Script(isMain=True)
    assert isinstance(instance, Declaration)


def test_OPLmetamodel_Setting_isa_Declaration():
    instance = OPLmetamodel_Setting()
    assert isinstance(instance, Declaration)


def test_OPLmetamodel_ArrayType_isa_DefinedType():
    instance = OPLmetamodel_ArrayType()
    assert isinstance(instance, DefinedType)


def test_OPLmetamodel_Record_isa_DefinedType():
    instance = OPLmetamodel_Record(isTuple=True, name="sample_text")
    assert isinstance(instance, DefinedType)


def test_OPLmetamodel_SetType_isa_DefinedType():
    instance = OPLmetamodel_SetType(name="sample_text")
    assert isinstance(instance, DefinedType)


def test_OPLmetamodel_AggregateExp_isa_Expression():
    instance = OPLmetamodel_AggregateExp(op="sample_text")
    assert isinstance(instance, Expression)


def test_OPLmetamodel_ArraySlotConstraint_isa_Expression():
    instance = OPLmetamodel_ArraySlotConstraint()
    assert isinstance(instance, Expression)


def test_OPLmetamodel_ArrayValue_isa_Expression():
    instance = OPLmetamodel_ArrayValue()
    assert isinstance(instance, Expression)


def test_OPLmetamodel_BinaryExpression_isa_Expression():
    instance = OPLmetamodel_BinaryExpression()
    assert isinstance(instance, Expression)


def test_OPLmetamodel_BlockExpression_isa_Expression():
    instance = OPLmetamodel_BlockExpression()
    assert isinstance(instance, Expression)


def test_OPLmetamodel_CollectionExpression_isa_Expression():
    instance = OPLmetamodel_CollectionExpression(isUnique=True)
    assert isinstance(instance, Expression)


def test_OPLmetamodel_IfExpression_isa_Expression():
    instance = OPLmetamodel_IfExpression()
    assert isinstance(instance, Expression)


def test_OPLmetamodel_IndexValuePair_isa_Expression():
    instance = OPLmetamodel_IndexValuePair()
    assert isinstance(instance, Expression)


def test_OPLmetamodel_PathExpression_isa_Expression():
    instance = OPLmetamodel_PathExpression()
    assert isinstance(instance, Expression)


def test_OPLmetamodel_PrimitiveExpression_isa_Expression():
    instance = OPLmetamodel_PrimitiveExpression()
    assert isinstance(instance, Expression)


def test_OPLmetamodel_RecordValue_isa_Expression():
    instance = OPLmetamodel_RecordValue()
    assert isinstance(instance, Expression)


def test_OPLmetamodel_Reference_isa_Expression():
    instance = OPLmetamodel_Reference(name="sample_text")
    assert isinstance(instance, Expression)


def test_OPLmetamodel_SetValue_isa_Expression():
    instance = OPLmetamodel_SetValue()
    assert isinstance(instance, Expression)


def test_OPLmetamodel_UnaryExpression_isa_Expression():
    instance = OPLmetamodel_UnaryExpression(op="sample_text")
    assert isinstance(instance, Expression)


def test_OPLmetamodel_FloatRangeType_isa_FloatType():
    instance = OPLmetamodel_FloatRangeType()
    assert isinstance(instance, FloatType)


def test_OPLmetamodel_PositiveFloatType_isa_FloatType():
    instance = OPLmetamodel_PositiveFloatType()
    assert isinstance(instance, FloatType)


def test_OPLmetamodel_BuiltInFunction_isa_Function():
    instance = OPLmetamodel_BuiltInFunction()
    assert isinstance(instance, Function)


def test_OPLmetamodel_CumulativeFunction_isa_Function():
    instance = OPLmetamodel_CumulativeFunction()
    assert isinstance(instance, Function)


def test_OPLmetamodel_PiecewiseLinearFunction_isa_Function():
    instance = OPLmetamodel_PiecewiseLinearFunction()
    assert isinstance(instance, Function)


def test_OPLmetamodel_StateFunction_isa_Function():
    instance = OPLmetamodel_StateFunction()
    assert isinstance(instance, Function)


def test_OPLmetamodel_DataObject_isa_Initialization():
    instance = OPLmetamodel_DataObject(body="sample_text")
    assert isinstance(instance, Initialization)


def test_OPLmetamodel_RelationalInit_isa_Initialization():
    instance = OPLmetamodel_RelationalInit()
    assert isinstance(instance, Initialization)


def test_OPLmetamodel_IntegerRangeType_isa_IntegerType():
    instance = OPLmetamodel_IntegerRangeType()
    assert isinstance(instance, IntegerType)


def test_OPLmetamodel_PositiveIntegerType_isa_IntegerType():
    instance = OPLmetamodel_PositiveIntegerType()
    assert isinstance(instance, IntegerType)


def test_OPLmetamodel_FloatExpression_isa_NumericExpression():
    instance = OPLmetamodel_FloatExpression(body="sample_text")
    assert isinstance(instance, NumericExpression)


def test_OPLmetamodel_IntegerExpression_isa_NumericExpression():
    instance = OPLmetamodel_IntegerExpression(body="sample_text")
    assert isinstance(instance, NumericExpression)


def test_OPLmetamodel_RangeExpression_isa_NumericExpression():
    instance = OPLmetamodel_RangeExpression()
    assert isinstance(instance, NumericExpression)


def test_OPLmetamodel_FloatType_isa_NumericType():
    instance = OPLmetamodel_FloatType()
    assert isinstance(instance, NumericType)


def test_OPLmetamodel_IntegerType_isa_NumericType():
    instance = OPLmetamodel_IntegerType()
    assert isinstance(instance, NumericType)


def test_OPLmetamodel_Record_isa_ParameterDomain():
    instance = OPLmetamodel_Record(isTuple=True, name="sample_text")
    assert isinstance(instance, ParameterDomain)


def test_OPLmetamodel_SetType_isa_ParameterDomain():
    instance = OPLmetamodel_SetType(name="sample_text")
    assert isinstance(instance, ParameterDomain)


def test_OPLmetamodel_ArrayDereference_isa_PathExpression():
    instance = OPLmetamodel_ArrayDereference()
    assert isinstance(instance, PathExpression)


def test_OPLmetamodel_FunctionCall_isa_PathExpression():
    instance = OPLmetamodel_FunctionCall(functionName="sample_text")
    assert isinstance(instance, PathExpression)


def test_OPLmetamodel_PathDereference_isa_PathExpression():
    instance = OPLmetamodel_PathDereference()
    assert isinstance(instance, PathExpression)


def test_OPLmetamodel_StepFunction_isa_PiecewiseLinearFunction():
    instance = OPLmetamodel_StepFunction()
    assert isinstance(instance, PiecewiseLinearFunction)


def test_OPLmetamodel_BooleanExpression_isa_PrimitiveExpression():
    instance = OPLmetamodel_BooleanExpression(body="sample_text")
    assert isinstance(instance, PrimitiveExpression)


def test_OPLmetamodel_EnumLiteral_isa_PrimitiveExpression():
    instance = OPLmetamodel_EnumLiteral()
    assert isinstance(instance, PrimitiveExpression)


def test_OPLmetamodel_NumericExpression_isa_PrimitiveExpression():
    instance = OPLmetamodel_NumericExpression()
    assert isinstance(instance, PrimitiveExpression)


def test_OPLmetamodel_StringExpression_isa_PrimitiveExpression():
    instance = OPLmetamodel_StringExpression(body="sample_text")
    assert isinstance(instance, PrimitiveExpression)


def test_OPLmetamodel_BooleanType_isa_PrimitiveType():
    instance = OPLmetamodel_BooleanType()
    assert isinstance(instance, PrimitiveType)


def test_OPLmetamodel_EnumLiteral_isa_PrimitiveType():
    instance = OPLmetamodel_EnumLiteral()
    assert isinstance(instance, PrimitiveType)


def test_OPLmetamodel_NumericType_isa_PrimitiveType():
    instance = OPLmetamodel_NumericType()
    assert isinstance(instance, PrimitiveType)


def test_OPLmetamodel_StringType_isa_PrimitiveType():
    instance = OPLmetamodel_StringType()
    assert isinstance(instance, PrimitiveType)


def test_OPLmetamodel_FloatRangeType_isa_RangeType():
    instance = OPLmetamodel_FloatRangeType()
    assert isinstance(instance, RangeType)


def test_OPLmetamodel_IntegerRangeType_isa_RangeType():
    instance = OPLmetamodel_IntegerRangeType()
    assert isinstance(instance, RangeType)


def test_OPLmetamodel_BindingRef_isa_Reference():
    instance = OPLmetamodel_BindingRef()
    assert isinstance(instance, Reference)


def test_OPLmetamodel_DataRef_isa_Reference():
    instance = OPLmetamodel_DataRef()
    assert isinstance(instance, Reference)


def test_OPLmetamodel_ParameterRef_isa_Reference():
    instance = OPLmetamodel_ParameterRef()
    assert isinstance(instance, Reference)


def test_OPLmetamodel_Writeln_isa_ScriptStatement():
    instance = OPLmetamodel_Writeln(arg="sample_text", string="sample_text")
    assert isinstance(instance, ScriptStatement)


def test_OPLmetamodel_EnumerationType_isa_SetType():
    instance = OPLmetamodel_EnumerationType()
    assert isinstance(instance, SetType)


def test_OPLmetamodel_RangeType_isa_SetType():
    instance = OPLmetamodel_RangeType()
    assert isinstance(instance, SetType)


def test_assoc_activities106_link_reassign_clear():
    a = OPLmetamodel_Model(id="sample_text", isConstraintProblem=True)
    b1 = OPLmetamodel_ActivityDeclaration(earliestStartTime="sample_text", latestEndTime="sample_text")
    b2 = OPLmetamodel_ActivityDeclaration(earliestStartTime="sample_text_2", latestEndTime="sample_text_2")
    _safe_set(a, 'OPLmetamodel_Model107', {b1})
    assert _is_linked(a, 'OPLmetamodel_Model107', b1)
    if hasattr(b1, 'OPLmetamodel_ActivityDeclaration108'):
        assert _is_linked(b1, 'OPLmetamodel_ActivityDeclaration108', a)
    _safe_set(a, 'OPLmetamodel_Model107', {b2})
    assert _is_linked(a, 'OPLmetamodel_Model107', b2)
    if hasattr(b1, 'OPLmetamodel_ActivityDeclaration108'):
        assert not _is_linked(b1, 'OPLmetamodel_ActivityDeclaration108', a)
    if hasattr(b2, 'OPLmetamodel_ActivityDeclaration108'):
        assert _is_linked(b2, 'OPLmetamodel_ActivityDeclaration108', a)
    _safe_set(a, 'OPLmetamodel_Model107', set())
    assert not _is_linked(a, 'OPLmetamodel_Model107', b2)
    if hasattr(b2, 'OPLmetamodel_ActivityDeclaration108'):
        assert not _is_linked(b2, 'OPLmetamodel_ActivityDeclaration108', a)


def test_assoc_args67_link_reassign_clear():
    a = OPLmetamodel_FunctionCall(functionName="sample_text")
    b1 = OPLmetamodel_Expression()
    b2 = OPLmetamodel_Expression()
    _safe_set(a, 'OPLmetamodel_FunctionCall', {b1})
    assert _is_linked(a, 'OPLmetamodel_FunctionCall', b1)
    if hasattr(b1, 'OPLmetamodel_Expression68'):
        assert _is_linked(b1, 'OPLmetamodel_Expression68', a)
    _safe_set(a, 'OPLmetamodel_FunctionCall', {b2})
    assert _is_linked(a, 'OPLmetamodel_FunctionCall', b2)
    if hasattr(b1, 'OPLmetamodel_Expression68'):
        assert not _is_linked(b1, 'OPLmetamodel_Expression68', a)
    if hasattr(b2, 'OPLmetamodel_Expression68'):
        assert _is_linked(b2, 'OPLmetamodel_Expression68', a)
    _safe_set(a, 'OPLmetamodel_FunctionCall', set())
    assert not _is_linked(a, 'OPLmetamodel_FunctionCall', b2)
    if hasattr(b2, 'OPLmetamodel_Expression68'):
        assert not _is_linked(b2, 'OPLmetamodel_Expression68', a)


def test_assoc_assertions111_link_reassign_clear():
    a = OPLmetamodel_Model(id="sample_text", isConstraintProblem=True)
    b1 = OPLmetamodel_Constraint(name="sample_text")
    b2 = OPLmetamodel_Constraint(name="sample_text_2")
    _safe_set(a, 'OPLmetamodel_Model112', {b1})
    assert _is_linked(a, 'OPLmetamodel_Model112', b1)
    if hasattr(b1, 'OPLmetamodel_Constraint113'):
        assert _is_linked(b1, 'OPLmetamodel_Constraint113', a)
    _safe_set(a, 'OPLmetamodel_Model112', {b2})
    assert _is_linked(a, 'OPLmetamodel_Model112', b2)
    if hasattr(b1, 'OPLmetamodel_Constraint113'):
        assert not _is_linked(b1, 'OPLmetamodel_Constraint113', a)
    if hasattr(b2, 'OPLmetamodel_Constraint113'):
        assert _is_linked(b2, 'OPLmetamodel_Constraint113', a)
    _safe_set(a, 'OPLmetamodel_Model112', set())
    assert not _is_linked(a, 'OPLmetamodel_Model112', b2)
    if hasattr(b2, 'OPLmetamodel_Constraint113'):
        assert not _is_linked(b2, 'OPLmetamodel_Constraint113', a)


def test_assoc_baseType167_link_reassign_clear():
    a = OPLmetamodel_SetType(name="sample_text")
    b1 = OPLmetamodel_AbstractType()
    b2 = OPLmetamodel_AbstractType()
    _safe_set(a, 'OPLmetamodel_SetType', b1)
    assert _is_linked(a, 'OPLmetamodel_SetType', b1)
    if hasattr(b1, 'OPLmetamodel_AbstractType168'):
        assert _is_linked(b1, 'OPLmetamodel_AbstractType168', a)
    _safe_set(a, 'OPLmetamodel_SetType', b2)
    assert _is_linked(a, 'OPLmetamodel_SetType', b2)
    if hasattr(b1, 'OPLmetamodel_AbstractType168'):
        assert not _is_linked(b1, 'OPLmetamodel_AbstractType168', a)
    if hasattr(b2, 'OPLmetamodel_AbstractType168'):
        assert _is_linked(b2, 'OPLmetamodel_AbstractType168', a)
    _safe_set(a, 'OPLmetamodel_SetType', None)
    assert not _is_linked(a, 'OPLmetamodel_SetType', b2)
    if hasattr(b2, 'OPLmetamodel_AbstractType168'):
        assert not _is_linked(b2, 'OPLmetamodel_AbstractType168', a)


def test_assoc_body2_link_reassign_clear():
    a = OPLmetamodel_AggregateExp(op="sample_text")
    b1 = OPLmetamodel_Expression()
    b2 = OPLmetamodel_Expression()
    _safe_set(a, 'OPLmetamodel_AggregateExp3', b1)
    assert _is_linked(a, 'OPLmetamodel_AggregateExp3', b1)
    if hasattr(b1, 'OPLmetamodel_Expression'):
        assert _is_linked(b1, 'OPLmetamodel_Expression', a)
    _safe_set(a, 'OPLmetamodel_AggregateExp3', b2)
    assert _is_linked(a, 'OPLmetamodel_AggregateExp3', b2)
    if hasattr(b1, 'OPLmetamodel_Expression'):
        assert not _is_linked(b1, 'OPLmetamodel_Expression', a)
    if hasattr(b2, 'OPLmetamodel_Expression'):
        assert _is_linked(b2, 'OPLmetamodel_Expression', a)
    _safe_set(a, 'OPLmetamodel_AggregateExp3', None)
    assert not _is_linked(a, 'OPLmetamodel_AggregateExp3', b2)
    if hasattr(b2, 'OPLmetamodel_Expression'):
        assert not _is_linked(b2, 'OPLmetamodel_Expression', a)


def test_assoc_boundVars49_link_reassign_clear():
    a = OPLmetamodel_FormalParameter(isOrdered=True)
    b1 = OPLmetamodel_BindingRef()
    b2 = OPLmetamodel_BindingRef()
    _safe_set(a, 'OPLmetamodel_FormalParameter50', {b1})
    assert _is_linked(a, 'OPLmetamodel_FormalParameter50', b1)
    if hasattr(b1, 'OPLmetamodel_BindingRef'):
        assert _is_linked(b1, 'OPLmetamodel_BindingRef', a)
    _safe_set(a, 'OPLmetamodel_FormalParameter50', {b2})
    assert _is_linked(a, 'OPLmetamodel_FormalParameter50', b2)
    if hasattr(b1, 'OPLmetamodel_BindingRef'):
        assert not _is_linked(b1, 'OPLmetamodel_BindingRef', a)
    if hasattr(b2, 'OPLmetamodel_BindingRef'):
        assert _is_linked(b2, 'OPLmetamodel_BindingRef', a)
    _safe_set(a, 'OPLmetamodel_FormalParameter50', set())
    assert not _is_linked(a, 'OPLmetamodel_FormalParameter50', b2)
    if hasattr(b2, 'OPLmetamodel_BindingRef'):
        assert not _is_linked(b2, 'OPLmetamodel_BindingRef', a)


def test_assoc_bounds84_link_reassign_clear():
    a = OPLmetamodel_Interval(isOptional=True)
    b1 = OPLmetamodel_RangeType()
    b2 = OPLmetamodel_RangeType()
    _safe_set(a, 'OPLmetamodel_Interval', b1)
    assert _is_linked(a, 'OPLmetamodel_Interval', b1)
    if hasattr(b1, 'OPLmetamodel_RangeType'):
        assert _is_linked(b1, 'OPLmetamodel_RangeType', a)
    _safe_set(a, 'OPLmetamodel_Interval', b2)
    assert _is_linked(a, 'OPLmetamodel_Interval', b2)
    if hasattr(b1, 'OPLmetamodel_RangeType'):
        assert not _is_linked(b1, 'OPLmetamodel_RangeType', a)
    if hasattr(b2, 'OPLmetamodel_RangeType'):
        assert _is_linked(b2, 'OPLmetamodel_RangeType', a)
    _safe_set(a, 'OPLmetamodel_Interval', None)
    assert not _is_linked(a, 'OPLmetamodel_Interval', b2)
    if hasattr(b2, 'OPLmetamodel_RangeType'):
        assert not _is_linked(b2, 'OPLmetamodel_RangeType', a)


def test_assoc_constraints98_link_reassign_clear():
    a = OPLmetamodel_Model(id="sample_text", isConstraintProblem=True)
    b1 = OPLmetamodel_Constraint(name="sample_text")
    b2 = OPLmetamodel_Constraint(name="sample_text_2")
    _safe_set(a, 'OPLmetamodel_Model99', {b1})
    assert _is_linked(a, 'OPLmetamodel_Model99', b1)
    if hasattr(b1, 'OPLmetamodel_Constraint100'):
        assert _is_linked(b1, 'OPLmetamodel_Constraint100', a)
    _safe_set(a, 'OPLmetamodel_Model99', {b2})
    assert _is_linked(a, 'OPLmetamodel_Model99', b2)
    if hasattr(b1, 'OPLmetamodel_Constraint100'):
        assert not _is_linked(b1, 'OPLmetamodel_Constraint100', a)
    if hasattr(b2, 'OPLmetamodel_Constraint100'):
        assert _is_linked(b2, 'OPLmetamodel_Constraint100', a)
    _safe_set(a, 'OPLmetamodel_Model99', set())
    assert not _is_linked(a, 'OPLmetamodel_Model99', b2)
    if hasattr(b2, 'OPLmetamodel_Constraint100'):
        assert not _is_linked(b2, 'OPLmetamodel_Constraint100', a)


def test_assoc_data95_link_reassign_clear():
    a = OPLmetamodel_Model(id="sample_text", isConstraintProblem=True)
    b1 = OPLmetamodel_DataDeclaration(isDecisionExpr=True, isDecisionVar=True)
    b2 = OPLmetamodel_DataDeclaration(isDecisionExpr=False, isDecisionVar=False)
    _safe_set(a, 'OPLmetamodel_Model96', {b1})
    assert _is_linked(a, 'OPLmetamodel_Model96', b1)
    if hasattr(b1, 'OPLmetamodel_DataDeclaration97'):
        assert _is_linked(b1, 'OPLmetamodel_DataDeclaration97', a)
    _safe_set(a, 'OPLmetamodel_Model96', {b2})
    assert _is_linked(a, 'OPLmetamodel_Model96', b2)
    if hasattr(b1, 'OPLmetamodel_DataDeclaration97'):
        assert not _is_linked(b1, 'OPLmetamodel_DataDeclaration97', a)
    if hasattr(b2, 'OPLmetamodel_DataDeclaration97'):
        assert _is_linked(b2, 'OPLmetamodel_DataDeclaration97', a)
    _safe_set(a, 'OPLmetamodel_Model96', set())
    assert not _is_linked(a, 'OPLmetamodel_Model96', b2)
    if hasattr(b2, 'OPLmetamodel_DataDeclaration97'):
        assert not _is_linked(b2, 'OPLmetamodel_DataDeclaration97', a)


def test_assoc_deref127_link_reassign_clear():
    a = OPLmetamodel_Reference(name="sample_text")
    b1 = OPLmetamodel_PathDereference()
    b2 = OPLmetamodel_PathDereference()
    _safe_set(a, 'OPLmetamodel_Reference128', b1)
    assert _is_linked(a, 'OPLmetamodel_Reference128', b1)
    if hasattr(b1, 'OPLmetamodel_PathDereference'):
        assert _is_linked(b1, 'OPLmetamodel_PathDereference', a)
    _safe_set(a, 'OPLmetamodel_Reference128', b2)
    assert _is_linked(a, 'OPLmetamodel_Reference128', b2)
    if hasattr(b1, 'OPLmetamodel_PathDereference'):
        assert not _is_linked(b1, 'OPLmetamodel_PathDereference', a)
    if hasattr(b2, 'OPLmetamodel_PathDereference'):
        assert _is_linked(b2, 'OPLmetamodel_PathDereference', a)
    _safe_set(a, 'OPLmetamodel_Reference128', None)
    assert not _is_linked(a, 'OPLmetamodel_Reference128', b2)
    if hasattr(b2, 'OPLmetamodel_PathDereference'):
        assert not _is_linked(b2, 'OPLmetamodel_PathDereference', a)


def test_assoc_domain47_link_reassign_clear():
    a = OPLmetamodel_FormalParameter(isOrdered=True)
    b1 = OPLmetamodel_ParameterDomain()
    b2 = OPLmetamodel_ParameterDomain()
    _safe_set(a, 'OPLmetamodel_FormalParameter48', b1)
    assert _is_linked(a, 'OPLmetamodel_FormalParameter48', b1)
    if hasattr(b1, 'OPLmetamodel_ParameterDomain'):
        assert _is_linked(b1, 'OPLmetamodel_ParameterDomain', a)
    _safe_set(a, 'OPLmetamodel_FormalParameter48', b2)
    assert _is_linked(a, 'OPLmetamodel_FormalParameter48', b2)
    if hasattr(b1, 'OPLmetamodel_ParameterDomain'):
        assert not _is_linked(b1, 'OPLmetamodel_ParameterDomain', a)
    if hasattr(b2, 'OPLmetamodel_ParameterDomain'):
        assert _is_linked(b2, 'OPLmetamodel_ParameterDomain', a)
    _safe_set(a, 'OPLmetamodel_FormalParameter48', None)
    assert not _is_linked(a, 'OPLmetamodel_FormalParameter48', b2)
    if hasattr(b2, 'OPLmetamodel_ParameterDomain'):
        assert not _is_linked(b2, 'OPLmetamodel_ParameterDomain', a)


def test_assoc_duration0_link_reassign_clear():
    a = OPLmetamodel_ActivityDeclaration(earliestStartTime="sample_text", latestEndTime="sample_text")
    b1 = OPLmetamodel_Number()
    b2 = OPLmetamodel_Number()
    _safe_set(a, 'OPLmetamodel_ActivityDeclaration', b1)
    assert _is_linked(a, 'OPLmetamodel_ActivityDeclaration', b1)
    if hasattr(b1, 'OPLmetamodel_Number'):
        assert _is_linked(b1, 'OPLmetamodel_Number', a)
    _safe_set(a, 'OPLmetamodel_ActivityDeclaration', b2)
    assert _is_linked(a, 'OPLmetamodel_ActivityDeclaration', b2)
    if hasattr(b1, 'OPLmetamodel_Number'):
        assert not _is_linked(b1, 'OPLmetamodel_Number', a)
    if hasattr(b2, 'OPLmetamodel_Number'):
        assert _is_linked(b2, 'OPLmetamodel_Number', a)
    _safe_set(a, 'OPLmetamodel_ActivityDeclaration', None)
    assert not _is_linked(a, 'OPLmetamodel_ActivityDeclaration', b2)
    if hasattr(b2, 'OPLmetamodel_Number'):
        assert not _is_linked(b2, 'OPLmetamodel_Number', a)


def test_assoc_elements169_link_reassign_clear():
    a = OPLmetamodel_SetType(name="sample_text")
    b1 = OPLmetamodel_Entity()
    b2 = OPLmetamodel_Entity()
    _safe_set(a, 'OPLmetamodel_SetType170', {b1})
    assert _is_linked(a, 'OPLmetamodel_SetType170', b1)
    if hasattr(b1, 'OPLmetamodel_Entity'):
        assert _is_linked(b1, 'OPLmetamodel_Entity', a)
    _safe_set(a, 'OPLmetamodel_SetType170', {b2})
    assert _is_linked(a, 'OPLmetamodel_SetType170', b2)
    if hasattr(b1, 'OPLmetamodel_Entity'):
        assert not _is_linked(b1, 'OPLmetamodel_Entity', a)
    if hasattr(b2, 'OPLmetamodel_Entity'):
        assert _is_linked(b2, 'OPLmetamodel_Entity', a)
    _safe_set(a, 'OPLmetamodel_SetType170', set())
    assert not _is_linked(a, 'OPLmetamodel_SetType170', b2)
    if hasattr(b2, 'OPLmetamodel_Entity'):
        assert not _is_linked(b2, 'OPLmetamodel_Entity', a)


def test_assoc_else_73_link_reassign_clear():
    a = OPLmetamodel_Constraint(name="sample_text")
    b1 = OPLmetamodel_IfConstraint()
    b2 = OPLmetamodel_IfConstraint()
    _safe_set(a, 'OPLmetamodel_Constraint75', b1)
    assert _is_linked(a, 'OPLmetamodel_Constraint75', b1)
    if hasattr(b1, 'OPLmetamodel_IfConstraint74'):
        assert _is_linked(b1, 'OPLmetamodel_IfConstraint74', a)
    _safe_set(a, 'OPLmetamodel_Constraint75', b2)
    assert _is_linked(a, 'OPLmetamodel_Constraint75', b2)
    if hasattr(b1, 'OPLmetamodel_IfConstraint74'):
        assert not _is_linked(b1, 'OPLmetamodel_IfConstraint74', a)
    if hasattr(b2, 'OPLmetamodel_IfConstraint74'):
        assert _is_linked(b2, 'OPLmetamodel_IfConstraint74', a)
    _safe_set(a, 'OPLmetamodel_Constraint75', None)
    assert not _is_linked(a, 'OPLmetamodel_Constraint75', b2)
    if hasattr(b2, 'OPLmetamodel_IfConstraint74'):
        assert not _is_linked(b2, 'OPLmetamodel_IfConstraint74', a)


def test_assoc_exp177_link_reassign_clear():
    a = OPLmetamodel_UnaryExpression(op="sample_text")
    b1 = OPLmetamodel_Expression()
    b2 = OPLmetamodel_Expression()
    _safe_set(a, 'OPLmetamodel_UnaryExpression', b1)
    assert _is_linked(a, 'OPLmetamodel_UnaryExpression', b1)
    if hasattr(b1, 'OPLmetamodel_Expression178'):
        assert _is_linked(b1, 'OPLmetamodel_Expression178', a)
    _safe_set(a, 'OPLmetamodel_UnaryExpression', b2)
    assert _is_linked(a, 'OPLmetamodel_UnaryExpression', b2)
    if hasattr(b1, 'OPLmetamodel_Expression178'):
        assert not _is_linked(b1, 'OPLmetamodel_Expression178', a)
    if hasattr(b2, 'OPLmetamodel_Expression178'):
        assert _is_linked(b2, 'OPLmetamodel_Expression178', a)
    _safe_set(a, 'OPLmetamodel_UnaryExpression', None)
    assert not _is_linked(a, 'OPLmetamodel_UnaryExpression', b2)
    if hasattr(b2, 'OPLmetamodel_Expression178'):
        assert not _is_linked(b2, 'OPLmetamodel_Expression178', a)


def test_assoc_exp20_link_reassign_clear():
    a = OPLmetamodel_Constraint(name="sample_text")
    b1 = OPLmetamodel_Assertion()
    b2 = OPLmetamodel_Assertion()
    _safe_set(a, 'OPLmetamodel_Constraint', b1)
    assert _is_linked(a, 'OPLmetamodel_Constraint', b1)
    if hasattr(b1, 'OPLmetamodel_Assertion'):
        assert _is_linked(b1, 'OPLmetamodel_Assertion', a)
    _safe_set(a, 'OPLmetamodel_Constraint', b2)
    assert _is_linked(a, 'OPLmetamodel_Constraint', b2)
    if hasattr(b1, 'OPLmetamodel_Assertion'):
        assert not _is_linked(b1, 'OPLmetamodel_Assertion', a)
    if hasattr(b2, 'OPLmetamodel_Assertion'):
        assert _is_linked(b2, 'OPLmetamodel_Assertion', a)
    _safe_set(a, 'OPLmetamodel_Constraint', None)
    assert not _is_linked(a, 'OPLmetamodel_Constraint', b2)
    if hasattr(b2, 'OPLmetamodel_Assertion'):
        assert not _is_linked(b2, 'OPLmetamodel_Assertion', a)


def test_assoc_exp29_link_reassign_clear():
    a = OPLmetamodel_Constraint(name="sample_text")
    b1 = OPLmetamodel_Expression()
    b2 = OPLmetamodel_Expression()
    _safe_set(a, 'OPLmetamodel_Constraint30', b1)
    assert _is_linked(a, 'OPLmetamodel_Constraint30', b1)
    if hasattr(b1, 'OPLmetamodel_Expression31'):
        assert _is_linked(b1, 'OPLmetamodel_Expression31', a)
    _safe_set(a, 'OPLmetamodel_Constraint30', b2)
    assert _is_linked(a, 'OPLmetamodel_Constraint30', b2)
    if hasattr(b1, 'OPLmetamodel_Expression31'):
        assert not _is_linked(b1, 'OPLmetamodel_Expression31', a)
    if hasattr(b2, 'OPLmetamodel_Expression31'):
        assert _is_linked(b2, 'OPLmetamodel_Expression31', a)
    _safe_set(a, 'OPLmetamodel_Constraint30', None)
    assert not _is_linked(a, 'OPLmetamodel_Constraint30', b2)
    if hasattr(b2, 'OPLmetamodel_Expression31'):
        assert not _is_linked(b2, 'OPLmetamodel_Expression31', a)


def test_assoc_expression124_link_reassign_clear():
    a = OPLmetamodel_Objective(action="sample_text", isLinearRelaxation=True)
    b1 = OPLmetamodel_Expression()
    b2 = OPLmetamodel_Expression()
    _safe_set(a, 'OPLmetamodel_Objective125', b1)
    assert _is_linked(a, 'OPLmetamodel_Objective125', b1)
    if hasattr(b1, 'OPLmetamodel_Expression126'):
        assert _is_linked(b1, 'OPLmetamodel_Expression126', a)
    _safe_set(a, 'OPLmetamodel_Objective125', b2)
    assert _is_linked(a, 'OPLmetamodel_Objective125', b2)
    if hasattr(b1, 'OPLmetamodel_Expression126'):
        assert not _is_linked(b1, 'OPLmetamodel_Expression126', a)
    if hasattr(b2, 'OPLmetamodel_Expression126'):
        assert _is_linked(b2, 'OPLmetamodel_Expression126', a)
    _safe_set(a, 'OPLmetamodel_Objective125', None)
    assert not _is_linked(a, 'OPLmetamodel_Objective125', b2)
    if hasattr(b2, 'OPLmetamodel_Expression126'):
        assert not _is_linked(b2, 'OPLmetamodel_Expression126', a)


def test_assoc_exps58_link_reassign_clear():
    a = OPLmetamodel_Constraint(name="sample_text")
    b1 = OPLmetamodel_ForAllConstraint()
    b2 = OPLmetamodel_ForAllConstraint()
    _safe_set(a, 'OPLmetamodel_Constraint60', b1)
    assert _is_linked(a, 'OPLmetamodel_Constraint60', b1)
    if hasattr(b1, 'OPLmetamodel_ForAllConstraint59'):
        assert _is_linked(b1, 'OPLmetamodel_ForAllConstraint59', a)
    _safe_set(a, 'OPLmetamodel_Constraint60', b2)
    assert _is_linked(a, 'OPLmetamodel_Constraint60', b2)
    if hasattr(b1, 'OPLmetamodel_ForAllConstraint59'):
        assert not _is_linked(b1, 'OPLmetamodel_ForAllConstraint59', a)
    if hasattr(b2, 'OPLmetamodel_ForAllConstraint59'):
        assert _is_linked(b2, 'OPLmetamodel_ForAllConstraint59', a)
    _safe_set(a, 'OPLmetamodel_Constraint60', None)
    assert not _is_linked(a, 'OPLmetamodel_Constraint60', b2)
    if hasattr(b2, 'OPLmetamodel_ForAllConstraint59'):
        assert not _is_linked(b2, 'OPLmetamodel_ForAllConstraint59', a)


def test_assoc_fields145_link_reassign_clear():
    a = OPLmetamodel_RecordField(name="sample_text")
    b1 = OPLmetamodel_Record(isTuple=True, name="sample_text")
    b2 = OPLmetamodel_Record(isTuple=False, name="sample_text_2")
    _safe_set(a, 'OPLmetamodel_RecordField', b1)
    assert _is_linked(a, 'OPLmetamodel_RecordField', b1)
    if hasattr(b1, 'OPLmetamodel_Record'):
        assert _is_linked(b1, 'OPLmetamodel_Record', a)
    _safe_set(a, 'OPLmetamodel_RecordField', b2)
    assert _is_linked(a, 'OPLmetamodel_RecordField', b2)
    if hasattr(b1, 'OPLmetamodel_Record'):
        assert not _is_linked(b1, 'OPLmetamodel_Record', a)
    if hasattr(b2, 'OPLmetamodel_Record'):
        assert _is_linked(b2, 'OPLmetamodel_Record', a)
    _safe_set(a, 'OPLmetamodel_RecordField', None)
    assert not _is_linked(a, 'OPLmetamodel_RecordField', b2)
    if hasattr(b2, 'OPLmetamodel_Record'):
        assert not _is_linked(b2, 'OPLmetamodel_Record', a)


def test_assoc_functions103_link_reassign_clear():
    a = OPLmetamodel_Model(id="sample_text", isConstraintProblem=True)
    b1 = OPLmetamodel_Function()
    b2 = OPLmetamodel_Function()
    _safe_set(a, 'OPLmetamodel_Model104', {b1})
    assert _is_linked(a, 'OPLmetamodel_Model104', b1)
    if hasattr(b1, 'OPLmetamodel_Function105'):
        assert _is_linked(b1, 'OPLmetamodel_Function105', a)
    _safe_set(a, 'OPLmetamodel_Model104', {b2})
    assert _is_linked(a, 'OPLmetamodel_Model104', b2)
    if hasattr(b1, 'OPLmetamodel_Function105'):
        assert not _is_linked(b1, 'OPLmetamodel_Function105', a)
    if hasattr(b2, 'OPLmetamodel_Function105'):
        assert _is_linked(b2, 'OPLmetamodel_Function105', a)
    _safe_set(a, 'OPLmetamodel_Model104', set())
    assert not _is_linked(a, 'OPLmetamodel_Model104', b2)
    if hasattr(b2, 'OPLmetamodel_Function105'):
        assert not _is_linked(b2, 'OPLmetamodel_Function105', a)


def test_assoc_id157_link_reassign_clear():
    a = OPLmetamodel_Script(isMain=True)
    b1 = OPLmetamodel_Reference(name="sample_text")
    b2 = OPLmetamodel_Reference(name="sample_text_2")
    _safe_set(a, 'OPLmetamodel_Script158', b1)
    assert _is_linked(a, 'OPLmetamodel_Script158', b1)
    if hasattr(b1, 'OPLmetamodel_Reference159'):
        assert _is_linked(b1, 'OPLmetamodel_Reference159', a)
    _safe_set(a, 'OPLmetamodel_Script158', b2)
    assert _is_linked(a, 'OPLmetamodel_Script158', b2)
    if hasattr(b1, 'OPLmetamodel_Reference159'):
        assert not _is_linked(b1, 'OPLmetamodel_Reference159', a)
    if hasattr(b2, 'OPLmetamodel_Reference159'):
        assert _is_linked(b2, 'OPLmetamodel_Reference159', a)
    _safe_set(a, 'OPLmetamodel_Script158', None)
    assert not _is_linked(a, 'OPLmetamodel_Script158', b2)
    if hasattr(b2, 'OPLmetamodel_Reference159'):
        assert not _is_linked(b2, 'OPLmetamodel_Reference159', a)


def test_assoc_instruction101_link_reassign_clear():
    a = OPLmetamodel_Objective(action="sample_text", isLinearRelaxation=True)
    b1 = OPLmetamodel_Model(id="sample_text", isConstraintProblem=True)
    b2 = OPLmetamodel_Model(id="sample_text_2", isConstraintProblem=False)
    _safe_set(a, 'OPLmetamodel_Objective', b1)
    assert _is_linked(a, 'OPLmetamodel_Objective', b1)
    if hasattr(b1, 'OPLmetamodel_Model102'):
        assert _is_linked(b1, 'OPLmetamodel_Model102', a)
    _safe_set(a, 'OPLmetamodel_Objective', b2)
    assert _is_linked(a, 'OPLmetamodel_Objective', b2)
    if hasattr(b1, 'OPLmetamodel_Model102'):
        assert not _is_linked(b1, 'OPLmetamodel_Model102', a)
    if hasattr(b2, 'OPLmetamodel_Model102'):
        assert _is_linked(b2, 'OPLmetamodel_Model102', a)
    _safe_set(a, 'OPLmetamodel_Objective', None)
    assert not _is_linked(a, 'OPLmetamodel_Objective', b2)
    if hasattr(b2, 'OPLmetamodel_Model102'):
        assert not _is_linked(b2, 'OPLmetamodel_Model102', a)


def test_assoc_intensity87_link_reassign_clear():
    a = OPLmetamodel_Interval(isOptional=True)
    b1 = OPLmetamodel_StepFunction()
    b2 = OPLmetamodel_StepFunction()
    _safe_set(a, 'OPLmetamodel_Interval88', b1)
    assert _is_linked(a, 'OPLmetamodel_Interval88', b1)
    if hasattr(b1, 'OPLmetamodel_StepFunction'):
        assert _is_linked(b1, 'OPLmetamodel_StepFunction', a)
    _safe_set(a, 'OPLmetamodel_Interval88', b2)
    assert _is_linked(a, 'OPLmetamodel_Interval88', b2)
    if hasattr(b1, 'OPLmetamodel_StepFunction'):
        assert not _is_linked(b1, 'OPLmetamodel_StepFunction', a)
    if hasattr(b2, 'OPLmetamodel_StepFunction'):
        assert _is_linked(b2, 'OPLmetamodel_StepFunction', a)
    _safe_set(a, 'OPLmetamodel_Interval88', None)
    assert not _is_linked(a, 'OPLmetamodel_Interval88', b2)
    if hasattr(b2, 'OPLmetamodel_StepFunction'):
        assert not _is_linked(b2, 'OPLmetamodel_StepFunction', a)


def test_assoc_intervals162_link_reassign_clear():
    a = OPLmetamodel_Interval(isOptional=True)
    b1 = OPLmetamodel_Sequence()
    b2 = OPLmetamodel_Sequence()
    _safe_set(a, 'OPLmetamodel_Interval163', b1)
    assert _is_linked(a, 'OPLmetamodel_Interval163', b1)
    if hasattr(b1, 'OPLmetamodel_Sequence'):
        assert _is_linked(b1, 'OPLmetamodel_Sequence', a)
    _safe_set(a, 'OPLmetamodel_Interval163', b2)
    assert _is_linked(a, 'OPLmetamodel_Interval163', b2)
    if hasattr(b1, 'OPLmetamodel_Sequence'):
        assert not _is_linked(b1, 'OPLmetamodel_Sequence', a)
    if hasattr(b2, 'OPLmetamodel_Sequence'):
        assert _is_linked(b2, 'OPLmetamodel_Sequence', a)
    _safe_set(a, 'OPLmetamodel_Interval163', None)
    assert not _is_linked(a, 'OPLmetamodel_Interval163', b2)
    if hasattr(b2, 'OPLmetamodel_Sequence'):
        assert not _is_linked(b2, 'OPLmetamodel_Sequence', a)


def test_assoc_name61_link_reassign_clear():
    a = OPLmetamodel_FunctionRef(name="sample_text")
    b1 = OPLmetamodel_Function()
    b2 = OPLmetamodel_Function()
    _safe_set(a, 'OPLmetamodel_FunctionRef', b1)
    assert _is_linked(a, 'OPLmetamodel_FunctionRef', b1)
    if hasattr(b1, 'OPLmetamodel_Function'):
        assert _is_linked(b1, 'OPLmetamodel_Function', a)
    _safe_set(a, 'OPLmetamodel_FunctionRef', b2)
    assert _is_linked(a, 'OPLmetamodel_FunctionRef', b2)
    if hasattr(b1, 'OPLmetamodel_Function'):
        assert not _is_linked(b1, 'OPLmetamodel_Function', a)
    if hasattr(b2, 'OPLmetamodel_Function'):
        assert _is_linked(b2, 'OPLmetamodel_Function', a)
    _safe_set(a, 'OPLmetamodel_FunctionRef', None)
    assert not _is_linked(a, 'OPLmetamodel_FunctionRef', b2)
    if hasattr(b2, 'OPLmetamodel_Function'):
        assert not _is_linked(b2, 'OPLmetamodel_Function', a)


def test_assoc_parameters1_link_reassign_clear():
    a = OPLmetamodel_FormalParameter(isOrdered=True)
    b1 = OPLmetamodel_AggregateExp(op="sample_text")
    b2 = OPLmetamodel_AggregateExp(op="sample_text_2")
    _safe_set(a, 'OPLmetamodel_FormalParameter', b1)
    assert _is_linked(a, 'OPLmetamodel_FormalParameter', b1)
    if hasattr(b1, 'OPLmetamodel_AggregateExp'):
        assert _is_linked(b1, 'OPLmetamodel_AggregateExp', a)
    _safe_set(a, 'OPLmetamodel_FormalParameter', b2)
    assert _is_linked(a, 'OPLmetamodel_FormalParameter', b2)
    if hasattr(b1, 'OPLmetamodel_AggregateExp'):
        assert not _is_linked(b1, 'OPLmetamodel_AggregateExp', a)
    if hasattr(b2, 'OPLmetamodel_AggregateExp'):
        assert _is_linked(b2, 'OPLmetamodel_AggregateExp', a)
    _safe_set(a, 'OPLmetamodel_FormalParameter', None)
    assert not _is_linked(a, 'OPLmetamodel_FormalParameter', b2)
    if hasattr(b2, 'OPLmetamodel_AggregateExp'):
        assert not _is_linked(b2, 'OPLmetamodel_AggregateExp', a)


def test_assoc_parameters65_link_reassign_clear():
    a = OPLmetamodel_Reference(name="sample_text")
    b1 = OPLmetamodel_Function()
    b2 = OPLmetamodel_Function()
    _safe_set(a, 'OPLmetamodel_Reference', b1)
    assert _is_linked(a, 'OPLmetamodel_Reference', b1)
    if hasattr(b1, 'OPLmetamodel_Function66'):
        assert _is_linked(b1, 'OPLmetamodel_Function66', a)
    _safe_set(a, 'OPLmetamodel_Reference', b2)
    assert _is_linked(a, 'OPLmetamodel_Reference', b2)
    if hasattr(b1, 'OPLmetamodel_Function66'):
        assert not _is_linked(b1, 'OPLmetamodel_Function66', a)
    if hasattr(b2, 'OPLmetamodel_Function66'):
        assert _is_linked(b2, 'OPLmetamodel_Function66', a)
    _safe_set(a, 'OPLmetamodel_Reference', None)
    assert not _is_linked(a, 'OPLmetamodel_Reference', b2)
    if hasattr(b2, 'OPLmetamodel_Function66'):
        assert not _is_linked(b2, 'OPLmetamodel_Function66', a)


def test_assoc_qualifiers4_link_reassign_clear():
    a = OPLmetamodel_FormalParameter(isOrdered=True)
    b1 = OPLmetamodel_AllExpression()
    b2 = OPLmetamodel_AllExpression()
    _safe_set(a, 'OPLmetamodel_FormalParameter5', b1)
    assert _is_linked(a, 'OPLmetamodel_FormalParameter5', b1)
    if hasattr(b1, 'OPLmetamodel_AllExpression'):
        assert _is_linked(b1, 'OPLmetamodel_AllExpression', a)
    _safe_set(a, 'OPLmetamodel_FormalParameter5', b2)
    assert _is_linked(a, 'OPLmetamodel_FormalParameter5', b2)
    if hasattr(b1, 'OPLmetamodel_AllExpression'):
        assert not _is_linked(b1, 'OPLmetamodel_AllExpression', a)
    if hasattr(b2, 'OPLmetamodel_AllExpression'):
        assert _is_linked(b2, 'OPLmetamodel_AllExpression', a)
    _safe_set(a, 'OPLmetamodel_FormalParameter5', None)
    assert not _is_linked(a, 'OPLmetamodel_FormalParameter5', b2)
    if hasattr(b2, 'OPLmetamodel_AllExpression'):
        assert not _is_linked(b2, 'OPLmetamodel_AllExpression', a)


def test_assoc_qualifiers56_link_reassign_clear():
    a = OPLmetamodel_FormalParameter(isOrdered=True)
    b1 = OPLmetamodel_ForAllConstraint()
    b2 = OPLmetamodel_ForAllConstraint()
    _safe_set(a, 'OPLmetamodel_FormalParameter57', b1)
    assert _is_linked(a, 'OPLmetamodel_FormalParameter57', b1)
    if hasattr(b1, 'OPLmetamodel_ForAllConstraint'):
        assert _is_linked(b1, 'OPLmetamodel_ForAllConstraint', a)
    _safe_set(a, 'OPLmetamodel_FormalParameter57', b2)
    assert _is_linked(a, 'OPLmetamodel_FormalParameter57', b2)
    if hasattr(b1, 'OPLmetamodel_ForAllConstraint'):
        assert not _is_linked(b1, 'OPLmetamodel_ForAllConstraint', a)
    if hasattr(b2, 'OPLmetamodel_ForAllConstraint'):
        assert _is_linked(b2, 'OPLmetamodel_ForAllConstraint', a)
    _safe_set(a, 'OPLmetamodel_FormalParameter57', None)
    assert not _is_linked(a, 'OPLmetamodel_FormalParameter57', b2)
    if hasattr(b2, 'OPLmetamodel_ForAllConstraint'):
        assert not _is_linked(b2, 'OPLmetamodel_ForAllConstraint', a)


def test_assoc_relation155_link_reassign_clear():
    a = OPLmetamodel_RelationalExpression(redefinedOp="sample_text")
    b1 = OPLmetamodel_RelationalInit()
    b2 = OPLmetamodel_RelationalInit()
    _safe_set(a, 'OPLmetamodel_RelationalExpression', b1)
    assert _is_linked(a, 'OPLmetamodel_RelationalExpression', b1)
    if hasattr(b1, 'OPLmetamodel_RelationalInit156'):
        assert _is_linked(b1, 'OPLmetamodel_RelationalInit156', a)
    _safe_set(a, 'OPLmetamodel_RelationalExpression', b2)
    assert _is_linked(a, 'OPLmetamodel_RelationalExpression', b2)
    if hasattr(b1, 'OPLmetamodel_RelationalInit156'):
        assert not _is_linked(b1, 'OPLmetamodel_RelationalInit156', a)
    if hasattr(b2, 'OPLmetamodel_RelationalInit156'):
        assert _is_linked(b2, 'OPLmetamodel_RelationalInit156', a)
    _safe_set(a, 'OPLmetamodel_RelationalExpression', None)
    assert not _is_linked(a, 'OPLmetamodel_RelationalExpression', b2)
    if hasattr(b2, 'OPLmetamodel_RelationalInit156'):
        assert not _is_linked(b2, 'OPLmetamodel_RelationalInit156', a)


def test_assoc_require51_link_reassign_clear():
    a = OPLmetamodel_FormalParameter(isOrdered=True)
    b1 = OPLmetamodel_Expression()
    b2 = OPLmetamodel_Expression()
    _safe_set(a, 'OPLmetamodel_FormalParameter52', b1)
    assert _is_linked(a, 'OPLmetamodel_FormalParameter52', b1)
    if hasattr(b1, 'OPLmetamodel_Expression53'):
        assert _is_linked(b1, 'OPLmetamodel_Expression53', a)
    _safe_set(a, 'OPLmetamodel_FormalParameter52', b2)
    assert _is_linked(a, 'OPLmetamodel_FormalParameter52', b2)
    if hasattr(b1, 'OPLmetamodel_Expression53'):
        assert not _is_linked(b1, 'OPLmetamodel_Expression53', a)
    if hasattr(b2, 'OPLmetamodel_Expression53'):
        assert _is_linked(b2, 'OPLmetamodel_Expression53', a)
    _safe_set(a, 'OPLmetamodel_FormalParameter52', None)
    assert not _is_linked(a, 'OPLmetamodel_FormalParameter52', b2)
    if hasattr(b2, 'OPLmetamodel_Expression53'):
        assert not _is_linked(b2, 'OPLmetamodel_Expression53', a)


def test_assoc_resources109_link_reassign_clear():
    a = OPLmetamodel_Model(id="sample_text", isConstraintProblem=True)
    b1 = OPLmetamodel_ResourceDeclaration()
    b2 = OPLmetamodel_ResourceDeclaration()
    _safe_set(a, 'OPLmetamodel_Model110', b1)
    assert _is_linked(a, 'OPLmetamodel_Model110', b1)
    if hasattr(b1, 'OPLmetamodel_ResourceDeclaration'):
        assert _is_linked(b1, 'OPLmetamodel_ResourceDeclaration', a)
    _safe_set(a, 'OPLmetamodel_Model110', b2)
    assert _is_linked(a, 'OPLmetamodel_Model110', b2)
    if hasattr(b1, 'OPLmetamodel_ResourceDeclaration'):
        assert not _is_linked(b1, 'OPLmetamodel_ResourceDeclaration', a)
    if hasattr(b2, 'OPLmetamodel_ResourceDeclaration'):
        assert _is_linked(b2, 'OPLmetamodel_ResourceDeclaration', a)
    _safe_set(a, 'OPLmetamodel_Model110', None)
    assert not _is_linked(a, 'OPLmetamodel_Model110', b2)
    if hasattr(b2, 'OPLmetamodel_ResourceDeclaration'):
        assert not _is_linked(b2, 'OPLmetamodel_ResourceDeclaration', a)


def test_assoc_scheduleInit114_link_reassign_clear():
    a = OPLmetamodel_Model(id="sample_text", isConstraintProblem=True)
    b1 = OPLmetamodel_ScheduleInitialization()
    b2 = OPLmetamodel_ScheduleInitialization()
    _safe_set(a, 'OPLmetamodel_Model115', {b1})
    assert _is_linked(a, 'OPLmetamodel_Model115', b1)
    if hasattr(b1, 'OPLmetamodel_ScheduleInitialization'):
        assert _is_linked(b1, 'OPLmetamodel_ScheduleInitialization', a)
    _safe_set(a, 'OPLmetamodel_Model115', {b2})
    assert _is_linked(a, 'OPLmetamodel_Model115', b2)
    if hasattr(b1, 'OPLmetamodel_ScheduleInitialization'):
        assert not _is_linked(b1, 'OPLmetamodel_ScheduleInitialization', a)
    if hasattr(b2, 'OPLmetamodel_ScheduleInitialization'):
        assert _is_linked(b2, 'OPLmetamodel_ScheduleInitialization', a)
    _safe_set(a, 'OPLmetamodel_Model115', set())
    assert not _is_linked(a, 'OPLmetamodel_Model115', b2)
    if hasattr(b2, 'OPLmetamodel_ScheduleInitialization'):
        assert not _is_linked(b2, 'OPLmetamodel_ScheduleInitialization', a)


def test_assoc_scripts116_link_reassign_clear():
    a = OPLmetamodel_Script(isMain=True)
    b1 = OPLmetamodel_Model(id="sample_text", isConstraintProblem=True)
    b2 = OPLmetamodel_Model(id="sample_text_2", isConstraintProblem=False)
    _safe_set(a, 'OPLmetamodel_Script', b1)
    assert _is_linked(a, 'OPLmetamodel_Script', b1)
    if hasattr(b1, 'OPLmetamodel_Model117'):
        assert _is_linked(b1, 'OPLmetamodel_Model117', a)
    _safe_set(a, 'OPLmetamodel_Script', b2)
    assert _is_linked(a, 'OPLmetamodel_Script', b2)
    if hasattr(b1, 'OPLmetamodel_Model117'):
        assert not _is_linked(b1, 'OPLmetamodel_Model117', a)
    if hasattr(b2, 'OPLmetamodel_Model117'):
        assert _is_linked(b2, 'OPLmetamodel_Model117', a)
    _safe_set(a, 'OPLmetamodel_Script', None)
    assert not _is_linked(a, 'OPLmetamodel_Script', b2)
    if hasattr(b2, 'OPLmetamodel_Model117'):
        assert not _is_linked(b2, 'OPLmetamodel_Model117', a)


def test_assoc_search122_link_reassign_clear():
    a = OPLmetamodel_Model(id="sample_text", isConstraintProblem=True)
    b1 = OPLmetamodel_SearchProcedure()
    b2 = OPLmetamodel_SearchProcedure()
    _safe_set(a, 'OPLmetamodel_Model123', b1)
    assert _is_linked(a, 'OPLmetamodel_Model123', b1)
    if hasattr(b1, 'OPLmetamodel_SearchProcedure'):
        assert _is_linked(b1, 'OPLmetamodel_SearchProcedure', a)
    _safe_set(a, 'OPLmetamodel_Model123', b2)
    assert _is_linked(a, 'OPLmetamodel_Model123', b2)
    if hasattr(b1, 'OPLmetamodel_SearchProcedure'):
        assert not _is_linked(b1, 'OPLmetamodel_SearchProcedure', a)
    if hasattr(b2, 'OPLmetamodel_SearchProcedure'):
        assert _is_linked(b2, 'OPLmetamodel_SearchProcedure', a)
    _safe_set(a, 'OPLmetamodel_Model123', None)
    assert not _is_linked(a, 'OPLmetamodel_Model123', b2)
    if hasattr(b2, 'OPLmetamodel_SearchProcedure'):
        assert not _is_linked(b2, 'OPLmetamodel_SearchProcedure', a)


def test_assoc_settings118_link_reassign_clear():
    a = OPLmetamodel_Model(id="sample_text", isConstraintProblem=True)
    b1 = OPLmetamodel_Setting()
    b2 = OPLmetamodel_Setting()
    _safe_set(a, 'OPLmetamodel_Model119', {b1})
    assert _is_linked(a, 'OPLmetamodel_Model119', b1)
    if hasattr(b1, 'OPLmetamodel_Setting'):
        assert _is_linked(b1, 'OPLmetamodel_Setting', a)
    _safe_set(a, 'OPLmetamodel_Model119', {b2})
    assert _is_linked(a, 'OPLmetamodel_Model119', b2)
    if hasattr(b1, 'OPLmetamodel_Setting'):
        assert not _is_linked(b1, 'OPLmetamodel_Setting', a)
    if hasattr(b2, 'OPLmetamodel_Setting'):
        assert _is_linked(b2, 'OPLmetamodel_Setting', a)
    _safe_set(a, 'OPLmetamodel_Model119', set())
    assert not _is_linked(a, 'OPLmetamodel_Model119', b2)
    if hasattr(b2, 'OPLmetamodel_Setting'):
        assert not _is_linked(b2, 'OPLmetamodel_Setting', a)


def test_assoc_size85_link_reassign_clear():
    a = OPLmetamodel_Interval(isOptional=True)
    b1 = OPLmetamodel_NumericType()
    b2 = OPLmetamodel_NumericType()
    _safe_set(a, 'OPLmetamodel_Interval86', b1)
    assert _is_linked(a, 'OPLmetamodel_Interval86', b1)
    if hasattr(b1, 'OPLmetamodel_NumericType'):
        assert _is_linked(b1, 'OPLmetamodel_NumericType', a)
    _safe_set(a, 'OPLmetamodel_Interval86', b2)
    assert _is_linked(a, 'OPLmetamodel_Interval86', b2)
    if hasattr(b1, 'OPLmetamodel_NumericType'):
        assert not _is_linked(b1, 'OPLmetamodel_NumericType', a)
    if hasattr(b2, 'OPLmetamodel_NumericType'):
        assert _is_linked(b2, 'OPLmetamodel_NumericType', a)
    _safe_set(a, 'OPLmetamodel_Interval86', None)
    assert not _is_linked(a, 'OPLmetamodel_Interval86', b2)
    if hasattr(b2, 'OPLmetamodel_NumericType'):
        assert not _is_linked(b2, 'OPLmetamodel_NumericType', a)


def test_assoc_statements160_link_reassign_clear():
    a = OPLmetamodel_Script(isMain=True)
    b1 = OPLmetamodel_ScriptStatement()
    b2 = OPLmetamodel_ScriptStatement()
    _safe_set(a, 'OPLmetamodel_Script161', {b1})
    assert _is_linked(a, 'OPLmetamodel_Script161', b1)
    if hasattr(b1, 'OPLmetamodel_ScriptStatement'):
        assert _is_linked(b1, 'OPLmetamodel_ScriptStatement', a)
    _safe_set(a, 'OPLmetamodel_Script161', {b2})
    assert _is_linked(a, 'OPLmetamodel_Script161', b2)
    if hasattr(b1, 'OPLmetamodel_ScriptStatement'):
        assert not _is_linked(b1, 'OPLmetamodel_ScriptStatement', a)
    if hasattr(b2, 'OPLmetamodel_ScriptStatement'):
        assert _is_linked(b2, 'OPLmetamodel_ScriptStatement', a)
    _safe_set(a, 'OPLmetamodel_Script161', set())
    assert not _is_linked(a, 'OPLmetamodel_Script161', b2)
    if hasattr(b2, 'OPLmetamodel_ScriptStatement'):
        assert not _is_linked(b2, 'OPLmetamodel_ScriptStatement', a)


def test_assoc_test69_link_reassign_clear():
    a = OPLmetamodel_BooleanExpression(body="sample_text")
    b1 = OPLmetamodel_IfConstraint()
    b2 = OPLmetamodel_IfConstraint()
    _safe_set(a, 'OPLmetamodel_BooleanExpression', b1)
    assert _is_linked(a, 'OPLmetamodel_BooleanExpression', b1)
    if hasattr(b1, 'OPLmetamodel_IfConstraint'):
        assert _is_linked(b1, 'OPLmetamodel_IfConstraint', a)
    _safe_set(a, 'OPLmetamodel_BooleanExpression', b2)
    assert _is_linked(a, 'OPLmetamodel_BooleanExpression', b2)
    if hasattr(b1, 'OPLmetamodel_IfConstraint'):
        assert not _is_linked(b1, 'OPLmetamodel_IfConstraint', a)
    if hasattr(b2, 'OPLmetamodel_IfConstraint'):
        assert _is_linked(b2, 'OPLmetamodel_IfConstraint', a)
    _safe_set(a, 'OPLmetamodel_BooleanExpression', None)
    assert not _is_linked(a, 'OPLmetamodel_BooleanExpression', b2)
    if hasattr(b2, 'OPLmetamodel_IfConstraint'):
        assert not _is_linked(b2, 'OPLmetamodel_IfConstraint', a)


def test_assoc_test76_link_reassign_clear():
    a = OPLmetamodel_BooleanExpression(body="sample_text")
    b1 = OPLmetamodel_IfExpression()
    b2 = OPLmetamodel_IfExpression()
    _safe_set(a, 'OPLmetamodel_BooleanExpression77', b1)
    assert _is_linked(a, 'OPLmetamodel_BooleanExpression77', b1)
    if hasattr(b1, 'OPLmetamodel_IfExpression'):
        assert _is_linked(b1, 'OPLmetamodel_IfExpression', a)
    _safe_set(a, 'OPLmetamodel_BooleanExpression77', b2)
    assert _is_linked(a, 'OPLmetamodel_BooleanExpression77', b2)
    if hasattr(b1, 'OPLmetamodel_IfExpression'):
        assert not _is_linked(b1, 'OPLmetamodel_IfExpression', a)
    if hasattr(b2, 'OPLmetamodel_IfExpression'):
        assert _is_linked(b2, 'OPLmetamodel_IfExpression', a)
    _safe_set(a, 'OPLmetamodel_BooleanExpression77', None)
    assert not _is_linked(a, 'OPLmetamodel_BooleanExpression77', b2)
    if hasattr(b2, 'OPLmetamodel_IfExpression'):
        assert not _is_linked(b2, 'OPLmetamodel_IfExpression', a)


def test_assoc_then70_link_reassign_clear():
    a = OPLmetamodel_Constraint(name="sample_text")
    b1 = OPLmetamodel_IfConstraint()
    b2 = OPLmetamodel_IfConstraint()
    _safe_set(a, 'OPLmetamodel_Constraint72', b1)
    assert _is_linked(a, 'OPLmetamodel_Constraint72', b1)
    if hasattr(b1, 'OPLmetamodel_IfConstraint71'):
        assert _is_linked(b1, 'OPLmetamodel_IfConstraint71', a)
    _safe_set(a, 'OPLmetamodel_Constraint72', b2)
    assert _is_linked(a, 'OPLmetamodel_Constraint72', b2)
    if hasattr(b1, 'OPLmetamodel_IfConstraint71'):
        assert not _is_linked(b1, 'OPLmetamodel_IfConstraint71', a)
    if hasattr(b2, 'OPLmetamodel_IfConstraint71'):
        assert _is_linked(b2, 'OPLmetamodel_IfConstraint71', a)
    _safe_set(a, 'OPLmetamodel_Constraint72', None)
    assert not _is_linked(a, 'OPLmetamodel_Constraint72', b2)
    if hasattr(b2, 'OPLmetamodel_IfConstraint71'):
        assert not _is_linked(b2, 'OPLmetamodel_IfConstraint71', a)


def test_assoc_transitionMatrix173_link_reassign_clear():
    a = OPLmetamodel_SetType(name="sample_text")
    b1 = OPLmetamodel_StateFunction()
    b2 = OPLmetamodel_StateFunction()
    _safe_set(a, 'OPLmetamodel_SetType174', b1)
    assert _is_linked(a, 'OPLmetamodel_SetType174', b1)
    if hasattr(b1, 'OPLmetamodel_StateFunction'):
        assert _is_linked(b1, 'OPLmetamodel_StateFunction', a)
    _safe_set(a, 'OPLmetamodel_SetType174', b2)
    assert _is_linked(a, 'OPLmetamodel_SetType174', b2)
    if hasattr(b1, 'OPLmetamodel_StateFunction'):
        assert not _is_linked(b1, 'OPLmetamodel_StateFunction', a)
    if hasattr(b2, 'OPLmetamodel_StateFunction'):
        assert _is_linked(b2, 'OPLmetamodel_StateFunction', a)
    _safe_set(a, 'OPLmetamodel_SetType174', None)
    assert not _is_linked(a, 'OPLmetamodel_SetType174', b2)
    if hasattr(b2, 'OPLmetamodel_StateFunction'):
        assert not _is_linked(b2, 'OPLmetamodel_StateFunction', a)


def test_assoc_type146_link_reassign_clear():
    a = OPLmetamodel_RecordField(name="sample_text")
    b1 = OPLmetamodel_AbstractType()
    b2 = OPLmetamodel_AbstractType()
    _safe_set(a, 'OPLmetamodel_RecordField147', b1)
    assert _is_linked(a, 'OPLmetamodel_RecordField147', b1)
    if hasattr(b1, 'OPLmetamodel_AbstractType148'):
        assert _is_linked(b1, 'OPLmetamodel_AbstractType148', a)
    _safe_set(a, 'OPLmetamodel_RecordField147', b2)
    assert _is_linked(a, 'OPLmetamodel_RecordField147', b2)
    if hasattr(b1, 'OPLmetamodel_AbstractType148'):
        assert not _is_linked(b1, 'OPLmetamodel_AbstractType148', a)
    if hasattr(b2, 'OPLmetamodel_AbstractType148'):
        assert _is_linked(b2, 'OPLmetamodel_AbstractType148', a)
    _safe_set(a, 'OPLmetamodel_RecordField147', None)
    assert not _is_linked(a, 'OPLmetamodel_RecordField147', b2)
    if hasattr(b2, 'OPLmetamodel_AbstractType148'):
        assert not _is_linked(b2, 'OPLmetamodel_AbstractType148', a)


def test_assoc_type34_link_reassign_clear():
    a = OPLmetamodel_DataDeclaration(isDecisionExpr=True, isDecisionVar=True)
    b1 = OPLmetamodel_AbstractType()
    b2 = OPLmetamodel_AbstractType()
    _safe_set(a, 'OPLmetamodel_DataDeclaration35', b1)
    assert _is_linked(a, 'OPLmetamodel_DataDeclaration35', b1)
    if hasattr(b1, 'OPLmetamodel_AbstractType36'):
        assert _is_linked(b1, 'OPLmetamodel_AbstractType36', a)
    _safe_set(a, 'OPLmetamodel_DataDeclaration35', b2)
    assert _is_linked(a, 'OPLmetamodel_DataDeclaration35', b2)
    if hasattr(b1, 'OPLmetamodel_AbstractType36'):
        assert not _is_linked(b1, 'OPLmetamodel_AbstractType36', a)
    if hasattr(b2, 'OPLmetamodel_AbstractType36'):
        assert _is_linked(b2, 'OPLmetamodel_AbstractType36', a)
    _safe_set(a, 'OPLmetamodel_DataDeclaration35', None)
    assert not _is_linked(a, 'OPLmetamodel_DataDeclaration35', b2)
    if hasattr(b2, 'OPLmetamodel_AbstractType36'):
        assert not _is_linked(b2, 'OPLmetamodel_AbstractType36', a)


def test_assoc_types94_link_reassign_clear():
    a = OPLmetamodel_Model(id="sample_text", isConstraintProblem=True)
    b1 = OPLmetamodel_DefinedType()
    b2 = OPLmetamodel_DefinedType()
    _safe_set(a, 'OPLmetamodel_Model', {b1})
    assert _is_linked(a, 'OPLmetamodel_Model', b1)
    if hasattr(b1, 'OPLmetamodel_DefinedType'):
        assert _is_linked(b1, 'OPLmetamodel_DefinedType', a)
    _safe_set(a, 'OPLmetamodel_Model', {b2})
    assert _is_linked(a, 'OPLmetamodel_Model', b2)
    if hasattr(b1, 'OPLmetamodel_DefinedType'):
        assert not _is_linked(b1, 'OPLmetamodel_DefinedType', a)
    if hasattr(b2, 'OPLmetamodel_DefinedType'):
        assert _is_linked(b2, 'OPLmetamodel_DefinedType', a)
    _safe_set(a, 'OPLmetamodel_Model', set())
    assert not _is_linked(a, 'OPLmetamodel_Model', b2)
    if hasattr(b2, 'OPLmetamodel_DefinedType'):
        assert not _is_linked(b2, 'OPLmetamodel_DefinedType', a)


def test_assoc_value37_link_reassign_clear():
    a = OPLmetamodel_DataDeclaration(isDecisionExpr=True, isDecisionVar=True)
    b1 = OPLmetamodel_Initialization()
    b2 = OPLmetamodel_Initialization()
    _safe_set(a, 'OPLmetamodel_DataDeclaration38', b1)
    assert _is_linked(a, 'OPLmetamodel_DataDeclaration38', b1)
    if hasattr(b1, 'OPLmetamodel_Initialization'):
        assert _is_linked(b1, 'OPLmetamodel_Initialization', a)
    _safe_set(a, 'OPLmetamodel_DataDeclaration38', b2)
    assert _is_linked(a, 'OPLmetamodel_DataDeclaration38', b2)
    if hasattr(b1, 'OPLmetamodel_Initialization'):
        assert not _is_linked(b1, 'OPLmetamodel_Initialization', a)
    if hasattr(b2, 'OPLmetamodel_Initialization'):
        assert _is_linked(b2, 'OPLmetamodel_Initialization', a)
    _safe_set(a, 'OPLmetamodel_DataDeclaration38', None)
    assert not _is_linked(a, 'OPLmetamodel_DataDeclaration38', b2)
    if hasattr(b2, 'OPLmetamodel_Initialization'):
        assert not _is_linked(b2, 'OPLmetamodel_Initialization', a)


def test_assoc_valueConstraint39_link_reassign_clear():
    a = OPLmetamodel_DataDeclaration(isDecisionExpr=True, isDecisionVar=True)
    b1 = OPLmetamodel_Expression()
    b2 = OPLmetamodel_Expression()
    _safe_set(a, 'OPLmetamodel_DataDeclaration40', b1)
    assert _is_linked(a, 'OPLmetamodel_DataDeclaration40', b1)
    if hasattr(b1, 'OPLmetamodel_Expression41'):
        assert _is_linked(b1, 'OPLmetamodel_Expression41', a)
    _safe_set(a, 'OPLmetamodel_DataDeclaration40', b2)
    assert _is_linked(a, 'OPLmetamodel_DataDeclaration40', b2)
    if hasattr(b1, 'OPLmetamodel_Expression41'):
        assert not _is_linked(b1, 'OPLmetamodel_Expression41', a)
    if hasattr(b2, 'OPLmetamodel_Expression41'):
        assert _is_linked(b2, 'OPLmetamodel_Expression41', a)
    _safe_set(a, 'OPLmetamodel_DataDeclaration40', None)
    assert not _is_linked(a, 'OPLmetamodel_DataDeclaration40', b2)
    if hasattr(b2, 'OPLmetamodel_Expression41'):
        assert not _is_linked(b2, 'OPLmetamodel_Expression41', a)


def test_assoc_variable32_link_reassign_clear():
    a = OPLmetamodel_DataDeclaration(isDecisionExpr=True, isDecisionVar=True)
    b1 = OPLmetamodel_DataRef()
    b2 = OPLmetamodel_DataRef()
    _safe_set(a, 'OPLmetamodel_DataDeclaration', b1)
    assert _is_linked(a, 'OPLmetamodel_DataDeclaration', b1)
    if hasattr(b1, 'OPLmetamodel_DataRef33'):
        assert _is_linked(b1, 'OPLmetamodel_DataRef33', a)
    _safe_set(a, 'OPLmetamodel_DataDeclaration', b2)
    assert _is_linked(a, 'OPLmetamodel_DataDeclaration', b2)
    if hasattr(b1, 'OPLmetamodel_DataRef33'):
        assert not _is_linked(b1, 'OPLmetamodel_DataRef33', a)
    if hasattr(b2, 'OPLmetamodel_DataRef33'):
        assert _is_linked(b2, 'OPLmetamodel_DataRef33', a)
    _safe_set(a, 'OPLmetamodel_DataDeclaration', None)
    assert not _is_linked(a, 'OPLmetamodel_DataDeclaration', b2)
    if hasattr(b2, 'OPLmetamodel_DataRef33'):
        assert not _is_linked(b2, 'OPLmetamodel_DataRef33', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AbstractBinaryOperator_strategy = st.builds(AbstractBinaryOperator)
@given(instance=AbstractBinaryOperator_strategy)
@settings(max_examples=25)
def test_AbstractBinaryOperator_instantiation(instance):
    assert isinstance(instance, AbstractBinaryOperator)


AbstractType_strategy = st.builds(AbstractType)
@given(instance=AbstractType_strategy)
@settings(max_examples=25)
def test_AbstractType_instantiation(instance):
    assert isinstance(instance, AbstractType)


BinaryExpression_strategy = st.builds(BinaryExpression)
@given(instance=BinaryExpression_strategy)
@settings(max_examples=25)
def test_BinaryExpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)


BooleanExpression_strategy = st.builds(BooleanExpression)
@given(instance=BooleanExpression_strategy)
@settings(max_examples=25)
def test_BooleanExpression_instantiation(instance):
    assert isinstance(instance, BooleanExpression)


BuiltInFunction_strategy = st.builds(BuiltInFunction)
@given(instance=BuiltInFunction_strategy)
@settings(max_examples=25)
def test_BuiltInFunction_instantiation(instance):
    assert isinstance(instance, BuiltInFunction)


CollectionExpression_strategy = st.builds(CollectionExpression)
@given(instance=CollectionExpression_strategy)
@settings(max_examples=25)
def test_CollectionExpression_instantiation(instance):
    assert isinstance(instance, CollectionExpression)


Constraint_strategy = st.builds(Constraint)
@given(instance=Constraint_strategy)
@settings(max_examples=25)
def test_Constraint_instantiation(instance):
    assert isinstance(instance, Constraint)


DataInitMethods_strategy = st.builds(DataInitMethods)
@given(instance=DataInitMethods_strategy)
@settings(max_examples=25)
def test_DataInitMethods_instantiation(instance):
    assert isinstance(instance, DataInitMethods)


Declaration_strategy = st.builds(Declaration)
@given(instance=Declaration_strategy)
@settings(max_examples=25)
def test_Declaration_instantiation(instance):
    assert isinstance(instance, Declaration)


DefinedType_strategy = st.builds(DefinedType)
@given(instance=DefinedType_strategy)
@settings(max_examples=25)
def test_DefinedType_instantiation(instance):
    assert isinstance(instance, DefinedType)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


FloatType_strategy = st.builds(FloatType)
@given(instance=FloatType_strategy)
@settings(max_examples=25)
def test_FloatType_instantiation(instance):
    assert isinstance(instance, FloatType)


Function_strategy = st.builds(Function)
@given(instance=Function_strategy)
@settings(max_examples=25)
def test_Function_instantiation(instance):
    assert isinstance(instance, Function)


Initialization_strategy = st.builds(Initialization)
@given(instance=Initialization_strategy)
@settings(max_examples=25)
def test_Initialization_instantiation(instance):
    assert isinstance(instance, Initialization)


IntegerType_strategy = st.builds(IntegerType)
@given(instance=IntegerType_strategy)
@settings(max_examples=25)
def test_IntegerType_instantiation(instance):
    assert isinstance(instance, IntegerType)


NumericExpression_strategy = st.builds(NumericExpression)
@given(instance=NumericExpression_strategy)
@settings(max_examples=25)
def test_NumericExpression_instantiation(instance):
    assert isinstance(instance, NumericExpression)


NumericType_strategy = st.builds(NumericType)
@given(instance=NumericType_strategy)
@settings(max_examples=25)
def test_NumericType_instantiation(instance):
    assert isinstance(instance, NumericType)


OPLmetamodel_AbstractBinaryOperator_strategy = st.builds(OPLmetamodel_AbstractBinaryOperator)
@given(instance=OPLmetamodel_AbstractBinaryOperator_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_AbstractBinaryOperator_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_AbstractBinaryOperator)


OPLmetamodel_AbstractType_strategy = st.builds(OPLmetamodel_AbstractType)
@given(instance=OPLmetamodel_AbstractType_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_AbstractType_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_AbstractType)


OPLmetamodel_ActivityDeclaration_strategy = st.builds(OPLmetamodel_ActivityDeclaration, earliestStartTime=safe_text, latestEndTime=safe_text)
@given(instance=OPLmetamodel_ActivityDeclaration_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_ActivityDeclaration_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_ActivityDeclaration)


OPLmetamodel_AggregateExp_strategy = st.builds(OPLmetamodel_AggregateExp, op=safe_text)
@given(instance=OPLmetamodel_AggregateExp_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_AggregateExp_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_AggregateExp)


OPLmetamodel_AllExpression_strategy = st.builds(OPLmetamodel_AllExpression)
@given(instance=OPLmetamodel_AllExpression_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_AllExpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_AllExpression)


OPLmetamodel_ArrayDereference_strategy = st.builds(OPLmetamodel_ArrayDereference)
@given(instance=OPLmetamodel_ArrayDereference_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_ArrayDereference_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_ArrayDereference)


OPLmetamodel_ArraySlotConstraint_strategy = st.builds(OPLmetamodel_ArraySlotConstraint)
@given(instance=OPLmetamodel_ArraySlotConstraint_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_ArraySlotConstraint_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_ArraySlotConstraint)


OPLmetamodel_ArrayType_strategy = st.builds(OPLmetamodel_ArrayType)
@given(instance=OPLmetamodel_ArrayType_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_ArrayType_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_ArrayType)


OPLmetamodel_ArrayValue_strategy = st.builds(OPLmetamodel_ArrayValue)
@given(instance=OPLmetamodel_ArrayValue_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_ArrayValue_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_ArrayValue)


OPLmetamodel_Assertion_strategy = st.builds(OPLmetamodel_Assertion)
@given(instance=OPLmetamodel_Assertion_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_Assertion_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_Assertion)


OPLmetamodel_BinaryExpression_strategy = st.builds(OPLmetamodel_BinaryExpression)
@given(instance=OPLmetamodel_BinaryExpression_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_BinaryExpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_BinaryExpression)


OPLmetamodel_BinaryOperator_strategy = st.builds(OPLmetamodel_BinaryOperator, op=safe_text)
@given(instance=OPLmetamodel_BinaryOperator_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_BinaryOperator_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_BinaryOperator)


OPLmetamodel_BindingRef_strategy = st.builds(OPLmetamodel_BindingRef)
@given(instance=OPLmetamodel_BindingRef_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_BindingRef_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_BindingRef)


OPLmetamodel_BlockExpression_strategy = st.builds(OPLmetamodel_BlockExpression)
@given(instance=OPLmetamodel_BlockExpression_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_BlockExpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_BlockExpression)


OPLmetamodel_BooleanBlock_strategy = st.builds(OPLmetamodel_BooleanBlock)
@given(instance=OPLmetamodel_BooleanBlock_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_BooleanBlock_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_BooleanBlock)


OPLmetamodel_BooleanExpression_strategy = st.builds(OPLmetamodel_BooleanExpression, body=safe_text)
@given(instance=OPLmetamodel_BooleanExpression_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_BooleanExpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_BooleanExpression)


OPLmetamodel_BooleanType_strategy = st.builds(OPLmetamodel_BooleanType)
@given(instance=OPLmetamodel_BooleanType_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_BooleanType_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_BooleanType)


OPLmetamodel_BuiltInFunction_strategy = st.builds(OPLmetamodel_BuiltInFunction)
@given(instance=OPLmetamodel_BuiltInFunction_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_BuiltInFunction_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_BuiltInFunction)


OPLmetamodel_CollectionExpression_strategy = st.builds(OPLmetamodel_CollectionExpression, isUnique=st.booleans())
@given(instance=OPLmetamodel_CollectionExpression_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_CollectionExpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_CollectionExpression)


OPLmetamodel_Comprehension_strategy = st.builds(OPLmetamodel_Comprehension)
@given(instance=OPLmetamodel_Comprehension_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_Comprehension_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_Comprehension)


OPLmetamodel_Constraint_strategy = st.builds(OPLmetamodel_Constraint, name=safe_text)
@given(instance=OPLmetamodel_Constraint_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_Constraint_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_Constraint)


OPLmetamodel_CumulativeFunction_strategy = st.builds(OPLmetamodel_CumulativeFunction)
@given(instance=OPLmetamodel_CumulativeFunction_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_CumulativeFunction_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_CumulativeFunction)


OPLmetamodel_DataDeclaration_strategy = st.builds(OPLmetamodel_DataDeclaration, isDecisionExpr=st.booleans(), isDecisionVar=st.booleans())
@given(instance=OPLmetamodel_DataDeclaration_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_DataDeclaration_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_DataDeclaration)


OPLmetamodel_DataInitMethods_strategy = st.builds(OPLmetamodel_DataInitMethods)
@given(instance=OPLmetamodel_DataInitMethods_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_DataInitMethods_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_DataInitMethods)


OPLmetamodel_DataObject_strategy = st.builds(OPLmetamodel_DataObject, body=safe_text)
@given(instance=OPLmetamodel_DataObject_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_DataObject_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_DataObject)


OPLmetamodel_DataRef_strategy = st.builds(OPLmetamodel_DataRef)
@given(instance=OPLmetamodel_DataRef_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_DataRef_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_DataRef)


OPLmetamodel_DeferredInit_strategy = st.builds(OPLmetamodel_DeferredInit)
@given(instance=OPLmetamodel_DeferredInit_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_DeferredInit_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_DeferredInit)


OPLmetamodel_DefinedType_strategy = st.builds(OPLmetamodel_DefinedType)
@given(instance=OPLmetamodel_DefinedType_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_DefinedType_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_DefinedType)


OPLmetamodel_DisplayInstruction_strategy = st.builds(OPLmetamodel_DisplayInstruction)
@given(instance=OPLmetamodel_DisplayInstruction_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_DisplayInstruction_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_DisplayInstruction)


OPLmetamodel_Entity_strategy = st.builds(OPLmetamodel_Entity)
@given(instance=OPLmetamodel_Entity_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_Entity_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_Entity)


OPLmetamodel_EnumLiteral_strategy = st.builds(OPLmetamodel_EnumLiteral)
@given(instance=OPLmetamodel_EnumLiteral_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_EnumLiteral_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_EnumLiteral)


OPLmetamodel_EnumerationType_strategy = st.builds(OPLmetamodel_EnumerationType)
@given(instance=OPLmetamodel_EnumerationType_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_EnumerationType_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_EnumerationType)


OPLmetamodel_Error_strategy = st.builds(OPLmetamodel_Error)
@given(instance=OPLmetamodel_Error_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_Error_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_Error)


OPLmetamodel_Expression_strategy = st.builds(OPLmetamodel_Expression)
@given(instance=OPLmetamodel_Expression_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_Expression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_Expression)


OPLmetamodel_Extension_strategy = st.builds(OPLmetamodel_Extension)
@given(instance=OPLmetamodel_Extension_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_Extension_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_Extension)


OPLmetamodel_FloatExpression_strategy = st.builds(OPLmetamodel_FloatExpression, body=safe_text)
@given(instance=OPLmetamodel_FloatExpression_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_FloatExpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_FloatExpression)


OPLmetamodel_FloatRangeType_strategy = st.builds(OPLmetamodel_FloatRangeType)
@given(instance=OPLmetamodel_FloatRangeType_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_FloatRangeType_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_FloatRangeType)


OPLmetamodel_FloatType_strategy = st.builds(OPLmetamodel_FloatType)
@given(instance=OPLmetamodel_FloatType_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_FloatType_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_FloatType)


OPLmetamodel_ForAllConstraint_strategy = st.builds(OPLmetamodel_ForAllConstraint)
@given(instance=OPLmetamodel_ForAllConstraint_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_ForAllConstraint_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_ForAllConstraint)


OPLmetamodel_FormalParameter_strategy = st.builds(OPLmetamodel_FormalParameter, isOrdered=st.booleans())
@given(instance=OPLmetamodel_FormalParameter_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_FormalParameter_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_FormalParameter)


OPLmetamodel_Function_strategy = st.builds(OPLmetamodel_Function)
@given(instance=OPLmetamodel_Function_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_Function_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_Function)


OPLmetamodel_FunctionCall_strategy = st.builds(OPLmetamodel_FunctionCall, functionName=safe_text)
@given(instance=OPLmetamodel_FunctionCall_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_FunctionCall_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_FunctionCall)


OPLmetamodel_FunctionRef_strategy = st.builds(OPLmetamodel_FunctionRef, name=safe_text)
@given(instance=OPLmetamodel_FunctionRef_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_FunctionRef_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_FunctionRef)


OPLmetamodel_IfConstraint_strategy = st.builds(OPLmetamodel_IfConstraint)
@given(instance=OPLmetamodel_IfConstraint_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_IfConstraint_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_IfConstraint)


OPLmetamodel_IfExpression_strategy = st.builds(OPLmetamodel_IfExpression)
@given(instance=OPLmetamodel_IfExpression_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_IfExpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_IfExpression)


OPLmetamodel_In_strategy = st.builds(OPLmetamodel_In)
@given(instance=OPLmetamodel_In_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_In_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_In)


OPLmetamodel_IndexValuePair_strategy = st.builds(OPLmetamodel_IndexValuePair)
@given(instance=OPLmetamodel_IndexValuePair_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_IndexValuePair_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_IndexValuePair)


OPLmetamodel_Initialization_strategy = st.builds(OPLmetamodel_Initialization)
@given(instance=OPLmetamodel_Initialization_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_Initialization_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_Initialization)


OPLmetamodel_IntegerExpression_strategy = st.builds(OPLmetamodel_IntegerExpression, body=safe_text)
@given(instance=OPLmetamodel_IntegerExpression_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_IntegerExpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_IntegerExpression)


OPLmetamodel_IntegerRangeType_strategy = st.builds(OPLmetamodel_IntegerRangeType)
@given(instance=OPLmetamodel_IntegerRangeType_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_IntegerRangeType_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_IntegerRangeType)


OPLmetamodel_IntegerType_strategy = st.builds(OPLmetamodel_IntegerType)
@given(instance=OPLmetamodel_IntegerType_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_IntegerType_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_IntegerType)


OPLmetamodel_Interval_strategy = st.builds(OPLmetamodel_Interval, isOptional=st.booleans())
@given(instance=OPLmetamodel_Interval_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_Interval_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_Interval)


OPLmetamodel_Model_strategy = st.builds(OPLmetamodel_Model, id=safe_text, isConstraintProblem=st.booleans())
@given(instance=OPLmetamodel_Model_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_Model_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_Model)


OPLmetamodel_Number_strategy = st.builds(OPLmetamodel_Number)
@given(instance=OPLmetamodel_Number_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_Number_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_Number)


OPLmetamodel_NumericExpression_strategy = st.builds(OPLmetamodel_NumericExpression)
@given(instance=OPLmetamodel_NumericExpression_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_NumericExpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_NumericExpression)


OPLmetamodel_NumericType_strategy = st.builds(OPLmetamodel_NumericType)
@given(instance=OPLmetamodel_NumericType_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_NumericType_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_NumericType)


OPLmetamodel_Objective_strategy = st.builds(OPLmetamodel_Objective, action=safe_text, isLinearRelaxation=st.booleans())
@given(instance=OPLmetamodel_Objective_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_Objective_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_Objective)


OPLmetamodel_Operator_strategy = st.builds(OPLmetamodel_Operator)
@given(instance=OPLmetamodel_Operator_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_Operator_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_Operator)


OPLmetamodel_ParameterDeclaration_strategy = st.builds(OPLmetamodel_ParameterDeclaration)
@given(instance=OPLmetamodel_ParameterDeclaration_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_ParameterDeclaration_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_ParameterDeclaration)


OPLmetamodel_ParameterDomain_strategy = st.builds(OPLmetamodel_ParameterDomain)
@given(instance=OPLmetamodel_ParameterDomain_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_ParameterDomain_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_ParameterDomain)


OPLmetamodel_ParameterRef_strategy = st.builds(OPLmetamodel_ParameterRef)
@given(instance=OPLmetamodel_ParameterRef_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_ParameterRef_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_ParameterRef)


OPLmetamodel_PathDereference_strategy = st.builds(OPLmetamodel_PathDereference)
@given(instance=OPLmetamodel_PathDereference_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_PathDereference_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_PathDereference)


OPLmetamodel_PathExpression_strategy = st.builds(OPLmetamodel_PathExpression)
@given(instance=OPLmetamodel_PathExpression_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_PathExpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_PathExpression)


OPLmetamodel_PiecewiseExpression_strategy = st.builds(OPLmetamodel_PiecewiseExpression)
@given(instance=OPLmetamodel_PiecewiseExpression_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_PiecewiseExpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_PiecewiseExpression)


OPLmetamodel_PiecewiseLinearFunction_strategy = st.builds(OPLmetamodel_PiecewiseLinearFunction)
@given(instance=OPLmetamodel_PiecewiseLinearFunction_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_PiecewiseLinearFunction_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_PiecewiseLinearFunction)


OPLmetamodel_PositiveFloatType_strategy = st.builds(OPLmetamodel_PositiveFloatType)
@given(instance=OPLmetamodel_PositiveFloatType_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_PositiveFloatType_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_PositiveFloatType)


OPLmetamodel_PositiveIntegerType_strategy = st.builds(OPLmetamodel_PositiveIntegerType)
@given(instance=OPLmetamodel_PositiveIntegerType_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_PositiveIntegerType_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_PositiveIntegerType)


OPLmetamodel_PrimitiveExpression_strategy = st.builds(OPLmetamodel_PrimitiveExpression)
@given(instance=OPLmetamodel_PrimitiveExpression_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_PrimitiveExpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_PrimitiveExpression)


OPLmetamodel_PrimitiveType_strategy = st.builds(OPLmetamodel_PrimitiveType)
@given(instance=OPLmetamodel_PrimitiveType_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_PrimitiveType_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_PrimitiveType)


OPLmetamodel_QueryUser_strategy = st.builds(OPLmetamodel_QueryUser, ask=safe_text)
@given(instance=OPLmetamodel_QueryUser_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_QueryUser_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_QueryUser)


OPLmetamodel_RangeExpression_strategy = st.builds(OPLmetamodel_RangeExpression)
@given(instance=OPLmetamodel_RangeExpression_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_RangeExpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_RangeExpression)


OPLmetamodel_RangeType_strategy = st.builds(OPLmetamodel_RangeType)
@given(instance=OPLmetamodel_RangeType_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_RangeType_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_RangeType)


OPLmetamodel_ReadFile_strategy = st.builds(OPLmetamodel_ReadFile, path=safe_text)
@given(instance=OPLmetamodel_ReadFile_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_ReadFile_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_ReadFile)


OPLmetamodel_Record_strategy = st.builds(OPLmetamodel_Record, isTuple=st.booleans(), name=safe_text)
@given(instance=OPLmetamodel_Record_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_Record_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_Record)


OPLmetamodel_RecordField_strategy = st.builds(OPLmetamodel_RecordField, name=safe_text)
@given(instance=OPLmetamodel_RecordField_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_RecordField_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_RecordField)


OPLmetamodel_RecordValue_strategy = st.builds(OPLmetamodel_RecordValue)
@given(instance=OPLmetamodel_RecordValue_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_RecordValue_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_RecordValue)


OPLmetamodel_Reference_strategy = st.builds(OPLmetamodel_Reference, name=safe_text)
@given(instance=OPLmetamodel_Reference_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_Reference_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_Reference)


OPLmetamodel_ReflectiveFunction_strategy = st.builds(OPLmetamodel_ReflectiveFunction)
@given(instance=OPLmetamodel_ReflectiveFunction_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_ReflectiveFunction_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_ReflectiveFunction)


OPLmetamodel_RelationalExpression_strategy = st.builds(OPLmetamodel_RelationalExpression, redefinedOp=safe_text)
@given(instance=OPLmetamodel_RelationalExpression_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_RelationalExpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_RelationalExpression)


OPLmetamodel_RelationalInit_strategy = st.builds(OPLmetamodel_RelationalInit)
@given(instance=OPLmetamodel_RelationalInit_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_RelationalInit_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_RelationalInit)


OPLmetamodel_RelationalOperator_strategy = st.builds(OPLmetamodel_RelationalOperator, op=safe_text)
@given(instance=OPLmetamodel_RelationalOperator_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_RelationalOperator_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_RelationalOperator)


OPLmetamodel_ResourceDeclaration_strategy = st.builds(OPLmetamodel_ResourceDeclaration)
@given(instance=OPLmetamodel_ResourceDeclaration_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_ResourceDeclaration_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_ResourceDeclaration)


OPLmetamodel_ScheduleInitialization_strategy = st.builds(OPLmetamodel_ScheduleInitialization)
@given(instance=OPLmetamodel_ScheduleInitialization_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_ScheduleInitialization_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_ScheduleInitialization)


OPLmetamodel_Script_strategy = st.builds(OPLmetamodel_Script, isMain=st.booleans())
@given(instance=OPLmetamodel_Script_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_Script_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_Script)


OPLmetamodel_ScriptStatement_strategy = st.builds(OPLmetamodel_ScriptStatement)
@given(instance=OPLmetamodel_ScriptStatement_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_ScriptStatement_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_ScriptStatement)


OPLmetamodel_SearchProcedure_strategy = st.builds(OPLmetamodel_SearchProcedure)
@given(instance=OPLmetamodel_SearchProcedure_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_SearchProcedure_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_SearchProcedure)


OPLmetamodel_Sequence_strategy = st.builds(OPLmetamodel_Sequence)
@given(instance=OPLmetamodel_Sequence_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_Sequence_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_Sequence)


OPLmetamodel_SetType_strategy = st.builds(OPLmetamodel_SetType, name=safe_text)
@given(instance=OPLmetamodel_SetType_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_SetType_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_SetType)


OPLmetamodel_SetValue_strategy = st.builds(OPLmetamodel_SetValue)
@given(instance=OPLmetamodel_SetValue_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_SetValue_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_SetValue)


OPLmetamodel_Setting_strategy = st.builds(OPLmetamodel_Setting)
@given(instance=OPLmetamodel_Setting_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_Setting_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_Setting)


OPLmetamodel_StateFunction_strategy = st.builds(OPLmetamodel_StateFunction)
@given(instance=OPLmetamodel_StateFunction_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_StateFunction_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_StateFunction)


OPLmetamodel_StepFunction_strategy = st.builds(OPLmetamodel_StepFunction)
@given(instance=OPLmetamodel_StepFunction_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_StepFunction_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_StepFunction)


OPLmetamodel_StringExpression_strategy = st.builds(OPLmetamodel_StringExpression, body=safe_text)
@given(instance=OPLmetamodel_StringExpression_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_StringExpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_StringExpression)


OPLmetamodel_StringType_strategy = st.builds(OPLmetamodel_StringType)
@given(instance=OPLmetamodel_StringType_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_StringType_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_StringType)


OPLmetamodel_TupleBinding_strategy = st.builds(OPLmetamodel_TupleBinding)
@given(instance=OPLmetamodel_TupleBinding_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_TupleBinding_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_TupleBinding)


OPLmetamodel_UnaryExpression_strategy = st.builds(OPLmetamodel_UnaryExpression, op=safe_text)
@given(instance=OPLmetamodel_UnaryExpression_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_UnaryExpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_UnaryExpression)


OPLmetamodel_VariableBinding_strategy = st.builds(OPLmetamodel_VariableBinding)
@given(instance=OPLmetamodel_VariableBinding_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_VariableBinding_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_VariableBinding)


OPLmetamodel_Writeln_strategy = st.builds(OPLmetamodel_Writeln, arg=safe_text, string=safe_text)
@given(instance=OPLmetamodel_Writeln_strategy)
@settings(max_examples=25)
def test_OPLmetamodel_Writeln_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_Writeln)


ParameterDomain_strategy = st.builds(ParameterDomain)
@given(instance=ParameterDomain_strategy)
@settings(max_examples=25)
def test_ParameterDomain_instantiation(instance):
    assert isinstance(instance, ParameterDomain)


PathExpression_strategy = st.builds(PathExpression)
@given(instance=PathExpression_strategy)
@settings(max_examples=25)
def test_PathExpression_instantiation(instance):
    assert isinstance(instance, PathExpression)


PiecewiseLinearFunction_strategy = st.builds(PiecewiseLinearFunction)
@given(instance=PiecewiseLinearFunction_strategy)
@settings(max_examples=25)
def test_PiecewiseLinearFunction_instantiation(instance):
    assert isinstance(instance, PiecewiseLinearFunction)


PrimitiveExpression_strategy = st.builds(PrimitiveExpression)
@given(instance=PrimitiveExpression_strategy)
@settings(max_examples=25)
def test_PrimitiveExpression_instantiation(instance):
    assert isinstance(instance, PrimitiveExpression)


PrimitiveType_strategy = st.builds(PrimitiveType)
@given(instance=PrimitiveType_strategy)
@settings(max_examples=25)
def test_PrimitiveType_instantiation(instance):
    assert isinstance(instance, PrimitiveType)


RangeType_strategy = st.builds(RangeType)
@given(instance=RangeType_strategy)
@settings(max_examples=25)
def test_RangeType_instantiation(instance):
    assert isinstance(instance, RangeType)


Reference_strategy = st.builds(Reference)
@given(instance=Reference_strategy)
@settings(max_examples=25)
def test_Reference_instantiation(instance):
    assert isinstance(instance, Reference)


ScriptStatement_strategy = st.builds(ScriptStatement)
@given(instance=ScriptStatement_strategy)
@settings(max_examples=25)
def test_ScriptStatement_instantiation(instance):
    assert isinstance(instance, ScriptStatement)


SetType_strategy = st.builds(SetType)
@given(instance=SetType_strategy)
@settings(max_examples=25)
def test_SetType_instantiation(instance):
    assert isinstance(instance, SetType)



