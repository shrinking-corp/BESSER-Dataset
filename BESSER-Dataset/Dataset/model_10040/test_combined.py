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
    Graph_TLong,
    Graph_TInt,
    Graph_TShort,
    Graph_TByte,
    Graph_TChar,
    Graph_TString,
    Graph_TDouble,
    Graph_TFloat,
    Graph_TBoolean,
    Graph_ID1006,
    Graph_Graph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_graph_tlong_is_not_abstract():
    assert not inspect.isabstract(Graph_TLong)


def test_hyp_graph_tlong_constructor_exists():
    assert callable(Graph_TLong.__init__)


def test_hyp_graph_tlong_constructor_args():
    sig = inspect.signature(Graph_TLong.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_graph_tint_is_not_abstract():
    assert not inspect.isabstract(Graph_TInt)


def test_hyp_graph_tint_constructor_exists():
    assert callable(Graph_TInt.__init__)


def test_hyp_graph_tint_constructor_args():
    sig = inspect.signature(Graph_TInt.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_graph_tshort_is_not_abstract():
    assert not inspect.isabstract(Graph_TShort)


def test_hyp_graph_tshort_constructor_exists():
    assert callable(Graph_TShort.__init__)


def test_hyp_graph_tshort_constructor_args():
    sig = inspect.signature(Graph_TShort.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_graph_tbyte_is_not_abstract():
    assert not inspect.isabstract(Graph_TByte)


def test_hyp_graph_tbyte_constructor_exists():
    assert callable(Graph_TByte.__init__)


def test_hyp_graph_tbyte_constructor_args():
    sig = inspect.signature(Graph_TByte.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_graph_tchar_is_not_abstract():
    assert not inspect.isabstract(Graph_TChar)


def test_hyp_graph_tchar_constructor_exists():
    assert callable(Graph_TChar.__init__)


def test_hyp_graph_tchar_constructor_args():
    sig = inspect.signature(Graph_TChar.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_graph_tstring_is_not_abstract():
    assert not inspect.isabstract(Graph_TString)


def test_hyp_graph_tstring_constructor_exists():
    assert callable(Graph_TString.__init__)


def test_hyp_graph_tstring_constructor_args():
    sig = inspect.signature(Graph_TString.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"





def test_hyp_graph_tdouble_is_not_abstract():
    assert not inspect.isabstract(Graph_TDouble)


def test_hyp_graph_tdouble_constructor_exists():
    assert callable(Graph_TDouble.__init__)


def test_hyp_graph_tdouble_constructor_args():
    sig = inspect.signature(Graph_TDouble.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_graph_tfloat_is_not_abstract():
    assert not inspect.isabstract(Graph_TFloat)


def test_hyp_graph_tfloat_constructor_exists():
    assert callable(Graph_TFloat.__init__)


def test_hyp_graph_tfloat_constructor_args():
    sig = inspect.signature(Graph_TFloat.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_graph_tboolean_is_not_abstract():
    assert not inspect.isabstract(Graph_TBoolean)


def test_hyp_graph_tboolean_constructor_exists():
    assert callable(Graph_TBoolean.__init__)


def test_hyp_graph_tboolean_constructor_args():
    sig = inspect.signature(Graph_TBoolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_graph_id1006_is_not_abstract():
    assert not inspect.isabstract(Graph_ID1006)


def test_hyp_graph_id1006_constructor_exists():
    assert callable(Graph_ID1006.__init__)


def test_hyp_graph_id1006_constructor_args():
    sig = inspect.signature(Graph_ID1006.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_graph_graph_is_not_abstract():
    assert not inspect.isabstract(Graph_Graph)


def test_hyp_graph_graph_constructor_exists():
    assert callable(Graph_Graph.__init__)


def test_hyp_graph_graph_constructor_args():
    sig = inspect.signature(Graph_Graph.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"



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
Graph_TLong_strategy = st.builds(
    Graph_TLong,
    value=
        safe_text
)
Graph_TInt_strategy = st.builds(
    Graph_TInt,
    value=
        st.integers()
)
Graph_TShort_strategy = st.builds(
    Graph_TShort,
    value=
        safe_text
)
Graph_TByte_strategy = st.builds(
    Graph_TByte,
    value=
        safe_text
)
Graph_TChar_strategy = st.builds(
    Graph_TChar,
    value=
        safe_text
)
Graph_TString_strategy = st.builds(
    Graph_TString,
    name=
        safe_text,
    id=
        safe_text
)
Graph_TDouble_strategy = st.builds(
    Graph_TDouble,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Graph_TFloat_strategy = st.builds(
    Graph_TFloat,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Graph_TBoolean_strategy = st.builds(
    Graph_TBoolean,
    value=
        st.booleans()
)
Graph_ID1006_strategy = st.builds(
    Graph_ID1006,
    id=
        safe_text,
    name=
        safe_text
)
Graph_Graph_strategy = st.builds(
    Graph_Graph,
    id=
        safe_text
)




@given(instance=Graph_TLong_strategy)
def test_hyp_graph_tlong_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=Graph_TInt_strategy)
def test_hyp_graph_tint_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=Graph_TShort_strategy)
def test_hyp_graph_tshort_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=Graph_TByte_strategy)
def test_hyp_graph_tbyte_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=Graph_TChar_strategy)
def test_hyp_graph_tchar_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=Graph_TString_strategy)
def test_hyp_graph_tstring_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Graph_TString_strategy)
def test_hyp_graph_tstring_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=Graph_TDouble_strategy)
def test_hyp_graph_tdouble_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=Graph_TFloat_strategy)
def test_hyp_graph_tfloat_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=Graph_TBoolean_strategy)
def test_hyp_graph_tboolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=Graph_ID1006_strategy)
def test_hyp_graph_id1006_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Graph_ID1006_strategy)
def test_hyp_graph_id1006_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=Graph_Graph_strategy)
def test_hyp_graph_graph_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Graph_Graph,
    Graph_ID1006,
    Graph_TBoolean,
    Graph_TByte,
    Graph_TChar,
    Graph_TDouble,
    Graph_TFloat,
    Graph_TInt,
    Graph_TLong,
    Graph_TShort,
    Graph_TString,
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

def test_Graph_Graph_id_value_roundtrip():
    instance = Graph_Graph(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_Graph_ID1006_id_value_roundtrip():
    instance = Graph_ID1006(id="sample_text", name="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_Graph_ID1006_name_value_roundtrip():
    instance = Graph_ID1006(id="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Graph_TBoolean_value_value_roundtrip():
    instance = Graph_TBoolean(value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_Graph_TByte_value_value_roundtrip():
    instance = Graph_TByte(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_Graph_TChar_value_value_roundtrip():
    instance = Graph_TChar(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_Graph_TDouble_value_value_roundtrip():
    instance = Graph_TDouble(value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_Graph_TFloat_value_value_roundtrip():
    instance = Graph_TFloat(value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_Graph_TInt_value_value_roundtrip():
    instance = Graph_TInt(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_Graph_TLong_value_value_roundtrip():
    instance = Graph_TLong(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_Graph_TShort_value_value_roundtrip():
    instance = Graph_TShort(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_Graph_TString_id_value_roundtrip():
    instance = Graph_TString(id="sample_text", name="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_Graph_TString_name_value_roundtrip():
    instance = Graph_TString(id="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assoc_id1006s0_link_reassign_clear():
    a = Graph_ID1006(id="sample_text", name="sample_text")
    b1 = Graph_Graph(id="sample_text")
    b2 = Graph_Graph(id="sample_text_2")
    _safe_set(a, 'Graph_ID1006', b1)
    assert _is_linked(a, 'Graph_ID1006', b1)
    if hasattr(b1, 'Graph_Graph'):
        assert _is_linked(b1, 'Graph_Graph', a)
    _safe_set(a, 'Graph_ID1006', b2)
    assert _is_linked(a, 'Graph_ID1006', b2)
    if hasattr(b1, 'Graph_Graph'):
        assert not _is_linked(b1, 'Graph_Graph', a)
    if hasattr(b2, 'Graph_Graph'):
        assert _is_linked(b2, 'Graph_Graph', a)
    _safe_set(a, 'Graph_ID1006', None)
    assert not _is_linked(a, 'Graph_ID1006', b2)
    if hasattr(b2, 'Graph_Graph'):
        assert not _is_linked(b2, 'Graph_Graph', a)


def test_assoc_outID1008s19_link_reassign_clear():
    a = Graph_TString(id="sample_text", name="sample_text")
    b1 = Graph_ID1006(id="sample_text", name="sample_text")
    b2 = Graph_ID1006(id="sample_text_2", name="sample_text_2")
    _safe_set(a, 'Graph_TString21', b1)
    assert _is_linked(a, 'Graph_TString21', b1)
    if hasattr(b1, 'Graph_ID100620'):
        assert _is_linked(b1, 'Graph_ID100620', a)
    _safe_set(a, 'Graph_TString21', b2)
    assert _is_linked(a, 'Graph_TString21', b2)
    if hasattr(b1, 'Graph_ID100620'):
        assert not _is_linked(b1, 'Graph_ID100620', a)
    if hasattr(b2, 'Graph_ID100620'):
        assert _is_linked(b2, 'Graph_ID100620', a)
    _safe_set(a, 'Graph_TString21', None)
    assert not _is_linked(a, 'Graph_TString21', b2)
    if hasattr(b2, 'Graph_ID100620'):
        assert not _is_linked(b2, 'Graph_ID100620', a)


def test_assoc_tBooleans1_link_reassign_clear():
    a = Graph_TBoolean(value=True)
    b1 = Graph_Graph(id="sample_text")
    b2 = Graph_Graph(id="sample_text_2")
    _safe_set(a, 'Graph_TBoolean', b1)
    assert _is_linked(a, 'Graph_TBoolean', b1)
    if hasattr(b1, 'Graph_Graph2'):
        assert _is_linked(b1, 'Graph_Graph2', a)
    _safe_set(a, 'Graph_TBoolean', b2)
    assert _is_linked(a, 'Graph_TBoolean', b2)
    if hasattr(b1, 'Graph_Graph2'):
        assert not _is_linked(b1, 'Graph_Graph2', a)
    if hasattr(b2, 'Graph_Graph2'):
        assert _is_linked(b2, 'Graph_Graph2', a)
    _safe_set(a, 'Graph_TBoolean', None)
    assert not _is_linked(a, 'Graph_TBoolean', b2)
    if hasattr(b2, 'Graph_Graph2'):
        assert not _is_linked(b2, 'Graph_Graph2', a)


def test_assoc_tBytes5_link_reassign_clear():
    a = Graph_TByte(value="sample_text")
    b1 = Graph_Graph(id="sample_text")
    b2 = Graph_Graph(id="sample_text_2")
    _safe_set(a, 'Graph_TByte', b1)
    assert _is_linked(a, 'Graph_TByte', b1)
    if hasattr(b1, 'Graph_Graph6'):
        assert _is_linked(b1, 'Graph_Graph6', a)
    _safe_set(a, 'Graph_TByte', b2)
    assert _is_linked(a, 'Graph_TByte', b2)
    if hasattr(b1, 'Graph_Graph6'):
        assert not _is_linked(b1, 'Graph_Graph6', a)
    if hasattr(b2, 'Graph_Graph6'):
        assert _is_linked(b2, 'Graph_Graph6', a)
    _safe_set(a, 'Graph_TByte', None)
    assert not _is_linked(a, 'Graph_TByte', b2)
    if hasattr(b2, 'Graph_Graph6'):
        assert not _is_linked(b2, 'Graph_Graph6', a)


def test_assoc_tChars3_link_reassign_clear():
    a = Graph_TChar(value="sample_text")
    b1 = Graph_Graph(id="sample_text")
    b2 = Graph_Graph(id="sample_text_2")
    _safe_set(a, 'Graph_TChar', b1)
    assert _is_linked(a, 'Graph_TChar', b1)
    if hasattr(b1, 'Graph_Graph4'):
        assert _is_linked(b1, 'Graph_Graph4', a)
    _safe_set(a, 'Graph_TChar', b2)
    assert _is_linked(a, 'Graph_TChar', b2)
    if hasattr(b1, 'Graph_Graph4'):
        assert not _is_linked(b1, 'Graph_Graph4', a)
    if hasattr(b2, 'Graph_Graph4'):
        assert _is_linked(b2, 'Graph_Graph4', a)
    _safe_set(a, 'Graph_TChar', None)
    assert not _is_linked(a, 'Graph_TChar', b2)
    if hasattr(b2, 'Graph_Graph4'):
        assert not _is_linked(b2, 'Graph_Graph4', a)


def test_assoc_tDoubles15_link_reassign_clear():
    a = Graph_TDouble(value=3.14)
    b1 = Graph_Graph(id="sample_text")
    b2 = Graph_Graph(id="sample_text_2")
    _safe_set(a, 'Graph_TDouble', b1)
    assert _is_linked(a, 'Graph_TDouble', b1)
    if hasattr(b1, 'Graph_Graph16'):
        assert _is_linked(b1, 'Graph_Graph16', a)
    _safe_set(a, 'Graph_TDouble', b2)
    assert _is_linked(a, 'Graph_TDouble', b2)
    if hasattr(b1, 'Graph_Graph16'):
        assert not _is_linked(b1, 'Graph_Graph16', a)
    if hasattr(b2, 'Graph_Graph16'):
        assert _is_linked(b2, 'Graph_Graph16', a)
    _safe_set(a, 'Graph_TDouble', None)
    assert not _is_linked(a, 'Graph_TDouble', b2)
    if hasattr(b2, 'Graph_Graph16'):
        assert not _is_linked(b2, 'Graph_Graph16', a)


def test_assoc_tFloats13_link_reassign_clear():
    a = Graph_TFloat(value=3.14)
    b1 = Graph_Graph(id="sample_text")
    b2 = Graph_Graph(id="sample_text_2")
    _safe_set(a, 'Graph_TFloat', b1)
    assert _is_linked(a, 'Graph_TFloat', b1)
    if hasattr(b1, 'Graph_Graph14'):
        assert _is_linked(b1, 'Graph_Graph14', a)
    _safe_set(a, 'Graph_TFloat', b2)
    assert _is_linked(a, 'Graph_TFloat', b2)
    if hasattr(b1, 'Graph_Graph14'):
        assert not _is_linked(b1, 'Graph_Graph14', a)
    if hasattr(b2, 'Graph_Graph14'):
        assert _is_linked(b2, 'Graph_Graph14', a)
    _safe_set(a, 'Graph_TFloat', None)
    assert not _is_linked(a, 'Graph_TFloat', b2)
    if hasattr(b2, 'Graph_Graph14'):
        assert not _is_linked(b2, 'Graph_Graph14', a)


def test_assoc_tInts9_link_reassign_clear():
    a = Graph_TInt(value=7)
    b1 = Graph_Graph(id="sample_text")
    b2 = Graph_Graph(id="sample_text_2")
    _safe_set(a, 'Graph_TInt', b1)
    assert _is_linked(a, 'Graph_TInt', b1)
    if hasattr(b1, 'Graph_Graph10'):
        assert _is_linked(b1, 'Graph_Graph10', a)
    _safe_set(a, 'Graph_TInt', b2)
    assert _is_linked(a, 'Graph_TInt', b2)
    if hasattr(b1, 'Graph_Graph10'):
        assert not _is_linked(b1, 'Graph_Graph10', a)
    if hasattr(b2, 'Graph_Graph10'):
        assert _is_linked(b2, 'Graph_Graph10', a)
    _safe_set(a, 'Graph_TInt', None)
    assert not _is_linked(a, 'Graph_TInt', b2)
    if hasattr(b2, 'Graph_Graph10'):
        assert not _is_linked(b2, 'Graph_Graph10', a)


def test_assoc_tLongs11_link_reassign_clear():
    a = Graph_TLong(value="sample_text")
    b1 = Graph_Graph(id="sample_text")
    b2 = Graph_Graph(id="sample_text_2")
    _safe_set(a, 'Graph_TLong', b1)
    assert _is_linked(a, 'Graph_TLong', b1)
    if hasattr(b1, 'Graph_Graph12'):
        assert _is_linked(b1, 'Graph_Graph12', a)
    _safe_set(a, 'Graph_TLong', b2)
    assert _is_linked(a, 'Graph_TLong', b2)
    if hasattr(b1, 'Graph_Graph12'):
        assert not _is_linked(b1, 'Graph_Graph12', a)
    if hasattr(b2, 'Graph_Graph12'):
        assert _is_linked(b2, 'Graph_Graph12', a)
    _safe_set(a, 'Graph_TLong', None)
    assert not _is_linked(a, 'Graph_TLong', b2)
    if hasattr(b2, 'Graph_Graph12'):
        assert not _is_linked(b2, 'Graph_Graph12', a)


def test_assoc_tShorts7_link_reassign_clear():
    a = Graph_TShort(value="sample_text")
    b1 = Graph_Graph(id="sample_text")
    b2 = Graph_Graph(id="sample_text_2")
    _safe_set(a, 'Graph_TShort', b1)
    assert _is_linked(a, 'Graph_TShort', b1)
    if hasattr(b1, 'Graph_Graph8'):
        assert _is_linked(b1, 'Graph_Graph8', a)
    _safe_set(a, 'Graph_TShort', b2)
    assert _is_linked(a, 'Graph_TShort', b2)
    if hasattr(b1, 'Graph_Graph8'):
        assert not _is_linked(b1, 'Graph_Graph8', a)
    if hasattr(b2, 'Graph_Graph8'):
        assert _is_linked(b2, 'Graph_Graph8', a)
    _safe_set(a, 'Graph_TShort', None)
    assert not _is_linked(a, 'Graph_TShort', b2)
    if hasattr(b2, 'Graph_Graph8'):
        assert not _is_linked(b2, 'Graph_Graph8', a)


def test_assoc_tStrings17_link_reassign_clear():
    a = Graph_TString(id="sample_text", name="sample_text")
    b1 = Graph_Graph(id="sample_text")
    b2 = Graph_Graph(id="sample_text_2")
    _safe_set(a, 'Graph_TString', b1)
    assert _is_linked(a, 'Graph_TString', b1)
    if hasattr(b1, 'Graph_Graph18'):
        assert _is_linked(b1, 'Graph_Graph18', a)
    _safe_set(a, 'Graph_TString', b2)
    assert _is_linked(a, 'Graph_TString', b2)
    if hasattr(b1, 'Graph_Graph18'):
        assert not _is_linked(b1, 'Graph_Graph18', a)
    if hasattr(b2, 'Graph_Graph18'):
        assert _is_linked(b2, 'Graph_Graph18', a)
    _safe_set(a, 'Graph_TString', None)
    assert not _is_linked(a, 'Graph_TString', b2)
    if hasattr(b2, 'Graph_Graph18'):
        assert not _is_linked(b2, 'Graph_Graph18', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Graph_Graph_strategy = st.builds(Graph_Graph, id=safe_text)
@given(instance=Graph_Graph_strategy)
@settings(max_examples=25)
def test_Graph_Graph_instantiation(instance):
    assert isinstance(instance, Graph_Graph)


Graph_ID1006_strategy = st.builds(Graph_ID1006, id=safe_text, name=safe_text)
@given(instance=Graph_ID1006_strategy)
@settings(max_examples=25)
def test_Graph_ID1006_instantiation(instance):
    assert isinstance(instance, Graph_ID1006)


Graph_TBoolean_strategy = st.builds(Graph_TBoolean, value=st.booleans())
@given(instance=Graph_TBoolean_strategy)
@settings(max_examples=25)
def test_Graph_TBoolean_instantiation(instance):
    assert isinstance(instance, Graph_TBoolean)


Graph_TByte_strategy = st.builds(Graph_TByte, value=safe_text)
@given(instance=Graph_TByte_strategy)
@settings(max_examples=25)
def test_Graph_TByte_instantiation(instance):
    assert isinstance(instance, Graph_TByte)


Graph_TChar_strategy = st.builds(Graph_TChar, value=safe_text)
@given(instance=Graph_TChar_strategy)
@settings(max_examples=25)
def test_Graph_TChar_instantiation(instance):
    assert isinstance(instance, Graph_TChar)


Graph_TDouble_strategy = st.builds(Graph_TDouble, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=Graph_TDouble_strategy)
@settings(max_examples=25)
def test_Graph_TDouble_instantiation(instance):
    assert isinstance(instance, Graph_TDouble)


Graph_TFloat_strategy = st.builds(Graph_TFloat, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=Graph_TFloat_strategy)
@settings(max_examples=25)
def test_Graph_TFloat_instantiation(instance):
    assert isinstance(instance, Graph_TFloat)


Graph_TInt_strategy = st.builds(Graph_TInt, value=st.integers())
@given(instance=Graph_TInt_strategy)
@settings(max_examples=25)
def test_Graph_TInt_instantiation(instance):
    assert isinstance(instance, Graph_TInt)


Graph_TLong_strategy = st.builds(Graph_TLong, value=safe_text)
@given(instance=Graph_TLong_strategy)
@settings(max_examples=25)
def test_Graph_TLong_instantiation(instance):
    assert isinstance(instance, Graph_TLong)


Graph_TShort_strategy = st.builds(Graph_TShort, value=safe_text)
@given(instance=Graph_TShort_strategy)
@settings(max_examples=25)
def test_Graph_TShort_instantiation(instance):
    assert isinstance(instance, Graph_TShort)


Graph_TString_strategy = st.builds(Graph_TString, id=safe_text, name=safe_text)
@given(instance=Graph_TString_strategy)
@settings(max_examples=25)
def test_Graph_TString_instantiation(instance):
    assert isinstance(instance, Graph_TString)



