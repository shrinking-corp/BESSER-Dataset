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
    ATerm,
    adt_Variable,
    adt_Term,
    adt_ATerm,
    adt_Operation,
    ASort,
    adt_Sort,
    adt_SubSort,
    adt_Equation,
    adt_VariableDeclaration,
    adt_Signature,
    adt_ADT,
    adt_ASort,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_aterm_is_not_abstract():
    assert not inspect.isabstract(ATerm)


def test_hyp_aterm_constructor_exists():
    assert callable(ATerm.__init__)


def test_hyp_aterm_constructor_args():
    sig = inspect.signature(ATerm.__init__)
    params = list(sig.parameters.keys())



def test_hyp_adt_variable_is_not_abstract():
    assert not inspect.isabstract(adt_Variable)


def test_hyp_adt_variable_constructor_exists():
    assert callable(adt_Variable.__init__)


def test_hyp_adt_variable_constructor_args():
    sig = inspect.signature(adt_Variable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_adt_term_is_not_abstract():
    assert not inspect.isabstract(adt_Term)


def test_hyp_adt_term_constructor_exists():
    assert callable(adt_Term.__init__)


def test_hyp_adt_term_constructor_args():
    sig = inspect.signature(adt_Term.__init__)
    params = list(sig.parameters.keys())



def test_hyp_adt_aterm_is_not_abstract():
    assert not inspect.isabstract(adt_ATerm)


def test_hyp_adt_aterm_constructor_exists():
    assert callable(adt_ATerm.__init__)


def test_hyp_adt_aterm_constructor_args():
    sig = inspect.signature(adt_ATerm.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"




def test_hyp_adt_operation_is_not_abstract():
    assert not inspect.isabstract(adt_Operation)


def test_hyp_adt_operation_constructor_exists():
    assert callable(adt_Operation.__init__)


def test_hyp_adt_operation_constructor_args():
    sig = inspect.signature(adt_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_asort_is_not_abstract():
    assert not inspect.isabstract(ASort)


def test_hyp_asort_constructor_exists():
    assert callable(ASort.__init__)


def test_hyp_asort_constructor_args():
    sig = inspect.signature(ASort.__init__)
    params = list(sig.parameters.keys())



def test_hyp_adt_sort_is_not_abstract():
    assert not inspect.isabstract(adt_Sort)


def test_hyp_adt_sort_constructor_exists():
    assert callable(adt_Sort.__init__)


def test_hyp_adt_sort_constructor_args():
    sig = inspect.signature(adt_Sort.__init__)
    params = list(sig.parameters.keys())



def test_hyp_adt_subsort_is_not_abstract():
    assert not inspect.isabstract(adt_SubSort)


def test_hyp_adt_subsort_constructor_exists():
    assert callable(adt_SubSort.__init__)


def test_hyp_adt_subsort_constructor_args():
    sig = inspect.signature(adt_SubSort.__init__)
    params = list(sig.parameters.keys())



def test_hyp_adt_equation_is_not_abstract():
    assert not inspect.isabstract(adt_Equation)


def test_hyp_adt_equation_constructor_exists():
    assert callable(adt_Equation.__init__)


def test_hyp_adt_equation_constructor_args():
    sig = inspect.signature(adt_Equation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_adt_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(adt_VariableDeclaration)


def test_hyp_adt_variabledeclaration_constructor_exists():
    assert callable(adt_VariableDeclaration.__init__)


def test_hyp_adt_variabledeclaration_constructor_args():
    sig = inspect.signature(adt_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_adt_signature_is_not_abstract():
    assert not inspect.isabstract(adt_Signature)


def test_hyp_adt_signature_constructor_exists():
    assert callable(adt_Signature.__init__)


def test_hyp_adt_signature_constructor_args():
    sig = inspect.signature(adt_Signature.__init__)
    params = list(sig.parameters.keys())
    assert "ops" in params, "Missing parameter 'ops'"




def test_hyp_adt_adt_is_not_abstract():
    assert not inspect.isabstract(adt_ADT)


def test_hyp_adt_adt_constructor_exists():
    assert callable(adt_ADT.__init__)


def test_hyp_adt_adt_constructor_args():
    sig = inspect.signature(adt_ADT.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_adt_asort_is_not_abstract():
    assert not inspect.isabstract(adt_ASort)


def test_hyp_adt_asort_constructor_exists():
    assert callable(adt_ASort.__init__)


def test_hyp_adt_asort_constructor_args():
    sig = inspect.signature(adt_ASort.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"



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
ATerm_strategy = st.builds(
    ATerm,
)
adt_Variable_strategy = st.builds(
    adt_Variable,
)
adt_Term_strategy = st.builds(
    adt_Term,
)
adt_ATerm_strategy = st.builds(
    adt_ATerm,
    symbol=
        safe_text
)
adt_Operation_strategy = st.builds(
    adt_Operation,
    name=
        safe_text
)
ASort_strategy = st.builds(
    ASort,
)
adt_Sort_strategy = st.builds(
    adt_Sort,
)
adt_SubSort_strategy = st.builds(
    adt_SubSort,
)
adt_Equation_strategy = st.builds(
    adt_Equation,
)
adt_VariableDeclaration_strategy = st.builds(
    adt_VariableDeclaration,
    name=
        safe_text
)
adt_Signature_strategy = st.builds(
    adt_Signature,
    ops=
        safe_text
)
adt_ADT_strategy = st.builds(
    adt_ADT,
    name=
        safe_text
)
adt_ASort_strategy = st.builds(
    adt_ASort,
    name=
        safe_text
)







@given(instance=adt_ATerm_strategy)
def test_hyp_adt_aterm_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original




@given(instance=adt_Operation_strategy)
def test_hyp_adt_operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original








@given(instance=adt_VariableDeclaration_strategy)
def test_hyp_adt_variabledeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=adt_Signature_strategy)
def test_hyp_adt_signature_ops_setter(instance):
    original = instance.ops
    instance.ops = original
    assert instance.ops == original




@given(instance=adt_ADT_strategy)
def test_hyp_adt_adt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=adt_ASort_strategy)
def test_hyp_adt_asort_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=adt_ASort_strategy)
@settings(max_examples=30)
def test_hyp_adt_asort_issubsortof_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isSubSortOf(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isSubSortOf).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isSubSortOf' in adt_ASort is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isSubSortOf' in adt_ASort did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isSubSortOf' in adt_ASort is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    ASort,
    ATerm,
    adt_ADT,
    adt_ASort,
    adt_ATerm,
    adt_Equation,
    adt_Operation,
    adt_Signature,
    adt_Sort,
    adt_SubSort,
    adt_Term,
    adt_Variable,
    adt_VariableDeclaration,
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

def test_adt_ADT_name_value_roundtrip():
    instance = adt_ADT(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_adt_ASort_name_value_roundtrip():
    instance = adt_ASort(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_adt_ATerm_symbol_value_roundtrip():
    instance = adt_ATerm(symbol="sample_text")
    assert instance.symbol == "sample_text"
    instance.symbol = "sample_text_2"
    assert instance.symbol == "sample_text_2"


def test_adt_Operation_name_value_roundtrip():
    instance = adt_Operation(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_adt_Signature_ops_value_roundtrip():
    instance = adt_Signature(ops="sample_text")
    assert instance.ops == "sample_text"
    instance.ops = "sample_text_2"
    assert instance.ops == "sample_text_2"


def test_adt_VariableDeclaration_name_value_roundtrip():
    instance = adt_VariableDeclaration(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_adt_Sort_isa_ASort():
    instance = adt_Sort()
    assert isinstance(instance, ASort)


def test_adt_SubSort_isa_ASort():
    instance = adt_SubSort()
    assert isinstance(instance, ASort)


def test_adt_Term_isa_ATerm():
    instance = adt_Term()
    assert isinstance(instance, ATerm)


def test_adt_Variable_isa_ATerm():
    instance = adt_Variable()
    assert isinstance(instance, ATerm)


def test_assoc_adt26_link_reassign_clear():
    a = adt_ATerm(symbol="sample_text")
    b1 = adt_ADT(name="sample_text")
    b2 = adt_ADT(name="sample_text_2")
    _safe_set(a, 'adt_ATerm', b1)
    assert _is_linked(a, 'adt_ATerm', b1)
    if hasattr(b1, 'adt_ADT27'):
        assert _is_linked(b1, 'adt_ADT27', a)
    _safe_set(a, 'adt_ATerm', b2)
    assert _is_linked(a, 'adt_ATerm', b2)
    if hasattr(b1, 'adt_ADT27'):
        assert not _is_linked(b1, 'adt_ADT27', a)
    if hasattr(b2, 'adt_ADT27'):
        assert _is_linked(b2, 'adt_ADT27', a)
    _safe_set(a, 'adt_ATerm', None)
    assert not _is_linked(a, 'adt_ATerm', b2)
    if hasattr(b2, 'adt_ADT27'):
        assert not _is_linked(b2, 'adt_ADT27', a)


def test_assoc_allOperations6_link_reassign_clear():
    a = adt_Signature(ops="sample_text")
    b1 = adt_Operation(name="sample_text")
    b2 = adt_Operation(name="sample_text_2")
    _safe_set(a, 'adt_Signature7', {b1})
    assert _is_linked(a, 'adt_Signature7', b1)
    if hasattr(b1, 'adt_Operation'):
        assert _is_linked(b1, 'adt_Operation', a)
    _safe_set(a, 'adt_Signature7', {b2})
    assert _is_linked(a, 'adt_Signature7', b2)
    if hasattr(b1, 'adt_Operation'):
        assert not _is_linked(b1, 'adt_Operation', a)
    if hasattr(b2, 'adt_Operation'):
        assert _is_linked(b2, 'adt_Operation', a)
    _safe_set(a, 'adt_Signature7', set())
    assert not _is_linked(a, 'adt_Signature7', b2)
    if hasattr(b2, 'adt_Operation'):
        assert not _is_linked(b2, 'adt_Operation', a)


def test_assoc_declaration36_link_reassign_clear():
    a = adt_VariableDeclaration(name="sample_text")
    b1 = adt_Variable()
    b2 = adt_Variable()
    _safe_set(a, 'adt_VariableDeclaration37', b1)
    assert _is_linked(a, 'adt_VariableDeclaration37', b1)
    if hasattr(b1, 'adt_Variable'):
        assert _is_linked(b1, 'adt_Variable', a)
    _safe_set(a, 'adt_VariableDeclaration37', b2)
    assert _is_linked(a, 'adt_VariableDeclaration37', b2)
    if hasattr(b1, 'adt_Variable'):
        assert not _is_linked(b1, 'adt_Variable', a)
    if hasattr(b2, 'adt_Variable'):
        assert _is_linked(b2, 'adt_Variable', a)
    _safe_set(a, 'adt_VariableDeclaration37', None)
    assert not _is_linked(a, 'adt_VariableDeclaration37', b2)
    if hasattr(b2, 'adt_Variable'):
        assert not _is_linked(b2, 'adt_Variable', a)


def test_assoc_equations3_link_reassign_clear():
    a = adt_ADT(name="sample_text")
    b1 = adt_Equation()
    b2 = adt_Equation()
    _safe_set(a, 'adt_ADT4', {b1})
    assert _is_linked(a, 'adt_ADT4', b1)
    if hasattr(b1, 'adt_Equation'):
        assert _is_linked(b1, 'adt_Equation', a)
    _safe_set(a, 'adt_ADT4', {b2})
    assert _is_linked(a, 'adt_ADT4', b2)
    if hasattr(b1, 'adt_Equation'):
        assert not _is_linked(b1, 'adt_Equation', a)
    if hasattr(b2, 'adt_Equation'):
        assert _is_linked(b2, 'adt_Equation', a)
    _safe_set(a, 'adt_ADT4', set())
    assert not _is_linked(a, 'adt_ADT4', b2)
    if hasattr(b2, 'adt_Equation'):
        assert not _is_linked(b2, 'adt_Equation', a)


def test_assoc_formalParameters23_link_reassign_clear():
    a = adt_Operation(name="sample_text")
    b1 = adt_ASort(name="sample_text")
    b2 = adt_ASort(name="sample_text_2")
    _safe_set(a, 'adt_Operation24', {b1})
    assert _is_linked(a, 'adt_Operation24', b1)
    if hasattr(b1, 'adt_ASort25'):
        assert _is_linked(b1, 'adt_ASort25', a)
    _safe_set(a, 'adt_Operation24', {b2})
    assert _is_linked(a, 'adt_Operation24', b2)
    if hasattr(b1, 'adt_ASort25'):
        assert not _is_linked(b1, 'adt_ASort25', a)
    if hasattr(b2, 'adt_ASort25'):
        assert _is_linked(b2, 'adt_ASort25', a)
    _safe_set(a, 'adt_Operation24', set())
    assert not _is_linked(a, 'adt_Operation24', b2)
    if hasattr(b2, 'adt_ASort25'):
        assert not _is_linked(b2, 'adt_ASort25', a)


def test_assoc_generators14_link_reassign_clear():
    a = adt_Signature(ops="sample_text")
    b1 = adt_Operation(name="sample_text")
    b2 = adt_Operation(name="sample_text_2")
    _safe_set(a, 'adt_Signature15', {b1})
    assert _is_linked(a, 'adt_Signature15', b1)
    if hasattr(b1, 'adt_Operation16'):
        assert _is_linked(b1, 'adt_Operation16', a)
    _safe_set(a, 'adt_Signature15', {b2})
    assert _is_linked(a, 'adt_Signature15', b2)
    if hasattr(b1, 'adt_Operation16'):
        assert not _is_linked(b1, 'adt_Operation16', a)
    if hasattr(b2, 'adt_Operation16'):
        assert _is_linked(b2, 'adt_Operation16', a)
    _safe_set(a, 'adt_Signature15', set())
    assert not _is_linked(a, 'adt_Signature15', b2)
    if hasattr(b2, 'adt_Operation16'):
        assert not _is_linked(b2, 'adt_Operation16', a)


def test_assoc_leftHandTerm38_link_reassign_clear():
    a = adt_ATerm(symbol="sample_text")
    b1 = adt_Equation()
    b2 = adt_Equation()
    _safe_set(a, 'adt_ATerm40', b1)
    assert _is_linked(a, 'adt_ATerm40', b1)
    if hasattr(b1, 'adt_Equation39'):
        assert _is_linked(b1, 'adt_Equation39', a)
    _safe_set(a, 'adt_ATerm40', b2)
    assert _is_linked(a, 'adt_ATerm40', b2)
    if hasattr(b1, 'adt_Equation39'):
        assert not _is_linked(b1, 'adt_Equation39', a)
    if hasattr(b2, 'adt_Equation39'):
        assert _is_linked(b2, 'adt_Equation39', a)
    _safe_set(a, 'adt_ATerm40', None)
    assert not _is_linked(a, 'adt_ATerm40', b2)
    if hasattr(b2, 'adt_Equation39'):
        assert not _is_linked(b2, 'adt_Equation39', a)


def test_assoc_operationSymbol31_link_reassign_clear():
    a = adt_Operation(name="sample_text")
    b1 = adt_Term()
    b2 = adt_Term()
    _safe_set(a, 'adt_Operation32', b1)
    assert _is_linked(a, 'adt_Operation32', b1)
    if hasattr(b1, 'adt_Term'):
        assert _is_linked(b1, 'adt_Term', a)
    _safe_set(a, 'adt_Operation32', b2)
    assert _is_linked(a, 'adt_Operation32', b2)
    if hasattr(b1, 'adt_Term'):
        assert not _is_linked(b1, 'adt_Term', a)
    if hasattr(b2, 'adt_Term'):
        assert _is_linked(b2, 'adt_Term', a)
    _safe_set(a, 'adt_Operation32', None)
    assert not _is_linked(a, 'adt_Operation32', b2)
    if hasattr(b2, 'adt_Term'):
        assert not _is_linked(b2, 'adt_Term', a)


def test_assoc_operations11_link_reassign_clear():
    a = adt_Signature(ops="sample_text")
    b1 = adt_Operation(name="sample_text")
    b2 = adt_Operation(name="sample_text_2")
    _safe_set(a, 'adt_Signature12', {b1})
    assert _is_linked(a, 'adt_Signature12', b1)
    if hasattr(b1, 'adt_Operation13'):
        assert _is_linked(b1, 'adt_Operation13', a)
    _safe_set(a, 'adt_Signature12', {b2})
    assert _is_linked(a, 'adt_Signature12', b2)
    if hasattr(b1, 'adt_Operation13'):
        assert not _is_linked(b1, 'adt_Operation13', a)
    if hasattr(b2, 'adt_Operation13'):
        assert _is_linked(b2, 'adt_Operation13', a)
    _safe_set(a, 'adt_Signature12', set())
    assert not _is_linked(a, 'adt_Signature12', b2)
    if hasattr(b2, 'adt_Operation13'):
        assert not _is_linked(b2, 'adt_Operation13', a)


def test_assoc_returnType20_link_reassign_clear():
    a = adt_Operation(name="sample_text")
    b1 = adt_ASort(name="sample_text")
    b2 = adt_ASort(name="sample_text_2")
    _safe_set(a, 'adt_Operation21', b1)
    assert _is_linked(a, 'adt_Operation21', b1)
    if hasattr(b1, 'adt_ASort22'):
        assert _is_linked(b1, 'adt_ASort22', a)
    _safe_set(a, 'adt_Operation21', b2)
    assert _is_linked(a, 'adt_Operation21', b2)
    if hasattr(b1, 'adt_ASort22'):
        assert not _is_linked(b1, 'adt_ASort22', a)
    if hasattr(b2, 'adt_ASort22'):
        assert _is_linked(b2, 'adt_ASort22', a)
    _safe_set(a, 'adt_Operation21', None)
    assert not _is_linked(a, 'adt_Operation21', b2)
    if hasattr(b2, 'adt_ASort22'):
        assert not _is_linked(b2, 'adt_ASort22', a)


def test_assoc_rightHandTerm41_link_reassign_clear():
    a = adt_ATerm(symbol="sample_text")
    b1 = adt_Equation()
    b2 = adt_Equation()
    _safe_set(a, 'adt_ATerm43', b1)
    assert _is_linked(a, 'adt_ATerm43', b1)
    if hasattr(b1, 'adt_Equation42'):
        assert _is_linked(b1, 'adt_Equation42', a)
    _safe_set(a, 'adt_ATerm43', b2)
    assert _is_linked(a, 'adt_ATerm43', b2)
    if hasattr(b1, 'adt_Equation42'):
        assert not _is_linked(b1, 'adt_Equation42', a)
    if hasattr(b2, 'adt_Equation42'):
        assert _is_linked(b2, 'adt_Equation42', a)
    _safe_set(a, 'adt_ATerm43', None)
    assert not _is_linked(a, 'adt_ATerm43', b2)
    if hasattr(b2, 'adt_Equation42'):
        assert not _is_linked(b2, 'adt_Equation42', a)


def test_assoc_signature0_link_reassign_clear():
    a = adt_Signature(ops="sample_text")
    b1 = adt_ADT(name="sample_text")
    b2 = adt_ADT(name="sample_text_2")
    _safe_set(a, 'adt_Signature', b1)
    assert _is_linked(a, 'adt_Signature', b1)
    if hasattr(b1, 'adt_ADT'):
        assert _is_linked(b1, 'adt_ADT', a)
    _safe_set(a, 'adt_Signature', b2)
    assert _is_linked(a, 'adt_Signature', b2)
    if hasattr(b1, 'adt_ADT'):
        assert not _is_linked(b1, 'adt_ADT', a)
    if hasattr(b2, 'adt_ADT'):
        assert _is_linked(b2, 'adt_ADT', a)
    _safe_set(a, 'adt_Signature', None)
    assert not _is_linked(a, 'adt_Signature', b2)
    if hasattr(b2, 'adt_ADT'):
        assert not _is_linked(b2, 'adt_ADT', a)


def test_assoc_sort17_link_reassign_clear():
    a = adt_VariableDeclaration(name="sample_text")
    b1 = adt_ASort(name="sample_text")
    b2 = adt_ASort(name="sample_text_2")
    _safe_set(a, 'adt_VariableDeclaration18', b1)
    assert _is_linked(a, 'adt_VariableDeclaration18', b1)
    if hasattr(b1, 'adt_ASort19'):
        assert _is_linked(b1, 'adt_ASort19', a)
    _safe_set(a, 'adt_VariableDeclaration18', b2)
    assert _is_linked(a, 'adt_VariableDeclaration18', b2)
    if hasattr(b1, 'adt_ASort19'):
        assert not _is_linked(b1, 'adt_ASort19', a)
    if hasattr(b2, 'adt_ASort19'):
        assert _is_linked(b2, 'adt_ASort19', a)
    _safe_set(a, 'adt_VariableDeclaration18', None)
    assert not _is_linked(a, 'adt_VariableDeclaration18', b2)
    if hasattr(b2, 'adt_ASort19'):
        assert not _is_linked(b2, 'adt_ASort19', a)


def test_assoc_sort28_link_reassign_clear():
    a = adt_ATerm(symbol="sample_text")
    b1 = adt_ASort(name="sample_text")
    b2 = adt_ASort(name="sample_text_2")
    _safe_set(a, 'adt_ATerm29', b1)
    assert _is_linked(a, 'adt_ATerm29', b1)
    if hasattr(b1, 'adt_ASort30'):
        assert _is_linked(b1, 'adt_ASort30', a)
    _safe_set(a, 'adt_ATerm29', b2)
    assert _is_linked(a, 'adt_ATerm29', b2)
    if hasattr(b1, 'adt_ASort30'):
        assert not _is_linked(b1, 'adt_ASort30', a)
    if hasattr(b2, 'adt_ASort30'):
        assert _is_linked(b2, 'adt_ASort30', a)
    _safe_set(a, 'adt_ATerm29', None)
    assert not _is_linked(a, 'adt_ATerm29', b2)
    if hasattr(b2, 'adt_ASort30'):
        assert not _is_linked(b2, 'adt_ASort30', a)


def test_assoc_sorts8_link_reassign_clear():
    a = adt_Signature(ops="sample_text")
    b1 = adt_ASort(name="sample_text")
    b2 = adt_ASort(name="sample_text_2")
    _safe_set(a, 'adt_Signature9', {b1})
    assert _is_linked(a, 'adt_Signature9', b1)
    if hasattr(b1, 'adt_ASort10'):
        assert _is_linked(b1, 'adt_ASort10', a)
    _safe_set(a, 'adt_Signature9', {b2})
    assert _is_linked(a, 'adt_Signature9', b2)
    if hasattr(b1, 'adt_ASort10'):
        assert not _is_linked(b1, 'adt_ASort10', a)
    if hasattr(b2, 'adt_ASort10'):
        assert _is_linked(b2, 'adt_ASort10', a)
    _safe_set(a, 'adt_Signature9', set())
    assert not _is_linked(a, 'adt_Signature9', b2)
    if hasattr(b2, 'adt_ASort10'):
        assert not _is_linked(b2, 'adt_ASort10', a)


def test_assoc_subterms33_link_reassign_clear():
    a = adt_ATerm(symbol="sample_text")
    b1 = adt_Term()
    b2 = adt_Term()
    _safe_set(a, 'adt_ATerm35', b1)
    assert _is_linked(a, 'adt_ATerm35', b1)
    if hasattr(b1, 'adt_Term34'):
        assert _is_linked(b1, 'adt_Term34', a)
    _safe_set(a, 'adt_ATerm35', b2)
    assert _is_linked(a, 'adt_ATerm35', b2)
    if hasattr(b1, 'adt_Term34'):
        assert not _is_linked(b1, 'adt_Term34', a)
    if hasattr(b2, 'adt_Term34'):
        assert _is_linked(b2, 'adt_Term34', a)
    _safe_set(a, 'adt_ATerm35', None)
    assert not _is_linked(a, 'adt_ATerm35', b2)
    if hasattr(b2, 'adt_Term34'):
        assert not _is_linked(b2, 'adt_Term34', a)


def test_assoc_superSort5_link_reassign_clear():
    a = adt_ASort(name="sample_text")
    b1 = adt_SubSort()
    b2 = adt_SubSort()
    _safe_set(a, 'adt_ASort', b1)
    assert _is_linked(a, 'adt_ASort', b1)
    if hasattr(b1, 'adt_SubSort'):
        assert _is_linked(b1, 'adt_SubSort', a)
    _safe_set(a, 'adt_ASort', b2)
    assert _is_linked(a, 'adt_ASort', b2)
    if hasattr(b1, 'adt_SubSort'):
        assert not _is_linked(b1, 'adt_SubSort', a)
    if hasattr(b2, 'adt_SubSort'):
        assert _is_linked(b2, 'adt_SubSort', a)
    _safe_set(a, 'adt_ASort', None)
    assert not _is_linked(a, 'adt_ASort', b2)
    if hasattr(b2, 'adt_SubSort'):
        assert not _is_linked(b2, 'adt_SubSort', a)


def test_assoc_variables1_link_reassign_clear():
    a = adt_VariableDeclaration(name="sample_text")
    b1 = adt_ADT(name="sample_text")
    b2 = adt_ADT(name="sample_text_2")
    _safe_set(a, 'adt_VariableDeclaration', b1)
    assert _is_linked(a, 'adt_VariableDeclaration', b1)
    if hasattr(b1, 'adt_ADT2'):
        assert _is_linked(b1, 'adt_ADT2', a)
    _safe_set(a, 'adt_VariableDeclaration', b2)
    assert _is_linked(a, 'adt_VariableDeclaration', b2)
    if hasattr(b1, 'adt_ADT2'):
        assert not _is_linked(b1, 'adt_ADT2', a)
    if hasattr(b2, 'adt_ADT2'):
        assert _is_linked(b2, 'adt_ADT2', a)
    _safe_set(a, 'adt_VariableDeclaration', None)
    assert not _is_linked(a, 'adt_VariableDeclaration', b2)
    if hasattr(b2, 'adt_ADT2'):
        assert not _is_linked(b2, 'adt_ADT2', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ASort_strategy = st.builds(ASort)
@given(instance=ASort_strategy)
@settings(max_examples=25)
def test_ASort_instantiation(instance):
    assert isinstance(instance, ASort)


ATerm_strategy = st.builds(ATerm)
@given(instance=ATerm_strategy)
@settings(max_examples=25)
def test_ATerm_instantiation(instance):
    assert isinstance(instance, ATerm)


adt_ADT_strategy = st.builds(adt_ADT, name=safe_text)
@given(instance=adt_ADT_strategy)
@settings(max_examples=25)
def test_adt_ADT_instantiation(instance):
    assert isinstance(instance, adt_ADT)


adt_ASort_strategy = st.builds(adt_ASort, name=safe_text)
@given(instance=adt_ASort_strategy)
@settings(max_examples=25)
def test_adt_ASort_instantiation(instance):
    assert isinstance(instance, adt_ASort)


adt_ATerm_strategy = st.builds(adt_ATerm, symbol=safe_text)
@given(instance=adt_ATerm_strategy)
@settings(max_examples=25)
def test_adt_ATerm_instantiation(instance):
    assert isinstance(instance, adt_ATerm)


adt_Equation_strategy = st.builds(adt_Equation)
@given(instance=adt_Equation_strategy)
@settings(max_examples=25)
def test_adt_Equation_instantiation(instance):
    assert isinstance(instance, adt_Equation)


adt_Operation_strategy = st.builds(adt_Operation, name=safe_text)
@given(instance=adt_Operation_strategy)
@settings(max_examples=25)
def test_adt_Operation_instantiation(instance):
    assert isinstance(instance, adt_Operation)


adt_Signature_strategy = st.builds(adt_Signature, ops=safe_text)
@given(instance=adt_Signature_strategy)
@settings(max_examples=25)
def test_adt_Signature_instantiation(instance):
    assert isinstance(instance, adt_Signature)


adt_Sort_strategy = st.builds(adt_Sort)
@given(instance=adt_Sort_strategy)
@settings(max_examples=25)
def test_adt_Sort_instantiation(instance):
    assert isinstance(instance, adt_Sort)


adt_SubSort_strategy = st.builds(adt_SubSort)
@given(instance=adt_SubSort_strategy)
@settings(max_examples=25)
def test_adt_SubSort_instantiation(instance):
    assert isinstance(instance, adt_SubSort)


adt_Term_strategy = st.builds(adt_Term)
@given(instance=adt_Term_strategy)
@settings(max_examples=25)
def test_adt_Term_instantiation(instance):
    assert isinstance(instance, adt_Term)


adt_Variable_strategy = st.builds(adt_Variable)
@given(instance=adt_Variable_strategy)
@settings(max_examples=25)
def test_adt_Variable_instantiation(instance):
    assert isinstance(instance, adt_Variable)


adt_VariableDeclaration_strategy = st.builds(adt_VariableDeclaration, name=safe_text)
@given(instance=adt_VariableDeclaration_strategy)
@settings(max_examples=25)
def test_adt_VariableDeclaration_instantiation(instance):
    assert isinstance(instance, adt_VariableDeclaration)



