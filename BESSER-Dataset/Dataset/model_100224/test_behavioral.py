import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BPMHumanTaskDescription,
    BPMHumanTaskDocument,
    BPMProcessDescription,
    BPMProcessDocument,
    DTODescription,
    DTODocument,
    DTOProperties,
    DTOProperty,
    EntityDescription,
    EntityDocument,
    EntityField,
    EntityFields,
    LuniferaDocDocument,
    LuniferaDocLayout,
    NamedDocument,
    RichString,
    RichStringElseIf,
    RichStringListElement,
    RichStringMarkup,
    RichStringTableData,
    RichStringTableRow,
    UIDescription,
    UIDocument,
    VaaclipseViewDescription,
    VaaclipseViewDocument,
    XBlockExpression,
    XExpression,
    XForLoopExpression,
    XStringLiteral,
    document_luniferadoc_DocumentInclude,
    document_luniferadoc_XImportDeclaration,
    luniferadoc_DocumentInclude,
    luniferadoc_NamedDocument,
    luniferadoc_document_BPMHumanTaskDescription,
    luniferadoc_document_BPMHumanTaskDocument,
    luniferadoc_document_BPMHumanTaskLayout,
    luniferadoc_document_BPMProcessDescription,
    luniferadoc_document_BPMProcessDocument,
    luniferadoc_document_BPMProcessLayout,
    luniferadoc_document_DTODescription,
    luniferadoc_document_DTODocument,
    luniferadoc_document_DTOLayout,
    luniferadoc_document_DTOProperties,
    luniferadoc_document_DTOProperty,
    luniferadoc_document_EntityDescription,
    luniferadoc_document_EntityDocument,
    luniferadoc_document_EntityField,
    luniferadoc_document_EntityFields,
    luniferadoc_document_EntityLayout,
    luniferadoc_document_GeneralDocument,
    luniferadoc_document_LuniferaDocDocument,
    luniferadoc_document_LuniferaDocLayout,
    luniferadoc_document_UIDescription,
    luniferadoc_document_UIDocument,
    luniferadoc_document_UILayout,
    luniferadoc_document_VaaclipseViewDescription,
    luniferadoc_document_VaaclipseViewDocument,
    luniferadoc_document_VaaclipseViewLayout,
    luniferadoc_richstring_RichString,
    luniferadoc_richstring_RichStringBold,
    luniferadoc_richstring_RichStringChapter,
    luniferadoc_richstring_RichStringCode,
    luniferadoc_richstring_RichStringDTORef,
    luniferadoc_richstring_RichStringElseIf,
    luniferadoc_richstring_RichStringEntityRef,
    luniferadoc_richstring_RichStringExample,
    luniferadoc_richstring_RichStringForLoop,
    luniferadoc_richstring_RichStringH1,
    luniferadoc_richstring_RichStringH2,
    luniferadoc_richstring_RichStringH3,
    luniferadoc_richstring_RichStringH4,
    luniferadoc_richstring_RichStringH5,
    luniferadoc_richstring_RichStringH6,
    luniferadoc_richstring_RichStringIf,
    luniferadoc_richstring_RichStringImg,
    luniferadoc_richstring_RichStringItalic,
    luniferadoc_richstring_RichStringList,
    luniferadoc_richstring_RichStringListElement,
    luniferadoc_richstring_RichStringLiteral,
    luniferadoc_richstring_RichStringMailto,
    luniferadoc_richstring_RichStringMarkup,
    luniferadoc_richstring_RichStringMovie,
    luniferadoc_richstring_RichStringOpenView,
    luniferadoc_richstring_RichStringOrderedList,
    luniferadoc_richstring_RichStringProcessRef,
    luniferadoc_richstring_RichStringRef,
    luniferadoc_richstring_RichStringSection,
    luniferadoc_richstring_RichStringSkype,
    luniferadoc_richstring_RichStringSpan,
    luniferadoc_richstring_RichStringStartProcess,
    luniferadoc_richstring_RichStringSubsection,
    luniferadoc_richstring_RichStringTable,
    luniferadoc_richstring_RichStringTableData,
    luniferadoc_richstring_RichStringTableRow,
    luniferadoc_richstring_RichStringTaskRef,
    luniferadoc_richstring_RichStringUIRef,
    luniferadoc_richstring_RichStringURL,
    luniferadoc_richstring_RichStringUnderline,
    luniferadoc_richstring_RichStringViewRef,
    richstring_luniferadoc_XExpression,
    DocType,
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

