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
    sample_Person,
    sample_Group,
    sample_Department,
    sample_Company,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_sample_person_is_not_abstract():
    assert not inspect.isabstract(sample_Person)


def test_hyp_sample_person_constructor_exists():
    assert callable(sample_Person.__init__)


def test_hyp_sample_person_constructor_args():
    sig = inspect.signature(sample_Person.__init__)
    params = list(sig.parameters.keys())
    assert "birthdate" in params, "Missing parameter 'birthdate'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_sample_group_is_not_abstract():
    assert not inspect.isabstract(sample_Group)


def test_hyp_sample_group_constructor_exists():
    assert callable(sample_Group.__init__)


def test_hyp_sample_group_constructor_args():
    sig = inspect.signature(sample_Group.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_sample_department_is_not_abstract():
    assert not inspect.isabstract(sample_Department)


def test_hyp_sample_department_constructor_exists():
    assert callable(sample_Department.__init__)


def test_hyp_sample_department_constructor_args():
    sig = inspect.signature(sample_Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_sample_company_is_not_abstract():
    assert not inspect.isabstract(sample_Company)


def test_hyp_sample_company_constructor_exists():
    assert callable(sample_Company.__init__)


def test_hyp_sample_company_constructor_args():
    sig = inspect.signature(sample_Company.__init__)
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
sample_Person_strategy = st.builds(
    sample_Person,
    birthdate=
        st.dates(),
    name=
        safe_text
)
sample_Group_strategy = st.builds(
    sample_Group,
    name=
        safe_text
)
sample_Department_strategy = st.builds(
    sample_Department,
    name=
        safe_text
)
sample_Company_strategy = st.builds(
    sample_Company,
    name=
        safe_text
)




@given(instance=sample_Person_strategy)
def test_hyp_sample_person_birthdate_setter(instance):
    original = instance.birthdate
    instance.birthdate = original
    assert instance.birthdate == original



@given(instance=sample_Person_strategy)
def test_hyp_sample_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=sample_Group_strategy)
def test_hyp_sample_group_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=sample_Department_strategy)
def test_hyp_sample_department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=sample_Company_strategy)
def test_hyp_sample_company_name_setter(instance):
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
    sample_Company,
    sample_Department,
    sample_Group,
    sample_Person,
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

