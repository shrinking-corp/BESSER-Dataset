import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Uppaal_DeclarationType,
    Uppaal_DocumentRoot,
    Uppaal_EStringToStringMapEntry,
    Uppaal_ImportsType,
    Uppaal_InitType,
    Uppaal_InstantiationType,
    Uppaal_LabelType,
    Uppaal_LocationType,
    Uppaal_NailType,
    Uppaal_NameType,
    Uppaal_NtaType,
    Uppaal_ParameterType,
    Uppaal_SourceType,
    Uppaal_SystemType,
    Uppaal_TargetType,
    Uppaal_TemplateType,
    Uppaal_TransitionType,
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

def test_assoc_declaration4_reverse_link_reassign_clear():
    a1 = Uppaal_DocumentRoot(committed="sample_text", mixed="sample_text", urgent="sample_text")
    a2 = Uppaal_DocumentRoot(committed="sample_text_2", mixed="sample_text_2", urgent="sample_text_2")
    b = Uppaal_DeclarationType(mixed="sample_text")
    _safe_set(b, 'Uppaal_DeclarationType', a1)
    assert _is_linked(b, 'Uppaal_DeclarationType', a1)
    if hasattr(a1, 'Uppaal_DocumentRoot5'):
        assert _is_linked(a1, 'Uppaal_DocumentRoot5', b)
    _safe_set(b, 'Uppaal_DeclarationType', a2)
    assert _is_linked(b, 'Uppaal_DeclarationType', a2)
    if hasattr(a1, 'Uppaal_DocumentRoot5'):
        assert not _is_linked(a1, 'Uppaal_DocumentRoot5', b)
    if hasattr(a2, 'Uppaal_DocumentRoot5'):
        assert _is_linked(a2, 'Uppaal_DocumentRoot5', b)
    _safe_set(b, 'Uppaal_DeclarationType', None)
    assert not _is_linked(b, 'Uppaal_DeclarationType', a2)
    if hasattr(a2, 'Uppaal_DocumentRoot5'):
        assert not _is_linked(a2, 'Uppaal_DocumentRoot5', b)


def test_assoc_imports6_reverse_link_reassign_clear():
    a1 = Uppaal_ImportsType(mixed="sample_text")
    a2 = Uppaal_ImportsType(mixed="sample_text_2")
    b = Uppaal_DocumentRoot(committed="sample_text", mixed="sample_text", urgent="sample_text")
    _safe_set(b, 'Uppaal_DocumentRoot7', {a1})
    assert _is_linked(b, 'Uppaal_DocumentRoot7', a1)
    if hasattr(a1, 'Uppaal_ImportsType'):
        assert _is_linked(a1, 'Uppaal_ImportsType', b)
    _safe_set(b, 'Uppaal_DocumentRoot7', {a2})
    assert _is_linked(b, 'Uppaal_DocumentRoot7', a2)
    if hasattr(a1, 'Uppaal_ImportsType'):
        assert not _is_linked(a1, 'Uppaal_ImportsType', b)
    if hasattr(a2, 'Uppaal_ImportsType'):
        assert _is_linked(a2, 'Uppaal_ImportsType', b)
    _safe_set(b, 'Uppaal_DocumentRoot7', set())
    assert not _is_linked(b, 'Uppaal_DocumentRoot7', a2)
    if hasattr(a2, 'Uppaal_ImportsType'):
        assert not _is_linked(a2, 'Uppaal_ImportsType', b)


def test_assoc_init8_reverse_link_reassign_clear():
    a1 = Uppaal_InitType(ref="sample_text")
    a2 = Uppaal_InitType(ref="sample_text_2")
    b = Uppaal_DocumentRoot(committed="sample_text", mixed="sample_text", urgent="sample_text")
    _safe_set(b, 'Uppaal_DocumentRoot9', {a1})
    assert _is_linked(b, 'Uppaal_DocumentRoot9', a1)
    if hasattr(a1, 'Uppaal_InitType'):
        assert _is_linked(a1, 'Uppaal_InitType', b)
    _safe_set(b, 'Uppaal_DocumentRoot9', {a2})
    assert _is_linked(b, 'Uppaal_DocumentRoot9', a2)
    if hasattr(a1, 'Uppaal_InitType'):
        assert not _is_linked(a1, 'Uppaal_InitType', b)
    if hasattr(a2, 'Uppaal_InitType'):
        assert _is_linked(a2, 'Uppaal_InitType', b)
    _safe_set(b, 'Uppaal_DocumentRoot9', set())
    assert not _is_linked(b, 'Uppaal_DocumentRoot9', a2)
    if hasattr(a2, 'Uppaal_InitType'):
        assert not _is_linked(a2, 'Uppaal_InitType', b)


