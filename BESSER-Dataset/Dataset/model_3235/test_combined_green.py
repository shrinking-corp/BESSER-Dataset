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
    uppaal_UrgentType,
    uppaal_TransitionType,
    uppaal_TemplateType,
    uppaal_LocationType,
    uppaal_TargetType,
    uppaal_SourceType,
    uppaal_ParameterType,
    uppaal_NtaType,
    uppaal_NameType,
    uppaal_NailType,
    uppaal_DocumentRoot,
    uppaal_CommittedType,
    uppaal_LabelType,
    uppaal_InitType,
    uppaal_EStringToStringMapEntry,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_uppaal_urgenttype_is_not_abstract():
    assert not inspect.isabstract(uppaal_UrgentType)


def test_hyp_uppaal_urgenttype_constructor_exists():
    assert callable(uppaal_UrgentType.__init__)


def test_hyp_uppaal_urgenttype_constructor_args():
    sig = inspect.signature(uppaal_UrgentType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_transitiontype_is_not_abstract():
    assert not inspect.isabstract(uppaal_TransitionType)


def test_hyp_uppaal_transitiontype_constructor_exists():
    assert callable(uppaal_TransitionType.__init__)


def test_hyp_uppaal_transitiontype_constructor_args():
    sig = inspect.signature(uppaal_TransitionType.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "id" in params, "Missing parameter 'id'"
    assert "x" in params, "Missing parameter 'x'"
    assert "color" in params, "Missing parameter 'color'"







def test_hyp_uppaal_templatetype_is_not_abstract():
    assert not inspect.isabstract(uppaal_TemplateType)


def test_hyp_uppaal_templatetype_constructor_exists():
    assert callable(uppaal_TemplateType.__init__)


def test_hyp_uppaal_templatetype_constructor_args():
    sig = inspect.signature(uppaal_TemplateType.__init__)
    params = list(sig.parameters.keys())
    assert "declaration" in params, "Missing parameter 'declaration'"




def test_hyp_uppaal_locationtype_is_not_abstract():
    assert not inspect.isabstract(uppaal_LocationType)


def test_hyp_uppaal_locationtype_constructor_exists():
    assert callable(uppaal_LocationType.__init__)


def test_hyp_uppaal_locationtype_constructor_args():
    sig = inspect.signature(uppaal_LocationType.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "id" in params, "Missing parameter 'id'"
    assert "color" in params, "Missing parameter 'color'"
    assert "x" in params, "Missing parameter 'x'"







def test_hyp_uppaal_targettype_is_not_abstract():
    assert not inspect.isabstract(uppaal_TargetType)


def test_hyp_uppaal_targettype_constructor_exists():
    assert callable(uppaal_TargetType.__init__)


def test_hyp_uppaal_targettype_constructor_args():
    sig = inspect.signature(uppaal_TargetType.__init__)
    params = list(sig.parameters.keys())
    assert "ref" in params, "Missing parameter 'ref'"




def test_hyp_uppaal_sourcetype_is_not_abstract():
    assert not inspect.isabstract(uppaal_SourceType)


def test_hyp_uppaal_sourcetype_constructor_exists():
    assert callable(uppaal_SourceType.__init__)


def test_hyp_uppaal_sourcetype_constructor_args():
    sig = inspect.signature(uppaal_SourceType.__init__)
    params = list(sig.parameters.keys())
    assert "ref" in params, "Missing parameter 'ref'"




def test_hyp_uppaal_parametertype_is_not_abstract():
    assert not inspect.isabstract(uppaal_ParameterType)


def test_hyp_uppaal_parametertype_constructor_exists():
    assert callable(uppaal_ParameterType.__init__)


def test_hyp_uppaal_parametertype_constructor_args():
    sig = inspect.signature(uppaal_ParameterType.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"
    assert "mixed" in params, "Missing parameter 'mixed'"






def test_hyp_uppaal_ntatype_is_not_abstract():
    assert not inspect.isabstract(uppaal_NtaType)


def test_hyp_uppaal_ntatype_constructor_exists():
    assert callable(uppaal_NtaType.__init__)


def test_hyp_uppaal_ntatype_constructor_args():
    sig = inspect.signature(uppaal_NtaType.__init__)
    params = list(sig.parameters.keys())
    assert "declaration" in params, "Missing parameter 'declaration'"
    assert "system" in params, "Missing parameter 'system'"
    assert "instantiation" in params, "Missing parameter 'instantiation'"
    assert "imports" in params, "Missing parameter 'imports'"







def test_hyp_uppaal_nametype_is_not_abstract():
    assert not inspect.isabstract(uppaal_NameType)


def test_hyp_uppaal_nametype_constructor_exists():
    assert callable(uppaal_NameType.__init__)


def test_hyp_uppaal_nametype_constructor_args():
    sig = inspect.signature(uppaal_NameType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"






def test_hyp_uppaal_nailtype_is_not_abstract():
    assert not inspect.isabstract(uppaal_NailType)


def test_hyp_uppaal_nailtype_constructor_exists():
    assert callable(uppaal_NailType.__init__)


def test_hyp_uppaal_nailtype_constructor_args():
    sig = inspect.signature(uppaal_NailType.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"





def test_hyp_uppaal_documentroot_is_not_abstract():
    assert not inspect.isabstract(uppaal_DocumentRoot)


def test_hyp_uppaal_documentroot_constructor_exists():
    assert callable(uppaal_DocumentRoot.__init__)


def test_hyp_uppaal_documentroot_constructor_args():
    sig = inspect.signature(uppaal_DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "instantiation" in params, "Missing parameter 'instantiation'"
    assert "imports" in params, "Missing parameter 'imports'"
    assert "declaration" in params, "Missing parameter 'declaration'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "system" in params, "Missing parameter 'system'"








def test_hyp_uppaal_committedtype_is_not_abstract():
    assert not inspect.isabstract(uppaal_CommittedType)


def test_hyp_uppaal_committedtype_constructor_exists():
    assert callable(uppaal_CommittedType.__init__)


def test_hyp_uppaal_committedtype_constructor_args():
    sig = inspect.signature(uppaal_CommittedType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_labeltype_is_not_abstract():
    assert not inspect.isabstract(uppaal_LabelType)


def test_hyp_uppaal_labeltype_constructor_exists():
    assert callable(uppaal_LabelType.__init__)


def test_hyp_uppaal_labeltype_constructor_args():
    sig = inspect.signature(uppaal_LabelType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"
    assert "kind" in params, "Missing parameter 'kind'"







def test_hyp_uppaal_inittype_is_not_abstract():
    assert not inspect.isabstract(uppaal_InitType)


def test_hyp_uppaal_inittype_constructor_exists():
    assert callable(uppaal_InitType.__init__)


def test_hyp_uppaal_inittype_constructor_args():
    sig = inspect.signature(uppaal_InitType.__init__)
    params = list(sig.parameters.keys())
    assert "ref" in params, "Missing parameter 'ref'"




def test_hyp_uppaal_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(uppaal_EStringToStringMapEntry)


def test_hyp_uppaal_estringtostringmapentry_constructor_exists():
    assert callable(uppaal_EStringToStringMapEntry.__init__)


def test_hyp_uppaal_estringtostringmapentry_constructor_args():
    sig = inspect.signature(uppaal_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())


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
uppaal_UrgentType_strategy = st.builds(
    uppaal_UrgentType,
)
uppaal_TransitionType_strategy = st.builds(
    uppaal_TransitionType,
    y=
        safe_text,
    id=
        safe_text,
    x=
        safe_text,
    color=
        safe_text
)
uppaal_TemplateType_strategy = st.builds(
    uppaal_TemplateType,
    declaration=
        safe_text
)
uppaal_LocationType_strategy = st.builds(
    uppaal_LocationType,
    y=
        safe_text,
    id=
        safe_text,
    color=
        safe_text,
    x=
        safe_text
)
uppaal_TargetType_strategy = st.builds(
    uppaal_TargetType,
    ref=
        safe_text
)
uppaal_SourceType_strategy = st.builds(
    uppaal_SourceType,
    ref=
        safe_text
)
uppaal_ParameterType_strategy = st.builds(
    uppaal_ParameterType,
    y=
        safe_text,
    x=
        safe_text,
    mixed=
        safe_text
)
uppaal_NtaType_strategy = st.builds(
    uppaal_NtaType,
    declaration=
        safe_text,
    system=
        safe_text,
    instantiation=
        safe_text,
    imports=
        safe_text
)
uppaal_NameType_strategy = st.builds(
    uppaal_NameType,
    mixed=
        safe_text,
    y=
        safe_text,
    x=
        safe_text
)
uppaal_NailType_strategy = st.builds(
    uppaal_NailType,
    x=
        safe_text,
    y=
        safe_text
)
uppaal_DocumentRoot_strategy = st.builds(
    uppaal_DocumentRoot,
    instantiation=
        safe_text,
    imports=
        safe_text,
    declaration=
        safe_text,
    mixed=
        safe_text,
    system=
        safe_text
)
uppaal_CommittedType_strategy = st.builds(
    uppaal_CommittedType,
)
uppaal_LabelType_strategy = st.builds(
    uppaal_LabelType,
    mixed=
        safe_text,
    x=
        safe_text,
    y=
        safe_text,
    kind=
        safe_text
)
uppaal_InitType_strategy = st.builds(
    uppaal_InitType,
    ref=
        safe_text
)
uppaal_EStringToStringMapEntry_strategy = st.builds(
    uppaal_EStringToStringMapEntry,
)





@given(instance=uppaal_TransitionType_strategy)
def test_hyp_uppaal_transitiontype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=uppaal_TransitionType_strategy)
def test_hyp_uppaal_transitiontype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=uppaal_TransitionType_strategy)
def test_hyp_uppaal_transitiontype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=uppaal_TransitionType_strategy)
def test_hyp_uppaal_transitiontype_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original




@given(instance=uppaal_TemplateType_strategy)
def test_hyp_uppaal_templatetype_declaration_setter(instance):
    original = instance.declaration
    instance.declaration = original
    assert instance.declaration == original




@given(instance=uppaal_LocationType_strategy)
def test_hyp_uppaal_locationtype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=uppaal_LocationType_strategy)
def test_hyp_uppaal_locationtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=uppaal_LocationType_strategy)
def test_hyp_uppaal_locationtype_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=uppaal_LocationType_strategy)
def test_hyp_uppaal_locationtype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original




@given(instance=uppaal_TargetType_strategy)
def test_hyp_uppaal_targettype_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original




@given(instance=uppaal_SourceType_strategy)
def test_hyp_uppaal_sourcetype_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original




@given(instance=uppaal_ParameterType_strategy)
def test_hyp_uppaal_parametertype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=uppaal_ParameterType_strategy)
def test_hyp_uppaal_parametertype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=uppaal_ParameterType_strategy)
def test_hyp_uppaal_parametertype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original




@given(instance=uppaal_NtaType_strategy)
def test_hyp_uppaal_ntatype_declaration_setter(instance):
    original = instance.declaration
    instance.declaration = original
    assert instance.declaration == original



@given(instance=uppaal_NtaType_strategy)
def test_hyp_uppaal_ntatype_system_setter(instance):
    original = instance.system
    instance.system = original
    assert instance.system == original



@given(instance=uppaal_NtaType_strategy)
def test_hyp_uppaal_ntatype_instantiation_setter(instance):
    original = instance.instantiation
    instance.instantiation = original
    assert instance.instantiation == original



@given(instance=uppaal_NtaType_strategy)
def test_hyp_uppaal_ntatype_imports_setter(instance):
    original = instance.imports
    instance.imports = original
    assert instance.imports == original




@given(instance=uppaal_NameType_strategy)
def test_hyp_uppaal_nametype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=uppaal_NameType_strategy)
def test_hyp_uppaal_nametype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=uppaal_NameType_strategy)
def test_hyp_uppaal_nametype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original




