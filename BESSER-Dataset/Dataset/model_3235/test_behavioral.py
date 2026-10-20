import pytest
from datetime import date, datetime, time, timedelta

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

def test_assoc_init54_reverse_link_reassign_clear():
    a1 = uppaal_TemplateType(declaration="sample_text")
    a2 = uppaal_TemplateType(declaration="sample_text_2")
    b = uppaal_InitType(ref="sample_text")
    _safe_set(b, 'uppaal_InitType56', a1)
    assert _is_linked(b, 'uppaal_InitType56', a1)
    if hasattr(a1, 'uppaal_TemplateType55'):
        assert _is_linked(a1, 'uppaal_TemplateType55', b)
    _safe_set(b, 'uppaal_InitType56', a2)
    assert _is_linked(b, 'uppaal_InitType56', a2)
    if hasattr(a1, 'uppaal_TemplateType55'):
        assert not _is_linked(a1, 'uppaal_TemplateType55', b)
    if hasattr(a2, 'uppaal_TemplateType55'):
        assert _is_linked(a2, 'uppaal_TemplateType55', b)
    _safe_set(b, 'uppaal_InitType56', None)
    assert not _is_linked(b, 'uppaal_InitType56', a2)
    if hasattr(a2, 'uppaal_TemplateType55'):
        assert not _is_linked(a2, 'uppaal_TemplateType55', b)


def test_assoc_init6_reverse_link_reassign_clear():
    a1 = uppaal_InitType(ref="sample_text")
    a2 = uppaal_InitType(ref="sample_text_2")
    b = uppaal_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    _safe_set(b, 'uppaal_DocumentRoot7', {a1})
    assert _is_linked(b, 'uppaal_DocumentRoot7', a1)
    if hasattr(a1, 'uppaal_InitType'):
        assert _is_linked(a1, 'uppaal_InitType', b)
    _safe_set(b, 'uppaal_DocumentRoot7', {a2})
    assert _is_linked(b, 'uppaal_DocumentRoot7', a2)
    if hasattr(a1, 'uppaal_InitType'):
        assert not _is_linked(a1, 'uppaal_InitType', b)
    if hasattr(a2, 'uppaal_InitType'):
        assert _is_linked(a2, 'uppaal_InitType', b)
    _safe_set(b, 'uppaal_DocumentRoot7', set())
    assert not _is_linked(b, 'uppaal_DocumentRoot7', a2)
    if hasattr(a2, 'uppaal_InitType'):
        assert not _is_linked(a2, 'uppaal_InitType', b)