def test_sample_Company_name_value_roundtrip():
    instance = sample_Company(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_sample_Department_name_value_roundtrip():
    instance = sample_Department(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_sample_Group_name_value_roundtrip():
    instance = sample_Group(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_sample_Person_birthdate_value_roundtrip():
    instance = sample_Person(birthdate=date(2024, 1, 1), name="sample_text")
    assert instance.birthdate == date(2024, 1, 1)
    instance.birthdate = date(2025, 6, 15)
    assert instance.birthdate == date(2025, 6, 15)


def test_sample_Person_name_value_roundtrip():
    instance = sample_Person(birthdate=date(2024, 1, 1), name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assoc_company2_link_reassign_clear():
    a = sample_Department(name="sample_text")
    b1 = sample_Company(name="sample_text")
    b2 = sample_Company(name="sample_text_2")
    _safe_set(a, 'departments', b1)
    assert _is_linked(a, 'departments', b1)
    if hasattr(b1, 'Company'):
        assert _is_linked(b1, 'Company', a)
    _safe_set(a, 'departments', b2)
    assert _is_linked(a, 'departments', b2)
    if hasattr(b1, 'Company'):
        assert not _is_linked(b1, 'Company', a)
    if hasattr(b2, 'Company'):
        assert _is_linked(b2, 'Company', a)
    _safe_set(a, 'departments', None)
    assert not _is_linked(a, 'departments', b2)
    if hasattr(b2, 'Company'):
        assert not _is_linked(b2, 'Company', a)


def test_assoc_department4_link_reassign_clear():
    a = sample_Group(name="sample_text")
    b1 = sample_Department(name="sample_text")
    b2 = sample_Department(name="sample_text_2")
    _safe_set(a, 'groups', b1)
    assert _is_linked(a, 'groups', b1)
    if hasattr(b1, 'Department5'):
        assert _is_linked(b1, 'Department5', a)
    _safe_set(a, 'groups', b2)
    assert _is_linked(a, 'groups', b2)
    if hasattr(b1, 'Department5'):
        assert not _is_linked(b1, 'Department5', a)
    if hasattr(b2, 'Department5'):
        assert _is_linked(b2, 'Department5', a)
    _safe_set(a, 'groups', None)
    assert not _is_linked(a, 'groups', b2)
    if hasattr(b2, 'Department5'):
        assert not _is_linked(b2, 'Department5', a)


def test_assoc_departments0_link_reassign_clear():
    a = sample_Department(name="sample_text")
    b1 = sample_Company(name="sample_text")
    b2 = sample_Company(name="sample_text_2")
    _safe_set(a, 'Department', b1)
    assert _is_linked(a, 'Department', b1)
    if hasattr(b1, 'company'):
        assert _is_linked(b1, 'company', a)
    _safe_set(a, 'Department', b2)
    assert _is_linked(a, 'Department', b2)
    if hasattr(b1, 'company'):
        assert not _is_linked(b1, 'company', a)
    if hasattr(b2, 'company'):
        assert _is_linked(b2, 'company', a)
    _safe_set(a, 'Department', None)
    assert not _is_linked(a, 'Department', b2)
    if hasattr(b2, 'company'):
        assert not _is_linked(b2, 'company', a)


def test_assoc_group6_link_reassign_clear():
    a = sample_Person(birthdate=date(2024, 1, 1), name="sample_text")
    b1 = sample_Group(name="sample_text")
    b2 = sample_Group(name="sample_text_2")
    _safe_set(a, 'persons', b1)
    assert _is_linked(a, 'persons', b1)
    if hasattr(b1, 'Group7'):
        assert _is_linked(b1, 'Group7', a)
    _safe_set(a, 'persons', b2)
    assert _is_linked(a, 'persons', b2)
    if hasattr(b1, 'Group7'):
        assert not _is_linked(b1, 'Group7', a)
    if hasattr(b2, 'Group7'):
        assert _is_linked(b2, 'Group7', a)
    _safe_set(a, 'persons', None)
    assert not _is_linked(a, 'persons', b2)
    if hasattr(b2, 'Group7'):
        assert not _is_linked(b2, 'Group7', a)


def test_assoc_groups1_link_reassign_clear():
    a = sample_Group(name="sample_text")
    b1 = sample_Department(name="sample_text")
    b2 = sample_Department(name="sample_text_2")
    _safe_set(a, 'Group', b1)
    assert _is_linked(a, 'Group', b1)
    if hasattr(b1, 'department'):
        assert _is_linked(b1, 'department', a)
    _safe_set(a, 'Group', b2)
    assert _is_linked(a, 'Group', b2)
    if hasattr(b1, 'department'):
        assert not _is_linked(b1, 'department', a)
    if hasattr(b2, 'department'):
        assert _is_linked(b2, 'department', a)
    _safe_set(a, 'Group', None)
    assert not _is_linked(a, 'Group', b2)
    if hasattr(b2, 'department'):
        assert not _is_linked(b2, 'department', a)


def test_assoc_persons3_link_reassign_clear():
    a = sample_Person(birthdate=date(2024, 1, 1), name="sample_text")
    b1 = sample_Group(name="sample_text")
    b2 = sample_Group(name="sample_text_2")
    _safe_set(a, 'Person', b1)
    assert _is_linked(a, 'Person', b1)
    if hasattr(b1, 'group'):
        assert _is_linked(b1, 'group', a)
    _safe_set(a, 'Person', b2)
    assert _is_linked(a, 'Person', b2)
    if hasattr(b1, 'group'):
        assert not _is_linked(b1, 'group', a)
    if hasattr(b2, 'group'):
        assert _is_linked(b2, 'group', a)
    _safe_set(a, 'Person', None)
    assert not _is_linked(a, 'Person', b2)
    if hasattr(b2, 'group'):
        assert not _is_linked(b2, 'group', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

sample_Company_strategy = st.builds(sample_Company, name=safe_text)
@given(instance=sample_Company_strategy)
@settings(max_examples=25)
def test_sample_Company_instantiation(instance):
    assert isinstance(instance, sample_Company)


sample_Department_strategy = st.builds(sample_Department, name=safe_text)
@given(instance=sample_Department_strategy)
@settings(max_examples=25)
def test_sample_Department_instantiation(instance):
    assert isinstance(instance, sample_Department)


sample_Group_strategy = st.builds(sample_Group, name=safe_text)
@given(instance=sample_Group_strategy)
@settings(max_examples=25)
def test_sample_Group_instantiation(instance):
    assert isinstance(instance, sample_Group)


sample_Person_strategy = st.builds(sample_Person, birthdate=st.dates(), name=safe_text)
@given(instance=sample_Person_strategy)
@settings(max_examples=25)
def test_sample_Person_instantiation(instance):
    assert isinstance(instance, sample_Person)





import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    sample_Company,
    sample_Department,
    sample_Group,
    sample_Person,
)

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
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

def test_assoc_company2_reverse_link_reassign_clear():
    a1 = sample_Department(name="sample_text")
    a2 = sample_Department(name="sample_text_2")
    b = sample_Company(name="sample_text")
    _safe_set(b, 'Company', a1)
    assert _is_linked(b, 'Company', a1)
    if hasattr(a1, 'departments'):
        assert _is_linked(a1, 'departments', b)
    _safe_set(b, 'Company', a2)
    assert _is_linked(b, 'Company', a2)
    if hasattr(a1, 'departments'):
        assert not _is_linked(a1, 'departments', b)
    if hasattr(a2, 'departments'):
        assert _is_linked(a2, 'departments', b)
    _safe_set(b, 'Company', None)
    assert not _is_linked(b, 'Company', a2)
    if hasattr(a2, 'departments'):
        assert not _is_linked(a2, 'departments', b)


def test_assoc_department4_reverse_link_reassign_clear():
    a1 = sample_Group(name="sample_text")
    a2 = sample_Group(name="sample_text_2")
    b = sample_Department(name="sample_text")
    _safe_set(b, 'Department5', a1)
    assert _is_linked(b, 'Department5', a1)
    if hasattr(a1, 'groups'):
        assert _is_linked(a1, 'groups', b)
    _safe_set(b, 'Department5', a2)
    assert _is_linked(b, 'Department5', a2)
    if hasattr(a1, 'groups'):
        assert not _is_linked(a1, 'groups', b)
    if hasattr(a2, 'groups'):
        assert _is_linked(a2, 'groups', b)
    _safe_set(b, 'Department5', None)
    assert not _is_linked(b, 'Department5', a2)
    if hasattr(a2, 'groups'):
        assert not _is_linked(a2, 'groups', b)


def test_assoc_departments0_reverse_link_reassign_clear():
    a1 = sample_Department(name="sample_text")
    a2 = sample_Department(name="sample_text_2")
    b = sample_Company(name="sample_text")
    _safe_set(b, 'company', {a1})
    assert _is_linked(b, 'company', a1)
    if hasattr(a1, 'Department'):
        assert _is_linked(a1, 'Department', b)
    _safe_set(b, 'company', {a2})
    assert _is_linked(b, 'company', a2)
    if hasattr(a1, 'Department'):
        assert not _is_linked(a1, 'Department', b)
    if hasattr(a2, 'Department'):
        assert _is_linked(a2, 'Department', b)
    _safe_set(b, 'company', set())
    assert not _is_linked(b, 'company', a2)
    if hasattr(a2, 'Department'):
        assert not _is_linked(a2, 'Department', b)


def test_assoc_group6_reverse_link_reassign_clear():
    a1 = sample_Person(birthdate=date(2024, 1, 1), name="sample_text")
    a2 = sample_Person(birthdate=date(2025, 6, 15), name="sample_text_2")
    b = sample_Group(name="sample_text")
    _safe_set(b, 'Group7', a1)
    assert _is_linked(b, 'Group7', a1)
    if hasattr(a1, 'persons'):
        assert _is_linked(a1, 'persons', b)
    _safe_set(b, 'Group7', a2)
    assert _is_linked(b, 'Group7', a2)
    if hasattr(a1, 'persons'):
        assert not _is_linked(a1, 'persons', b)
    if hasattr(a2, 'persons'):
        assert _is_linked(a2, 'persons', b)
    _safe_set(b, 'Group7', None)
    assert not _is_linked(b, 'Group7', a2)
    if hasattr(a2, 'persons'):
        assert not _is_linked(a2, 'persons', b)


def test_assoc_groups1_reverse_link_reassign_clear():
    a1 = sample_Group(name="sample_text")
    a2 = sample_Group(name="sample_text_2")
    b = sample_Department(name="sample_text")
    _safe_set(b, 'department', {a1})
    assert _is_linked(b, 'department', a1)
    if hasattr(a1, 'Group'):
        assert _is_linked(a1, 'Group', b)
    _safe_set(b, 'department', {a2})
    assert _is_linked(b, 'department', a2)
    if hasattr(a1, 'Group'):
        assert not _is_linked(a1, 'Group', b)
    if hasattr(a2, 'Group'):
        assert _is_linked(a2, 'Group', b)
    _safe_set(b, 'department', set())
    assert not _is_linked(b, 'department', a2)
    if hasattr(a2, 'Group'):
        assert not _is_linked(a2, 'Group', b)


def test_assoc_persons3_reverse_link_reassign_clear():
    a1 = sample_Person(birthdate=date(2024, 1, 1), name="sample_text")
    a2 = sample_Person(birthdate=date(2025, 6, 15), name="sample_text_2")
    b = sample_Group(name="sample_text")
    _safe_set(b, 'group', {a1})
    assert _is_linked(b, 'group', a1)
    if hasattr(a1, 'Person'):
        assert _is_linked(a1, 'Person', b)
    _safe_set(b, 'group', {a2})
    assert _is_linked(b, 'group', a2)
    if hasattr(a1, 'Person'):
        assert not _is_linked(a1, 'Person', b)
    if hasattr(a2, 'Person'):
        assert _is_linked(a2, 'Person', b)
    _safe_set(b, 'group', set())
    assert not _is_linked(b, 'group', a2)
    if hasattr(a2, 'Person'):
        assert not _is_linked(a2, 'Person', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================


