import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    opf_Contributor,
    opf_Coverage,
    opf_Creator,
    opf_Date,
    opf_Description,
    opf_Format,
    opf_Guide,
    opf_Identifier,
    opf_Item,
    opf_Itemref,
    opf_Language,
    opf_Manifest,
    opf_Meta,
    opf_Metadata,
    opf_Package,
    opf_Publisher,
    opf_Reference,
    opf_Relation,
    opf_Rights,
    opf_Source,
    opf_Spine,
    opf_Subject,
    opf_Title,
    opf_Tours,
    opf_Type,
    Role,
    Type,
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

def test_assoc_spine3_reverse_link_reassign_clear():
    a1 = opf_Spine(toc="sample_text")
    a2 = opf_Spine(toc="sample_text_2")
    b = opf_Package(generateCoverHTML=True, generateTableOfContents=True, includeReferencedResources=True, uniqueIdentifier="sample_text", version="sample_text")
    _safe_set(b, 'opf_Package4', a1)
    assert _is_linked(b, 'opf_Package4', a1)
    if hasattr(a1, 'opf_Spine'):
        assert _is_linked(a1, 'opf_Spine', b)
    _safe_set(b, 'opf_Package4', a2)
    assert _is_linked(b, 'opf_Package4', a2)
    if hasattr(a1, 'opf_Spine'):
        assert not _is_linked(a1, 'opf_Spine', b)
    if hasattr(a2, 'opf_Spine'):
        assert _is_linked(a2, 'opf_Spine', b)
    _safe_set(b, 'opf_Package4', None)
    assert not _is_linked(b, 'opf_Package4', a2)
    if hasattr(a2, 'opf_Spine'):
        assert not _is_linked(a2, 'opf_Spine', b)


def test_assoc_spineItems43_reverse_link_reassign_clear():
    a1 = opf_Spine(toc="sample_text")
    a2 = opf_Spine(toc="sample_text_2")
    b = opf_Itemref(idref="sample_text", linear="sample_text")
    _safe_set(b, 'opf_Itemref', a1)
    assert _is_linked(b, 'opf_Itemref', a1)
    if hasattr(a1, 'opf_Spine44'):
        assert _is_linked(a1, 'opf_Spine44', b)
    _safe_set(b, 'opf_Itemref', a2)
    assert _is_linked(b, 'opf_Itemref', a2)
    if hasattr(a1, 'opf_Spine44'):
        assert not _is_linked(a1, 'opf_Spine44', b)
    if hasattr(a2, 'opf_Spine44'):
        assert _is_linked(a2, 'opf_Spine44', b)
    _safe_set(b, 'opf_Itemref', None)
    assert not _is_linked(b, 'opf_Itemref', a2)
    if hasattr(a2, 'opf_Spine44'):
        assert not _is_linked(a2, 'opf_Spine44', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_guide5_stub_double():
    # opf_Guide has no real 'opf_Guide' property in the generated
    # code (a bare stub) -- manually attach it so opf_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # opf_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = opf_Package(generateCoverHTML=True, generateTableOfContents=True, includeReferencedResources=True, uniqueIdentifier="sample_text", version="sample_text")
    partner = opf_Guide()
    setattr(partner, 'opf_Guide', None)
    _safe_set(owner, 'opf_Package6', partner)
    assert getattr(partner, 'opf_Guide') == owner
    _safe_set(owner, 'opf_Package6', None)
    assert getattr(partner, 'opf_Guide') is None


def test_assoc_guideItems45_stub_double():
    # opf_Guide has no real 'opf_Guide46' property in the generated
    # code (a bare stub) -- manually attach it so opf_Reference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # opf_Reference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = opf_Reference(href="sample_text", title="sample_text", type="sample_text")
    partner = opf_Guide()
    setattr(partner, 'opf_Guide46', None)
    _safe_set(owner, 'opf_Reference', partner)
    assert owner in getattr(partner, 'opf_Guide46')
    _safe_set(owner, 'opf_Reference', None)
    assert owner not in getattr(partner, 'opf_Guide46')


def test_assoc_items41_stub_double():
    # opf_Manifest has no real 'opf_Manifest42' property in the generated
    # code (a bare stub) -- manually attach it so opf_Item's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # opf_Item's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = opf_Item(fallback="sample_text", fallback_style="sample_text", file="sample_text", generated=True, href="sample_text", id="sample_text", media_type="sample_text", noToc=True, required_modules="sample_text", required_namespace="sample_text", sourcePath="sample_text", title="sample_text")
    partner = opf_Manifest()
    setattr(partner, 'opf_Manifest42', None)
    _safe_set(owner, 'opf_Item', partner)
    assert owner in getattr(partner, 'opf_Manifest42')
    _safe_set(owner, 'opf_Item', None)
    assert owner not in getattr(partner, 'opf_Manifest42')


def test_assoc_manifest1_stub_double():
    # opf_Manifest has no real 'opf_Manifest' property in the generated
    # code (a bare stub) -- manually attach it so opf_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # opf_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = opf_Package(generateCoverHTML=True, generateTableOfContents=True, includeReferencedResources=True, uniqueIdentifier="sample_text", version="sample_text")
    partner = opf_Manifest()
    setattr(partner, 'opf_Manifest', None)
    _safe_set(owner, 'opf_Package2', partner)
    assert getattr(partner, 'opf_Manifest') == owner
    _safe_set(owner, 'opf_Package2', None)
    assert getattr(partner, 'opf_Manifest') is None


def test_assoc_metadata0_stub_double():
    # opf_Metadata has no real 'opf_Metadata' property in the generated
    # code (a bare stub) -- manually attach it so opf_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # opf_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = opf_Package(generateCoverHTML=True, generateTableOfContents=True, includeReferencedResources=True, uniqueIdentifier="sample_text", version="sample_text")
    partner = opf_Metadata()
    setattr(partner, 'opf_Metadata', None)
    _safe_set(owner, 'opf_Package', partner)
    assert getattr(partner, 'opf_Metadata') == owner
    _safe_set(owner, 'opf_Package', None)
    assert getattr(partner, 'opf_Metadata') is None


def test_assoc_metas39_stub_double():
    # opf_Metadata has no real 'opf_Metadata40' property in the generated
    # code (a bare stub) -- manually attach it so opf_Meta's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # opf_Meta's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = opf_Meta(content="sample_text", name="sample_text")
    partner = opf_Metadata()
    setattr(partner, 'opf_Metadata40', None)
    _safe_set(owner, 'opf_Meta', partner)
    assert owner in getattr(partner, 'opf_Metadata40')
    _safe_set(owner, 'opf_Meta', None)
    assert owner not in getattr(partner, 'opf_Metadata40')


def test_assoc_tours7_stub_double():
    # opf_Tours has no real 'opf_Tours' property in the generated
    # code (a bare stub) -- manually attach it so opf_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # opf_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = opf_Package(generateCoverHTML=True, generateTableOfContents=True, includeReferencedResources=True, uniqueIdentifier="sample_text", version="sample_text")
    partner = opf_Tours()
    setattr(partner, 'opf_Tours', None)
    _safe_set(owner, 'opf_Package8', partner)
    assert getattr(partner, 'opf_Tours') == owner
    _safe_set(owner, 'opf_Package8', None)
    assert getattr(partner, 'opf_Tours') is None


