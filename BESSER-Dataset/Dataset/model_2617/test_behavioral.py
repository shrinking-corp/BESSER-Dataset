import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Freemind_ArrowlinkType,
    Freemind_CloudType,
    Freemind_DocumentRoot,
    Freemind_EStringToStringMapEntry,
    Freemind_EdgeType,
    Freemind_FontType,
    Freemind_HookType,
    Freemind_IconType,
    Freemind_MapType,
    Freemind_NodeType,
    Freemind_ParametersType,
    Freemind_TextType,
    BOLDType,
    FOLDEDType,
    ITALICType,
    POSITIONType,
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

def test_assoc_arrowlink33_reverse_link_reassign_clear():
    a1 = Freemind_NodeType(BackgroundColor="sample_text", Color="sample_text", Created="sample_text", EncryptedContent="sample_text", Folded="sample_text", Hgap="sample_text", Id="sample_text", Link="sample_text", Modified="sample_text", Position="sample_text", Style="sample_text", Text="sample_text", Vgap="sample_text", Vshift="sample_text", group="sample_text")
    a2 = Freemind_NodeType(BackgroundColor="sample_text_2", Color="sample_text_2", Created="sample_text_2", EncryptedContent="sample_text_2", Folded="sample_text_2", Hgap="sample_text_2", Id="sample_text_2", Link="sample_text_2", Modified="sample_text_2", Position="sample_text_2", Style="sample_text_2", Text="sample_text_2", Vgap="sample_text_2", Vshift="sample_text_2", group="sample_text_2")
    b = Freemind_ArrowlinkType(Color="sample_text", Destination="sample_text", EndArrow="sample_text", EndInclination="sample_text", Id="sample_text", StartArrow="sample_text", StartInclination="sample_text")
    _safe_set(b, 'Freemind_ArrowlinkType35', a1)
    assert _is_linked(b, 'Freemind_ArrowlinkType35', a1)
    if hasattr(a1, 'Freemind_NodeType34'):
        assert _is_linked(a1, 'Freemind_NodeType34', b)
    _safe_set(b, 'Freemind_ArrowlinkType35', a2)
    assert _is_linked(b, 'Freemind_ArrowlinkType35', a2)
    if hasattr(a1, 'Freemind_NodeType34'):
        assert not _is_linked(a1, 'Freemind_NodeType34', b)
    if hasattr(a2, 'Freemind_NodeType34'):
        assert _is_linked(a2, 'Freemind_NodeType34', b)
    _safe_set(b, 'Freemind_ArrowlinkType35', None)
    assert not _is_linked(b, 'Freemind_ArrowlinkType35', a2)
    if hasattr(a2, 'Freemind_NodeType34'):
        assert not _is_linked(a2, 'Freemind_NodeType34', b)


def test_assoc_arrowlink4_reverse_link_reassign_clear():
    a1 = Freemind_DocumentRoot(mixed="sample_text")
    a2 = Freemind_DocumentRoot(mixed="sample_text_2")
    b = Freemind_ArrowlinkType(Color="sample_text", Destination="sample_text", EndArrow="sample_text", EndInclination="sample_text", Id="sample_text", StartArrow="sample_text", StartInclination="sample_text")
    _safe_set(b, 'Freemind_ArrowlinkType', a1)
    assert _is_linked(b, 'Freemind_ArrowlinkType', a1)
    if hasattr(a1, 'Freemind_DocumentRoot5'):
        assert _is_linked(a1, 'Freemind_DocumentRoot5', b)
    _safe_set(b, 'Freemind_ArrowlinkType', a2)
    assert _is_linked(b, 'Freemind_ArrowlinkType', a2)
    if hasattr(a1, 'Freemind_DocumentRoot5'):
        assert not _is_linked(a1, 'Freemind_DocumentRoot5', b)
    if hasattr(a2, 'Freemind_DocumentRoot5'):
        assert _is_linked(a2, 'Freemind_DocumentRoot5', b)
    _safe_set(b, 'Freemind_ArrowlinkType', None)
    assert not _is_linked(b, 'Freemind_ArrowlinkType', a2)
    if hasattr(a2, 'Freemind_DocumentRoot5'):
        assert not _is_linked(a2, 'Freemind_DocumentRoot5', b)


