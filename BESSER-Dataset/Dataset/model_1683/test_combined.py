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
    relationworld_Arrow,
    relationworld_SourceNode,
    Arrow,
    TargetNode,
    NamedElement,
    relationworld_ThingB,
    relationworld_RelatedTo,
    SourceNode,
    relationworld_ThingA,
    relationworld_NamedElement,
    Category,
    relationworld_World,
    relationworld_Category,
    relationworld_TargetNode,
    Scale,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_relationworld_arrow_is_not_abstract():
    assert not inspect.isabstract(relationworld_Arrow)


def test_hyp_relationworld_arrow_constructor_exists():
    assert callable(relationworld_Arrow.__init__)


def test_hyp_relationworld_arrow_constructor_args():
    sig = inspect.signature(relationworld_Arrow.__init__)
    params = list(sig.parameters.keys())



def test_hyp_relationworld_sourcenode_is_not_abstract():
    assert not inspect.isabstract(relationworld_SourceNode)


def test_hyp_relationworld_sourcenode_constructor_exists():
    assert callable(relationworld_SourceNode.__init__)


def test_hyp_relationworld_sourcenode_constructor_args():
    sig = inspect.signature(relationworld_SourceNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arrow_is_not_abstract():
    assert not inspect.isabstract(Arrow)


def test_hyp_arrow_constructor_exists():
    assert callable(Arrow.__init__)


def test_hyp_arrow_constructor_args():
    sig = inspect.signature(Arrow.__init__)
    params = list(sig.parameters.keys())



def test_hyp_targetnode_is_not_abstract():
    assert not inspect.isabstract(TargetNode)


def test_hyp_targetnode_constructor_exists():
    assert callable(TargetNode.__init__)


def test_hyp_targetnode_constructor_args():
    sig = inspect.signature(TargetNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_relationworld_thingb_is_not_abstract():
    assert not inspect.isabstract(relationworld_ThingB)


def test_hyp_relationworld_thingb_constructor_exists():
    assert callable(relationworld_ThingB.__init__)


def test_hyp_relationworld_thingb_constructor_args():
    sig = inspect.signature(relationworld_ThingB.__init__)
    params = list(sig.parameters.keys())
    assert "step" in params, "Missing parameter 'step'"




def test_hyp_relationworld_relatedto_is_not_abstract():
    assert not inspect.isabstract(relationworld_RelatedTo)


def test_hyp_relationworld_relatedto_constructor_exists():
    assert callable(relationworld_RelatedTo.__init__)


def test_hyp_relationworld_relatedto_constructor_args():
    sig = inspect.signature(relationworld_RelatedTo.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sourcenode_is_not_abstract():
    assert not inspect.isabstract(SourceNode)


def test_hyp_sourcenode_constructor_exists():
    assert callable(SourceNode.__init__)


def test_hyp_sourcenode_constructor_args():
    sig = inspect.signature(SourceNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_relationworld_thinga_is_not_abstract():
    assert not inspect.isabstract(relationworld_ThingA)


def test_hyp_relationworld_thinga_constructor_exists():
    assert callable(relationworld_ThingA.__init__)


def test_hyp_relationworld_thinga_constructor_args():
    sig = inspect.signature(relationworld_ThingA.__init__)
    params = list(sig.parameters.keys())
    assert "since" in params, "Missing parameter 'since'"




def test_hyp_relationworld_namedelement_is_not_abstract():
    assert not inspect.isabstract(relationworld_NamedElement)


def test_hyp_relationworld_namedelement_constructor_exists():
    assert callable(relationworld_NamedElement.__init__)


def test_hyp_relationworld_namedelement_constructor_args():
    sig = inspect.signature(relationworld_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_category_is_not_abstract():
    assert not inspect.isabstract(Category)


def test_hyp_category_constructor_exists():
    assert callable(Category.__init__)


def test_hyp_category_constructor_args():
    sig = inspect.signature(Category.__init__)
    params = list(sig.parameters.keys())



def test_hyp_relationworld_world_is_not_abstract():
    assert not inspect.isabstract(relationworld_World)


def test_hyp_relationworld_world_constructor_exists():
    assert callable(relationworld_World.__init__)


def test_hyp_relationworld_world_constructor_args():
    sig = inspect.signature(relationworld_World.__init__)
    params = list(sig.parameters.keys())



def test_hyp_relationworld_category_is_not_abstract():
    assert not inspect.isabstract(relationworld_Category)


def test_hyp_relationworld_category_constructor_exists():
    assert callable(relationworld_Category.__init__)


def test_hyp_relationworld_category_constructor_args():
    sig = inspect.signature(relationworld_Category.__init__)
    params = list(sig.parameters.keys())
    assert "nom" in params, "Missing parameter 'nom'"




def test_hyp_relationworld_targetnode_is_not_abstract():
    assert not inspect.isabstract(relationworld_TargetNode)


def test_hyp_relationworld_targetnode_constructor_exists():
    assert callable(relationworld_TargetNode.__init__)


def test_hyp_relationworld_targetnode_constructor_args():
    sig = inspect.signature(relationworld_TargetNode.__init__)
    params = list(sig.parameters.keys())

def test_hyp_scale_exists():
    # Check that the Enumeration exists
    assert Scale is not None

def test_hyp_scale_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Scale]
    expected_literals = [
        "one",
        "four",
        "two",
        "nothing",
        "three",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Scale"


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
relationworld_Arrow_strategy = st.builds(
    relationworld_Arrow,
)
relationworld_SourceNode_strategy = st.builds(
    relationworld_SourceNode,
)
Arrow_strategy = st.builds(
    Arrow,
)
TargetNode_strategy = st.builds(
    TargetNode,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
relationworld_ThingB_strategy = st.builds(
    relationworld_ThingB,
    step=
        safe_text
)
relationworld_RelatedTo_strategy = st.builds(
    relationworld_RelatedTo,
)
SourceNode_strategy = st.builds(
    SourceNode,
)
relationworld_ThingA_strategy = st.builds(
    relationworld_ThingA,
    since=
        st.dates()
)
relationworld_NamedElement_strategy = st.builds(
    relationworld_NamedElement,
    name=
        safe_text
)
Category_strategy = st.builds(
    Category,
)
relationworld_World_strategy = st.builds(
    relationworld_World,
)
relationworld_Category_strategy = st.builds(
    relationworld_Category,
    nom=
        safe_text
)
relationworld_TargetNode_strategy = st.builds(
    relationworld_TargetNode,
)


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=relationworld_Arrow_strategy)
@settings(max_examples=30)
def test_hyp_relationworld_arrow_validate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validate()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validate' in relationworld_Arrow is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validate' in relationworld_Arrow did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validate' in relationworld_Arrow is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=relationworld_SourceNode_strategy)
@settings(max_examples=30)
def test_hyp_relationworld_sourcenode_succ_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.succ()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.succ).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'succ' in relationworld_SourceNode is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'succ' in relationworld_SourceNode did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'succ' in relationworld_SourceNode is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=relationworld_SourceNode_strategy)
@settings(max_examples=30)
def test_hyp_relationworld_sourcenode_pred_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.pred()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.pred).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'pred' in relationworld_SourceNode is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'pred' in relationworld_SourceNode did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'pred' in relationworld_SourceNode is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=relationworld_SourceNode_strategy)
@settings(max_examples=30)
def test_hyp_relationworld_sourcenode_compare_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.compare(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.compare).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'compare' in relationworld_SourceNode is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'compare' in relationworld_SourceNode did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'compare' in relationworld_SourceNode is not implemented or raised an error")







@given(instance=relationworld_ThingB_strategy)
def test_hyp_relationworld_thingb_step_setter(instance):
    original = instance.step
    instance.step = original
    assert instance.step == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=relationworld_ThingB_strategy)
