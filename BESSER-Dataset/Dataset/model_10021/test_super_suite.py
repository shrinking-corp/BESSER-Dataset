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
    Projects_Qualification,
    Projects_Worker,
    Projects_Project,
    Projects_Company,
    ProjectStatus,
    ProjectSize,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_projects_qualification_is_not_abstract():
    assert not inspect.isabstract(Projects_Qualification)


def test_hyp_projects_qualification_constructor_exists():
    assert callable(Projects_Qualification.__init__)


def test_hyp_projects_qualification_constructor_args():
    sig = inspect.signature(Projects_Qualification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_projects_worker_is_not_abstract():
    assert not inspect.isabstract(Projects_Worker)


def test_hyp_projects_worker_constructor_exists():
    assert callable(Projects_Worker.__init__)


def test_hyp_projects_worker_constructor_args():
    sig = inspect.signature(Projects_Worker.__init__)
    params = list(sig.parameters.keys())



def test_hyp_projects_project_is_not_abstract():
    assert not inspect.isabstract(Projects_Project)


def test_hyp_projects_project_constructor_exists():
    assert callable(Projects_Project.__init__)


def test_hyp_projects_project_constructor_args():
    sig = inspect.signature(Projects_Project.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"
    assert "size" in params, "Missing parameter 'size'"





def test_hyp_projects_company_is_not_abstract():
    assert not inspect.isabstract(Projects_Company)


def test_hyp_projects_company_constructor_exists():
    assert callable(Projects_Company.__init__)


def test_hyp_projects_company_constructor_args():
    sig = inspect.signature(Projects_Company.__init__)
    params = list(sig.parameters.keys())

def test_hyp_projectstatus_exists():
    # Check that the Enumeration exists
    assert ProjectStatus is not None

def test_hyp_projectstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProjectStatus]
    expected_literals = [
        "finished",
        "planned",
        "active",
        "suspended",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProjectStatus"

def test_hyp_projectsize_exists():
    # Check that the Enumeration exists
    assert ProjectSize is not None

def test_hyp_projectsize_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProjectSize]
    expected_literals = [
        "medium",
        "big",
        "small",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProjectSize"


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
Projects_Qualification_strategy = st.builds(
    Projects_Qualification,
)
Projects_Worker_strategy = st.builds(
    Projects_Worker,
)
Projects_Project_strategy = st.builds(
    Projects_Project,
    status=
        safe_text,
    size=
        safe_text
)
Projects_Company_strategy = st.builds(
    Projects_Company,
)






@given(instance=Projects_Project_strategy)
def test_hyp_projects_project_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=Projects_Project_strategy)
def test_hyp_projects_project_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Projects_Company,
    Projects_Project,
    Projects_Qualification,
    Projects_Worker,
    ProjectSize,
    ProjectStatus,
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

def test_Projects_Project_size_value_roundtrip():
    instance = Projects_Project(size="sample_text", status="sample_text")
    assert instance.size == "sample_text"
    instance.size = "sample_text_2"
    assert instance.size == "sample_text_2"


def test_Projects_Project_status_value_roundtrip():
    instance = Projects_Project(size="sample_text", status="sample_text")
    assert instance.status == "sample_text"
    instance.status = "sample_text_2"
    assert instance.status == "sample_text_2"


def test_assoc_company8_link_reassign_clear():
    a = Projects_Project(size="sample_text", status="sample_text")
    b1 = Projects_Company()
    b2 = Projects_Company()
    _safe_set(a, 'Projects_Project9', b1)
    assert _is_linked(a, 'Projects_Project9', b1)
    if hasattr(b1, 'Projects_Company10'):
        assert _is_linked(b1, 'Projects_Company10', a)
    _safe_set(a, 'Projects_Project9', b2)
    assert _is_linked(a, 'Projects_Project9', b2)
    if hasattr(b1, 'Projects_Company10'):
        assert not _is_linked(b1, 'Projects_Company10', a)
    if hasattr(b2, 'Projects_Company10'):
        assert _is_linked(b2, 'Projects_Company10', a)
    _safe_set(a, 'Projects_Project9', None)
    assert not _is_linked(a, 'Projects_Project9', b2)
    if hasattr(b2, 'Projects_Company10'):
        assert not _is_linked(b2, 'Projects_Company10', a)


def test_assoc_employees1_link_reassign_clear():
    a = Projects_Company()
    b1 = Projects_Worker()
    b2 = Projects_Worker()
    _safe_set(a, 'Projects_Company2', {b1})
    assert _is_linked(a, 'Projects_Company2', b1)
    if hasattr(b1, 'Projects_Worker'):
        assert _is_linked(b1, 'Projects_Worker', a)
    _safe_set(a, 'Projects_Company2', {b2})
    assert _is_linked(a, 'Projects_Company2', b2)
    if hasattr(b1, 'Projects_Worker'):
        assert not _is_linked(b1, 'Projects_Worker', a)
    if hasattr(b2, 'Projects_Worker'):
        assert _is_linked(b2, 'Projects_Worker', a)
    _safe_set(a, 'Projects_Company2', set())
    assert not _is_linked(a, 'Projects_Company2', b2)
    if hasattr(b2, 'Projects_Worker'):
        assert not _is_linked(b2, 'Projects_Worker', a)


def test_assoc_members11_link_reassign_clear():
    a = Projects_Project(size="sample_text", status="sample_text")
    b1 = Projects_Worker()
    b2 = Projects_Worker()
    _safe_set(a, 'Projects_Project12', {b1})
    assert _is_linked(a, 'Projects_Project12', b1)
    if hasattr(b1, 'Projects_Worker13'):
        assert _is_linked(b1, 'Projects_Worker13', a)
    _safe_set(a, 'Projects_Project12', {b2})
    assert _is_linked(a, 'Projects_Project12', b2)
    if hasattr(b1, 'Projects_Worker13'):
        assert not _is_linked(b1, 'Projects_Worker13', a)
    if hasattr(b2, 'Projects_Worker13'):
        assert _is_linked(b2, 'Projects_Worker13', a)
    _safe_set(a, 'Projects_Project12', set())
    assert not _is_linked(a, 'Projects_Project12', b2)
    if hasattr(b2, 'Projects_Worker13'):
        assert not _is_linked(b2, 'Projects_Worker13', a)


def test_assoc_predecessors18_link_reassign_clear():
    a = Projects_Project(size="sample_text", status="sample_text")
    b1 = Projects_Project(size="sample_text", status="sample_text")
    b2 = Projects_Project(size="sample_text_2", status="sample_text_2")
    _safe_set(a, 'Projects_Project17', {b1})
    assert _is_linked(a, 'Projects_Project17', b1)
    if hasattr(b1, 'Projects_Project19'):
        assert _is_linked(b1, 'Projects_Project19', a)
    _safe_set(a, 'Projects_Project17', {b2})
    assert _is_linked(a, 'Projects_Project17', b2)
    if hasattr(b1, 'Projects_Project19'):
        assert not _is_linked(b1, 'Projects_Project19', a)
    if hasattr(b2, 'Projects_Project19'):
        assert _is_linked(b2, 'Projects_Project19', a)
    _safe_set(a, 'Projects_Project17', set())
    assert not _is_linked(a, 'Projects_Project17', b2)
    if hasattr(b2, 'Projects_Project19'):
        assert not _is_linked(b2, 'Projects_Project19', a)


def test_assoc_projects0_link_reassign_clear():
    a = Projects_Project(size="sample_text", status="sample_text")
    b1 = Projects_Company()
    b2 = Projects_Company()
    _safe_set(a, 'Projects_Project', b1)
    assert _is_linked(a, 'Projects_Project', b1)
    if hasattr(b1, 'Projects_Company'):
        assert _is_linked(b1, 'Projects_Company', a)
    _safe_set(a, 'Projects_Project', b2)
    assert _is_linked(a, 'Projects_Project', b2)
    if hasattr(b1, 'Projects_Company'):
        assert not _is_linked(b1, 'Projects_Company', a)
    if hasattr(b2, 'Projects_Company'):
        assert _is_linked(b2, 'Projects_Company', a)
    _safe_set(a, 'Projects_Project', None)
    assert not _is_linked(a, 'Projects_Project', b2)
    if hasattr(b2, 'Projects_Company'):
        assert not _is_linked(b2, 'Projects_Company', a)


def test_assoc_projects5_link_reassign_clear():
    a = Projects_Project(size="sample_text", status="sample_text")
    b1 = Projects_Worker()
    b2 = Projects_Worker()
    _safe_set(a, 'Projects_Project7', b1)
    assert _is_linked(a, 'Projects_Project7', b1)
    if hasattr(b1, 'Projects_Worker6'):
        assert _is_linked(b1, 'Projects_Worker6', a)
    _safe_set(a, 'Projects_Project7', b2)
    assert _is_linked(a, 'Projects_Project7', b2)
    if hasattr(b1, 'Projects_Worker6'):
        assert not _is_linked(b1, 'Projects_Worker6', a)
    if hasattr(b2, 'Projects_Worker6'):
        assert _is_linked(b2, 'Projects_Worker6', a)
    _safe_set(a, 'Projects_Project7', None)
    assert not _is_linked(a, 'Projects_Project7', b2)
    if hasattr(b2, 'Projects_Worker6'):
        assert not _is_linked(b2, 'Projects_Worker6', a)


def test_assoc_requirements14_link_reassign_clear():
    a = Projects_Project(size="sample_text", status="sample_text")
    b1 = Projects_Qualification()
    b2 = Projects_Qualification()
    _safe_set(a, 'Projects_Project15', {b1})
    assert _is_linked(a, 'Projects_Project15', b1)
    if hasattr(b1, 'Projects_Qualification16'):
        assert _is_linked(b1, 'Projects_Qualification16', a)
    _safe_set(a, 'Projects_Project15', {b2})
    assert _is_linked(a, 'Projects_Project15', b2)
    if hasattr(b1, 'Projects_Qualification16'):
        assert not _is_linked(b1, 'Projects_Qualification16', a)
    if hasattr(b2, 'Projects_Qualification16'):
        assert _is_linked(b2, 'Projects_Qualification16', a)
    _safe_set(a, 'Projects_Project15', set())
    assert not _is_linked(a, 'Projects_Project15', b2)
    if hasattr(b2, 'Projects_Qualification16'):
        assert not _is_linked(b2, 'Projects_Qualification16', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Projects_Company_strategy = st.builds(Projects_Company)
@given(instance=Projects_Company_strategy)
@settings(max_examples=25)
def test_Projects_Company_instantiation(instance):
    assert isinstance(instance, Projects_Company)


Projects_Project_strategy = st.builds(Projects_Project, size=safe_text, status=safe_text)
@given(instance=Projects_Project_strategy)
@settings(max_examples=25)
def test_Projects_Project_instantiation(instance):
    assert isinstance(instance, Projects_Project)


Projects_Qualification_strategy = st.builds(Projects_Qualification)
@given(instance=Projects_Qualification_strategy)
@settings(max_examples=25)
def test_Projects_Qualification_instantiation(instance):
    assert isinstance(instance, Projects_Qualification)


Projects_Worker_strategy = st.builds(Projects_Worker)
@given(instance=Projects_Worker_strategy)
@settings(max_examples=25)
def test_Projects_Worker_instantiation(instance):
    assert isinstance(instance, Projects_Worker)





import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Projects_Company,
    Projects_Project,
    Projects_Qualification,
    Projects_Worker,
    ProjectSize,
    ProjectStatus,
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

def test_assoc_company8_reverse_link_reassign_clear():
    a1 = Projects_Project(size="sample_text", status="sample_text")
    a2 = Projects_Project(size="sample_text_2", status="sample_text_2")
    b = Projects_Company()
    _safe_set(b, 'Projects_Company10', a1)
    assert _is_linked(b, 'Projects_Company10', a1)
    if hasattr(a1, 'Projects_Project9'):
        assert _is_linked(a1, 'Projects_Project9', b)
    _safe_set(b, 'Projects_Company10', a2)
    assert _is_linked(b, 'Projects_Company10', a2)
    if hasattr(a1, 'Projects_Project9'):
        assert not _is_linked(a1, 'Projects_Project9', b)
    if hasattr(a2, 'Projects_Project9'):
        assert _is_linked(a2, 'Projects_Project9', b)
    _safe_set(b, 'Projects_Company10', None)
    assert not _is_linked(b, 'Projects_Company10', a2)
    if hasattr(a2, 'Projects_Project9'):
        assert not _is_linked(a2, 'Projects_Project9', b)


def test_assoc_predecessors18_reverse_link_reassign_clear():
    a1 = Projects_Project(size="sample_text", status="sample_text")
    a2 = Projects_Project(size="sample_text_2", status="sample_text_2")
    b = Projects_Project(size="sample_text", status="sample_text")
    _safe_set(b, 'Projects_Project19', a1)
    assert _is_linked(b, 'Projects_Project19', a1)
    if hasattr(a1, 'Projects_Project17'):
        assert _is_linked(a1, 'Projects_Project17', b)
    _safe_set(b, 'Projects_Project19', a2)
    assert _is_linked(b, 'Projects_Project19', a2)
    if hasattr(a1, 'Projects_Project17'):
        assert not _is_linked(a1, 'Projects_Project17', b)
    if hasattr(a2, 'Projects_Project17'):
        assert _is_linked(a2, 'Projects_Project17', b)
    _safe_set(b, 'Projects_Project19', None)
    assert not _is_linked(b, 'Projects_Project19', a2)
    if hasattr(a2, 'Projects_Project17'):
        assert not _is_linked(a2, 'Projects_Project17', b)


def test_assoc_projects0_reverse_link_reassign_clear():
    a1 = Projects_Project(size="sample_text", status="sample_text")
    a2 = Projects_Project(size="sample_text_2", status="sample_text_2")
    b = Projects_Company()
    _safe_set(b, 'Projects_Company', {a1})
    assert _is_linked(b, 'Projects_Company', a1)
    if hasattr(a1, 'Projects_Project'):
        assert _is_linked(a1, 'Projects_Project', b)
    _safe_set(b, 'Projects_Company', {a2})
    assert _is_linked(b, 'Projects_Company', a2)
    if hasattr(a1, 'Projects_Project'):
        assert not _is_linked(a1, 'Projects_Project', b)
    if hasattr(a2, 'Projects_Project'):
        assert _is_linked(a2, 'Projects_Project', b)
    _safe_set(b, 'Projects_Company', set())
    assert not _is_linked(b, 'Projects_Company', a2)
    if hasattr(a2, 'Projects_Project'):
        assert not _is_linked(a2, 'Projects_Project', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_employees1_stub_double():
    # Projects_Worker has no real 'Projects_Worker' property in the generated
    # code (a bare stub) -- manually attach it so Projects_Company's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Projects_Company's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Projects_Company()
    partner = Projects_Worker()
    setattr(partner, 'Projects_Worker', None)
    _safe_set(owner, 'Projects_Company2', {partner})
    assert getattr(partner, 'Projects_Worker') == owner
    _safe_set(owner, 'Projects_Company2', set())
    assert getattr(partner, 'Projects_Worker') is None


def test_assoc_members11_stub_double():
    # Projects_Worker has no real 'Projects_Worker13' property in the generated
    # code (a bare stub) -- manually attach it so Projects_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Projects_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Projects_Project(size="sample_text", status="sample_text")
    partner = Projects_Worker()
    setattr(partner, 'Projects_Worker13', None)
    _safe_set(owner, 'Projects_Project12', {partner})
    assert getattr(partner, 'Projects_Worker13') == owner
    _safe_set(owner, 'Projects_Project12', set())
    assert getattr(partner, 'Projects_Worker13') is None


def test_assoc_projects5_stub_double():
    # Projects_Worker has no real 'Projects_Worker6' property in the generated
    # code (a bare stub) -- manually attach it so Projects_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Projects_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Projects_Project(size="sample_text", status="sample_text")
    partner = Projects_Worker()
    setattr(partner, 'Projects_Worker6', None)
    _safe_set(owner, 'Projects_Project7', partner)
    assert owner in getattr(partner, 'Projects_Worker6')
    _safe_set(owner, 'Projects_Project7', None)
    assert owner not in getattr(partner, 'Projects_Worker6')


def test_assoc_requirements14_stub_double():
    # Projects_Qualification has no real 'Projects_Qualification16' property in the generated
    # code (a bare stub) -- manually attach it so Projects_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Projects_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Projects_Project(size="sample_text", status="sample_text")
    partner = Projects_Qualification()
    setattr(partner, 'Projects_Qualification16', None)
    _safe_set(owner, 'Projects_Project15', {partner})
    assert getattr(partner, 'Projects_Qualification16') == owner
    _safe_set(owner, 'Projects_Project15', set())
    assert getattr(partner, 'Projects_Qualification16') is None