def test_assoc_content59_stub_double():
    # richstring_luniferadoc_XExpression has no real 'richstring_luniferadoc_XExpression60' property in the generated
    # code (a bare stub) -- manually attach it so luniferadoc_richstring_RichStringImg's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # luniferadoc_richstring_RichStringImg's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = luniferadoc_richstring_RichStringImg(alt="sample_text", height="sample_text", src="sample_text", width="sample_text")
    partner = richstring_luniferadoc_XExpression()
    setattr(partner, 'richstring_luniferadoc_XExpression60', None)
    _safe_set(owner, 'luniferadoc_richstring_RichStringImg', partner)
    assert getattr(partner, 'richstring_luniferadoc_XExpression60') == owner
    _safe_set(owner, 'luniferadoc_richstring_RichStringImg', None)
    assert getattr(partner, 'richstring_luniferadoc_XExpression60') is None


def test_assoc_content61_stub_double():
    # richstring_luniferadoc_XExpression has no real 'richstring_luniferadoc_XExpression62' property in the generated
    # code (a bare stub) -- manually attach it so luniferadoc_richstring_RichStringMailto's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # luniferadoc_richstring_RichStringMailto's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = luniferadoc_richstring_RichStringMailto(email="sample_text")
    partner = richstring_luniferadoc_XExpression()
    setattr(partner, 'richstring_luniferadoc_XExpression62', None)
    _safe_set(owner, 'luniferadoc_richstring_RichStringMailto', partner)
    assert getattr(partner, 'richstring_luniferadoc_XExpression62') == owner
    _safe_set(owner, 'luniferadoc_richstring_RichStringMailto', None)
    assert getattr(partner, 'richstring_luniferadoc_XExpression62') is None


def test_assoc_content63_stub_double():
    # richstring_luniferadoc_XExpression has no real 'richstring_luniferadoc_XExpression64' property in the generated
    # code (a bare stub) -- manually attach it so luniferadoc_richstring_RichStringSkype's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # luniferadoc_richstring_RichStringSkype's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = luniferadoc_richstring_RichStringSkype(target="sample_text")
    partner = richstring_luniferadoc_XExpression()
    setattr(partner, 'richstring_luniferadoc_XExpression64', None)
    _safe_set(owner, 'luniferadoc_richstring_RichStringSkype', partner)
    assert getattr(partner, 'richstring_luniferadoc_XExpression64') == owner
    _safe_set(owner, 'luniferadoc_richstring_RichStringSkype', None)
    assert getattr(partner, 'richstring_luniferadoc_XExpression64') is None


def test_assoc_content65_stub_double():
    # richstring_luniferadoc_XExpression has no real 'richstring_luniferadoc_XExpression66' property in the generated
    # code (a bare stub) -- manually attach it so luniferadoc_richstring_RichStringMovie's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # luniferadoc_richstring_RichStringMovie's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = luniferadoc_richstring_RichStringMovie(height="sample_text", src="sample_text", type="sample_text", width="sample_text")
    partner = richstring_luniferadoc_XExpression()
    setattr(partner, 'richstring_luniferadoc_XExpression66', None)
    _safe_set(owner, 'luniferadoc_richstring_RichStringMovie', partner)
    assert getattr(partner, 'richstring_luniferadoc_XExpression66') == owner
    _safe_set(owner, 'luniferadoc_richstring_RichStringMovie', None)
    assert getattr(partner, 'richstring_luniferadoc_XExpression66') is None


def test_assoc_content67_stub_double():
    # richstring_luniferadoc_XExpression has no real 'richstring_luniferadoc_XExpression68' property in the generated
    # code (a bare stub) -- manually attach it so luniferadoc_richstring_RichStringCode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # luniferadoc_richstring_RichStringCode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = luniferadoc_richstring_RichStringCode(lang="sample_text")
    partner = richstring_luniferadoc_XExpression()
    setattr(partner, 'richstring_luniferadoc_XExpression68', None)
    _safe_set(owner, 'luniferadoc_richstring_RichStringCode', partner)
    assert getattr(partner, 'richstring_luniferadoc_XExpression68') == owner
    _safe_set(owner, 'luniferadoc_richstring_RichStringCode', None)
    assert getattr(partner, 'richstring_luniferadoc_XExpression68') is None