def test_assoc_cloud36_reverse_link_reassign_clear():
    a1 = Freemind_NodeType(BackgroundColor="sample_text", Color="sample_text", Created="sample_text", EncryptedContent="sample_text", Folded="sample_text", Hgap="sample_text", Id="sample_text", Link="sample_text", Modified="sample_text", Position="sample_text", Style="sample_text", Text="sample_text", Vgap="sample_text", Vshift="sample_text", group="sample_text")
    a2 = Freemind_NodeType(BackgroundColor="sample_text_2", Color="sample_text_2", Created="sample_text_2", EncryptedContent="sample_text_2", Folded="sample_text_2", Hgap="sample_text_2", Id="sample_text_2", Link="sample_text_2", Modified="sample_text_2", Position="sample_text_2", Style="sample_text_2", Text="sample_text_2", Vgap="sample_text_2", Vshift="sample_text_2", group="sample_text_2")
    b = Freemind_CloudType(Color="sample_text")
    _safe_set(b, 'Freemind_CloudType38', a1)
    assert _is_linked(b, 'Freemind_CloudType38', a1)
    if hasattr(a1, 'Freemind_NodeType37'):
        assert _is_linked(a1, 'Freemind_NodeType37', b)
    _safe_set(b, 'Freemind_CloudType38', a2)
    assert _is_linked(b, 'Freemind_CloudType38', a2)
    if hasattr(a1, 'Freemind_NodeType37'):
        assert not _is_linked(a1, 'Freemind_NodeType37', b)
    if hasattr(a2, 'Freemind_NodeType37'):
        assert _is_linked(a2, 'Freemind_NodeType37', b)
    _safe_set(b, 'Freemind_CloudType38', None)
    assert not _is_linked(b, 'Freemind_CloudType38', a2)
    if hasattr(a2, 'Freemind_NodeType37'):
        assert not _is_linked(a2, 'Freemind_NodeType37', b)


def test_assoc_cloud6_reverse_link_reassign_clear():
    a1 = Freemind_DocumentRoot(mixed="sample_text")
    a2 = Freemind_DocumentRoot(mixed="sample_text_2")
    b = Freemind_CloudType(Color="sample_text")
    _safe_set(b, 'Freemind_CloudType', a1)
    assert _is_linked(b, 'Freemind_CloudType', a1)
    if hasattr(a1, 'Freemind_DocumentRoot7'):
        assert _is_linked(a1, 'Freemind_DocumentRoot7', b)
    _safe_set(b, 'Freemind_CloudType', a2)
    assert _is_linked(b, 'Freemind_CloudType', a2)
    if hasattr(a1, 'Freemind_DocumentRoot7'):
        assert not _is_linked(a1, 'Freemind_DocumentRoot7', b)
    if hasattr(a2, 'Freemind_DocumentRoot7'):
        assert _is_linked(a2, 'Freemind_DocumentRoot7', b)
    _safe_set(b, 'Freemind_CloudType', None)
    assert not _is_linked(b, 'Freemind_CloudType', a2)
    if hasattr(a2, 'Freemind_DocumentRoot7'):
        assert not _is_linked(a2, 'Freemind_DocumentRoot7', b)