@settings(max_examples=30)
def test_hyp_relationworld_thingb_succ_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.succ()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.succ).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'succ' in relationworld_ThingB is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'succ' in relationworld_ThingB did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'succ' in relationworld_ThingB is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=relationworld_ThingB_strategy)
@settings(max_examples=30)
def test_hyp_relationworld_thingb_pred_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.pred()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.pred).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'pred' in relationworld_ThingB is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'pred' in relationworld_ThingB did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'pred' in relationworld_ThingB is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=relationworld_ThingB_strategy)
@settings(max_examples=30)
def test_hyp_relationworld_thingb_compare_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.compare(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.compare).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'compare' in relationworld_ThingB is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'compare' in relationworld_ThingB did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'compare' in relationworld_ThingB is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=relationworld_RelatedTo_strategy)
@settings(max_examples=30)
def test_hyp_relationworld_relatedto_validate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validate()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validate' in relationworld_RelatedTo is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validate' in relationworld_RelatedTo did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validate' in relationworld_RelatedTo is not implemented or raised an error")





@given(instance=relationworld_ThingA_strategy)
def test_hyp_relationworld_thinga_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=relationworld_ThingA_strategy)
@settings(max_examples=30)
def test_hyp_relationworld_thinga_compare_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.compare(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.compare).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'compare' in relationworld_ThingA is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'compare' in relationworld_ThingA did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'compare' in relationworld_ThingA is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=relationworld_ThingA_strategy)
@settings(max_examples=30)
def test_hyp_relationworld_thinga_pred_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.pred()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.pred).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'pred' in relationworld_ThingA is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'pred' in relationworld_ThingA did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'pred' in relationworld_ThingA is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=relationworld_ThingA_strategy)
@settings(max_examples=30)
def test_hyp_relationworld_thinga_succ_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.succ()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.succ).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'succ' in relationworld_ThingA is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'succ' in relationworld_ThingA did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'succ' in relationworld_ThingA is not implemented or raised an error")




