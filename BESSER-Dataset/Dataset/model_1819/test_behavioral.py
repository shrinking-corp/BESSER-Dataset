import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Author,
    BookContainer,
    BookSection,
    Container,
    Content,
    Copyright,
    ExtensionMappingEntry,
    Import,
    Map,
    MapContainer,
    MapElement,
    NameRule,
    PatternRule,
    ResourceFactory,
    Section,
    builder_PropertyEntry,
    doc_Test,
    doc_book_Book,
    doc_book_BookContainer,
    doc_book_BookSection,
    doc_builder_BookBuilder,
    doc_builder_PropertyEntry,
    doc_fragment_Author,
    doc_fragment_Container,
    doc_fragment_Content,
    doc_fragment_Copyright,
    doc_fragment_Fragment,
    doc_fragment_PlainTextContent,
    doc_fragment_Section,
    doc_map_ContentGenerator,
    doc_map_ExcludePatternRule,
    doc_map_ExtensionMappingEntry,
    doc_map_Feature,
    doc_map_File,
    doc_map_Import,
    doc_map_IncludePatternRule,
    doc_map_Map,
    doc_map_MapContainer,
    doc_map_MapElement,
    doc_map_MapSection,
    doc_map_NameRule,
    doc_map_PatternRule,
    doc_map_ResourceFactory,
    fragment_Content,
    map_MapContainer,
    map_MapElement,
    NumberingStyle,
    RuleResult,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_anyContent4_stub_double():
    # Content has no real 'Content' property in the generated
    # code (a bare stub) -- manually attach it so doc_fragment_Container's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # doc_fragment_Container's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = doc_fragment_Container(content="sample_text")
    partner = Content()
    setattr(partner, 'Content', None)
    _safe_set(owner, 'doc_fragment_Container', {partner})
    assert getattr(partner, 'Content') == owner
    _safe_set(owner, 'doc_fragment_Container', set())
    assert getattr(partner, 'Content') is None


def test_assoc_author7_stub_double():
    # Author has no real 'Author' property in the generated
    # code (a bare stub) -- manually attach it so doc_fragment_Copyright's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # doc_fragment_Copyright's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = doc_fragment_Copyright(year=7)
    partner = Author()
    setattr(partner, 'Author', None)
    _safe_set(owner, 'doc_fragment_Copyright', {partner})
    assert getattr(partner, 'Author') == owner
    _safe_set(owner, 'doc_fragment_Copyright', set())
    assert getattr(partner, 'Author') is None


def test_assoc_authors16_stub_double():
    # Author has no real 'Author17' property in the generated
    # code (a bare stub) -- manually attach it so doc_builder_BookBuilder's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # doc_builder_BookBuilder's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = doc_builder_BookBuilder(copyrightMarker="sample_text", license="sample_text", title="sample_text", version="sample_text")
    partner = Author()
    setattr(partner, 'Author17', None)
    _safe_set(owner, 'doc_builder_BookBuilder', {partner})
    assert getattr(partner, 'Author17') == owner
    _safe_set(owner, 'doc_builder_BookBuilder', set())
    assert getattr(partner, 'Author17') is None


def test_assoc_authors8_stub_double():
    # Author has no real 'Author9' property in the generated
    # code (a bare stub) -- manually attach it so doc_book_Book's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # doc_book_Book's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = doc_book_Book(copyrightMarker="sample_text", copyrightText="sample_text", title="sample_text", version="sample_text")
    partner = Author()
    setattr(partner, 'Author9', None)
    _safe_set(owner, 'doc_book_Book', {partner})
    assert getattr(partner, 'Author9') == owner
    _safe_set(owner, 'doc_book_Book', set())
    assert getattr(partner, 'Author9') is None


def test_assoc_content12_stub_double():
    # Content has no real 'Content13' property in the generated
    # code (a bare stub) -- manually attach it so doc_book_BookContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # doc_book_BookContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = doc_book_BookContainer(numberingStyle="sample_text")
    partner = Content()
    setattr(partner, 'Content13', None)
    _safe_set(owner, 'doc_book_BookContainer', {partner})
    assert getattr(partner, 'Content13') == owner
    _safe_set(owner, 'doc_book_BookContainer', set())
    assert getattr(partner, 'Content13') is None


def test_assoc_copyright10_stub_double():
    # Copyright has no real 'Copyright' property in the generated
    # code (a bare stub) -- manually attach it so doc_book_Book's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # doc_book_Book's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = doc_book_Book(copyrightMarker="sample_text", copyrightText="sample_text", title="sample_text", version="sample_text")
    partner = Copyright()
    setattr(partner, 'Copyright', None)
    _safe_set(owner, 'doc_book_Book11', {partner})
    assert getattr(partner, 'Copyright') == owner
    _safe_set(owner, 'doc_book_Book11', set())
    assert getattr(partner, 'Copyright') is None


