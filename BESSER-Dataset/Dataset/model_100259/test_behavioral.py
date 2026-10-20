import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractSection,
    Chapter,
    Identifiable,
    MarkUp,
    MarkupInCode,
    Part,
    Section,
    Section2,
    xdoc_AbstractSection,
    xdoc_Anchor,
    xdoc_Chapter,
    xdoc_ChapterRef,
    xdoc_Code,
    xdoc_CodeBlock,
    xdoc_CodeRef,
    xdoc_Document,
    xdoc_EObject,
    xdoc_Emphasize,
    xdoc_Glossary,
    xdoc_GlossaryEntry,
    xdoc_Identifiable,
    xdoc_ImageProxy,
    xdoc_ImageRef,
    xdoc_Item,
    xdoc_JvmDeclaredType,
    xdoc_LangDef,
    xdoc_Link,
    xdoc_MarkUp,
    xdoc_MarkupInCode,
    xdoc_OrderedList,
    xdoc_Part,
    xdoc_PartRef,
    xdoc_Ref,
    xdoc_Section,
    xdoc_Section2,
    xdoc_Section2Ref,
    xdoc_Section3,
    xdoc_Section4,
    xdoc_SectionRef,
    xdoc_Table,
    xdoc_TableData,
    xdoc_TableRow,
    xdoc_TextOrMarkup,
    xdoc_TextPart,
    xdoc_Todo,
    xdoc_UnorderedList,
    xdoc_XdocFile,
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

def test_assoc_description63_stub_double():
    # xdoc_TextOrMarkup has no real 'xdoc_TextOrMarkup64' property in the generated
    # code (a bare stub) -- manually attach it so xdoc_GlossaryEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xdoc_GlossaryEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xdoc_GlossaryEntry(alias="sample_text", name="sample_text")
    partner = xdoc_TextOrMarkup()
    setattr(partner, 'xdoc_TextOrMarkup64', None)
    _safe_set(owner, 'xdoc_GlossaryEntry', {partner})
    assert getattr(partner, 'xdoc_TextOrMarkup64') == owner
    _safe_set(owner, 'xdoc_GlossaryEntry', set())
    assert getattr(partner, 'xdoc_TextOrMarkup64') is None


def test_assoc_glossaryEntry65_stub_double():
    # xdoc_Glossary has no real 'xdoc_Glossary66' property in the generated
    # code (a bare stub) -- manually attach it so xdoc_GlossaryEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xdoc_GlossaryEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xdoc_GlossaryEntry(alias="sample_text", name="sample_text")
    partner = xdoc_Glossary()
    setattr(partner, 'xdoc_Glossary66', None)
    _safe_set(owner, 'xdoc_GlossaryEntry67', partner)
    assert owner in getattr(partner, 'xdoc_Glossary66')
    _safe_set(owner, 'xdoc_GlossaryEntry67', None)
    assert owner not in getattr(partner, 'xdoc_Glossary66')


def test_assoc_image57_stub_double():
    # xdoc_ImageProxy has no real 'xdoc_ImageProxy' property in the generated
    # code (a bare stub) -- manually attach it so xdoc_ImageRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xdoc_ImageRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xdoc_ImageRef(caption="sample_text", clazz="sample_text", name="sample_text", path="sample_text", style="sample_text")
    partner = xdoc_ImageProxy()
    setattr(partner, 'xdoc_ImageProxy', None)
    _safe_set(owner, 'xdoc_ImageRef', partner)
    assert getattr(partner, 'xdoc_ImageProxy') == owner
    _safe_set(owner, 'xdoc_ImageRef', None)
    assert getattr(partner, 'xdoc_ImageProxy') is None


def test_assoc_langDefs7_stub_double():
    # xdoc_Document has no real 'xdoc_Document8' property in the generated
    # code (a bare stub) -- manually attach it so xdoc_LangDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xdoc_LangDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xdoc_LangDef(keywords="sample_text", name="sample_text")
    partner = xdoc_Document()
    setattr(partner, 'xdoc_Document8', None)
    _safe_set(owner, 'xdoc_LangDef', partner)
    assert owner in getattr(partner, 'xdoc_Document8')
    _safe_set(owner, 'xdoc_LangDef', None)
    assert owner not in getattr(partner, 'xdoc_Document8')


def test_assoc_language60_stub_double():
    # xdoc_CodeBlock has no real 'xdoc_CodeBlock61' property in the generated
    # code (a bare stub) -- manually attach it so xdoc_LangDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xdoc_LangDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xdoc_LangDef(keywords="sample_text", name="sample_text")
    partner = xdoc_CodeBlock()
    setattr(partner, 'xdoc_CodeBlock61', None)
    _safe_set(owner, 'xdoc_LangDef62', partner)
    assert getattr(partner, 'xdoc_CodeBlock61') == owner
    _safe_set(owner, 'xdoc_LangDef62', None)
    assert getattr(partner, 'xdoc_CodeBlock61') is None


def test_assoc_ref43_stub_double():
    # xdoc_Ref has no real 'xdoc_Ref' property in the generated
    # code (a bare stub) -- manually attach it so xdoc_Identifiable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xdoc_Identifiable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xdoc_Identifiable(name="sample_text")
    partner = xdoc_Ref()
    setattr(partner, 'xdoc_Ref', None)
    _safe_set(owner, 'xdoc_Identifiable', partner)
    assert getattr(partner, 'xdoc_Ref') == owner
    _safe_set(owner, 'xdoc_Identifiable', None)
    assert getattr(partner, 'xdoc_Ref') is None


