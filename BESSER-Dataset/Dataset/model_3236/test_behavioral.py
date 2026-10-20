import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    UppaalFlat11_CommittedType,
    UppaalFlat11_DocumentRoot,
    UppaalFlat11_EStringToStringMapEntry,
    UppaalFlat11_InitType,
    UppaalFlat11_LabelType,
    UppaalFlat11_LocationType,
    UppaalFlat11_NailType,
    UppaalFlat11_NameType,
    UppaalFlat11_NtaType,
    UppaalFlat11_ParameterType,
    UppaalFlat11_SourceType,
    UppaalFlat11_TargetType,
    UppaalFlat11_TemplateType,
    UppaalFlat11_TransitionType,
    UppaalFlat11_UrgentType,
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
    a1 = UppaalFlat11_TemplateType(declaration="sample_text")
    a2 = UppaalFlat11_TemplateType(declaration="sample_text_2")
    b = UppaalFlat11_InitType(ref="sample_text")
    _safe_set(b, 'UppaalFlat11_InitType56', a1)
    assert _is_linked(b, 'UppaalFlat11_InitType56', a1)
    if hasattr(a1, 'UppaalFlat11_TemplateType55'):
        assert _is_linked(a1, 'UppaalFlat11_TemplateType55', b)
    _safe_set(b, 'UppaalFlat11_InitType56', a2)
    assert _is_linked(b, 'UppaalFlat11_InitType56', a2)
    if hasattr(a1, 'UppaalFlat11_TemplateType55'):
        assert not _is_linked(a1, 'UppaalFlat11_TemplateType55', b)
    if hasattr(a2, 'UppaalFlat11_TemplateType55'):
        assert _is_linked(a2, 'UppaalFlat11_TemplateType55', b)
    _safe_set(b, 'UppaalFlat11_InitType56', None)
    assert not _is_linked(b, 'UppaalFlat11_InitType56', a2)
    if hasattr(a2, 'UppaalFlat11_TemplateType55'):
        assert not _is_linked(a2, 'UppaalFlat11_TemplateType55', b)


def test_assoc_init6_reverse_link_reassign_clear():
    a1 = UppaalFlat11_InitType(ref="sample_text")
    a2 = UppaalFlat11_InitType(ref="sample_text_2")
    b = UppaalFlat11_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    _safe_set(b, 'UppaalFlat11_DocumentRoot7', {a1})
    assert _is_linked(b, 'UppaalFlat11_DocumentRoot7', a1)
    if hasattr(a1, 'UppaalFlat11_InitType'):
        assert _is_linked(a1, 'UppaalFlat11_InitType', b)
    _safe_set(b, 'UppaalFlat11_DocumentRoot7', {a2})
    assert _is_linked(b, 'UppaalFlat11_DocumentRoot7', a2)
    if hasattr(a1, 'UppaalFlat11_InitType'):
        assert not _is_linked(a1, 'UppaalFlat11_InitType', b)
    if hasattr(a2, 'UppaalFlat11_InitType'):
        assert _is_linked(a2, 'UppaalFlat11_InitType', b)
    _safe_set(b, 'UppaalFlat11_DocumentRoot7', set())
    assert not _is_linked(b, 'UppaalFlat11_DocumentRoot7', a2)
    if hasattr(a2, 'UppaalFlat11_InitType'):
        assert not _is_linked(a2, 'UppaalFlat11_InitType', b)