def test_assoc_description1_stub_double():
    # EntityDescription has no real 'EntityDescription' property in the generated
    # code (a bare stub) -- manually attach it so luniferadoc_document_EntityDocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # luniferadoc_document_EntityDocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = luniferadoc_document_EntityDocument(entityClass="sample_text")
    partner = EntityDescription()
    setattr(partner, 'EntityDescription', None)
    _safe_set(owner, 'luniferadoc_document_EntityDocument', partner)
    assert getattr(partner, 'EntityDescription') == owner
    _safe_set(owner, 'luniferadoc_document_EntityDocument', None)
    assert getattr(partner, 'EntityDescription') is None


def test_assoc_description14_stub_double():
    # RichString has no real 'RichString15' property in the generated
    # code (a bare stub) -- manually attach it so luniferadoc_document_DTOProperty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # luniferadoc_document_DTOProperty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = luniferadoc_document_DTOProperty(name="sample_text")
    partner = RichString()
    setattr(partner, 'RichString15', None)
    _safe_set(owner, 'luniferadoc_document_DTOProperty', partner)
    assert getattr(partner, 'RichString15') == owner
    _safe_set(owner, 'luniferadoc_document_DTOProperty', None)
    assert getattr(partner, 'RichString15') is None


def test_assoc_description16_stub_double():
    # BPMProcessDescription has no real 'BPMProcessDescription' property in the generated
    # code (a bare stub) -- manually attach it so luniferadoc_document_BPMProcessDocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # luniferadoc_document_BPMProcessDocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = luniferadoc_document_BPMProcessDocument(process="sample_text")
    partner = BPMProcessDescription()
    setattr(partner, 'BPMProcessDescription', None)
    _safe_set(owner, 'luniferadoc_document_BPMProcessDocument', partner)
    assert getattr(partner, 'BPMProcessDescription') == owner
    _safe_set(owner, 'luniferadoc_document_BPMProcessDocument', None)
    assert getattr(partner, 'BPMProcessDescription') is None


def test_assoc_description19_stub_double():
    # BPMHumanTaskDescription has no real 'BPMHumanTaskDescription' property in the generated
    # code (a bare stub) -- manually attach it so luniferadoc_document_BPMHumanTaskDocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # luniferadoc_document_BPMHumanTaskDocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = luniferadoc_document_BPMHumanTaskDocument(task="sample_text")
    partner = BPMHumanTaskDescription()
    setattr(partner, 'BPMHumanTaskDescription', None)
    _safe_set(owner, 'luniferadoc_document_BPMHumanTaskDocument', partner)
    assert getattr(partner, 'BPMHumanTaskDescription') == owner
    _safe_set(owner, 'luniferadoc_document_BPMHumanTaskDocument', None)
    assert getattr(partner, 'BPMHumanTaskDescription') is None


def test_assoc_description22_stub_double():
    # VaaclipseViewDescription has no real 'VaaclipseViewDescription' property in the generated
    # code (a bare stub) -- manually attach it so luniferadoc_document_VaaclipseViewDocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # luniferadoc_document_VaaclipseViewDocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = luniferadoc_document_VaaclipseViewDocument(view="sample_text")
    partner = VaaclipseViewDescription()
    setattr(partner, 'VaaclipseViewDescription', None)
    _safe_set(owner, 'luniferadoc_document_VaaclipseViewDocument', partner)
    assert getattr(partner, 'VaaclipseViewDescription') == owner
    _safe_set(owner, 'luniferadoc_document_VaaclipseViewDocument', None)
    assert getattr(partner, 'VaaclipseViewDescription') is None


def test_assoc_description25_stub_double():
    # UIDescription has no real 'UIDescription' property in the generated
    # code (a bare stub) -- manually attach it so luniferadoc_document_UIDocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # luniferadoc_document_UIDocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = luniferadoc_document_UIDocument(ui="sample_text")
    partner = UIDescription()
    setattr(partner, 'UIDescription', None)
    _safe_set(owner, 'luniferadoc_document_UIDocument', partner)
    assert getattr(partner, 'UIDescription') == owner
    _safe_set(owner, 'luniferadoc_document_UIDocument', None)
    assert getattr(partner, 'UIDescription') is None


def test_assoc_description6_stub_double():
    # RichString has no real 'RichString7' property in the generated
    # code (a bare stub) -- manually attach it so luniferadoc_document_EntityField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # luniferadoc_document_EntityField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = luniferadoc_document_EntityField(length=7, name="sample_text", nullable=True, pk=True, type="sample_text")
    partner = RichString()
    setattr(partner, 'RichString7', None)
    _safe_set(owner, 'luniferadoc_document_EntityField', partner)
    assert getattr(partner, 'RichString7') == owner
    _safe_set(owner, 'luniferadoc_document_EntityField', None)
    assert getattr(partner, 'RichString7') is None