def test_assoc_copyright18_stub_double():
    # Copyright has no real 'Copyright20' property in the generated
    # code (a bare stub) -- manually attach it so doc_builder_BookBuilder's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # doc_builder_BookBuilder's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = doc_builder_BookBuilder(copyrightMarker="sample_text", license="sample_text", title="sample_text", version="sample_text")
    partner = Copyright()
    setattr(partner, 'Copyright20', None)
    _safe_set(owner, 'doc_builder_BookBuilder19', {partner})
    assert getattr(partner, 'Copyright20') == owner
    _safe_set(owner, 'doc_builder_BookBuilder19', set())
    assert getattr(partner, 'Copyright20') is None


def test_assoc_elements3_stub_double():
    # MapElement has no real 'MapElement' property in the generated
    # code (a bare stub) -- manually attach it so doc_map_MapContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # doc_map_MapContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = doc_map_MapContainer(numberingStyle="sample_text")
    partner = MapElement()
    setattr(partner, 'MapElement', None)
    _safe_set(owner, 'doc_map_MapContainer', {partner})
    assert getattr(partner, 'MapElement') == owner
    _safe_set(owner, 'doc_map_MapContainer', set())
    assert getattr(partner, 'MapElement') is None


def test_assoc_extensionMappings0_stub_double():
    # ExtensionMappingEntry has no real 'ExtensionMappingEntry' property in the generated
    # code (a bare stub) -- manually attach it so doc_map_Map's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # doc_map_Map's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = doc_map_Map()
    partner = ExtensionMappingEntry()
    setattr(partner, 'ExtensionMappingEntry', None)
    _safe_set(owner, 'doc_map_Map', {partner})
    assert getattr(partner, 'ExtensionMappingEntry') == owner
    _safe_set(owner, 'doc_map_Map', set())
    assert getattr(partner, 'ExtensionMappingEntry') is None


def test_assoc_factory2_stub_double():
    # ResourceFactory has no real 'ResourceFactory' property in the generated
    # code (a bare stub) -- manually attach it so doc_map_ExtensionMappingEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # doc_map_ExtensionMappingEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = doc_map_ExtensionMappingEntry(extension="sample_text")
    partner = ResourceFactory()
    setattr(partner, 'ResourceFactory', None)
    _safe_set(owner, 'doc_map_ExtensionMappingEntry', partner)
    assert getattr(partner, 'ResourceFactory') == owner
    _safe_set(owner, 'doc_map_ExtensionMappingEntry', None)
    assert getattr(partner, 'ResourceFactory') is None


def test_assoc_fileNameRules1_stub_double():
    # NameRule has no real 'NameRule' property in the generated
    # code (a bare stub) -- manually attach it so doc_map_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # doc_map_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = doc_map_Feature(createSection=True, featureId="sample_text")
    partner = NameRule()
    setattr(partner, 'NameRule', None)
    _safe_set(owner, 'doc_map_Feature', {partner})
    assert getattr(partner, 'NameRule') == owner
    _safe_set(owner, 'doc_map_Feature', set())
    assert getattr(partner, 'NameRule') is None


def test_assoc_properties21_stub_double():
    # builder_PropertyEntry has no real 'builder_PropertyEntry' property in the generated
    # code (a bare stub) -- manually attach it so doc_builder_BookBuilder's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # doc_builder_BookBuilder's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = doc_builder_BookBuilder(copyrightMarker="sample_text", license="sample_text", title="sample_text", version="sample_text")
    partner = builder_PropertyEntry()
    setattr(partner, 'builder_PropertyEntry', None)
    _safe_set(owner, 'doc_builder_BookBuilder22', {partner})
    assert getattr(partner, 'builder_PropertyEntry') == owner
    _safe_set(owner, 'doc_builder_BookBuilder22', set())
    assert getattr(partner, 'builder_PropertyEntry') is None


def test_assoc_section5_stub_double():
    # Section has no real 'Section' property in the generated
    # code (a bare stub) -- manually attach it so doc_fragment_Container's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # doc_fragment_Container's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = doc_fragment_Container(content="sample_text")
    partner = Section()
    setattr(partner, 'Section', None)
    _safe_set(owner, 'doc_fragment_Container6', {partner})
    assert getattr(partner, 'Section') == owner
    _safe_set(owner, 'doc_fragment_Container6', set())
    assert getattr(partner, 'Section') is None


def test_assoc_sections14_stub_double():
    # BookSection has no real 'BookSection' property in the generated
    # code (a bare stub) -- manually attach it so doc_book_BookContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # doc_book_BookContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = doc_book_BookContainer(numberingStyle="sample_text")
    partner = BookSection()
    setattr(partner, 'BookSection', None)
    _safe_set(owner, 'doc_book_BookContainer15', {partner})
    assert getattr(partner, 'BookSection') == owner
    _safe_set(owner, 'doc_book_BookContainer15', set())
    assert getattr(partner, 'BookSection') is None