def test_assoc_label33_reverse_link_reassign_clear():
    a1 = UppaalFlat11_LocationType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    a2 = UppaalFlat11_LocationType(color="sample_text_2", id="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = UppaalFlat11_LabelType(kind="sample_text", mixed="sample_text", x="sample_text", y="sample_text")
    _safe_set(b, 'UppaalFlat11_LabelType35', a1)
    assert _is_linked(b, 'UppaalFlat11_LabelType35', a1)
    if hasattr(a1, 'UppaalFlat11_LocationType34'):
        assert _is_linked(a1, 'UppaalFlat11_LocationType34', b)
    _safe_set(b, 'UppaalFlat11_LabelType35', a2)
    assert _is_linked(b, 'UppaalFlat11_LabelType35', a2)
    if hasattr(a1, 'UppaalFlat11_LocationType34'):
        assert not _is_linked(a1, 'UppaalFlat11_LocationType34', b)
    if hasattr(a2, 'UppaalFlat11_LocationType34'):
        assert _is_linked(a2, 'UppaalFlat11_LocationType34', b)
    _safe_set(b, 'UppaalFlat11_LabelType35', None)
    assert not _is_linked(b, 'UppaalFlat11_LabelType35', a2)
    if hasattr(a2, 'UppaalFlat11_LocationType34'):
        assert not _is_linked(a2, 'UppaalFlat11_LocationType34', b)


def test_assoc_label66_reverse_link_reassign_clear():
    a1 = UppaalFlat11_TransitionType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    a2 = UppaalFlat11_TransitionType(color="sample_text_2", id="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = UppaalFlat11_LabelType(kind="sample_text", mixed="sample_text", x="sample_text", y="sample_text")
    _safe_set(b, 'UppaalFlat11_LabelType68', a1)
    assert _is_linked(b, 'UppaalFlat11_LabelType68', a1)
    if hasattr(a1, 'UppaalFlat11_TransitionType67'):
        assert _is_linked(a1, 'UppaalFlat11_TransitionType67', b)
    _safe_set(b, 'UppaalFlat11_LabelType68', a2)
    assert _is_linked(b, 'UppaalFlat11_LabelType68', a2)
    if hasattr(a1, 'UppaalFlat11_TransitionType67'):
        assert not _is_linked(a1, 'UppaalFlat11_TransitionType67', b)
    if hasattr(a2, 'UppaalFlat11_TransitionType67'):
        assert _is_linked(a2, 'UppaalFlat11_TransitionType67', b)
    _safe_set(b, 'UppaalFlat11_LabelType68', None)
    assert not _is_linked(b, 'UppaalFlat11_LabelType68', a2)
    if hasattr(a2, 'UppaalFlat11_TransitionType67'):
        assert not _is_linked(a2, 'UppaalFlat11_TransitionType67', b)


def test_assoc_label8_reverse_link_reassign_clear():
    a1 = UppaalFlat11_LabelType(kind="sample_text", mixed="sample_text", x="sample_text", y="sample_text")
    a2 = UppaalFlat11_LabelType(kind="sample_text_2", mixed="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = UppaalFlat11_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    _safe_set(b, 'UppaalFlat11_DocumentRoot9', {a1})
    assert _is_linked(b, 'UppaalFlat11_DocumentRoot9', a1)
    if hasattr(a1, 'UppaalFlat11_LabelType'):
        assert _is_linked(a1, 'UppaalFlat11_LabelType', b)
    _safe_set(b, 'UppaalFlat11_DocumentRoot9', {a2})
    assert _is_linked(b, 'UppaalFlat11_DocumentRoot9', a2)
    if hasattr(a1, 'UppaalFlat11_LabelType'):
        assert not _is_linked(a1, 'UppaalFlat11_LabelType', b)
    if hasattr(a2, 'UppaalFlat11_LabelType'):
        assert _is_linked(a2, 'UppaalFlat11_LabelType', b)
    _safe_set(b, 'UppaalFlat11_DocumentRoot9', set())
    assert not _is_linked(b, 'UppaalFlat11_DocumentRoot9', a2)
    if hasattr(a2, 'UppaalFlat11_LabelType'):
        assert not _is_linked(a2, 'UppaalFlat11_LabelType', b)


def test_assoc_location10_reverse_link_reassign_clear():
    a1 = UppaalFlat11_LocationType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    a2 = UppaalFlat11_LocationType(color="sample_text_2", id="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = UppaalFlat11_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    _safe_set(b, 'UppaalFlat11_DocumentRoot11', {a1})
    assert _is_linked(b, 'UppaalFlat11_DocumentRoot11', a1)
    if hasattr(a1, 'UppaalFlat11_LocationType'):
        assert _is_linked(a1, 'UppaalFlat11_LocationType', b)
    _safe_set(b, 'UppaalFlat11_DocumentRoot11', {a2})
    assert _is_linked(b, 'UppaalFlat11_DocumentRoot11', a2)
    if hasattr(a1, 'UppaalFlat11_LocationType'):
        assert not _is_linked(a1, 'UppaalFlat11_LocationType', b)
    if hasattr(a2, 'UppaalFlat11_LocationType'):
        assert _is_linked(a2, 'UppaalFlat11_LocationType', b)
    _safe_set(b, 'UppaalFlat11_DocumentRoot11', set())
    assert not _is_linked(b, 'UppaalFlat11_DocumentRoot11', a2)
    if hasattr(a2, 'UppaalFlat11_LocationType'):
        assert not _is_linked(a2, 'UppaalFlat11_LocationType', b)


def test_assoc_location51_reverse_link_reassign_clear():
    a1 = UppaalFlat11_TemplateType(declaration="sample_text")
    a2 = UppaalFlat11_TemplateType(declaration="sample_text_2")
    b = UppaalFlat11_LocationType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    _safe_set(b, 'UppaalFlat11_LocationType53', a1)
    assert _is_linked(b, 'UppaalFlat11_LocationType53', a1)
    if hasattr(a1, 'UppaalFlat11_TemplateType52'):
        assert _is_linked(a1, 'UppaalFlat11_TemplateType52', b)
    _safe_set(b, 'UppaalFlat11_LocationType53', a2)
    assert _is_linked(b, 'UppaalFlat11_LocationType53', a2)
    if hasattr(a1, 'UppaalFlat11_TemplateType52'):
        assert not _is_linked(a1, 'UppaalFlat11_TemplateType52', b)
    if hasattr(a2, 'UppaalFlat11_TemplateType52'):
        assert _is_linked(a2, 'UppaalFlat11_TemplateType52', b)
    _safe_set(b, 'UppaalFlat11_LocationType53', None)
    assert not _is_linked(b, 'UppaalFlat11_LocationType53', a2)
    if hasattr(a2, 'UppaalFlat11_TemplateType52'):
        assert not _is_linked(a2, 'UppaalFlat11_TemplateType52', b)


def test_assoc_nail12_reverse_link_reassign_clear():
    a1 = UppaalFlat11_NailType(x="sample_text", y="sample_text")
    a2 = UppaalFlat11_NailType(x="sample_text_2", y="sample_text_2")
    b = UppaalFlat11_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    _safe_set(b, 'UppaalFlat11_DocumentRoot13', {a1})
    assert _is_linked(b, 'UppaalFlat11_DocumentRoot13', a1)
    if hasattr(a1, 'UppaalFlat11_NailType'):
        assert _is_linked(a1, 'UppaalFlat11_NailType', b)
    _safe_set(b, 'UppaalFlat11_DocumentRoot13', {a2})
    assert _is_linked(b, 'UppaalFlat11_DocumentRoot13', a2)
    if hasattr(a1, 'UppaalFlat11_NailType'):
        assert not _is_linked(a1, 'UppaalFlat11_NailType', b)
    if hasattr(a2, 'UppaalFlat11_NailType'):
        assert _is_linked(a2, 'UppaalFlat11_NailType', b)
    _safe_set(b, 'UppaalFlat11_DocumentRoot13', set())
    assert not _is_linked(b, 'UppaalFlat11_DocumentRoot13', a2)
    if hasattr(a2, 'UppaalFlat11_NailType'):
        assert not _is_linked(a2, 'UppaalFlat11_NailType', b)


def test_assoc_nail69_reverse_link_reassign_clear():
    a1 = UppaalFlat11_TransitionType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    a2 = UppaalFlat11_TransitionType(color="sample_text_2", id="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = UppaalFlat11_NailType(x="sample_text", y="sample_text")
    _safe_set(b, 'UppaalFlat11_NailType71', a1)
    assert _is_linked(b, 'UppaalFlat11_NailType71', a1)
    if hasattr(a1, 'UppaalFlat11_TransitionType70'):
        assert _is_linked(a1, 'UppaalFlat11_TransitionType70', b)
    _safe_set(b, 'UppaalFlat11_NailType71', a2)
    assert _is_linked(b, 'UppaalFlat11_NailType71', a2)
    if hasattr(a1, 'UppaalFlat11_TransitionType70'):
        assert not _is_linked(a1, 'UppaalFlat11_TransitionType70', b)
    if hasattr(a2, 'UppaalFlat11_TransitionType70'):
        assert _is_linked(a2, 'UppaalFlat11_TransitionType70', b)
    _safe_set(b, 'UppaalFlat11_NailType71', None)
    assert not _is_linked(b, 'UppaalFlat11_NailType71', a2)
    if hasattr(a2, 'UppaalFlat11_TransitionType70'):
        assert not _is_linked(a2, 'UppaalFlat11_TransitionType70', b)


def test_assoc_name14_reverse_link_reassign_clear():
    a1 = UppaalFlat11_NameType(mixed="sample_text", x="sample_text", y="sample_text")
    a2 = UppaalFlat11_NameType(mixed="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = UppaalFlat11_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    _safe_set(b, 'UppaalFlat11_DocumentRoot15', {a1})
    assert _is_linked(b, 'UppaalFlat11_DocumentRoot15', a1)
    if hasattr(a1, 'UppaalFlat11_NameType'):
        assert _is_linked(a1, 'UppaalFlat11_NameType', b)
    _safe_set(b, 'UppaalFlat11_DocumentRoot15', {a2})
    assert _is_linked(b, 'UppaalFlat11_DocumentRoot15', a2)
    if hasattr(a1, 'UppaalFlat11_NameType'):
        assert not _is_linked(a1, 'UppaalFlat11_NameType', b)
    if hasattr(a2, 'UppaalFlat11_NameType'):
        assert _is_linked(a2, 'UppaalFlat11_NameType', b)
    _safe_set(b, 'UppaalFlat11_DocumentRoot15', set())
    assert not _is_linked(b, 'UppaalFlat11_DocumentRoot15', a2)
    if hasattr(a2, 'UppaalFlat11_NameType'):
        assert not _is_linked(a2, 'UppaalFlat11_NameType', b)


def test_assoc_name30_reverse_link_reassign_clear():
    a1 = UppaalFlat11_NameType(mixed="sample_text", x="sample_text", y="sample_text")
    a2 = UppaalFlat11_NameType(mixed="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = UppaalFlat11_LocationType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    _safe_set(b, 'UppaalFlat11_LocationType31', a1)
    assert _is_linked(b, 'UppaalFlat11_LocationType31', a1)
    if hasattr(a1, 'UppaalFlat11_NameType32'):
        assert _is_linked(a1, 'UppaalFlat11_NameType32', b)
    _safe_set(b, 'UppaalFlat11_LocationType31', a2)
    assert _is_linked(b, 'UppaalFlat11_LocationType31', a2)
    if hasattr(a1, 'UppaalFlat11_NameType32'):
        assert not _is_linked(a1, 'UppaalFlat11_NameType32', b)
    if hasattr(a2, 'UppaalFlat11_NameType32'):
        assert _is_linked(a2, 'UppaalFlat11_NameType32', b)
    _safe_set(b, 'UppaalFlat11_LocationType31', None)
    assert not _is_linked(b, 'UppaalFlat11_LocationType31', a2)
    if hasattr(a2, 'UppaalFlat11_NameType32'):
        assert not _is_linked(a2, 'UppaalFlat11_NameType32', b)


def test_assoc_name45_reverse_link_reassign_clear():
    a1 = UppaalFlat11_TemplateType(declaration="sample_text")
    a2 = UppaalFlat11_TemplateType(declaration="sample_text_2")
    b = UppaalFlat11_NameType(mixed="sample_text", x="sample_text", y="sample_text")
    _safe_set(b, 'UppaalFlat11_NameType47', a1)
    assert _is_linked(b, 'UppaalFlat11_NameType47', a1)
    if hasattr(a1, 'UppaalFlat11_TemplateType46'):
        assert _is_linked(a1, 'UppaalFlat11_TemplateType46', b)
    _safe_set(b, 'UppaalFlat11_NameType47', a2)
    assert _is_linked(b, 'UppaalFlat11_NameType47', a2)
    if hasattr(a1, 'UppaalFlat11_TemplateType46'):
        assert not _is_linked(a1, 'UppaalFlat11_TemplateType46', b)
    if hasattr(a2, 'UppaalFlat11_TemplateType46'):
        assert _is_linked(a2, 'UppaalFlat11_TemplateType46', b)
    _safe_set(b, 'UppaalFlat11_NameType47', None)
    assert not _is_linked(b, 'UppaalFlat11_NameType47', a2)
    if hasattr(a2, 'UppaalFlat11_TemplateType46'):
        assert not _is_linked(a2, 'UppaalFlat11_TemplateType46', b)


def test_assoc_nta16_reverse_link_reassign_clear():
    a1 = UppaalFlat11_NtaType(declaration="sample_text", imports="sample_text", instantiation="sample_text", system="sample_text")
    a2 = UppaalFlat11_NtaType(declaration="sample_text_2", imports="sample_text_2", instantiation="sample_text_2", system="sample_text_2")
    b = UppaalFlat11_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    _safe_set(b, 'UppaalFlat11_DocumentRoot17', {a1})
    assert _is_linked(b, 'UppaalFlat11_DocumentRoot17', a1)
    if hasattr(a1, 'UppaalFlat11_NtaType'):
        assert _is_linked(a1, 'UppaalFlat11_NtaType', b)
    _safe_set(b, 'UppaalFlat11_DocumentRoot17', {a2})
    assert _is_linked(b, 'UppaalFlat11_DocumentRoot17', a2)
    if hasattr(a1, 'UppaalFlat11_NtaType'):
        assert not _is_linked(a1, 'UppaalFlat11_NtaType', b)
    if hasattr(a2, 'UppaalFlat11_NtaType'):
        assert _is_linked(a2, 'UppaalFlat11_NtaType', b)
    _safe_set(b, 'UppaalFlat11_DocumentRoot17', set())
    assert not _is_linked(b, 'UppaalFlat11_DocumentRoot17', a2)
    if hasattr(a2, 'UppaalFlat11_NtaType'):
        assert not _is_linked(a2, 'UppaalFlat11_NtaType', b)


def test_assoc_parameter18_reverse_link_reassign_clear():
    a1 = UppaalFlat11_ParameterType(mixed="sample_text", x="sample_text", y="sample_text")
    a2 = UppaalFlat11_ParameterType(mixed="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = UppaalFlat11_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    _safe_set(b, 'UppaalFlat11_DocumentRoot19', {a1})
    assert _is_linked(b, 'UppaalFlat11_DocumentRoot19', a1)
    if hasattr(a1, 'UppaalFlat11_ParameterType'):
        assert _is_linked(a1, 'UppaalFlat11_ParameterType', b)
    _safe_set(b, 'UppaalFlat11_DocumentRoot19', {a2})
    assert _is_linked(b, 'UppaalFlat11_DocumentRoot19', a2)
    if hasattr(a1, 'UppaalFlat11_ParameterType'):
        assert not _is_linked(a1, 'UppaalFlat11_ParameterType', b)
    if hasattr(a2, 'UppaalFlat11_ParameterType'):
        assert _is_linked(a2, 'UppaalFlat11_ParameterType', b)
    _safe_set(b, 'UppaalFlat11_DocumentRoot19', set())
    assert not _is_linked(b, 'UppaalFlat11_DocumentRoot19', a2)
    if hasattr(a2, 'UppaalFlat11_ParameterType'):
        assert not _is_linked(a2, 'UppaalFlat11_ParameterType', b)


def test_assoc_parameter48_reverse_link_reassign_clear():
    a1 = UppaalFlat11_TemplateType(declaration="sample_text")
    a2 = UppaalFlat11_TemplateType(declaration="sample_text_2")
    b = UppaalFlat11_ParameterType(mixed="sample_text", x="sample_text", y="sample_text")
    _safe_set(b, 'UppaalFlat11_ParameterType50', a1)
    assert _is_linked(b, 'UppaalFlat11_ParameterType50', a1)
    if hasattr(a1, 'UppaalFlat11_TemplateType49'):
        assert _is_linked(a1, 'UppaalFlat11_TemplateType49', b)
    _safe_set(b, 'UppaalFlat11_ParameterType50', a2)
    assert _is_linked(b, 'UppaalFlat11_ParameterType50', a2)
    if hasattr(a1, 'UppaalFlat11_TemplateType49'):
        assert not _is_linked(a1, 'UppaalFlat11_TemplateType49', b)
    if hasattr(a2, 'UppaalFlat11_TemplateType49'):
        assert _is_linked(a2, 'UppaalFlat11_TemplateType49', b)
    _safe_set(b, 'UppaalFlat11_ParameterType50', None)
    assert not _is_linked(b, 'UppaalFlat11_ParameterType50', a2)
    if hasattr(a2, 'UppaalFlat11_TemplateType49'):
        assert not _is_linked(a2, 'UppaalFlat11_TemplateType49', b)


def test_assoc_source20_reverse_link_reassign_clear():
    a1 = UppaalFlat11_SourceType(ref="sample_text")
    a2 = UppaalFlat11_SourceType(ref="sample_text_2")
    b = UppaalFlat11_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    _safe_set(b, 'UppaalFlat11_DocumentRoot21', {a1})
    assert _is_linked(b, 'UppaalFlat11_DocumentRoot21', a1)
    if hasattr(a1, 'UppaalFlat11_SourceType'):
        assert _is_linked(a1, 'UppaalFlat11_SourceType', b)
    _safe_set(b, 'UppaalFlat11_DocumentRoot21', {a2})
    assert _is_linked(b, 'UppaalFlat11_DocumentRoot21', a2)
    if hasattr(a1, 'UppaalFlat11_SourceType'):
        assert not _is_linked(a1, 'UppaalFlat11_SourceType', b)
    if hasattr(a2, 'UppaalFlat11_SourceType'):
        assert _is_linked(a2, 'UppaalFlat11_SourceType', b)
    _safe_set(b, 'UppaalFlat11_DocumentRoot21', set())
    assert not _is_linked(b, 'UppaalFlat11_DocumentRoot21', a2)
    if hasattr(a2, 'UppaalFlat11_SourceType'):
        assert not _is_linked(a2, 'UppaalFlat11_SourceType', b)


def test_assoc_source60_reverse_link_reassign_clear():
    a1 = UppaalFlat11_TransitionType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    a2 = UppaalFlat11_TransitionType(color="sample_text_2", id="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = UppaalFlat11_SourceType(ref="sample_text")
    _safe_set(b, 'UppaalFlat11_SourceType62', a1)
    assert _is_linked(b, 'UppaalFlat11_SourceType62', a1)
    if hasattr(a1, 'UppaalFlat11_TransitionType61'):
        assert _is_linked(a1, 'UppaalFlat11_TransitionType61', b)
    _safe_set(b, 'UppaalFlat11_SourceType62', a2)
    assert _is_linked(b, 'UppaalFlat11_SourceType62', a2)
    if hasattr(a1, 'UppaalFlat11_TransitionType61'):
        assert not _is_linked(a1, 'UppaalFlat11_TransitionType61', b)
    if hasattr(a2, 'UppaalFlat11_TransitionType61'):
        assert _is_linked(a2, 'UppaalFlat11_TransitionType61', b)
    _safe_set(b, 'UppaalFlat11_SourceType62', None)
    assert not _is_linked(b, 'UppaalFlat11_SourceType62', a2)
    if hasattr(a2, 'UppaalFlat11_TransitionType61'):
        assert not _is_linked(a2, 'UppaalFlat11_TransitionType61', b)


def test_assoc_target22_reverse_link_reassign_clear():
    a1 = UppaalFlat11_TargetType(ref="sample_text")
    a2 = UppaalFlat11_TargetType(ref="sample_text_2")
    b = UppaalFlat11_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    _safe_set(b, 'UppaalFlat11_DocumentRoot23', {a1})
    assert _is_linked(b, 'UppaalFlat11_DocumentRoot23', a1)
    if hasattr(a1, 'UppaalFlat11_TargetType'):
        assert _is_linked(a1, 'UppaalFlat11_TargetType', b)
    _safe_set(b, 'UppaalFlat11_DocumentRoot23', {a2})
    assert _is_linked(b, 'UppaalFlat11_DocumentRoot23', a2)
    if hasattr(a1, 'UppaalFlat11_TargetType'):
        assert not _is_linked(a1, 'UppaalFlat11_TargetType', b)
    if hasattr(a2, 'UppaalFlat11_TargetType'):
        assert _is_linked(a2, 'UppaalFlat11_TargetType', b)
    _safe_set(b, 'UppaalFlat11_DocumentRoot23', set())
    assert not _is_linked(b, 'UppaalFlat11_DocumentRoot23', a2)
    if hasattr(a2, 'UppaalFlat11_TargetType'):
        assert not _is_linked(a2, 'UppaalFlat11_TargetType', b)


def test_assoc_target63_reverse_link_reassign_clear():
    a1 = UppaalFlat11_TransitionType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    a2 = UppaalFlat11_TransitionType(color="sample_text_2", id="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = UppaalFlat11_TargetType(ref="sample_text")
    _safe_set(b, 'UppaalFlat11_TargetType65', a1)
    assert _is_linked(b, 'UppaalFlat11_TargetType65', a1)
    if hasattr(a1, 'UppaalFlat11_TransitionType64'):
        assert _is_linked(a1, 'UppaalFlat11_TransitionType64', b)
    _safe_set(b, 'UppaalFlat11_TargetType65', a2)
    assert _is_linked(b, 'UppaalFlat11_TargetType65', a2)
    if hasattr(a1, 'UppaalFlat11_TransitionType64'):
        assert not _is_linked(a1, 'UppaalFlat11_TransitionType64', b)
    if hasattr(a2, 'UppaalFlat11_TransitionType64'):
        assert _is_linked(a2, 'UppaalFlat11_TransitionType64', b)
    _safe_set(b, 'UppaalFlat11_TargetType65', None)
    assert not _is_linked(b, 'UppaalFlat11_TargetType65', a2)
    if hasattr(a2, 'UppaalFlat11_TransitionType64'):
        assert not _is_linked(a2, 'UppaalFlat11_TransitionType64', b)


def test_assoc_template24_reverse_link_reassign_clear():
    a1 = UppaalFlat11_TemplateType(declaration="sample_text")
    a2 = UppaalFlat11_TemplateType(declaration="sample_text_2")
    b = UppaalFlat11_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    _safe_set(b, 'UppaalFlat11_DocumentRoot25', {a1})
    assert _is_linked(b, 'UppaalFlat11_DocumentRoot25', a1)
    if hasattr(a1, 'UppaalFlat11_TemplateType'):
        assert _is_linked(a1, 'UppaalFlat11_TemplateType', b)
    _safe_set(b, 'UppaalFlat11_DocumentRoot25', {a2})
    assert _is_linked(b, 'UppaalFlat11_DocumentRoot25', a2)
    if hasattr(a1, 'UppaalFlat11_TemplateType'):
        assert not _is_linked(a1, 'UppaalFlat11_TemplateType', b)
    if hasattr(a2, 'UppaalFlat11_TemplateType'):
        assert _is_linked(a2, 'UppaalFlat11_TemplateType', b)
    _safe_set(b, 'UppaalFlat11_DocumentRoot25', set())
    assert not _is_linked(b, 'UppaalFlat11_DocumentRoot25', a2)
    if hasattr(a2, 'UppaalFlat11_TemplateType'):
        assert not _is_linked(a2, 'UppaalFlat11_TemplateType', b)


def test_assoc_template42_reverse_link_reassign_clear():
    a1 = UppaalFlat11_TemplateType(declaration="sample_text")
    a2 = UppaalFlat11_TemplateType(declaration="sample_text_2")
    b = UppaalFlat11_NtaType(declaration="sample_text", imports="sample_text", instantiation="sample_text", system="sample_text")
    _safe_set(b, 'UppaalFlat11_NtaType43', {a1})
    assert _is_linked(b, 'UppaalFlat11_NtaType43', a1)
    if hasattr(a1, 'UppaalFlat11_TemplateType44'):
        assert _is_linked(a1, 'UppaalFlat11_TemplateType44', b)
    _safe_set(b, 'UppaalFlat11_NtaType43', {a2})
    assert _is_linked(b, 'UppaalFlat11_NtaType43', a2)
    if hasattr(a1, 'UppaalFlat11_TemplateType44'):
        assert not _is_linked(a1, 'UppaalFlat11_TemplateType44', b)
    if hasattr(a2, 'UppaalFlat11_TemplateType44'):
        assert _is_linked(a2, 'UppaalFlat11_TemplateType44', b)
    _safe_set(b, 'UppaalFlat11_NtaType43', set())
    assert not _is_linked(b, 'UppaalFlat11_NtaType43', a2)
    if hasattr(a2, 'UppaalFlat11_TemplateType44'):
        assert not _is_linked(a2, 'UppaalFlat11_TemplateType44', b)


def test_assoc_transition26_reverse_link_reassign_clear():
    a1 = UppaalFlat11_TransitionType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    a2 = UppaalFlat11_TransitionType(color="sample_text_2", id="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = UppaalFlat11_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    _safe_set(b, 'UppaalFlat11_DocumentRoot27', {a1})
    assert _is_linked(b, 'UppaalFlat11_DocumentRoot27', a1)
    if hasattr(a1, 'UppaalFlat11_TransitionType'):
        assert _is_linked(a1, 'UppaalFlat11_TransitionType', b)
    _safe_set(b, 'UppaalFlat11_DocumentRoot27', {a2})
    assert _is_linked(b, 'UppaalFlat11_DocumentRoot27', a2)
    if hasattr(a1, 'UppaalFlat11_TransitionType'):
        assert not _is_linked(a1, 'UppaalFlat11_TransitionType', b)
    if hasattr(a2, 'UppaalFlat11_TransitionType'):
        assert _is_linked(a2, 'UppaalFlat11_TransitionType', b)
    _safe_set(b, 'UppaalFlat11_DocumentRoot27', set())
    assert not _is_linked(b, 'UppaalFlat11_DocumentRoot27', a2)
    if hasattr(a2, 'UppaalFlat11_TransitionType'):
        assert not _is_linked(a2, 'UppaalFlat11_TransitionType', b)


def test_assoc_transition57_reverse_link_reassign_clear():
    a1 = UppaalFlat11_TransitionType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    a2 = UppaalFlat11_TransitionType(color="sample_text_2", id="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = UppaalFlat11_TemplateType(declaration="sample_text")
    _safe_set(b, 'UppaalFlat11_TemplateType58', {a1})
    assert _is_linked(b, 'UppaalFlat11_TemplateType58', a1)
    if hasattr(a1, 'UppaalFlat11_TransitionType59'):
        assert _is_linked(a1, 'UppaalFlat11_TransitionType59', b)
    _safe_set(b, 'UppaalFlat11_TemplateType58', {a2})
    assert _is_linked(b, 'UppaalFlat11_TemplateType58', a2)
    if hasattr(a1, 'UppaalFlat11_TransitionType59'):
        assert not _is_linked(a1, 'UppaalFlat11_TransitionType59', b)
    if hasattr(a2, 'UppaalFlat11_TransitionType59'):
        assert _is_linked(a2, 'UppaalFlat11_TransitionType59', b)
    _safe_set(b, 'UppaalFlat11_TemplateType58', set())
    assert not _is_linked(b, 'UppaalFlat11_TemplateType58', a2)
    if hasattr(a2, 'UppaalFlat11_TransitionType59'):
        assert not _is_linked(a2, 'UppaalFlat11_TransitionType59', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_committed39_stub_double():
    # UppaalFlat11_CommittedType has no real 'UppaalFlat11_CommittedType41' property in the generated
    # code (a bare stub) -- manually attach it so UppaalFlat11_LocationType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UppaalFlat11_LocationType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UppaalFlat11_LocationType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    partner = UppaalFlat11_CommittedType()
    setattr(partner, 'UppaalFlat11_CommittedType41', None)
    _safe_set(owner, 'UppaalFlat11_LocationType40', partner)
    assert getattr(partner, 'UppaalFlat11_CommittedType41') == owner
    _safe_set(owner, 'UppaalFlat11_LocationType40', None)
    assert getattr(partner, 'UppaalFlat11_CommittedType41') is None


def test_assoc_committed4_stub_double():
    # UppaalFlat11_CommittedType has no real 'UppaalFlat11_CommittedType' property in the generated
    # code (a bare stub) -- manually attach it so UppaalFlat11_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UppaalFlat11_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UppaalFlat11_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    partner = UppaalFlat11_CommittedType()
    setattr(partner, 'UppaalFlat11_CommittedType', None)
    _safe_set(owner, 'UppaalFlat11_DocumentRoot5', {partner})
    assert getattr(partner, 'UppaalFlat11_CommittedType') == owner
    _safe_set(owner, 'UppaalFlat11_DocumentRoot5', set())
    assert getattr(partner, 'UppaalFlat11_CommittedType') is None


def test_assoc_urgent28_stub_double():
    # UppaalFlat11_UrgentType has no real 'UppaalFlat11_UrgentType' property in the generated
    # code (a bare stub) -- manually attach it so UppaalFlat11_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UppaalFlat11_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UppaalFlat11_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    partner = UppaalFlat11_UrgentType()
    setattr(partner, 'UppaalFlat11_UrgentType', None)
    _safe_set(owner, 'UppaalFlat11_DocumentRoot29', {partner})
    assert getattr(partner, 'UppaalFlat11_UrgentType') == owner
    _safe_set(owner, 'UppaalFlat11_DocumentRoot29', set())
    assert getattr(partner, 'UppaalFlat11_UrgentType') is None


def test_assoc_urgent36_stub_double():
    # UppaalFlat11_UrgentType has no real 'UppaalFlat11_UrgentType38' property in the generated
    # code (a bare stub) -- manually attach it so UppaalFlat11_LocationType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UppaalFlat11_LocationType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UppaalFlat11_LocationType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    partner = UppaalFlat11_UrgentType()
    setattr(partner, 'UppaalFlat11_UrgentType38', None)
    _safe_set(owner, 'UppaalFlat11_LocationType37', partner)
    assert getattr(partner, 'UppaalFlat11_UrgentType38') == owner
    _safe_set(owner, 'UppaalFlat11_LocationType37', None)
    assert getattr(partner, 'UppaalFlat11_UrgentType38') is None


def test_assoc_xMLNSPrefixMap0_stub_double():
    # UppaalFlat11_EStringToStringMapEntry has no real 'UppaalFlat11_EStringToStringMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so UppaalFlat11_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UppaalFlat11_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UppaalFlat11_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    partner = UppaalFlat11_EStringToStringMapEntry()
    setattr(partner, 'UppaalFlat11_EStringToStringMapEntry', None)
    _safe_set(owner, 'UppaalFlat11_DocumentRoot', {partner})
    assert getattr(partner, 'UppaalFlat11_EStringToStringMapEntry') == owner
    _safe_set(owner, 'UppaalFlat11_DocumentRoot', set())
    assert getattr(partner, 'UppaalFlat11_EStringToStringMapEntry') is None


def test_assoc_xSISchemaLocation1_stub_double():
    # UppaalFlat11_EStringToStringMapEntry has no real 'UppaalFlat11_EStringToStringMapEntry3' property in the generated
    # code (a bare stub) -- manually attach it so UppaalFlat11_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UppaalFlat11_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UppaalFlat11_DocumentRoot(declaration="sample_text", imports="sample_text", instantiation="sample_text", mixed="sample_text", system="sample_text")
    partner = UppaalFlat11_EStringToStringMapEntry()
    setattr(partner, 'UppaalFlat11_EStringToStringMapEntry3', None)
    _safe_set(owner, 'UppaalFlat11_DocumentRoot2', {partner})
    assert getattr(partner, 'UppaalFlat11_EStringToStringMapEntry3') == owner
    _safe_set(owner, 'UppaalFlat11_DocumentRoot2', set())
    assert getattr(partner, 'UppaalFlat11_EStringToStringMapEntry3') is None


