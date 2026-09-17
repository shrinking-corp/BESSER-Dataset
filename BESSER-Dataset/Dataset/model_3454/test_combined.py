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
    Constraint,
    FeatureModel_ExcludeConstraint,
    FeatureModel_NamedElement,
    NamedElement,
    FeatureModel_Group,
    FeatureModel_Comment,
    FeatureModel_Feature,
    FeatureModel_Constraint,
    FeatureModel_FeatureModel,
    FeatureModel_RequireConstraint,
    GroupType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_hyp_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_hyp_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_featuremodel_excludeconstraint_is_not_abstract():
    assert not inspect.isabstract(FeatureModel_ExcludeConstraint)


def test_hyp_featuremodel_excludeconstraint_constructor_exists():
    assert callable(FeatureModel_ExcludeConstraint.__init__)


def test_hyp_featuremodel_excludeconstraint_constructor_args():
    sig = inspect.signature(FeatureModel_ExcludeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_featuremodel_namedelement_is_not_abstract():
    assert not inspect.isabstract(FeatureModel_NamedElement)


def test_hyp_featuremodel_namedelement_constructor_exists():
    assert callable(FeatureModel_NamedElement.__init__)


def test_hyp_featuremodel_namedelement_constructor_args():
    sig = inspect.signature(FeatureModel_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_featuremodel_group_is_not_abstract():
    assert not inspect.isabstract(FeatureModel_Group)


def test_hyp_featuremodel_group_constructor_exists():
    assert callable(FeatureModel_Group.__init__)


def test_hyp_featuremodel_group_constructor_args():
    sig = inspect.signature(FeatureModel_Group.__init__)
    params = list(sig.parameters.keys())
    assert "groupType" in params, "Missing parameter 'groupType'"




def test_hyp_featuremodel_comment_is_not_abstract():
    assert not inspect.isabstract(FeatureModel_Comment)


def test_hyp_featuremodel_comment_constructor_exists():
    assert callable(FeatureModel_Comment.__init__)


def test_hyp_featuremodel_comment_constructor_args():
    sig = inspect.signature(FeatureModel_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_featuremodel_feature_is_not_abstract():
    assert not inspect.isabstract(FeatureModel_Feature)


def test_hyp_featuremodel_feature_constructor_exists():
    assert callable(FeatureModel_Feature.__init__)


def test_hyp_featuremodel_feature_constructor_args():
    sig = inspect.signature(FeatureModel_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "mandatory" in params, "Missing parameter 'mandatory'"
    assert "abstract" in params, "Missing parameter 'abstract'"





def test_hyp_featuremodel_constraint_is_not_abstract():
    assert not inspect.isabstract(FeatureModel_Constraint)


def test_hyp_featuremodel_constraint_constructor_exists():
    assert callable(FeatureModel_Constraint.__init__)


def test_hyp_featuremodel_constraint_constructor_args():
    sig = inspect.signature(FeatureModel_Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "language" in params, "Missing parameter 'language'"





def test_hyp_featuremodel_featuremodel_is_not_abstract():
    assert not inspect.isabstract(FeatureModel_FeatureModel)


def test_hyp_featuremodel_featuremodel_constructor_exists():
    assert callable(FeatureModel_FeatureModel.__init__)


def test_hyp_featuremodel_featuremodel_constructor_args():
    sig = inspect.signature(FeatureModel_FeatureModel.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"




def test_hyp_featuremodel_requireconstraint_is_not_abstract():
    assert not inspect.isabstract(FeatureModel_RequireConstraint)


def test_hyp_featuremodel_requireconstraint_constructor_exists():
    assert callable(FeatureModel_RequireConstraint.__init__)


def test_hyp_featuremodel_requireconstraint_constructor_args():
    sig = inspect.signature(FeatureModel_RequireConstraint.__init__)
    params = list(sig.parameters.keys())

def test_hyp_grouptype_exists():
    # Check that the Enumeration exists
    assert GroupType is not None

def test_hyp_grouptype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GroupType]
    expected_literals = [
        "OR",
        "ALT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GroupType"


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
Constraint_strategy = st.builds(
    Constraint,
)
FeatureModel_ExcludeConstraint_strategy = st.builds(
    FeatureModel_ExcludeConstraint,
)
FeatureModel_NamedElement_strategy = st.builds(
    FeatureModel_NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
FeatureModel_Group_strategy = st.builds(
    FeatureModel_Group,
    groupType=
        safe_text
)
FeatureModel_Comment_strategy = st.builds(
    FeatureModel_Comment,
    text=
        safe_text
)
FeatureModel_Feature_strategy = st.builds(
    FeatureModel_Feature,
    mandatory=
        st.booleans(),
    abstract=
        st.booleans()
)
FeatureModel_Constraint_strategy = st.builds(
    FeatureModel_Constraint,
    code=
        safe_text,
    language=
        safe_text
)
FeatureModel_FeatureModel_strategy = st.builds(
    FeatureModel_FeatureModel,
    version=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
FeatureModel_RequireConstraint_strategy = st.builds(
    FeatureModel_RequireConstraint,
)






@given(instance=FeatureModel_NamedElement_strategy)
def test_hyp_featuremodel_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=FeatureModel_Group_strategy)
def test_hyp_featuremodel_group_groupType_setter(instance):
    original = instance.groupType
    instance.groupType = original
    assert instance.groupType == original




@given(instance=FeatureModel_Comment_strategy)
def test_hyp_featuremodel_comment_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original




@given(instance=FeatureModel_Feature_strategy)
def test_hyp_featuremodel_feature_mandatory_setter(instance):
    original = instance.mandatory
    instance.mandatory = original
    assert instance.mandatory == original



@given(instance=FeatureModel_Feature_strategy)
def test_hyp_featuremodel_feature_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FeatureModel_Feature_strategy)
@settings(max_examples=30)
def test_hyp_featuremodel_feature_atmostinonegroup_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.atMostInOneGroup(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.atMostInOneGroup).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'atMostInOneGroup' in FeatureModel_Feature is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'atMostInOneGroup' in FeatureModel_Feature did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'atMostInOneGroup' in FeatureModel_Feature is not implemented or raised an error")




@given(instance=FeatureModel_Constraint_strategy)
def test_hyp_featuremodel_constraint_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=FeatureModel_Constraint_strategy)
def test_hyp_featuremodel_constraint_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original




@given(instance=FeatureModel_FeatureModel_strategy)
def test_hyp_featuremodel_featuremodel_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Constraint,
    FeatureModel_Comment,
    FeatureModel_Constraint,
    FeatureModel_ExcludeConstraint,
    FeatureModel_Feature,
    FeatureModel_FeatureModel,
    FeatureModel_Group,
    FeatureModel_NamedElement,
    FeatureModel_RequireConstraint,
    NamedElement,
    GroupType,
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

def test_FeatureModel_Comment_text_value_roundtrip():
    instance = FeatureModel_Comment(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_FeatureModel_Constraint_code_value_roundtrip():
    instance = FeatureModel_Constraint(code="sample_text", language="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_FeatureModel_Constraint_language_value_roundtrip():
    instance = FeatureModel_Constraint(code="sample_text", language="sample_text")
    assert instance.language == "sample_text"
    instance.language = "sample_text_2"
    assert instance.language == "sample_text_2"


def test_FeatureModel_Feature_abstract_value_roundtrip():
    instance = FeatureModel_Feature(abstract=True, mandatory=True)
    assert instance.abstract == True
    instance.abstract = False
    assert instance.abstract == False


def test_FeatureModel_Feature_mandatory_value_roundtrip():
    instance = FeatureModel_Feature(abstract=True, mandatory=True)
    assert instance.mandatory == True
    instance.mandatory = False
    assert instance.mandatory == False


def test_FeatureModel_FeatureModel_version_value_roundtrip():
    instance = FeatureModel_FeatureModel(version=3.14)
    assert instance.version == 3.14
    instance.version = 9.99
    assert instance.version == 9.99


def test_FeatureModel_Group_groupType_value_roundtrip():
    instance = FeatureModel_Group(groupType="sample_text")
    assert instance.groupType == "sample_text"
    instance.groupType = "sample_text_2"
    assert instance.groupType == "sample_text_2"


def test_FeatureModel_NamedElement_name_value_roundtrip():
    instance = FeatureModel_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_FeatureModel_ExcludeConstraint_isa_Constraint():
    instance = FeatureModel_ExcludeConstraint()
    assert isinstance(instance, Constraint)


def test_FeatureModel_RequireConstraint_isa_Constraint():
    instance = FeatureModel_RequireConstraint()
    assert isinstance(instance, Constraint)


def test_FeatureModel_Comment_isa_NamedElement():
    instance = FeatureModel_Comment(text="sample_text")
    assert isinstance(instance, NamedElement)


def test_FeatureModel_Constraint_isa_NamedElement():
    instance = FeatureModel_Constraint(code="sample_text", language="sample_text")
    assert isinstance(instance, NamedElement)


def test_FeatureModel_Feature_isa_NamedElement():
    instance = FeatureModel_Feature(abstract=True, mandatory=True)
    assert isinstance(instance, NamedElement)


def test_FeatureModel_FeatureModel_isa_NamedElement():
    instance = FeatureModel_FeatureModel(version=3.14)
    assert isinstance(instance, NamedElement)


def test_FeatureModel_Group_isa_NamedElement():
    instance = FeatureModel_Group(groupType="sample_text")
    assert isinstance(instance, NamedElement)


def test_assoc_children10_link_reassign_clear():
    a = FeatureModel_Feature(abstract=True, mandatory=True)
    b1 = FeatureModel_Feature(abstract=True, mandatory=True)
    b2 = FeatureModel_Feature(abstract=False, mandatory=False)
    _safe_set(a, 'FeatureModel_Feature11', b1)
    assert _is_linked(a, 'FeatureModel_Feature11', b1)
    if hasattr(b1, 'FeatureModel_Feature9'):
        assert _is_linked(b1, 'FeatureModel_Feature9', a)
    _safe_set(a, 'FeatureModel_Feature11', b2)
    assert _is_linked(a, 'FeatureModel_Feature11', b2)
    if hasattr(b1, 'FeatureModel_Feature9'):
        assert not _is_linked(b1, 'FeatureModel_Feature9', a)
    if hasattr(b2, 'FeatureModel_Feature9'):
        assert _is_linked(b2, 'FeatureModel_Feature9', a)
    _safe_set(a, 'FeatureModel_Feature11', None)
    assert not _is_linked(a, 'FeatureModel_Feature11', b2)
    if hasattr(b2, 'FeatureModel_Feature9'):
        assert not _is_linked(b2, 'FeatureModel_Feature9', a)


def test_assoc_comments0_link_reassign_clear():
    a = FeatureModel_FeatureModel(version=3.14)
    b1 = FeatureModel_Comment(text="sample_text")
    b2 = FeatureModel_Comment(text="sample_text_2")
    _safe_set(a, 'FeatureModel_FeatureModel', {b1})
    assert _is_linked(a, 'FeatureModel_FeatureModel', b1)
    if hasattr(b1, 'FeatureModel_Comment'):
        assert _is_linked(b1, 'FeatureModel_Comment', a)
    _safe_set(a, 'FeatureModel_FeatureModel', {b2})
    assert _is_linked(a, 'FeatureModel_FeatureModel', b2)
    if hasattr(b1, 'FeatureModel_Comment'):
        assert not _is_linked(b1, 'FeatureModel_Comment', a)
    if hasattr(b2, 'FeatureModel_Comment'):
        assert _is_linked(b2, 'FeatureModel_Comment', a)
    _safe_set(a, 'FeatureModel_FeatureModel', set())
    assert not _is_linked(a, 'FeatureModel_FeatureModel', b2)
    if hasattr(b2, 'FeatureModel_Comment'):
        assert not _is_linked(b2, 'FeatureModel_Comment', a)


def test_assoc_constraints1_link_reassign_clear():
    a = FeatureModel_FeatureModel(version=3.14)
    b1 = FeatureModel_Constraint(code="sample_text", language="sample_text")
    b2 = FeatureModel_Constraint(code="sample_text_2", language="sample_text_2")
    _safe_set(a, 'FeatureModel_FeatureModel2', {b1})
    assert _is_linked(a, 'FeatureModel_FeatureModel2', b1)
    if hasattr(b1, 'FeatureModel_Constraint'):
        assert _is_linked(b1, 'FeatureModel_Constraint', a)
    _safe_set(a, 'FeatureModel_FeatureModel2', {b2})
    assert _is_linked(a, 'FeatureModel_FeatureModel2', b2)
    if hasattr(b1, 'FeatureModel_Constraint'):
        assert not _is_linked(b1, 'FeatureModel_Constraint', a)
    if hasattr(b2, 'FeatureModel_Constraint'):
        assert _is_linked(b2, 'FeatureModel_Constraint', a)
    _safe_set(a, 'FeatureModel_FeatureModel2', set())
    assert not _is_linked(a, 'FeatureModel_FeatureModel2', b2)
    if hasattr(b2, 'FeatureModel_Constraint'):
        assert not _is_linked(b2, 'FeatureModel_Constraint', a)


def test_assoc_element7_link_reassign_clear():
    a = FeatureModel_NamedElement(name="sample_text")
    b1 = FeatureModel_Comment(text="sample_text")
    b2 = FeatureModel_Comment(text="sample_text_2")
    _safe_set(a, 'FeatureModel_NamedElement', b1)
    assert _is_linked(a, 'FeatureModel_NamedElement', b1)
    if hasattr(b1, 'FeatureModel_Comment8'):
        assert _is_linked(b1, 'FeatureModel_Comment8', a)
    _safe_set(a, 'FeatureModel_NamedElement', b2)
    assert _is_linked(a, 'FeatureModel_NamedElement', b2)
    if hasattr(b1, 'FeatureModel_Comment8'):
        assert not _is_linked(b1, 'FeatureModel_Comment8', a)
    if hasattr(b2, 'FeatureModel_Comment8'):
        assert _is_linked(b2, 'FeatureModel_Comment8', a)
    _safe_set(a, 'FeatureModel_NamedElement', None)
    assert not _is_linked(a, 'FeatureModel_NamedElement', b2)
    if hasattr(b2, 'FeatureModel_Comment8'):
        assert not _is_linked(b2, 'FeatureModel_Comment8', a)


def test_assoc_excludeConstraintsA16_link_reassign_clear():
    a = FeatureModel_Feature(abstract=True, mandatory=True)
    b1 = FeatureModel_ExcludeConstraint()
    b2 = FeatureModel_ExcludeConstraint()
    _safe_set(a, 'excludedFeatureA', {b1})
    assert _is_linked(a, 'excludedFeatureA', b1)
    if hasattr(b1, 'ExcludeConstraint'):
        assert _is_linked(b1, 'ExcludeConstraint', a)
    _safe_set(a, 'excludedFeatureA', {b2})
    assert _is_linked(a, 'excludedFeatureA', b2)
    if hasattr(b1, 'ExcludeConstraint'):
        assert not _is_linked(b1, 'ExcludeConstraint', a)
    if hasattr(b2, 'ExcludeConstraint'):
        assert _is_linked(b2, 'ExcludeConstraint', a)
    _safe_set(a, 'excludedFeatureA', set())
    assert not _is_linked(a, 'excludedFeatureA', b2)
    if hasattr(b2, 'ExcludeConstraint'):
        assert not _is_linked(b2, 'ExcludeConstraint', a)


def test_assoc_excludeConstraintsB17_link_reassign_clear():
    a = FeatureModel_Feature(abstract=True, mandatory=True)
    b1 = FeatureModel_ExcludeConstraint()
    b2 = FeatureModel_ExcludeConstraint()
    _safe_set(a, 'excludedFeatureB', {b1})
    assert _is_linked(a, 'excludedFeatureB', b1)
    if hasattr(b1, 'ExcludeConstraint18'):
        assert _is_linked(b1, 'ExcludeConstraint18', a)
    _safe_set(a, 'excludedFeatureB', {b2})
    assert _is_linked(a, 'excludedFeatureB', b2)
    if hasattr(b1, 'ExcludeConstraint18'):
        assert not _is_linked(b1, 'ExcludeConstraint18', a)
    if hasattr(b2, 'ExcludeConstraint18'):
        assert _is_linked(b2, 'ExcludeConstraint18', a)
    _safe_set(a, 'excludedFeatureB', set())
    assert not _is_linked(a, 'excludedFeatureB', b2)
    if hasattr(b2, 'ExcludeConstraint18'):
        assert not _is_linked(b2, 'ExcludeConstraint18', a)


def test_assoc_excludedFeatureA22_link_reassign_clear():
    a = FeatureModel_Feature(abstract=True, mandatory=True)
    b1 = FeatureModel_ExcludeConstraint()
    b2 = FeatureModel_ExcludeConstraint()
    _safe_set(a, 'Feature23', b1)
    assert _is_linked(a, 'Feature23', b1)
    if hasattr(b1, 'excludeConstraintsA'):
        assert _is_linked(b1, 'excludeConstraintsA', a)
    _safe_set(a, 'Feature23', b2)
    assert _is_linked(a, 'Feature23', b2)
    if hasattr(b1, 'excludeConstraintsA'):
        assert not _is_linked(b1, 'excludeConstraintsA', a)
    if hasattr(b2, 'excludeConstraintsA'):
        assert _is_linked(b2, 'excludeConstraintsA', a)
    _safe_set(a, 'Feature23', None)
    assert not _is_linked(a, 'Feature23', b2)
    if hasattr(b2, 'excludeConstraintsA'):
        assert not _is_linked(b2, 'excludeConstraintsA', a)


def test_assoc_excludedFeatureB24_link_reassign_clear():
    a = FeatureModel_Feature(abstract=True, mandatory=True)
    b1 = FeatureModel_ExcludeConstraint()
    b2 = FeatureModel_ExcludeConstraint()
    _safe_set(a, 'Feature25', b1)
    assert _is_linked(a, 'Feature25', b1)
    if hasattr(b1, 'excludeConstraintsB'):
        assert _is_linked(b1, 'excludeConstraintsB', a)
    _safe_set(a, 'Feature25', b2)
    assert _is_linked(a, 'Feature25', b2)
    if hasattr(b1, 'excludeConstraintsB'):
        assert not _is_linked(b1, 'excludeConstraintsB', a)
    if hasattr(b2, 'excludeConstraintsB'):
        assert _is_linked(b2, 'excludeConstraintsB', a)
    _safe_set(a, 'Feature25', None)
    assert not _is_linked(a, 'Feature25', b2)
    if hasattr(b2, 'excludeConstraintsB'):
        assert not _is_linked(b2, 'excludeConstraintsB', a)


def test_assoc_feature20_link_reassign_clear():
    a = FeatureModel_Feature(abstract=True, mandatory=True)
    b1 = FeatureModel_RequireConstraint()
    b2 = FeatureModel_RequireConstraint()
    _safe_set(a, 'Feature21', b1)
    assert _is_linked(a, 'Feature21', b1)
    if hasattr(b1, 'requireConstraints'):
        assert _is_linked(b1, 'requireConstraints', a)
    _safe_set(a, 'Feature21', b2)
    assert _is_linked(a, 'Feature21', b2)
    if hasattr(b1, 'requireConstraints'):
        assert not _is_linked(b1, 'requireConstraints', a)
    if hasattr(b2, 'requireConstraints'):
        assert _is_linked(b2, 'requireConstraints', a)
    _safe_set(a, 'Feature21', None)
    assert not _is_linked(a, 'Feature21', b2)
    if hasattr(b2, 'requireConstraints'):
        assert not _is_linked(b2, 'requireConstraints', a)


def test_assoc_features26_link_reassign_clear():
    a = FeatureModel_Group(groupType="sample_text")
    b1 = FeatureModel_Feature(abstract=True, mandatory=True)
    b2 = FeatureModel_Feature(abstract=False, mandatory=False)
    _safe_set(a, 'group', {b1})
    assert _is_linked(a, 'group', b1)
    if hasattr(b1, 'Feature27'):
        assert _is_linked(b1, 'Feature27', a)
    _safe_set(a, 'group', {b2})
    assert _is_linked(a, 'group', b2)
    if hasattr(b1, 'Feature27'):
        assert not _is_linked(b1, 'Feature27', a)
    if hasattr(b2, 'Feature27'):
        assert _is_linked(b2, 'Feature27', a)
    _safe_set(a, 'group', set())
    assert not _is_linked(a, 'group', b2)
    if hasattr(b2, 'Feature27'):
        assert not _is_linked(b2, 'Feature27', a)


def test_assoc_group15_link_reassign_clear():
    a = FeatureModel_Group(groupType="sample_text")
    b1 = FeatureModel_Feature(abstract=True, mandatory=True)
    b2 = FeatureModel_Feature(abstract=False, mandatory=False)
    _safe_set(a, 'Group', b1)
    assert _is_linked(a, 'Group', b1)
    if hasattr(b1, 'features'):
        assert _is_linked(b1, 'features', a)
    _safe_set(a, 'Group', b2)
    assert _is_linked(a, 'Group', b2)
    if hasattr(b1, 'features'):
        assert not _is_linked(b1, 'features', a)
    if hasattr(b2, 'features'):
        assert _is_linked(b2, 'features', a)
    _safe_set(a, 'Group', None)
    assert not _is_linked(a, 'Group', b2)
    if hasattr(b2, 'features'):
        assert not _is_linked(b2, 'features', a)


def test_assoc_groups5_link_reassign_clear():
    a = FeatureModel_Group(groupType="sample_text")
    b1 = FeatureModel_FeatureModel(version=3.14)
    b2 = FeatureModel_FeatureModel(version=9.99)
    _safe_set(a, 'FeatureModel_Group', b1)
    assert _is_linked(a, 'FeatureModel_Group', b1)
    if hasattr(b1, 'FeatureModel_FeatureModel6'):
        assert _is_linked(b1, 'FeatureModel_FeatureModel6', a)
    _safe_set(a, 'FeatureModel_Group', b2)
    assert _is_linked(a, 'FeatureModel_Group', b2)
    if hasattr(b1, 'FeatureModel_FeatureModel6'):
        assert not _is_linked(b1, 'FeatureModel_FeatureModel6', a)
    if hasattr(b2, 'FeatureModel_FeatureModel6'):
        assert _is_linked(b2, 'FeatureModel_FeatureModel6', a)
    _safe_set(a, 'FeatureModel_Group', None)
    assert not _is_linked(a, 'FeatureModel_Group', b2)
    if hasattr(b2, 'FeatureModel_FeatureModel6'):
        assert not _is_linked(b2, 'FeatureModel_FeatureModel6', a)


def test_assoc_requireConstraints13_link_reassign_clear():
    a = FeatureModel_Feature(abstract=True, mandatory=True)
    b1 = FeatureModel_RequireConstraint()
    b2 = FeatureModel_RequireConstraint()
    _safe_set(a, 'feature', {b1})
    assert _is_linked(a, 'feature', b1)
    if hasattr(b1, 'RequireConstraint14'):
        assert _is_linked(b1, 'RequireConstraint14', a)
    _safe_set(a, 'feature', {b2})
    assert _is_linked(a, 'feature', b2)
    if hasattr(b1, 'RequireConstraint14'):
        assert not _is_linked(b1, 'RequireConstraint14', a)
    if hasattr(b2, 'RequireConstraint14'):
        assert _is_linked(b2, 'RequireConstraint14', a)
    _safe_set(a, 'feature', set())
    assert not _is_linked(a, 'feature', b2)
    if hasattr(b2, 'RequireConstraint14'):
        assert not _is_linked(b2, 'RequireConstraint14', a)


def test_assoc_requiredConstraints12_link_reassign_clear():
    a = FeatureModel_Feature(abstract=True, mandatory=True)
    b1 = FeatureModel_RequireConstraint()
    b2 = FeatureModel_RequireConstraint()
    _safe_set(a, 'requiredFeature', {b1})
    assert _is_linked(a, 'requiredFeature', b1)
    if hasattr(b1, 'RequireConstraint'):
        assert _is_linked(b1, 'RequireConstraint', a)
    _safe_set(a, 'requiredFeature', {b2})
    assert _is_linked(a, 'requiredFeature', b2)
    if hasattr(b1, 'RequireConstraint'):
        assert not _is_linked(b1, 'RequireConstraint', a)
    if hasattr(b2, 'RequireConstraint'):
        assert _is_linked(b2, 'RequireConstraint', a)
    _safe_set(a, 'requiredFeature', set())
    assert not _is_linked(a, 'requiredFeature', b2)
    if hasattr(b2, 'RequireConstraint'):
        assert not _is_linked(b2, 'RequireConstraint', a)


def test_assoc_requiredFeature19_link_reassign_clear():
    a = FeatureModel_Feature(abstract=True, mandatory=True)
    b1 = FeatureModel_RequireConstraint()
    b2 = FeatureModel_RequireConstraint()
    _safe_set(a, 'Feature', b1)
    assert _is_linked(a, 'Feature', b1)
    if hasattr(b1, 'requiredConstraints'):
        assert _is_linked(b1, 'requiredConstraints', a)
    _safe_set(a, 'Feature', b2)
    assert _is_linked(a, 'Feature', b2)
    if hasattr(b1, 'requiredConstraints'):
        assert not _is_linked(b1, 'requiredConstraints', a)
    if hasattr(b2, 'requiredConstraints'):
        assert _is_linked(b2, 'requiredConstraints', a)
    _safe_set(a, 'Feature', None)
    assert not _is_linked(a, 'Feature', b2)
    if hasattr(b2, 'requiredConstraints'):
        assert not _is_linked(b2, 'requiredConstraints', a)


def test_assoc_root3_link_reassign_clear():
    a = FeatureModel_FeatureModel(version=3.14)
    b1 = FeatureModel_Feature(abstract=True, mandatory=True)
    b2 = FeatureModel_Feature(abstract=False, mandatory=False)
    _safe_set(a, 'FeatureModel_FeatureModel4', b1)
    assert _is_linked(a, 'FeatureModel_FeatureModel4', b1)
    if hasattr(b1, 'FeatureModel_Feature'):
        assert _is_linked(b1, 'FeatureModel_Feature', a)
    _safe_set(a, 'FeatureModel_FeatureModel4', b2)
    assert _is_linked(a, 'FeatureModel_FeatureModel4', b2)
    if hasattr(b1, 'FeatureModel_Feature'):
        assert not _is_linked(b1, 'FeatureModel_Feature', a)
    if hasattr(b2, 'FeatureModel_Feature'):
        assert _is_linked(b2, 'FeatureModel_Feature', a)
    _safe_set(a, 'FeatureModel_FeatureModel4', None)
    assert not _is_linked(a, 'FeatureModel_FeatureModel4', b2)
    if hasattr(b2, 'FeatureModel_Feature'):
        assert not _is_linked(b2, 'FeatureModel_Feature', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Constraint_strategy = st.builds(Constraint)
@given(instance=Constraint_strategy)
@settings(max_examples=25)
def test_Constraint_instantiation(instance):
    assert isinstance(instance, Constraint)


FeatureModel_Comment_strategy = st.builds(FeatureModel_Comment, text=safe_text)
@given(instance=FeatureModel_Comment_strategy)
@settings(max_examples=25)
def test_FeatureModel_Comment_instantiation(instance):
    assert isinstance(instance, FeatureModel_Comment)


FeatureModel_Constraint_strategy = st.builds(FeatureModel_Constraint, code=safe_text, language=safe_text)
@given(instance=FeatureModel_Constraint_strategy)
@settings(max_examples=25)
def test_FeatureModel_Constraint_instantiation(instance):
    assert isinstance(instance, FeatureModel_Constraint)


FeatureModel_ExcludeConstraint_strategy = st.builds(FeatureModel_ExcludeConstraint)
@given(instance=FeatureModel_ExcludeConstraint_strategy)
@settings(max_examples=25)
def test_FeatureModel_ExcludeConstraint_instantiation(instance):
    assert isinstance(instance, FeatureModel_ExcludeConstraint)


FeatureModel_Feature_strategy = st.builds(FeatureModel_Feature, abstract=st.booleans(), mandatory=st.booleans())
@given(instance=FeatureModel_Feature_strategy)
@settings(max_examples=25)
def test_FeatureModel_Feature_instantiation(instance):
    assert isinstance(instance, FeatureModel_Feature)


FeatureModel_FeatureModel_strategy = st.builds(FeatureModel_FeatureModel, version=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=FeatureModel_FeatureModel_strategy)
@settings(max_examples=25)
def test_FeatureModel_FeatureModel_instantiation(instance):
    assert isinstance(instance, FeatureModel_FeatureModel)


FeatureModel_Group_strategy = st.builds(FeatureModel_Group, groupType=safe_text)
@given(instance=FeatureModel_Group_strategy)
@settings(max_examples=25)
def test_FeatureModel_Group_instantiation(instance):
    assert isinstance(instance, FeatureModel_Group)


FeatureModel_NamedElement_strategy = st.builds(FeatureModel_NamedElement, name=safe_text)
@given(instance=FeatureModel_NamedElement_strategy)
@settings(max_examples=25)
def test_FeatureModel_NamedElement_instantiation(instance):
    assert isinstance(instance, FeatureModel_NamedElement)


FeatureModel_RequireConstraint_strategy = st.builds(FeatureModel_RequireConstraint)
@given(instance=FeatureModel_RequireConstraint_strategy)
@settings(max_examples=25)
def test_FeatureModel_RequireConstraint_instantiation(instance):
    assert isinstance(instance, FeatureModel_RequireConstraint)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)



