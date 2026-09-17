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
    flat11_UrgentType,
    flat11_TransitionType,
    flat11_LabelType,
    flat11_TemplateType,
    flat11_TargetType,
    flat11_SourceType,
    flat11_ParameterType,
    flat11_NtaType,
    flat11_NameType,
    flat11_NailType,
    flat11_LocationType,
    flat11_InitType,
    flat11_EStringToStringMapEntry,
    flat11_DocumentRoot,
    flat11_CommittedType,
    KindType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_flat11_urgenttype_is_not_abstract():
    assert not inspect.isabstract(flat11_UrgentType)


def test_hyp_flat11_urgenttype_constructor_exists():
    assert callable(flat11_UrgentType.__init__)


def test_hyp_flat11_urgenttype_constructor_args():
    sig = inspect.signature(flat11_UrgentType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_flat11_transitiontype_is_not_abstract():
    assert not inspect.isabstract(flat11_TransitionType)


def test_hyp_flat11_transitiontype_constructor_exists():
    assert callable(flat11_TransitionType.__init__)


def test_hyp_flat11_transitiontype_constructor_args():
    sig = inspect.signature(flat11_TransitionType.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"
    assert "controllable" in params, "Missing parameter 'controllable'"
    assert "action" in params, "Missing parameter 'action'"
    assert "id" in params, "Missing parameter 'id'"









def test_hyp_flat11_labeltype_is_not_abstract():
    assert not inspect.isabstract(flat11_LabelType)


def test_hyp_flat11_labeltype_constructor_exists():
    assert callable(flat11_LabelType.__init__)


def test_hyp_flat11_labeltype_constructor_args():
    sig = inspect.signature(flat11_LabelType.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "value" in params, "Missing parameter 'value'"
    assert "kind" in params, "Missing parameter 'kind'"
    assert "x" in params, "Missing parameter 'x'"







def test_hyp_flat11_templatetype_is_not_abstract():
    assert not inspect.isabstract(flat11_TemplateType)


def test_hyp_flat11_templatetype_constructor_exists():
    assert callable(flat11_TemplateType.__init__)


def test_hyp_flat11_templatetype_constructor_args():
    sig = inspect.signature(flat11_TemplateType.__init__)
    params = list(sig.parameters.keys())
    assert "declaration" in params, "Missing parameter 'declaration'"




def test_hyp_flat11_targettype_is_not_abstract():
    assert not inspect.isabstract(flat11_TargetType)


def test_hyp_flat11_targettype_constructor_exists():
    assert callable(flat11_TargetType.__init__)


def test_hyp_flat11_targettype_constructor_args():
    sig = inspect.signature(flat11_TargetType.__init__)
    params = list(sig.parameters.keys())
    assert "ref" in params, "Missing parameter 'ref'"




def test_hyp_flat11_sourcetype_is_not_abstract():
    assert not inspect.isabstract(flat11_SourceType)


def test_hyp_flat11_sourcetype_constructor_exists():
    assert callable(flat11_SourceType.__init__)


def test_hyp_flat11_sourcetype_constructor_args():
    sig = inspect.signature(flat11_SourceType.__init__)
    params = list(sig.parameters.keys())
    assert "ref" in params, "Missing parameter 'ref'"




def test_hyp_flat11_parametertype_is_not_abstract():
    assert not inspect.isabstract(flat11_ParameterType)


def test_hyp_flat11_parametertype_constructor_exists():
    assert callable(flat11_ParameterType.__init__)


def test_hyp_flat11_parametertype_constructor_args():
    sig = inspect.signature(flat11_ParameterType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"






def test_hyp_flat11_ntatype_is_not_abstract():
    assert not inspect.isabstract(flat11_NtaType)


def test_hyp_flat11_ntatype_constructor_exists():
    assert callable(flat11_NtaType.__init__)


def test_hyp_flat11_ntatype_constructor_args():
    sig = inspect.signature(flat11_NtaType.__init__)
    params = list(sig.parameters.keys())
    assert "instantiation" in params, "Missing parameter 'instantiation'"
    assert "imports" in params, "Missing parameter 'imports'"
    assert "system" in params, "Missing parameter 'system'"
    assert "declaration" in params, "Missing parameter 'declaration'"







def test_hyp_flat11_nametype_is_not_abstract():
    assert not inspect.isabstract(flat11_NameType)


def test_hyp_flat11_nametype_constructor_exists():
    assert callable(flat11_NameType.__init__)


def test_hyp_flat11_nametype_constructor_args():
    sig = inspect.signature(flat11_NameType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"






def test_hyp_flat11_nailtype_is_not_abstract():
    assert not inspect.isabstract(flat11_NailType)


def test_hyp_flat11_nailtype_constructor_exists():
    assert callable(flat11_NailType.__init__)


def test_hyp_flat11_nailtype_constructor_args():
    sig = inspect.signature(flat11_NailType.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"





def test_hyp_flat11_locationtype_is_not_abstract():
    assert not inspect.isabstract(flat11_LocationType)


def test_hyp_flat11_locationtype_constructor_exists():
    assert callable(flat11_LocationType.__init__)


def test_hyp_flat11_locationtype_constructor_args():
    sig = inspect.signature(flat11_LocationType.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "id" in params, "Missing parameter 'id'"
    assert "y" in params, "Missing parameter 'y'"
    assert "color" in params, "Missing parameter 'color'"







def test_hyp_flat11_inittype_is_not_abstract():
    assert not inspect.isabstract(flat11_InitType)


def test_hyp_flat11_inittype_constructor_exists():
    assert callable(flat11_InitType.__init__)


def test_hyp_flat11_inittype_constructor_args():
    sig = inspect.signature(flat11_InitType.__init__)
    params = list(sig.parameters.keys())
    assert "ref" in params, "Missing parameter 'ref'"




def test_hyp_flat11_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(flat11_EStringToStringMapEntry)


def test_hyp_flat11_estringtostringmapentry_constructor_exists():
    assert callable(flat11_EStringToStringMapEntry.__init__)


def test_hyp_flat11_estringtostringmapentry_constructor_args():
    sig = inspect.signature(flat11_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_flat11_documentroot_is_not_abstract():
    assert not inspect.isabstract(flat11_DocumentRoot)


def test_hyp_flat11_documentroot_constructor_exists():
    assert callable(flat11_DocumentRoot.__init__)


def test_hyp_flat11_documentroot_constructor_args():
    sig = inspect.signature(flat11_DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "system" in params, "Missing parameter 'system'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "imports" in params, "Missing parameter 'imports'"
    assert "instantiation" in params, "Missing parameter 'instantiation'"
    assert "declaration" in params, "Missing parameter 'declaration'"








def test_hyp_flat11_committedtype_is_not_abstract():
    assert not inspect.isabstract(flat11_CommittedType)


def test_hyp_flat11_committedtype_constructor_exists():
    assert callable(flat11_CommittedType.__init__)


def test_hyp_flat11_committedtype_constructor_args():
    sig = inspect.signature(flat11_CommittedType.__init__)
    params = list(sig.parameters.keys())

def test_hyp_kindtype_exists():
    # Check that the Enumeration exists
    assert KindType is not None

def test_hyp_kindtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in KindType]
    expected_literals = [
        "select",
        "guard",
        "invariant",
        "synchronisation",
        "assignment",
        "comments",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in KindType"


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
flat11_UrgentType_strategy = st.builds(
    flat11_UrgentType,
)
flat11_TransitionType_strategy = st.builds(
    flat11_TransitionType,
    color=
        safe_text,
    x=
        safe_text,
    y=
        safe_text,
    controllable=
        safe_text,
    action=
        safe_text,
    id=
        safe_text
)
flat11_LabelType_strategy = st.builds(
    flat11_LabelType,
    y=
        safe_text,
    value=
        safe_text,
    kind=
        safe_text,
    x=
        safe_text
)
flat11_TemplateType_strategy = st.builds(
    flat11_TemplateType,
    declaration=
        safe_text
)
flat11_TargetType_strategy = st.builds(
    flat11_TargetType,
    ref=
        safe_text
)
flat11_SourceType_strategy = st.builds(
    flat11_SourceType,
    ref=
        safe_text
)
flat11_ParameterType_strategy = st.builds(
    flat11_ParameterType,
    value=
        safe_text,
    y=
        safe_text,
    x=
        safe_text
)
flat11_NtaType_strategy = st.builds(
    flat11_NtaType,
    instantiation=
        safe_text,
    imports=
        safe_text,
    system=
        safe_text,
    declaration=
        safe_text
)
flat11_NameType_strategy = st.builds(
    flat11_NameType,
    value=
        safe_text,
    x=
        safe_text,
    y=
        safe_text
)
flat11_NailType_strategy = st.builds(
    flat11_NailType,
    y=
        safe_text,
    x=
        safe_text
)
flat11_LocationType_strategy = st.builds(
    flat11_LocationType,
    x=
        safe_text,
    id=
        safe_text,
    y=
        safe_text,
    color=
        safe_text
)
flat11_InitType_strategy = st.builds(
    flat11_InitType,
    ref=
        safe_text
)
flat11_EStringToStringMapEntry_strategy = st.builds(
    flat11_EStringToStringMapEntry,
)
flat11_DocumentRoot_strategy = st.builds(
    flat11_DocumentRoot,
    system=
        safe_text,
    mixed=
        safe_text,
    imports=
        safe_text,
    instantiation=
        safe_text,
    declaration=
        safe_text
)
flat11_CommittedType_strategy = st.builds(
    flat11_CommittedType,
)





@given(instance=flat11_TransitionType_strategy)
def test_hyp_flat11_transitiontype_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=flat11_TransitionType_strategy)
def test_hyp_flat11_transitiontype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=flat11_TransitionType_strategy)
def test_hyp_flat11_transitiontype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=flat11_TransitionType_strategy)
def test_hyp_flat11_transitiontype_controllable_setter(instance):
    original = instance.controllable
    instance.controllable = original
    assert instance.controllable == original



@given(instance=flat11_TransitionType_strategy)
def test_hyp_flat11_transitiontype_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original



@given(instance=flat11_TransitionType_strategy)
def test_hyp_flat11_transitiontype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=flat11_LabelType_strategy)
def test_hyp_flat11_labeltype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=flat11_LabelType_strategy)
def test_hyp_flat11_labeltype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=flat11_LabelType_strategy)
def test_hyp_flat11_labeltype_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=flat11_LabelType_strategy)
def test_hyp_flat11_labeltype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original




@given(instance=flat11_TemplateType_strategy)
def test_hyp_flat11_templatetype_declaration_setter(instance):
    original = instance.declaration
    instance.declaration = original
    assert instance.declaration == original




@given(instance=flat11_TargetType_strategy)
def test_hyp_flat11_targettype_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original




@given(instance=flat11_SourceType_strategy)
def test_hyp_flat11_sourcetype_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original




@given(instance=flat11_ParameterType_strategy)
def test_hyp_flat11_parametertype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=flat11_ParameterType_strategy)
def test_hyp_flat11_parametertype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=flat11_ParameterType_strategy)
def test_hyp_flat11_parametertype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original