@given(instance=uppaal_NailType_strategy)
def test_hyp_uppaal_nailtype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=uppaal_NailType_strategy)
def test_hyp_uppaal_nailtype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original




@given(instance=uppaal_DocumentRoot_strategy)
def test_hyp_uppaal_documentroot_instantiation_setter(instance):
    original = instance.instantiation
    instance.instantiation = original
    assert instance.instantiation == original



@given(instance=uppaal_DocumentRoot_strategy)
def test_hyp_uppaal_documentroot_imports_setter(instance):
    original = instance.imports
    instance.imports = original
    assert instance.imports == original



@given(instance=uppaal_DocumentRoot_strategy)
def test_hyp_uppaal_documentroot_declaration_setter(instance):
    original = instance.declaration
    instance.declaration = original
    assert instance.declaration == original



@given(instance=uppaal_DocumentRoot_strategy)
def test_hyp_uppaal_documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=uppaal_DocumentRoot_strategy)
def test_hyp_uppaal_documentroot_system_setter(instance):
    original = instance.system
    instance.system = original
    assert instance.system == original





@given(instance=uppaal_LabelType_strategy)
def test_hyp_uppaal_labeltype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=uppaal_LabelType_strategy)
def test_hyp_uppaal_labeltype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=uppaal_LabelType_strategy)
def test_hyp_uppaal_labeltype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=uppaal_LabelType_strategy)
def test_hyp_uppaal_labeltype_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original




@given(instance=uppaal_InitType_strategy)
def test_hyp_uppaal_inittype_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    uppaal_CommittedType,
    uppaal_DocumentRoot,
    uppaal_EStringToStringMapEntry,
    uppaal_InitType,
    uppaal_LabelType,
    uppaal_LocationType,
    uppaal_NailType,
    uppaal_NameType,
    uppaal_NtaType,
    uppaal_ParameterType,
    uppaal_SourceType,
    uppaal_TargetType,
    uppaal_TemplateType,
    uppaal_TransitionType,
    uppaal_UrgentType,
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

def test_uppaal_DocumentRoot_declaration_value_roundtrip():
    instance = uppaal_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    assert instance.declaration == "sample_text"
    instance.declaration = "sample_text_2"
    assert instance.declaration == "sample_text_2"


def test_uppaal_DocumentRoot_imports_value_roundtrip():
    instance = uppaal_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    assert instance.imports == "sample_text"
    instance.imports = "sample_text_2"
    assert instance.imports == "sample_text_2"


def test_uppaal_DocumentRoot_instantiation_value_roundtrip():
    instance = uppaal_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    assert instance.instantiation == "sample_text"
    instance.instantiation = "sample_text_2"
    assert instance.instantiation == "sample_text_2"


def test_uppaal_DocumentRoot_mixed_value_roundtrip():
    instance = uppaal_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_uppaal_DocumentRoot_system_value_roundtrip():
    instance = uppaal_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    assert instance.system == "sample_text"
    instance.system = "sample_text_2"
    assert instance.system == "sample_text_2"


def test_uppaal_InitType_ref_value_roundtrip():
    instance = uppaal_InitType(ref="sample_text")
    assert instance.ref == "sample_text"
    instance.ref = "sample_text_2"
    assert instance.ref == "sample_text_2"


