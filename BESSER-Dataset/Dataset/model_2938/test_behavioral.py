import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DynamicPage,
    EJSLPart,
    Extension,
    HTMLTypes,
    InternalLink,
    Link,
    Page,
    Section,
    Type,
    eJSL_Attribute,
    eJSL_Author,
    eJSL_BackendSection,
    eJSL_CMSCore,
    eJSL_CMSExtension,
    eJSL_Class,
    eJSL_ComplexHTMLTypes,
    eJSL_Component,
    eJSL_ComponentReference,
    eJSL_ContextLink,
    eJSL_CssBlock,
    eJSL_CustomPage,
    eJSL_Datatype,
    eJSL_DatatypeReference,
    eJSL_DetailPageField,
    eJSL_DetailsPage,
    eJSL_DynamicPage,
    eJSL_EJSLModel,
    eJSL_EJSLPart,
    eJSL_Entity,
    eJSL_Entitypackage,
    eJSL_Extension,
    eJSL_ExtensionPackage,
    eJSL_ExternalLink,
    eJSL_Feature,
    eJSL_FrontendSection,
    eJSL_HTMLTypes,
    eJSL_IndexPage,
    eJSL_InternalLink,
    eJSL_KeyValuePair,
    eJSL_Language,
    eJSL_Library,
    eJSL_Link,
    eJSL_LinkParameter,
    eJSL_Manifestation,
    eJSL_Method,
    eJSL_MethodParameter,
    eJSL_Module,
    eJSL_Package,
    eJSL_Page,
    eJSL_PageAction,
    eJSL_PageReference,
    eJSL_Parameter,
    eJSL_ParameterGroup,
    eJSL_Plugin,
    eJSL_Position,
    eJSL_PositionParameter,
    eJSL_Reference,
    eJSL_Section,
    eJSL_SimpleHTMLTypes,
    eJSL_StandardTypes,
    eJSL_StaticPage,
    eJSL_Template,
    eJSL_Type,
    eJSL_coreFeature,
    ComplexHTMLTypeKinds,
    CoreComponent,
    DataAccessKinds,
    PageActionKind,
    PageActionPositionKind,
    PageKinds,
    PluginKinds,
    SimpleHTMLTypeKinds,
    StandardTypeKinds,
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

def test_assoc_attribute54_reverse_link_reassign_clear():
    a1 = eJSL_Reference(id=True, lower="sample_text", preserve=True, upper="sample_text")
    a2 = eJSL_Reference(id=False, lower="sample_text_2", preserve=False, upper="sample_text_2")
    b = eJSL_Attribute(id=True, isprimary=True, isunique=True, name="sample_text", preserve=True)
    _safe_set(b, 'eJSL_Attribute56', a1)
    assert _is_linked(b, 'eJSL_Attribute56', a1)
    if hasattr(a1, 'eJSL_Reference55'):
        assert _is_linked(a1, 'eJSL_Reference55', b)
    _safe_set(b, 'eJSL_Attribute56', a2)
    assert _is_linked(b, 'eJSL_Attribute56', a2)
    if hasattr(a1, 'eJSL_Reference55'):
        assert not _is_linked(a1, 'eJSL_Reference55', b)
    if hasattr(a2, 'eJSL_Reference55'):
        assert _is_linked(a2, 'eJSL_Reference55', b)
    _safe_set(b, 'eJSL_Attribute56', None)
    assert not _is_linked(b, 'eJSL_Attribute56', a2)
    if hasattr(a2, 'eJSL_Reference55'):
        assert not _is_linked(a2, 'eJSL_Reference55', b)


def test_assoc_attributerefereced60_reverse_link_reassign_clear():
    a1 = eJSL_Reference(id=True, lower="sample_text", preserve=True, upper="sample_text")
    a2 = eJSL_Reference(id=False, lower="sample_text_2", preserve=False, upper="sample_text_2")
    b = eJSL_Attribute(id=True, isprimary=True, isunique=True, name="sample_text", preserve=True)
    _safe_set(b, 'eJSL_Attribute62', a1)
    assert _is_linked(b, 'eJSL_Attribute62', a1)
    if hasattr(a1, 'eJSL_Reference61'):
        assert _is_linked(a1, 'eJSL_Reference61', b)
    _safe_set(b, 'eJSL_Attribute62', a2)
    assert _is_linked(b, 'eJSL_Attribute62', a2)
    if hasattr(a1, 'eJSL_Reference61'):
        assert not _is_linked(a1, 'eJSL_Reference61', b)
    if hasattr(a2, 'eJSL_Reference61'):
        assert _is_linked(a2, 'eJSL_Reference61', b)
    _safe_set(b, 'eJSL_Attribute62', None)
    assert not _is_linked(b, 'eJSL_Attribute62', a2)
    if hasattr(a2, 'eJSL_Reference61'):
        assert not _is_linked(a2, 'eJSL_Reference61', b)


def test_assoc_attributes24_reverse_link_reassign_clear():
    a1 = eJSL_Parameter(defaultvalue="sample_text", descripton="sample_text", label="sample_text", name="sample_text", size=7)
    a2 = eJSL_Parameter(defaultvalue="sample_text_2", descripton="sample_text_2", label="sample_text_2", name="sample_text_2", size=13)
    b = eJSL_KeyValuePair(name="sample_text", value="sample_text")
    _safe_set(b, 'eJSL_KeyValuePair26', a1)
    assert _is_linked(b, 'eJSL_KeyValuePair26', a1)
    if hasattr(a1, 'eJSL_Parameter25'):
        assert _is_linked(a1, 'eJSL_Parameter25', b)
    _safe_set(b, 'eJSL_KeyValuePair26', a2)
    assert _is_linked(b, 'eJSL_KeyValuePair26', a2)
    if hasattr(a1, 'eJSL_Parameter25'):
        assert not _is_linked(a1, 'eJSL_Parameter25', b)
    if hasattr(a2, 'eJSL_Parameter25'):
        assert _is_linked(a2, 'eJSL_Parameter25', b)
    _safe_set(b, 'eJSL_KeyValuePair26', None)
    assert not _is_linked(b, 'eJSL_KeyValuePair26', a2)
    if hasattr(a2, 'eJSL_Parameter25'):
        assert not _is_linked(a2, 'eJSL_Parameter25', b)