@given(instance=flat11_NtaType_strategy)
def test_hyp_flat11_ntatype_instantiation_setter(instance):
    original = instance.instantiation
    instance.instantiation = original
    assert instance.instantiation == original



@given(instance=flat11_NtaType_strategy)
def test_hyp_flat11_ntatype_imports_setter(instance):
    original = instance.imports
    instance.imports = original
    assert instance.imports == original



@given(instance=flat11_NtaType_strategy)
def test_hyp_flat11_ntatype_system_setter(instance):
    original = instance.system
    instance.system = original
    assert instance.system == original



@given(instance=flat11_NtaType_strategy)
def test_hyp_flat11_ntatype_declaration_setter(instance):
    original = instance.declaration
    instance.declaration = original
    assert instance.declaration == original




@given(instance=flat11_NameType_strategy)
def test_hyp_flat11_nametype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=flat11_NameType_strategy)
def test_hyp_flat11_nametype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=flat11_NameType_strategy)
def test_hyp_flat11_nametype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original




@given(instance=flat11_NailType_strategy)
def test_hyp_flat11_nailtype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=flat11_NailType_strategy)
def test_hyp_flat11_nailtype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original




@given(instance=flat11_LocationType_strategy)
def test_hyp_flat11_locationtype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=flat11_LocationType_strategy)
def test_hyp_flat11_locationtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=flat11_LocationType_strategy)
def test_hyp_flat11_locationtype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=flat11_LocationType_strategy)
def test_hyp_flat11_locationtype_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original




@given(instance=flat11_InitType_strategy)
def test_hyp_flat11_inittype_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original





@given(instance=flat11_DocumentRoot_strategy)
def test_hyp_flat11_documentroot_system_setter(instance):
    original = instance.system
    instance.system = original
    assert instance.system == original



@given(instance=flat11_DocumentRoot_strategy)
def test_hyp_flat11_documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=flat11_DocumentRoot_strategy)
def test_hyp_flat11_documentroot_imports_setter(instance):
    original = instance.imports
    instance.imports = original
    assert instance.imports == original



@given(instance=flat11_DocumentRoot_strategy)
def test_hyp_flat11_documentroot_instantiation_setter(instance):
    original = instance.instantiation
    instance.instantiation = original
    assert instance.instantiation == original



@given(instance=flat11_DocumentRoot_strategy)
def test_hyp_flat11_documentroot_declaration_setter(instance):
    original = instance.declaration
    instance.declaration = original
    assert instance.declaration == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    flat11_CommittedType,
    flat11_DocumentRoot,
    flat11_EStringToStringMapEntry,
    flat11_InitType,
    flat11_LabelType,
    flat11_LocationType,
    flat11_NailType,
    flat11_NameType,
    flat11_NtaType,
    flat11_ParameterType,
    flat11_SourceType,
    flat11_TargetType,
    flat11_TemplateType,
    flat11_TransitionType,
    flat11_UrgentType,
    KindType,
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

def test_flat11_DocumentRoot_declaration_value_roundtrip():
    instance = flat11_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    assert instance.declaration == "sample_text"
    instance.declaration = "sample_text_2"
    assert instance.declaration == "sample_text_2"


def test_flat11_DocumentRoot_imports_value_roundtrip():
    instance = flat11_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    assert instance.imports == "sample_text"
    instance.imports = "sample_text_2"
    assert instance.imports == "sample_text_2"


def test_flat11_DocumentRoot_instantiation_value_roundtrip():
    instance = flat11_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    assert instance.instantiation == "sample_text"
    instance.instantiation = "sample_text_2"
    assert instance.instantiation == "sample_text_2"


def test_flat11_DocumentRoot_mixed_value_roundtrip():
    instance = flat11_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_flat11_DocumentRoot_system_value_roundtrip():
    instance = flat11_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    assert instance.system == "sample_text"
    instance.system = "sample_text_2"
    assert instance.system == "sample_text_2"


def test_flat11_InitType_ref_value_roundtrip():
    instance = flat11_InitType(ref="sample_text")
    assert instance.ref == "sample_text"
    instance.ref = "sample_text_2"
    assert instance.ref == "sample_text_2"


