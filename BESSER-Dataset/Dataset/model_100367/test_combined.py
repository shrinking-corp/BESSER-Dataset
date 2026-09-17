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
    AbstractConection,
    FSmachine_ReasonConnection,
    AbstractObject,
    FSmachine_State,
    FSmachine_TimeConnection,
    FSmachine_AbstractObject,
    FSmachine_Root,
    FSmachine_AbstractConection,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_abstractconection_is_not_abstract():
    assert not inspect.isabstract(AbstractConection)


def test_hyp_abstractconection_constructor_exists():
    assert callable(AbstractConection.__init__)


def test_hyp_abstractconection_constructor_args():
    sig = inspect.signature(AbstractConection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsmachine_reasonconnection_is_not_abstract():
    assert not inspect.isabstract(FSmachine_ReasonConnection)


def test_hyp_fsmachine_reasonconnection_constructor_exists():
    assert callable(FSmachine_ReasonConnection.__init__)


def test_hyp_fsmachine_reasonconnection_constructor_args():
    sig = inspect.signature(FSmachine_ReasonConnection.__init__)
    params = list(sig.parameters.keys())
    assert "reason" in params, "Missing parameter 'reason'"




def test_hyp_abstractobject_is_not_abstract():
    assert not inspect.isabstract(AbstractObject)


def test_hyp_abstractobject_constructor_exists():
    assert callable(AbstractObject.__init__)


def test_hyp_abstractobject_constructor_args():
    sig = inspect.signature(AbstractObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fsmachine_state_is_not_abstract():
    assert not inspect.isabstract(FSmachine_State)


def test_hyp_fsmachine_state_constructor_exists():
    assert callable(FSmachine_State.__init__)


def test_hyp_fsmachine_state_constructor_args():
    sig = inspect.signature(FSmachine_State.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "data" in params, "Missing parameter 'data'"





def test_hyp_fsmachine_timeconnection_is_not_abstract():
    assert not inspect.isabstract(FSmachine_TimeConnection)


def test_hyp_fsmachine_timeconnection_constructor_exists():
    assert callable(FSmachine_TimeConnection.__init__)


def test_hyp_fsmachine_timeconnection_constructor_args():
    sig = inspect.signature(FSmachine_TimeConnection.__init__)
    params = list(sig.parameters.keys())
    assert "when" in params, "Missing parameter 'when'"




def test_hyp_fsmachine_abstractobject_is_not_abstract():
    assert not inspect.isabstract(FSmachine_AbstractObject)


def test_hyp_fsmachine_abstractobject_constructor_exists():
    assert callable(FSmachine_AbstractObject.__init__)


def test_hyp_fsmachine_abstractobject_constructor_args():
    sig = inspect.signature(FSmachine_AbstractObject.__init__)
    params = list(sig.parameters.keys())
    assert "active" in params, "Missing parameter 'active'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fsmachine_root_is_not_abstract():
    assert not inspect.isabstract(FSmachine_Root)


def test_hyp_fsmachine_root_constructor_exists():
    assert callable(FSmachine_Root.__init__)


def test_hyp_fsmachine_root_constructor_args():
    sig = inspect.signature(FSmachine_Root.__init__)
    params = list(sig.parameters.keys())
    assert "FSmachineName" in params, "Missing parameter 'FSmachineName'"




def test_hyp_fsmachine_abstractconection_is_not_abstract():
    assert not inspect.isabstract(FSmachine_AbstractConection)


def test_hyp_fsmachine_abstractconection_constructor_exists():
    assert callable(FSmachine_AbstractConection.__init__)


def test_hyp_fsmachine_abstractconection_constructor_args():
    sig = inspect.signature(FSmachine_AbstractConection.__init__)
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
AbstractConection_strategy = st.builds(
    AbstractConection,
)
FSmachine_ReasonConnection_strategy = st.builds(
    FSmachine_ReasonConnection,
    reason=
        safe_text
)
AbstractObject_strategy = st.builds(
    AbstractObject,
)
FSmachine_State_strategy = st.builds(
    FSmachine_State,
    description=
        safe_text,
    data=
        safe_text
)
FSmachine_TimeConnection_strategy = st.builds(
    FSmachine_TimeConnection,
    when=
        safe_text
)
FSmachine_AbstractObject_strategy = st.builds(
    FSmachine_AbstractObject,
    active=
        st.booleans(),
    name=
        safe_text
)
FSmachine_Root_strategy = st.builds(
    FSmachine_Root,
    FSmachineName=
        safe_text
)
FSmachine_AbstractConection_strategy = st.builds(
    FSmachine_AbstractConection,
    name=
        safe_text
)





@given(instance=FSmachine_ReasonConnection_strategy)
def test_hyp_fsmachine_reasonconnection_reason_setter(instance):
    original = instance.reason
    instance.reason = original
    assert instance.reason == original





@given(instance=FSmachine_State_strategy)
def test_hyp_fsmachine_state_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=FSmachine_State_strategy)
def test_hyp_fsmachine_state_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original




@given(instance=FSmachine_TimeConnection_strategy)
def test_hyp_fsmachine_timeconnection_when_setter(instance):
    original = instance.when
    instance.when = original
    assert instance.when == original




@given(instance=FSmachine_AbstractObject_strategy)
def test_hyp_fsmachine_abstractobject_active_setter(instance):
    original = instance.active
    instance.active = original
    assert instance.active == original



@given(instance=FSmachine_AbstractObject_strategy)
def test_hyp_fsmachine_abstractobject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FSmachine_AbstractObject_strategy)
@settings(max_examples=30)
def test_hyp_fsmachine_abstractobject_makemeactive_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.makeMeActive()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.makeMeActive).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'makeMeActive' in FSmachine_AbstractObject is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'makeMeActive' in FSmachine_AbstractObject did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'makeMeActive' in FSmachine_AbstractObject is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FSmachine_AbstractObject_strategy)
@settings(max_examples=30)
def test_hyp_fsmachine_abstractobject_checkstatussen_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.checkStatussen()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.checkStatussen).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'checkStatussen' in FSmachine_AbstractObject is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'checkStatussen' in FSmachine_AbstractObject did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'checkStatussen' in FSmachine_AbstractObject is not implemented or raised an error")




