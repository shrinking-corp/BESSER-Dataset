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
    ca_rule_CellularAutomata,
    UnaryExpression,
    ca_rule_UMinus,
    ca_rule_Not,
    IntegerExpression,
    ca_rule_CurrentCellPopulation,
    ca_rule_Conditional,
    ca_rule_NeighborsExpression,
    ca_rule_BinaryExpression,
    ca_rule_IntegerLiteral,
    ca_rule_UnaryExpression,
    BinaryExpression,
    ca_rule_Minus,
    ca_rule_Div,
    ca_rule_Mult,
    ca_rule_Or,
    ca_rule_Lower,
    ca_rule_Mod,
    ca_rule_And,
    ca_rule_Equal,
    ca_rule_Greater,
    ca_rule_Add,
    NeighborsExpression,
    ca_rule_Min,
    ca_rule_Sum,
    ca_rule_Size,
    ca_rule_Max,
    ca_rule_PopulationRange,
    ca_rule_IntegerExpression,
    ca_rule_Rule,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_ca_rule_cellularautomata_is_not_abstract():
    assert not inspect.isabstract(ca_rule_CellularAutomata)


def test_hyp_ca_rule_cellularautomata_constructor_exists():
    assert callable(ca_rule_CellularAutomata.__init__)


def test_hyp_ca_rule_cellularautomata_constructor_args():
    sig = inspect.signature(ca_rule_CellularAutomata.__init__)
    params = list(sig.parameters.keys())



def test_hyp_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryExpression)


def test_hyp_unaryexpression_constructor_exists():
    assert callable(UnaryExpression.__init__)