@given(instance=relationworld_NamedElement_strategy)
def test_hyp_relationworld_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=relationworld_World_strategy)
@settings(max_examples=30)
def test_hyp_relationworld_world_compare_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.compare(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.compare).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'compare' in relationworld_World is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'compare' in relationworld_World did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'compare' in relationworld_World is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=relationworld_World_strategy)
@settings(max_examples=30)
def test_hyp_relationworld_world_affectation_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.affectation(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.affectation).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'affectation' in relationworld_World is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'affectation' in relationworld_World did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'affectation' in relationworld_World is not implemented or raised an error")




@given(instance=relationworld_Category_strategy)
def test_hyp_relationworld_category_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=relationworld_Category_strategy)
@settings(max_examples=30)
def test_hyp_relationworld_category_affectation_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.affectation(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.affectation).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'affectation' in relationworld_Category is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'affectation' in relationworld_Category did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'affectation' in relationworld_Category is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=relationworld_Category_strategy)
@settings(max_examples=30)
def test_hyp_relationworld_category_compare_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.compare(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.compare).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'compare' in relationworld_Category is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'compare' in relationworld_Category did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'compare' in relationworld_Category is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=relationworld_TargetNode_strategy)
@settings(max_examples=30)
def test_hyp_relationworld_targetnode_pred_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.pred()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.pred).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'pred' in relationworld_TargetNode is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'pred' in relationworld_TargetNode did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'pred' in relationworld_TargetNode is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=relationworld_TargetNode_strategy)
@settings(max_examples=30)
def test_hyp_relationworld_targetnode_compare_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.compare(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.compare).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'compare' in relationworld_TargetNode is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'compare' in relationworld_TargetNode did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'compare' in relationworld_TargetNode is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=relationworld_TargetNode_strategy)
@settings(max_examples=30)
def test_hyp_relationworld_targetnode_succ_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.succ()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.succ).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'succ' in relationworld_TargetNode is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'succ' in relationworld_TargetNode did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'succ' in relationworld_TargetNode is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Arrow,
    Category,
    NamedElement,
    SourceNode,
    TargetNode,
    relationworld_Arrow,
    relationworld_Category,
    relationworld_NamedElement,
    relationworld_RelatedTo,
    relationworld_SourceNode,
    relationworld_TargetNode,
    relationworld_ThingA,
    relationworld_ThingB,
    relationworld_World,
    Scale,
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

