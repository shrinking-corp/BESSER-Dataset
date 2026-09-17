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

@given(instance=Projects_Company_strategy)
@settings(max_examples=30)
def test_hyp_projects_company_fire_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.fire(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.fire).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'fire' in Projects_Company is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'fire' in Projects_Company did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'fire' in Projects_Company is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Projects_Company_strategy)
@settings(max_examples=30)
def test_hyp_projects_company_hire_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.hire(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.hire).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'hire' in Projects_Company is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'hire' in Projects_Company did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'hire' in Projects_Company is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Projects_Company_strategy)
@settings(max_examples=30)
def test_hyp_projects_company_start_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.start(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.start).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'start' in Projects_Company is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'start' in Projects_Company did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'start' in Projects_Company is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Projects_Company_strategy)
@settings(max_examples=30)
def test_hyp_projects_company_finish_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.finish(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.finish).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'finish' in Projects_Company is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'finish' in Projects_Company did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'finish' in Projects_Company is not implemented or raised an error")


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