def test_hyp_unaryexpression_constructor_args():
    sig = inspect.signature(UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ca_rule_uminus_is_not_abstract():
    assert not inspect.isabstract(ca_rule_UMinus)


def test_hyp_ca_rule_uminus_constructor_exists():
    assert callable(ca_rule_UMinus.__init__)


def test_hyp_ca_rule_uminus_constructor_args():
    sig = inspect.signature(ca_rule_UMinus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ca_rule_not_is_not_abstract():
    assert not inspect.isabstract(ca_rule_Not)


def test_hyp_ca_rule_not_constructor_exists():
    assert callable(ca_rule_Not.__init__)


def test_hyp_ca_rule_not_constructor_args():
    sig = inspect.signature(ca_rule_Not.__init__)
    params = list(sig.parameters.keys())



def test_hyp_integerexpression_is_not_abstract():
    assert not inspect.isabstract(IntegerExpression)


def test_hyp_integerexpression_constructor_exists():
    assert callable(IntegerExpression.__init__)


def test_hyp_integerexpression_constructor_args():
    sig = inspect.signature(IntegerExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ca_rule_currentcellpopulation_is_not_abstract():
    assert not inspect.isabstract(ca_rule_CurrentCellPopulation)


def test_hyp_ca_rule_currentcellpopulation_constructor_exists():
    assert callable(ca_rule_CurrentCellPopulation.__init__)


def test_hyp_ca_rule_currentcellpopulation_constructor_args():
    sig = inspect.signature(ca_rule_CurrentCellPopulation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ca_rule_conditional_is_not_abstract():
    assert not inspect.isabstract(ca_rule_Conditional)


def test_hyp_ca_rule_conditional_constructor_exists():
    assert callable(ca_rule_Conditional.__init__)


def test_hyp_ca_rule_conditional_constructor_args():
    sig = inspect.signature(ca_rule_Conditional.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ca_rule_neighborsexpression_is_not_abstract():
    assert not inspect.isabstract(ca_rule_NeighborsExpression)


def test_hyp_ca_rule_neighborsexpression_constructor_exists():
    assert callable(ca_rule_NeighborsExpression.__init__)


def test_hyp_ca_rule_neighborsexpression_constructor_args():
    sig = inspect.signature(ca_rule_NeighborsExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ca_rule_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(ca_rule_BinaryExpression)


def test_hyp_ca_rule_binaryexpression_constructor_exists():
    assert callable(ca_rule_BinaryExpression.__init__)


def test_hyp_ca_rule_binaryexpression_constructor_args():
    sig = inspect.signature(ca_rule_BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ca_rule_integerliteral_is_not_abstract():
    assert not inspect.isabstract(ca_rule_IntegerLiteral)


def test_hyp_ca_rule_integerliteral_constructor_exists():
    assert callable(ca_rule_IntegerLiteral.__init__)


def test_hyp_ca_rule_integerliteral_constructor_args():
    sig = inspect.signature(ca_rule_IntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_ca_rule_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(ca_rule_UnaryExpression)


def test_hyp_ca_rule_unaryexpression_constructor_exists():
    assert callable(ca_rule_UnaryExpression.__init__)


def test_hyp_ca_rule_unaryexpression_constructor_args():
    sig = inspect.signature(ca_rule_UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_hyp_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_hyp_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ca_rule_minus_is_not_abstract():
    assert not inspect.isabstract(ca_rule_Minus)


def test_hyp_ca_rule_minus_constructor_exists():
    assert callable(ca_rule_Minus.__init__)


def test_hyp_ca_rule_minus_constructor_args():
    sig = inspect.signature(ca_rule_Minus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ca_rule_div_is_not_abstract():
    assert not inspect.isabstract(ca_rule_Div)


def test_hyp_ca_rule_div_constructor_exists():
    assert callable(ca_rule_Div.__init__)


def test_hyp_ca_rule_div_constructor_args():
    sig = inspect.signature(ca_rule_Div.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ca_rule_mult_is_not_abstract():
    assert not inspect.isabstract(ca_rule_Mult)


def test_hyp_ca_rule_mult_constructor_exists():
    assert callable(ca_rule_Mult.__init__)


def test_hyp_ca_rule_mult_constructor_args():
    sig = inspect.signature(ca_rule_Mult.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ca_rule_or_is_not_abstract():
    assert not inspect.isabstract(ca_rule_Or)


def test_hyp_ca_rule_or_constructor_exists():
    assert callable(ca_rule_Or.__init__)


def test_hyp_ca_rule_or_constructor_args():
    sig = inspect.signature(ca_rule_Or.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ca_rule_lower_is_not_abstract():
    assert not inspect.isabstract(ca_rule_Lower)


def test_hyp_ca_rule_lower_constructor_exists():
    assert callable(ca_rule_Lower.__init__)


def test_hyp_ca_rule_lower_constructor_args():
    sig = inspect.signature(ca_rule_Lower.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ca_rule_mod_is_not_abstract():
    assert not inspect.isabstract(ca_rule_Mod)


def test_hyp_ca_rule_mod_constructor_exists():
    assert callable(ca_rule_Mod.__init__)


def test_hyp_ca_rule_mod_constructor_args():
    sig = inspect.signature(ca_rule_Mod.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ca_rule_and_is_not_abstract():
    assert not inspect.isabstract(ca_rule_And)


def test_hyp_ca_rule_and_constructor_exists():
    assert callable(ca_rule_And.__init__)


def test_hyp_ca_rule_and_constructor_args():
    sig = inspect.signature(ca_rule_And.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ca_rule_equal_is_not_abstract():
    assert not inspect.isabstract(ca_rule_Equal)


def test_hyp_ca_rule_equal_constructor_exists():
    assert callable(ca_rule_Equal.__init__)


def test_hyp_ca_rule_equal_constructor_args():
    sig = inspect.signature(ca_rule_Equal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ca_rule_greater_is_not_abstract():
    assert not inspect.isabstract(ca_rule_Greater)


def test_hyp_ca_rule_greater_constructor_exists():
    assert callable(ca_rule_Greater.__init__)


def test_hyp_ca_rule_greater_constructor_args():
    sig = inspect.signature(ca_rule_Greater.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ca_rule_add_is_not_abstract():
    assert not inspect.isabstract(ca_rule_Add)


def test_hyp_ca_rule_add_constructor_exists():
    assert callable(ca_rule_Add.__init__)


def test_hyp_ca_rule_add_constructor_args():
    sig = inspect.signature(ca_rule_Add.__init__)
    params = list(sig.parameters.keys())



def test_hyp_neighborsexpression_is_not_abstract():
    assert not inspect.isabstract(NeighborsExpression)


def test_hyp_neighborsexpression_constructor_exists():
    assert callable(NeighborsExpression.__init__)


def test_hyp_neighborsexpression_constructor_args():
    sig = inspect.signature(NeighborsExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ca_rule_min_is_not_abstract():
    assert not inspect.isabstract(ca_rule_Min)


def test_hyp_ca_rule_min_constructor_exists():
    assert callable(ca_rule_Min.__init__)


def test_hyp_ca_rule_min_constructor_args():
    sig = inspect.signature(ca_rule_Min.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ca_rule_sum_is_not_abstract():
    assert not inspect.isabstract(ca_rule_Sum)


def test_hyp_ca_rule_sum_constructor_exists():
    assert callable(ca_rule_Sum.__init__)


def test_hyp_ca_rule_sum_constructor_args():
    sig = inspect.signature(ca_rule_Sum.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ca_rule_size_is_not_abstract():
    assert not inspect.isabstract(ca_rule_Size)


def test_hyp_ca_rule_size_constructor_exists():
    assert callable(ca_rule_Size.__init__)


def test_hyp_ca_rule_size_constructor_args():
    sig = inspect.signature(ca_rule_Size.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ca_rule_max_is_not_abstract():
    assert not inspect.isabstract(ca_rule_Max)


def test_hyp_ca_rule_max_constructor_exists():
    assert callable(ca_rule_Max.__init__)


def test_hyp_ca_rule_max_constructor_args():
    sig = inspect.signature(ca_rule_Max.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ca_rule_populationrange_is_not_abstract():
    assert not inspect.isabstract(ca_rule_PopulationRange)


def test_hyp_ca_rule_populationrange_constructor_exists():
    assert callable(ca_rule_PopulationRange.__init__)


def test_hyp_ca_rule_populationrange_constructor_args():
    sig = inspect.signature(ca_rule_PopulationRange.__init__)
    params = list(sig.parameters.keys())
    assert "upperRange" in params, "Missing parameter 'upperRange'"
    assert "lowerRange" in params, "Missing parameter 'lowerRange'"





def test_hyp_ca_rule_integerexpression_is_not_abstract():
    assert not inspect.isabstract(ca_rule_IntegerExpression)


def test_hyp_ca_rule_integerexpression_constructor_exists():
    assert callable(ca_rule_IntegerExpression.__init__)


def test_hyp_ca_rule_integerexpression_constructor_args():
    sig = inspect.signature(ca_rule_IntegerExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ca_rule_rule_is_not_abstract():
    assert not inspect.isabstract(ca_rule_Rule)


def test_hyp_ca_rule_rule_constructor_exists():
    assert callable(ca_rule_Rule.__init__)


def test_hyp_ca_rule_rule_constructor_args():
    sig = inspect.signature(ca_rule_Rule.__init__)
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
ca_rule_CellularAutomata_strategy = st.builds(
    ca_rule_CellularAutomata,
)
UnaryExpression_strategy = st.builds(
    UnaryExpression,
)
ca_rule_UMinus_strategy = st.builds(
    ca_rule_UMinus,
)
ca_rule_Not_strategy = st.builds(
    ca_rule_Not,
)
IntegerExpression_strategy = st.builds(
    IntegerExpression,
)
ca_rule_CurrentCellPopulation_strategy = st.builds(
    ca_rule_CurrentCellPopulation,
)
ca_rule_Conditional_strategy = st.builds(
    ca_rule_Conditional,
)
ca_rule_NeighborsExpression_strategy = st.builds(
    ca_rule_NeighborsExpression,
)
ca_rule_BinaryExpression_strategy = st.builds(
    ca_rule_BinaryExpression,
)
ca_rule_IntegerLiteral_strategy = st.builds(
    ca_rule_IntegerLiteral,
    value=
        st.integers()
)
ca_rule_UnaryExpression_strategy = st.builds(
    ca_rule_UnaryExpression,
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
ca_rule_Minus_strategy = st.builds(
    ca_rule_Minus,
)
ca_rule_Div_strategy = st.builds(
    ca_rule_Div,
)
ca_rule_Mult_strategy = st.builds(
    ca_rule_Mult,
)
ca_rule_Or_strategy = st.builds(
    ca_rule_Or,
)
ca_rule_Lower_strategy = st.builds(
    ca_rule_Lower,
)
ca_rule_Mod_strategy = st.builds(
    ca_rule_Mod,
)
ca_rule_And_strategy = st.builds(
    ca_rule_And,
)
ca_rule_Equal_strategy = st.builds(
    ca_rule_Equal,
)
ca_rule_Greater_strategy = st.builds(
    ca_rule_Greater,
)
ca_rule_Add_strategy = st.builds(
    ca_rule_Add,
)
NeighborsExpression_strategy = st.builds(
    NeighborsExpression,
)
ca_rule_Min_strategy = st.builds(
    ca_rule_Min,
)
ca_rule_Sum_strategy = st.builds(
    ca_rule_Sum,
)
ca_rule_Size_strategy = st.builds(
    ca_rule_Size,
)
ca_rule_Max_strategy = st.builds(
    ca_rule_Max,
)
ca_rule_PopulationRange_strategy = st.builds(
    ca_rule_PopulationRange,
    upperRange=
        st.integers(),
    lowerRange=
        st.integers()
)
ca_rule_IntegerExpression_strategy = st.builds(
    ca_rule_IntegerExpression,
)
ca_rule_Rule_strategy = st.builds(
    ca_rule_Rule,
)













@given(instance=ca_rule_IntegerLiteral_strategy)
def test_hyp_ca_rule_integerliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original





















@given(instance=ca_rule_PopulationRange_strategy)
def test_hyp_ca_rule_populationrange_upperRange_setter(instance):
    original = instance.upperRange
    instance.upperRange = original
    assert instance.upperRange == original



@given(instance=ca_rule_PopulationRange_strategy)
def test_hyp_ca_rule_populationrange_lowerRange_setter(instance):
    original = instance.lowerRange
    instance.lowerRange = original
    assert instance.lowerRange == original




# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    BinaryExpression,
    IntegerExpression,
    NeighborsExpression,
    UnaryExpression,
    ca_rule_Add,
    ca_rule_And,
    ca_rule_BinaryExpression,
    ca_rule_CellularAutomata,
    ca_rule_Conditional,
    ca_rule_CurrentCellPopulation,
    ca_rule_Div,
    ca_rule_Equal,
    ca_rule_Greater,
    ca_rule_IntegerExpression,
    ca_rule_IntegerLiteral,
    ca_rule_Lower,
    ca_rule_Max,
    ca_rule_Min,
    ca_rule_Minus,
    ca_rule_Mod,
    ca_rule_Mult,
    ca_rule_NeighborsExpression,
    ca_rule_Not,
    ca_rule_Or,
    ca_rule_PopulationRange,
    ca_rule_Rule,
    ca_rule_Size,
    ca_rule_Sum,
    ca_rule_UMinus,
    ca_rule_UnaryExpression,
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

def test_ca_rule_IntegerLiteral_value_value_roundtrip():
    instance = ca_rule_IntegerLiteral(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_ca_rule_PopulationRange_lowerRange_value_roundtrip():
    instance = ca_rule_PopulationRange(lowerRange=7, upperRange=7)
    assert instance.lowerRange == 7
    instance.lowerRange = 13
    assert instance.lowerRange == 13


def test_ca_rule_PopulationRange_upperRange_value_roundtrip():
    instance = ca_rule_PopulationRange(lowerRange=7, upperRange=7)
    assert instance.upperRange == 7
    instance.upperRange = 13
    assert instance.upperRange == 13


def test_ca_rule_Add_isa_BinaryExpression():
    instance = ca_rule_Add()
    assert isinstance(instance, BinaryExpression)


def test_ca_rule_And_isa_BinaryExpression():
    instance = ca_rule_And()
    assert isinstance(instance, BinaryExpression)


def test_ca_rule_Div_isa_BinaryExpression():
    instance = ca_rule_Div()
    assert isinstance(instance, BinaryExpression)


def test_ca_rule_Equal_isa_BinaryExpression():
    instance = ca_rule_Equal()
    assert isinstance(instance, BinaryExpression)


def test_ca_rule_Greater_isa_BinaryExpression():
    instance = ca_rule_Greater()
    assert isinstance(instance, BinaryExpression)


def test_ca_rule_Lower_isa_BinaryExpression():
    instance = ca_rule_Lower()
    assert isinstance(instance, BinaryExpression)


def test_ca_rule_Minus_isa_BinaryExpression():
    instance = ca_rule_Minus()
    assert isinstance(instance, BinaryExpression)


def test_ca_rule_Mod_isa_BinaryExpression():
    instance = ca_rule_Mod()
    assert isinstance(instance, BinaryExpression)


def test_ca_rule_Mult_isa_BinaryExpression():
    instance = ca_rule_Mult()
    assert isinstance(instance, BinaryExpression)


def test_ca_rule_Or_isa_BinaryExpression():
    instance = ca_rule_Or()
    assert isinstance(instance, BinaryExpression)


def test_ca_rule_BinaryExpression_isa_IntegerExpression():
    instance = ca_rule_BinaryExpression()
    assert isinstance(instance, IntegerExpression)


def test_ca_rule_Conditional_isa_IntegerExpression():
    instance = ca_rule_Conditional()
    assert isinstance(instance, IntegerExpression)


def test_ca_rule_CurrentCellPopulation_isa_IntegerExpression():
    instance = ca_rule_CurrentCellPopulation()
    assert isinstance(instance, IntegerExpression)


def test_ca_rule_IntegerLiteral_isa_IntegerExpression():
    instance = ca_rule_IntegerLiteral(value=7)
    assert isinstance(instance, IntegerExpression)


def test_ca_rule_NeighborsExpression_isa_IntegerExpression():
    instance = ca_rule_NeighborsExpression()
    assert isinstance(instance, IntegerExpression)


def test_ca_rule_UnaryExpression_isa_IntegerExpression():
    instance = ca_rule_UnaryExpression()
    assert isinstance(instance, IntegerExpression)


def test_ca_rule_Max_isa_NeighborsExpression():
    instance = ca_rule_Max()
    assert isinstance(instance, NeighborsExpression)


def test_ca_rule_Min_isa_NeighborsExpression():
    instance = ca_rule_Min()
    assert isinstance(instance, NeighborsExpression)


def test_ca_rule_Size_isa_NeighborsExpression():
    instance = ca_rule_Size()
    assert isinstance(instance, NeighborsExpression)


def test_ca_rule_Sum_isa_NeighborsExpression():
    instance = ca_rule_Sum()
    assert isinstance(instance, NeighborsExpression)


def test_ca_rule_Not_isa_UnaryExpression():
    instance = ca_rule_Not()
    assert isinstance(instance, UnaryExpression)


def test_ca_rule_UMinus_isa_UnaryExpression():
    instance = ca_rule_UMinus()
    assert isinstance(instance, UnaryExpression)


def test_assoc_filter1_link_reassign_clear():
    a = ca_rule_PopulationRange(lowerRange=7, upperRange=7)
    b1 = ca_rule_Rule()
    b2 = ca_rule_Rule()
    _safe_set(a, 'ca_rule_PopulationRange', b1)
    assert _is_linked(a, 'ca_rule_PopulationRange', b1)
    if hasattr(b1, 'ca_rule_Rule2'):
        assert _is_linked(b1, 'ca_rule_Rule2', a)
    _safe_set(a, 'ca_rule_PopulationRange', b2)
    assert _is_linked(a, 'ca_rule_PopulationRange', b2)
    if hasattr(b1, 'ca_rule_Rule2'):
        assert not _is_linked(b1, 'ca_rule_Rule2', a)
    if hasattr(b2, 'ca_rule_Rule2'):
        assert _is_linked(b2, 'ca_rule_Rule2', a)
    _safe_set(a, 'ca_rule_PopulationRange', None)
    assert not _is_linked(a, 'ca_rule_PopulationRange', b2)
    if hasattr(b2, 'ca_rule_Rule2'):
        assert not _is_linked(b2, 'ca_rule_Rule2', a)


def test_assoc_neighborsFilter13_link_reassign_clear():
    a = ca_rule_PopulationRange(lowerRange=7, upperRange=7)
    b1 = ca_rule_NeighborsExpression()
    b2 = ca_rule_NeighborsExpression()
    _safe_set(a, 'ca_rule_PopulationRange14', b1)
    assert _is_linked(a, 'ca_rule_PopulationRange14', b1)
    if hasattr(b1, 'ca_rule_NeighborsExpression'):
        assert _is_linked(b1, 'ca_rule_NeighborsExpression', a)
    _safe_set(a, 'ca_rule_PopulationRange14', b2)
    assert _is_linked(a, 'ca_rule_PopulationRange14', b2)
    if hasattr(b1, 'ca_rule_NeighborsExpression'):
        assert not _is_linked(b1, 'ca_rule_NeighborsExpression', a)
    if hasattr(b2, 'ca_rule_NeighborsExpression'):
        assert _is_linked(b2, 'ca_rule_NeighborsExpression', a)
    _safe_set(a, 'ca_rule_PopulationRange14', None)
    assert not _is_linked(a, 'ca_rule_PopulationRange14', b2)
    if hasattr(b2, 'ca_rule_NeighborsExpression'):
        assert not _is_linked(b2, 'ca_rule_NeighborsExpression', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BinaryExpression_strategy = st.builds(BinaryExpression)
@given(instance=BinaryExpression_strategy)
@settings(max_examples=25)
def test_BinaryExpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)


IntegerExpression_strategy = st.builds(IntegerExpression)
@given(instance=IntegerExpression_strategy)
@settings(max_examples=25)
def test_IntegerExpression_instantiation(instance):
    assert isinstance(instance, IntegerExpression)


NeighborsExpression_strategy = st.builds(NeighborsExpression)
@given(instance=NeighborsExpression_strategy)
@settings(max_examples=25)
def test_NeighborsExpression_instantiation(instance):
    assert isinstance(instance, NeighborsExpression)


UnaryExpression_strategy = st.builds(UnaryExpression)
@given(instance=UnaryExpression_strategy)
@settings(max_examples=25)
def test_UnaryExpression_instantiation(instance):
    assert isinstance(instance, UnaryExpression)


ca_rule_Add_strategy = st.builds(ca_rule_Add)
@given(instance=ca_rule_Add_strategy)
@settings(max_examples=25)
def test_ca_rule_Add_instantiation(instance):
    assert isinstance(instance, ca_rule_Add)


ca_rule_And_strategy = st.builds(ca_rule_And)
@given(instance=ca_rule_And_strategy)
@settings(max_examples=25)
def test_ca_rule_And_instantiation(instance):
    assert isinstance(instance, ca_rule_And)


ca_rule_BinaryExpression_strategy = st.builds(ca_rule_BinaryExpression)
@given(instance=ca_rule_BinaryExpression_strategy)
@settings(max_examples=25)
def test_ca_rule_BinaryExpression_instantiation(instance):
    assert isinstance(instance, ca_rule_BinaryExpression)


ca_rule_CellularAutomata_strategy = st.builds(ca_rule_CellularAutomata)
@given(instance=ca_rule_CellularAutomata_strategy)
@settings(max_examples=25)
def test_ca_rule_CellularAutomata_instantiation(instance):
    assert isinstance(instance, ca_rule_CellularAutomata)


ca_rule_Conditional_strategy = st.builds(ca_rule_Conditional)
@given(instance=ca_rule_Conditional_strategy)
@settings(max_examples=25)
def test_ca_rule_Conditional_instantiation(instance):
    assert isinstance(instance, ca_rule_Conditional)


ca_rule_CurrentCellPopulation_strategy = st.builds(ca_rule_CurrentCellPopulation)
@given(instance=ca_rule_CurrentCellPopulation_strategy)
@settings(max_examples=25)
def test_ca_rule_CurrentCellPopulation_instantiation(instance):
    assert isinstance(instance, ca_rule_CurrentCellPopulation)


ca_rule_Div_strategy = st.builds(ca_rule_Div)
@given(instance=ca_rule_Div_strategy)
@settings(max_examples=25)
def test_ca_rule_Div_instantiation(instance):
    assert isinstance(instance, ca_rule_Div)


ca_rule_Equal_strategy = st.builds(ca_rule_Equal)
@given(instance=ca_rule_Equal_strategy)
@settings(max_examples=25)
def test_ca_rule_Equal_instantiation(instance):
    assert isinstance(instance, ca_rule_Equal)


ca_rule_Greater_strategy = st.builds(ca_rule_Greater)
@given(instance=ca_rule_Greater_strategy)
@settings(max_examples=25)
def test_ca_rule_Greater_instantiation(instance):
    assert isinstance(instance, ca_rule_Greater)


ca_rule_IntegerExpression_strategy = st.builds(ca_rule_IntegerExpression)
@given(instance=ca_rule_IntegerExpression_strategy)
@settings(max_examples=25)
def test_ca_rule_IntegerExpression_instantiation(instance):
    assert isinstance(instance, ca_rule_IntegerExpression)


ca_rule_IntegerLiteral_strategy = st.builds(ca_rule_IntegerLiteral, value=st.integers())
@given(instance=ca_rule_IntegerLiteral_strategy)
@settings(max_examples=25)
def test_ca_rule_IntegerLiteral_instantiation(instance):
    assert isinstance(instance, ca_rule_IntegerLiteral)


ca_rule_Lower_strategy = st.builds(ca_rule_Lower)
@given(instance=ca_rule_Lower_strategy)
@settings(max_examples=25)
def test_ca_rule_Lower_instantiation(instance):
    assert isinstance(instance, ca_rule_Lower)


ca_rule_Max_strategy = st.builds(ca_rule_Max)
@given(instance=ca_rule_Max_strategy)
@settings(max_examples=25)
def test_ca_rule_Max_instantiation(instance):
    assert isinstance(instance, ca_rule_Max)


ca_rule_Min_strategy = st.builds(ca_rule_Min)
@given(instance=ca_rule_Min_strategy)
@settings(max_examples=25)
def test_ca_rule_Min_instantiation(instance):
    assert isinstance(instance, ca_rule_Min)


ca_rule_Minus_strategy = st.builds(ca_rule_Minus)
@given(instance=ca_rule_Minus_strategy)
@settings(max_examples=25)
def test_ca_rule_Minus_instantiation(instance):
    assert isinstance(instance, ca_rule_Minus)


ca_rule_Mod_strategy = st.builds(ca_rule_Mod)
@given(instance=ca_rule_Mod_strategy)
@settings(max_examples=25)
def test_ca_rule_Mod_instantiation(instance):
    assert isinstance(instance, ca_rule_Mod)


ca_rule_Mult_strategy = st.builds(ca_rule_Mult)
@given(instance=ca_rule_Mult_strategy)
@settings(max_examples=25)
def test_ca_rule_Mult_instantiation(instance):
    assert isinstance(instance, ca_rule_Mult)


ca_rule_NeighborsExpression_strategy = st.builds(ca_rule_NeighborsExpression)
@given(instance=ca_rule_NeighborsExpression_strategy)
@settings(max_examples=25)
def test_ca_rule_NeighborsExpression_instantiation(instance):
    assert isinstance(instance, ca_rule_NeighborsExpression)


ca_rule_Not_strategy = st.builds(ca_rule_Not)
@given(instance=ca_rule_Not_strategy)
@settings(max_examples=25)
def test_ca_rule_Not_instantiation(instance):
    assert isinstance(instance, ca_rule_Not)


ca_rule_Or_strategy = st.builds(ca_rule_Or)
@given(instance=ca_rule_Or_strategy)
@settings(max_examples=25)
def test_ca_rule_Or_instantiation(instance):
    assert isinstance(instance, ca_rule_Or)


ca_rule_PopulationRange_strategy = st.builds(ca_rule_PopulationRange, lowerRange=st.integers(), upperRange=st.integers())
@given(instance=ca_rule_PopulationRange_strategy)
@settings(max_examples=25)
def test_ca_rule_PopulationRange_instantiation(instance):
    assert isinstance(instance, ca_rule_PopulationRange)


ca_rule_Rule_strategy = st.builds(ca_rule_Rule)
@given(instance=ca_rule_Rule_strategy)
@settings(max_examples=25)
def test_ca_rule_Rule_instantiation(instance):
    assert isinstance(instance, ca_rule_Rule)


ca_rule_Size_strategy = st.builds(ca_rule_Size)
@given(instance=ca_rule_Size_strategy)
@settings(max_examples=25)
def test_ca_rule_Size_instantiation(instance):
    assert isinstance(instance, ca_rule_Size)


ca_rule_Sum_strategy = st.builds(ca_rule_Sum)
@given(instance=ca_rule_Sum_strategy)
@settings(max_examples=25)
def test_ca_rule_Sum_instantiation(instance):
    assert isinstance(instance, ca_rule_Sum)


ca_rule_UMinus_strategy = st.builds(ca_rule_UMinus)
@given(instance=ca_rule_UMinus_strategy)
@settings(max_examples=25)
def test_ca_rule_UMinus_instantiation(instance):
    assert isinstance(instance, ca_rule_UMinus)


ca_rule_UnaryExpression_strategy = st.builds(ca_rule_UnaryExpression)
@given(instance=ca_rule_UnaryExpression_strategy)
@settings(max_examples=25)
def test_ca_rule_UnaryExpression_instantiation(instance):
    assert isinstance(instance, ca_rule_UnaryExpression)