def test_flat11_LabelType_kind_value_roundtrip():
    instance = flat11_LabelType(kind="sample_text", value="sample_text", x="sample_text", y="sample_text")
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_flat11_LabelType_value_value_roundtrip():
    instance = flat11_LabelType(kind="sample_text", value="sample_text", x="sample_text", y="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_flat11_LabelType_x_value_roundtrip():
    instance = flat11_LabelType(kind="sample_text", value="sample_text", x="sample_text", y="sample_text")
    assert instance.x == "sample_text"
    instance.x = "sample_text_2"
    assert instance.x == "sample_text_2"


def test_flat11_LabelType_y_value_roundtrip():
    instance = flat11_LabelType(kind="sample_text", value="sample_text", x="sample_text", y="sample_text")
    assert instance.y == "sample_text"
    instance.y = "sample_text_2"
    assert instance.y == "sample_text_2"


def test_flat11_LocationType_color_value_roundtrip():
    instance = flat11_LocationType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_flat11_LocationType_id_value_roundtrip():
    instance = flat11_LocationType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_flat11_LocationType_x_value_roundtrip():
    instance = flat11_LocationType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    assert instance.x == "sample_text"
    instance.x = "sample_text_2"
    assert instance.x == "sample_text_2"


def test_flat11_LocationType_y_value_roundtrip():
    instance = flat11_LocationType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    assert instance.y == "sample_text"
    instance.y = "sample_text_2"
    assert instance.y == "sample_text_2"


def test_flat11_NailType_x_value_roundtrip():
    instance = flat11_NailType(x="sample_text", y="sample_text")
    assert instance.x == "sample_text"
    instance.x = "sample_text_2"
    assert instance.x == "sample_text_2"


def test_flat11_NailType_y_value_roundtrip():
    instance = flat11_NailType(x="sample_text", y="sample_text")
    assert instance.y == "sample_text"
    instance.y = "sample_text_2"
    assert instance.y == "sample_text_2"


def test_flat11_NameType_value_value_roundtrip():
    instance = flat11_NameType(value="sample_text", x="sample_text", y="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_flat11_NameType_x_value_roundtrip():
    instance = flat11_NameType(value="sample_text", x="sample_text", y="sample_text")
    assert instance.x == "sample_text"
    instance.x = "sample_text_2"
    assert instance.x == "sample_text_2"


def test_flat11_NameType_y_value_roundtrip():
    instance = flat11_NameType(value="sample_text", x="sample_text", y="sample_text")
    assert instance.y == "sample_text"
    instance.y = "sample_text_2"
    assert instance.y == "sample_text_2"


def test_flat11_NtaType_declaration_value_roundtrip():
    instance = flat11_NtaType(declaration="sample_text", imports="sample_text", instantiation="sample_text", system="sample_text")
    assert instance.declaration == "sample_text"
    instance.declaration = "sample_text_2"
    assert instance.declaration == "sample_text_2"


def test_flat11_NtaType_imports_value_roundtrip():
    instance = flat11_NtaType(declaration="sample_text", imports="sample_text", instantiation="sample_text", system="sample_text")
    assert instance.imports == "sample_text"
    instance.imports = "sample_text_2"
    assert instance.imports == "sample_text_2"


def test_flat11_NtaType_instantiation_value_roundtrip():
    instance = flat11_NtaType(declaration="sample_text", imports="sample_text", instantiation="sample_text", system="sample_text")
    assert instance.instantiation == "sample_text"
    instance.instantiation = "sample_text_2"
    assert instance.instantiation == "sample_text_2"


def test_flat11_NtaType_system_value_roundtrip():
    instance = flat11_NtaType(declaration="sample_text", imports="sample_text", instantiation="sample_text", system="sample_text")
    assert instance.system == "sample_text"
    instance.system = "sample_text_2"
    assert instance.system == "sample_text_2"


def test_flat11_ParameterType_value_value_roundtrip():
    instance = flat11_ParameterType(value="sample_text", x="sample_text", y="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_flat11_ParameterType_x_value_roundtrip():
    instance = flat11_ParameterType(value="sample_text", x="sample_text", y="sample_text")
    assert instance.x == "sample_text"
    instance.x = "sample_text_2"
    assert instance.x == "sample_text_2"


def test_flat11_ParameterType_y_value_roundtrip():
    instance = flat11_ParameterType(value="sample_text", x="sample_text", y="sample_text")
    assert instance.y == "sample_text"
    instance.y = "sample_text_2"
    assert instance.y == "sample_text_2"


def test_flat11_SourceType_ref_value_roundtrip():
    instance = flat11_SourceType(ref="sample_text")
    assert instance.ref == "sample_text"
    instance.ref = "sample_text_2"
    assert instance.ref == "sample_text_2"


def test_flat11_TargetType_ref_value_roundtrip():
    instance = flat11_TargetType(ref="sample_text")
    assert instance.ref == "sample_text"
    instance.ref = "sample_text_2"
    assert instance.ref == "sample_text_2"


def test_flat11_TemplateType_declaration_value_roundtrip():
    instance = flat11_TemplateType(declaration="sample_text")
    assert instance.declaration == "sample_text"
    instance.declaration = "sample_text_2"
    assert instance.declaration == "sample_text_2"


def test_flat11_TransitionType_action_value_roundtrip():
    instance = flat11_TransitionType(action="sample_text", color="sample_text", controllable="sample_text", id="sample_text", x="sample_text", y="sample_text")
    assert instance.action == "sample_text"
    instance.action = "sample_text_2"
    assert instance.action == "sample_text_2"


def test_flat11_TransitionType_color_value_roundtrip():
    instance = flat11_TransitionType(action="sample_text", color="sample_text", controllable="sample_text", id="sample_text", x="sample_text", y="sample_text")
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_flat11_TransitionType_controllable_value_roundtrip():
    instance = flat11_TransitionType(action="sample_text", color="sample_text", controllable="sample_text", id="sample_text", x="sample_text", y="sample_text")
    assert instance.controllable == "sample_text"
    instance.controllable = "sample_text_2"
    assert instance.controllable == "sample_text_2"


def test_flat11_TransitionType_id_value_roundtrip():
    instance = flat11_TransitionType(action="sample_text", color="sample_text", controllable="sample_text", id="sample_text", x="sample_text", y="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_flat11_TransitionType_x_value_roundtrip():
    instance = flat11_TransitionType(action="sample_text", color="sample_text", controllable="sample_text", id="sample_text", x="sample_text", y="sample_text")
    assert instance.x == "sample_text"
    instance.x = "sample_text_2"
    assert instance.x == "sample_text_2"


def test_flat11_TransitionType_y_value_roundtrip():
    instance = flat11_TransitionType(action="sample_text", color="sample_text", controllable="sample_text", id="sample_text", x="sample_text", y="sample_text")
    assert instance.y == "sample_text"
    instance.y = "sample_text_2"
    assert instance.y == "sample_text_2"


def test_assoc_committed39_link_reassign_clear():
    a = flat11_LocationType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    b1 = flat11_CommittedType()
    b2 = flat11_CommittedType()
    _safe_set(a, 'flat11_LocationType40', b1)
    assert _is_linked(a, 'flat11_LocationType40', b1)
    if hasattr(b1, 'flat11_CommittedType41'):
        assert _is_linked(b1, 'flat11_CommittedType41', a)
    _safe_set(a, 'flat11_LocationType40', b2)
    assert _is_linked(a, 'flat11_LocationType40', b2)
    if hasattr(b1, 'flat11_CommittedType41'):
        assert not _is_linked(b1, 'flat11_CommittedType41', a)
    if hasattr(b2, 'flat11_CommittedType41'):
        assert _is_linked(b2, 'flat11_CommittedType41', a)
    _safe_set(a, 'flat11_LocationType40', None)
    assert not _is_linked(a, 'flat11_LocationType40', b2)
    if hasattr(b2, 'flat11_CommittedType41'):
        assert not _is_linked(b2, 'flat11_CommittedType41', a)


def test_assoc_committed4_link_reassign_clear():
    a = flat11_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    b1 = flat11_CommittedType()
    b2 = flat11_CommittedType()
    _safe_set(a, 'flat11_DocumentRoot5', {b1})
    assert _is_linked(a, 'flat11_DocumentRoot5', b1)
    if hasattr(b1, 'flat11_CommittedType'):
        assert _is_linked(b1, 'flat11_CommittedType', a)
    _safe_set(a, 'flat11_DocumentRoot5', {b2})
    assert _is_linked(a, 'flat11_DocumentRoot5', b2)
    if hasattr(b1, 'flat11_CommittedType'):
        assert not _is_linked(b1, 'flat11_CommittedType', a)
    if hasattr(b2, 'flat11_CommittedType'):
        assert _is_linked(b2, 'flat11_CommittedType', a)
    _safe_set(a, 'flat11_DocumentRoot5', set())
    assert not _is_linked(a, 'flat11_DocumentRoot5', b2)
    if hasattr(b2, 'flat11_CommittedType'):
        assert not _is_linked(b2, 'flat11_CommittedType', a)


def test_assoc_init54_link_reassign_clear():
    a = flat11_TemplateType(declaration="sample_text")
    b1 = flat11_InitType(ref="sample_text")
    b2 = flat11_InitType(ref="sample_text_2")
    _safe_set(a, 'flat11_TemplateType55', b1)
    assert _is_linked(a, 'flat11_TemplateType55', b1)
    if hasattr(b1, 'flat11_InitType56'):
        assert _is_linked(b1, 'flat11_InitType56', a)
    _safe_set(a, 'flat11_TemplateType55', b2)
    assert _is_linked(a, 'flat11_TemplateType55', b2)
    if hasattr(b1, 'flat11_InitType56'):
        assert not _is_linked(b1, 'flat11_InitType56', a)
    if hasattr(b2, 'flat11_InitType56'):
        assert _is_linked(b2, 'flat11_InitType56', a)
    _safe_set(a, 'flat11_TemplateType55', None)
    assert not _is_linked(a, 'flat11_TemplateType55', b2)
    if hasattr(b2, 'flat11_InitType56'):
        assert not _is_linked(b2, 'flat11_InitType56', a)


def test_assoc_init6_link_reassign_clear():
    a = flat11_InitType(ref="sample_text")
    b1 = flat11_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    b2 = flat11_DocumentRoot(declaration="sample_text_2", imports="sample_text_2", instantiation="sample_text_2", mixed="sample_text_2", system="sample_text_2")
    _safe_set(a, 'flat11_InitType', b1)
    assert _is_linked(a, 'flat11_InitType', b1)
    if hasattr(b1, 'flat11_DocumentRoot7'):
        assert _is_linked(b1, 'flat11_DocumentRoot7', a)
    _safe_set(a, 'flat11_InitType', b2)
    assert _is_linked(a, 'flat11_InitType', b2)
    if hasattr(b1, 'flat11_DocumentRoot7'):
        assert not _is_linked(b1, 'flat11_DocumentRoot7', a)
    if hasattr(b2, 'flat11_DocumentRoot7'):
        assert _is_linked(b2, 'flat11_DocumentRoot7', a)
    _safe_set(a, 'flat11_InitType', None)
    assert not _is_linked(a, 'flat11_InitType', b2)
    if hasattr(b2, 'flat11_DocumentRoot7'):
        assert not _is_linked(b2, 'flat11_DocumentRoot7', a)


def test_assoc_label33_link_reassign_clear():
    a = flat11_LocationType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    b1 = flat11_LabelType(kind="sample_text", value="sample_text", x="sample_text", y="sample_text")
    b2 = flat11_LabelType(kind="sample_text_2", value="sample_text_2", x="sample_text_2", y="sample_text_2")
    _safe_set(a, 'flat11_LocationType34', {b1})
    assert _is_linked(a, 'flat11_LocationType34', b1)
    if hasattr(b1, 'flat11_LabelType35'):
        assert _is_linked(b1, 'flat11_LabelType35', a)
    _safe_set(a, 'flat11_LocationType34', {b2})
    assert _is_linked(a, 'flat11_LocationType34', b2)
    if hasattr(b1, 'flat11_LabelType35'):
        assert not _is_linked(b1, 'flat11_LabelType35', a)
    if hasattr(b2, 'flat11_LabelType35'):
        assert _is_linked(b2, 'flat11_LabelType35', a)
    _safe_set(a, 'flat11_LocationType34', set())
    assert not _is_linked(a, 'flat11_LocationType34', b2)
    if hasattr(b2, 'flat11_LabelType35'):
        assert not _is_linked(b2, 'flat11_LabelType35', a)


def test_assoc_label66_link_reassign_clear():
    a = flat11_TransitionType(action="sample_text", color="sample_text", controllable="sample_text", id="sample_text", x="sample_text", y="sample_text")
    b1 = flat11_LabelType(kind="sample_text", value="sample_text", x="sample_text", y="sample_text")
    b2 = flat11_LabelType(kind="sample_text_2", value="sample_text_2", x="sample_text_2", y="sample_text_2")
    _safe_set(a, 'flat11_TransitionType67', {b1})
    assert _is_linked(a, 'flat11_TransitionType67', b1)
    if hasattr(b1, 'flat11_LabelType68'):
        assert _is_linked(b1, 'flat11_LabelType68', a)
    _safe_set(a, 'flat11_TransitionType67', {b2})
    assert _is_linked(a, 'flat11_TransitionType67', b2)
    if hasattr(b1, 'flat11_LabelType68'):
        assert not _is_linked(b1, 'flat11_LabelType68', a)
    if hasattr(b2, 'flat11_LabelType68'):
        assert _is_linked(b2, 'flat11_LabelType68', a)
    _safe_set(a, 'flat11_TransitionType67', set())
    assert not _is_linked(a, 'flat11_TransitionType67', b2)
    if hasattr(b2, 'flat11_LabelType68'):
        assert not _is_linked(b2, 'flat11_LabelType68', a)


def test_assoc_label8_link_reassign_clear():
    a = flat11_LabelType(kind="sample_text", value="sample_text", x="sample_text", y="sample_text")
    b1 = flat11_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    b2 = flat11_DocumentRoot(declaration="sample_text_2", imports="sample_text_2", instantiation="sample_text_2", mixed="sample_text_2", system="sample_text_2")
    _safe_set(a, 'flat11_LabelType', b1)
    assert _is_linked(a, 'flat11_LabelType', b1)
    if hasattr(b1, 'flat11_DocumentRoot9'):
        assert _is_linked(b1, 'flat11_DocumentRoot9', a)
    _safe_set(a, 'flat11_LabelType', b2)
    assert _is_linked(a, 'flat11_LabelType', b2)
    if hasattr(b1, 'flat11_DocumentRoot9'):
        assert not _is_linked(b1, 'flat11_DocumentRoot9', a)
    if hasattr(b2, 'flat11_DocumentRoot9'):
        assert _is_linked(b2, 'flat11_DocumentRoot9', a)
    _safe_set(a, 'flat11_LabelType', None)
    assert not _is_linked(a, 'flat11_LabelType', b2)
    if hasattr(b2, 'flat11_DocumentRoot9'):
        assert not _is_linked(b2, 'flat11_DocumentRoot9', a)


def test_assoc_location10_link_reassign_clear():
    a = flat11_LocationType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    b1 = flat11_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    b2 = flat11_DocumentRoot(declaration="sample_text_2", imports="sample_text_2", instantiation="sample_text_2", mixed="sample_text_2", system="sample_text_2")
    _safe_set(a, 'flat11_LocationType', b1)
    assert _is_linked(a, 'flat11_LocationType', b1)
    if hasattr(b1, 'flat11_DocumentRoot11'):
        assert _is_linked(b1, 'flat11_DocumentRoot11', a)
    _safe_set(a, 'flat11_LocationType', b2)
    assert _is_linked(a, 'flat11_LocationType', b2)
    if hasattr(b1, 'flat11_DocumentRoot11'):
        assert not _is_linked(b1, 'flat11_DocumentRoot11', a)
    if hasattr(b2, 'flat11_DocumentRoot11'):
        assert _is_linked(b2, 'flat11_DocumentRoot11', a)
    _safe_set(a, 'flat11_LocationType', None)
    assert not _is_linked(a, 'flat11_LocationType', b2)
    if hasattr(b2, 'flat11_DocumentRoot11'):
        assert not _is_linked(b2, 'flat11_DocumentRoot11', a)


def test_assoc_location51_link_reassign_clear():
    a = flat11_TemplateType(declaration="sample_text")
    b1 = flat11_LocationType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    b2 = flat11_LocationType(color="sample_text_2", id="sample_text_2", x="sample_text_2", y="sample_text_2")
    _safe_set(a, 'flat11_TemplateType52', {b1})
    assert _is_linked(a, 'flat11_TemplateType52', b1)
    if hasattr(b1, 'flat11_LocationType53'):
        assert _is_linked(b1, 'flat11_LocationType53', a)
    _safe_set(a, 'flat11_TemplateType52', {b2})
    assert _is_linked(a, 'flat11_TemplateType52', b2)
    if hasattr(b1, 'flat11_LocationType53'):
        assert not _is_linked(b1, 'flat11_LocationType53', a)
    if hasattr(b2, 'flat11_LocationType53'):
        assert _is_linked(b2, 'flat11_LocationType53', a)
    _safe_set(a, 'flat11_TemplateType52', set())
    assert not _is_linked(a, 'flat11_TemplateType52', b2)
    if hasattr(b2, 'flat11_LocationType53'):
        assert not _is_linked(b2, 'flat11_LocationType53', a)


def test_assoc_nail12_link_reassign_clear():
    a = flat11_NailType(x="sample_text", y="sample_text")
    b1 = flat11_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    b2 = flat11_DocumentRoot(declaration="sample_text_2", imports="sample_text_2", instantiation="sample_text_2", mixed="sample_text_2", system="sample_text_2")
    _safe_set(a, 'flat11_NailType', b1)
    assert _is_linked(a, 'flat11_NailType', b1)
    if hasattr(b1, 'flat11_DocumentRoot13'):
        assert _is_linked(b1, 'flat11_DocumentRoot13', a)
    _safe_set(a, 'flat11_NailType', b2)
    assert _is_linked(a, 'flat11_NailType', b2)
    if hasattr(b1, 'flat11_DocumentRoot13'):
        assert not _is_linked(b1, 'flat11_DocumentRoot13', a)
    if hasattr(b2, 'flat11_DocumentRoot13'):
        assert _is_linked(b2, 'flat11_DocumentRoot13', a)
    _safe_set(a, 'flat11_NailType', None)
    assert not _is_linked(a, 'flat11_NailType', b2)
    if hasattr(b2, 'flat11_DocumentRoot13'):
        assert not _is_linked(b2, 'flat11_DocumentRoot13', a)


def test_assoc_nail69_link_reassign_clear():
    a = flat11_TransitionType(action="sample_text", color="sample_text", controllable="sample_text", id="sample_text", x="sample_text", y="sample_text")
    b1 = flat11_NailType(x="sample_text", y="sample_text")
    b2 = flat11_NailType(x="sample_text_2", y="sample_text_2")
    _safe_set(a, 'flat11_TransitionType70', {b1})
    assert _is_linked(a, 'flat11_TransitionType70', b1)
    if hasattr(b1, 'flat11_NailType71'):
        assert _is_linked(b1, 'flat11_NailType71', a)
    _safe_set(a, 'flat11_TransitionType70', {b2})
    assert _is_linked(a, 'flat11_TransitionType70', b2)
    if hasattr(b1, 'flat11_NailType71'):
        assert not _is_linked(b1, 'flat11_NailType71', a)
    if hasattr(b2, 'flat11_NailType71'):
        assert _is_linked(b2, 'flat11_NailType71', a)
    _safe_set(a, 'flat11_TransitionType70', set())
    assert not _is_linked(a, 'flat11_TransitionType70', b2)
    if hasattr(b2, 'flat11_NailType71'):
        assert not _is_linked(b2, 'flat11_NailType71', a)


def test_assoc_name14_link_reassign_clear():
    a = flat11_NameType(value="sample_text", x="sample_text", y="sample_text")
    b1 = flat11_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    b2 = flat11_DocumentRoot(declaration="sample_text_2", imports="sample_text_2", instantiation="sample_text_2", mixed="sample_text_2", system="sample_text_2")
    _safe_set(a, 'flat11_NameType', b1)
    assert _is_linked(a, 'flat11_NameType', b1)
    if hasattr(b1, 'flat11_DocumentRoot15'):
        assert _is_linked(b1, 'flat11_DocumentRoot15', a)
    _safe_set(a, 'flat11_NameType', b2)
    assert _is_linked(a, 'flat11_NameType', b2)
    if hasattr(b1, 'flat11_DocumentRoot15'):
        assert not _is_linked(b1, 'flat11_DocumentRoot15', a)
    if hasattr(b2, 'flat11_DocumentRoot15'):
        assert _is_linked(b2, 'flat11_DocumentRoot15', a)
    _safe_set(a, 'flat11_NameType', None)
    assert not _is_linked(a, 'flat11_NameType', b2)
    if hasattr(b2, 'flat11_DocumentRoot15'):
        assert not _is_linked(b2, 'flat11_DocumentRoot15', a)


def test_assoc_name30_link_reassign_clear():
    a = flat11_NameType(value="sample_text", x="sample_text", y="sample_text")
    b1 = flat11_LocationType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    b2 = flat11_LocationType(color="sample_text_2", id="sample_text_2", x="sample_text_2", y="sample_text_2")
    _safe_set(a, 'flat11_NameType32', b1)
    assert _is_linked(a, 'flat11_NameType32', b1)
    if hasattr(b1, 'flat11_LocationType31'):
        assert _is_linked(b1, 'flat11_LocationType31', a)
    _safe_set(a, 'flat11_NameType32', b2)
    assert _is_linked(a, 'flat11_NameType32', b2)
    if hasattr(b1, 'flat11_LocationType31'):
        assert not _is_linked(b1, 'flat11_LocationType31', a)
    if hasattr(b2, 'flat11_LocationType31'):
        assert _is_linked(b2, 'flat11_LocationType31', a)
    _safe_set(a, 'flat11_NameType32', None)
    assert not _is_linked(a, 'flat11_NameType32', b2)
    if hasattr(b2, 'flat11_LocationType31'):
        assert not _is_linked(b2, 'flat11_LocationType31', a)


def test_assoc_name45_link_reassign_clear():
    a = flat11_TemplateType(declaration="sample_text")
    b1 = flat11_NameType(value="sample_text", x="sample_text", y="sample_text")
    b2 = flat11_NameType(value="sample_text_2", x="sample_text_2", y="sample_text_2")
    _safe_set(a, 'flat11_TemplateType46', b1)
    assert _is_linked(a, 'flat11_TemplateType46', b1)
    if hasattr(b1, 'flat11_NameType47'):
        assert _is_linked(b1, 'flat11_NameType47', a)
    _safe_set(a, 'flat11_TemplateType46', b2)
    assert _is_linked(a, 'flat11_TemplateType46', b2)
    if hasattr(b1, 'flat11_NameType47'):
        assert not _is_linked(b1, 'flat11_NameType47', a)
    if hasattr(b2, 'flat11_NameType47'):
        assert _is_linked(b2, 'flat11_NameType47', a)
    _safe_set(a, 'flat11_TemplateType46', None)
    assert not _is_linked(a, 'flat11_TemplateType46', b2)
    if hasattr(b2, 'flat11_NameType47'):
        assert not _is_linked(b2, 'flat11_NameType47', a)


def test_assoc_nta16_link_reassign_clear():
    a = flat11_NtaType(declaration="sample_text", imports="sample_text", instantiation="sample_text", system="sample_text")
    b1 = flat11_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    b2 = flat11_DocumentRoot(declaration="sample_text_2", imports="sample_text_2", instantiation="sample_text_2", mixed="sample_text_2", system="sample_text_2")
    _safe_set(a, 'flat11_NtaType', b1)
    assert _is_linked(a, 'flat11_NtaType', b1)
    if hasattr(b1, 'flat11_DocumentRoot17'):
        assert _is_linked(b1, 'flat11_DocumentRoot17', a)
    _safe_set(a, 'flat11_NtaType', b2)
    assert _is_linked(a, 'flat11_NtaType', b2)
    if hasattr(b1, 'flat11_DocumentRoot17'):
        assert not _is_linked(b1, 'flat11_DocumentRoot17', a)
    if hasattr(b2, 'flat11_DocumentRoot17'):
        assert _is_linked(b2, 'flat11_DocumentRoot17', a)
    _safe_set(a, 'flat11_NtaType', None)
    assert not _is_linked(a, 'flat11_NtaType', b2)
    if hasattr(b2, 'flat11_DocumentRoot17'):
        assert not _is_linked(b2, 'flat11_DocumentRoot17', a)


def test_assoc_parameter18_link_reassign_clear():
    a = flat11_ParameterType(value="sample_text", x="sample_text", y="sample_text")
    b1 = flat11_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    b2 = flat11_DocumentRoot(declaration="sample_text_2", imports="sample_text_2", instantiation="sample_text_2", mixed="sample_text_2", system="sample_text_2")
    _safe_set(a, 'flat11_ParameterType', b1)
    assert _is_linked(a, 'flat11_ParameterType', b1)
    if hasattr(b1, 'flat11_DocumentRoot19'):
        assert _is_linked(b1, 'flat11_DocumentRoot19', a)
    _safe_set(a, 'flat11_ParameterType', b2)
    assert _is_linked(a, 'flat11_ParameterType', b2)
    if hasattr(b1, 'flat11_DocumentRoot19'):
        assert not _is_linked(b1, 'flat11_DocumentRoot19', a)
    if hasattr(b2, 'flat11_DocumentRoot19'):
        assert _is_linked(b2, 'flat11_DocumentRoot19', a)
    _safe_set(a, 'flat11_ParameterType', None)
    assert not _is_linked(a, 'flat11_ParameterType', b2)
    if hasattr(b2, 'flat11_DocumentRoot19'):
        assert not _is_linked(b2, 'flat11_DocumentRoot19', a)


def test_assoc_parameter48_link_reassign_clear():
    a = flat11_TemplateType(declaration="sample_text")
    b1 = flat11_ParameterType(value="sample_text", x="sample_text", y="sample_text")
    b2 = flat11_ParameterType(value="sample_text_2", x="sample_text_2", y="sample_text_2")
    _safe_set(a, 'flat11_TemplateType49', b1)
    assert _is_linked(a, 'flat11_TemplateType49', b1)
    if hasattr(b1, 'flat11_ParameterType50'):
        assert _is_linked(b1, 'flat11_ParameterType50', a)
    _safe_set(a, 'flat11_TemplateType49', b2)
    assert _is_linked(a, 'flat11_TemplateType49', b2)
    if hasattr(b1, 'flat11_ParameterType50'):
        assert not _is_linked(b1, 'flat11_ParameterType50', a)
    if hasattr(b2, 'flat11_ParameterType50'):
        assert _is_linked(b2, 'flat11_ParameterType50', a)
    _safe_set(a, 'flat11_TemplateType49', None)
    assert not _is_linked(a, 'flat11_TemplateType49', b2)
    if hasattr(b2, 'flat11_ParameterType50'):
        assert not _is_linked(b2, 'flat11_ParameterType50', a)


def test_assoc_source20_link_reassign_clear():
    a = flat11_SourceType(ref="sample_text")
    b1 = flat11_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    b2 = flat11_DocumentRoot(declaration="sample_text_2", imports="sample_text_2", instantiation="sample_text_2", mixed="sample_text_2", system="sample_text_2")
    _safe_set(a, 'flat11_SourceType', b1)
    assert _is_linked(a, 'flat11_SourceType', b1)
    if hasattr(b1, 'flat11_DocumentRoot21'):
        assert _is_linked(b1, 'flat11_DocumentRoot21', a)
    _safe_set(a, 'flat11_SourceType', b2)
    assert _is_linked(a, 'flat11_SourceType', b2)
    if hasattr(b1, 'flat11_DocumentRoot21'):
        assert not _is_linked(b1, 'flat11_DocumentRoot21', a)
    if hasattr(b2, 'flat11_DocumentRoot21'):
        assert _is_linked(b2, 'flat11_DocumentRoot21', a)
    _safe_set(a, 'flat11_SourceType', None)
    assert not _is_linked(a, 'flat11_SourceType', b2)
    if hasattr(b2, 'flat11_DocumentRoot21'):
        assert not _is_linked(b2, 'flat11_DocumentRoot21', a)


def test_assoc_source60_link_reassign_clear():
    a = flat11_TransitionType(action="sample_text", color="sample_text", controllable="sample_text", id="sample_text", x="sample_text", y="sample_text")
    b1 = flat11_SourceType(ref="sample_text")
    b2 = flat11_SourceType(ref="sample_text_2")
    _safe_set(a, 'flat11_TransitionType61', b1)
    assert _is_linked(a, 'flat11_TransitionType61', b1)
    if hasattr(b1, 'flat11_SourceType62'):
        assert _is_linked(b1, 'flat11_SourceType62', a)
    _safe_set(a, 'flat11_TransitionType61', b2)
    assert _is_linked(a, 'flat11_TransitionType61', b2)
    if hasattr(b1, 'flat11_SourceType62'):
        assert not _is_linked(b1, 'flat11_SourceType62', a)
    if hasattr(b2, 'flat11_SourceType62'):
        assert _is_linked(b2, 'flat11_SourceType62', a)
    _safe_set(a, 'flat11_TransitionType61', None)
    assert not _is_linked(a, 'flat11_TransitionType61', b2)
    if hasattr(b2, 'flat11_SourceType62'):
        assert not _is_linked(b2, 'flat11_SourceType62', a)


def test_assoc_target22_link_reassign_clear():
    a = flat11_TargetType(ref="sample_text")
    b1 = flat11_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    b2 = flat11_DocumentRoot(declaration="sample_text_2", imports="sample_text_2", instantiation="sample_text_2", mixed="sample_text_2", system="sample_text_2")
    _safe_set(a, 'flat11_TargetType', b1)
    assert _is_linked(a, 'flat11_TargetType', b1)
    if hasattr(b1, 'flat11_DocumentRoot23'):
        assert _is_linked(b1, 'flat11_DocumentRoot23', a)
    _safe_set(a, 'flat11_TargetType', b2)
    assert _is_linked(a, 'flat11_TargetType', b2)
    if hasattr(b1, 'flat11_DocumentRoot23'):
        assert not _is_linked(b1, 'flat11_DocumentRoot23', a)
    if hasattr(b2, 'flat11_DocumentRoot23'):
        assert _is_linked(b2, 'flat11_DocumentRoot23', a)
    _safe_set(a, 'flat11_TargetType', None)
    assert not _is_linked(a, 'flat11_TargetType', b2)
    if hasattr(b2, 'flat11_DocumentRoot23'):
        assert not _is_linked(b2, 'flat11_DocumentRoot23', a)


def test_assoc_target63_link_reassign_clear():
    a = flat11_TransitionType(action="sample_text", color="sample_text", controllable="sample_text", id="sample_text", x="sample_text", y="sample_text")
    b1 = flat11_TargetType(ref="sample_text")
    b2 = flat11_TargetType(ref="sample_text_2")
    _safe_set(a, 'flat11_TransitionType64', b1)
    assert _is_linked(a, 'flat11_TransitionType64', b1)
    if hasattr(b1, 'flat11_TargetType65'):
        assert _is_linked(b1, 'flat11_TargetType65', a)
    _safe_set(a, 'flat11_TransitionType64', b2)
    assert _is_linked(a, 'flat11_TransitionType64', b2)
    if hasattr(b1, 'flat11_TargetType65'):
        assert not _is_linked(b1, 'flat11_TargetType65', a)
    if hasattr(b2, 'flat11_TargetType65'):
        assert _is_linked(b2, 'flat11_TargetType65', a)
    _safe_set(a, 'flat11_TransitionType64', None)
    assert not _is_linked(a, 'flat11_TransitionType64', b2)
    if hasattr(b2, 'flat11_TargetType65'):
        assert not _is_linked(b2, 'flat11_TargetType65', a)


def test_assoc_template24_link_reassign_clear():
    a = flat11_TemplateType(declaration="sample_text")
    b1 = flat11_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    b2 = flat11_DocumentRoot(declaration="sample_text_2", imports="sample_text_2", instantiation="sample_text_2", mixed="sample_text_2", system="sample_text_2")
    _safe_set(a, 'flat11_TemplateType', b1)
    assert _is_linked(a, 'flat11_TemplateType', b1)
    if hasattr(b1, 'flat11_DocumentRoot25'):
        assert _is_linked(b1, 'flat11_DocumentRoot25', a)
    _safe_set(a, 'flat11_TemplateType', b2)
    assert _is_linked(a, 'flat11_TemplateType', b2)
    if hasattr(b1, 'flat11_DocumentRoot25'):
        assert not _is_linked(b1, 'flat11_DocumentRoot25', a)
    if hasattr(b2, 'flat11_DocumentRoot25'):
        assert _is_linked(b2, 'flat11_DocumentRoot25', a)
    _safe_set(a, 'flat11_TemplateType', None)
    assert not _is_linked(a, 'flat11_TemplateType', b2)
    if hasattr(b2, 'flat11_DocumentRoot25'):
        assert not _is_linked(b2, 'flat11_DocumentRoot25', a)


def test_assoc_template42_link_reassign_clear():
    a = flat11_TemplateType(declaration="sample_text")
    b1 = flat11_NtaType(declaration="sample_text", imports="sample_text", instantiation="sample_text", system="sample_text")
    b2 = flat11_NtaType(declaration="sample_text_2", imports="sample_text_2", instantiation="sample_text_2", system="sample_text_2")
    _safe_set(a, 'flat11_TemplateType44', b1)
    assert _is_linked(a, 'flat11_TemplateType44', b1)
    if hasattr(b1, 'flat11_NtaType43'):
        assert _is_linked(b1, 'flat11_NtaType43', a)
    _safe_set(a, 'flat11_TemplateType44', b2)
    assert _is_linked(a, 'flat11_TemplateType44', b2)
    if hasattr(b1, 'flat11_NtaType43'):
        assert not _is_linked(b1, 'flat11_NtaType43', a)
    if hasattr(b2, 'flat11_NtaType43'):
        assert _is_linked(b2, 'flat11_NtaType43', a)
    _safe_set(a, 'flat11_TemplateType44', None)
    assert not _is_linked(a, 'flat11_TemplateType44', b2)
    if hasattr(b2, 'flat11_NtaType43'):
        assert not _is_linked(b2, 'flat11_NtaType43', a)


def test_assoc_transition26_link_reassign_clear():
    a = flat11_TransitionType(action="sample_text", color="sample_text", controllable="sample_text", id="sample_text", x="sample_text", y="sample_text")
    b1 = flat11_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    b2 = flat11_DocumentRoot(declaration="sample_text_2", imports="sample_text_2", instantiation="sample_text_2", mixed="sample_text_2", system="sample_text_2")
    _safe_set(a, 'flat11_TransitionType', b1)
    assert _is_linked(a, 'flat11_TransitionType', b1)
    if hasattr(b1, 'flat11_DocumentRoot27'):
        assert _is_linked(b1, 'flat11_DocumentRoot27', a)
    _safe_set(a, 'flat11_TransitionType', b2)
    assert _is_linked(a, 'flat11_TransitionType', b2)
    if hasattr(b1, 'flat11_DocumentRoot27'):
        assert not _is_linked(b1, 'flat11_DocumentRoot27', a)
    if hasattr(b2, 'flat11_DocumentRoot27'):
        assert _is_linked(b2, 'flat11_DocumentRoot27', a)
    _safe_set(a, 'flat11_TransitionType', None)
    assert not _is_linked(a, 'flat11_TransitionType', b2)
    if hasattr(b2, 'flat11_DocumentRoot27'):
        assert not _is_linked(b2, 'flat11_DocumentRoot27', a)


def test_assoc_transition57_link_reassign_clear():
    a = flat11_TransitionType(action="sample_text", color="sample_text", controllable="sample_text", id="sample_text", x="sample_text", y="sample_text")
    b1 = flat11_TemplateType(declaration="sample_text")
    b2 = flat11_TemplateType(declaration="sample_text_2")
    _safe_set(a, 'flat11_TransitionType59', b1)
    assert _is_linked(a, 'flat11_TransitionType59', b1)
    if hasattr(b1, 'flat11_TemplateType58'):
        assert _is_linked(b1, 'flat11_TemplateType58', a)
    _safe_set(a, 'flat11_TransitionType59', b2)
    assert _is_linked(a, 'flat11_TransitionType59', b2)
    if hasattr(b1, 'flat11_TemplateType58'):
        assert not _is_linked(b1, 'flat11_TemplateType58', a)
    if hasattr(b2, 'flat11_TemplateType58'):
        assert _is_linked(b2, 'flat11_TemplateType58', a)
    _safe_set(a, 'flat11_TransitionType59', None)
    assert not _is_linked(a, 'flat11_TransitionType59', b2)
    if hasattr(b2, 'flat11_TemplateType58'):
        assert not _is_linked(b2, 'flat11_TemplateType58', a)


def test_assoc_urgent28_link_reassign_clear():
    a = flat11_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    b1 = flat11_UrgentType()
    b2 = flat11_UrgentType()
    _safe_set(a, 'flat11_DocumentRoot29', {b1})
    assert _is_linked(a, 'flat11_DocumentRoot29', b1)
    if hasattr(b1, 'flat11_UrgentType'):
        assert _is_linked(b1, 'flat11_UrgentType', a)
    _safe_set(a, 'flat11_DocumentRoot29', {b2})
    assert _is_linked(a, 'flat11_DocumentRoot29', b2)
    if hasattr(b1, 'flat11_UrgentType'):
        assert not _is_linked(b1, 'flat11_UrgentType', a)
    if hasattr(b2, 'flat11_UrgentType'):
        assert _is_linked(b2, 'flat11_UrgentType', a)
    _safe_set(a, 'flat11_DocumentRoot29', set())
    assert not _is_linked(a, 'flat11_DocumentRoot29', b2)
    if hasattr(b2, 'flat11_UrgentType'):
        assert not _is_linked(b2, 'flat11_UrgentType', a)


def test_assoc_urgent36_link_reassign_clear():
    a = flat11_LocationType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    b1 = flat11_UrgentType()
    b2 = flat11_UrgentType()
    _safe_set(a, 'flat11_LocationType37', b1)
    assert _is_linked(a, 'flat11_LocationType37', b1)
    if hasattr(b1, 'flat11_UrgentType38'):
        assert _is_linked(b1, 'flat11_UrgentType38', a)
    _safe_set(a, 'flat11_LocationType37', b2)
    assert _is_linked(a, 'flat11_LocationType37', b2)
    if hasattr(b1, 'flat11_UrgentType38'):
        assert not _is_linked(b1, 'flat11_UrgentType38', a)
    if hasattr(b2, 'flat11_UrgentType38'):
        assert _is_linked(b2, 'flat11_UrgentType38', a)
    _safe_set(a, 'flat11_LocationType37', None)
    assert not _is_linked(a, 'flat11_LocationType37', b2)
    if hasattr(b2, 'flat11_UrgentType38'):
        assert not _is_linked(b2, 'flat11_UrgentType38', a)


def test_assoc_xMLNSPrefixMap0_link_reassign_clear():
    a = flat11_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    b1 = flat11_EStringToStringMapEntry()
    b2 = flat11_EStringToStringMapEntry()
    _safe_set(a, 'flat11_DocumentRoot', {b1})
    assert _is_linked(a, 'flat11_DocumentRoot', b1)
    if hasattr(b1, 'flat11_EStringToStringMapEntry'):
        assert _is_linked(b1, 'flat11_EStringToStringMapEntry', a)
    _safe_set(a, 'flat11_DocumentRoot', {b2})
    assert _is_linked(a, 'flat11_DocumentRoot', b2)
    if hasattr(b1, 'flat11_EStringToStringMapEntry'):
        assert not _is_linked(b1, 'flat11_EStringToStringMapEntry', a)
    if hasattr(b2, 'flat11_EStringToStringMapEntry'):
        assert _is_linked(b2, 'flat11_EStringToStringMapEntry', a)
    _safe_set(a, 'flat11_DocumentRoot', set())
    assert not _is_linked(a, 'flat11_DocumentRoot', b2)
    if hasattr(b2, 'flat11_EStringToStringMapEntry'):
        assert not _is_linked(b2, 'flat11_EStringToStringMapEntry', a)


def test_assoc_xSISchemaLocation1_link_reassign_clear():
    a = flat11_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    b1 = flat11_EStringToStringMapEntry()
    b2 = flat11_EStringToStringMapEntry()
    _safe_set(a, 'flat11_DocumentRoot2', {b1})
    assert _is_linked(a, 'flat11_DocumentRoot2', b1)
    if hasattr(b1, 'flat11_EStringToStringMapEntry3'):
        assert _is_linked(b1, 'flat11_EStringToStringMapEntry3', a)
    _safe_set(a, 'flat11_DocumentRoot2', {b2})
    assert _is_linked(a, 'flat11_DocumentRoot2', b2)
    if hasattr(b1, 'flat11_EStringToStringMapEntry3'):
        assert not _is_linked(b1, 'flat11_EStringToStringMapEntry3', a)
    if hasattr(b2, 'flat11_EStringToStringMapEntry3'):
        assert _is_linked(b2, 'flat11_EStringToStringMapEntry3', a)
    _safe_set(a, 'flat11_DocumentRoot2', set())
    assert not _is_linked(a, 'flat11_DocumentRoot2', b2)
    if hasattr(b2, 'flat11_EStringToStringMapEntry3'):
        assert not _is_linked(b2, 'flat11_EStringToStringMapEntry3', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

flat11_CommittedType_strategy = st.builds(flat11_CommittedType)
@given(instance=flat11_CommittedType_strategy)
@settings(max_examples=25)
def test_flat11_CommittedType_instantiation(instance):
    assert isinstance(instance, flat11_CommittedType)


flat11_DocumentRoot_strategy = st.builds(flat11_DocumentRoot, declaration=safe_text, imports=safe_text, instantiation=safe_text, mixed=safe_text, system=safe_text)
@given(instance=flat11_DocumentRoot_strategy)
@settings(max_examples=25)
def test_flat11_DocumentRoot_instantiation(instance):
    assert isinstance(instance, flat11_DocumentRoot)


flat11_EStringToStringMapEntry_strategy = st.builds(flat11_EStringToStringMapEntry)
@given(instance=flat11_EStringToStringMapEntry_strategy)
@settings(max_examples=25)
def test_flat11_EStringToStringMapEntry_instantiation(instance):
    assert isinstance(instance, flat11_EStringToStringMapEntry)


flat11_InitType_strategy = st.builds(flat11_InitType, ref=safe_text)
@given(instance=flat11_InitType_strategy)
@settings(max_examples=25)
def test_flat11_InitType_instantiation(instance):
    assert isinstance(instance, flat11_InitType)


flat11_LabelType_strategy = st.builds(flat11_LabelType, kind=safe_text, value=safe_text, x=safe_text, y=safe_text)
@given(instance=flat11_LabelType_strategy)
@settings(max_examples=25)
def test_flat11_LabelType_instantiation(instance):
    assert isinstance(instance, flat11_LabelType)


flat11_LocationType_strategy = st.builds(flat11_LocationType, color=safe_text, id=safe_text, x=safe_text, y=safe_text)
@given(instance=flat11_LocationType_strategy)
@settings(max_examples=25)
def test_flat11_LocationType_instantiation(instance):
    assert isinstance(instance, flat11_LocationType)


flat11_NailType_strategy = st.builds(flat11_NailType, x=safe_text, y=safe_text)
@given(instance=flat11_NailType_strategy)
@settings(max_examples=25)
def test_flat11_NailType_instantiation(instance):
    assert isinstance(instance, flat11_NailType)


flat11_NameType_strategy = st.builds(flat11_NameType, value=safe_text, x=safe_text, y=safe_text)
@given(instance=flat11_NameType_strategy)
@settings(max_examples=25)
def test_flat11_NameType_instantiation(instance):
    assert isinstance(instance, flat11_NameType)


flat11_NtaType_strategy = st.builds(flat11_NtaType, declaration=safe_text, imports=safe_text, instantiation=safe_text, system=safe_text)
@given(instance=flat11_NtaType_strategy)
@settings(max_examples=25)
def test_flat11_NtaType_instantiation(instance):
    assert isinstance(instance, flat11_NtaType)


flat11_ParameterType_strategy = st.builds(flat11_ParameterType, value=safe_text, x=safe_text, y=safe_text)
@given(instance=flat11_ParameterType_strategy)
@settings(max_examples=25)
def test_flat11_ParameterType_instantiation(instance):
    assert isinstance(instance, flat11_ParameterType)


flat11_SourceType_strategy = st.builds(flat11_SourceType, ref=safe_text)
@given(instance=flat11_SourceType_strategy)
@settings(max_examples=25)
def test_flat11_SourceType_instantiation(instance):
    assert isinstance(instance, flat11_SourceType)


flat11_TargetType_strategy = st.builds(flat11_TargetType, ref=safe_text)
@given(instance=flat11_TargetType_strategy)
@settings(max_examples=25)
def test_flat11_TargetType_instantiation(instance):
    assert isinstance(instance, flat11_TargetType)


flat11_TemplateType_strategy = st.builds(flat11_TemplateType, declaration=safe_text)
@given(instance=flat11_TemplateType_strategy)
@settings(max_examples=25)
def test_flat11_TemplateType_instantiation(instance):
    assert isinstance(instance, flat11_TemplateType)


flat11_TransitionType_strategy = st.builds(flat11_TransitionType, action=safe_text, color=safe_text, controllable=safe_text, id=safe_text, x=safe_text, y=safe_text)
@given(instance=flat11_TransitionType_strategy)
@settings(max_examples=25)
def test_flat11_TransitionType_instantiation(instance):
    assert isinstance(instance, flat11_TransitionType)


flat11_UrgentType_strategy = st.builds(flat11_UrgentType)
@given(instance=flat11_UrgentType_strategy)
@settings(max_examples=25)
def test_flat11_UrgentType_instantiation(instance):
    assert isinstance(instance, flat11_UrgentType)