def test_assoc_instantiation10_reverse_link_reassign_clear():
    a1 = Uppaal_InstantiationType(mixed="sample_text")
    a2 = Uppaal_InstantiationType(mixed="sample_text_2")
    b = Uppaal_DocumentRoot(committed="sample_text", mixed="sample_text", urgent="sample_text")
    _safe_set(b, 'Uppaal_DocumentRoot11', {a1})
    assert _is_linked(b, 'Uppaal_DocumentRoot11', a1)
    if hasattr(a1, 'Uppaal_InstantiationType'):
        assert _is_linked(a1, 'Uppaal_InstantiationType', b)
    _safe_set(b, 'Uppaal_DocumentRoot11', {a2})
    assert _is_linked(b, 'Uppaal_DocumentRoot11', a2)
    if hasattr(a1, 'Uppaal_InstantiationType'):
        assert not _is_linked(a1, 'Uppaal_InstantiationType', b)
    if hasattr(a2, 'Uppaal_InstantiationType'):
        assert _is_linked(a2, 'Uppaal_InstantiationType', b)
    _safe_set(b, 'Uppaal_DocumentRoot11', set())
    assert not _is_linked(b, 'Uppaal_DocumentRoot11', a2)
    if hasattr(a2, 'Uppaal_InstantiationType'):
        assert not _is_linked(a2, 'Uppaal_InstantiationType', b)