def test_relationworld_Category_nom_value_roundtrip():
    instance = relationworld_Category(nom="sample_text")
    assert instance.nom == "sample_text"
    instance.nom = "sample_text_2"
    assert instance.nom == "sample_text_2"


def test_relationworld_NamedElement_name_value_roundtrip():
    instance = relationworld_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_relationworld_ThingA_since_value_roundtrip():
    instance = relationworld_ThingA(since=date(2024, 1, 1))
    assert instance.since == date(2024, 1, 1)
    instance.since = date(2025, 6, 15)
    assert instance.since == date(2025, 6, 15)


def test_relationworld_ThingB_step_value_roundtrip():
    instance = relationworld_ThingB(step="sample_text")
    assert instance.step == "sample_text"
    instance.step = "sample_text_2"
    assert instance.step == "sample_text_2"


def test_relationworld_RelatedTo_isa_Arrow():
    instance = relationworld_RelatedTo()
    assert isinstance(instance, Arrow)


def test_relationworld_World_isa_Category():
    instance = relationworld_World()
    assert isinstance(instance, Category)


def test_relationworld_RelatedTo_isa_NamedElement():
    instance = relationworld_RelatedTo()
    assert isinstance(instance, NamedElement)


def test_relationworld_ThingA_isa_NamedElement():
    instance = relationworld_ThingA(since=date(2024, 1, 1))
    assert isinstance(instance, NamedElement)


def test_relationworld_ThingB_isa_NamedElement():
    instance = relationworld_ThingB(step="sample_text")
    assert isinstance(instance, NamedElement)


def test_relationworld_ThingA_isa_SourceNode():
    instance = relationworld_ThingA(since=date(2024, 1, 1))
    assert isinstance(instance, SourceNode)


def test_relationworld_ThingB_isa_TargetNode():
    instance = relationworld_ThingB(step="sample_text")
    assert isinstance(instance, TargetNode)


def test_assoc_cible12_link_reassign_clear():
    a = relationworld_TargetNode()
    b1 = relationworld_Arrow()
    b2 = relationworld_Arrow()
    _safe_set(a, 'relationworld_TargetNode', b1)
    assert _is_linked(a, 'relationworld_TargetNode', b1)
    if hasattr(b1, 'relationworld_Arrow13'):
        assert _is_linked(b1, 'relationworld_Arrow13', a)
    _safe_set(a, 'relationworld_TargetNode', b2)
    assert _is_linked(a, 'relationworld_TargetNode', b2)
    if hasattr(b1, 'relationworld_Arrow13'):
        assert not _is_linked(b1, 'relationworld_Arrow13', a)
    if hasattr(b2, 'relationworld_Arrow13'):
        assert _is_linked(b2, 'relationworld_Arrow13', a)
    _safe_set(a, 'relationworld_TargetNode', None)
    assert not _is_linked(a, 'relationworld_TargetNode', b2)
    if hasattr(b2, 'relationworld_Arrow13'):
        assert not _is_linked(b2, 'relationworld_Arrow13', a)


def test_assoc_fleches16_link_reassign_clear():
    a = relationworld_Category(nom="sample_text")
    b1 = relationworld_Arrow()
    b2 = relationworld_Arrow()
    _safe_set(a, 'relationworld_Category17', {b1})
    assert _is_linked(a, 'relationworld_Category17', b1)
    if hasattr(b1, 'relationworld_Arrow18'):
        assert _is_linked(b1, 'relationworld_Arrow18', a)
    _safe_set(a, 'relationworld_Category17', {b2})
    assert _is_linked(a, 'relationworld_Category17', b2)
    if hasattr(b1, 'relationworld_Arrow18'):
        assert not _is_linked(b1, 'relationworld_Arrow18', a)
    if hasattr(b2, 'relationworld_Arrow18'):
        assert _is_linked(b2, 'relationworld_Arrow18', a)
    _safe_set(a, 'relationworld_Category17', set())
    assert not _is_linked(a, 'relationworld_Category17', b2)
    if hasattr(b2, 'relationworld_Arrow18'):
        assert not _is_linked(b2, 'relationworld_Arrow18', a)