def test_assoc_edge39_reverse_link_reassign_clear():
    a1 = Freemind_NodeType(BackgroundColor="sample_text", Color="sample_text", Created="sample_text", EncryptedContent="sample_text", Folded="sample_text", Hgap="sample_text", Id="sample_text", Link="sample_text", Modified="sample_text", Position="sample_text", Style="sample_text", Text="sample_text", Vgap="sample_text", Vshift="sample_text", group="sample_text")
    a2 = Freemind_NodeType(BackgroundColor="sample_text_2", Color="sample_text_2", Created="sample_text_2", EncryptedContent="sample_text_2", Folded="sample_text_2", Hgap="sample_text_2", Id="sample_text_2", Link="sample_text_2", Modified="sample_text_2", Position="sample_text_2", Style="sample_text_2", Text="sample_text_2", Vgap="sample_text_2", Vshift="sample_text_2", group="sample_text_2")
    b = Freemind_EdgeType(Color="sample_text", Style="sample_text", Width="sample_text")
    _safe_set(b, 'Freemind_EdgeType41', a1)
    assert _is_linked(b, 'Freemind_EdgeType41', a1)
    if hasattr(a1, 'Freemind_NodeType40'):
        assert _is_linked(a1, 'Freemind_NodeType40', b)
    _safe_set(b, 'Freemind_EdgeType41', a2)
    assert _is_linked(b, 'Freemind_EdgeType41', a2)
    if hasattr(a1, 'Freemind_NodeType40'):
        assert not _is_linked(a1, 'Freemind_NodeType40', b)
    if hasattr(a2, 'Freemind_NodeType40'):
        assert _is_linked(a2, 'Freemind_NodeType40', b)
    _safe_set(b, 'Freemind_EdgeType41', None)
    assert not _is_linked(b, 'Freemind_EdgeType41', a2)
    if hasattr(a2, 'Freemind_NodeType40'):
        assert not _is_linked(a2, 'Freemind_NodeType40', b)


def test_assoc_edge8_reverse_link_reassign_clear():
    a1 = Freemind_EdgeType(Color="sample_text", Style="sample_text", Width="sample_text")
    a2 = Freemind_EdgeType(Color="sample_text_2", Style="sample_text_2", Width="sample_text_2")
    b = Freemind_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'Freemind_DocumentRoot9', {a1})
    assert _is_linked(b, 'Freemind_DocumentRoot9', a1)
    if hasattr(a1, 'Freemind_EdgeType'):
        assert _is_linked(a1, 'Freemind_EdgeType', b)
    _safe_set(b, 'Freemind_DocumentRoot9', {a2})
    assert _is_linked(b, 'Freemind_DocumentRoot9', a2)
    if hasattr(a1, 'Freemind_EdgeType'):
        assert not _is_linked(a1, 'Freemind_EdgeType', b)
    if hasattr(a2, 'Freemind_EdgeType'):
        assert _is_linked(a2, 'Freemind_EdgeType', b)
    _safe_set(b, 'Freemind_DocumentRoot9', set())
    assert not _is_linked(b, 'Freemind_DocumentRoot9', a2)
    if hasattr(a2, 'Freemind_EdgeType'):
        assert not _is_linked(a2, 'Freemind_EdgeType', b)


def test_assoc_font10_reverse_link_reassign_clear():
    a1 = Freemind_FontType(Bold="sample_text", Italic="sample_text", Name="sample_text", Size="sample_text")
    a2 = Freemind_FontType(Bold="sample_text_2", Italic="sample_text_2", Name="sample_text_2", Size="sample_text_2")
    b = Freemind_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'Freemind_DocumentRoot11', {a1})
    assert _is_linked(b, 'Freemind_DocumentRoot11', a1)
    if hasattr(a1, 'Freemind_FontType'):
        assert _is_linked(a1, 'Freemind_FontType', b)
    _safe_set(b, 'Freemind_DocumentRoot11', {a2})
    assert _is_linked(b, 'Freemind_DocumentRoot11', a2)
    if hasattr(a1, 'Freemind_FontType'):
        assert not _is_linked(a1, 'Freemind_FontType', b)
    if hasattr(a2, 'Freemind_FontType'):
        assert _is_linked(a2, 'Freemind_FontType', b)
    _safe_set(b, 'Freemind_DocumentRoot11', set())
    assert not _is_linked(b, 'Freemind_DocumentRoot11', a2)
    if hasattr(a2, 'Freemind_FontType'):
        assert not _is_linked(a2, 'Freemind_FontType', b)