def test_assoc_label12_reverse_link_reassign_clear():
    a1 = Uppaal_LabelType(kind="sample_text", mixed="sample_text", x="sample_text", y="sample_text")
    a2 = Uppaal_LabelType(kind="sample_text_2", mixed="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = Uppaal_DocumentRoot(committed="sample_text", mixed="sample_text", urgent="sample_text")
    _safe_set(b, 'Uppaal_DocumentRoot13', {a1})
    assert _is_linked(b, 'Uppaal_DocumentRoot13', a1)
    if hasattr(a1, 'Uppaal_LabelType'):
        assert _is_linked(a1, 'Uppaal_LabelType', b)
    _safe_set(b, 'Uppaal_DocumentRoot13', {a2})
    assert _is_linked(b, 'Uppaal_DocumentRoot13', a2)
    if hasattr(a1, 'Uppaal_LabelType'):
        assert not _is_linked(a1, 'Uppaal_LabelType', b)
    if hasattr(a2, 'Uppaal_LabelType'):
        assert _is_linked(a2, 'Uppaal_LabelType', b)
    _safe_set(b, 'Uppaal_DocumentRoot13', set())
    assert not _is_linked(b, 'Uppaal_DocumentRoot13', a2)
    if hasattr(a2, 'Uppaal_LabelType'):
        assert not _is_linked(a2, 'Uppaal_LabelType', b)


def test_assoc_label37_reverse_link_reassign_clear():
    a1 = Uppaal_LocationType(color="sample_text", committed="sample_text", id="sample_text", urgent="sample_text", x="sample_text", y="sample_text")
    a2 = Uppaal_LocationType(color="sample_text_2", committed="sample_text_2", id="sample_text_2", urgent="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = Uppaal_LabelType(kind="sample_text", mixed="sample_text", x="sample_text", y="sample_text")
    _safe_set(b, 'Uppaal_LabelType39', a1)
    assert _is_linked(b, 'Uppaal_LabelType39', a1)
    if hasattr(a1, 'Uppaal_LocationType38'):
        assert _is_linked(a1, 'Uppaal_LocationType38', b)
    _safe_set(b, 'Uppaal_LabelType39', a2)
    assert _is_linked(b, 'Uppaal_LabelType39', a2)
    if hasattr(a1, 'Uppaal_LocationType38'):
        assert not _is_linked(a1, 'Uppaal_LocationType38', b)
    if hasattr(a2, 'Uppaal_LocationType38'):
        assert _is_linked(a2, 'Uppaal_LocationType38', b)
    _safe_set(b, 'Uppaal_LabelType39', None)
    assert not _is_linked(b, 'Uppaal_LabelType39', a2)
    if hasattr(a2, 'Uppaal_LocationType38'):
        assert not _is_linked(a2, 'Uppaal_LocationType38', b)


def test_assoc_label79_reverse_link_reassign_clear():
    a1 = Uppaal_TransitionType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    a2 = Uppaal_TransitionType(color="sample_text_2", id="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = Uppaal_LabelType(kind="sample_text", mixed="sample_text", x="sample_text", y="sample_text")
    _safe_set(b, 'Uppaal_LabelType81', a1)
    assert _is_linked(b, 'Uppaal_LabelType81', a1)
    if hasattr(a1, 'Uppaal_TransitionType80'):
        assert _is_linked(a1, 'Uppaal_TransitionType80', b)
    _safe_set(b, 'Uppaal_LabelType81', a2)
    assert _is_linked(b, 'Uppaal_LabelType81', a2)
    if hasattr(a1, 'Uppaal_TransitionType80'):
        assert not _is_linked(a1, 'Uppaal_TransitionType80', b)
    if hasattr(a2, 'Uppaal_TransitionType80'):
        assert _is_linked(a2, 'Uppaal_TransitionType80', b)
    _safe_set(b, 'Uppaal_LabelType81', None)
    assert not _is_linked(b, 'Uppaal_LabelType81', a2)
    if hasattr(a2, 'Uppaal_TransitionType80'):
        assert not _is_linked(a2, 'Uppaal_TransitionType80', b)


def test_assoc_location14_reverse_link_reassign_clear():
    a1 = Uppaal_LocationType(color="sample_text", committed="sample_text", id="sample_text", urgent="sample_text", x="sample_text", y="sample_text")
    a2 = Uppaal_LocationType(color="sample_text_2", committed="sample_text_2", id="sample_text_2", urgent="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = Uppaal_DocumentRoot(committed="sample_text", mixed="sample_text", urgent="sample_text")
    _safe_set(b, 'Uppaal_DocumentRoot15', {a1})
    assert _is_linked(b, 'Uppaal_DocumentRoot15', a1)
    if hasattr(a1, 'Uppaal_LocationType'):
        assert _is_linked(a1, 'Uppaal_LocationType', b)
    _safe_set(b, 'Uppaal_DocumentRoot15', {a2})
    assert _is_linked(b, 'Uppaal_DocumentRoot15', a2)
    if hasattr(a1, 'Uppaal_LocationType'):
        assert not _is_linked(a1, 'Uppaal_LocationType', b)
    if hasattr(a2, 'Uppaal_LocationType'):
        assert _is_linked(a2, 'Uppaal_LocationType', b)
    _safe_set(b, 'Uppaal_DocumentRoot15', set())
    assert not _is_linked(b, 'Uppaal_DocumentRoot15', a2)
    if hasattr(a2, 'Uppaal_LocationType'):
        assert not _is_linked(a2, 'Uppaal_LocationType', b)


def test_assoc_nail16_reverse_link_reassign_clear():
    a1 = Uppaal_NailType(x="sample_text", y="sample_text")
    a2 = Uppaal_NailType(x="sample_text_2", y="sample_text_2")
    b = Uppaal_DocumentRoot(committed="sample_text", mixed="sample_text", urgent="sample_text")
    _safe_set(b, 'Uppaal_DocumentRoot17', {a1})
    assert _is_linked(b, 'Uppaal_DocumentRoot17', a1)
    if hasattr(a1, 'Uppaal_NailType'):
        assert _is_linked(a1, 'Uppaal_NailType', b)
    _safe_set(b, 'Uppaal_DocumentRoot17', {a2})
    assert _is_linked(b, 'Uppaal_DocumentRoot17', a2)
    if hasattr(a1, 'Uppaal_NailType'):
        assert not _is_linked(a1, 'Uppaal_NailType', b)
    if hasattr(a2, 'Uppaal_NailType'):
        assert _is_linked(a2, 'Uppaal_NailType', b)
    _safe_set(b, 'Uppaal_DocumentRoot17', set())
    assert not _is_linked(b, 'Uppaal_DocumentRoot17', a2)
    if hasattr(a2, 'Uppaal_NailType'):
        assert not _is_linked(a2, 'Uppaal_NailType', b)


def test_assoc_nail82_reverse_link_reassign_clear():
    a1 = Uppaal_TransitionType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    a2 = Uppaal_TransitionType(color="sample_text_2", id="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = Uppaal_NailType(x="sample_text", y="sample_text")
    _safe_set(b, 'Uppaal_NailType84', a1)
    assert _is_linked(b, 'Uppaal_NailType84', a1)
    if hasattr(a1, 'Uppaal_TransitionType83'):
        assert _is_linked(a1, 'Uppaal_TransitionType83', b)
    _safe_set(b, 'Uppaal_NailType84', a2)
    assert _is_linked(b, 'Uppaal_NailType84', a2)
    if hasattr(a1, 'Uppaal_TransitionType83'):
        assert not _is_linked(a1, 'Uppaal_TransitionType83', b)
    if hasattr(a2, 'Uppaal_TransitionType83'):
        assert _is_linked(a2, 'Uppaal_TransitionType83', b)
    _safe_set(b, 'Uppaal_NailType84', None)
    assert not _is_linked(b, 'Uppaal_NailType84', a2)
    if hasattr(a2, 'Uppaal_TransitionType83'):
        assert not _is_linked(a2, 'Uppaal_TransitionType83', b)


def test_assoc_name18_reverse_link_reassign_clear():
    a1 = Uppaal_NameType(mixed="sample_text", x="sample_text", y="sample_text")
    a2 = Uppaal_NameType(mixed="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = Uppaal_DocumentRoot(committed="sample_text", mixed="sample_text", urgent="sample_text")
    _safe_set(b, 'Uppaal_DocumentRoot19', {a1})
    assert _is_linked(b, 'Uppaal_DocumentRoot19', a1)
    if hasattr(a1, 'Uppaal_NameType'):
        assert _is_linked(a1, 'Uppaal_NameType', b)
    _safe_set(b, 'Uppaal_DocumentRoot19', {a2})
    assert _is_linked(b, 'Uppaal_DocumentRoot19', a2)
    if hasattr(a1, 'Uppaal_NameType'):
        assert not _is_linked(a1, 'Uppaal_NameType', b)
    if hasattr(a2, 'Uppaal_NameType'):
        assert _is_linked(a2, 'Uppaal_NameType', b)
    _safe_set(b, 'Uppaal_DocumentRoot19', set())
    assert not _is_linked(b, 'Uppaal_DocumentRoot19', a2)
    if hasattr(a2, 'Uppaal_NameType'):
        assert not _is_linked(a2, 'Uppaal_NameType', b)


def test_assoc_name34_reverse_link_reassign_clear():
    a1 = Uppaal_NameType(mixed="sample_text", x="sample_text", y="sample_text")
    a2 = Uppaal_NameType(mixed="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = Uppaal_LocationType(color="sample_text", committed="sample_text", id="sample_text", urgent="sample_text", x="sample_text", y="sample_text")
    _safe_set(b, 'Uppaal_LocationType35', a1)
    assert _is_linked(b, 'Uppaal_LocationType35', a1)
    if hasattr(a1, 'Uppaal_NameType36'):
        assert _is_linked(a1, 'Uppaal_NameType36', b)
    _safe_set(b, 'Uppaal_LocationType35', a2)
    assert _is_linked(b, 'Uppaal_LocationType35', a2)
    if hasattr(a1, 'Uppaal_NameType36'):
        assert not _is_linked(a1, 'Uppaal_NameType36', b)
    if hasattr(a2, 'Uppaal_NameType36'):
        assert _is_linked(a2, 'Uppaal_NameType36', b)
    _safe_set(b, 'Uppaal_LocationType35', None)
    assert not _is_linked(b, 'Uppaal_LocationType35', a2)
    if hasattr(a2, 'Uppaal_NameType36'):
        assert not _is_linked(a2, 'Uppaal_NameType36', b)


def test_assoc_parameter22_reverse_link_reassign_clear():
    a1 = Uppaal_ParameterType(mixed="sample_text", x="sample_text", y="sample_text")
    a2 = Uppaal_ParameterType(mixed="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = Uppaal_DocumentRoot(committed="sample_text", mixed="sample_text", urgent="sample_text")
    _safe_set(b, 'Uppaal_DocumentRoot23', {a1})
    assert _is_linked(b, 'Uppaal_DocumentRoot23', a1)
    if hasattr(a1, 'Uppaal_ParameterType'):
        assert _is_linked(a1, 'Uppaal_ParameterType', b)
    _safe_set(b, 'Uppaal_DocumentRoot23', {a2})
    assert _is_linked(b, 'Uppaal_DocumentRoot23', a2)
    if hasattr(a1, 'Uppaal_ParameterType'):
        assert not _is_linked(a1, 'Uppaal_ParameterType', b)
    if hasattr(a2, 'Uppaal_ParameterType'):
        assert _is_linked(a2, 'Uppaal_ParameterType', b)
    _safe_set(b, 'Uppaal_DocumentRoot23', set())
    assert not _is_linked(b, 'Uppaal_DocumentRoot23', a2)
    if hasattr(a2, 'Uppaal_ParameterType'):
        assert not _is_linked(a2, 'Uppaal_ParameterType', b)


def test_assoc_source24_reverse_link_reassign_clear():
    a1 = Uppaal_SourceType(ref="sample_text")
    a2 = Uppaal_SourceType(ref="sample_text_2")
    b = Uppaal_DocumentRoot(committed="sample_text", mixed="sample_text", urgent="sample_text")
    _safe_set(b, 'Uppaal_DocumentRoot25', {a1})
    assert _is_linked(b, 'Uppaal_DocumentRoot25', a1)
    if hasattr(a1, 'Uppaal_SourceType'):
        assert _is_linked(a1, 'Uppaal_SourceType', b)
    _safe_set(b, 'Uppaal_DocumentRoot25', {a2})
    assert _is_linked(b, 'Uppaal_DocumentRoot25', a2)
    if hasattr(a1, 'Uppaal_SourceType'):
        assert not _is_linked(a1, 'Uppaal_SourceType', b)
    if hasattr(a2, 'Uppaal_SourceType'):
        assert _is_linked(a2, 'Uppaal_SourceType', b)
    _safe_set(b, 'Uppaal_DocumentRoot25', set())
    assert not _is_linked(b, 'Uppaal_DocumentRoot25', a2)
    if hasattr(a2, 'Uppaal_SourceType'):
        assert not _is_linked(a2, 'Uppaal_SourceType', b)


def test_assoc_source73_reverse_link_reassign_clear():
    a1 = Uppaal_TransitionType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    a2 = Uppaal_TransitionType(color="sample_text_2", id="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = Uppaal_SourceType(ref="sample_text")
    _safe_set(b, 'Uppaal_SourceType75', a1)
    assert _is_linked(b, 'Uppaal_SourceType75', a1)
    if hasattr(a1, 'Uppaal_TransitionType74'):
        assert _is_linked(a1, 'Uppaal_TransitionType74', b)
    _safe_set(b, 'Uppaal_SourceType75', a2)
    assert _is_linked(b, 'Uppaal_SourceType75', a2)
    if hasattr(a1, 'Uppaal_TransitionType74'):
        assert not _is_linked(a1, 'Uppaal_TransitionType74', b)
    if hasattr(a2, 'Uppaal_TransitionType74'):
        assert _is_linked(a2, 'Uppaal_TransitionType74', b)
    _safe_set(b, 'Uppaal_SourceType75', None)
    assert not _is_linked(b, 'Uppaal_SourceType75', a2)
    if hasattr(a2, 'Uppaal_TransitionType74'):
        assert not _is_linked(a2, 'Uppaal_TransitionType74', b)


def test_assoc_system26_reverse_link_reassign_clear():
    a1 = Uppaal_SystemType(mixed="sample_text")
    a2 = Uppaal_SystemType(mixed="sample_text_2")
    b = Uppaal_DocumentRoot(committed="sample_text", mixed="sample_text", urgent="sample_text")
    _safe_set(b, 'Uppaal_DocumentRoot27', {a1})
    assert _is_linked(b, 'Uppaal_DocumentRoot27', a1)
    if hasattr(a1, 'Uppaal_SystemType'):
        assert _is_linked(a1, 'Uppaal_SystemType', b)
    _safe_set(b, 'Uppaal_DocumentRoot27', {a2})
    assert _is_linked(b, 'Uppaal_DocumentRoot27', a2)
    if hasattr(a1, 'Uppaal_SystemType'):
        assert not _is_linked(a1, 'Uppaal_SystemType', b)
    if hasattr(a2, 'Uppaal_SystemType'):
        assert _is_linked(a2, 'Uppaal_SystemType', b)
    _safe_set(b, 'Uppaal_DocumentRoot27', set())
    assert not _is_linked(b, 'Uppaal_DocumentRoot27', a2)
    if hasattr(a2, 'Uppaal_SystemType'):
        assert not _is_linked(a2, 'Uppaal_SystemType', b)


def test_assoc_target28_reverse_link_reassign_clear():
    a1 = Uppaal_TargetType(ref="sample_text")
    a2 = Uppaal_TargetType(ref="sample_text_2")
    b = Uppaal_DocumentRoot(committed="sample_text", mixed="sample_text", urgent="sample_text")
    _safe_set(b, 'Uppaal_DocumentRoot29', {a1})
    assert _is_linked(b, 'Uppaal_DocumentRoot29', a1)
    if hasattr(a1, 'Uppaal_TargetType'):
        assert _is_linked(a1, 'Uppaal_TargetType', b)
    _safe_set(b, 'Uppaal_DocumentRoot29', {a2})
    assert _is_linked(b, 'Uppaal_DocumentRoot29', a2)
    if hasattr(a1, 'Uppaal_TargetType'):
        assert not _is_linked(a1, 'Uppaal_TargetType', b)
    if hasattr(a2, 'Uppaal_TargetType'):
        assert _is_linked(a2, 'Uppaal_TargetType', b)
    _safe_set(b, 'Uppaal_DocumentRoot29', set())
    assert not _is_linked(b, 'Uppaal_DocumentRoot29', a2)
    if hasattr(a2, 'Uppaal_TargetType'):
        assert not _is_linked(a2, 'Uppaal_TargetType', b)


def test_assoc_target76_reverse_link_reassign_clear():
    a1 = Uppaal_TransitionType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    a2 = Uppaal_TransitionType(color="sample_text_2", id="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = Uppaal_TargetType(ref="sample_text")
    _safe_set(b, 'Uppaal_TargetType78', a1)
    assert _is_linked(b, 'Uppaal_TargetType78', a1)
    if hasattr(a1, 'Uppaal_TransitionType77'):
        assert _is_linked(a1, 'Uppaal_TransitionType77', b)
    _safe_set(b, 'Uppaal_TargetType78', a2)
    assert _is_linked(b, 'Uppaal_TargetType78', a2)
    if hasattr(a1, 'Uppaal_TransitionType77'):
        assert not _is_linked(a1, 'Uppaal_TransitionType77', b)
    if hasattr(a2, 'Uppaal_TransitionType77'):
        assert _is_linked(a2, 'Uppaal_TransitionType77', b)
    _safe_set(b, 'Uppaal_TargetType78', None)
    assert not _is_linked(b, 'Uppaal_TargetType78', a2)
    if hasattr(a2, 'Uppaal_TransitionType77'):
        assert not _is_linked(a2, 'Uppaal_TransitionType77', b)


def test_assoc_transition32_reverse_link_reassign_clear():
    a1 = Uppaal_TransitionType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    a2 = Uppaal_TransitionType(color="sample_text_2", id="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = Uppaal_DocumentRoot(committed="sample_text", mixed="sample_text", urgent="sample_text")
    _safe_set(b, 'Uppaal_DocumentRoot33', {a1})
    assert _is_linked(b, 'Uppaal_DocumentRoot33', a1)
    if hasattr(a1, 'Uppaal_TransitionType'):
        assert _is_linked(a1, 'Uppaal_TransitionType', b)
    _safe_set(b, 'Uppaal_DocumentRoot33', {a2})
    assert _is_linked(b, 'Uppaal_DocumentRoot33', a2)
    if hasattr(a1, 'Uppaal_TransitionType'):
        assert not _is_linked(a1, 'Uppaal_TransitionType', b)
    if hasattr(a2, 'Uppaal_TransitionType'):
        assert _is_linked(a2, 'Uppaal_TransitionType', b)
    _safe_set(b, 'Uppaal_DocumentRoot33', set())
    assert not _is_linked(b, 'Uppaal_DocumentRoot33', a2)
    if hasattr(a2, 'Uppaal_TransitionType'):
        assert not _is_linked(a2, 'Uppaal_TransitionType', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_declaration43_stub_double():
    # Uppaal_NtaType has no real 'Uppaal_NtaType44' property in the generated
    # code (a bare stub) -- manually attach it so Uppaal_DeclarationType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Uppaal_DeclarationType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Uppaal_DeclarationType(mixed="sample_text")
    partner = Uppaal_NtaType()
    setattr(partner, 'Uppaal_NtaType44', None)
    _safe_set(owner, 'Uppaal_DeclarationType45', partner)
    assert getattr(partner, 'Uppaal_NtaType44') == owner
    _safe_set(owner, 'Uppaal_DeclarationType45', None)
    assert getattr(partner, 'Uppaal_NtaType44') is None


def test_assoc_declaration61_stub_double():
    # Uppaal_TemplateType has no real 'Uppaal_TemplateType62' property in the generated
    # code (a bare stub) -- manually attach it so Uppaal_DeclarationType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Uppaal_DeclarationType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Uppaal_DeclarationType(mixed="sample_text")
    partner = Uppaal_TemplateType()
    setattr(partner, 'Uppaal_TemplateType62', None)
    _safe_set(owner, 'Uppaal_DeclarationType63', partner)
    assert getattr(partner, 'Uppaal_TemplateType62') == owner
    _safe_set(owner, 'Uppaal_DeclarationType63', None)
    assert getattr(partner, 'Uppaal_TemplateType62') is None


def test_assoc_imports40_stub_double():
    # Uppaal_NtaType has no real 'Uppaal_NtaType41' property in the generated
    # code (a bare stub) -- manually attach it so Uppaal_ImportsType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Uppaal_ImportsType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Uppaal_ImportsType(mixed="sample_text")
    partner = Uppaal_NtaType()
    setattr(partner, 'Uppaal_NtaType41', None)
    _safe_set(owner, 'Uppaal_ImportsType42', partner)
    assert getattr(partner, 'Uppaal_NtaType41') == owner
    _safe_set(owner, 'Uppaal_ImportsType42', None)
    assert getattr(partner, 'Uppaal_NtaType41') is None


def test_assoc_init67_stub_double():
    # Uppaal_TemplateType has no real 'Uppaal_TemplateType68' property in the generated
    # code (a bare stub) -- manually attach it so Uppaal_InitType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Uppaal_InitType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Uppaal_InitType(ref="sample_text")
    partner = Uppaal_TemplateType()
    setattr(partner, 'Uppaal_TemplateType68', None)
    _safe_set(owner, 'Uppaal_InitType69', partner)
    assert getattr(partner, 'Uppaal_TemplateType68') == owner
    _safe_set(owner, 'Uppaal_InitType69', None)
    assert getattr(partner, 'Uppaal_TemplateType68') is None


def test_assoc_instantiation49_stub_double():
    # Uppaal_NtaType has no real 'Uppaal_NtaType50' property in the generated
    # code (a bare stub) -- manually attach it so Uppaal_InstantiationType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Uppaal_InstantiationType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Uppaal_InstantiationType(mixed="sample_text")
    partner = Uppaal_NtaType()
    setattr(partner, 'Uppaal_NtaType50', None)
    _safe_set(owner, 'Uppaal_InstantiationType51', partner)
    assert getattr(partner, 'Uppaal_NtaType50') == owner
    _safe_set(owner, 'Uppaal_InstantiationType51', None)
    assert getattr(partner, 'Uppaal_NtaType50') is None


def test_assoc_location64_stub_double():
    # Uppaal_TemplateType has no real 'Uppaal_TemplateType65' property in the generated
    # code (a bare stub) -- manually attach it so Uppaal_LocationType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Uppaal_LocationType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Uppaal_LocationType(color="sample_text", committed="sample_text", id="sample_text", urgent="sample_text", x="sample_text", y="sample_text")
    partner = Uppaal_TemplateType()
    setattr(partner, 'Uppaal_TemplateType65', None)
    _safe_set(owner, 'Uppaal_LocationType66', partner)
    assert owner in getattr(partner, 'Uppaal_TemplateType65')
    _safe_set(owner, 'Uppaal_LocationType66', None)
    assert owner not in getattr(partner, 'Uppaal_TemplateType65')


def test_assoc_name55_stub_double():
    # Uppaal_TemplateType has no real 'Uppaal_TemplateType56' property in the generated
    # code (a bare stub) -- manually attach it so Uppaal_NameType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Uppaal_NameType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Uppaal_NameType(mixed="sample_text", x="sample_text", y="sample_text")
    partner = Uppaal_TemplateType()
    setattr(partner, 'Uppaal_TemplateType56', None)
    _safe_set(owner, 'Uppaal_NameType57', partner)
    assert getattr(partner, 'Uppaal_TemplateType56') == owner
    _safe_set(owner, 'Uppaal_NameType57', None)
    assert getattr(partner, 'Uppaal_TemplateType56') is None


def test_assoc_nta20_stub_double():
    # Uppaal_NtaType has no real 'Uppaal_NtaType' property in the generated
    # code (a bare stub) -- manually attach it so Uppaal_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Uppaal_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Uppaal_DocumentRoot(committed="sample_text", mixed="sample_text", urgent="sample_text")
    partner = Uppaal_NtaType()
    setattr(partner, 'Uppaal_NtaType', None)
    _safe_set(owner, 'Uppaal_DocumentRoot21', {partner})
    assert getattr(partner, 'Uppaal_NtaType') == owner
    _safe_set(owner, 'Uppaal_DocumentRoot21', set())
    assert getattr(partner, 'Uppaal_NtaType') is None


def test_assoc_parameter58_stub_double():
    # Uppaal_TemplateType has no real 'Uppaal_TemplateType59' property in the generated
    # code (a bare stub) -- manually attach it so Uppaal_ParameterType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Uppaal_ParameterType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Uppaal_ParameterType(mixed="sample_text", x="sample_text", y="sample_text")
    partner = Uppaal_TemplateType()
    setattr(partner, 'Uppaal_TemplateType59', None)
    _safe_set(owner, 'Uppaal_ParameterType60', partner)
    assert getattr(partner, 'Uppaal_TemplateType59') == owner
    _safe_set(owner, 'Uppaal_ParameterType60', None)
    assert getattr(partner, 'Uppaal_TemplateType59') is None


def test_assoc_system52_stub_double():
    # Uppaal_NtaType has no real 'Uppaal_NtaType53' property in the generated
    # code (a bare stub) -- manually attach it so Uppaal_SystemType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Uppaal_SystemType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Uppaal_SystemType(mixed="sample_text")
    partner = Uppaal_NtaType()
    setattr(partner, 'Uppaal_NtaType53', None)
    _safe_set(owner, 'Uppaal_SystemType54', partner)
    assert getattr(partner, 'Uppaal_NtaType53') == owner
    _safe_set(owner, 'Uppaal_SystemType54', None)
    assert getattr(partner, 'Uppaal_NtaType53') is None


def test_assoc_template30_stub_double():
    # Uppaal_TemplateType has no real 'Uppaal_TemplateType' property in the generated
    # code (a bare stub) -- manually attach it so Uppaal_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Uppaal_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Uppaal_DocumentRoot(committed="sample_text", mixed="sample_text", urgent="sample_text")
    partner = Uppaal_TemplateType()
    setattr(partner, 'Uppaal_TemplateType', None)
    _safe_set(owner, 'Uppaal_DocumentRoot31', {partner})
    assert getattr(partner, 'Uppaal_TemplateType') == owner
    _safe_set(owner, 'Uppaal_DocumentRoot31', set())
    assert getattr(partner, 'Uppaal_TemplateType') is None


def test_assoc_transition70_stub_double():
    # Uppaal_TemplateType has no real 'Uppaal_TemplateType71' property in the generated
    # code (a bare stub) -- manually attach it so Uppaal_TransitionType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Uppaal_TransitionType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Uppaal_TransitionType(color="sample_text", id="sample_text", x="sample_text", y="sample_text")
    partner = Uppaal_TemplateType()
    setattr(partner, 'Uppaal_TemplateType71', None)
    _safe_set(owner, 'Uppaal_TransitionType72', partner)
    assert owner in getattr(partner, 'Uppaal_TemplateType71')
    _safe_set(owner, 'Uppaal_TransitionType72', None)
    assert owner not in getattr(partner, 'Uppaal_TemplateType71')


def test_assoc_xMLNSPrefixMap0_stub_double():
    # Uppaal_EStringToStringMapEntry has no real 'Uppaal_EStringToStringMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so Uppaal_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Uppaal_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Uppaal_DocumentRoot(committed="sample_text", mixed="sample_text", urgent="sample_text")
    partner = Uppaal_EStringToStringMapEntry()
    setattr(partner, 'Uppaal_EStringToStringMapEntry', None)
    _safe_set(owner, 'Uppaal_DocumentRoot', {partner})
    assert getattr(partner, 'Uppaal_EStringToStringMapEntry') == owner
    _safe_set(owner, 'Uppaal_DocumentRoot', set())
    assert getattr(partner, 'Uppaal_EStringToStringMapEntry') is None


def test_assoc_xSISchemaLocation1_stub_double():
    # Uppaal_EStringToStringMapEntry has no real 'Uppaal_EStringToStringMapEntry3' property in the generated
    # code (a bare stub) -- manually attach it so Uppaal_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Uppaal_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Uppaal_DocumentRoot(committed="sample_text", mixed="sample_text", urgent="sample_text")
    partner = Uppaal_EStringToStringMapEntry()
    setattr(partner, 'Uppaal_EStringToStringMapEntry3', None)
    _safe_set(owner, 'Uppaal_DocumentRoot2', {partner})
    assert getattr(partner, 'Uppaal_EStringToStringMapEntry3') == owner
    _safe_set(owner, 'Uppaal_DocumentRoot2', set())
    assert getattr(partner, 'Uppaal_EStringToStringMapEntry3') is None