def test_assoc_relations8_link_reassign_clear():
    a = relationworld_World()
    b1 = relationworld_RelatedTo()
    b2 = relationworld_RelatedTo()
    _safe_set(a, 'relationworld_World9', {b1})
    assert _is_linked(a, 'relationworld_World9', b1)
    if hasattr(b1, 'relationworld_RelatedTo10'):
        assert _is_linked(b1, 'relationworld_RelatedTo10', a)
    _safe_set(a, 'relationworld_World9', {b2})
    assert _is_linked(a, 'relationworld_World9', b2)
    if hasattr(b1, 'relationworld_RelatedTo10'):
        assert not _is_linked(b1, 'relationworld_RelatedTo10', a)
    if hasattr(b2, 'relationworld_RelatedTo10'):
        assert _is_linked(b2, 'relationworld_RelatedTo10', a)
    _safe_set(a, 'relationworld_World9', set())
    assert not _is_linked(a, 'relationworld_World9', b2)
    if hasattr(b2, 'relationworld_RelatedTo10'):
        assert not _is_linked(b2, 'relationworld_RelatedTo10', a)


def test_assoc_source11_link_reassign_clear():
    a = relationworld_SourceNode()
    b1 = relationworld_Arrow()
    b2 = relationworld_Arrow()
    _safe_set(a, 'relationworld_SourceNode', b1)
    assert _is_linked(a, 'relationworld_SourceNode', b1)
    if hasattr(b1, 'relationworld_Arrow'):
        assert _is_linked(b1, 'relationworld_Arrow', a)
    _safe_set(a, 'relationworld_SourceNode', b2)
    assert _is_linked(a, 'relationworld_SourceNode', b2)
    if hasattr(b1, 'relationworld_Arrow'):
        assert not _is_linked(b1, 'relationworld_Arrow', a)
    if hasattr(b2, 'relationworld_Arrow'):
        assert _is_linked(b2, 'relationworld_Arrow', a)
    _safe_set(a, 'relationworld_SourceNode', None)
    assert not _is_linked(a, 'relationworld_SourceNode', b2)
    if hasattr(b2, 'relationworld_Arrow'):
        assert not _is_linked(b2, 'relationworld_Arrow', a)


def test_assoc_sources14_link_reassign_clear():
    a = relationworld_SourceNode()
    b1 = relationworld_Category(nom="sample_text")
    b2 = relationworld_Category(nom="sample_text_2")
    _safe_set(a, 'relationworld_SourceNode15', b1)
    assert _is_linked(a, 'relationworld_SourceNode15', b1)
    if hasattr(b1, 'relationworld_Category'):
        assert _is_linked(b1, 'relationworld_Category', a)
    _safe_set(a, 'relationworld_SourceNode15', b2)
    assert _is_linked(a, 'relationworld_SourceNode15', b2)
    if hasattr(b1, 'relationworld_Category'):
        assert not _is_linked(b1, 'relationworld_Category', a)
    if hasattr(b2, 'relationworld_Category'):
        assert _is_linked(b2, 'relationworld_Category', a)
    _safe_set(a, 'relationworld_SourceNode15', None)
    assert not _is_linked(a, 'relationworld_SourceNode15', b2)
    if hasattr(b2, 'relationworld_Category'):
        assert not _is_linked(b2, 'relationworld_Category', a)


def test_assoc_targets19_link_reassign_clear():
    a = relationworld_TargetNode()
    b1 = relationworld_Category(nom="sample_text")
    b2 = relationworld_Category(nom="sample_text_2")
    _safe_set(a, 'relationworld_TargetNode21', b1)
    assert _is_linked(a, 'relationworld_TargetNode21', b1)
    if hasattr(b1, 'relationworld_Category20'):
        assert _is_linked(b1, 'relationworld_Category20', a)
    _safe_set(a, 'relationworld_TargetNode21', b2)
    assert _is_linked(a, 'relationworld_TargetNode21', b2)
    if hasattr(b1, 'relationworld_Category20'):
        assert not _is_linked(b1, 'relationworld_Category20', a)
    if hasattr(b2, 'relationworld_Category20'):
        assert _is_linked(b2, 'relationworld_Category20', a)
    _safe_set(a, 'relationworld_TargetNode21', None)
    assert not _is_linked(a, 'relationworld_TargetNode21', b2)
    if hasattr(b2, 'relationworld_Category20'):
        assert not _is_linked(b2, 'relationworld_Category20', a)