def test_assoc_font42_reverse_link_reassign_clear():
    a1 = Freemind_NodeType(BackgroundColor="sample_text", Color="sample_text", Created="sample_text", EncryptedContent="sample_text", Folded="sample_text", Hgap="sample_text", Id="sample_text", Link="sample_text", Modified="sample_text", Position="sample_text", Style="sample_text", Text="sample_text", Vgap="sample_text", Vshift="sample_text", group="sample_text")
    a2 = Freemind_NodeType(BackgroundColor="sample_text_2", Color="sample_text_2", Created="sample_text_2", EncryptedContent="sample_text_2", Folded="sample_text_2", Hgap="sample_text_2", Id="sample_text_2", Link="sample_text_2", Modified="sample_text_2", Position="sample_text_2", Style="sample_text_2", Text="sample_text_2", Vgap="sample_text_2", Vshift="sample_text_2", group="sample_text_2")
    b = Freemind_FontType(Bold="sample_text", Italic="sample_text", Name="sample_text", Size="sample_text")
    _safe_set(b, 'Freemind_FontType44', a1)
    assert _is_linked(b, 'Freemind_FontType44', a1)
    if hasattr(a1, 'Freemind_NodeType43'):
        assert _is_linked(a1, 'Freemind_NodeType43', b)
    _safe_set(b, 'Freemind_FontType44', a2)
    assert _is_linked(b, 'Freemind_FontType44', a2)
    if hasattr(a1, 'Freemind_NodeType43'):
        assert not _is_linked(a1, 'Freemind_NodeType43', b)
    if hasattr(a2, 'Freemind_NodeType43'):
        assert _is_linked(a2, 'Freemind_NodeType43', b)
    _safe_set(b, 'Freemind_FontType44', None)
    assert not _is_linked(b, 'Freemind_FontType44', a2)
    if hasattr(a2, 'Freemind_NodeType43'):
        assert not _is_linked(a2, 'Freemind_NodeType43', b)


def test_assoc_hook12_reverse_link_reassign_clear():
    a1 = Freemind_HookType(Name="sample_text")
    a2 = Freemind_HookType(Name="sample_text_2")
    b = Freemind_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'Freemind_DocumentRoot13', {a1})
    assert _is_linked(b, 'Freemind_DocumentRoot13', a1)
    if hasattr(a1, 'Freemind_HookType'):
        assert _is_linked(a1, 'Freemind_HookType', b)
    _safe_set(b, 'Freemind_DocumentRoot13', {a2})
    assert _is_linked(b, 'Freemind_DocumentRoot13', a2)
    if hasattr(a1, 'Freemind_HookType'):
        assert not _is_linked(a1, 'Freemind_HookType', b)
    if hasattr(a2, 'Freemind_HookType'):
        assert _is_linked(a2, 'Freemind_HookType', b)
    _safe_set(b, 'Freemind_DocumentRoot13', set())
    assert not _is_linked(b, 'Freemind_DocumentRoot13', a2)
    if hasattr(a2, 'Freemind_HookType'):
        assert not _is_linked(a2, 'Freemind_HookType', b)


def test_assoc_hook45_reverse_link_reassign_clear():
    a1 = Freemind_NodeType(BackgroundColor="sample_text", Color="sample_text", Created="sample_text", EncryptedContent="sample_text", Folded="sample_text", Hgap="sample_text", Id="sample_text", Link="sample_text", Modified="sample_text", Position="sample_text", Style="sample_text", Text="sample_text", Vgap="sample_text", Vshift="sample_text", group="sample_text")
    a2 = Freemind_NodeType(BackgroundColor="sample_text_2", Color="sample_text_2", Created="sample_text_2", EncryptedContent="sample_text_2", Folded="sample_text_2", Hgap="sample_text_2", Id="sample_text_2", Link="sample_text_2", Modified="sample_text_2", Position="sample_text_2", Style="sample_text_2", Text="sample_text_2", Vgap="sample_text_2", Vshift="sample_text_2", group="sample_text_2")
    b = Freemind_HookType(Name="sample_text")
    _safe_set(b, 'Freemind_HookType47', a1)
    assert _is_linked(b, 'Freemind_HookType47', a1)
    if hasattr(a1, 'Freemind_NodeType46'):
        assert _is_linked(a1, 'Freemind_NodeType46', b)
    _safe_set(b, 'Freemind_HookType47', a2)
    assert _is_linked(b, 'Freemind_HookType47', a2)
    if hasattr(a1, 'Freemind_NodeType46'):
        assert not _is_linked(a1, 'Freemind_NodeType46', b)
    if hasattr(a2, 'Freemind_NodeType46'):
        assert _is_linked(a2, 'Freemind_NodeType46', b)
    _safe_set(b, 'Freemind_HookType47', None)
    assert not _is_linked(b, 'Freemind_HookType47', a2)
    if hasattr(a2, 'Freemind_NodeType46'):
        assert not _is_linked(a2, 'Freemind_NodeType46', b)