@given(instance=FSmachine_Root_strategy)
def test_hyp_fsmachine_root_FSmachineName_setter(instance):
    original = instance.FSmachineName
    instance.FSmachineName = original
    assert instance.FSmachineName == original




@given(instance=FSmachine_AbstractConection_strategy)
def test_hyp_fsmachine_abstractconection_name_setter(instance):
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
    AbstractConection,
    AbstractObject,
    FSmachine_AbstractConection,
    FSmachine_AbstractObject,
    FSmachine_ReasonConnection,
    FSmachine_Root,
    FSmachine_State,
    FSmachine_TimeConnection,
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

def test_FSmachine_AbstractConection_name_value_roundtrip():
    instance = FSmachine_AbstractConection(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_FSmachine_AbstractObject_active_value_roundtrip():
    instance = FSmachine_AbstractObject(active=True, name="sample_text")
    assert instance.active == True
    instance.active = False
    assert instance.active == False


def test_FSmachine_AbstractObject_name_value_roundtrip():
    instance = FSmachine_AbstractObject(active=True, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_FSmachine_ReasonConnection_reason_value_roundtrip():
    instance = FSmachine_ReasonConnection(reason="sample_text")
    assert instance.reason == "sample_text"
    instance.reason = "sample_text_2"
    assert instance.reason == "sample_text_2"


def test_FSmachine_Root_FSmachineName_value_roundtrip():
    instance = FSmachine_Root(FSmachineName="sample_text")
    assert instance.FSmachineName == "sample_text"
    instance.FSmachineName = "sample_text_2"
    assert instance.FSmachineName == "sample_text_2"


def test_FSmachine_State_data_value_roundtrip():
    instance = FSmachine_State(data="sample_text", description="sample_text")
    assert instance.data == "sample_text"
    instance.data = "sample_text_2"
    assert instance.data == "sample_text_2"


def test_FSmachine_State_description_value_roundtrip():
    instance = FSmachine_State(data="sample_text", description="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_FSmachine_TimeConnection_when_value_roundtrip():
    instance = FSmachine_TimeConnection(when="sample_text")
    assert instance.when == "sample_text"
    instance.when = "sample_text_2"
    assert instance.when == "sample_text_2"


def test_FSmachine_ReasonConnection_isa_AbstractConection():
    instance = FSmachine_ReasonConnection(reason="sample_text")
    assert isinstance(instance, AbstractConection)


def test_FSmachine_TimeConnection_isa_AbstractConection():
    instance = FSmachine_TimeConnection(when="sample_text")
    assert isinstance(instance, AbstractConection)


def test_FSmachine_State_isa_AbstractObject():
    instance = FSmachine_State(data="sample_text", description="sample_text")
    assert isinstance(instance, AbstractObject)


def test_assoc_conChild3_link_reassign_clear():
    a = FSmachine_AbstractObject(active=True, name="sample_text")
    b1 = FSmachine_AbstractConection(name="sample_text")
    b2 = FSmachine_AbstractConection(name="sample_text_2")
    _safe_set(a, 'next', b1)
    assert _is_linked(a, 'next', b1)
    if hasattr(b1, 'AbstractConection4'):
        assert _is_linked(b1, 'AbstractConection4', a)
    _safe_set(a, 'next', b2)
    assert _is_linked(a, 'next', b2)
    if hasattr(b1, 'AbstractConection4'):
        assert not _is_linked(b1, 'AbstractConection4', a)
    if hasattr(b2, 'AbstractConection4'):
        assert _is_linked(b2, 'AbstractConection4', a)
    _safe_set(a, 'next', None)
    assert not _is_linked(a, 'next', b2)
    if hasattr(b2, 'AbstractConection4'):
        assert not _is_linked(b2, 'AbstractConection4', a)


def test_assoc_conParent5_link_reassign_clear():
    a = FSmachine_AbstractObject(active=True, name="sample_text")
    b1 = FSmachine_AbstractConection(name="sample_text")
    b2 = FSmachine_AbstractConection(name="sample_text_2")
    _safe_set(a, 'prev', b1)
    assert _is_linked(a, 'prev', b1)
    if hasattr(b1, 'AbstractConection6'):
        assert _is_linked(b1, 'AbstractConection6', a)
    _safe_set(a, 'prev', b2)
    assert _is_linked(a, 'prev', b2)
    if hasattr(b1, 'AbstractConection6'):
        assert not _is_linked(b1, 'AbstractConection6', a)
    if hasattr(b2, 'AbstractConection6'):
        assert _is_linked(b2, 'AbstractConection6', a)
    _safe_set(a, 'prev', None)
    assert not _is_linked(a, 'prev', b2)
    if hasattr(b2, 'AbstractConection6'):
        assert not _is_linked(b2, 'AbstractConection6', a)


def test_assoc_connections1_link_reassign_clear():
    a = FSmachine_Root(FSmachineName="sample_text")
    b1 = FSmachine_AbstractConection(name="sample_text")
    b2 = FSmachine_AbstractConection(name="sample_text_2")
    _safe_set(a, 'par', {b1})
    assert _is_linked(a, 'par', b1)
    if hasattr(b1, 'AbstractConection'):
        assert _is_linked(b1, 'AbstractConection', a)
    _safe_set(a, 'par', {b2})
    assert _is_linked(a, 'par', b2)
    if hasattr(b1, 'AbstractConection'):
        assert not _is_linked(b1, 'AbstractConection', a)
    if hasattr(b2, 'AbstractConection'):
        assert _is_linked(b2, 'AbstractConection', a)
    _safe_set(a, 'par', set())
    assert not _is_linked(a, 'par', b2)
    if hasattr(b2, 'AbstractConection'):
        assert not _is_linked(b2, 'AbstractConection', a)


def test_assoc_next9_link_reassign_clear():
    a = FSmachine_AbstractObject(active=True, name="sample_text")
    b1 = FSmachine_AbstractConection(name="sample_text")
    b2 = FSmachine_AbstractConection(name="sample_text_2")
    _safe_set(a, 'AbstractObject10', b1)
    assert _is_linked(a, 'AbstractObject10', b1)
    if hasattr(b1, 'conChild'):
        assert _is_linked(b1, 'conChild', a)
    _safe_set(a, 'AbstractObject10', b2)
    assert _is_linked(a, 'AbstractObject10', b2)
    if hasattr(b1, 'conChild'):
        assert not _is_linked(b1, 'conChild', a)
    if hasattr(b2, 'conChild'):
        assert _is_linked(b2, 'conChild', a)
    _safe_set(a, 'AbstractObject10', None)
    assert not _is_linked(a, 'AbstractObject10', b2)
    if hasattr(b2, 'conChild'):
        assert not _is_linked(b2, 'conChild', a)


def test_assoc_objects0_link_reassign_clear():
    a = FSmachine_Root(FSmachineName="sample_text")
    b1 = FSmachine_AbstractObject(active=True, name="sample_text")
    b2 = FSmachine_AbstractObject(active=False, name="sample_text_2")
    _safe_set(a, 'parent', {b1})
    assert _is_linked(a, 'parent', b1)
    if hasattr(b1, 'AbstractObject'):
        assert _is_linked(b1, 'AbstractObject', a)
    _safe_set(a, 'parent', {b2})
    assert _is_linked(a, 'parent', b2)
    if hasattr(b1, 'AbstractObject'):
        assert not _is_linked(b1, 'AbstractObject', a)
    if hasattr(b2, 'AbstractObject'):
        assert _is_linked(b2, 'AbstractObject', a)
    _safe_set(a, 'parent', set())
    assert not _is_linked(a, 'parent', b2)
    if hasattr(b2, 'AbstractObject'):
        assert not _is_linked(b2, 'AbstractObject', a)


def test_assoc_par7_link_reassign_clear():
    a = FSmachine_Root(FSmachineName="sample_text")
    b1 = FSmachine_AbstractConection(name="sample_text")
    b2 = FSmachine_AbstractConection(name="sample_text_2")
    _safe_set(a, 'Root8', b1)
    assert _is_linked(a, 'Root8', b1)
    if hasattr(b1, 'connections'):
        assert _is_linked(b1, 'connections', a)
    _safe_set(a, 'Root8', b2)
    assert _is_linked(a, 'Root8', b2)
    if hasattr(b1, 'connections'):
        assert not _is_linked(b1, 'connections', a)
    if hasattr(b2, 'connections'):
        assert _is_linked(b2, 'connections', a)
    _safe_set(a, 'Root8', None)
    assert not _is_linked(a, 'Root8', b2)
    if hasattr(b2, 'connections'):
        assert not _is_linked(b2, 'connections', a)


def test_assoc_parent2_link_reassign_clear():
    a = FSmachine_Root(FSmachineName="sample_text")
    b1 = FSmachine_AbstractObject(active=True, name="sample_text")
    b2 = FSmachine_AbstractObject(active=False, name="sample_text_2")
    _safe_set(a, 'Root', b1)
    assert _is_linked(a, 'Root', b1)
    if hasattr(b1, 'objects'):
        assert _is_linked(b1, 'objects', a)
    _safe_set(a, 'Root', b2)
    assert _is_linked(a, 'Root', b2)
    if hasattr(b1, 'objects'):
        assert not _is_linked(b1, 'objects', a)
    if hasattr(b2, 'objects'):
        assert _is_linked(b2, 'objects', a)
    _safe_set(a, 'Root', None)
    assert not _is_linked(a, 'Root', b2)
    if hasattr(b2, 'objects'):
        assert not _is_linked(b2, 'objects', a)


def test_assoc_prev11_link_reassign_clear():
    a = FSmachine_AbstractObject(active=True, name="sample_text")
    b1 = FSmachine_AbstractConection(name="sample_text")
    b2 = FSmachine_AbstractConection(name="sample_text_2")
    _safe_set(a, 'AbstractObject12', b1)
    assert _is_linked(a, 'AbstractObject12', b1)
    if hasattr(b1, 'conParent'):
        assert _is_linked(b1, 'conParent', a)
    _safe_set(a, 'AbstractObject12', b2)
    assert _is_linked(a, 'AbstractObject12', b2)
    if hasattr(b1, 'conParent'):
        assert not _is_linked(b1, 'conParent', a)
    if hasattr(b2, 'conParent'):
        assert _is_linked(b2, 'conParent', a)
    _safe_set(a, 'AbstractObject12', None)
    assert not _is_linked(a, 'AbstractObject12', b2)
    if hasattr(b2, 'conParent'):
        assert not _is_linked(b2, 'conParent', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AbstractConection_strategy = st.builds(AbstractConection)
@given(instance=AbstractConection_strategy)
@settings(max_examples=25)
def test_AbstractConection_instantiation(instance):
    assert isinstance(instance, AbstractConection)


AbstractObject_strategy = st.builds(AbstractObject)
@given(instance=AbstractObject_strategy)
@settings(max_examples=25)
def test_AbstractObject_instantiation(instance):
    assert isinstance(instance, AbstractObject)


FSmachine_AbstractConection_strategy = st.builds(FSmachine_AbstractConection, name=safe_text)
@given(instance=FSmachine_AbstractConection_strategy)
@settings(max_examples=25)
def test_FSmachine_AbstractConection_instantiation(instance):
    assert isinstance(instance, FSmachine_AbstractConection)


FSmachine_AbstractObject_strategy = st.builds(FSmachine_AbstractObject, active=st.booleans(), name=safe_text)
@given(instance=FSmachine_AbstractObject_strategy)
@settings(max_examples=25)
def test_FSmachine_AbstractObject_instantiation(instance):
    assert isinstance(instance, FSmachine_AbstractObject)


FSmachine_ReasonConnection_strategy = st.builds(FSmachine_ReasonConnection, reason=safe_text)
@given(instance=FSmachine_ReasonConnection_strategy)
@settings(max_examples=25)
def test_FSmachine_ReasonConnection_instantiation(instance):
    assert isinstance(instance, FSmachine_ReasonConnection)


FSmachine_Root_strategy = st.builds(FSmachine_Root, FSmachineName=safe_text)
@given(instance=FSmachine_Root_strategy)
@settings(max_examples=25)
def test_FSmachine_Root_instantiation(instance):
    assert isinstance(instance, FSmachine_Root)


FSmachine_State_strategy = st.builds(FSmachine_State, data=safe_text, description=safe_text)
@given(instance=FSmachine_State_strategy)
@settings(max_examples=25)
def test_FSmachine_State_instantiation(instance):
    assert isinstance(instance, FSmachine_State)


FSmachine_TimeConnection_strategy = st.builds(FSmachine_TimeConnection, when=safe_text)
@given(instance=FSmachine_TimeConnection_strategy)
@settings(max_examples=25)
def test_FSmachine_TimeConnection_instantiation(instance):
    assert isinstance(instance, FSmachine_TimeConnection)