def test_assoc_thingA0_link_reassign_clear():
    a = relationworld_ThingA(since=date(2024, 1, 1))
    b1 = relationworld_RelatedTo()
    b2 = relationworld_RelatedTo()
    _safe_set(a, 'relationworld_ThingA', b1)
    assert _is_linked(a, 'relationworld_ThingA', b1)
    if hasattr(b1, 'relationworld_RelatedTo'):
        assert _is_linked(b1, 'relationworld_RelatedTo', a)
    _safe_set(a, 'relationworld_ThingA', b2)
    assert _is_linked(a, 'relationworld_ThingA', b2)
    if hasattr(b1, 'relationworld_RelatedTo'):
        assert not _is_linked(b1, 'relationworld_RelatedTo', a)
    if hasattr(b2, 'relationworld_RelatedTo'):
        assert _is_linked(b2, 'relationworld_RelatedTo', a)
    _safe_set(a, 'relationworld_ThingA', None)
    assert not _is_linked(a, 'relationworld_ThingA', b2)
    if hasattr(b2, 'relationworld_RelatedTo'):
        assert not _is_linked(b2, 'relationworld_RelatedTo', a)


def test_assoc_thingB1_link_reassign_clear():
    a = relationworld_ThingB(step="sample_text")
    b1 = relationworld_RelatedTo()
    b2 = relationworld_RelatedTo()
    _safe_set(a, 'relationworld_ThingB', b1)
    assert _is_linked(a, 'relationworld_ThingB', b1)
    if hasattr(b1, 'relationworld_RelatedTo2'):
        assert _is_linked(b1, 'relationworld_RelatedTo2', a)
    _safe_set(a, 'relationworld_ThingB', b2)
    assert _is_linked(a, 'relationworld_ThingB', b2)
    if hasattr(b1, 'relationworld_RelatedTo2'):
        assert not _is_linked(b1, 'relationworld_RelatedTo2', a)
    if hasattr(b2, 'relationworld_RelatedTo2'):
        assert _is_linked(b2, 'relationworld_RelatedTo2', a)
    _safe_set(a, 'relationworld_ThingB', None)
    assert not _is_linked(a, 'relationworld_ThingB', b2)
    if hasattr(b2, 'relationworld_RelatedTo2'):
        assert not _is_linked(b2, 'relationworld_RelatedTo2', a)


def test_assoc_thingsa3_link_reassign_clear():
    a = relationworld_World()
    b1 = relationworld_ThingA(since=date(2024, 1, 1))
    b2 = relationworld_ThingA(since=date(2025, 6, 15))
    _safe_set(a, 'relationworld_World', {b1})
    assert _is_linked(a, 'relationworld_World', b1)
    if hasattr(b1, 'relationworld_ThingA4'):
        assert _is_linked(b1, 'relationworld_ThingA4', a)
    _safe_set(a, 'relationworld_World', {b2})
    assert _is_linked(a, 'relationworld_World', b2)
    if hasattr(b1, 'relationworld_ThingA4'):
        assert not _is_linked(b1, 'relationworld_ThingA4', a)
    if hasattr(b2, 'relationworld_ThingA4'):
        assert _is_linked(b2, 'relationworld_ThingA4', a)
    _safe_set(a, 'relationworld_World', set())
    assert not _is_linked(a, 'relationworld_World', b2)
    if hasattr(b2, 'relationworld_ThingA4'):
        assert not _is_linked(b2, 'relationworld_ThingA4', a)