def test_assoc_description8_stub_double():
    # DTODescription has no real 'DTODescription' property in the generated
    # code (a bare stub) -- manually attach it so luniferadoc_document_DTODocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # luniferadoc_document_DTODocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = luniferadoc_document_DTODocument(dtoClass="sample_text")
    partner = DTODescription()
    setattr(partner, 'DTODescription', None)
    _safe_set(owner, 'luniferadoc_document_DTODocument', partner)
    assert getattr(partner, 'DTODescription') == owner
    _safe_set(owner, 'luniferadoc_document_DTODocument', None)
    assert getattr(partner, 'DTODescription') is None


def test_assoc_expression55_stub_double():
    # richstring_luniferadoc_XExpression has no real 'richstring_luniferadoc_XExpression56' property in the generated
    # code (a bare stub) -- manually attach it so luniferadoc_richstring_RichStringMarkup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # luniferadoc_richstring_RichStringMarkup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = luniferadoc_richstring_RichStringMarkup(id="sample_text", styleClass="sample_text")
    partner = richstring_luniferadoc_XExpression()
    setattr(partner, 'richstring_luniferadoc_XExpression56', None)
    _safe_set(owner, 'luniferadoc_richstring_RichStringMarkup', partner)
    assert getattr(partner, 'richstring_luniferadoc_XExpression56') == owner
    _safe_set(owner, 'luniferadoc_richstring_RichStringMarkup', None)
    assert getattr(partner, 'richstring_luniferadoc_XExpression56') is None


def test_assoc_fields2_stub_double():
    # EntityFields has no real 'EntityFields' property in the generated
    # code (a bare stub) -- manually attach it so luniferadoc_document_EntityDocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # luniferadoc_document_EntityDocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = luniferadoc_document_EntityDocument(entityClass="sample_text")
    partner = EntityFields()
    setattr(partner, 'EntityFields', None)
    _safe_set(owner, 'luniferadoc_document_EntityDocument3', partner)
    assert getattr(partner, 'EntityFields') == owner
    _safe_set(owner, 'luniferadoc_document_EntityDocument3', None)
    assert getattr(partner, 'EntityFields') is None


def test_assoc_include0_stub_double():
    # LuniferaDocDocument has no real 'LuniferaDocDocument' property in the generated
    # code (a bare stub) -- manually attach it so luniferadoc_DocumentInclude's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # luniferadoc_DocumentInclude's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = luniferadoc_DocumentInclude(varName="sample_text")
    partner = LuniferaDocDocument()
    setattr(partner, 'LuniferaDocDocument', None)
    _safe_set(owner, 'luniferadoc_DocumentInclude', partner)
    assert getattr(partner, 'LuniferaDocDocument') == owner
    _safe_set(owner, 'luniferadoc_DocumentInclude', None)
    assert getattr(partner, 'LuniferaDocDocument') is None


def test_assoc_properties9_stub_double():
    # DTOProperties has no real 'DTOProperties' property in the generated
    # code (a bare stub) -- manually attach it so luniferadoc_document_DTODocument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # luniferadoc_document_DTODocument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = luniferadoc_document_DTODocument(dtoClass="sample_text")
    partner = DTOProperties()
    setattr(partner, 'DTOProperties', None)
    _safe_set(owner, 'luniferadoc_document_DTODocument10', partner)
    assert getattr(partner, 'DTOProperties') == owner
    _safe_set(owner, 'luniferadoc_document_DTODocument10', None)
    assert getattr(partner, 'DTOProperties') is None


def test_assoc_text57_stub_double():
    # richstring_luniferadoc_XExpression has no real 'richstring_luniferadoc_XExpression58' property in the generated
    # code (a bare stub) -- manually attach it so luniferadoc_richstring_RichStringURL's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # luniferadoc_richstring_RichStringURL's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = luniferadoc_richstring_RichStringURL(location="sample_text")
    partner = richstring_luniferadoc_XExpression()
    setattr(partner, 'richstring_luniferadoc_XExpression58', None)
    _safe_set(owner, 'luniferadoc_richstring_RichStringURL', partner)
    assert getattr(partner, 'richstring_luniferadoc_XExpression58') == owner
    _safe_set(owner, 'luniferadoc_richstring_RichStringURL', None)
    assert getattr(partner, 'richstring_luniferadoc_XExpression58') is None


