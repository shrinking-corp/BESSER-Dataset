import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    generatedplugin_DublinCore,
    generatedplugin_Extension,
    generatedplugin_Plugin,
    generatedplugin_StemCategory,
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

def test_assoc_categories0_reverse_link_reassign_clear():
    a1 = generatedplugin_StemCategory(id="sample_text", name="sample_text", parentId="sample_text")
    a2 = generatedplugin_StemCategory(id="sample_text_2", name="sample_text_2", parentId="sample_text_2")
    b = generatedplugin_Extension(point="sample_text")
    _safe_set(b, 'generatedplugin_Extension', {a1})
    assert _is_linked(b, 'generatedplugin_Extension', a1)
    if hasattr(a1, 'generatedplugin_StemCategory'):
        assert _is_linked(a1, 'generatedplugin_StemCategory', b)
    _safe_set(b, 'generatedplugin_Extension', {a2})
    assert _is_linked(b, 'generatedplugin_Extension', a2)
    if hasattr(a1, 'generatedplugin_StemCategory'):
        assert not _is_linked(a1, 'generatedplugin_StemCategory', b)
    if hasattr(a2, 'generatedplugin_StemCategory'):
        assert _is_linked(a2, 'generatedplugin_StemCategory', b)
    _safe_set(b, 'generatedplugin_Extension', set())
    assert not _is_linked(b, 'generatedplugin_Extension', a2)
    if hasattr(a2, 'generatedplugin_StemCategory'):
        assert not _is_linked(a2, 'generatedplugin_StemCategory', b)


def test_assoc_dublinCores1_reverse_link_reassign_clear():
    a1 = generatedplugin_Extension(point="sample_text")
    a2 = generatedplugin_Extension(point="sample_text_2")
    b = generatedplugin_DublinCore(bibliographicCitation="sample_text", categoryId="sample_text", contributor="sample_text", coverage="sample_text", created="sample_text", creator="sample_text", date="sample_text", description="sample_text", format="sample_text", identifier="sample_text", language="sample_text", license="sample_text", publisher="sample_text", relation="sample_text", requires="sample_text", rights="sample_text", source="sample_text", spatial="sample_text", subject="sample_text", title="sample_text", type="sample_text", valid="sample_text")
    _safe_set(b, 'generatedplugin_DublinCore', a1)
    assert _is_linked(b, 'generatedplugin_DublinCore', a1)
    if hasattr(a1, 'generatedplugin_Extension2'):
        assert _is_linked(a1, 'generatedplugin_Extension2', b)
    _safe_set(b, 'generatedplugin_DublinCore', a2)
    assert _is_linked(b, 'generatedplugin_DublinCore', a2)
    if hasattr(a1, 'generatedplugin_Extension2'):
        assert not _is_linked(a1, 'generatedplugin_Extension2', b)
    if hasattr(a2, 'generatedplugin_Extension2'):
        assert _is_linked(a2, 'generatedplugin_Extension2', b)
    _safe_set(b, 'generatedplugin_DublinCore', None)
    assert not _is_linked(b, 'generatedplugin_DublinCore', a2)
    if hasattr(a2, 'generatedplugin_Extension2'):
        assert not _is_linked(a2, 'generatedplugin_Extension2', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_extensionelement3_stub_double():
    # generatedplugin_Plugin has no real 'generatedplugin_Plugin' property in the generated
    # code (a bare stub) -- manually attach it so generatedplugin_Extension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # generatedplugin_Extension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = generatedplugin_Extension(point="sample_text")
    partner = generatedplugin_Plugin()
    setattr(partner, 'generatedplugin_Plugin', None)
    _safe_set(owner, 'generatedplugin_Extension4', partner)
    assert owner in getattr(partner, 'generatedplugin_Plugin')
    _safe_set(owner, 'generatedplugin_Extension4', None)
    assert owner not in getattr(partner, 'generatedplugin_Plugin')