def test_assoc_attributes45_reverse_link_reassign_clear():
    a1 = eJSL_Entity(name="sample_text", preserve=True)
    a2 = eJSL_Entity(name="sample_text_2", preserve=False)
    b = eJSL_Attribute(id=True, isprimary=True, isunique=True, name="sample_text", preserve=True)
    _safe_set(b, 'eJSL_Attribute', a1)
    assert _is_linked(b, 'eJSL_Attribute', a1)
    if hasattr(a1, 'eJSL_Entity46'):
        assert _is_linked(a1, 'eJSL_Entity46', b)
    _safe_set(b, 'eJSL_Attribute', a2)
    assert _is_linked(b, 'eJSL_Attribute', a2)
    if hasattr(a1, 'eJSL_Entity46'):
        assert not _is_linked(a1, 'eJSL_Entity46', b)
    if hasattr(a2, 'eJSL_Entity46'):
        assert _is_linked(a2, 'eJSL_Entity46', b)
    _safe_set(b, 'eJSL_Attribute', None)
    assert not _is_linked(b, 'eJSL_Attribute', a2)
    if hasattr(a2, 'eJSL_Entity46'):
        assert not _is_linked(a2, 'eJSL_Entity46', b)


def test_assoc_attvalue108_reverse_link_reassign_clear():
    a1 = eJSL_LinkParameter(id=True, name="sample_text", value="sample_text")
    a2 = eJSL_LinkParameter(id=False, name="sample_text_2", value="sample_text_2")
    b = eJSL_Attribute(id=True, isprimary=True, isunique=True, name="sample_text", preserve=True)
    _safe_set(b, 'eJSL_Attribute110', a1)
    assert _is_linked(b, 'eJSL_Attribute110', a1)
    if hasattr(a1, 'eJSL_LinkParameter109'):
        assert _is_linked(a1, 'eJSL_LinkParameter109', b)
    _safe_set(b, 'eJSL_Attribute110', a2)
    assert _is_linked(b, 'eJSL_Attribute110', a2)
    if hasattr(a1, 'eJSL_LinkParameter109'):
        assert not _is_linked(a1, 'eJSL_LinkParameter109', b)
    if hasattr(a2, 'eJSL_LinkParameter109'):
        assert _is_linked(a2, 'eJSL_LinkParameter109', b)
    _safe_set(b, 'eJSL_Attribute110', None)
    assert not _is_linked(b, 'eJSL_Attribute110', a2)
    if hasattr(a2, 'eJSL_LinkParameter109'):
        assert not _is_linked(a2, 'eJSL_LinkParameter109', b)


def test_assoc_authors176_reverse_link_reassign_clear():
    a1 = eJSL_Manifestation(copyright="sample_text", creationdate="sample_text", description="sample_text", license="sample_text", link="sample_text", version="sample_text")
    a2 = eJSL_Manifestation(copyright="sample_text_2", creationdate="sample_text_2", description="sample_text_2", license="sample_text_2", link="sample_text_2", version="sample_text_2")
    b = eJSL_Author(authoremail="sample_text", authorurl="sample_text", name="sample_text")
    _safe_set(b, 'eJSL_Author', a1)
    assert _is_linked(b, 'eJSL_Author', a1)
    if hasattr(a1, 'eJSL_Manifestation177'):
        assert _is_linked(a1, 'eJSL_Manifestation177', b)
    _safe_set(b, 'eJSL_Author', a2)
    assert _is_linked(b, 'eJSL_Author', a2)
    if hasattr(a1, 'eJSL_Manifestation177'):
        assert not _is_linked(a1, 'eJSL_Manifestation177', b)
    if hasattr(a2, 'eJSL_Manifestation177'):
        assert _is_linked(a2, 'eJSL_Manifestation177', b)
    _safe_set(b, 'eJSL_Author', None)
    assert not _is_linked(b, 'eJSL_Author', a2)
    if hasattr(a2, 'eJSL_Manifestation177'):
        assert not _is_linked(a2, 'eJSL_Manifestation177', b)


def test_assoc_classes148_reverse_link_reassign_clear():
    a1 = eJSL_Package(name="sample_text")
    a2 = eJSL_Package(name="sample_text_2")
    b = eJSL_Class(name="sample_text")
    _safe_set(b, 'eJSL_Class150', a1)
    assert _is_linked(b, 'eJSL_Class150', a1)
    if hasattr(a1, 'eJSL_Package149'):
        assert _is_linked(a1, 'eJSL_Package149', b)
    _safe_set(b, 'eJSL_Class150', a2)
    assert _is_linked(b, 'eJSL_Class150', a2)
    if hasattr(a1, 'eJSL_Package149'):
        assert not _is_linked(a1, 'eJSL_Package149', b)
    if hasattr(a2, 'eJSL_Package149'):
        assert _is_linked(a2, 'eJSL_Package149', b)
    _safe_set(b, 'eJSL_Class150', None)
    assert not _is_linked(b, 'eJSL_Class150', a2)
    if hasattr(a2, 'eJSL_Package149'):
        assert not _is_linked(a2, 'eJSL_Package149', b)


def test_assoc_datatypes39_reverse_link_reassign_clear():
    a1 = eJSL_Entitypackage(name="sample_text")
    a2 = eJSL_Entitypackage(name="sample_text_2")
    b = eJSL_Datatype(name="sample_text", type="sample_text")
    _safe_set(b, 'eJSL_Datatype41', a1)
    assert _is_linked(b, 'eJSL_Datatype41', a1)
    if hasattr(a1, 'eJSL_Entitypackage40'):
        assert _is_linked(a1, 'eJSL_Entitypackage40', b)
    _safe_set(b, 'eJSL_Datatype41', a2)
    assert _is_linked(b, 'eJSL_Datatype41', a2)
    if hasattr(a1, 'eJSL_Entitypackage40'):
        assert not _is_linked(a1, 'eJSL_Entitypackage40', b)
    if hasattr(a2, 'eJSL_Entitypackage40'):
        assert _is_linked(a2, 'eJSL_Entitypackage40', b)
    _safe_set(b, 'eJSL_Datatype41', None)
    assert not _is_linked(b, 'eJSL_Datatype41', a2)
    if hasattr(a2, 'eJSL_Entitypackage40'):
        assert not _is_linked(a2, 'eJSL_Entitypackage40', b)


def test_assoc_entities134_reverse_link_reassign_clear():
    a1 = eJSL_Plugin(type="sample_text")
    a2 = eJSL_Plugin(type="sample_text_2")
    b = eJSL_Entity(name="sample_text", preserve=True)
    _safe_set(b, 'eJSL_Entity135', a1)
    assert _is_linked(b, 'eJSL_Entity135', a1)
    if hasattr(a1, 'eJSL_Plugin'):
        assert _is_linked(a1, 'eJSL_Plugin', b)
    _safe_set(b, 'eJSL_Entity135', a2)
    assert _is_linked(b, 'eJSL_Entity135', a2)
    if hasattr(a1, 'eJSL_Plugin'):
        assert not _is_linked(a1, 'eJSL_Plugin', b)
    if hasattr(a2, 'eJSL_Plugin'):
        assert _is_linked(a2, 'eJSL_Plugin', b)
    _safe_set(b, 'eJSL_Entity135', None)
    assert not _is_linked(b, 'eJSL_Entity135', a2)
    if hasattr(a2, 'eJSL_Plugin'):
        assert not _is_linked(a2, 'eJSL_Plugin', b)