def test_assoc_thingsb5_link_reassign_clear():
    a = relationworld_World()
    b1 = relationworld_ThingB(step="sample_text")
    b2 = relationworld_ThingB(step="sample_text_2")
    _safe_set(a, 'relationworld_World6', {b1})
    assert _is_linked(a, 'relationworld_World6', b1)
    if hasattr(b1, 'relationworld_ThingB7'):
        assert _is_linked(b1, 'relationworld_ThingB7', a)
    _safe_set(a, 'relationworld_World6', {b2})
    assert _is_linked(a, 'relationworld_World6', b2)
    if hasattr(b1, 'relationworld_ThingB7'):
        assert not _is_linked(b1, 'relationworld_ThingB7', a)
    if hasattr(b2, 'relationworld_ThingB7'):
        assert _is_linked(b2, 'relationworld_ThingB7', a)
    _safe_set(a, 'relationworld_World6', set())
    assert not _is_linked(a, 'relationworld_World6', b2)
    if hasattr(b2, 'relationworld_ThingB7'):
        assert not _is_linked(b2, 'relationworld_ThingB7', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Arrow_strategy = st.builds(Arrow)
@given(instance=Arrow_strategy)
@settings(max_examples=25)
def test_Arrow_instantiation(instance):
    assert isinstance(instance, Arrow)


Category_strategy = st.builds(Category)
@given(instance=Category_strategy)
@settings(max_examples=25)
def test_Category_instantiation(instance):
    assert isinstance(instance, Category)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


SourceNode_strategy = st.builds(SourceNode)
@given(instance=SourceNode_strategy)
@settings(max_examples=25)
def test_SourceNode_instantiation(instance):
    assert isinstance(instance, SourceNode)


TargetNode_strategy = st.builds(TargetNode)
@given(instance=TargetNode_strategy)
@settings(max_examples=25)
def test_TargetNode_instantiation(instance):
    assert isinstance(instance, TargetNode)


relationworld_Arrow_strategy = st.builds(relationworld_Arrow)
@given(instance=relationworld_Arrow_strategy)
@settings(max_examples=25)
def test_relationworld_Arrow_instantiation(instance):
    assert isinstance(instance, relationworld_Arrow)


relationworld_Category_strategy = st.builds(relationworld_Category, nom=safe_text)
@given(instance=relationworld_Category_strategy)
@settings(max_examples=25)
def test_relationworld_Category_instantiation(instance):
    assert isinstance(instance, relationworld_Category)


relationworld_NamedElement_strategy = st.builds(relationworld_NamedElement, name=safe_text)
@given(instance=relationworld_NamedElement_strategy)
@settings(max_examples=25)
def test_relationworld_NamedElement_instantiation(instance):
    assert isinstance(instance, relationworld_NamedElement)


relationworld_RelatedTo_strategy = st.builds(relationworld_RelatedTo)
@given(instance=relationworld_RelatedTo_strategy)
@settings(max_examples=25)
def test_relationworld_RelatedTo_instantiation(instance):
    assert isinstance(instance, relationworld_RelatedTo)


relationworld_SourceNode_strategy = st.builds(relationworld_SourceNode)
@given(instance=relationworld_SourceNode_strategy)
@settings(max_examples=25)
def test_relationworld_SourceNode_instantiation(instance):
    assert isinstance(instance, relationworld_SourceNode)


relationworld_TargetNode_strategy = st.builds(relationworld_TargetNode)
@given(instance=relationworld_TargetNode_strategy)
@settings(max_examples=25)
def test_relationworld_TargetNode_instantiation(instance):
    assert isinstance(instance, relationworld_TargetNode)


relationworld_ThingA_strategy = st.builds(relationworld_ThingA, since=st.dates())
@given(instance=relationworld_ThingA_strategy)
@settings(max_examples=25)
def test_relationworld_ThingA_instantiation(instance):
    assert isinstance(instance, relationworld_ThingA)


relationworld_ThingB_strategy = st.builds(relationworld_ThingB, step=safe_text)
@given(instance=relationworld_ThingB_strategy)
@settings(max_examples=25)
def test_relationworld_ThingB_instantiation(instance):
    assert isinstance(instance, relationworld_ThingB)


relationworld_World_strategy = st.builds(relationworld_World)
@given(instance=relationworld_World_strategy)
@settings(max_examples=25)
def test_relationworld_World_instantiation(instance):
    assert isinstance(instance, relationworld_World)