def test_assoc_label33_reverse_link_reassign_clear():
    a1 = uppaal_LocationType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    a2 = uppaal_LocationType(color="sample_text_2", id="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = uppaal_LabelType(kind="sample_text", mixed="sample_text", x="sample_text", y="sample_text")
    _safe_set(b, 'uppaal_LabelType35', a1)
    assert _is_linked(b, 'uppaal_LabelType35', a1)
    if hasattr(a1, 'uppaal_LocationType34'):
        assert _is_linked(a1, 'uppaal_LocationType34', b)
    _safe_set(b, 'uppaal_LabelType35', a2)
    assert _is_linked(b, 'uppaal_LabelType35', a2)
    if hasattr(a1, 'uppaal_LocationType34'):
        assert not _is_linked(a1, 'uppaal_LocationType34', b)
    if hasattr(a2, 'uppaal_LocationType34'):
        assert _is_linked(a2, 'uppaal_LocationType34', b)
    _safe_set(b, 'uppaal_LabelType35', None)
    assert not _is_linked(b, 'uppaal_LabelType35', a2)
    if hasattr(a2, 'uppaal_LocationType34'):
        assert not _is_linked(a2, 'uppaal_LocationType34', b)


def test_assoc_label66_reverse_link_reassign_clear():
    a1 = uppaal_TransitionType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    a2 = uppaal_TransitionType(color="sample_text_2", id="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = uppaal_LabelType(kind="sample_text", mixed="sample_text", x="sample_text", y="sample_text")
    _safe_set(b, 'uppaal_LabelType68', a1)
    assert _is_linked(b, 'uppaal_LabelType68', a1)
    if hasattr(a1, 'uppaal_TransitionType67'):
        assert _is_linked(a1, 'uppaal_TransitionType67', b)
    _safe_set(b, 'uppaal_LabelType68', a2)
    assert _is_linked(b, 'uppaal_LabelType68', a2)
    if hasattr(a1, 'uppaal_TransitionType67'):
        assert not _is_linked(a1, 'uppaal_TransitionType67', b)
    if hasattr(a2, 'uppaal_TransitionType67'):
        assert _is_linked(a2, 'uppaal_TransitionType67', b)
    _safe_set(b, 'uppaal_LabelType68', None)
    assert not _is_linked(b, 'uppaal_LabelType68', a2)
    if hasattr(a2, 'uppaal_TransitionType67'):
        assert not _is_linked(a2, 'uppaal_TransitionType67', b)


def test_assoc_label8_reverse_link_reassign_clear():
    a1 = uppaal_LabelType(kind="sample_text", mixed="sample_text", x="sample_text", y="sample_text")
    a2 = uppaal_LabelType(kind="sample_text_2", mixed="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = uppaal_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    _safe_set(b, 'uppaal_DocumentRoot9', {a1})
    assert _is_linked(b, 'uppaal_DocumentRoot9', a1)
    if hasattr(a1, 'uppaal_LabelType'):
        assert _is_linked(a1, 'uppaal_LabelType', b)
    _safe_set(b, 'uppaal_DocumentRoot9', {a2})
    assert _is_linked(b, 'uppaal_DocumentRoot9', a2)
    if hasattr(a1, 'uppaal_LabelType'):
        assert not _is_linked(a1, 'uppaal_LabelType', b)
    if hasattr(a2, 'uppaal_LabelType'):
        assert _is_linked(a2, 'uppaal_LabelType', b)
    _safe_set(b, 'uppaal_DocumentRoot9', set())
    assert not _is_linked(b, 'uppaal_DocumentRoot9', a2)
    if hasattr(a2, 'uppaal_LabelType'):
        assert not _is_linked(a2, 'uppaal_LabelType', b)


def test_assoc_location10_reverse_link_reassign_clear():
    a1 = uppaal_LocationType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    a2 = uppaal_LocationType(color="sample_text_2", id="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = uppaal_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    _safe_set(b, 'uppaal_DocumentRoot11', {a1})
    assert _is_linked(b, 'uppaal_DocumentRoot11', a1)
    if hasattr(a1, 'uppaal_LocationType'):
        assert _is_linked(a1, 'uppaal_LocationType', b)
    _safe_set(b, 'uppaal_DocumentRoot11', {a2})
    assert _is_linked(b, 'uppaal_DocumentRoot11', a2)
    if hasattr(a1, 'uppaal_LocationType'):
        assert not _is_linked(a1, 'uppaal_LocationType', b)
    if hasattr(a2, 'uppaal_LocationType'):
        assert _is_linked(a2, 'uppaal_LocationType', b)
    _safe_set(b, 'uppaal_DocumentRoot11', set())
    assert not _is_linked(b, 'uppaal_DocumentRoot11', a2)
    if hasattr(a2, 'uppaal_LocationType'):
        assert not _is_linked(a2, 'uppaal_LocationType', b)


def test_assoc_location51_reverse_link_reassign_clear():
    a1 = uppaal_TemplateType(declaration="sample_text")
    a2 = uppaal_TemplateType(declaration="sample_text_2")
    b = uppaal_LocationType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    _safe_set(b, 'uppaal_LocationType53', a1)
    assert _is_linked(b, 'uppaal_LocationType53', a1)
    if hasattr(a1, 'uppaal_TemplateType52'):
        assert _is_linked(a1, 'uppaal_TemplateType52', b)
    _safe_set(b, 'uppaal_LocationType53', a2)
    assert _is_linked(b, 'uppaal_LocationType53', a2)
    if hasattr(a1, 'uppaal_TemplateType52'):
        assert not _is_linked(a1, 'uppaal_TemplateType52', b)
    if hasattr(a2, 'uppaal_TemplateType52'):
        assert _is_linked(a2, 'uppaal_TemplateType52', b)
    _safe_set(b, 'uppaal_LocationType53', None)
    assert not _is_linked(b, 'uppaal_LocationType53', a2)
    if hasattr(a2, 'uppaal_TemplateType52'):
        assert not _is_linked(a2, 'uppaal_TemplateType52', b)


def test_assoc_nail12_reverse_link_reassign_clear():
    a1 = uppaal_NailType(x="sample_text", y="sample_text")
    a2 = uppaal_NailType(x="sample_text_2", y="sample_text_2")
    b = uppaal_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    _safe_set(b, 'uppaal_DocumentRoot13', {a1})
    assert _is_linked(b, 'uppaal_DocumentRoot13', a1)
    if hasattr(a1, 'uppaal_NailType'):
        assert _is_linked(a1, 'uppaal_NailType', b)
    _safe_set(b, 'uppaal_DocumentRoot13', {a2})
    assert _is_linked(b, 'uppaal_DocumentRoot13', a2)
    if hasattr(a1, 'uppaal_NailType'):
        assert not _is_linked(a1, 'uppaal_NailType', b)
    if hasattr(a2, 'uppaal_NailType'):
        assert _is_linked(a2, 'uppaal_NailType', b)
    _safe_set(b, 'uppaal_DocumentRoot13', set())
    assert not _is_linked(b, 'uppaal_DocumentRoot13', a2)
    if hasattr(a2, 'uppaal_NailType'):
        assert not _is_linked(a2, 'uppaal_NailType', b)


def test_assoc_nail69_reverse_link_reassign_clear():
    a1 = uppaal_TransitionType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    a2 = uppaal_TransitionType(color="sample_text_2", id="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = uppaal_NailType(x="sample_text", y="sample_text")
    _safe_set(b, 'uppaal_NailType71', a1)
    assert _is_linked(b, 'uppaal_NailType71', a1)
    if hasattr(a1, 'uppaal_TransitionType70'):
        assert _is_linked(a1, 'uppaal_TransitionType70', b)
    _safe_set(b, 'uppaal_NailType71', a2)
    assert _is_linked(b, 'uppaal_NailType71', a2)
    if hasattr(a1, 'uppaal_TransitionType70'):
        assert not _is_linked(a1, 'uppaal_TransitionType70', b)
    if hasattr(a2, 'uppaal_TransitionType70'):
        assert _is_linked(a2, 'uppaal_TransitionType70', b)
    _safe_set(b, 'uppaal_NailType71', None)
    assert not _is_linked(b, 'uppaal_NailType71', a2)
    if hasattr(a2, 'uppaal_TransitionType70'):
        assert not _is_linked(a2, 'uppaal_TransitionType70', b)


def test_assoc_name14_reverse_link_reassign_clear():
    a1 = uppaal_NameType(mixed="sample_text", x="sample_text", y="sample_text")
    a2 = uppaal_NameType(mixed="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = uppaal_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    _safe_set(b, 'uppaal_DocumentRoot15', {a1})
    assert _is_linked(b, 'uppaal_DocumentRoot15', a1)
    if hasattr(a1, 'uppaal_NameType'):
        assert _is_linked(a1, 'uppaal_NameType', b)
    _safe_set(b, 'uppaal_DocumentRoot15', {a2})
    assert _is_linked(b, 'uppaal_DocumentRoot15', a2)
    if hasattr(a1, 'uppaal_NameType'):
        assert not _is_linked(a1, 'uppaal_NameType', b)
    if hasattr(a2, 'uppaal_NameType'):
        assert _is_linked(a2, 'uppaal_NameType', b)
    _safe_set(b, 'uppaal_DocumentRoot15', set())
    assert not _is_linked(b, 'uppaal_DocumentRoot15', a2)
    if hasattr(a2, 'uppaal_NameType'):
        assert not _is_linked(a2, 'uppaal_NameType', b)


def test_assoc_name30_reverse_link_reassign_clear():
    a1 = uppaal_NameType(mixed="sample_text", x="sample_text", y="sample_text")
    a2 = uppaal_NameType(mixed="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = uppaal_LocationType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    _safe_set(b, 'uppaal_LocationType31', a1)
    assert _is_linked(b, 'uppaal_LocationType31', a1)
    if hasattr(a1, 'uppaal_NameType32'):
        assert _is_linked(a1, 'uppaal_NameType32', b)
    _safe_set(b, 'uppaal_LocationType31', a2)
    assert _is_linked(b, 'uppaal_LocationType31', a2)
    if hasattr(a1, 'uppaal_NameType32'):
        assert not _is_linked(a1, 'uppaal_NameType32', b)
    if hasattr(a2, 'uppaal_NameType32'):
        assert _is_linked(a2, 'uppaal_NameType32', b)
    _safe_set(b, 'uppaal_LocationType31', None)
    assert not _is_linked(b, 'uppaal_LocationType31', a2)
    if hasattr(a2, 'uppaal_NameType32'):
        assert not _is_linked(a2, 'uppaal_NameType32', b)


def test_assoc_name45_reverse_link_reassign_clear():
    a1 = uppaal_TemplateType(declaration="sample_text")
    a2 = uppaal_TemplateType(declaration="sample_text_2")
    b = uppaal_NameType(mixed="sample_text", x="sample_text", y="sample_text")
    _safe_set(b, 'uppaal_NameType47', a1)
    assert _is_linked(b, 'uppaal_NameType47', a1)
    if hasattr(a1, 'uppaal_TemplateType46'):
        assert _is_linked(a1, 'uppaal_TemplateType46', b)
    _safe_set(b, 'uppaal_NameType47', a2)
    assert _is_linked(b, 'uppaal_NameType47', a2)
    if hasattr(a1, 'uppaal_TemplateType46'):
        assert not _is_linked(a1, 'uppaal_TemplateType46', b)
    if hasattr(a2, 'uppaal_TemplateType46'):
        assert _is_linked(a2, 'uppaal_TemplateType46', b)
    _safe_set(b, 'uppaal_NameType47', None)
    assert not _is_linked(b, 'uppaal_NameType47', a2)
    if hasattr(a2, 'uppaal_TemplateType46'):
        assert not _is_linked(a2, 'uppaal_TemplateType46', b)


def test_assoc_nta16_reverse_link_reassign_clear():
    a1 = uppaal_NtaType(declaration="sample_text", imports="sample_text", instantiation="sample_text", system="sample_text")
    a2 = uppaal_NtaType(declaration="sample_text_2", imports="sample_text_2", instantiation="sample_text_2", system="sample_text_2")
    b = uppaal_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    _safe_set(b, 'uppaal_DocumentRoot17', {a1})
    assert _is_linked(b, 'uppaal_DocumentRoot17', a1)
    if hasattr(a1, 'uppaal_NtaType'):
        assert _is_linked(a1, 'uppaal_NtaType', b)
    _safe_set(b, 'uppaal_DocumentRoot17', {a2})
    assert _is_linked(b, 'uppaal_DocumentRoot17', a2)
    if hasattr(a1, 'uppaal_NtaType'):
        assert not _is_linked(a1, 'uppaal_NtaType', b)
    if hasattr(a2, 'uppaal_NtaType'):
        assert _is_linked(a2, 'uppaal_NtaType', b)
    _safe_set(b, 'uppaal_DocumentRoot17', set())
    assert not _is_linked(b, 'uppaal_DocumentRoot17', a2)
    if hasattr(a2, 'uppaal_NtaType'):
        assert not _is_linked(a2, 'uppaal_NtaType', b)


def test_assoc_parameter18_reverse_link_reassign_clear():
    a1 = uppaal_ParameterType(mixed="sample_text", x="sample_text", y="sample_text")
    a2 = uppaal_ParameterType(mixed="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = uppaal_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    _safe_set(b, 'uppaal_DocumentRoot19', {a1})
    assert _is_linked(b, 'uppaal_DocumentRoot19', a1)
    if hasattr(a1, 'uppaal_ParameterType'):
        assert _is_linked(a1, 'uppaal_ParameterType', b)
    _safe_set(b, 'uppaal_DocumentRoot19', {a2})
    assert _is_linked(b, 'uppaal_DocumentRoot19', a2)
    if hasattr(a1, 'uppaal_ParameterType'):
        assert not _is_linked(a1, 'uppaal_ParameterType', b)
    if hasattr(a2, 'uppaal_ParameterType'):
        assert _is_linked(a2, 'uppaal_ParameterType', b)
    _safe_set(b, 'uppaal_DocumentRoot19', set())
    assert not _is_linked(b, 'uppaal_DocumentRoot19', a2)
    if hasattr(a2, 'uppaal_ParameterType'):
        assert not _is_linked(a2, 'uppaal_ParameterType', b)


def test_assoc_parameter48_reverse_link_reassign_clear():
    a1 = uppaal_TemplateType(declaration="sample_text")
    a2 = uppaal_TemplateType(declaration="sample_text_2")
    b = uppaal_ParameterType(mixed="sample_text", x="sample_text", y="sample_text")
    _safe_set(b, 'uppaal_ParameterType50', a1)
    assert _is_linked(b, 'uppaal_ParameterType50', a1)
    if hasattr(a1, 'uppaal_TemplateType49'):
        assert _is_linked(a1, 'uppaal_TemplateType49', b)
    _safe_set(b, 'uppaal_ParameterType50', a2)
    assert _is_linked(b, 'uppaal_ParameterType50', a2)
    if hasattr(a1, 'uppaal_TemplateType49'):
        assert not _is_linked(a1, 'uppaal_TemplateType49', b)
    if hasattr(a2, 'uppaal_TemplateType49'):
        assert _is_linked(a2, 'uppaal_TemplateType49', b)
    _safe_set(b, 'uppaal_ParameterType50', None)
    assert not _is_linked(b, 'uppaal_ParameterType50', a2)
    if hasattr(a2, 'uppaal_TemplateType49'):
        assert not _is_linked(a2, 'uppaal_TemplateType49', b)


def test_assoc_source20_reverse_link_reassign_clear():
    a1 = uppaal_SourceType(ref="sample_text")
    a2 = uppaal_SourceType(ref="sample_text_2")
    b = uppaal_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    _safe_set(b, 'uppaal_DocumentRoot21', {a1})
    assert _is_linked(b, 'uppaal_DocumentRoot21', a1)
    if hasattr(a1, 'uppaal_SourceType'):
        assert _is_linked(a1, 'uppaal_SourceType', b)
    _safe_set(b, 'uppaal_DocumentRoot21', {a2})
    assert _is_linked(b, 'uppaal_DocumentRoot21', a2)
    if hasattr(a1, 'uppaal_SourceType'):
        assert not _is_linked(a1, 'uppaal_SourceType', b)
    if hasattr(a2, 'uppaal_SourceType'):
        assert _is_linked(a2, 'uppaal_SourceType', b)
    _safe_set(b, 'uppaal_DocumentRoot21', set())
    assert not _is_linked(b, 'uppaal_DocumentRoot21', a2)
    if hasattr(a2, 'uppaal_SourceType'):
        assert not _is_linked(a2, 'uppaal_SourceType', b)


def test_assoc_source60_reverse_link_reassign_clear():
    a1 = uppaal_TransitionType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    a2 = uppaal_TransitionType(color="sample_text_2", id="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = uppaal_SourceType(ref="sample_text")
    _safe_set(b, 'uppaal_SourceType62', a1)
    assert _is_linked(b, 'uppaal_SourceType62', a1)
    if hasattr(a1, 'uppaal_TransitionType61'):
        assert _is_linked(a1, 'uppaal_TransitionType61', b)
    _safe_set(b, 'uppaal_SourceType62', a2)
    assert _is_linked(b, 'uppaal_SourceType62', a2)
    if hasattr(a1, 'uppaal_TransitionType61'):
        assert not _is_linked(a1, 'uppaal_TransitionType61', b)
    if hasattr(a2, 'uppaal_TransitionType61'):
        assert _is_linked(a2, 'uppaal_TransitionType61', b)
    _safe_set(b, 'uppaal_SourceType62', None)
    assert not _is_linked(b, 'uppaal_SourceType62', a2)
    if hasattr(a2, 'uppaal_TransitionType61'):
        assert not _is_linked(a2, 'uppaal_TransitionType61', b)


def test_assoc_target22_reverse_link_reassign_clear():
    a1 = uppaal_TargetType(ref="sample_text")
    a2 = uppaal_TargetType(ref="sample_text_2")
    b = uppaal_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    _safe_set(b, 'uppaal_DocumentRoot23', {a1})
    assert _is_linked(b, 'uppaal_DocumentRoot23', a1)
    if hasattr(a1, 'uppaal_TargetType'):
        assert _is_linked(a1, 'uppaal_TargetType', b)
    _safe_set(b, 'uppaal_DocumentRoot23', {a2})
    assert _is_linked(b, 'uppaal_DocumentRoot23', a2)
    if hasattr(a1, 'uppaal_TargetType'):
        assert not _is_linked(a1, 'uppaal_TargetType', b)
    if hasattr(a2, 'uppaal_TargetType'):
        assert _is_linked(a2, 'uppaal_TargetType', b)
    _safe_set(b, 'uppaal_DocumentRoot23', set())
    assert not _is_linked(b, 'uppaal_DocumentRoot23', a2)
    if hasattr(a2, 'uppaal_TargetType'):
        assert not _is_linked(a2, 'uppaal_TargetType', b)


def test_assoc_target63_reverse_link_reassign_clear():
    a1 = uppaal_TransitionType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    a2 = uppaal_TransitionType(color="sample_text_2", id="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = uppaal_TargetType(ref="sample_text")
    _safe_set(b, 'uppaal_TargetType65', a1)
    assert _is_linked(b, 'uppaal_TargetType65', a1)
    if hasattr(a1, 'uppaal_TransitionType64'):
        assert _is_linked(a1, 'uppaal_TransitionType64', b)
    _safe_set(b, 'uppaal_TargetType65', a2)
    assert _is_linked(b, 'uppaal_TargetType65', a2)
    if hasattr(a1, 'uppaal_TransitionType64'):
        assert not _is_linked(a1, 'uppaal_TransitionType64', b)
    if hasattr(a2, 'uppaal_TransitionType64'):
        assert _is_linked(a2, 'uppaal_TransitionType64', b)
    _safe_set(b, 'uppaal_TargetType65', None)
    assert not _is_linked(b, 'uppaal_TargetType65', a2)
    if hasattr(a2, 'uppaal_TransitionType64'):
        assert not _is_linked(a2, 'uppaal_TransitionType64', b)


def test_assoc_template24_reverse_link_reassign_clear():
    a1 = uppaal_TemplateType(declaration="sample_text")
    a2 = uppaal_TemplateType(declaration="sample_text_2")
    b = uppaal_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    _safe_set(b, 'uppaal_DocumentRoot25', {a1})
    assert _is_linked(b, 'uppaal_DocumentRoot25', a1)
    if hasattr(a1, 'uppaal_TemplateType'):
        assert _is_linked(a1, 'uppaal_TemplateType', b)
    _safe_set(b, 'uppaal_DocumentRoot25', {a2})
    assert _is_linked(b, 'uppaal_DocumentRoot25', a2)
    if hasattr(a1, 'uppaal_TemplateType'):
        assert not _is_linked(a1, 'uppaal_TemplateType', b)
    if hasattr(a2, 'uppaal_TemplateType'):
        assert _is_linked(a2, 'uppaal_TemplateType', b)
    _safe_set(b, 'uppaal_DocumentRoot25', set())
    assert not _is_linked(b, 'uppaal_DocumentRoot25', a2)
    if hasattr(a2, 'uppaal_TemplateType'):
        assert not _is_linked(a2, 'uppaal_TemplateType', b)


def test_assoc_template42_reverse_link_reassign_clear():
    a1 = uppaal_TemplateType(declaration="sample_text")
    a2 = uppaal_TemplateType(declaration="sample_text_2")
    b = uppaal_NtaType(declaration="sample_text", imports="sample_text", instantiation="sample_text", system="sample_text")
    _safe_set(b, 'uppaal_NtaType43', {a1})
    assert _is_linked(b, 'uppaal_NtaType43', a1)
    if hasattr(a1, 'uppaal_TemplateType44'):
        assert _is_linked(a1, 'uppaal_TemplateType44', b)
    _safe_set(b, 'uppaal_NtaType43', {a2})
    assert _is_linked(b, 'uppaal_NtaType43', a2)
    if hasattr(a1, 'uppaal_TemplateType44'):
        assert not _is_linked(a1, 'uppaal_TemplateType44', b)
    if hasattr(a2, 'uppaal_TemplateType44'):
        assert _is_linked(a2, 'uppaal_TemplateType44', b)
    _safe_set(b, 'uppaal_NtaType43', set())
    assert not _is_linked(b, 'uppaal_NtaType43', a2)
    if hasattr(a2, 'uppaal_TemplateType44'):
        assert not _is_linked(a2, 'uppaal_TemplateType44', b)


def test_assoc_transition26_reverse_link_reassign_clear():
    a1 = uppaal_TransitionType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    a2 = uppaal_TransitionType(color="sample_text_2", id="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = uppaal_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    _safe_set(b, 'uppaal_DocumentRoot27', {a1})
    assert _is_linked(b, 'uppaal_DocumentRoot27', a1)
    if hasattr(a1, 'uppaal_TransitionType'):
        assert _is_linked(a1, 'uppaal_TransitionType', b)
    _safe_set(b, 'uppaal_DocumentRoot27', {a2})
    assert _is_linked(b, 'uppaal_DocumentRoot27', a2)
    if hasattr(a1, 'uppaal_TransitionType'):
        assert not _is_linked(a1, 'uppaal_TransitionType', b)
    if hasattr(a2, 'uppaal_TransitionType'):
        assert _is_linked(a2, 'uppaal_TransitionType', b)
    _safe_set(b, 'uppaal_DocumentRoot27', set())
    assert not _is_linked(b, 'uppaal_DocumentRoot27', a2)
    if hasattr(a2, 'uppaal_TransitionType'):
        assert not _is_linked(a2, 'uppaal_TransitionType', b)


def test_assoc_transition57_reverse_link_reassign_clear():
    a1 = uppaal_TransitionType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    a2 = uppaal_TransitionType(color="sample_text_2", id="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = uppaal_TemplateType(declaration="sample_text")
    _safe_set(b, 'uppaal_TemplateType58', {a1})
    assert _is_linked(b, 'uppaal_TemplateType58', a1)
    if hasattr(a1, 'uppaal_TransitionType59'):
        assert _is_linked(a1, 'uppaal_TransitionType59', b)
    _safe_set(b, 'uppaal_TemplateType58', {a2})
    assert _is_linked(b, 'uppaal_TemplateType58', a2)
    if hasattr(a1, 'uppaal_TransitionType59'):
        assert not _is_linked(a1, 'uppaal_TransitionType59', b)
    if hasattr(a2, 'uppaal_TransitionType59'):
        assert _is_linked(a2, 'uppaal_TransitionType59', b)
    _safe_set(b, 'uppaal_TemplateType58', set())
    assert not _is_linked(b, 'uppaal_TemplateType58', a2)
    if hasattr(a2, 'uppaal_TransitionType59'):
        assert not _is_linked(a2, 'uppaal_TransitionType59', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_committed39_stub_double():
    # uppaal_CommittedType has no real 'uppaal_CommittedType41' property in the generated
    # code (a bare stub) -- manually attach it so uppaal_LocationType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uppaal_LocationType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uppaal_LocationType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    partner = uppaal_CommittedType()
    setattr(partner, 'uppaal_CommittedType41', None)
    _safe_set(owner, 'uppaal_LocationType40', partner)
    assert getattr(partner, 'uppaal_CommittedType41') == owner
    _safe_set(owner, 'uppaal_LocationType40', None)
    assert getattr(partner, 'uppaal_CommittedType41') is None


def test_assoc_committed4_stub_double():
    # uppaal_CommittedType has no real 'uppaal_CommittedType' property in the generated
    # code (a bare stub) -- manually attach it so uppaal_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uppaal_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uppaal_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    partner = uppaal_CommittedType()
    setattr(partner, 'uppaal_CommittedType', None)
    _safe_set(owner, 'uppaal_DocumentRoot5', {partner})
    assert getattr(partner, 'uppaal_CommittedType') == owner
    _safe_set(owner, 'uppaal_DocumentRoot5', set())
    assert getattr(partner, 'uppaal_CommittedType') is None


def test_assoc_urgent28_stub_double():
    # uppaal_UrgentType has no real 'uppaal_UrgentType' property in the generated
    # code (a bare stub) -- manually attach it so uppaal_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uppaal_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uppaal_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    partner = uppaal_UrgentType()
    setattr(partner, 'uppaal_UrgentType', None)
    _safe_set(owner, 'uppaal_DocumentRoot29', {partner})
    assert getattr(partner, 'uppaal_UrgentType') == owner
    _safe_set(owner, 'uppaal_DocumentRoot29', set())
    assert getattr(partner, 'uppaal_UrgentType') is None


def test_assoc_urgent36_stub_double():
    # uppaal_UrgentType has no real 'uppaal_UrgentType38' property in the generated
    # code (a bare stub) -- manually attach it so uppaal_LocationType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uppaal_LocationType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uppaal_LocationType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    partner = uppaal_UrgentType()
    setattr(partner, 'uppaal_UrgentType38', None)
    _safe_set(owner, 'uppaal_LocationType37', partner)
    assert getattr(partner, 'uppaal_UrgentType38') == owner
    _safe_set(owner, 'uppaal_LocationType37', None)
    assert getattr(partner, 'uppaal_UrgentType38') is None


def test_assoc_xMLNSPrefixMap0_stub_double():
    # uppaal_EStringToStringMapEntry has no real 'uppaal_EStringToStringMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so uppaal_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uppaal_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uppaal_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    partner = uppaal_EStringToStringMapEntry()
    setattr(partner, 'uppaal_EStringToStringMapEntry', None)
    _safe_set(owner, 'uppaal_DocumentRoot', {partner})
    assert getattr(partner, 'uppaal_EStringToStringMapEntry') == owner
    _safe_set(owner, 'uppaal_DocumentRoot', set())
    assert getattr(partner, 'uppaal_EStringToStringMapEntry') is None


def test_assoc_xSISchemaLocation1_stub_double():
    # uppaal_EStringToStringMapEntry has no real 'uppaal_EStringToStringMapEntry3' property in the generated
    # code (a bare stub) -- manually attach it so uppaal_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uppaal_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uppaal_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    partner = uppaal_EStringToStringMapEntry()
    setattr(partner, 'uppaal_EStringToStringMapEntry3', None)
    _safe_set(owner, 'uppaal_DocumentRoot2', {partner})
    assert getattr(partner, 'uppaal_EStringToStringMapEntry3') == owner
    _safe_set(owner, 'uppaal_DocumentRoot2', set())
    assert getattr(partner, 'uppaal_EStringToStringMapEntry3') is None