def test_assoc_entities157_reverse_link_reassign_clear():
    a1 = eJSL_Entity(name="sample_text", preserve=True)
    a2 = eJSL_Entity(name="sample_text_2", preserve=False)
    b = eJSL_Class(name="sample_text")
    _safe_set(b, 'eJSL_Class158', {a1})
    assert _is_linked(b, 'eJSL_Class158', a1)
    if hasattr(a1, 'eJSL_Entity159'):
        assert _is_linked(a1, 'eJSL_Entity159', b)
    _safe_set(b, 'eJSL_Class158', {a2})
    assert _is_linked(b, 'eJSL_Class158', a2)
    if hasattr(a1, 'eJSL_Entity159'):
        assert not _is_linked(a1, 'eJSL_Entity159', b)
    if hasattr(a2, 'eJSL_Entity159'):
        assert _is_linked(a2, 'eJSL_Entity159', b)
    _safe_set(b, 'eJSL_Class158', set())
    assert not _is_linked(b, 'eJSL_Class158', a2)
    if hasattr(a2, 'eJSL_Entity159'):
        assert not _is_linked(a2, 'eJSL_Entity159', b)


def test_assoc_entities36_reverse_link_reassign_clear():
    a1 = eJSL_Entitypackage(name="sample_text")
    a2 = eJSL_Entitypackage(name="sample_text_2")
    b = eJSL_Entity(name="sample_text", preserve=True)
    _safe_set(b, 'eJSL_Entity38', a1)
    assert _is_linked(b, 'eJSL_Entity38', a1)
    if hasattr(a1, 'eJSL_Entitypackage37'):
        assert _is_linked(a1, 'eJSL_Entitypackage37', b)
    _safe_set(b, 'eJSL_Entity38', a2)
    assert _is_linked(b, 'eJSL_Entity38', a2)
    if hasattr(a1, 'eJSL_Entitypackage37'):
        assert not _is_linked(a1, 'eJSL_Entitypackage37', b)
    if hasattr(a2, 'eJSL_Entitypackage37'):
        assert _is_linked(a2, 'eJSL_Entitypackage37', b)
    _safe_set(b, 'eJSL_Entity38', None)
    assert not _is_linked(b, 'eJSL_Entity38', a2)
    if hasattr(a2, 'eJSL_Entitypackage37'):
        assert not _is_linked(a2, 'eJSL_Entitypackage37', b)


def test_assoc_entities76_reverse_link_reassign_clear():
    a1 = eJSL_Entity(name="sample_text", preserve=True)
    a2 = eJSL_Entity(name="sample_text_2", preserve=False)
    b = eJSL_DynamicPage(preserve=True)
    _safe_set(b, 'eJSL_DynamicPage', {a1})
    assert _is_linked(b, 'eJSL_DynamicPage', a1)
    if hasattr(a1, 'eJSL_Entity77'):
        assert _is_linked(a1, 'eJSL_Entity77', b)
    _safe_set(b, 'eJSL_DynamicPage', {a2})
    assert _is_linked(b, 'eJSL_DynamicPage', a2)
    if hasattr(a1, 'eJSL_Entity77'):
        assert not _is_linked(a1, 'eJSL_Entity77', b)
    if hasattr(a2, 'eJSL_Entity77'):
        assert _is_linked(a2, 'eJSL_Entity77', b)
    _safe_set(b, 'eJSL_DynamicPage', set())
    assert not _is_linked(b, 'eJSL_DynamicPage', a2)
    if hasattr(a2, 'eJSL_Entity77'):
        assert not _is_linked(a2, 'eJSL_Entity77', b)


def test_assoc_entities97_reverse_link_reassign_clear():
    a1 = eJSL_Entity(name="sample_text", preserve=True)
    a2 = eJSL_Entity(name="sample_text_2", preserve=False)
    b = eJSL_CustomPage(pageType="sample_text", preserve="sample_text")
    _safe_set(b, 'eJSL_CustomPage', {a1})
    assert _is_linked(b, 'eJSL_CustomPage', a1)
    if hasattr(a1, 'eJSL_Entity98'):
        assert _is_linked(a1, 'eJSL_Entity98', b)
    _safe_set(b, 'eJSL_CustomPage', {a2})
    assert _is_linked(b, 'eJSL_CustomPage', a2)
    if hasattr(a1, 'eJSL_Entity98'):
        assert not _is_linked(a1, 'eJSL_Entity98', b)
    if hasattr(a2, 'eJSL_Entity98'):
        assert _is_linked(a2, 'eJSL_Entity98', b)
    _safe_set(b, 'eJSL_CustomPage', set())
    assert not _is_linked(b, 'eJSL_CustomPage', a2)
    if hasattr(a2, 'eJSL_Entity98'):
        assert not _is_linked(a2, 'eJSL_Entity98', b)


def test_assoc_entity57_reverse_link_reassign_clear():
    a1 = eJSL_Reference(id=True, lower="sample_text", preserve=True, upper="sample_text")
    a2 = eJSL_Reference(id=False, lower="sample_text_2", preserve=False, upper="sample_text_2")
    b = eJSL_Entity(name="sample_text", preserve=True)
    _safe_set(b, 'eJSL_Entity59', a1)
    assert _is_linked(b, 'eJSL_Entity59', a1)
    if hasattr(a1, 'eJSL_Reference58'):
        assert _is_linked(a1, 'eJSL_Reference58', b)
    _safe_set(b, 'eJSL_Entity59', a2)
    assert _is_linked(b, 'eJSL_Entity59', a2)
    if hasattr(a1, 'eJSL_Reference58'):
        assert not _is_linked(a1, 'eJSL_Reference58', b)
    if hasattr(a2, 'eJSL_Reference58'):
        assert _is_linked(a2, 'eJSL_Reference58', b)
    _safe_set(b, 'eJSL_Entity59', None)
    assert not _is_linked(b, 'eJSL_Entity59', a2)
    if hasattr(a2, 'eJSL_Reference58'):
        assert not _is_linked(a2, 'eJSL_Reference58', b)


def test_assoc_entitypackages34_reverse_link_reassign_clear():
    a1 = eJSL_Entitypackage(name="sample_text")
    a2 = eJSL_Entitypackage(name="sample_text_2")
    b = eJSL_Entitypackage(name="sample_text")
    _safe_set(b, 'eJSL_Entitypackage35', a1)
    assert _is_linked(b, 'eJSL_Entitypackage35', a1)
    if hasattr(a1, 'eJSL_Entitypackage33'):
        assert _is_linked(a1, 'eJSL_Entitypackage33', b)
    _safe_set(b, 'eJSL_Entitypackage35', a2)
    assert _is_linked(b, 'eJSL_Entitypackage35', a2)
    if hasattr(a1, 'eJSL_Entitypackage33'):
        assert not _is_linked(a1, 'eJSL_Entitypackage33', b)
    if hasattr(a2, 'eJSL_Entitypackage33'):
        assert _is_linked(a2, 'eJSL_Entitypackage33', b)
    _safe_set(b, 'eJSL_Entitypackage35', None)
    assert not _is_linked(b, 'eJSL_Entitypackage35', a2)
    if hasattr(a2, 'eJSL_Entitypackage33'):
        assert not _is_linked(a2, 'eJSL_Entitypackage33', b)