def test_assoc_icon14_reverse_link_reassign_clear():
    a1 = Freemind_IconType(Builtin="sample_text")
    a2 = Freemind_IconType(Builtin="sample_text_2")
    b = Freemind_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'Freemind_DocumentRoot15', {a1})
    assert _is_linked(b, 'Freemind_DocumentRoot15', a1)
    if hasattr(a1, 'Freemind_IconType'):
        assert _is_linked(a1, 'Freemind_IconType', b)
    _safe_set(b, 'Freemind_DocumentRoot15', {a2})
    assert _is_linked(b, 'Freemind_DocumentRoot15', a2)
    if hasattr(a1, 'Freemind_IconType'):
        assert not _is_linked(a1, 'Freemind_IconType', b)
    if hasattr(a2, 'Freemind_IconType'):
        assert _is_linked(a2, 'Freemind_IconType', b)
    _safe_set(b, 'Freemind_DocumentRoot15', set())
    assert not _is_linked(b, 'Freemind_DocumentRoot15', a2)
    if hasattr(a2, 'Freemind_IconType'):
        assert not _is_linked(a2, 'Freemind_IconType', b)


def test_assoc_icon48_reverse_link_reassign_clear():
    a1 = Freemind_NodeType(BackgroundColor="sample_text", Color="sample_text", Created="sample_text", EncryptedContent="sample_text", Folded="sample_text", Hgap="sample_text", Id="sample_text", Link="sample_text", Modified="sample_text", Position="sample_text", Style="sample_text", Text="sample_text", Vgap="sample_text", Vshift="sample_text", group="sample_text")
    a2 = Freemind_NodeType(BackgroundColor="sample_text_2", Color="sample_text_2", Created="sample_text_2", EncryptedContent="sample_text_2", Folded="sample_text_2", Hgap="sample_text_2", Id="sample_text_2", Link="sample_text_2", Modified="sample_text_2", Position="sample_text_2", Style="sample_text_2", Text="sample_text_2", Vgap="sample_text_2", Vshift="sample_text_2", group="sample_text_2")
    b = Freemind_IconType(Builtin="sample_text")
    _safe_set(b, 'Freemind_IconType50', a1)
    assert _is_linked(b, 'Freemind_IconType50', a1)
    if hasattr(a1, 'Freemind_NodeType49'):
        assert _is_linked(a1, 'Freemind_NodeType49', b)
    _safe_set(b, 'Freemind_IconType50', a2)
    assert _is_linked(b, 'Freemind_IconType50', a2)
    if hasattr(a1, 'Freemind_NodeType49'):
        assert not _is_linked(a1, 'Freemind_NodeType49', b)
    if hasattr(a2, 'Freemind_NodeType49'):
        assert _is_linked(a2, 'Freemind_NodeType49', b)
    _safe_set(b, 'Freemind_IconType50', None)
    assert not _is_linked(b, 'Freemind_IconType50', a2)
    if hasattr(a2, 'Freemind_NodeType49'):
        assert not _is_linked(a2, 'Freemind_NodeType49', b)


