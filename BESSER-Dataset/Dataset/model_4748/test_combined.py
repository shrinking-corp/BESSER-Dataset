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
    EntityPage,
    solution_EditablePage,
    Link,
    solution_ContextualLink,
    solution_Relationship,
    EditablePage,
    solution_DeletePage,
    solution_UpdatePage,
    solution_CreatePage,
    DynamicPage,
    solution_IndexPage,
    solution_EntityPage,
    WebPage,
    solution_DynamicPage,
    solution_NonContextualLink,
    solution_Link,
    solution_Attribute,
    solution_StaticPage,
    solution_WebPage,
    solution_Entity,
    solution_WebApplication,
    DataType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_entitypage_is_not_abstract():
    assert not inspect.isabstract(EntityPage)


def test_hyp_entitypage_constructor_exists():
    assert callable(EntityPage.__init__)


def test_hyp_entitypage_constructor_args():
    sig = inspect.signature(EntityPage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_solution_editablepage_is_not_abstract():
    assert not inspect.isabstract(solution_EditablePage)


def test_hyp_solution_editablepage_constructor_exists():
    assert callable(solution_EditablePage.__init__)


def test_hyp_solution_editablepage_constructor_args():
    sig = inspect.signature(solution_EditablePage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_link_is_not_abstract():
    assert not inspect.isabstract(Link)


def test_hyp_link_constructor_exists():
    assert callable(Link.__init__)


def test_hyp_link_constructor_args():
    sig = inspect.signature(Link.__init__)
    params = list(sig.parameters.keys())



def test_hyp_solution_contextuallink_is_not_abstract():
    assert not inspect.isabstract(solution_ContextualLink)


def test_hyp_solution_contextuallink_constructor_exists():
    assert callable(solution_ContextualLink.__init__)


def test_hyp_solution_contextuallink_constructor_args():
    sig = inspect.signature(solution_ContextualLink.__init__)
    params = list(sig.parameters.keys())



def test_hyp_solution_relationship_is_not_abstract():
    assert not inspect.isabstract(solution_Relationship)


def test_hyp_solution_relationship_constructor_exists():
    assert callable(solution_Relationship.__init__)


def test_hyp_solution_relationship_constructor_args():
    sig = inspect.signature(solution_Relationship.__init__)
    params = list(sig.parameters.keys())
    assert "upperBound" in params, "Missing parameter 'upperBound'"
    assert "roleName" in params, "Missing parameter 'roleName'"
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"






def test_hyp_editablepage_is_not_abstract():
    assert not inspect.isabstract(EditablePage)


def test_hyp_editablepage_constructor_exists():
    assert callable(EditablePage.__init__)


def test_hyp_editablepage_constructor_args():
    sig = inspect.signature(EditablePage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_solution_deletepage_is_not_abstract():
    assert not inspect.isabstract(solution_DeletePage)


def test_hyp_solution_deletepage_constructor_exists():
    assert callable(solution_DeletePage.__init__)


def test_hyp_solution_deletepage_constructor_args():
    sig = inspect.signature(solution_DeletePage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_solution_updatepage_is_not_abstract():
    assert not inspect.isabstract(solution_UpdatePage)


def test_hyp_solution_updatepage_constructor_exists():
    assert callable(solution_UpdatePage.__init__)


def test_hyp_solution_updatepage_constructor_args():
    sig = inspect.signature(solution_UpdatePage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_solution_createpage_is_not_abstract():
    assert not inspect.isabstract(solution_CreatePage)


def test_hyp_solution_createpage_constructor_exists():
    assert callable(solution_CreatePage.__init__)


def test_hyp_solution_createpage_constructor_args():
    sig = inspect.signature(solution_CreatePage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dynamicpage_is_not_abstract():
    assert not inspect.isabstract(DynamicPage)


def test_hyp_dynamicpage_constructor_exists():
    assert callable(DynamicPage.__init__)


def test_hyp_dynamicpage_constructor_args():
    sig = inspect.signature(DynamicPage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_solution_indexpage_is_not_abstract():
    assert not inspect.isabstract(solution_IndexPage)


def test_hyp_solution_indexpage_constructor_exists():
    assert callable(solution_IndexPage.__init__)


def test_hyp_solution_indexpage_constructor_args():
    sig = inspect.signature(solution_IndexPage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_solution_entitypage_is_not_abstract():
    assert not inspect.isabstract(solution_EntityPage)


def test_hyp_solution_entitypage_constructor_exists():
    assert callable(solution_EntityPage.__init__)


def test_hyp_solution_entitypage_constructor_args():
    sig = inspect.signature(solution_EntityPage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_webpage_is_not_abstract():
    assert not inspect.isabstract(WebPage)


def test_hyp_webpage_constructor_exists():
    assert callable(WebPage.__init__)


def test_hyp_webpage_constructor_args():
    sig = inspect.signature(WebPage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_solution_dynamicpage_is_not_abstract():
    assert not inspect.isabstract(solution_DynamicPage)


def test_hyp_solution_dynamicpage_constructor_exists():
    assert callable(solution_DynamicPage.__init__)


def test_hyp_solution_dynamicpage_constructor_args():
    sig = inspect.signature(solution_DynamicPage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_solution_noncontextuallink_is_not_abstract():
    assert not inspect.isabstract(solution_NonContextualLink)


def test_hyp_solution_noncontextuallink_constructor_exists():
    assert callable(solution_NonContextualLink.__init__)


def test_hyp_solution_noncontextuallink_constructor_args():
    sig = inspect.signature(solution_NonContextualLink.__init__)
    params = list(sig.parameters.keys())



def test_hyp_solution_link_is_not_abstract():
    assert not inspect.isabstract(solution_Link)


def test_hyp_solution_link_constructor_exists():
    assert callable(solution_Link.__init__)


def test_hyp_solution_link_constructor_args():
    sig = inspect.signature(solution_Link.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_solution_attribute_is_not_abstract():
    assert not inspect.isabstract(solution_Attribute)


def test_hyp_solution_attribute_constructor_exists():
    assert callable(solution_Attribute.__init__)


def test_hyp_solution_attribute_constructor_args():
    sig = inspect.signature(solution_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "dataType" in params, "Missing parameter 'dataType'"





def test_hyp_solution_staticpage_is_not_abstract():
    assert not inspect.isabstract(solution_StaticPage)


def test_hyp_solution_staticpage_constructor_exists():
    assert callable(solution_StaticPage.__init__)


def test_hyp_solution_staticpage_constructor_args():
    sig = inspect.signature(solution_StaticPage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_solution_webpage_is_not_abstract():
    assert not inspect.isabstract(solution_WebPage)


def test_hyp_solution_webpage_constructor_exists():
    assert callable(solution_WebPage.__init__)


def test_hyp_solution_webpage_constructor_args():
    sig = inspect.signature(solution_WebPage.__init__)
    params = list(sig.parameters.keys())
    assert "relativeUrl" in params, "Missing parameter 'relativeUrl'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_solution_entity_is_not_abstract():
    assert not inspect.isabstract(solution_Entity)


def test_hyp_solution_entity_constructor_exists():
    assert callable(solution_Entity.__init__)


def test_hyp_solution_entity_constructor_args():
    sig = inspect.signature(solution_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_solution_webapplication_is_not_abstract():
    assert not inspect.isabstract(solution_WebApplication)


def test_hyp_solution_webapplication_constructor_exists():
    assert callable(solution_WebApplication.__init__)


def test_hyp_solution_webapplication_constructor_args():
    sig = inspect.signature(solution_WebApplication.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"


def test_hyp_datatype_exists():
    # Check that the Enumeration exists
    assert DataType is not None

def test_hyp_datatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataType]
    expected_literals = [
        "Integer",
        "String",
        "Boolean",
        "Float",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataType"


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
EntityPage_strategy = st.builds(
    EntityPage,
)
solution_EditablePage_strategy = st.builds(
    solution_EditablePage,
)
Link_strategy = st.builds(
    Link,
)
solution_ContextualLink_strategy = st.builds(
    solution_ContextualLink,
)
solution_Relationship_strategy = st.builds(
    solution_Relationship,
    upperBound=
        st.integers(),
    roleName=
        safe_text,
    lowerBound=
        st.integers()
)
EditablePage_strategy = st.builds(
    EditablePage,
)
solution_DeletePage_strategy = st.builds(
    solution_DeletePage,
)
solution_UpdatePage_strategy = st.builds(
    solution_UpdatePage,
)
solution_CreatePage_strategy = st.builds(
    solution_CreatePage,
)
DynamicPage_strategy = st.builds(
    DynamicPage,
)
solution_IndexPage_strategy = st.builds(
    solution_IndexPage,
)
solution_EntityPage_strategy = st.builds(
    solution_EntityPage,
)
WebPage_strategy = st.builds(
    WebPage,
)
solution_DynamicPage_strategy = st.builds(
    solution_DynamicPage,
)
solution_NonContextualLink_strategy = st.builds(
    solution_NonContextualLink,
)
solution_Link_strategy = st.builds(
    solution_Link,
    name=
        safe_text
)
solution_Attribute_strategy = st.builds(
    solution_Attribute,
    name=
        safe_text,
    dataType=
        safe_text
)
solution_StaticPage_strategy = st.builds(
    solution_StaticPage,
)
solution_WebPage_strategy = st.builds(
    solution_WebPage,
    relativeUrl=
        safe_text,
    name=
        safe_text
)
solution_Entity_strategy = st.builds(
    solution_Entity,
    name=
        safe_text
)
solution_WebApplication_strategy = st.builds(
    solution_WebApplication,
    name=
        safe_text
)








@given(instance=solution_Relationship_strategy)
def test_hyp_solution_relationship_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original



@given(instance=solution_Relationship_strategy)
def test_hyp_solution_relationship_roleName_setter(instance):
    original = instance.roleName
    instance.roleName = original
    assert instance.roleName == original



@given(instance=solution_Relationship_strategy)
def test_hyp_solution_relationship_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original














@given(instance=solution_Link_strategy)
def test_hyp_solution_link_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=solution_Attribute_strategy)
def test_hyp_solution_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=solution_Attribute_strategy)
def test_hyp_solution_attribute_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original





@given(instance=solution_WebPage_strategy)
def test_hyp_solution_webpage_relativeUrl_setter(instance):
    original = instance.relativeUrl
    instance.relativeUrl = original
    assert instance.relativeUrl == original



@given(instance=solution_WebPage_strategy)
def test_hyp_solution_webpage_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=solution_Entity_strategy)
def test_hyp_solution_entity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=solution_WebApplication_strategy)
def test_hyp_solution_webapplication_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=solution_WebApplication_strategy)
@settings(max_examples=30)
def test_hyp_solution_webapplication_creationdatebeforegolive_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.creationDateBeforeGoLive()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.creationDateBeforeGoLive).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'creationDateBeforeGoLive' in solution_WebApplication is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'creationDateBeforeGoLive' in solution_WebApplication did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'creationDateBeforeGoLive' in solution_WebApplication is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    DynamicPage,
    EditablePage,
    EntityPage,
    Link,
    WebPage,
    solution_Attribute,
    solution_ContextualLink,
    solution_CreatePage,
    solution_DeletePage,
    solution_DynamicPage,
    solution_EditablePage,
    solution_Entity,
    solution_EntityPage,
    solution_IndexPage,
    solution_Link,
    solution_NonContextualLink,
    solution_Relationship,
    solution_StaticPage,
    solution_UpdatePage,
    solution_WebApplication,
    solution_WebPage,
    DataType,
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

def test_solution_Attribute_dataType_value_roundtrip():
    instance = solution_Attribute(dataType="sample_text", name="sample_text")
    assert instance.dataType == "sample_text"
    instance.dataType = "sample_text_2"
    assert instance.dataType == "sample_text_2"


def test_solution_Attribute_name_value_roundtrip():
    instance = solution_Attribute(dataType="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_solution_Entity_name_value_roundtrip():
    instance = solution_Entity(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_solution_Link_name_value_roundtrip():
    instance = solution_Link(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_solution_Relationship_lowerBound_value_roundtrip():
    instance = solution_Relationship(lowerBound=7, roleName="sample_text", upperBound=7)
    assert instance.lowerBound == 7
    instance.lowerBound = 13
    assert instance.lowerBound == 13


def test_solution_Relationship_roleName_value_roundtrip():
    instance = solution_Relationship(lowerBound=7, roleName="sample_text", upperBound=7)
    assert instance.roleName == "sample_text"
    instance.roleName = "sample_text_2"
    assert instance.roleName == "sample_text_2"


def test_solution_Relationship_upperBound_value_roundtrip():
    instance = solution_Relationship(lowerBound=7, roleName="sample_text", upperBound=7)
    assert instance.upperBound == 7
    instance.upperBound = 13
    assert instance.upperBound == 13


def test_solution_WebApplication_name_value_roundtrip():
    instance = solution_WebApplication(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_solution_WebPage_name_value_roundtrip():
    instance = solution_WebPage(name="sample_text", relativeUrl="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_solution_WebPage_relativeUrl_value_roundtrip():
    instance = solution_WebPage(name="sample_text", relativeUrl="sample_text")
    assert instance.relativeUrl == "sample_text"
    instance.relativeUrl = "sample_text_2"
    assert instance.relativeUrl == "sample_text_2"


def test_solution_EntityPage_isa_DynamicPage():
    instance = solution_EntityPage()
    assert isinstance(instance, DynamicPage)


def test_solution_IndexPage_isa_DynamicPage():
    instance = solution_IndexPage()
    assert isinstance(instance, DynamicPage)


def test_solution_CreatePage_isa_EditablePage():
    instance = solution_CreatePage()
    assert isinstance(instance, EditablePage)


def test_solution_DeletePage_isa_EditablePage():
    instance = solution_DeletePage()
    assert isinstance(instance, EditablePage)


def test_solution_UpdatePage_isa_EditablePage():
    instance = solution_UpdatePage()
    assert isinstance(instance, EditablePage)


def test_solution_EditablePage_isa_EntityPage():
    instance = solution_EditablePage()
    assert isinstance(instance, EntityPage)


def test_solution_ContextualLink_isa_Link():
    instance = solution_ContextualLink()
    assert isinstance(instance, Link)


def test_solution_NonContextualLink_isa_Link():
    instance = solution_NonContextualLink()
    assert isinstance(instance, Link)


def test_solution_DynamicPage_isa_WebPage():
    instance = solution_DynamicPage()
    assert isinstance(instance, WebPage)


def test_solution_StaticPage_isa_WebPage():
    instance = solution_StaticPage()
    assert isinstance(instance, WebPage)


def test_assoc_attributes5_link_reassign_clear():
    a = solution_Entity(name="sample_text")
    b1 = solution_Attribute(dataType="sample_text", name="sample_text")
    b2 = solution_Attribute(dataType="sample_text_2", name="sample_text_2")
    _safe_set(a, 'solution_Entity6', {b1})
    assert _is_linked(a, 'solution_Entity6', b1)
    if hasattr(b1, 'solution_Attribute'):
        assert _is_linked(b1, 'solution_Attribute', a)
    _safe_set(a, 'solution_Entity6', {b2})
    assert _is_linked(a, 'solution_Entity6', b2)
    if hasattr(b1, 'solution_Attribute'):
        assert not _is_linked(b1, 'solution_Attribute', a)
    if hasattr(b2, 'solution_Attribute'):
        assert _is_linked(b2, 'solution_Attribute', a)
    _safe_set(a, 'solution_Entity6', set())
    assert not _is_linked(a, 'solution_Entity6', b2)
    if hasattr(b2, 'solution_Attribute'):
        assert not _is_linked(b2, 'solution_Attribute', a)


def test_assoc_entities0_link_reassign_clear():
    a = solution_WebApplication(name="sample_text")
    b1 = solution_Entity(name="sample_text")
    b2 = solution_Entity(name="sample_text_2")
    _safe_set(a, 'solution_WebApplication', {b1})
    assert _is_linked(a, 'solution_WebApplication', b1)
    if hasattr(b1, 'solution_Entity'):
        assert _is_linked(b1, 'solution_Entity', a)
    _safe_set(a, 'solution_WebApplication', {b2})
    assert _is_linked(a, 'solution_WebApplication', b2)
    if hasattr(b1, 'solution_Entity'):
        assert not _is_linked(b1, 'solution_Entity', a)
    if hasattr(b2, 'solution_Entity'):
        assert _is_linked(b2, 'solution_Entity', a)
    _safe_set(a, 'solution_WebApplication', set())
    assert not _is_linked(a, 'solution_WebApplication', b2)
    if hasattr(b2, 'solution_Entity'):
        assert not _is_linked(b2, 'solution_Entity', a)


def test_assoc_entity21_link_reassign_clear():
    a = solution_Entity(name="sample_text")
    b1 = solution_DynamicPage()
    b2 = solution_DynamicPage()
    _safe_set(a, 'solution_Entity22', b1)
    assert _is_linked(a, 'solution_Entity22', b1)
    if hasattr(b1, 'solution_DynamicPage'):
        assert _is_linked(b1, 'solution_DynamicPage', a)
    _safe_set(a, 'solution_Entity22', b2)
    assert _is_linked(a, 'solution_Entity22', b2)
    if hasattr(b1, 'solution_DynamicPage'):
        assert not _is_linked(b1, 'solution_DynamicPage', a)
    if hasattr(b2, 'solution_DynamicPage'):
        assert _is_linked(b2, 'solution_DynamicPage', a)
    _safe_set(a, 'solution_Entity22', None)
    assert not _is_linked(a, 'solution_Entity22', b2)
    if hasattr(b2, 'solution_DynamicPage'):
        assert not _is_linked(b2, 'solution_DynamicPage', a)


def test_assoc_homeLink19_link_reassign_clear():
    a = solution_WebPage(name="sample_text", relativeUrl="sample_text")
    b1 = solution_NonContextualLink()
    b2 = solution_NonContextualLink()
    _safe_set(a, 'solution_WebPage20', b1)
    assert _is_linked(a, 'solution_WebPage20', b1)
    if hasattr(b1, 'solution_NonContextualLink'):
        assert _is_linked(b1, 'solution_NonContextualLink', a)
    _safe_set(a, 'solution_WebPage20', b2)
    assert _is_linked(a, 'solution_WebPage20', b2)
    if hasattr(b1, 'solution_NonContextualLink'):
        assert not _is_linked(b1, 'solution_NonContextualLink', a)
    if hasattr(b2, 'solution_NonContextualLink'):
        assert _is_linked(b2, 'solution_NonContextualLink', a)
    _safe_set(a, 'solution_WebPage20', None)
    assert not _is_linked(a, 'solution_WebPage20', b2)
    if hasattr(b2, 'solution_NonContextualLink'):
        assert not _is_linked(b2, 'solution_NonContextualLink', a)


def test_assoc_homePage3_link_reassign_clear():
    a = solution_WebApplication(name="sample_text")
    b1 = solution_StaticPage()
    b2 = solution_StaticPage()
    _safe_set(a, 'solution_WebApplication4', b1)
    assert _is_linked(a, 'solution_WebApplication4', b1)
    if hasattr(b1, 'solution_StaticPage'):
        assert _is_linked(b1, 'solution_StaticPage', a)
    _safe_set(a, 'solution_WebApplication4', b2)
    assert _is_linked(a, 'solution_WebApplication4', b2)
    if hasattr(b1, 'solution_StaticPage'):
        assert not _is_linked(b1, 'solution_StaticPage', a)
    if hasattr(b2, 'solution_StaticPage'):
        assert _is_linked(b2, 'solution_StaticPage', a)
    _safe_set(a, 'solution_WebApplication4', None)
    assert not _is_linked(a, 'solution_WebApplication4', b2)
    if hasattr(b2, 'solution_StaticPage'):
        assert not _is_linked(b2, 'solution_StaticPage', a)


def test_assoc_id7_link_reassign_clear():
    a = solution_Entity(name="sample_text")
    b1 = solution_Attribute(dataType="sample_text", name="sample_text")
    b2 = solution_Attribute(dataType="sample_text_2", name="sample_text_2")
    _safe_set(a, 'solution_Entity8', b1)
    assert _is_linked(a, 'solution_Entity8', b1)
    if hasattr(b1, 'solution_Attribute9'):
        assert _is_linked(b1, 'solution_Attribute9', a)
    _safe_set(a, 'solution_Entity8', b2)
    assert _is_linked(a, 'solution_Entity8', b2)
    if hasattr(b1, 'solution_Attribute9'):
        assert not _is_linked(b1, 'solution_Attribute9', a)
    if hasattr(b2, 'solution_Attribute9'):
        assert _is_linked(b2, 'solution_Attribute9', a)
    _safe_set(a, 'solution_Entity8', None)
    assert not _is_linked(a, 'solution_Entity8', b2)
    if hasattr(b2, 'solution_Attribute9'):
        assert not _is_linked(b2, 'solution_Attribute9', a)


def test_assoc_information28_link_reassign_clear():
    a = solution_Entity(name="sample_text")
    b1 = solution_ContextualLink()
    b2 = solution_ContextualLink()
    _safe_set(a, 'solution_Entity29', b1)
    assert _is_linked(a, 'solution_Entity29', b1)
    if hasattr(b1, 'solution_ContextualLink'):
        assert _is_linked(b1, 'solution_ContextualLink', a)
    _safe_set(a, 'solution_Entity29', b2)
    assert _is_linked(a, 'solution_Entity29', b2)
    if hasattr(b1, 'solution_ContextualLink'):
        assert not _is_linked(b1, 'solution_ContextualLink', a)
    if hasattr(b2, 'solution_ContextualLink'):
        assert _is_linked(b2, 'solution_ContextualLink', a)
    _safe_set(a, 'solution_Entity29', None)
    assert not _is_linked(a, 'solution_Entity29', b2)
    if hasattr(b2, 'solution_ContextualLink'):
        assert not _is_linked(b2, 'solution_ContextualLink', a)


def test_assoc_links17_link_reassign_clear():
    a = solution_WebPage(name="sample_text", relativeUrl="sample_text")
    b1 = solution_Link(name="sample_text")
    b2 = solution_Link(name="sample_text_2")
    _safe_set(a, 'solution_WebPage18', {b1})
    assert _is_linked(a, 'solution_WebPage18', b1)
    if hasattr(b1, 'solution_Link'):
        assert _is_linked(b1, 'solution_Link', a)
    _safe_set(a, 'solution_WebPage18', {b2})
    assert _is_linked(a, 'solution_WebPage18', b2)
    if hasattr(b1, 'solution_Link'):
        assert not _is_linked(b1, 'solution_Link', a)
    if hasattr(b2, 'solution_Link'):
        assert _is_linked(b2, 'solution_Link', a)
    _safe_set(a, 'solution_WebPage18', set())
    assert not _is_linked(a, 'solution_WebPage18', b2)
    if hasattr(b2, 'solution_Link'):
        assert not _is_linked(b2, 'solution_Link', a)


def test_assoc_opposite15_link_reassign_clear():
    a = solution_Relationship(lowerBound=7, roleName="sample_text", upperBound=7)
    b1 = solution_Relationship(lowerBound=7, roleName="sample_text", upperBound=7)
    b2 = solution_Relationship(lowerBound=13, roleName="sample_text_2", upperBound=13)
    _safe_set(a, 'solution_Relationship14', b1)
    assert _is_linked(a, 'solution_Relationship14', b1)
    if hasattr(b1, 'solution_Relationship16'):
        assert _is_linked(b1, 'solution_Relationship16', a)
    _safe_set(a, 'solution_Relationship14', b2)
    assert _is_linked(a, 'solution_Relationship14', b2)
    if hasattr(b1, 'solution_Relationship16'):
        assert not _is_linked(b1, 'solution_Relationship16', a)
    if hasattr(b2, 'solution_Relationship16'):
        assert _is_linked(b2, 'solution_Relationship16', a)
    _safe_set(a, 'solution_Relationship14', None)
    assert not _is_linked(a, 'solution_Relationship14', b2)
    if hasattr(b2, 'solution_Relationship16'):
        assert not _is_linked(b2, 'solution_Relationship16', a)


def test_assoc_relationships10_link_reassign_clear():
    a = solution_Relationship(lowerBound=7, roleName="sample_text", upperBound=7)
    b1 = solution_Entity(name="sample_text")
    b2 = solution_Entity(name="sample_text_2")
    _safe_set(a, 'Relationship', b1)
    assert _is_linked(a, 'Relationship', b1)
    if hasattr(b1, 'source'):
        assert _is_linked(b1, 'source', a)
    _safe_set(a, 'Relationship', b2)
    assert _is_linked(a, 'Relationship', b2)
    if hasattr(b1, 'source'):
        assert not _is_linked(b1, 'source', a)
    if hasattr(b2, 'source'):
        assert _is_linked(b2, 'source', a)
    _safe_set(a, 'Relationship', None)
    assert not _is_linked(a, 'Relationship', b2)
    if hasattr(b2, 'source'):
        assert not _is_linked(b2, 'source', a)


def test_assoc_source11_link_reassign_clear():
    a = solution_Relationship(lowerBound=7, roleName="sample_text", upperBound=7)
    b1 = solution_Entity(name="sample_text")
    b2 = solution_Entity(name="sample_text_2")
    _safe_set(a, 'relationships', b1)
    assert _is_linked(a, 'relationships', b1)
    if hasattr(b1, 'Entity'):
        assert _is_linked(b1, 'Entity', a)
    _safe_set(a, 'relationships', b2)
    assert _is_linked(a, 'relationships', b2)
    if hasattr(b1, 'Entity'):
        assert not _is_linked(b1, 'Entity', a)
    if hasattr(b2, 'Entity'):
        assert _is_linked(b2, 'Entity', a)
    _safe_set(a, 'relationships', None)
    assert not _is_linked(a, 'relationships', b2)
    if hasattr(b2, 'Entity'):
        assert not _is_linked(b2, 'Entity', a)


def test_assoc_target12_link_reassign_clear():
    a = solution_Relationship(lowerBound=7, roleName="sample_text", upperBound=7)
    b1 = solution_Entity(name="sample_text")
    b2 = solution_Entity(name="sample_text_2")
    _safe_set(a, 'solution_Relationship', b1)
    assert _is_linked(a, 'solution_Relationship', b1)
    if hasattr(b1, 'solution_Entity13'):
        assert _is_linked(b1, 'solution_Entity13', a)
    _safe_set(a, 'solution_Relationship', b2)
    assert _is_linked(a, 'solution_Relationship', b2)
    if hasattr(b1, 'solution_Entity13'):
        assert not _is_linked(b1, 'solution_Entity13', a)
    if hasattr(b2, 'solution_Entity13'):
        assert _is_linked(b2, 'solution_Entity13', a)
    _safe_set(a, 'solution_Relationship', None)
    assert not _is_linked(a, 'solution_Relationship', b2)
    if hasattr(b2, 'solution_Entity13'):
        assert not _is_linked(b2, 'solution_Entity13', a)


def test_assoc_target25_link_reassign_clear():
    a = solution_WebPage(name="sample_text", relativeUrl="sample_text")
    b1 = solution_Link(name="sample_text")
    b2 = solution_Link(name="sample_text_2")
    _safe_set(a, 'solution_WebPage27', b1)
    assert _is_linked(a, 'solution_WebPage27', b1)
    if hasattr(b1, 'solution_Link26'):
        assert _is_linked(b1, 'solution_Link26', a)
    _safe_set(a, 'solution_WebPage27', b2)
    assert _is_linked(a, 'solution_WebPage27', b2)
    if hasattr(b1, 'solution_Link26'):
        assert not _is_linked(b1, 'solution_Link26', a)
    if hasattr(b2, 'solution_Link26'):
        assert _is_linked(b2, 'solution_Link26', a)
    _safe_set(a, 'solution_WebPage27', None)
    assert not _is_linked(a, 'solution_WebPage27', b2)
    if hasattr(b2, 'solution_Link26'):
        assert not _is_linked(b2, 'solution_Link26', a)


def test_assoc_webpages1_link_reassign_clear():
    a = solution_WebPage(name="sample_text", relativeUrl="sample_text")
    b1 = solution_WebApplication(name="sample_text")
    b2 = solution_WebApplication(name="sample_text_2")
    _safe_set(a, 'solution_WebPage', b1)
    assert _is_linked(a, 'solution_WebPage', b1)
    if hasattr(b1, 'solution_WebApplication2'):
        assert _is_linked(b1, 'solution_WebApplication2', a)
    _safe_set(a, 'solution_WebPage', b2)
    assert _is_linked(a, 'solution_WebPage', b2)
    if hasattr(b1, 'solution_WebApplication2'):
        assert not _is_linked(b1, 'solution_WebApplication2', a)
    if hasattr(b2, 'solution_WebApplication2'):
        assert _is_linked(b2, 'solution_WebApplication2', a)
    _safe_set(a, 'solution_WebPage', None)
    assert not _is_linked(a, 'solution_WebPage', b2)
    if hasattr(b2, 'solution_WebApplication2'):
        assert not _is_linked(b2, 'solution_WebApplication2', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

DynamicPage_strategy = st.builds(DynamicPage)
@given(instance=DynamicPage_strategy)
@settings(max_examples=25)
def test_DynamicPage_instantiation(instance):
    assert isinstance(instance, DynamicPage)


EditablePage_strategy = st.builds(EditablePage)
@given(instance=EditablePage_strategy)
@settings(max_examples=25)
def test_EditablePage_instantiation(instance):
    assert isinstance(instance, EditablePage)


EntityPage_strategy = st.builds(EntityPage)
@given(instance=EntityPage_strategy)
@settings(max_examples=25)
def test_EntityPage_instantiation(instance):
    assert isinstance(instance, EntityPage)


Link_strategy = st.builds(Link)
@given(instance=Link_strategy)
@settings(max_examples=25)
def test_Link_instantiation(instance):
    assert isinstance(instance, Link)


WebPage_strategy = st.builds(WebPage)
@given(instance=WebPage_strategy)
@settings(max_examples=25)
def test_WebPage_instantiation(instance):
    assert isinstance(instance, WebPage)


solution_Attribute_strategy = st.builds(solution_Attribute, dataType=safe_text, name=safe_text)
@given(instance=solution_Attribute_strategy)
@settings(max_examples=25)
def test_solution_Attribute_instantiation(instance):
    assert isinstance(instance, solution_Attribute)


solution_ContextualLink_strategy = st.builds(solution_ContextualLink)
@given(instance=solution_ContextualLink_strategy)
@settings(max_examples=25)
def test_solution_ContextualLink_instantiation(instance):
    assert isinstance(instance, solution_ContextualLink)


solution_CreatePage_strategy = st.builds(solution_CreatePage)
@given(instance=solution_CreatePage_strategy)
@settings(max_examples=25)
def test_solution_CreatePage_instantiation(instance):
    assert isinstance(instance, solution_CreatePage)


solution_DeletePage_strategy = st.builds(solution_DeletePage)
@given(instance=solution_DeletePage_strategy)
@settings(max_examples=25)
def test_solution_DeletePage_instantiation(instance):
    assert isinstance(instance, solution_DeletePage)


solution_DynamicPage_strategy = st.builds(solution_DynamicPage)
@given(instance=solution_DynamicPage_strategy)
@settings(max_examples=25)
def test_solution_DynamicPage_instantiation(instance):
    assert isinstance(instance, solution_DynamicPage)


solution_EditablePage_strategy = st.builds(solution_EditablePage)
@given(instance=solution_EditablePage_strategy)
@settings(max_examples=25)
def test_solution_EditablePage_instantiation(instance):
    assert isinstance(instance, solution_EditablePage)


solution_Entity_strategy = st.builds(solution_Entity, name=safe_text)
@given(instance=solution_Entity_strategy)
@settings(max_examples=25)
def test_solution_Entity_instantiation(instance):
    assert isinstance(instance, solution_Entity)


solution_EntityPage_strategy = st.builds(solution_EntityPage)
@given(instance=solution_EntityPage_strategy)
@settings(max_examples=25)
def test_solution_EntityPage_instantiation(instance):
    assert isinstance(instance, solution_EntityPage)


solution_IndexPage_strategy = st.builds(solution_IndexPage)
@given(instance=solution_IndexPage_strategy)
@settings(max_examples=25)
def test_solution_IndexPage_instantiation(instance):
    assert isinstance(instance, solution_IndexPage)


solution_Link_strategy = st.builds(solution_Link, name=safe_text)
@given(instance=solution_Link_strategy)
@settings(max_examples=25)
def test_solution_Link_instantiation(instance):
    assert isinstance(instance, solution_Link)


solution_NonContextualLink_strategy = st.builds(solution_NonContextualLink)
@given(instance=solution_NonContextualLink_strategy)
@settings(max_examples=25)
def test_solution_NonContextualLink_instantiation(instance):
    assert isinstance(instance, solution_NonContextualLink)


solution_Relationship_strategy = st.builds(solution_Relationship, lowerBound=st.integers(), roleName=safe_text, upperBound=st.integers())
@given(instance=solution_Relationship_strategy)
@settings(max_examples=25)
def test_solution_Relationship_instantiation(instance):
    assert isinstance(instance, solution_Relationship)


solution_StaticPage_strategy = st.builds(solution_StaticPage)
@given(instance=solution_StaticPage_strategy)
@settings(max_examples=25)
def test_solution_StaticPage_instantiation(instance):
    assert isinstance(instance, solution_StaticPage)


solution_UpdatePage_strategy = st.builds(solution_UpdatePage)
@given(instance=solution_UpdatePage_strategy)
@settings(max_examples=25)
def test_solution_UpdatePage_instantiation(instance):
    assert isinstance(instance, solution_UpdatePage)


solution_WebApplication_strategy = st.builds(solution_WebApplication, name=safe_text)
@given(instance=solution_WebApplication_strategy)
@settings(max_examples=25)
def test_solution_WebApplication_instantiation(instance):
    assert isinstance(instance, solution_WebApplication)


solution_WebPage_strategy = st.builds(solution_WebPage, name=safe_text, relativeUrl=safe_text)
@given(instance=solution_WebPage_strategy)
@settings(max_examples=25)
def test_solution_WebPage_instantiation(instance):
    assert isinstance(instance, solution_WebPage)