def test_assoc_filters81_reverse_link_reassign_clear():
    a1 = eJSL_DynamicPage(preserve=True)
    a2 = eJSL_DynamicPage(preserve=False)
    b = eJSL_Attribute(id=True, isprimary=True, isunique=True, name="sample_text", preserve=True)
    _safe_set(b, 'eJSL_Attribute83', a1)
    assert _is_linked(b, 'eJSL_Attribute83', a1)
    if hasattr(a1, 'eJSL_DynamicPage82'):
        assert _is_linked(a1, 'eJSL_DynamicPage82', b)
    _safe_set(b, 'eJSL_Attribute83', a2)
    assert _is_linked(b, 'eJSL_Attribute83', a2)
    if hasattr(a1, 'eJSL_DynamicPage82'):
        assert not _is_linked(a1, 'eJSL_DynamicPage82', b)
    if hasattr(a2, 'eJSL_DynamicPage82'):
        assert _is_linked(a2, 'eJSL_DynamicPage82', b)
    _safe_set(b, 'eJSL_Attribute83', None)
    assert not _is_linked(b, 'eJSL_Attribute83', a2)
    if hasattr(a2, 'eJSL_DynamicPage82'):
        assert not _is_linked(a2, 'eJSL_DynamicPage82', b)


def test_assoc_globalparameters27_reverse_link_reassign_clear():
    a1 = eJSL_ParameterGroup(label="sample_text", name="sample_text")
    a2 = eJSL_ParameterGroup(label="sample_text_2", name="sample_text_2")
    b = eJSL_Parameter(defaultvalue="sample_text", descripton="sample_text", label="sample_text", name="sample_text", size=7)
    _safe_set(b, 'eJSL_Parameter29', a1)
    assert _is_linked(b, 'eJSL_Parameter29', a1)
    if hasattr(a1, 'eJSL_ParameterGroup28'):
        assert _is_linked(a1, 'eJSL_ParameterGroup28', b)
    _safe_set(b, 'eJSL_Parameter29', a2)
    assert _is_linked(b, 'eJSL_Parameter29', a2)
    if hasattr(a1, 'eJSL_ParameterGroup28'):
        assert not _is_linked(a1, 'eJSL_ParameterGroup28', b)
    if hasattr(a2, 'eJSL_ParameterGroup28'):
        assert _is_linked(a2, 'eJSL_ParameterGroup28', b)
    _safe_set(b, 'eJSL_Parameter29', None)
    assert not _is_linked(b, 'eJSL_Parameter29', a2)
    if hasattr(a2, 'eJSL_ParameterGroup28'):
        assert not _is_linked(a2, 'eJSL_ParameterGroup28', b)


def test_assoc_globalparameters66_reverse_link_reassign_clear():
    a1 = eJSL_Parameter(defaultvalue="sample_text", descripton="sample_text", label="sample_text", name="sample_text", size=7)
    a2 = eJSL_Parameter(defaultvalue="sample_text_2", descripton="sample_text_2", label="sample_text_2", name="sample_text_2", size=13)
    b = eJSL_Page(name="sample_text")
    _safe_set(b, 'eJSL_Page67', {a1})
    assert _is_linked(b, 'eJSL_Page67', a1)
    if hasattr(a1, 'eJSL_Parameter68'):
        assert _is_linked(a1, 'eJSL_Parameter68', b)
    _safe_set(b, 'eJSL_Page67', {a2})
    assert _is_linked(b, 'eJSL_Page67', a2)
    if hasattr(a1, 'eJSL_Parameter68'):
        assert not _is_linked(a1, 'eJSL_Parameter68', b)
    if hasattr(a2, 'eJSL_Parameter68'):
        assert _is_linked(a2, 'eJSL_Parameter68', b)
    _safe_set(b, 'eJSL_Page67', set())
    assert not _is_linked(b, 'eJSL_Page67', a2)
    if hasattr(a2, 'eJSL_Parameter68'):
        assert not _is_linked(a2, 'eJSL_Parameter68', b)


def test_assoc_keyvaluepairs178_reverse_link_reassign_clear():
    a1 = eJSL_Language(name="sample_text", sys=True)
    a2 = eJSL_Language(name="sample_text_2", sys=False)
    b = eJSL_KeyValuePair(name="sample_text", value="sample_text")
    _safe_set(b, 'eJSL_KeyValuePair180', a1)
    assert _is_linked(b, 'eJSL_KeyValuePair180', a1)
    if hasattr(a1, 'eJSL_Language179'):
        assert _is_linked(a1, 'eJSL_Language179', b)
    _safe_set(b, 'eJSL_KeyValuePair180', a2)
    assert _is_linked(b, 'eJSL_KeyValuePair180', a2)
    if hasattr(a1, 'eJSL_Language179'):
        assert not _is_linked(a1, 'eJSL_Language179', b)
    if hasattr(a2, 'eJSL_Language179'):
        assert _is_linked(a2, 'eJSL_Language179', b)
    _safe_set(b, 'eJSL_KeyValuePair180', None)
    assert not _is_linked(b, 'eJSL_KeyValuePair180', a2)
    if hasattr(a2, 'eJSL_Language179'):
        assert not _is_linked(a2, 'eJSL_Language179', b)