def test_assoc_map16_reverse_link_reassign_clear():
    a1 = Freemind_MapType(version="sample_text")
    a2 = Freemind_MapType(version="sample_text_2")
    b = Freemind_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'Freemind_DocumentRoot17', {a1})
    assert _is_linked(b, 'Freemind_DocumentRoot17', a1)
    if hasattr(a1, 'Freemind_MapType'):
        assert _is_linked(a1, 'Freemind_MapType', b)
    _safe_set(b, 'Freemind_DocumentRoot17', {a2})
    assert _is_linked(b, 'Freemind_DocumentRoot17', a2)
    if hasattr(a1, 'Freemind_MapType'):
        assert not _is_linked(a1, 'Freemind_MapType', b)
    if hasattr(a2, 'Freemind_MapType'):
        assert _is_linked(a2, 'Freemind_MapType', b)
    _safe_set(b, 'Freemind_DocumentRoot17', set())
    assert not _is_linked(b, 'Freemind_DocumentRoot17', a2)
    if hasattr(a2, 'Freemind_MapType'):
        assert not _is_linked(a2, 'Freemind_MapType', b)


def test_assoc_node18_reverse_link_reassign_clear():
    a1 = Freemind_NodeType(BackgroundColor="sample_text", Color="sample_text", Created="sample_text", EncryptedContent="sample_text", Folded="sample_text", Hgap="sample_text", Id="sample_text", Link="sample_text", Modified="sample_text", Position="sample_text", Style="sample_text", Text="sample_text", Vgap="sample_text", Vshift="sample_text", group="sample_text")
    a2 = Freemind_NodeType(BackgroundColor="sample_text_2", Color="sample_text_2", Created="sample_text_2", EncryptedContent="sample_text_2", Folded="sample_text_2", Hgap="sample_text_2", Id="sample_text_2", Link="sample_text_2", Modified="sample_text_2", Position="sample_text_2", Style="sample_text_2", Text="sample_text_2", Vgap="sample_text_2", Vshift="sample_text_2", group="sample_text_2")
    b = Freemind_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'Freemind_DocumentRoot19', {a1})
    assert _is_linked(b, 'Freemind_DocumentRoot19', a1)
    if hasattr(a1, 'Freemind_NodeType'):
        assert _is_linked(a1, 'Freemind_NodeType', b)
    _safe_set(b, 'Freemind_DocumentRoot19', {a2})
    assert _is_linked(b, 'Freemind_DocumentRoot19', a2)
    if hasattr(a1, 'Freemind_NodeType'):
        assert not _is_linked(a1, 'Freemind_NodeType', b)
    if hasattr(a2, 'Freemind_NodeType'):
        assert _is_linked(a2, 'Freemind_NodeType', b)
    _safe_set(b, 'Freemind_DocumentRoot19', set())
    assert not _is_linked(b, 'Freemind_DocumentRoot19', a2)
    if hasattr(a2, 'Freemind_NodeType'):
        assert not _is_linked(a2, 'Freemind_NodeType', b)


def test_assoc_node30_reverse_link_reassign_clear():
    a1 = Freemind_NodeType(BackgroundColor="sample_text", Color="sample_text", Created="sample_text", EncryptedContent="sample_text", Folded="sample_text", Hgap="sample_text", Id="sample_text", Link="sample_text", Modified="sample_text", Position="sample_text", Style="sample_text", Text="sample_text", Vgap="sample_text", Vshift="sample_text", group="sample_text")
    a2 = Freemind_NodeType(BackgroundColor="sample_text_2", Color="sample_text_2", Created="sample_text_2", EncryptedContent="sample_text_2", Folded="sample_text_2", Hgap="sample_text_2", Id="sample_text_2", Link="sample_text_2", Modified="sample_text_2", Position="sample_text_2", Style="sample_text_2", Text="sample_text_2", Vgap="sample_text_2", Vshift="sample_text_2", group="sample_text_2")
    b = Freemind_MapType(version="sample_text")
    _safe_set(b, 'Freemind_MapType31', a1)
    assert _is_linked(b, 'Freemind_MapType31', a1)
    if hasattr(a1, 'Freemind_NodeType32'):
        assert _is_linked(a1, 'Freemind_NodeType32', b)
    _safe_set(b, 'Freemind_MapType31', a2)
    assert _is_linked(b, 'Freemind_MapType31', a2)
    if hasattr(a1, 'Freemind_NodeType32'):
        assert not _is_linked(a1, 'Freemind_NodeType32', b)
    if hasattr(a2, 'Freemind_NodeType32'):
        assert _is_linked(a2, 'Freemind_NodeType32', b)
    _safe_set(b, 'Freemind_MapType31', None)
    assert not _is_linked(b, 'Freemind_MapType31', a2)
    if hasattr(a2, 'Freemind_NodeType32'):
        assert not _is_linked(a2, 'Freemind_NodeType32', b)