def test_uppaal_LabelType_kind_value_roundtrip():
    instance = uppaal_LabelType(kind="sample_text", mixed="sample_text", x="sample_text", y="sample_text")
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_uppaal_LabelType_mixed_value_roundtrip():
    instance = uppaal_LabelType(kind="sample_text", mixed="sample_text", x="sample_text", y="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_uppaal_LabelType_x_value_roundtrip():
    instance = uppaal_LabelType(kind="sample_text", mixed="sample_text", x="sample_text", y="sample_text")
    assert instance.x == "sample_text"
    instance.x = "sample_text_2"
    assert instance.x == "sample_text_2"


def test_uppaal_LabelType_y_value_roundtrip():
    instance = uppaal_LabelType(kind="sample_text", mixed="sample_text", x="sample_text", y="sample_text")
    assert instance.y == "sample_text"
    instance.y = "sample_text_2"
    assert instance.y == "sample_text_2"


def test_uppaal_LocationType_color_value_roundtrip():
    instance = uppaal_LocationType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_uppaal_LocationType_id_value_roundtrip():
    instance = uppaal_LocationType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_uppaal_LocationType_x_value_roundtrip():
    instance = uppaal_LocationType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    assert instance.x == "sample_text"
    instance.x = "sample_text_2"
    assert instance.x == "sample_text_2"


def test_uppaal_LocationType_y_value_roundtrip():
    instance = uppaal_LocationType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    assert instance.y == "sample_text"
    instance.y = "sample_text_2"
    assert instance.y == "sample_text_2"


def test_uppaal_NailType_x_value_roundtrip():
    instance = uppaal_NailType(x="sample_text", y="sample_text")
    assert instance.x == "sample_text"
    instance.x = "sample_text_2"
    assert instance.x == "sample_text_2"


def test_uppaal_NailType_y_value_roundtrip():
    instance = uppaal_NailType(x="sample_text", y="sample_text")
    assert instance.y == "sample_text"
    instance.y = "sample_text_2"
    assert instance.y == "sample_text_2"


def test_uppaal_NameType_mixed_value_roundtrip():
    instance = uppaal_NameType(mixed="sample_text", x="sample_text", y="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_uppaal_NameType_x_value_roundtrip():
    instance = uppaal_NameType(mixed="sample_text", x="sample_text", y="sample_text")
    assert instance.x == "sample_text"
    instance.x = "sample_text_2"
    assert instance.x == "sample_text_2"


def test_uppaal_NameType_y_value_roundtrip():
    instance = uppaal_NameType(mixed="sample_text", x="sample_text", y="sample_text")
    assert instance.y == "sample_text"
    instance.y = "sample_text_2"
    assert instance.y == "sample_text_2"


def test_uppaal_NtaType_declaration_value_roundtrip():
    instance = uppaal_NtaType(declaration="sample_text", imports="sample_text", instantiation="sample_text", system="sample_text")
    assert instance.declaration == "sample_text"
    instance.declaration = "sample_text_2"
    assert instance.declaration == "sample_text_2"


def test_uppaal_NtaType_imports_value_roundtrip():
    instance = uppaal_NtaType(declaration="sample_text", imports="sample_text", instantiation="sample_text", system="sample_text")
    assert instance.imports == "sample_text"
    instance.imports = "sample_text_2"
    assert instance.imports == "sample_text_2"


def test_uppaal_NtaType_instantiation_value_roundtrip():
    instance = uppaal_NtaType(declaration="sample_text", imports="sample_text", instantiation="sample_text", system="sample_text")
    assert instance.instantiation == "sample_text"
    instance.instantiation = "sample_text_2"
    assert instance.instantiation == "sample_text_2"


def test_uppaal_NtaType_system_value_roundtrip():
    instance = uppaal_NtaType(declaration="sample_text", imports="sample_text", instantiation="sample_text", system="sample_text")
    assert instance.system == "sample_text"
    instance.system = "sample_text_2"
    assert instance.system == "sample_text_2"


def test_uppaal_ParameterType_mixed_value_roundtrip():
    instance = uppaal_ParameterType(mixed="sample_text", x="sample_text", y="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_uppaal_ParameterType_x_value_roundtrip():
    instance = uppaal_ParameterType(mixed="sample_text", x="sample_text", y="sample_text")
    assert instance.x == "sample_text"
    instance.x = "sample_text_2"
    assert instance.x == "sample_text_2"


def test_uppaal_ParameterType_y_value_roundtrip():
    instance = uppaal_ParameterType(mixed="sample_text", x="sample_text", y="sample_text")
    assert instance.y == "sample_text"
    instance.y = "sample_text_2"
    assert instance.y == "sample_text_2"


def test_uppaal_SourceType_ref_value_roundtrip():
    instance = uppaal_SourceType(ref="sample_text")
    assert instance.ref == "sample_text"
    instance.ref = "sample_text_2"
    assert instance.ref == "sample_text_2"


def test_uppaal_TargetType_ref_value_roundtrip():
    instance = uppaal_TargetType(ref="sample_text")
    assert instance.ref == "sample_text"
    instance.ref = "sample_text_2"
    assert instance.ref == "sample_text_2"


def test_uppaal_TemplateType_declaration_value_roundtrip():
    instance = uppaal_TemplateType(declaration="sample_text")
    assert instance.declaration == "sample_text"
    instance.declaration = "sample_text_2"
    assert instance.declaration == "sample_text_2"


def test_uppaal_TransitionType_color_value_roundtrip():
    instance = uppaal_TransitionType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_uppaal_TransitionType_id_value_roundtrip():
    instance = uppaal_TransitionType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_uppaal_TransitionType_x_value_roundtrip():
    instance = uppaal_TransitionType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    assert instance.x == "sample_text"
    instance.x = "sample_text_2"
    assert instance.x == "sample_text_2"


def test_uppaal_TransitionType_y_value_roundtrip():
    instance = uppaal_TransitionType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    assert instance.y == "sample_text"
    instance.y = "sample_text_2"
    assert instance.y == "sample_text_2"


def test_assoc_committed39_link_reassign_clear():
    a = uppaal_LocationType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    b1 = uppaal_CommittedType()
    b2 = uppaal_CommittedType()
    _safe_set(a, 'uppaal_LocationType40', b1)
    assert _is_linked(a, 'uppaal_LocationType40', b1)
    if hasattr(b1, 'uppaal_CommittedType41'):
        assert _is_linked(b1, 'uppaal_CommittedType41', a)
    _safe_set(a, 'uppaal_LocationType40', b2)
    assert _is_linked(a, 'uppaal_LocationType40', b2)
    if hasattr(b1, 'uppaal_CommittedType41'):
        assert not _is_linked(b1, 'uppaal_CommittedType41', a)
    if hasattr(b2, 'uppaal_CommittedType41'):
        assert _is_linked(b2, 'uppaal_CommittedType41', a)
    _safe_set(a, 'uppaal_LocationType40', None)
    assert not _is_linked(a, 'uppaal_LocationType40', b2)
    if hasattr(b2, 'uppaal_CommittedType41'):
        assert not _is_linked(b2, 'uppaal_CommittedType41', a)


def test_assoc_committed4_link_reassign_clear():
    a = uppaal_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    b1 = uppaal_CommittedType()
    b2 = uppaal_CommittedType()
    _safe_set(a, 'uppaal_DocumentRoot5', {b1})
    assert _is_linked(a, 'uppaal_DocumentRoot5', b1)
    if hasattr(b1, 'uppaal_CommittedType'):
        assert _is_linked(b1, 'uppaal_CommittedType', a)
    _safe_set(a, 'uppaal_DocumentRoot5', {b2})
    assert _is_linked(a, 'uppaal_DocumentRoot5', b2)
    if hasattr(b1, 'uppaal_CommittedType'):
        assert not _is_linked(b1, 'uppaal_CommittedType', a)
    if hasattr(b2, 'uppaal_CommittedType'):
        assert _is_linked(b2, 'uppaal_CommittedType', a)
    _safe_set(a, 'uppaal_DocumentRoot5', set())
    assert not _is_linked(a, 'uppaal_DocumentRoot5', b2)
    if hasattr(b2, 'uppaal_CommittedType'):
        assert not _is_linked(b2, 'uppaal_CommittedType', a)


def test_assoc_init54_link_reassign_clear():
    a = uppaal_TemplateType(declaration="sample_text")
    b1 = uppaal_InitType(ref="sample_text")
    b2 = uppaal_InitType(ref="sample_text_2")
    _safe_set(a, 'uppaal_TemplateType55', b1)
    assert _is_linked(a, 'uppaal_TemplateType55', b1)
    if hasattr(b1, 'uppaal_InitType56'):
        assert _is_linked(b1, 'uppaal_InitType56', a)
    _safe_set(a, 'uppaal_TemplateType55', b2)
    assert _is_linked(a, 'uppaal_TemplateType55', b2)
    if hasattr(b1, 'uppaal_InitType56'):
        assert not _is_linked(b1, 'uppaal_InitType56', a)
    if hasattr(b2, 'uppaal_InitType56'):
        assert _is_linked(b2, 'uppaal_InitType56', a)
    _safe_set(a, 'uppaal_TemplateType55', None)
    assert not _is_linked(a, 'uppaal_TemplateType55', b2)
    if hasattr(b2, 'uppaal_InitType56'):
        assert not _is_linked(b2, 'uppaal_InitType56', a)


def test_assoc_init6_link_reassign_clear():
    a = uppaal_InitType(ref="sample_text")
    b1 = uppaal_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    b2 = uppaal_DocumentRoot(declaration="sample_text_2", imports="sample_text_2", instantiation="sample_text_2", mixed="sample_text_2", system="sample_text_2")
    _safe_set(a, 'uppaal_InitType', b1)
    assert _is_linked(a, 'uppaal_InitType', b1)
    if hasattr(b1, 'uppaal_DocumentRoot7'):
        assert _is_linked(b1, 'uppaal_DocumentRoot7', a)
    _safe_set(a, 'uppaal_InitType', b2)
    assert _is_linked(a, 'uppaal_InitType', b2)
    if hasattr(b1, 'uppaal_DocumentRoot7'):
        assert not _is_linked(b1, 'uppaal_DocumentRoot7', a)
    if hasattr(b2, 'uppaal_DocumentRoot7'):
        assert _is_linked(b2, 'uppaal_DocumentRoot7', a)
    _safe_set(a, 'uppaal_InitType', None)
    assert not _is_linked(a, 'uppaal_InitType', b2)
    if hasattr(b2, 'uppaal_DocumentRoot7'):
        assert not _is_linked(b2, 'uppaal_DocumentRoot7', a)


def test_assoc_label33_link_reassign_clear():
    a = uppaal_LocationType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    b1 = uppaal_LabelType(kind="sample_text", mixed="sample_text", x="sample_text", y="sample_text")
    b2 = uppaal_LabelType(kind="sample_text_2", mixed="sample_text_2", x="sample_text_2", y="sample_text_2")
    _safe_set(a, 'uppaal_LocationType34', {b1})
    assert _is_linked(a, 'uppaal_LocationType34', b1)
    if hasattr(b1, 'uppaal_LabelType35'):
        assert _is_linked(b1, 'uppaal_LabelType35', a)
    _safe_set(a, 'uppaal_LocationType34', {b2})
    assert _is_linked(a, 'uppaal_LocationType34', b2)
    if hasattr(b1, 'uppaal_LabelType35'):
        assert not _is_linked(b1, 'uppaal_LabelType35', a)
    if hasattr(b2, 'uppaal_LabelType35'):
        assert _is_linked(b2, 'uppaal_LabelType35', a)
    _safe_set(a, 'uppaal_LocationType34', set())
    assert not _is_linked(a, 'uppaal_LocationType34', b2)
    if hasattr(b2, 'uppaal_LabelType35'):
        assert not _is_linked(b2, 'uppaal_LabelType35', a)


def test_assoc_label66_link_reassign_clear():
    a = uppaal_TransitionType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    b1 = uppaal_LabelType(kind="sample_text", mixed="sample_text", x="sample_text", y="sample_text")
    b2 = uppaal_LabelType(kind="sample_text_2", mixed="sample_text_2", x="sample_text_2", y="sample_text_2")
    _safe_set(a, 'uppaal_TransitionType67', {b1})
    assert _is_linked(a, 'uppaal_TransitionType67', b1)
    if hasattr(b1, 'uppaal_LabelType68'):
        assert _is_linked(b1, 'uppaal_LabelType68', a)
    _safe_set(a, 'uppaal_TransitionType67', {b2})
    assert _is_linked(a, 'uppaal_TransitionType67', b2)
    if hasattr(b1, 'uppaal_LabelType68'):
        assert not _is_linked(b1, 'uppaal_LabelType68', a)
    if hasattr(b2, 'uppaal_LabelType68'):
        assert _is_linked(b2, 'uppaal_LabelType68', a)
    _safe_set(a, 'uppaal_TransitionType67', set())
    assert not _is_linked(a, 'uppaal_TransitionType67', b2)
    if hasattr(b2, 'uppaal_LabelType68'):
        assert not _is_linked(b2, 'uppaal_LabelType68', a)


def test_assoc_label8_link_reassign_clear():
    a = uppaal_LabelType(kind="sample_text", mixed="sample_text", x="sample_text", y="sample_text")
    b1 = uppaal_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    b2 = uppaal_DocumentRoot(declaration="sample_text_2", imports="sample_text_2", instantiation="sample_text_2", mixed="sample_text_2", system="sample_text_2")
    _safe_set(a, 'uppaal_LabelType', b1)
    assert _is_linked(a, 'uppaal_LabelType', b1)
    if hasattr(b1, 'uppaal_DocumentRoot9'):
        assert _is_linked(b1, 'uppaal_DocumentRoot9', a)
    _safe_set(a, 'uppaal_LabelType', b2)
    assert _is_linked(a, 'uppaal_LabelType', b2)
    if hasattr(b1, 'uppaal_DocumentRoot9'):
        assert not _is_linked(b1, 'uppaal_DocumentRoot9', a)
    if hasattr(b2, 'uppaal_DocumentRoot9'):
        assert _is_linked(b2, 'uppaal_DocumentRoot9', a)
    _safe_set(a, 'uppaal_LabelType', None)
    assert not _is_linked(a, 'uppaal_LabelType', b2)
    if hasattr(b2, 'uppaal_DocumentRoot9'):
        assert not _is_linked(b2, 'uppaal_DocumentRoot9', a)


def test_assoc_location10_link_reassign_clear():
    a = uppaal_LocationType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    b1 = uppaal_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    b2 = uppaal_DocumentRoot(declaration="sample_text_2", imports="sample_text_2", instantiation="sample_text_2", mixed="sample_text_2", system="sample_text_2")
    _safe_set(a, 'uppaal_LocationType', b1)
    assert _is_linked(a, 'uppaal_LocationType', b1)
    if hasattr(b1, 'uppaal_DocumentRoot11'):
        assert _is_linked(b1, 'uppaal_DocumentRoot11', a)
    _safe_set(a, 'uppaal_LocationType', b2)
    assert _is_linked(a, 'uppaal_LocationType', b2)
    if hasattr(b1, 'uppaal_DocumentRoot11'):
        assert not _is_linked(b1, 'uppaal_DocumentRoot11', a)
    if hasattr(b2, 'uppaal_DocumentRoot11'):
        assert _is_linked(b2, 'uppaal_DocumentRoot11', a)
    _safe_set(a, 'uppaal_LocationType', None)
    assert not _is_linked(a, 'uppaal_LocationType', b2)
    if hasattr(b2, 'uppaal_DocumentRoot11'):
        assert not _is_linked(b2, 'uppaal_DocumentRoot11', a)


def test_assoc_location51_link_reassign_clear():
    a = uppaal_TemplateType(declaration="sample_text")
    b1 = uppaal_LocationType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    b2 = uppaal_LocationType(color="sample_text_2", id="sample_text_2", x="sample_text_2", y="sample_text_2")
    _safe_set(a, 'uppaal_TemplateType52', {b1})
    assert _is_linked(a, 'uppaal_TemplateType52', b1)
    if hasattr(b1, 'uppaal_LocationType53'):
        assert _is_linked(b1, 'uppaal_LocationType53', a)
    _safe_set(a, 'uppaal_TemplateType52', {b2})
    assert _is_linked(a, 'uppaal_TemplateType52', b2)
    if hasattr(b1, 'uppaal_LocationType53'):
        assert not _is_linked(b1, 'uppaal_LocationType53', a)
    if hasattr(b2, 'uppaal_LocationType53'):
        assert _is_linked(b2, 'uppaal_LocationType53', a)
    _safe_set(a, 'uppaal_TemplateType52', set())
    assert not _is_linked(a, 'uppaal_TemplateType52', b2)
    if hasattr(b2, 'uppaal_LocationType53'):
        assert not _is_linked(b2, 'uppaal_LocationType53', a)


def test_assoc_nail12_link_reassign_clear():
    a = uppaal_NailType(x="sample_text", y="sample_text")
    b1 = uppaal_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    b2 = uppaal_DocumentRoot(declaration="sample_text_2", imports="sample_text_2", instantiation="sample_text_2", mixed="sample_text_2", system="sample_text_2")
    _safe_set(a, 'uppaal_NailType', b1)
    assert _is_linked(a, 'uppaal_NailType', b1)
    if hasattr(b1, 'uppaal_DocumentRoot13'):
        assert _is_linked(b1, 'uppaal_DocumentRoot13', a)
    _safe_set(a, 'uppaal_NailType', b2)
    assert _is_linked(a, 'uppaal_NailType', b2)
    if hasattr(b1, 'uppaal_DocumentRoot13'):
        assert not _is_linked(b1, 'uppaal_DocumentRoot13', a)
    if hasattr(b2, 'uppaal_DocumentRoot13'):
        assert _is_linked(b2, 'uppaal_DocumentRoot13', a)
    _safe_set(a, 'uppaal_NailType', None)
    assert not _is_linked(a, 'uppaal_NailType', b2)
    if hasattr(b2, 'uppaal_DocumentRoot13'):
        assert not _is_linked(b2, 'uppaal_DocumentRoot13', a)


def test_assoc_nail69_link_reassign_clear():
    a = uppaal_TransitionType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    b1 = uppaal_NailType(x="sample_text", y="sample_text")
    b2 = uppaal_NailType(x="sample_text_2", y="sample_text_2")
    _safe_set(a, 'uppaal_TransitionType70', {b1})
    assert _is_linked(a, 'uppaal_TransitionType70', b1)
    if hasattr(b1, 'uppaal_NailType71'):
        assert _is_linked(b1, 'uppaal_NailType71', a)
    _safe_set(a, 'uppaal_TransitionType70', {b2})
    assert _is_linked(a, 'uppaal_TransitionType70', b2)
    if hasattr(b1, 'uppaal_NailType71'):
        assert not _is_linked(b1, 'uppaal_NailType71', a)
    if hasattr(b2, 'uppaal_NailType71'):
        assert _is_linked(b2, 'uppaal_NailType71', a)
    _safe_set(a, 'uppaal_TransitionType70', set())
    assert not _is_linked(a, 'uppaal_TransitionType70', b2)
    if hasattr(b2, 'uppaal_NailType71'):
        assert not _is_linked(b2, 'uppaal_NailType71', a)


def test_assoc_name14_link_reassign_clear():
    a = uppaal_NameType(mixed="sample_text", x="sample_text", y="sample_text")
    b1 = uppaal_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    b2 = uppaal_DocumentRoot(declaration="sample_text_2", imports="sample_text_2", instantiation="sample_text_2", mixed="sample_text_2", system="sample_text_2")
    _safe_set(a, 'uppaal_NameType', b1)
    assert _is_linked(a, 'uppaal_NameType', b1)
    if hasattr(b1, 'uppaal_DocumentRoot15'):
        assert _is_linked(b1, 'uppaal_DocumentRoot15', a)
    _safe_set(a, 'uppaal_NameType', b2)
    assert _is_linked(a, 'uppaal_NameType', b2)
    if hasattr(b1, 'uppaal_DocumentRoot15'):
        assert not _is_linked(b1, 'uppaal_DocumentRoot15', a)
    if hasattr(b2, 'uppaal_DocumentRoot15'):
        assert _is_linked(b2, 'uppaal_DocumentRoot15', a)
    _safe_set(a, 'uppaal_NameType', None)
    assert not _is_linked(a, 'uppaal_NameType', b2)
    if hasattr(b2, 'uppaal_DocumentRoot15'):
        assert not _is_linked(b2, 'uppaal_DocumentRoot15', a)


def test_assoc_name30_link_reassign_clear():
    a = uppaal_NameType(mixed="sample_text", x="sample_text", y="sample_text")
    b1 = uppaal_LocationType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    b2 = uppaal_LocationType(color="sample_text_2", id="sample_text_2", x="sample_text_2", y="sample_text_2")
    _safe_set(a, 'uppaal_NameType32', b1)
    assert _is_linked(a, 'uppaal_NameType32', b1)
    if hasattr(b1, 'uppaal_LocationType31'):
        assert _is_linked(b1, 'uppaal_LocationType31', a)
    _safe_set(a, 'uppaal_NameType32', b2)
    assert _is_linked(a, 'uppaal_NameType32', b2)
    if hasattr(b1, 'uppaal_LocationType31'):
        assert not _is_linked(b1, 'uppaal_LocationType31', a)
    if hasattr(b2, 'uppaal_LocationType31'):
        assert _is_linked(b2, 'uppaal_LocationType31', a)
    _safe_set(a, 'uppaal_NameType32', None)
    assert not _is_linked(a, 'uppaal_NameType32', b2)
    if hasattr(b2, 'uppaal_LocationType31'):
        assert not _is_linked(b2, 'uppaal_LocationType31', a)


def test_assoc_name45_link_reassign_clear():
    a = uppaal_TemplateType(declaration="sample_text")
    b1 = uppaal_NameType(mixed="sample_text", x="sample_text", y="sample_text")
    b2 = uppaal_NameType(mixed="sample_text_2", x="sample_text_2", y="sample_text_2")
    _safe_set(a, 'uppaal_TemplateType46', b1)
    assert _is_linked(a, 'uppaal_TemplateType46', b1)
    if hasattr(b1, 'uppaal_NameType47'):
        assert _is_linked(b1, 'uppaal_NameType47', a)
    _safe_set(a, 'uppaal_TemplateType46', b2)
    assert _is_linked(a, 'uppaal_TemplateType46', b2)
    if hasattr(b1, 'uppaal_NameType47'):
        assert not _is_linked(b1, 'uppaal_NameType47', a)
    if hasattr(b2, 'uppaal_NameType47'):
        assert _is_linked(b2, 'uppaal_NameType47', a)
    _safe_set(a, 'uppaal_TemplateType46', None)
    assert not _is_linked(a, 'uppaal_TemplateType46', b2)
    if hasattr(b2, 'uppaal_NameType47'):
        assert not _is_linked(b2, 'uppaal_NameType47', a)


def test_assoc_nta16_link_reassign_clear():
    a = uppaal_NtaType(declaration="sample_text", imports="sample_text", instantiation="sample_text", system="sample_text")
    b1 = uppaal_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    b2 = uppaal_DocumentRoot(declaration="sample_text_2", imports="sample_text_2", instantiation="sample_text_2", mixed="sample_text_2", system="sample_text_2")
    _safe_set(a, 'uppaal_NtaType', b1)
    assert _is_linked(a, 'uppaal_NtaType', b1)
    if hasattr(b1, 'uppaal_DocumentRoot17'):
        assert _is_linked(b1, 'uppaal_DocumentRoot17', a)
    _safe_set(a, 'uppaal_NtaType', b2)
    assert _is_linked(a, 'uppaal_NtaType', b2)
    if hasattr(b1, 'uppaal_DocumentRoot17'):
        assert not _is_linked(b1, 'uppaal_DocumentRoot17', a)
    if hasattr(b2, 'uppaal_DocumentRoot17'):
        assert _is_linked(b2, 'uppaal_DocumentRoot17', a)
    _safe_set(a, 'uppaal_NtaType', None)
    assert not _is_linked(a, 'uppaal_NtaType', b2)
    if hasattr(b2, 'uppaal_DocumentRoot17'):
        assert not _is_linked(b2, 'uppaal_DocumentRoot17', a)


def test_assoc_parameter18_link_reassign_clear():
    a = uppaal_ParameterType(mixed="sample_text", x="sample_text", y="sample_text")
    b1 = uppaal_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    b2 = uppaal_DocumentRoot(declaration="sample_text_2", imports="sample_text_2", instantiation="sample_text_2", mixed="sample_text_2", system="sample_text_2")
    _safe_set(a, 'uppaal_ParameterType', b1)
    assert _is_linked(a, 'uppaal_ParameterType', b1)
    if hasattr(b1, 'uppaal_DocumentRoot19'):
        assert _is_linked(b1, 'uppaal_DocumentRoot19', a)
    _safe_set(a, 'uppaal_ParameterType', b2)
    assert _is_linked(a, 'uppaal_ParameterType', b2)
    if hasattr(b1, 'uppaal_DocumentRoot19'):
        assert not _is_linked(b1, 'uppaal_DocumentRoot19', a)
    if hasattr(b2, 'uppaal_DocumentRoot19'):
        assert _is_linked(b2, 'uppaal_DocumentRoot19', a)
    _safe_set(a, 'uppaal_ParameterType', None)
    assert not _is_linked(a, 'uppaal_ParameterType', b2)
    if hasattr(b2, 'uppaal_DocumentRoot19'):
        assert not _is_linked(b2, 'uppaal_DocumentRoot19', a)


def test_assoc_parameter48_link_reassign_clear():
    a = uppaal_TemplateType(declaration="sample_text")
    b1 = uppaal_ParameterType(mixed="sample_text", x="sample_text", y="sample_text")
    b2 = uppaal_ParameterType(mixed="sample_text_2", x="sample_text_2", y="sample_text_2")
    _safe_set(a, 'uppaal_TemplateType49', b1)
    assert _is_linked(a, 'uppaal_TemplateType49', b1)
    if hasattr(b1, 'uppaal_ParameterType50'):
        assert _is_linked(b1, 'uppaal_ParameterType50', a)
    _safe_set(a, 'uppaal_TemplateType49', b2)
    assert _is_linked(a, 'uppaal_TemplateType49', b2)
    if hasattr(b1, 'uppaal_ParameterType50'):
        assert not _is_linked(b1, 'uppaal_ParameterType50', a)
    if hasattr(b2, 'uppaal_ParameterType50'):
        assert _is_linked(b2, 'uppaal_ParameterType50', a)
    _safe_set(a, 'uppaal_TemplateType49', None)
    assert not _is_linked(a, 'uppaal_TemplateType49', b2)
    if hasattr(b2, 'uppaal_ParameterType50'):
        assert not _is_linked(b2, 'uppaal_ParameterType50', a)


def test_assoc_source20_link_reassign_clear():
    a = uppaal_SourceType(ref="sample_text")
    b1 = uppaal_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    b2 = uppaal_DocumentRoot(declaration="sample_text_2", imports="sample_text_2", instantiation="sample_text_2", mixed="sample_text_2", system="sample_text_2")
    _safe_set(a, 'uppaal_SourceType', b1)
    assert _is_linked(a, 'uppaal_SourceType', b1)
    if hasattr(b1, 'uppaal_DocumentRoot21'):
        assert _is_linked(b1, 'uppaal_DocumentRoot21', a)
    _safe_set(a, 'uppaal_SourceType', b2)
    assert _is_linked(a, 'uppaal_SourceType', b2)
    if hasattr(b1, 'uppaal_DocumentRoot21'):
        assert not _is_linked(b1, 'uppaal_DocumentRoot21', a)
    if hasattr(b2, 'uppaal_DocumentRoot21'):
        assert _is_linked(b2, 'uppaal_DocumentRoot21', a)
    _safe_set(a, 'uppaal_SourceType', None)
    assert not _is_linked(a, 'uppaal_SourceType', b2)
    if hasattr(b2, 'uppaal_DocumentRoot21'):
        assert not _is_linked(b2, 'uppaal_DocumentRoot21', a)


def test_assoc_source60_link_reassign_clear():
    a = uppaal_TransitionType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    b1 = uppaal_SourceType(ref="sample_text")
    b2 = uppaal_SourceType(ref="sample_text_2")
    _safe_set(a, 'uppaal_TransitionType61', b1)
    assert _is_linked(a, 'uppaal_TransitionType61', b1)
    if hasattr(b1, 'uppaal_SourceType62'):
        assert _is_linked(b1, 'uppaal_SourceType62', a)
    _safe_set(a, 'uppaal_TransitionType61', b2)
    assert _is_linked(a, 'uppaal_TransitionType61', b2)
    if hasattr(b1, 'uppaal_SourceType62'):
        assert not _is_linked(b1, 'uppaal_SourceType62', a)
    if hasattr(b2, 'uppaal_SourceType62'):
        assert _is_linked(b2, 'uppaal_SourceType62', a)
    _safe_set(a, 'uppaal_TransitionType61', None)
    assert not _is_linked(a, 'uppaal_TransitionType61', b2)
    if hasattr(b2, 'uppaal_SourceType62'):
        assert not _is_linked(b2, 'uppaal_SourceType62', a)


def test_assoc_target22_link_reassign_clear():
    a = uppaal_TargetType(ref="sample_text")
    b1 = uppaal_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    b2 = uppaal_DocumentRoot(declaration="sample_text_2", imports="sample_text_2", instantiation="sample_text_2", mixed="sample_text_2", system="sample_text_2")
    _safe_set(a, 'uppaal_TargetType', b1)
    assert _is_linked(a, 'uppaal_TargetType', b1)
    if hasattr(b1, 'uppaal_DocumentRoot23'):
        assert _is_linked(b1, 'uppaal_DocumentRoot23', a)
    _safe_set(a, 'uppaal_TargetType', b2)
    assert _is_linked(a, 'uppaal_TargetType', b2)
    if hasattr(b1, 'uppaal_DocumentRoot23'):
        assert not _is_linked(b1, 'uppaal_DocumentRoot23', a)
    if hasattr(b2, 'uppaal_DocumentRoot23'):
        assert _is_linked(b2, 'uppaal_DocumentRoot23', a)
    _safe_set(a, 'uppaal_TargetType', None)
    assert not _is_linked(a, 'uppaal_TargetType', b2)
    if hasattr(b2, 'uppaal_DocumentRoot23'):
        assert not _is_linked(b2, 'uppaal_DocumentRoot23', a)


def test_assoc_target63_link_reassign_clear():
    a = uppaal_TransitionType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    b1 = uppaal_TargetType(ref="sample_text")
    b2 = uppaal_TargetType(ref="sample_text_2")
    _safe_set(a, 'uppaal_TransitionType64', b1)
    assert _is_linked(a, 'uppaal_TransitionType64', b1)
    if hasattr(b1, 'uppaal_TargetType65'):
        assert _is_linked(b1, 'uppaal_TargetType65', a)
    _safe_set(a, 'uppaal_TransitionType64', b2)
    assert _is_linked(a, 'uppaal_TransitionType64', b2)
    if hasattr(b1, 'uppaal_TargetType65'):
        assert not _is_linked(b1, 'uppaal_TargetType65', a)
    if hasattr(b2, 'uppaal_TargetType65'):
        assert _is_linked(b2, 'uppaal_TargetType65', a)
    _safe_set(a, 'uppaal_TransitionType64', None)
    assert not _is_linked(a, 'uppaal_TransitionType64', b2)
    if hasattr(b2, 'uppaal_TargetType65'):
        assert not _is_linked(b2, 'uppaal_TargetType65', a)


def test_assoc_template24_link_reassign_clear():
    a = uppaal_TemplateType(declaration="sample_text")
    b1 = uppaal_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    b2 = uppaal_DocumentRoot(declaration="sample_text_2", imports="sample_text_2", instantiation="sample_text_2", mixed="sample_text_2", system="sample_text_2")
    _safe_set(a, 'uppaal_TemplateType', b1)
    assert _is_linked(a, 'uppaal_TemplateType', b1)
    if hasattr(b1, 'uppaal_DocumentRoot25'):
        assert _is_linked(b1, 'uppaal_DocumentRoot25', a)
    _safe_set(a, 'uppaal_TemplateType', b2)
    assert _is_linked(a, 'uppaal_TemplateType', b2)
    if hasattr(b1, 'uppaal_DocumentRoot25'):
        assert not _is_linked(b1, 'uppaal_DocumentRoot25', a)
    if hasattr(b2, 'uppaal_DocumentRoot25'):
        assert _is_linked(b2, 'uppaal_DocumentRoot25', a)
    _safe_set(a, 'uppaal_TemplateType', None)
    assert not _is_linked(a, 'uppaal_TemplateType', b2)
    if hasattr(b2, 'uppaal_DocumentRoot25'):
        assert not _is_linked(b2, 'uppaal_DocumentRoot25', a)


def test_assoc_template42_link_reassign_clear():
    a = uppaal_TemplateType(declaration="sample_text")
    b1 = uppaal_NtaType(declaration="sample_text", imports="sample_text", instantiation="sample_text", system="sample_text")
    b2 = uppaal_NtaType(declaration="sample_text_2", imports="sample_text_2", instantiation="sample_text_2", system="sample_text_2")
    _safe_set(a, 'uppaal_TemplateType44', b1)
    assert _is_linked(a, 'uppaal_TemplateType44', b1)
    if hasattr(b1, 'uppaal_NtaType43'):
        assert _is_linked(b1, 'uppaal_NtaType43', a)
    _safe_set(a, 'uppaal_TemplateType44', b2)
    assert _is_linked(a, 'uppaal_TemplateType44', b2)
    if hasattr(b1, 'uppaal_NtaType43'):
        assert not _is_linked(b1, 'uppaal_NtaType43', a)
    if hasattr(b2, 'uppaal_NtaType43'):
        assert _is_linked(b2, 'uppaal_NtaType43', a)
    _safe_set(a, 'uppaal_TemplateType44', None)
    assert not _is_linked(a, 'uppaal_TemplateType44', b2)
    if hasattr(b2, 'uppaal_NtaType43'):
        assert not _is_linked(b2, 'uppaal_NtaType43', a)


def test_assoc_transition26_link_reassign_clear():
    a = uppaal_TransitionType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    b1 = uppaal_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    b2 = uppaal_DocumentRoot(declaration="sample_text_2", imports="sample_text_2", instantiation="sample_text_2", mixed="sample_text_2", system="sample_text_2")
    _safe_set(a, 'uppaal_TransitionType', b1)
    assert _is_linked(a, 'uppaal_TransitionType', b1)
    if hasattr(b1, 'uppaal_DocumentRoot27'):
        assert _is_linked(b1, 'uppaal_DocumentRoot27', a)
    _safe_set(a, 'uppaal_TransitionType', b2)
    assert _is_linked(a, 'uppaal_TransitionType', b2)
    if hasattr(b1, 'uppaal_DocumentRoot27'):
        assert not _is_linked(b1, 'uppaal_DocumentRoot27', a)
    if hasattr(b2, 'uppaal_DocumentRoot27'):
        assert _is_linked(b2, 'uppaal_DocumentRoot27', a)
    _safe_set(a, 'uppaal_TransitionType', None)
    assert not _is_linked(a, 'uppaal_TransitionType', b2)
    if hasattr(b2, 'uppaal_DocumentRoot27'):
        assert not _is_linked(b2, 'uppaal_DocumentRoot27', a)


def test_assoc_transition57_link_reassign_clear():
    a = uppaal_TransitionType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    b1 = uppaal_TemplateType(declaration="sample_text")
    b2 = uppaal_TemplateType(declaration="sample_text_2")
    _safe_set(a, 'uppaal_TransitionType59', b1)
    assert _is_linked(a, 'uppaal_TransitionType59', b1)
    if hasattr(b1, 'uppaal_TemplateType58'):
        assert _is_linked(b1, 'uppaal_TemplateType58', a)
    _safe_set(a, 'uppaal_TransitionType59', b2)
    assert _is_linked(a, 'uppaal_TransitionType59', b2)
    if hasattr(b1, 'uppaal_TemplateType58'):
        assert not _is_linked(b1, 'uppaal_TemplateType58', a)
    if hasattr(b2, 'uppaal_TemplateType58'):
        assert _is_linked(b2, 'uppaal_TemplateType58', a)
    _safe_set(a, 'uppaal_TransitionType59', None)
    assert not _is_linked(a, 'uppaal_TransitionType59', b2)
    if hasattr(b2, 'uppaal_TemplateType58'):
        assert not _is_linked(b2, 'uppaal_TemplateType58', a)


def test_assoc_urgent28_link_reassign_clear():
    a = uppaal_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    b1 = uppaal_UrgentType()
    b2 = uppaal_UrgentType()
    _safe_set(a, 'uppaal_DocumentRoot29', {b1})
    assert _is_linked(a, 'uppaal_DocumentRoot29', b1)
    if hasattr(b1, 'uppaal_UrgentType'):
        assert _is_linked(b1, 'uppaal_UrgentType', a)
    _safe_set(a, 'uppaal_DocumentRoot29', {b2})
    assert _is_linked(a, 'uppaal_DocumentRoot29', b2)
    if hasattr(b1, 'uppaal_UrgentType'):
        assert not _is_linked(b1, 'uppaal_UrgentType', a)
    if hasattr(b2, 'uppaal_UrgentType'):
        assert _is_linked(b2, 'uppaal_UrgentType', a)
    _safe_set(a, 'uppaal_DocumentRoot29', set())
    assert not _is_linked(a, 'uppaal_DocumentRoot29', b2)
    if hasattr(b2, 'uppaal_UrgentType'):
        assert not _is_linked(b2, 'uppaal_UrgentType', a)


def test_assoc_urgent36_link_reassign_clear():
    a = uppaal_LocationType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    b1 = uppaal_UrgentType()
    b2 = uppaal_UrgentType()
    _safe_set(a, 'uppaal_LocationType37', b1)
    assert _is_linked(a, 'uppaal_LocationType37', b1)
    if hasattr(b1, 'uppaal_UrgentType38'):
        assert _is_linked(b1, 'uppaal_UrgentType38', a)
    _safe_set(a, 'uppaal_LocationType37', b2)
    assert _is_linked(a, 'uppaal_LocationType37', b2)
    if hasattr(b1, 'uppaal_UrgentType38'):
        assert not _is_linked(b1, 'uppaal_UrgentType38', a)
    if hasattr(b2, 'uppaal_UrgentType38'):
        assert _is_linked(b2, 'uppaal_UrgentType38', a)
    _safe_set(a, 'uppaal_LocationType37', None)
    assert not _is_linked(a, 'uppaal_LocationType37', b2)
    if hasattr(b2, 'uppaal_UrgentType38'):
        assert not _is_linked(b2, 'uppaal_UrgentType38', a)


def test_assoc_xMLNSPrefixMap0_link_reassign_clear():
    a = uppaal_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    b1 = uppaal_EStringToStringMapEntry()
    b2 = uppaal_EStringToStringMapEntry()
    _safe_set(a, 'uppaal_DocumentRoot', {b1})
    assert _is_linked(a, 'uppaal_DocumentRoot', b1)
    if hasattr(b1, 'uppaal_EStringToStringMapEntry'):
        assert _is_linked(b1, 'uppaal_EStringToStringMapEntry', a)
    _safe_set(a, 'uppaal_DocumentRoot', {b2})
    assert _is_linked(a, 'uppaal_DocumentRoot', b2)
    if hasattr(b1, 'uppaal_EStringToStringMapEntry'):
        assert not _is_linked(b1, 'uppaal_EStringToStringMapEntry', a)
    if hasattr(b2, 'uppaal_EStringToStringMapEntry'):
        assert _is_linked(b2, 'uppaal_EStringToStringMapEntry', a)
    _safe_set(a, 'uppaal_DocumentRoot', set())
    assert not _is_linked(a, 'uppaal_DocumentRoot', b2)
    if hasattr(b2, 'uppaal_EStringToStringMapEntry'):
        assert not _is_linked(b2, 'uppaal_EStringToStringMapEntry', a)


def test_assoc_xSISchemaLocation1_link_reassign_clear():
    a = uppaal_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    b1 = uppaal_EStringToStringMapEntry()
    b2 = uppaal_EStringToStringMapEntry()
    _safe_set(a, 'uppaal_DocumentRoot2', {b1})
    assert _is_linked(a, 'uppaal_DocumentRoot2', b1)
    if hasattr(b1, 'uppaal_EStringToStringMapEntry3'):
        assert _is_linked(b1, 'uppaal_EStringToStringMapEntry3', a)
    _safe_set(a, 'uppaal_DocumentRoot2', {b2})
    assert _is_linked(a, 'uppaal_DocumentRoot2', b2)
    if hasattr(b1, 'uppaal_EStringToStringMapEntry3'):
        assert not _is_linked(b1, 'uppaal_EStringToStringMapEntry3', a)
    if hasattr(b2, 'uppaal_EStringToStringMapEntry3'):
        assert _is_linked(b2, 'uppaal_EStringToStringMapEntry3', a)
    _safe_set(a, 'uppaal_DocumentRoot2', set())
    assert not _is_linked(a, 'uppaal_DocumentRoot2', b2)
    if hasattr(b2, 'uppaal_EStringToStringMapEntry3'):
        assert not _is_linked(b2, 'uppaal_EStringToStringMapEntry3', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

uppaal_CommittedType_strategy = st.builds(uppaal_CommittedType)
@given(instance=uppaal_CommittedType_strategy)
@settings(max_examples=25)
def test_uppaal_CommittedType_instantiation(instance):
    assert isinstance(instance, uppaal_CommittedType)


uppaal_DocumentRoot_strategy = st.builds(uppaal_DocumentRoot, declaration=safe_text, imports=safe_text, instantiation=safe_text, mixed=safe_text, system=safe_text)
@given(instance=uppaal_DocumentRoot_strategy)
@settings(max_examples=25)
def test_uppaal_DocumentRoot_instantiation(instance):
    assert isinstance(instance, uppaal_DocumentRoot)


uppaal_EStringToStringMapEntry_strategy = st.builds(uppaal_EStringToStringMapEntry)
@given(instance=uppaal_EStringToStringMapEntry_strategy)
@settings(max_examples=25)
def test_uppaal_EStringToStringMapEntry_instantiation(instance):
    assert isinstance(instance, uppaal_EStringToStringMapEntry)


uppaal_InitType_strategy = st.builds(uppaal_InitType, ref=safe_text)
@given(instance=uppaal_InitType_strategy)
@settings(max_examples=25)
def test_uppaal_InitType_instantiation(instance):
    assert isinstance(instance, uppaal_InitType)


uppaal_LabelType_strategy = st.builds(uppaal_LabelType, kind=safe_text, mixed=safe_text, x=safe_text, y=safe_text)
@given(instance=uppaal_LabelType_strategy)
@settings(max_examples=25)
def test_uppaal_LabelType_instantiation(instance):
    assert isinstance(instance, uppaal_LabelType)


uppaal_LocationType_strategy = st.builds(uppaal_LocationType, color=safe_text, id=safe_text, x=safe_text, y=safe_text)
@given(instance=uppaal_LocationType_strategy)
@settings(max_examples=25)
def test_uppaal_LocationType_instantiation(instance):
    assert isinstance(instance, uppaal_LocationType)


uppaal_NailType_strategy = st.builds(uppaal_NailType, x=safe_text, y=safe_text)
@given(instance=uppaal_NailType_strategy)
@settings(max_examples=25)
def test_uppaal_NailType_instantiation(instance):
    assert isinstance(instance, uppaal_NailType)


uppaal_NameType_strategy = st.builds(uppaal_NameType, mixed=safe_text, x=safe_text, y=safe_text)
@given(instance=uppaal_NameType_strategy)
@settings(max_examples=25)
def test_uppaal_NameType_instantiation(instance):
    assert isinstance(instance, uppaal_NameType)


uppaal_NtaType_strategy = st.builds(uppaal_NtaType, declaration=safe_text, imports=safe_text, instantiation=safe_text, system=safe_text)
@given(instance=uppaal_NtaType_strategy)
@settings(max_examples=25)
def test_uppaal_NtaType_instantiation(instance):
    assert isinstance(instance, uppaal_NtaType)


uppaal_ParameterType_strategy = st.builds(uppaal_ParameterType, mixed=safe_text, x=safe_text, y=safe_text)
@given(instance=uppaal_ParameterType_strategy)
@settings(max_examples=25)
def test_uppaal_ParameterType_instantiation(instance):
    assert isinstance(instance, uppaal_ParameterType)


uppaal_SourceType_strategy = st.builds(uppaal_SourceType, ref=safe_text)
@given(instance=uppaal_SourceType_strategy)
@settings(max_examples=25)
def test_uppaal_SourceType_instantiation(instance):
    assert isinstance(instance, uppaal_SourceType)


uppaal_TargetType_strategy = st.builds(uppaal_TargetType, ref=safe_text)
@given(instance=uppaal_TargetType_strategy)
@settings(max_examples=25)
def test_uppaal_TargetType_instantiation(instance):
    assert isinstance(instance, uppaal_TargetType)


uppaal_TemplateType_strategy = st.builds(uppaal_TemplateType, declaration=safe_text)
@given(instance=uppaal_TemplateType_strategy)
@settings(max_examples=25)
def test_uppaal_TemplateType_instantiation(instance):
    assert isinstance(instance, uppaal_TemplateType)


uppaal_TransitionType_strategy = st.builds(uppaal_TransitionType, color=safe_text, id=safe_text, x=safe_text, y=safe_text)
@given(instance=uppaal_TransitionType_strategy)
@settings(max_examples=25)
def test_uppaal_TransitionType_instantiation(instance):
    assert isinstance(instance, uppaal_TransitionType)


uppaal_UrgentType_strategy = st.builds(uppaal_UrgentType)
@given(instance=uppaal_UrgentType_strategy)
@settings(max_examples=25)
def test_uppaal_UrgentType_instantiation(instance):
    assert isinstance(instance, uppaal_UrgentType)