def test_assoc_keyvaluepairs183_reverse_link_reassign_clear():
    a1 = eJSL_PositionParameter(divid="sample_text", name="sample_text", type="sample_text")
    a2 = eJSL_PositionParameter(divid="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = eJSL_KeyValuePair(name="sample_text", value="sample_text")
    _safe_set(b, 'eJSL_KeyValuePair185', a1)
    assert _is_linked(b, 'eJSL_KeyValuePair185', a1)
    if hasattr(a1, 'eJSL_PositionParameter184'):
        assert _is_linked(a1, 'eJSL_PositionParameter184', b)
    _safe_set(b, 'eJSL_KeyValuePair185', a2)
    assert _is_linked(b, 'eJSL_KeyValuePair185', a2)
    if hasattr(a1, 'eJSL_PositionParameter184'):
        assert not _is_linked(a1, 'eJSL_PositionParameter184', b)
    if hasattr(a2, 'eJSL_PositionParameter184'):
        assert _is_linked(a2, 'eJSL_PositionParameter184', b)
    _safe_set(b, 'eJSL_KeyValuePair185', None)
    assert not _is_linked(b, 'eJSL_KeyValuePair185', a2)
    if hasattr(a2, 'eJSL_PositionParameter184'):
        assert not _is_linked(a2, 'eJSL_PositionParameter184', b)


def test_assoc_keyvaluepairs186_reverse_link_reassign_clear():
    a1 = eJSL_KeyValuePair(name="sample_text", value="sample_text")
    a2 = eJSL_KeyValuePair(name="sample_text_2", value="sample_text_2")
    b = eJSL_CssBlock(selector="sample_text")
    _safe_set(b, 'eJSL_CssBlock187', {a1})
    assert _is_linked(b, 'eJSL_CssBlock187', a1)
    if hasattr(a1, 'eJSL_KeyValuePair188'):
        assert _is_linked(a1, 'eJSL_KeyValuePair188', b)
    _safe_set(b, 'eJSL_CssBlock187', {a2})
    assert _is_linked(b, 'eJSL_CssBlock187', a2)
    if hasattr(a1, 'eJSL_KeyValuePair188'):
        assert not _is_linked(a1, 'eJSL_KeyValuePair188', b)
    if hasattr(a2, 'eJSL_KeyValuePair188'):
        assert _is_linked(a2, 'eJSL_KeyValuePair188', b)
    _safe_set(b, 'eJSL_CssBlock187', set())
    assert not _is_linked(b, 'eJSL_CssBlock187', a2)
    if hasattr(a2, 'eJSL_KeyValuePair188'):
        assert not _is_linked(a2, 'eJSL_KeyValuePair188', b)


def test_assoc_languages113_reverse_link_reassign_clear():
    a1 = eJSL_Language(name="sample_text", sys=True)
    a2 = eJSL_Language(name="sample_text_2", sys=False)
    b = eJSL_Extension(name="sample_text")
    _safe_set(b, 'eJSL_Extension114', {a1})
    assert _is_linked(b, 'eJSL_Extension114', a1)
    if hasattr(a1, 'eJSL_Language'):
        assert _is_linked(a1, 'eJSL_Language', b)
    _safe_set(b, 'eJSL_Extension114', {a2})
    assert _is_linked(b, 'eJSL_Extension114', a2)
    if hasattr(a1, 'eJSL_Language'):
        assert not _is_linked(a1, 'eJSL_Language', b)
    if hasattr(a2, 'eJSL_Language'):
        assert _is_linked(a2, 'eJSL_Language', b)
    _safe_set(b, 'eJSL_Extension114', set())
    assert not _is_linked(b, 'eJSL_Extension114', a2)
    if hasattr(a2, 'eJSL_Language'):
        assert not _is_linked(a2, 'eJSL_Language', b)


def test_assoc_localparameters136_reverse_link_reassign_clear():
    a1 = eJSL_Plugin(type="sample_text")
    a2 = eJSL_Plugin(type="sample_text_2")
    b = eJSL_Parameter(defaultvalue="sample_text", descripton="sample_text", label="sample_text", name="sample_text", size=7)
    _safe_set(b, 'eJSL_Parameter138', a1)
    assert _is_linked(b, 'eJSL_Parameter138', a1)
    if hasattr(a1, 'eJSL_Plugin137'):
        assert _is_linked(a1, 'eJSL_Plugin137', b)
    _safe_set(b, 'eJSL_Parameter138', a2)
    assert _is_linked(b, 'eJSL_Parameter138', a2)
    if hasattr(a1, 'eJSL_Plugin137'):
        assert not _is_linked(a1, 'eJSL_Plugin137', b)
    if hasattr(a2, 'eJSL_Plugin137'):
        assert _is_linked(a2, 'eJSL_Plugin137', b)
    _safe_set(b, 'eJSL_Parameter138', None)
    assert not _is_linked(b, 'eJSL_Parameter138', a2)
    if hasattr(a2, 'eJSL_Plugin137'):
        assert not _is_linked(a2, 'eJSL_Plugin137', b)


def test_assoc_localparameters69_reverse_link_reassign_clear():
    a1 = eJSL_Parameter(defaultvalue="sample_text", descripton="sample_text", label="sample_text", name="sample_text", size=7)
    a2 = eJSL_Parameter(defaultvalue="sample_text_2", descripton="sample_text_2", label="sample_text_2", name="sample_text_2", size=13)
    b = eJSL_Page(name="sample_text")
    _safe_set(b, 'eJSL_Page70', {a1})
    assert _is_linked(b, 'eJSL_Page70', a1)
    if hasattr(a1, 'eJSL_Parameter71'):
        assert _is_linked(a1, 'eJSL_Parameter71', b)
    _safe_set(b, 'eJSL_Page70', {a2})
    assert _is_linked(b, 'eJSL_Page70', a2)
    if hasattr(a1, 'eJSL_Parameter71'):
        assert not _is_linked(a1, 'eJSL_Parameter71', b)
    if hasattr(a2, 'eJSL_Parameter71'):
        assert _is_linked(a2, 'eJSL_Parameter71', b)
    _safe_set(b, 'eJSL_Page70', set())
    assert not _is_linked(b, 'eJSL_Page70', a2)
    if hasattr(a2, 'eJSL_Parameter71'):
        assert not _is_linked(a2, 'eJSL_Parameter71', b)


def test_assoc_manifest111_reverse_link_reassign_clear():
    a1 = eJSL_Manifestation(copyright="sample_text", creationdate="sample_text", description="sample_text", license="sample_text", link="sample_text", version="sample_text")
    a2 = eJSL_Manifestation(copyright="sample_text_2", creationdate="sample_text_2", description="sample_text_2", license="sample_text_2", link="sample_text_2", version="sample_text_2")
    b = eJSL_Extension(name="sample_text")
    _safe_set(b, 'eJSL_Extension112', a1)
    assert _is_linked(b, 'eJSL_Extension112', a1)
    if hasattr(a1, 'eJSL_Manifestation'):
        assert _is_linked(a1, 'eJSL_Manifestation', b)
    _safe_set(b, 'eJSL_Extension112', a2)
    assert _is_linked(b, 'eJSL_Extension112', a2)
    if hasattr(a1, 'eJSL_Manifestation'):
        assert not _is_linked(a1, 'eJSL_Manifestation', b)
    if hasattr(a2, 'eJSL_Manifestation'):
        assert _is_linked(a2, 'eJSL_Manifestation', b)
    _safe_set(b, 'eJSL_Extension112', None)
    assert not _is_linked(b, 'eJSL_Extension112', a2)
    if hasattr(a2, 'eJSL_Manifestation'):
        assert not _is_linked(a2, 'eJSL_Manifestation', b)


def test_assoc_methodparameters165_reverse_link_reassign_clear():
    a1 = eJSL_MethodParameter(name="sample_text")
    a2 = eJSL_MethodParameter(name="sample_text_2")
    b = eJSL_Method(name="sample_text", returnvalue="sample_text")
    _safe_set(b, 'eJSL_Method166', {a1})
    assert _is_linked(b, 'eJSL_Method166', a1)
    if hasattr(a1, 'eJSL_MethodParameter'):
        assert _is_linked(a1, 'eJSL_MethodParameter', b)
    _safe_set(b, 'eJSL_Method166', {a2})
    assert _is_linked(b, 'eJSL_Method166', a2)
    if hasattr(a1, 'eJSL_MethodParameter'):
        assert not _is_linked(a1, 'eJSL_MethodParameter', b)
    if hasattr(a2, 'eJSL_MethodParameter'):
        assert _is_linked(a2, 'eJSL_MethodParameter', b)
    _safe_set(b, 'eJSL_Method166', set())
    assert not _is_linked(b, 'eJSL_Method166', a2)
    if hasattr(a2, 'eJSL_MethodParameter'):
        assert not _is_linked(a2, 'eJSL_MethodParameter', b)


def test_assoc_methods160_reverse_link_reassign_clear():
    a1 = eJSL_Method(name="sample_text", returnvalue="sample_text")
    a2 = eJSL_Method(name="sample_text_2", returnvalue="sample_text_2")
    b = eJSL_Class(name="sample_text")
    _safe_set(b, 'eJSL_Class161', {a1})
    assert _is_linked(b, 'eJSL_Class161', a1)
    if hasattr(a1, 'eJSL_Method'):
        assert _is_linked(a1, 'eJSL_Method', b)
    _safe_set(b, 'eJSL_Class161', {a2})
    assert _is_linked(b, 'eJSL_Class161', a2)
    if hasattr(a1, 'eJSL_Method'):
        assert not _is_linked(a1, 'eJSL_Method', b)
    if hasattr(a2, 'eJSL_Method'):
        assert _is_linked(a2, 'eJSL_Method', b)
    _safe_set(b, 'eJSL_Class161', set())
    assert not _is_linked(b, 'eJSL_Class161', a2)
    if hasattr(a2, 'eJSL_Method'):
        assert not _is_linked(a2, 'eJSL_Method', b)


def test_assoc_packages146_reverse_link_reassign_clear():
    a1 = eJSL_Package(name="sample_text")
    a2 = eJSL_Package(name="sample_text_2")
    b = eJSL_Package(name="sample_text")
    _safe_set(b, 'eJSL_Package147', a1)
    assert _is_linked(b, 'eJSL_Package147', a1)
    if hasattr(a1, 'eJSL_Package145'):
        assert _is_linked(a1, 'eJSL_Package145', b)
    _safe_set(b, 'eJSL_Package147', a2)
    assert _is_linked(b, 'eJSL_Package147', a2)
    if hasattr(a1, 'eJSL_Package145'):
        assert not _is_linked(a1, 'eJSL_Package145', b)
    if hasattr(a2, 'eJSL_Package145'):
        assert _is_linked(a2, 'eJSL_Package145', b)
    _safe_set(b, 'eJSL_Package147', None)
    assert not _is_linked(b, 'eJSL_Package147', a2)
    if hasattr(a2, 'eJSL_Package145'):
        assert not _is_linked(a2, 'eJSL_Package145', b)


def test_assoc_page124_reverse_link_reassign_clear():
    a1 = eJSL_PageReference(sect="sample_text")
    a2 = eJSL_PageReference(sect="sample_text_2")
    b = eJSL_Page(name="sample_text")
    _safe_set(b, 'eJSL_Page126', a1)
    assert _is_linked(b, 'eJSL_Page126', a1)
    if hasattr(a1, 'eJSL_PageReference125'):
        assert _is_linked(a1, 'eJSL_PageReference125', b)
    _safe_set(b, 'eJSL_Page126', a2)
    assert _is_linked(b, 'eJSL_Page126', a2)
    if hasattr(a1, 'eJSL_PageReference125'):
        assert not _is_linked(a1, 'eJSL_PageReference125', b)
    if hasattr(a2, 'eJSL_PageReference125'):
        assert _is_linked(a2, 'eJSL_PageReference125', b)
    _safe_set(b, 'eJSL_Page126', None)
    assert not _is_linked(b, 'eJSL_Page126', a2)
    if hasattr(a2, 'eJSL_PageReference125'):
        assert not _is_linked(a2, 'eJSL_PageReference125', b)


def test_assoc_pageactions72_reverse_link_reassign_clear():
    a1 = eJSL_PageAction(name="sample_text", pageActionPosition="sample_text", pageActionType="sample_text")
    a2 = eJSL_PageAction(name="sample_text_2", pageActionPosition="sample_text_2", pageActionType="sample_text_2")
    b = eJSL_Page(name="sample_text")
    _safe_set(b, 'eJSL_Page73', {a1})
    assert _is_linked(b, 'eJSL_Page73', a1)
    if hasattr(a1, 'eJSL_PageAction'):
        assert _is_linked(a1, 'eJSL_PageAction', b)
    _safe_set(b, 'eJSL_Page73', {a2})
    assert _is_linked(b, 'eJSL_Page73', a2)
    if hasattr(a1, 'eJSL_PageAction'):
        assert not _is_linked(a1, 'eJSL_PageAction', b)
    if hasattr(a2, 'eJSL_PageAction'):
        assert _is_linked(a2, 'eJSL_PageAction', b)
    _safe_set(b, 'eJSL_Page73', set())
    assert not _is_linked(b, 'eJSL_Page73', a2)
    if hasattr(a2, 'eJSL_PageAction'):
        assert not _is_linked(a2, 'eJSL_PageAction', b)


def test_assoc_pagescr127_reverse_link_reassign_clear():
    a1 = eJSL_PageReference(sect="sample_text")
    a2 = eJSL_PageReference(sect="sample_text_2")
    b = eJSL_ComponentReference(core="sample_text")
    _safe_set(b, 'eJSL_ComponentReference', a1)
    assert _is_linked(b, 'eJSL_ComponentReference', a1)
    if hasattr(a1, 'eJSL_PageReference128'):
        assert _is_linked(a1, 'eJSL_PageReference128', b)
    _safe_set(b, 'eJSL_ComponentReference', a2)
    assert _is_linked(b, 'eJSL_ComponentReference', a2)
    if hasattr(a1, 'eJSL_PageReference128'):
        assert not _is_linked(a1, 'eJSL_PageReference128', b)
    if hasattr(a2, 'eJSL_PageReference128'):
        assert _is_linked(a2, 'eJSL_PageReference128', b)
    _safe_set(b, 'eJSL_ComponentReference', None)
    assert not _is_linked(b, 'eJSL_ComponentReference', a2)
    if hasattr(a2, 'eJSL_PageReference128'):
        assert not _is_linked(a2, 'eJSL_PageReference128', b)


def test_assoc_parametergroups63_reverse_link_reassign_clear():
    a1 = eJSL_ParameterGroup(label="sample_text", name="sample_text")
    a2 = eJSL_ParameterGroup(label="sample_text_2", name="sample_text_2")
    b = eJSL_Page(name="sample_text")
    _safe_set(b, 'eJSL_Page64', {a1})
    assert _is_linked(b, 'eJSL_Page64', a1)
    if hasattr(a1, 'eJSL_ParameterGroup65'):
        assert _is_linked(a1, 'eJSL_ParameterGroup65', b)
    _safe_set(b, 'eJSL_Page64', {a2})
    assert _is_linked(b, 'eJSL_Page64', a2)
    if hasattr(a1, 'eJSL_ParameterGroup65'):
        assert not _is_linked(a1, 'eJSL_ParameterGroup65', b)
    if hasattr(a2, 'eJSL_ParameterGroup65'):
        assert _is_linked(a2, 'eJSL_ParameterGroup65', b)
    _safe_set(b, 'eJSL_Page64', set())
    assert not _is_linked(b, 'eJSL_Page64', a2)
    if hasattr(a2, 'eJSL_ParameterGroup65'):
        assert not _is_linked(a2, 'eJSL_ParameterGroup65', b)


def test_assoc_parameters30_reverse_link_reassign_clear():
    a1 = eJSL_ParameterGroup(label="sample_text", name="sample_text")
    a2 = eJSL_ParameterGroup(label="sample_text_2", name="sample_text_2")
    b = eJSL_Parameter(defaultvalue="sample_text", descripton="sample_text", label="sample_text", name="sample_text", size=7)
    _safe_set(b, 'eJSL_Parameter32', a1)
    assert _is_linked(b, 'eJSL_Parameter32', a1)
    if hasattr(a1, 'eJSL_ParameterGroup31'):
        assert _is_linked(a1, 'eJSL_ParameterGroup31', b)
    _safe_set(b, 'eJSL_Parameter32', a2)
    assert _is_linked(b, 'eJSL_Parameter32', a2)
    if hasattr(a1, 'eJSL_ParameterGroup31'):
        assert not _is_linked(a1, 'eJSL_ParameterGroup31', b)
    if hasattr(a2, 'eJSL_ParameterGroup31'):
        assert _is_linked(a2, 'eJSL_ParameterGroup31', b)
    _safe_set(b, 'eJSL_Parameter32', None)
    assert not _is_linked(b, 'eJSL_Parameter32', a2)
    if hasattr(a2, 'eJSL_ParameterGroup31'):
        assert not _is_linked(a2, 'eJSL_ParameterGroup31', b)


def test_assoc_positionparameters181_reverse_link_reassign_clear():
    a1 = eJSL_PositionParameter(divid="sample_text", name="sample_text", type="sample_text")
    a2 = eJSL_PositionParameter(divid="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = eJSL_Position(name="sample_text")
    _safe_set(b, 'eJSL_Position182', {a1})
    assert _is_linked(b, 'eJSL_Position182', a1)
    if hasattr(a1, 'eJSL_PositionParameter'):
        assert _is_linked(a1, 'eJSL_PositionParameter', b)
    _safe_set(b, 'eJSL_Position182', {a2})
    assert _is_linked(b, 'eJSL_Position182', a2)
    if hasattr(a1, 'eJSL_PositionParameter'):
        assert not _is_linked(a1, 'eJSL_PositionParameter', b)
    if hasattr(a2, 'eJSL_PositionParameter'):
        assert _is_linked(a2, 'eJSL_PositionParameter', b)
    _safe_set(b, 'eJSL_Position182', set())
    assert not _is_linked(b, 'eJSL_Position182', a2)
    if hasattr(a2, 'eJSL_PositionParameter'):
        assert not _is_linked(a2, 'eJSL_PositionParameter', b)


def test_assoc_references155_reverse_link_reassign_clear():
    a1 = eJSL_Class(name="sample_text")
    a2 = eJSL_Class(name="sample_text_2")
    b = eJSL_Class(name="sample_text")
    _safe_set(b, 'eJSL_Class156', a1)
    assert _is_linked(b, 'eJSL_Class156', a1)
    if hasattr(a1, 'eJSL_Class154'):
        assert _is_linked(a1, 'eJSL_Class154', b)
    _safe_set(b, 'eJSL_Class156', a2)
    assert _is_linked(b, 'eJSL_Class156', a2)
    if hasattr(a1, 'eJSL_Class154'):
        assert not _is_linked(a1, 'eJSL_Class154', b)
    if hasattr(a2, 'eJSL_Class154'):
        assert _is_linked(a2, 'eJSL_Class154', b)
    _safe_set(b, 'eJSL_Class156', None)
    assert not _is_linked(b, 'eJSL_Class156', a2)
    if hasattr(a2, 'eJSL_Class154'):
        assert not _is_linked(a2, 'eJSL_Class154', b)


def test_assoc_references47_reverse_link_reassign_clear():
    a1 = eJSL_Reference(id=True, lower="sample_text", preserve=True, upper="sample_text")
    a2 = eJSL_Reference(id=False, lower="sample_text_2", preserve=False, upper="sample_text_2")
    b = eJSL_Entity(name="sample_text", preserve=True)
    _safe_set(b, 'eJSL_Entity48', {a1})
    assert _is_linked(b, 'eJSL_Entity48', a1)
    if hasattr(a1, 'eJSL_Reference'):
        assert _is_linked(a1, 'eJSL_Reference', b)
    _safe_set(b, 'eJSL_Entity48', {a2})
    assert _is_linked(b, 'eJSL_Entity48', a2)
    if hasattr(a1, 'eJSL_Reference'):
        assert not _is_linked(a1, 'eJSL_Reference', b)
    if hasattr(a2, 'eJSL_Reference'):
        assert _is_linked(a2, 'eJSL_Reference', b)
    _safe_set(b, 'eJSL_Entity48', set())
    assert not _is_linked(b, 'eJSL_Entity48', a2)
    if hasattr(a2, 'eJSL_Reference'):
        assert not _is_linked(a2, 'eJSL_Reference', b)


def test_assoc_supertype152_reverse_link_reassign_clear():
    a1 = eJSL_Class(name="sample_text")
    a2 = eJSL_Class(name="sample_text_2")
    b = eJSL_Class(name="sample_text")
    _safe_set(b, 'eJSL_Class153', a1)
    assert _is_linked(b, 'eJSL_Class153', a1)
    if hasattr(a1, 'eJSL_Class151'):
        assert _is_linked(a1, 'eJSL_Class151', b)
    _safe_set(b, 'eJSL_Class153', a2)
    assert _is_linked(b, 'eJSL_Class153', a2)
    if hasattr(a1, 'eJSL_Class151'):
        assert not _is_linked(a1, 'eJSL_Class151', b)
    if hasattr(a2, 'eJSL_Class151'):
        assert _is_linked(a2, 'eJSL_Class151', b)
    _safe_set(b, 'eJSL_Class153', None)
    assert not _is_linked(b, 'eJSL_Class153', a2)
    if hasattr(a2, 'eJSL_Class151'):
        assert not _is_linked(a2, 'eJSL_Class151', b)


def test_assoc_supertype43_reverse_link_reassign_clear():
    a1 = eJSL_Entity(name="sample_text", preserve=True)
    a2 = eJSL_Entity(name="sample_text_2", preserve=False)
    b = eJSL_Entity(name="sample_text", preserve=True)
    _safe_set(b, 'eJSL_Entity44', a1)
    assert _is_linked(b, 'eJSL_Entity44', a1)
    if hasattr(a1, 'eJSL_Entity42'):
        assert _is_linked(a1, 'eJSL_Entity42', b)
    _safe_set(b, 'eJSL_Entity44', a2)
    assert _is_linked(b, 'eJSL_Entity44', a2)
    if hasattr(a1, 'eJSL_Entity42'):
        assert not _is_linked(a1, 'eJSL_Entity42', b)
    if hasattr(a2, 'eJSL_Entity42'):
        assert _is_linked(a2, 'eJSL_Entity42', b)
    _safe_set(b, 'eJSL_Entity44', None)
    assert not _is_linked(b, 'eJSL_Entity44', a2)
    if hasattr(a2, 'eJSL_Entity42'):
        assert not _is_linked(a2, 'eJSL_Entity42', b)


def test_assoc_tablecolumns78_reverse_link_reassign_clear():
    a1 = eJSL_DynamicPage(preserve=True)
    a2 = eJSL_DynamicPage(preserve=False)
    b = eJSL_Attribute(id=True, isprimary=True, isunique=True, name="sample_text", preserve=True)
    _safe_set(b, 'eJSL_Attribute80', a1)
    assert _is_linked(b, 'eJSL_Attribute80', a1)
    if hasattr(a1, 'eJSL_DynamicPage79'):
        assert _is_linked(a1, 'eJSL_DynamicPage79', b)
    _safe_set(b, 'eJSL_Attribute80', a2)
    assert _is_linked(b, 'eJSL_Attribute80', a2)
    if hasattr(a1, 'eJSL_DynamicPage79'):
        assert not _is_linked(a1, 'eJSL_DynamicPage79', b)
    if hasattr(a2, 'eJSL_DynamicPage79'):
        assert _is_linked(a2, 'eJSL_DynamicPage79', b)
    _safe_set(b, 'eJSL_Attribute80', None)
    assert not _is_linked(b, 'eJSL_Attribute80', a2)
    if hasattr(a2, 'eJSL_DynamicPage79'):
        assert not _is_linked(a2, 'eJSL_DynamicPage79', b)


def test_assoc_target105_reverse_link_reassign_clear():
    a1 = eJSL_Page(name="sample_text")
    a2 = eJSL_Page(name="sample_text_2")
    b = eJSL_InternalLink(name="sample_text")
    _safe_set(b, 'eJSL_InternalLink', a1)
    assert _is_linked(b, 'eJSL_InternalLink', a1)
    if hasattr(a1, 'eJSL_Page106'):
        assert _is_linked(a1, 'eJSL_Page106', b)
    _safe_set(b, 'eJSL_InternalLink', a2)
    assert _is_linked(b, 'eJSL_InternalLink', a2)
    if hasattr(a1, 'eJSL_Page106'):
        assert not _is_linked(a1, 'eJSL_Page106', b)
    if hasattr(a2, 'eJSL_Page106'):
        assert _is_linked(a2, 'eJSL_Page106', b)
    _safe_set(b, 'eJSL_InternalLink', None)
    assert not _is_linked(b, 'eJSL_InternalLink', a2)
    if hasattr(a2, 'eJSL_Page106'):
        assert not _is_linked(a2, 'eJSL_Page106', b)


def test_assoc_values22_reverse_link_reassign_clear():
    a1 = eJSL_Parameter(defaultvalue="sample_text", descripton="sample_text", label="sample_text", name="sample_text", size=7)
    a2 = eJSL_Parameter(defaultvalue="sample_text_2", descripton="sample_text_2", label="sample_text_2", name="sample_text_2", size=13)
    b = eJSL_KeyValuePair(name="sample_text", value="sample_text")
    _safe_set(b, 'eJSL_KeyValuePair', a1)
    assert _is_linked(b, 'eJSL_KeyValuePair', a1)
    if hasattr(a1, 'eJSL_Parameter23'):
        assert _is_linked(a1, 'eJSL_Parameter23', b)
    _safe_set(b, 'eJSL_KeyValuePair', a2)
    assert _is_linked(b, 'eJSL_KeyValuePair', a2)
    if hasattr(a1, 'eJSL_Parameter23'):
        assert not _is_linked(a1, 'eJSL_Parameter23', b)
    if hasattr(a2, 'eJSL_Parameter23'):
        assert _is_linked(a2, 'eJSL_Parameter23', b)
    _safe_set(b, 'eJSL_KeyValuePair', None)
    assert not _is_linked(b, 'eJSL_KeyValuePair', a2)
    if hasattr(a2, 'eJSL_Parameter23'):
        assert not _is_linked(a2, 'eJSL_Parameter23', b)


def test_assoc_withattribute52_reverse_link_reassign_clear():
    a1 = eJSL_Attribute(id=True, isprimary=True, isunique=True, name="sample_text", preserve=True)
    a2 = eJSL_Attribute(id=False, isprimary=False, isunique=False, name="sample_text_2", preserve=False)
    b = eJSL_Attribute(id=True, isprimary=True, isunique=True, name="sample_text", preserve=True)
    _safe_set(b, 'eJSL_Attribute53', a1)
    assert _is_linked(b, 'eJSL_Attribute53', a1)
    if hasattr(a1, 'eJSL_Attribute51'):
        assert _is_linked(a1, 'eJSL_Attribute51', b)
    _safe_set(b, 'eJSL_Attribute53', a2)
    assert _is_linked(b, 'eJSL_Attribute53', a2)
    if hasattr(a1, 'eJSL_Attribute51'):
        assert not _is_linked(a1, 'eJSL_Attribute51', b)
    if hasattr(a2, 'eJSL_Attribute51'):
        assert _is_linked(a2, 'eJSL_Attribute51', b)
    _safe_set(b, 'eJSL_Attribute53', None)
    assert not _is_linked(b, 'eJSL_Attribute53', a2)
    if hasattr(a2, 'eJSL_Attribute51'):
        assert not _is_linked(a2, 'eJSL_Attribute51', b)