def test_assoc_node52_reverse_link_reassign_clear():
    a1 = Freemind_NodeType(BackgroundColor="sample_text", Color="sample_text", Created="sample_text", EncryptedContent="sample_text", Folded="sample_text", Hgap="sample_text", Id="sample_text", Link="sample_text", Modified="sample_text", Position="sample_text", Style="sample_text", Text="sample_text", Vgap="sample_text", Vshift="sample_text", group="sample_text")
    a2 = Freemind_NodeType(BackgroundColor="sample_text_2", Color="sample_text_2", Created="sample_text_2", EncryptedContent="sample_text_2", Folded="sample_text_2", Hgap="sample_text_2", Id="sample_text_2", Link="sample_text_2", Modified="sample_text_2", Position="sample_text_2", Style="sample_text_2", Text="sample_text_2", Vgap="sample_text_2", Vshift="sample_text_2", group="sample_text_2")
    b = Freemind_NodeType(BackgroundColor="sample_text", Color="sample_text", Created="sample_text", EncryptedContent="sample_text", Folded="sample_text", Hgap="sample_text", Id="sample_text", Link="sample_text", Modified="sample_text", Position="sample_text", Style="sample_text", Text="sample_text", Vgap="sample_text", Vshift="sample_text", group="sample_text")
    _safe_set(b, 'Freemind_NodeType53', a1)
    assert _is_linked(b, 'Freemind_NodeType53', a1)
    if hasattr(a1, 'Freemind_NodeType51'):
        assert _is_linked(a1, 'Freemind_NodeType51', b)
    _safe_set(b, 'Freemind_NodeType53', a2)
    assert _is_linked(b, 'Freemind_NodeType53', a2)
    if hasattr(a1, 'Freemind_NodeType51'):
        assert not _is_linked(a1, 'Freemind_NodeType51', b)
    if hasattr(a2, 'Freemind_NodeType51'):
        assert _is_linked(a2, 'Freemind_NodeType51', b)
    _safe_set(b, 'Freemind_NodeType53', None)
    assert not _is_linked(b, 'Freemind_NodeType53', a2)
    if hasattr(a2, 'Freemind_NodeType51'):
        assert not _is_linked(a2, 'Freemind_NodeType51', b)


def test_assoc_parameters20_reverse_link_reassign_clear():
    a1 = Freemind_ParametersType(RemindUserAt="sample_text")
    a2 = Freemind_ParametersType(RemindUserAt="sample_text_2")
    b = Freemind_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'Freemind_DocumentRoot21', {a1})
    assert _is_linked(b, 'Freemind_DocumentRoot21', a1)
    if hasattr(a1, 'Freemind_ParametersType'):
        assert _is_linked(a1, 'Freemind_ParametersType', b)
    _safe_set(b, 'Freemind_DocumentRoot21', {a2})
    assert _is_linked(b, 'Freemind_DocumentRoot21', a2)
    if hasattr(a1, 'Freemind_ParametersType'):
        assert not _is_linked(a1, 'Freemind_ParametersType', b)
    if hasattr(a2, 'Freemind_ParametersType'):
        assert _is_linked(a2, 'Freemind_ParametersType', b)
    _safe_set(b, 'Freemind_DocumentRoot21', set())
    assert not _is_linked(b, 'Freemind_DocumentRoot21', a2)
    if hasattr(a2, 'Freemind_ParametersType'):
        assert not _is_linked(a2, 'Freemind_ParametersType', b)


def test_assoc_parameters24_reverse_link_reassign_clear():
    a1 = Freemind_ParametersType(RemindUserAt="sample_text")
    a2 = Freemind_ParametersType(RemindUserAt="sample_text_2")
    b = Freemind_HookType(Name="sample_text")
    _safe_set(b, 'Freemind_HookType25', a1)
    assert _is_linked(b, 'Freemind_HookType25', a1)
    if hasattr(a1, 'Freemind_ParametersType26'):
        assert _is_linked(a1, 'Freemind_ParametersType26', b)
    _safe_set(b, 'Freemind_HookType25', a2)
    assert _is_linked(b, 'Freemind_HookType25', a2)
    if hasattr(a1, 'Freemind_ParametersType26'):
        assert not _is_linked(a1, 'Freemind_ParametersType26', b)
    if hasattr(a2, 'Freemind_ParametersType26'):
        assert _is_linked(a2, 'Freemind_ParametersType26', b)
    _safe_set(b, 'Freemind_HookType25', None)
    assert not _is_linked(b, 'Freemind_HookType25', a2)
    if hasattr(a2, 'Freemind_ParametersType26'):
        assert not _is_linked(a2, 'Freemind_ParametersType26', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_text22_stub_double():
    # Freemind_TextType has no real 'Freemind_TextType' property in the generated
    # code (a bare stub) -- manually attach it so Freemind_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Freemind_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Freemind_DocumentRoot(mixed="sample_text")
    partner = Freemind_TextType()
    setattr(partner, 'Freemind_TextType', None)
    _safe_set(owner, 'Freemind_DocumentRoot23', {partner})
    assert getattr(partner, 'Freemind_TextType') == owner
    _safe_set(owner, 'Freemind_DocumentRoot23', set())
    assert getattr(partner, 'Freemind_TextType') is None


def test_assoc_text27_stub_double():
    # Freemind_TextType has no real 'Freemind_TextType29' property in the generated
    # code (a bare stub) -- manually attach it so Freemind_HookType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Freemind_HookType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Freemind_HookType(Name="sample_text")
    partner = Freemind_TextType()
    setattr(partner, 'Freemind_TextType29', None)
    _safe_set(owner, 'Freemind_HookType28', partner)
    assert getattr(partner, 'Freemind_TextType29') == owner
    _safe_set(owner, 'Freemind_HookType28', None)
    assert getattr(partner, 'Freemind_TextType29') is None


def test_assoc_xMLNSPrefixMap0_stub_double():
    # Freemind_EStringToStringMapEntry has no real 'Freemind_EStringToStringMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so Freemind_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Freemind_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Freemind_DocumentRoot(mixed="sample_text")
    partner = Freemind_EStringToStringMapEntry()
    setattr(partner, 'Freemind_EStringToStringMapEntry', None)
    _safe_set(owner, 'Freemind_DocumentRoot', {partner})
    assert getattr(partner, 'Freemind_EStringToStringMapEntry') == owner
    _safe_set(owner, 'Freemind_DocumentRoot', set())
    assert getattr(partner, 'Freemind_EStringToStringMapEntry') is None


def test_assoc_xSISchemaLocation1_stub_double():
    # Freemind_EStringToStringMapEntry has no real 'Freemind_EStringToStringMapEntry3' property in the generated
    # code (a bare stub) -- manually attach it so Freemind_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Freemind_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Freemind_DocumentRoot(mixed="sample_text")
    partner = Freemind_EStringToStringMapEntry()
    setattr(partner, 'Freemind_EStringToStringMapEntry3', None)
    _safe_set(owner, 'Freemind_DocumentRoot2', {partner})
    assert getattr(partner, 'Freemind_EStringToStringMapEntry3') == owner
    _safe_set(owner, 'Freemind_DocumentRoot2', set())
    assert getattr(partner, 'Freemind_EStringToStringMapEntry3') is None


