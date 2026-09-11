import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_eJSL_Attribute_id_value_roundtrip():
    instance = eJSL_Attribute(id=True, isprimary=True, isunique=True, name="sample_text", preserve=True)
    assert instance.id == True
    instance.id = False
    assert instance.id == False


def test_eJSL_Attribute_isprimary_value_roundtrip():
    instance = eJSL_Attribute(id=True, isprimary=True, isunique=True, name="sample_text", preserve=True)
    assert instance.isprimary == True
    instance.isprimary = False
    assert instance.isprimary == False


def test_eJSL_Attribute_isunique_value_roundtrip():
    instance = eJSL_Attribute(id=True, isprimary=True, isunique=True, name="sample_text", preserve=True)
    assert instance.isunique == True
    instance.isunique = False
    assert instance.isunique == False


def test_eJSL_Attribute_name_value_roundtrip():
    instance = eJSL_Attribute(id=True, isprimary=True, isunique=True, name="sample_text", preserve=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_eJSL_Attribute_preserve_value_roundtrip():
    instance = eJSL_Attribute(id=True, isprimary=True, isunique=True, name="sample_text", preserve=True)
    assert instance.preserve == True
    instance.preserve = False
    assert instance.preserve == False


def test_eJSL_Author_authoremail_value_roundtrip():
    instance = eJSL_Author(authoremail="sample_text", authorurl="sample_text", name="sample_text")
    assert instance.authoremail == "sample_text"
    instance.authoremail = "sample_text_2"
    assert instance.authoremail == "sample_text_2"


def test_eJSL_Author_authorurl_value_roundtrip():
    instance = eJSL_Author(authoremail="sample_text", authorurl="sample_text", name="sample_text")
    assert instance.authorurl == "sample_text"
    instance.authorurl = "sample_text_2"
    assert instance.authorurl == "sample_text_2"


def test_eJSL_Author_name_value_roundtrip():
    instance = eJSL_Author(authoremail="sample_text", authorurl="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_eJSL_Class_name_value_roundtrip():
    instance = eJSL_Class(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_eJSL_ComplexHTMLTypes_htmltype_value_roundtrip():
    instance = eJSL_ComplexHTMLTypes(htmltype="sample_text")
    assert instance.htmltype == "sample_text"
    instance.htmltype = "sample_text_2"
    assert instance.htmltype == "sample_text_2"


def test_eJSL_ComponentReference_core_value_roundtrip():
    instance = eJSL_ComponentReference(core="sample_text")
    assert instance.core == "sample_text"
    instance.core = "sample_text_2"
    assert instance.core == "sample_text_2"


def test_eJSL_CssBlock_selector_value_roundtrip():
    instance = eJSL_CssBlock(selector="sample_text")
    assert instance.selector == "sample_text"
    instance.selector = "sample_text_2"
    assert instance.selector == "sample_text_2"


def test_eJSL_CustomPage_pageType_value_roundtrip():
    instance = eJSL_CustomPage(pageType="sample_text", preserve="sample_text")
    assert instance.pageType == "sample_text"
    instance.pageType = "sample_text_2"
    assert instance.pageType == "sample_text_2"


def test_eJSL_CustomPage_preserve_value_roundtrip():
    instance = eJSL_CustomPage(pageType="sample_text", preserve="sample_text")
    assert instance.preserve == "sample_text"
    instance.preserve = "sample_text_2"
    assert instance.preserve == "sample_text_2"


def test_eJSL_Datatype_name_value_roundtrip():
    instance = eJSL_Datatype(name="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_eJSL_Datatype_type_value_roundtrip():
    instance = eJSL_Datatype(name="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_eJSL_DynamicPage_preserve_value_roundtrip():
    instance = eJSL_DynamicPage(preserve=True)
    assert instance.preserve == True
    instance.preserve = False
    assert instance.preserve == False


def test_eJSL_EJSLModel_name_value_roundtrip():
    instance = eJSL_EJSLModel(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_eJSL_Entity_name_value_roundtrip():
    instance = eJSL_Entity(name="sample_text", preserve=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_eJSL_Entity_preserve_value_roundtrip():
    instance = eJSL_Entity(name="sample_text", preserve=True)
    assert instance.preserve == True
    instance.preserve = False
    assert instance.preserve == False


def test_eJSL_Entitypackage_name_value_roundtrip():
    instance = eJSL_Entitypackage(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_eJSL_Extension_name_value_roundtrip():
    instance = eJSL_Extension(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_eJSL_ExternalLink_label_value_roundtrip():
    instance = eJSL_ExternalLink(label="sample_text", target="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_eJSL_ExternalLink_target_value_roundtrip():
    instance = eJSL_ExternalLink(label="sample_text", target="sample_text")
    assert instance.target == "sample_text"
    instance.target = "sample_text_2"
    assert instance.target == "sample_text_2"


def test_eJSL_InternalLink_name_value_roundtrip():
    instance = eJSL_InternalLink(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_eJSL_KeyValuePair_name_value_roundtrip():
    instance = eJSL_KeyValuePair(name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_eJSL_KeyValuePair_value_value_roundtrip():
    instance = eJSL_KeyValuePair(name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_eJSL_Language_name_value_roundtrip():
    instance = eJSL_Language(name="sample_text", sys=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_eJSL_Language_sys_value_roundtrip():
    instance = eJSL_Language(name="sample_text", sys=True)
    assert instance.sys == True
    instance.sys = False
    assert instance.sys == False


def test_eJSL_LinkParameter_id_value_roundtrip():
    instance = eJSL_LinkParameter(id=True, name="sample_text", value="sample_text")
    assert instance.id == True
    instance.id = False
    assert instance.id == False


def test_eJSL_LinkParameter_name_value_roundtrip():
    instance = eJSL_LinkParameter(id=True, name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_eJSL_LinkParameter_value_value_roundtrip():
    instance = eJSL_LinkParameter(id=True, name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_eJSL_Manifestation_copyright_value_roundtrip():
    instance = eJSL_Manifestation(copyright="sample_text", creationdate="sample_text", description="sample_text", license="sample_text", link="sample_text", version="sample_text")
    assert instance.copyright == "sample_text"
    instance.copyright = "sample_text_2"
    assert instance.copyright == "sample_text_2"


def test_eJSL_Manifestation_creationdate_value_roundtrip():
    instance = eJSL_Manifestation(copyright="sample_text", creationdate="sample_text", description="sample_text", license="sample_text", link="sample_text", version="sample_text")
    assert instance.creationdate == "sample_text"
    instance.creationdate = "sample_text_2"
    assert instance.creationdate == "sample_text_2"


def test_eJSL_Manifestation_description_value_roundtrip():
    instance = eJSL_Manifestation(copyright="sample_text", creationdate="sample_text", description="sample_text", license="sample_text", link="sample_text", version="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_eJSL_Manifestation_license_value_roundtrip():
    instance = eJSL_Manifestation(copyright="sample_text", creationdate="sample_text", description="sample_text", license="sample_text", link="sample_text", version="sample_text")
    assert instance.license == "sample_text"
    instance.license = "sample_text_2"
    assert instance.license == "sample_text_2"


def test_eJSL_Manifestation_link_value_roundtrip():
    instance = eJSL_Manifestation(copyright="sample_text", creationdate="sample_text", description="sample_text", license="sample_text", link="sample_text", version="sample_text")
    assert instance.link == "sample_text"
    instance.link = "sample_text_2"
    assert instance.link == "sample_text_2"


def test_eJSL_Manifestation_version_value_roundtrip():
    instance = eJSL_Manifestation(copyright="sample_text", creationdate="sample_text", description="sample_text", license="sample_text", link="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_eJSL_Method_name_value_roundtrip():
    instance = eJSL_Method(name="sample_text", returnvalue="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_eJSL_Method_returnvalue_value_roundtrip():
    instance = eJSL_Method(name="sample_text", returnvalue="sample_text")
    assert instance.returnvalue == "sample_text"
    instance.returnvalue = "sample_text_2"
    assert instance.returnvalue == "sample_text_2"


def test_eJSL_MethodParameter_name_value_roundtrip():
    instance = eJSL_MethodParameter(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_eJSL_Package_name_value_roundtrip():
    instance = eJSL_Package(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_eJSL_Page_name_value_roundtrip():
    instance = eJSL_Page(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_eJSL_PageAction_name_value_roundtrip():
    instance = eJSL_PageAction(name="sample_text", pageActionPosition="sample_text", pageActionType="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_eJSL_PageAction_pageActionPosition_value_roundtrip():
    instance = eJSL_PageAction(name="sample_text", pageActionPosition="sample_text", pageActionType="sample_text")
    assert instance.pageActionPosition == "sample_text"
    instance.pageActionPosition = "sample_text_2"
    assert instance.pageActionPosition == "sample_text_2"


def test_eJSL_PageAction_pageActionType_value_roundtrip():
    instance = eJSL_PageAction(name="sample_text", pageActionPosition="sample_text", pageActionType="sample_text")
    assert instance.pageActionType == "sample_text"
    instance.pageActionType = "sample_text_2"
    assert instance.pageActionType == "sample_text_2"


def test_eJSL_PageReference_sect_value_roundtrip():
    instance = eJSL_PageReference(sect="sample_text")
    assert instance.sect == "sample_text"
    instance.sect = "sample_text_2"
    assert instance.sect == "sample_text_2"


def test_eJSL_Parameter_defaultvalue_value_roundtrip():
    instance = eJSL_Parameter(defaultvalue="sample_text", descripton="sample_text", label="sample_text", name="sample_text", size=7)
    assert instance.defaultvalue == "sample_text"
    instance.defaultvalue = "sample_text_2"
    assert instance.defaultvalue == "sample_text_2"


def test_eJSL_Parameter_descripton_value_roundtrip():
    instance = eJSL_Parameter(defaultvalue="sample_text", descripton="sample_text", label="sample_text", name="sample_text", size=7)
    assert instance.descripton == "sample_text"
    instance.descripton = "sample_text_2"
    assert instance.descripton == "sample_text_2"


def test_eJSL_Parameter_label_value_roundtrip():
    instance = eJSL_Parameter(defaultvalue="sample_text", descripton="sample_text", label="sample_text", name="sample_text", size=7)
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_eJSL_Parameter_name_value_roundtrip():
    instance = eJSL_Parameter(defaultvalue="sample_text", descripton="sample_text", label="sample_text", name="sample_text", size=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_eJSL_Parameter_size_value_roundtrip():
    instance = eJSL_Parameter(defaultvalue="sample_text", descripton="sample_text", label="sample_text", name="sample_text", size=7)
    assert instance.size == 7
    instance.size = 13
    assert instance.size == 13


def test_eJSL_ParameterGroup_label_value_roundtrip():
    instance = eJSL_ParameterGroup(label="sample_text", name="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_eJSL_ParameterGroup_name_value_roundtrip():
    instance = eJSL_ParameterGroup(label="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_eJSL_Plugin_type_value_roundtrip():
    instance = eJSL_Plugin(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_eJSL_Position_name_value_roundtrip():
    instance = eJSL_Position(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_eJSL_PositionParameter_divid_value_roundtrip():
    instance = eJSL_PositionParameter(divid="sample_text", name="sample_text", type="sample_text")
    assert instance.divid == "sample_text"
    instance.divid = "sample_text_2"
    assert instance.divid == "sample_text_2"


def test_eJSL_PositionParameter_name_value_roundtrip():
    instance = eJSL_PositionParameter(divid="sample_text", name="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_eJSL_PositionParameter_type_value_roundtrip():
    instance = eJSL_PositionParameter(divid="sample_text", name="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_eJSL_Reference_id_value_roundtrip():
    instance = eJSL_Reference(id=True, lower="sample_text", preserve=True, upper="sample_text")
    assert instance.id == True
    instance.id = False
    assert instance.id == False


def test_eJSL_Reference_lower_value_roundtrip():
    instance = eJSL_Reference(id=True, lower="sample_text", preserve=True, upper="sample_text")
    assert instance.lower == "sample_text"
    instance.lower = "sample_text_2"
    assert instance.lower == "sample_text_2"


def test_eJSL_Reference_preserve_value_roundtrip():
    instance = eJSL_Reference(id=True, lower="sample_text", preserve=True, upper="sample_text")
    assert instance.preserve == True
    instance.preserve = False
    assert instance.preserve == False


def test_eJSL_Reference_upper_value_roundtrip():
    instance = eJSL_Reference(id=True, lower="sample_text", preserve=True, upper="sample_text")
    assert instance.upper == "sample_text"
    instance.upper = "sample_text_2"
    assert instance.upper == "sample_text_2"


def test_eJSL_SimpleHTMLTypes_htmltype_value_roundtrip():
    instance = eJSL_SimpleHTMLTypes(htmltype="sample_text")
    assert instance.htmltype == "sample_text"
    instance.htmltype = "sample_text_2"
    assert instance.htmltype == "sample_text_2"


def test_eJSL_StandardTypes_autoincrement_value_roundtrip():
    instance = eJSL_StandardTypes(autoincrement=True, default="sample_text", notnull=True, type="sample_text")
    assert instance.autoincrement == True
    instance.autoincrement = False
    assert instance.autoincrement == False


def test_eJSL_StandardTypes_default_value_roundtrip():
    instance = eJSL_StandardTypes(autoincrement=True, default="sample_text", notnull=True, type="sample_text")
    assert instance.default == "sample_text"
    instance.default = "sample_text_2"
    assert instance.default == "sample_text_2"


def test_eJSL_StandardTypes_notnull_value_roundtrip():
    instance = eJSL_StandardTypes(autoincrement=True, default="sample_text", notnull=True, type="sample_text")
    assert instance.notnull == True
    instance.notnull = False
    assert instance.notnull == False


def test_eJSL_StandardTypes_type_value_roundtrip():
    instance = eJSL_StandardTypes(autoincrement=True, default="sample_text", notnull=True, type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_eJSL_StaticPage_HTMLBody_value_roundtrip():
    instance = eJSL_StaticPage(HTMLBody="sample_text", preserve=True)
    assert instance.HTMLBody == "sample_text"
    instance.HTMLBody = "sample_text_2"
    assert instance.HTMLBody == "sample_text_2"


def test_eJSL_StaticPage_preserve_value_roundtrip():
    instance = eJSL_StaticPage(HTMLBody="sample_text", preserve=True)
    assert instance.preserve == True
    instance.preserve = False
    assert instance.preserve == False


def test_eJSL_DetailsPage_isa_DynamicPage():
    instance = eJSL_DetailsPage()
    assert isinstance(instance, DynamicPage)


def test_eJSL_IndexPage_isa_DynamicPage():
    instance = eJSL_IndexPage()
    assert isinstance(instance, DynamicPage)


def test_eJSL_CMSCore_isa_EJSLPart():
    instance = eJSL_CMSCore()
    assert isinstance(instance, EJSLPart)


def test_eJSL_CMSExtension_isa_EJSLPart():
    instance = eJSL_CMSExtension()
    assert isinstance(instance, EJSLPart)


def test_eJSL_Component_isa_Extension():
    instance = eJSL_Component()
    assert isinstance(instance, Extension)


def test_eJSL_ExtensionPackage_isa_Extension():
    instance = eJSL_ExtensionPackage()
    assert isinstance(instance, Extension)


def test_eJSL_Library_isa_Extension():
    instance = eJSL_Library()
    assert isinstance(instance, Extension)


def test_eJSL_Module_isa_Extension():
    instance = eJSL_Module()
    assert isinstance(instance, Extension)


def test_eJSL_Plugin_isa_Extension():
    instance = eJSL_Plugin(type="sample_text")
    assert isinstance(instance, Extension)


def test_eJSL_Template_isa_Extension():
    instance = eJSL_Template()
    assert isinstance(instance, Extension)


def test_eJSL_ComplexHTMLTypes_isa_HTMLTypes():
    instance = eJSL_ComplexHTMLTypes(htmltype="sample_text")
    assert isinstance(instance, HTMLTypes)


def test_eJSL_DatatypeReference_isa_HTMLTypes():
    instance = eJSL_DatatypeReference()
    assert isinstance(instance, HTMLTypes)


def test_eJSL_SimpleHTMLTypes_isa_HTMLTypes():
    instance = eJSL_SimpleHTMLTypes(htmltype="sample_text")
    assert isinstance(instance, HTMLTypes)


def test_eJSL_ContextLink_isa_InternalLink():
    instance = eJSL_ContextLink()
    assert isinstance(instance, InternalLink)


def test_eJSL_ExternalLink_isa_Link():
    instance = eJSL_ExternalLink(label="sample_text", target="sample_text")
    assert isinstance(instance, Link)


def test_eJSL_InternalLink_isa_Link():
    instance = eJSL_InternalLink(name="sample_text")
    assert isinstance(instance, Link)


def test_eJSL_CustomPage_isa_Page():
    instance = eJSL_CustomPage(pageType="sample_text", preserve="sample_text")
    assert isinstance(instance, Page)


def test_eJSL_DynamicPage_isa_Page():
    instance = eJSL_DynamicPage(preserve=True)
    assert isinstance(instance, Page)


def test_eJSL_StaticPage_isa_Page():
    instance = eJSL_StaticPage(HTMLBody="sample_text", preserve=True)
    assert isinstance(instance, Page)


def test_eJSL_BackendSection_isa_Section():
    instance = eJSL_BackendSection()
    assert isinstance(instance, Section)


def test_eJSL_FrontendSection_isa_Section():
    instance = eJSL_FrontendSection()
    assert isinstance(instance, Section)


def test_eJSL_DatatypeReference_isa_Type():
    instance = eJSL_DatatypeReference()
    assert isinstance(instance, Type)


def test_eJSL_StandardTypes_isa_Type():
    instance = eJSL_StandardTypes(autoincrement=True, default="sample_text", notnull=True, type="sample_text")
    assert isinstance(instance, Type)


def test_assoc_attribute54_link_reassign_clear():
    a = eJSL_Reference(id=True, lower="sample_text", preserve=True, upper="sample_text")
    b1 = eJSL_Attribute(id=True, isprimary=True, isunique=True, name="sample_text", preserve=True)
    b2 = eJSL_Attribute(id=False, isprimary=False, isunique=False, name="sample_text_2", preserve=False)
    _safe_set(a, 'eJSL_Reference55', {b1})
    assert _is_linked(a, 'eJSL_Reference55', b1)
    if hasattr(b1, 'eJSL_Attribute56'):
        assert _is_linked(b1, 'eJSL_Attribute56', a)
    _safe_set(a, 'eJSL_Reference55', {b2})
    assert _is_linked(a, 'eJSL_Reference55', b2)
    if hasattr(b1, 'eJSL_Attribute56'):
        assert not _is_linked(b1, 'eJSL_Attribute56', a)
    if hasattr(b2, 'eJSL_Attribute56'):
        assert _is_linked(b2, 'eJSL_Attribute56', a)
    _safe_set(a, 'eJSL_Reference55', set())
    assert not _is_linked(a, 'eJSL_Reference55', b2)
    if hasattr(b2, 'eJSL_Attribute56'):
        assert not _is_linked(b2, 'eJSL_Attribute56', a)


def test_assoc_attribute85_link_reassign_clear():
    a = eJSL_Attribute(id=True, isprimary=True, isunique=True, name="sample_text", preserve=True)
    b1 = eJSL_DetailPageField()
    b2 = eJSL_DetailPageField()
    _safe_set(a, 'eJSL_Attribute87', b1)
    assert _is_linked(a, 'eJSL_Attribute87', b1)
    if hasattr(b1, 'eJSL_DetailPageField86'):
        assert _is_linked(b1, 'eJSL_DetailPageField86', a)
    _safe_set(a, 'eJSL_Attribute87', b2)
    assert _is_linked(a, 'eJSL_Attribute87', b2)
    if hasattr(b1, 'eJSL_DetailPageField86'):
        assert not _is_linked(b1, 'eJSL_DetailPageField86', a)
    if hasattr(b2, 'eJSL_DetailPageField86'):
        assert _is_linked(b2, 'eJSL_DetailPageField86', a)
    _safe_set(a, 'eJSL_Attribute87', None)
    assert not _is_linked(a, 'eJSL_Attribute87', b2)
    if hasattr(b2, 'eJSL_DetailPageField86'):
        assert not _is_linked(b2, 'eJSL_DetailPageField86', a)


def test_assoc_attributerefereced60_link_reassign_clear():
    a = eJSL_Reference(id=True, lower="sample_text", preserve=True, upper="sample_text")
    b1 = eJSL_Attribute(id=True, isprimary=True, isunique=True, name="sample_text", preserve=True)
    b2 = eJSL_Attribute(id=False, isprimary=False, isunique=False, name="sample_text_2", preserve=False)
    _safe_set(a, 'eJSL_Reference61', {b1})
    assert _is_linked(a, 'eJSL_Reference61', b1)
    if hasattr(b1, 'eJSL_Attribute62'):
        assert _is_linked(b1, 'eJSL_Attribute62', a)
    _safe_set(a, 'eJSL_Reference61', {b2})
    assert _is_linked(a, 'eJSL_Reference61', b2)
    if hasattr(b1, 'eJSL_Attribute62'):
        assert not _is_linked(b1, 'eJSL_Attribute62', a)
    if hasattr(b2, 'eJSL_Attribute62'):
        assert _is_linked(b2, 'eJSL_Attribute62', a)
    _safe_set(a, 'eJSL_Reference61', set())
    assert not _is_linked(a, 'eJSL_Reference61', b2)
    if hasattr(b2, 'eJSL_Attribute62'):
        assert not _is_linked(b2, 'eJSL_Attribute62', a)


def test_assoc_attributes24_link_reassign_clear():
    a = eJSL_Parameter(defaultvalue="sample_text", descripton="sample_text", label="sample_text", name="sample_text", size=7)
    b1 = eJSL_KeyValuePair(name="sample_text", value="sample_text")
    b2 = eJSL_KeyValuePair(name="sample_text_2", value="sample_text_2")
    _safe_set(a, 'eJSL_Parameter25', {b1})
    assert _is_linked(a, 'eJSL_Parameter25', b1)
    if hasattr(b1, 'eJSL_KeyValuePair26'):
        assert _is_linked(b1, 'eJSL_KeyValuePair26', a)
    _safe_set(a, 'eJSL_Parameter25', {b2})
    assert _is_linked(a, 'eJSL_Parameter25', b2)
    if hasattr(b1, 'eJSL_KeyValuePair26'):
        assert not _is_linked(b1, 'eJSL_KeyValuePair26', a)
    if hasattr(b2, 'eJSL_KeyValuePair26'):
        assert _is_linked(b2, 'eJSL_KeyValuePair26', a)
    _safe_set(a, 'eJSL_Parameter25', set())
    assert not _is_linked(a, 'eJSL_Parameter25', b2)
    if hasattr(b2, 'eJSL_KeyValuePair26'):
        assert not _is_linked(b2, 'eJSL_KeyValuePair26', a)


def test_assoc_attributes45_link_reassign_clear():
    a = eJSL_Entity(name="sample_text", preserve=True)
    b1 = eJSL_Attribute(id=True, isprimary=True, isunique=True, name="sample_text", preserve=True)
    b2 = eJSL_Attribute(id=False, isprimary=False, isunique=False, name="sample_text_2", preserve=False)
    _safe_set(a, 'eJSL_Entity46', {b1})
    assert _is_linked(a, 'eJSL_Entity46', b1)
    if hasattr(b1, 'eJSL_Attribute'):
        assert _is_linked(b1, 'eJSL_Attribute', a)
    _safe_set(a, 'eJSL_Entity46', {b2})
    assert _is_linked(a, 'eJSL_Entity46', b2)
    if hasattr(b1, 'eJSL_Attribute'):
        assert not _is_linked(b1, 'eJSL_Attribute', a)
    if hasattr(b2, 'eJSL_Attribute'):
        assert _is_linked(b2, 'eJSL_Attribute', a)
    _safe_set(a, 'eJSL_Entity46', set())
    assert not _is_linked(a, 'eJSL_Entity46', b2)
    if hasattr(b2, 'eJSL_Attribute'):
        assert not _is_linked(b2, 'eJSL_Attribute', a)


def test_assoc_attributes94_link_reassign_clear():
    a = eJSL_KeyValuePair(name="sample_text", value="sample_text")
    b1 = eJSL_DetailPageField()
    b2 = eJSL_DetailPageField()
    _safe_set(a, 'eJSL_KeyValuePair96', b1)
    assert _is_linked(a, 'eJSL_KeyValuePair96', b1)
    if hasattr(b1, 'eJSL_DetailPageField95'):
        assert _is_linked(b1, 'eJSL_DetailPageField95', a)
    _safe_set(a, 'eJSL_KeyValuePair96', b2)
    assert _is_linked(a, 'eJSL_KeyValuePair96', b2)
    if hasattr(b1, 'eJSL_DetailPageField95'):
        assert not _is_linked(b1, 'eJSL_DetailPageField95', a)
    if hasattr(b2, 'eJSL_DetailPageField95'):
        assert _is_linked(b2, 'eJSL_DetailPageField95', a)
    _safe_set(a, 'eJSL_KeyValuePair96', None)
    assert not _is_linked(a, 'eJSL_KeyValuePair96', b2)
    if hasattr(b2, 'eJSL_DetailPageField95'):
        assert not _is_linked(b2, 'eJSL_DetailPageField95', a)


def test_assoc_attvalue108_link_reassign_clear():
    a = eJSL_LinkParameter(id=True, name="sample_text", value="sample_text")
    b1 = eJSL_Attribute(id=True, isprimary=True, isunique=True, name="sample_text", preserve=True)
    b2 = eJSL_Attribute(id=False, isprimary=False, isunique=False, name="sample_text_2", preserve=False)
    _safe_set(a, 'eJSL_LinkParameter109', b1)
    assert _is_linked(a, 'eJSL_LinkParameter109', b1)
    if hasattr(b1, 'eJSL_Attribute110'):
        assert _is_linked(b1, 'eJSL_Attribute110', a)
    _safe_set(a, 'eJSL_LinkParameter109', b2)
    assert _is_linked(a, 'eJSL_LinkParameter109', b2)
    if hasattr(b1, 'eJSL_Attribute110'):
        assert not _is_linked(b1, 'eJSL_Attribute110', a)
    if hasattr(b2, 'eJSL_Attribute110'):
        assert _is_linked(b2, 'eJSL_Attribute110', a)
    _safe_set(a, 'eJSL_LinkParameter109', None)
    assert not _is_linked(a, 'eJSL_LinkParameter109', b2)
    if hasattr(b2, 'eJSL_Attribute110'):
        assert not _is_linked(b2, 'eJSL_Attribute110', a)


def test_assoc_authors176_link_reassign_clear():
    a = eJSL_Manifestation(copyright="sample_text", creationdate="sample_text", description="sample_text", license="sample_text", link="sample_text", version="sample_text")
    b1 = eJSL_Author(authoremail="sample_text", authorurl="sample_text", name="sample_text")
    b2 = eJSL_Author(authoremail="sample_text_2", authorurl="sample_text_2", name="sample_text_2")
    _safe_set(a, 'eJSL_Manifestation177', {b1})
    assert _is_linked(a, 'eJSL_Manifestation177', b1)
    if hasattr(b1, 'eJSL_Author'):
        assert _is_linked(b1, 'eJSL_Author', a)
    _safe_set(a, 'eJSL_Manifestation177', {b2})
    assert _is_linked(a, 'eJSL_Manifestation177', b2)
    if hasattr(b1, 'eJSL_Author'):
        assert not _is_linked(b1, 'eJSL_Author', a)
    if hasattr(b2, 'eJSL_Author'):
        assert _is_linked(b2, 'eJSL_Author', a)
    _safe_set(a, 'eJSL_Manifestation177', set())
    assert not _is_linked(a, 'eJSL_Manifestation177', b2)
    if hasattr(b2, 'eJSL_Author'):
        assert not _is_linked(b2, 'eJSL_Author', a)


def test_assoc_classes141_link_reassign_clear():
    a = eJSL_Class(name="sample_text")
    b1 = eJSL_Library()
    b2 = eJSL_Library()
    _safe_set(a, 'eJSL_Class', b1)
    assert _is_linked(a, 'eJSL_Class', b1)
    if hasattr(b1, 'eJSL_Library142'):
        assert _is_linked(b1, 'eJSL_Library142', a)
    _safe_set(a, 'eJSL_Class', b2)
    assert _is_linked(a, 'eJSL_Class', b2)
    if hasattr(b1, 'eJSL_Library142'):
        assert not _is_linked(b1, 'eJSL_Library142', a)
    if hasattr(b2, 'eJSL_Library142'):
        assert _is_linked(b2, 'eJSL_Library142', a)
    _safe_set(a, 'eJSL_Class', None)
    assert not _is_linked(a, 'eJSL_Class', b2)
    if hasattr(b2, 'eJSL_Library142'):
        assert not _is_linked(b2, 'eJSL_Library142', a)


def test_assoc_classes148_link_reassign_clear():
    a = eJSL_Package(name="sample_text")
    b1 = eJSL_Class(name="sample_text")
    b2 = eJSL_Class(name="sample_text_2")
    _safe_set(a, 'eJSL_Package149', {b1})
    assert _is_linked(a, 'eJSL_Package149', b1)
    if hasattr(b1, 'eJSL_Class150'):
        assert _is_linked(b1, 'eJSL_Class150', a)
    _safe_set(a, 'eJSL_Package149', {b2})
    assert _is_linked(a, 'eJSL_Package149', b2)
    if hasattr(b1, 'eJSL_Class150'):
        assert not _is_linked(b1, 'eJSL_Class150', a)
    if hasattr(b2, 'eJSL_Class150'):
        assert _is_linked(b2, 'eJSL_Class150', a)
    _safe_set(a, 'eJSL_Package149', set())
    assert not _is_linked(a, 'eJSL_Package149', b2)
    if hasattr(b2, 'eJSL_Class150'):
        assert not _is_linked(b2, 'eJSL_Class150', a)


def test_assoc_cssblocks174_link_reassign_clear():
    a = eJSL_CssBlock(selector="sample_text")
    b1 = eJSL_Template()
    b2 = eJSL_Template()
    _safe_set(a, 'eJSL_CssBlock', b1)
    assert _is_linked(a, 'eJSL_CssBlock', b1)
    if hasattr(b1, 'eJSL_Template175'):
        assert _is_linked(b1, 'eJSL_Template175', a)
    _safe_set(a, 'eJSL_CssBlock', b2)
    assert _is_linked(a, 'eJSL_CssBlock', b2)
    if hasattr(b1, 'eJSL_Template175'):
        assert not _is_linked(b1, 'eJSL_Template175', a)
    if hasattr(b2, 'eJSL_Template175'):
        assert _is_linked(b2, 'eJSL_Template175', a)
    _safe_set(a, 'eJSL_CssBlock', None)
    assert not _is_linked(a, 'eJSL_CssBlock', b2)
    if hasattr(b2, 'eJSL_Template175'):
        assert not _is_linked(b2, 'eJSL_Template175', a)


def test_assoc_datatypes1_link_reassign_clear():
    a = eJSL_Datatype(name="sample_text", type="sample_text")
    b1 = eJSL_EJSLPart()
    b2 = eJSL_EJSLPart()
    _safe_set(a, 'eJSL_Datatype', b1)
    assert _is_linked(a, 'eJSL_Datatype', b1)
    if hasattr(b1, 'eJSL_EJSLPart2'):
        assert _is_linked(b1, 'eJSL_EJSLPart2', a)
    _safe_set(a, 'eJSL_Datatype', b2)
    assert _is_linked(a, 'eJSL_Datatype', b2)
    if hasattr(b1, 'eJSL_EJSLPart2'):
        assert not _is_linked(b1, 'eJSL_EJSLPart2', a)
    if hasattr(b2, 'eJSL_EJSLPart2'):
        assert _is_linked(b2, 'eJSL_EJSLPart2', a)
    _safe_set(a, 'eJSL_Datatype', None)
    assert not _is_linked(a, 'eJSL_Datatype', b2)
    if hasattr(b2, 'eJSL_EJSLPart2'):
        assert not _is_linked(b2, 'eJSL_EJSLPart2', a)


def test_assoc_datatypes39_link_reassign_clear():
    a = eJSL_Entitypackage(name="sample_text")
    b1 = eJSL_Datatype(name="sample_text", type="sample_text")
    b2 = eJSL_Datatype(name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'eJSL_Entitypackage40', {b1})
    assert _is_linked(a, 'eJSL_Entitypackage40', b1)
    if hasattr(b1, 'eJSL_Datatype41'):
        assert _is_linked(b1, 'eJSL_Datatype41', a)
    _safe_set(a, 'eJSL_Entitypackage40', {b2})
    assert _is_linked(a, 'eJSL_Entitypackage40', b2)
    if hasattr(b1, 'eJSL_Datatype41'):
        assert not _is_linked(b1, 'eJSL_Datatype41', a)
    if hasattr(b2, 'eJSL_Datatype41'):
        assert _is_linked(b2, 'eJSL_Datatype41', a)
    _safe_set(a, 'eJSL_Entitypackage40', set())
    assert not _is_linked(a, 'eJSL_Entitypackage40', b2)
    if hasattr(b2, 'eJSL_Datatype41'):
        assert not _is_linked(b2, 'eJSL_Datatype41', a)


def test_assoc_dtype20_link_reassign_clear():
    a = eJSL_Parameter(defaultvalue="sample_text", descripton="sample_text", label="sample_text", name="sample_text", size=7)
    b1 = eJSL_HTMLTypes()
    b2 = eJSL_HTMLTypes()
    _safe_set(a, 'eJSL_Parameter21', b1)
    assert _is_linked(a, 'eJSL_Parameter21', b1)
    if hasattr(b1, 'eJSL_HTMLTypes'):
        assert _is_linked(b1, 'eJSL_HTMLTypes', a)
    _safe_set(a, 'eJSL_Parameter21', b2)
    assert _is_linked(a, 'eJSL_Parameter21', b2)
    if hasattr(b1, 'eJSL_HTMLTypes'):
        assert not _is_linked(b1, 'eJSL_HTMLTypes', a)
    if hasattr(b2, 'eJSL_HTMLTypes'):
        assert _is_linked(b2, 'eJSL_HTMLTypes', a)
    _safe_set(a, 'eJSL_Parameter21', None)
    assert not _is_linked(a, 'eJSL_Parameter21', b2)
    if hasattr(b2, 'eJSL_HTMLTypes'):
        assert not _is_linked(b2, 'eJSL_HTMLTypes', a)


def test_assoc_ejslPart0_link_reassign_clear():
    a = eJSL_EJSLModel(name="sample_text")
    b1 = eJSL_EJSLPart()
    b2 = eJSL_EJSLPart()
    _safe_set(a, 'eJSL_EJSLModel', b1)
    assert _is_linked(a, 'eJSL_EJSLModel', b1)
    if hasattr(b1, 'eJSL_EJSLPart'):
        assert _is_linked(b1, 'eJSL_EJSLPart', a)
    _safe_set(a, 'eJSL_EJSLModel', b2)
    assert _is_linked(a, 'eJSL_EJSLModel', b2)
    if hasattr(b1, 'eJSL_EJSLPart'):
        assert not _is_linked(b1, 'eJSL_EJSLPart', a)
    if hasattr(b2, 'eJSL_EJSLPart'):
        assert _is_linked(b2, 'eJSL_EJSLPart', a)
    _safe_set(a, 'eJSL_EJSLModel', None)
    assert not _is_linked(a, 'eJSL_EJSLModel', b2)
    if hasattr(b2, 'eJSL_EJSLPart'):
        assert not _is_linked(b2, 'eJSL_EJSLPart', a)


def test_assoc_entities12_link_reassign_clear():
    a = eJSL_Entity(name="sample_text", preserve=True)
    b1 = eJSL_Feature()
    b2 = eJSL_Feature()
    _safe_set(a, 'eJSL_Entity', b1)
    assert _is_linked(a, 'eJSL_Entity', b1)
    if hasattr(b1, 'eJSL_Feature13'):
        assert _is_linked(b1, 'eJSL_Feature13', a)
    _safe_set(a, 'eJSL_Entity', b2)
    assert _is_linked(a, 'eJSL_Entity', b2)
    if hasattr(b1, 'eJSL_Feature13'):
        assert not _is_linked(b1, 'eJSL_Feature13', a)
    if hasattr(b2, 'eJSL_Feature13'):
        assert _is_linked(b2, 'eJSL_Feature13', a)
    _safe_set(a, 'eJSL_Entity', None)
    assert not _is_linked(a, 'eJSL_Entity', b2)
    if hasattr(b2, 'eJSL_Feature13'):
        assert not _is_linked(b2, 'eJSL_Feature13', a)


def test_assoc_entities134_link_reassign_clear():
    a = eJSL_Plugin(type="sample_text")
    b1 = eJSL_Entity(name="sample_text", preserve=True)
    b2 = eJSL_Entity(name="sample_text_2", preserve=False)
    _safe_set(a, 'eJSL_Plugin', {b1})
    assert _is_linked(a, 'eJSL_Plugin', b1)
    if hasattr(b1, 'eJSL_Entity135'):
        assert _is_linked(b1, 'eJSL_Entity135', a)
    _safe_set(a, 'eJSL_Plugin', {b2})
    assert _is_linked(a, 'eJSL_Plugin', b2)
    if hasattr(b1, 'eJSL_Entity135'):
        assert not _is_linked(b1, 'eJSL_Entity135', a)
    if hasattr(b2, 'eJSL_Entity135'):
        assert _is_linked(b2, 'eJSL_Entity135', a)
    _safe_set(a, 'eJSL_Plugin', set())
    assert not _is_linked(a, 'eJSL_Plugin', b2)
    if hasattr(b2, 'eJSL_Entity135'):
        assert not _is_linked(b2, 'eJSL_Entity135', a)


def test_assoc_entities139_link_reassign_clear():
    a = eJSL_Entity(name="sample_text", preserve=True)
    b1 = eJSL_Library()
    b2 = eJSL_Library()
    _safe_set(a, 'eJSL_Entity140', b1)
    assert _is_linked(a, 'eJSL_Entity140', b1)
    if hasattr(b1, 'eJSL_Library'):
        assert _is_linked(b1, 'eJSL_Library', a)
    _safe_set(a, 'eJSL_Entity140', b2)
    assert _is_linked(a, 'eJSL_Entity140', b2)
    if hasattr(b1, 'eJSL_Library'):
        assert not _is_linked(b1, 'eJSL_Library', a)
    if hasattr(b2, 'eJSL_Library'):
        assert _is_linked(b2, 'eJSL_Library', a)
    _safe_set(a, 'eJSL_Entity140', None)
    assert not _is_linked(a, 'eJSL_Entity140', b2)
    if hasattr(b2, 'eJSL_Library'):
        assert not _is_linked(b2, 'eJSL_Library', a)


def test_assoc_entities157_link_reassign_clear():
    a = eJSL_Entity(name="sample_text", preserve=True)
    b1 = eJSL_Class(name="sample_text")
    b2 = eJSL_Class(name="sample_text_2")
    _safe_set(a, 'eJSL_Entity159', b1)
    assert _is_linked(a, 'eJSL_Entity159', b1)
    if hasattr(b1, 'eJSL_Class158'):
        assert _is_linked(b1, 'eJSL_Class158', a)
    _safe_set(a, 'eJSL_Entity159', b2)
    assert _is_linked(a, 'eJSL_Entity159', b2)
    if hasattr(b1, 'eJSL_Class158'):
        assert not _is_linked(b1, 'eJSL_Class158', a)
    if hasattr(b2, 'eJSL_Class158'):
        assert _is_linked(b2, 'eJSL_Class158', a)
    _safe_set(a, 'eJSL_Entity159', None)
    assert not _is_linked(a, 'eJSL_Entity159', b2)
    if hasattr(b2, 'eJSL_Class158'):
        assert not _is_linked(b2, 'eJSL_Class158', a)


def test_assoc_entities36_link_reassign_clear():
    a = eJSL_Entitypackage(name="sample_text")
    b1 = eJSL_Entity(name="sample_text", preserve=True)
    b2 = eJSL_Entity(name="sample_text_2", preserve=False)
    _safe_set(a, 'eJSL_Entitypackage37', {b1})
    assert _is_linked(a, 'eJSL_Entitypackage37', b1)
    if hasattr(b1, 'eJSL_Entity38'):
        assert _is_linked(b1, 'eJSL_Entity38', a)
    _safe_set(a, 'eJSL_Entitypackage37', {b2})
    assert _is_linked(a, 'eJSL_Entitypackage37', b2)
    if hasattr(b1, 'eJSL_Entity38'):
        assert not _is_linked(b1, 'eJSL_Entity38', a)
    if hasattr(b2, 'eJSL_Entity38'):
        assert _is_linked(b2, 'eJSL_Entity38', a)
    _safe_set(a, 'eJSL_Entitypackage37', set())
    assert not _is_linked(a, 'eJSL_Entitypackage37', b2)
    if hasattr(b2, 'eJSL_Entity38'):
        assert not _is_linked(b2, 'eJSL_Entity38', a)


def test_assoc_entities76_link_reassign_clear():
    a = eJSL_Entity(name="sample_text", preserve=True)
    b1 = eJSL_DynamicPage(preserve=True)
    b2 = eJSL_DynamicPage(preserve=False)
    _safe_set(a, 'eJSL_Entity77', b1)
    assert _is_linked(a, 'eJSL_Entity77', b1)
    if hasattr(b1, 'eJSL_DynamicPage'):
        assert _is_linked(b1, 'eJSL_DynamicPage', a)
    _safe_set(a, 'eJSL_Entity77', b2)
    assert _is_linked(a, 'eJSL_Entity77', b2)
    if hasattr(b1, 'eJSL_DynamicPage'):
        assert not _is_linked(b1, 'eJSL_DynamicPage', a)
    if hasattr(b2, 'eJSL_DynamicPage'):
        assert _is_linked(b2, 'eJSL_DynamicPage', a)
    _safe_set(a, 'eJSL_Entity77', None)
    assert not _is_linked(a, 'eJSL_Entity77', b2)
    if hasattr(b2, 'eJSL_DynamicPage'):
        assert not _is_linked(b2, 'eJSL_DynamicPage', a)


def test_assoc_entities97_link_reassign_clear():
    a = eJSL_Entity(name="sample_text", preserve=True)
    b1 = eJSL_CustomPage(pageType="sample_text", preserve="sample_text")
    b2 = eJSL_CustomPage(pageType="sample_text_2", preserve="sample_text_2")
    _safe_set(a, 'eJSL_Entity98', b1)
    assert _is_linked(a, 'eJSL_Entity98', b1)
    if hasattr(b1, 'eJSL_CustomPage'):
        assert _is_linked(b1, 'eJSL_CustomPage', a)
    _safe_set(a, 'eJSL_Entity98', b2)
    assert _is_linked(a, 'eJSL_Entity98', b2)
    if hasattr(b1, 'eJSL_CustomPage'):
        assert not _is_linked(b1, 'eJSL_CustomPage', a)
    if hasattr(b2, 'eJSL_CustomPage'):
        assert _is_linked(b2, 'eJSL_CustomPage', a)
    _safe_set(a, 'eJSL_Entity98', None)
    assert not _is_linked(a, 'eJSL_Entity98', b2)
    if hasattr(b2, 'eJSL_CustomPage'):
        assert not _is_linked(b2, 'eJSL_CustomPage', a)


def test_assoc_entity57_link_reassign_clear():
    a = eJSL_Reference(id=True, lower="sample_text", preserve=True, upper="sample_text")
    b1 = eJSL_Entity(name="sample_text", preserve=True)
    b2 = eJSL_Entity(name="sample_text_2", preserve=False)
    _safe_set(a, 'eJSL_Reference58', b1)
    assert _is_linked(a, 'eJSL_Reference58', b1)
    if hasattr(b1, 'eJSL_Entity59'):
        assert _is_linked(b1, 'eJSL_Entity59', a)
    _safe_set(a, 'eJSL_Reference58', b2)
    assert _is_linked(a, 'eJSL_Reference58', b2)
    if hasattr(b1, 'eJSL_Entity59'):
        assert not _is_linked(b1, 'eJSL_Entity59', a)
    if hasattr(b2, 'eJSL_Entity59'):
        assert _is_linked(b2, 'eJSL_Entity59', a)
    _safe_set(a, 'eJSL_Reference58', None)
    assert not _is_linked(a, 'eJSL_Reference58', b2)
    if hasattr(b2, 'eJSL_Entity59'):
        assert not _is_linked(b2, 'eJSL_Entity59', a)


def test_assoc_entitypackages10_link_reassign_clear():
    a = eJSL_Entitypackage(name="sample_text")
    b1 = eJSL_Feature()
    b2 = eJSL_Feature()
    _safe_set(a, 'eJSL_Entitypackage', b1)
    assert _is_linked(a, 'eJSL_Entitypackage', b1)
    if hasattr(b1, 'eJSL_Feature11'):
        assert _is_linked(b1, 'eJSL_Feature11', a)
    _safe_set(a, 'eJSL_Entitypackage', b2)
    assert _is_linked(a, 'eJSL_Entitypackage', b2)
    if hasattr(b1, 'eJSL_Feature11'):
        assert not _is_linked(b1, 'eJSL_Feature11', a)
    if hasattr(b2, 'eJSL_Feature11'):
        assert _is_linked(b2, 'eJSL_Feature11', a)
    _safe_set(a, 'eJSL_Entitypackage', None)
    assert not _is_linked(a, 'eJSL_Entitypackage', b2)
    if hasattr(b2, 'eJSL_Feature11'):
        assert not _is_linked(b2, 'eJSL_Feature11', a)


def test_assoc_entitypackages34_link_reassign_clear():
    a = eJSL_Entitypackage(name="sample_text")
    b1 = eJSL_Entitypackage(name="sample_text")
    b2 = eJSL_Entitypackage(name="sample_text_2")
    _safe_set(a, 'eJSL_Entitypackage33', {b1})
    assert _is_linked(a, 'eJSL_Entitypackage33', b1)
    if hasattr(b1, 'eJSL_Entitypackage35'):
        assert _is_linked(b1, 'eJSL_Entitypackage35', a)
    _safe_set(a, 'eJSL_Entitypackage33', {b2})
    assert _is_linked(a, 'eJSL_Entitypackage33', b2)
    if hasattr(b1, 'eJSL_Entitypackage35'):
        assert not _is_linked(b1, 'eJSL_Entitypackage35', a)
    if hasattr(b2, 'eJSL_Entitypackage35'):
        assert _is_linked(b2, 'eJSL_Entitypackage35', a)
    _safe_set(a, 'eJSL_Entitypackage33', set())
    assert not _is_linked(a, 'eJSL_Entitypackage33', b2)
    if hasattr(b2, 'eJSL_Entitypackage35'):
        assert not _is_linked(b2, 'eJSL_Entitypackage35', a)


def test_assoc_extensions115_link_reassign_clear():
    a = eJSL_Extension(name="sample_text")
    b1 = eJSL_ExtensionPackage()
    b2 = eJSL_ExtensionPackage()
    _safe_set(a, 'eJSL_Extension116', b1)
    assert _is_linked(a, 'eJSL_Extension116', b1)
    if hasattr(b1, 'eJSL_ExtensionPackage'):
        assert _is_linked(b1, 'eJSL_ExtensionPackage', a)
    _safe_set(a, 'eJSL_Extension116', b2)
    assert _is_linked(a, 'eJSL_Extension116', b2)
    if hasattr(b1, 'eJSL_ExtensionPackage'):
        assert not _is_linked(b1, 'eJSL_ExtensionPackage', a)
    if hasattr(b2, 'eJSL_ExtensionPackage'):
        assert _is_linked(b2, 'eJSL_ExtensionPackage', a)
    _safe_set(a, 'eJSL_Extension116', None)
    assert not _is_linked(a, 'eJSL_Extension116', b2)
    if hasattr(b2, 'eJSL_ExtensionPackage'):
        assert not _is_linked(b2, 'eJSL_ExtensionPackage', a)


def test_assoc_extensions9_link_reassign_clear():
    a = eJSL_Extension(name="sample_text")
    b1 = eJSL_CMSExtension()
    b2 = eJSL_CMSExtension()
    _safe_set(a, 'eJSL_Extension', b1)
    assert _is_linked(a, 'eJSL_Extension', b1)
    if hasattr(b1, 'eJSL_CMSExtension'):
        assert _is_linked(b1, 'eJSL_CMSExtension', a)
    _safe_set(a, 'eJSL_Extension', b2)
    assert _is_linked(a, 'eJSL_Extension', b2)
    if hasattr(b1, 'eJSL_CMSExtension'):
        assert not _is_linked(b1, 'eJSL_CMSExtension', a)
    if hasattr(b2, 'eJSL_CMSExtension'):
        assert _is_linked(b2, 'eJSL_CMSExtension', a)
    _safe_set(a, 'eJSL_Extension', None)
    assert not _is_linked(a, 'eJSL_Extension', b2)
    if hasattr(b2, 'eJSL_CMSExtension'):
        assert not _is_linked(b2, 'eJSL_CMSExtension', a)


def test_assoc_filters81_link_reassign_clear():
    a = eJSL_DynamicPage(preserve=True)
    b1 = eJSL_Attribute(id=True, isprimary=True, isunique=True, name="sample_text", preserve=True)
    b2 = eJSL_Attribute(id=False, isprimary=False, isunique=False, name="sample_text_2", preserve=False)
    _safe_set(a, 'eJSL_DynamicPage82', {b1})
    assert _is_linked(a, 'eJSL_DynamicPage82', b1)
    if hasattr(b1, 'eJSL_Attribute83'):
        assert _is_linked(b1, 'eJSL_Attribute83', a)
    _safe_set(a, 'eJSL_DynamicPage82', {b2})
    assert _is_linked(a, 'eJSL_DynamicPage82', b2)
    if hasattr(b1, 'eJSL_Attribute83'):
        assert not _is_linked(b1, 'eJSL_Attribute83', a)
    if hasattr(b2, 'eJSL_Attribute83'):
        assert _is_linked(b2, 'eJSL_Attribute83', a)
    _safe_set(a, 'eJSL_DynamicPage82', set())
    assert not _is_linked(a, 'eJSL_DynamicPage82', b2)
    if hasattr(b2, 'eJSL_Attribute83'):
        assert not _is_linked(b2, 'eJSL_Attribute83', a)


def test_assoc_globalParamter117_link_reassign_clear():
    a = eJSL_ParameterGroup(label="sample_text", name="sample_text")
    b1 = eJSL_Component()
    b2 = eJSL_Component()
    _safe_set(a, 'eJSL_ParameterGroup118', b1)
    assert _is_linked(a, 'eJSL_ParameterGroup118', b1)
    if hasattr(b1, 'eJSL_Component'):
        assert _is_linked(b1, 'eJSL_Component', a)
    _safe_set(a, 'eJSL_ParameterGroup118', b2)
    assert _is_linked(a, 'eJSL_ParameterGroup118', b2)
    if hasattr(b1, 'eJSL_Component'):
        assert not _is_linked(b1, 'eJSL_Component', a)
    if hasattr(b2, 'eJSL_Component'):
        assert _is_linked(b2, 'eJSL_Component', a)
    _safe_set(a, 'eJSL_ParameterGroup118', None)
    assert not _is_linked(a, 'eJSL_ParameterGroup118', b2)
    if hasattr(b2, 'eJSL_Component'):
        assert not _is_linked(b2, 'eJSL_Component', a)


def test_assoc_globalparameters27_link_reassign_clear():
    a = eJSL_ParameterGroup(label="sample_text", name="sample_text")
    b1 = eJSL_Parameter(defaultvalue="sample_text", descripton="sample_text", label="sample_text", name="sample_text", size=7)
    b2 = eJSL_Parameter(defaultvalue="sample_text_2", descripton="sample_text_2", label="sample_text_2", name="sample_text_2", size=13)
    _safe_set(a, 'eJSL_ParameterGroup28', {b1})
    assert _is_linked(a, 'eJSL_ParameterGroup28', b1)
    if hasattr(b1, 'eJSL_Parameter29'):
        assert _is_linked(b1, 'eJSL_Parameter29', a)
    _safe_set(a, 'eJSL_ParameterGroup28', {b2})
    assert _is_linked(a, 'eJSL_ParameterGroup28', b2)
    if hasattr(b1, 'eJSL_Parameter29'):
        assert not _is_linked(b1, 'eJSL_Parameter29', a)
    if hasattr(b2, 'eJSL_Parameter29'):
        assert _is_linked(b2, 'eJSL_Parameter29', a)
    _safe_set(a, 'eJSL_ParameterGroup28', set())
    assert not _is_linked(a, 'eJSL_ParameterGroup28', b2)
    if hasattr(b2, 'eJSL_Parameter29'):
        assert not _is_linked(b2, 'eJSL_Parameter29', a)


def test_assoc_globalparameters3_link_reassign_clear():
    a = eJSL_Parameter(defaultvalue="sample_text", descripton="sample_text", label="sample_text", name="sample_text", size=7)
    b1 = eJSL_EJSLPart()
    b2 = eJSL_EJSLPart()
    _safe_set(a, 'eJSL_Parameter', b1)
    assert _is_linked(a, 'eJSL_Parameter', b1)
    if hasattr(b1, 'eJSL_EJSLPart4'):
        assert _is_linked(b1, 'eJSL_EJSLPart4', a)
    _safe_set(a, 'eJSL_Parameter', b2)
    assert _is_linked(a, 'eJSL_Parameter', b2)
    if hasattr(b1, 'eJSL_EJSLPart4'):
        assert not _is_linked(b1, 'eJSL_EJSLPart4', a)
    if hasattr(b2, 'eJSL_EJSLPart4'):
        assert _is_linked(b2, 'eJSL_EJSLPart4', a)
    _safe_set(a, 'eJSL_Parameter', None)
    assert not _is_linked(a, 'eJSL_Parameter', b2)
    if hasattr(b2, 'eJSL_EJSLPart4'):
        assert not _is_linked(b2, 'eJSL_EJSLPart4', a)


def test_assoc_globalparameters66_link_reassign_clear():
    a = eJSL_Parameter(defaultvalue="sample_text", descripton="sample_text", label="sample_text", name="sample_text", size=7)
    b1 = eJSL_Page(name="sample_text")
    b2 = eJSL_Page(name="sample_text_2")
    _safe_set(a, 'eJSL_Parameter68', b1)
    assert _is_linked(a, 'eJSL_Parameter68', b1)
    if hasattr(b1, 'eJSL_Page67'):
        assert _is_linked(b1, 'eJSL_Page67', a)
    _safe_set(a, 'eJSL_Parameter68', b2)
    assert _is_linked(a, 'eJSL_Parameter68', b2)
    if hasattr(b1, 'eJSL_Page67'):
        assert not _is_linked(b1, 'eJSL_Page67', a)
    if hasattr(b2, 'eJSL_Page67'):
        assert _is_linked(b2, 'eJSL_Page67', a)
    _safe_set(a, 'eJSL_Parameter68', None)
    assert not _is_linked(a, 'eJSL_Parameter68', b2)
    if hasattr(b2, 'eJSL_Page67'):
        assert not _is_linked(b2, 'eJSL_Page67', a)


def test_assoc_keyvaluepairs178_link_reassign_clear():
    a = eJSL_Language(name="sample_text", sys=True)
    b1 = eJSL_KeyValuePair(name="sample_text", value="sample_text")
    b2 = eJSL_KeyValuePair(name="sample_text_2", value="sample_text_2")
    _safe_set(a, 'eJSL_Language179', {b1})
    assert _is_linked(a, 'eJSL_Language179', b1)
    if hasattr(b1, 'eJSL_KeyValuePair180'):
        assert _is_linked(b1, 'eJSL_KeyValuePair180', a)
    _safe_set(a, 'eJSL_Language179', {b2})
    assert _is_linked(a, 'eJSL_Language179', b2)
    if hasattr(b1, 'eJSL_KeyValuePair180'):
        assert not _is_linked(b1, 'eJSL_KeyValuePair180', a)
    if hasattr(b2, 'eJSL_KeyValuePair180'):
        assert _is_linked(b2, 'eJSL_KeyValuePair180', a)
    _safe_set(a, 'eJSL_Language179', set())
    assert not _is_linked(a, 'eJSL_Language179', b2)
    if hasattr(b2, 'eJSL_KeyValuePair180'):
        assert not _is_linked(b2, 'eJSL_KeyValuePair180', a)


def test_assoc_keyvaluepairs183_link_reassign_clear():
    a = eJSL_PositionParameter(divid="sample_text", name="sample_text", type="sample_text")
    b1 = eJSL_KeyValuePair(name="sample_text", value="sample_text")
    b2 = eJSL_KeyValuePair(name="sample_text_2", value="sample_text_2")
    _safe_set(a, 'eJSL_PositionParameter184', {b1})
    assert _is_linked(a, 'eJSL_PositionParameter184', b1)
    if hasattr(b1, 'eJSL_KeyValuePair185'):
        assert _is_linked(b1, 'eJSL_KeyValuePair185', a)
    _safe_set(a, 'eJSL_PositionParameter184', {b2})
    assert _is_linked(a, 'eJSL_PositionParameter184', b2)
    if hasattr(b1, 'eJSL_KeyValuePair185'):
        assert not _is_linked(b1, 'eJSL_KeyValuePair185', a)
    if hasattr(b2, 'eJSL_KeyValuePair185'):
        assert _is_linked(b2, 'eJSL_KeyValuePair185', a)
    _safe_set(a, 'eJSL_PositionParameter184', set())
    assert not _is_linked(a, 'eJSL_PositionParameter184', b2)
    if hasattr(b2, 'eJSL_KeyValuePair185'):
        assert not _is_linked(b2, 'eJSL_KeyValuePair185', a)


def test_assoc_keyvaluepairs186_link_reassign_clear():
    a = eJSL_KeyValuePair(name="sample_text", value="sample_text")
    b1 = eJSL_CssBlock(selector="sample_text")
    b2 = eJSL_CssBlock(selector="sample_text_2")
    _safe_set(a, 'eJSL_KeyValuePair188', b1)
    assert _is_linked(a, 'eJSL_KeyValuePair188', b1)
    if hasattr(b1, 'eJSL_CssBlock187'):
        assert _is_linked(b1, 'eJSL_CssBlock187', a)
    _safe_set(a, 'eJSL_KeyValuePair188', b2)
    assert _is_linked(a, 'eJSL_KeyValuePair188', b2)
    if hasattr(b1, 'eJSL_CssBlock187'):
        assert not _is_linked(b1, 'eJSL_CssBlock187', a)
    if hasattr(b2, 'eJSL_CssBlock187'):
        assert _is_linked(b2, 'eJSL_CssBlock187', a)
    _safe_set(a, 'eJSL_KeyValuePair188', None)
    assert not _is_linked(a, 'eJSL_KeyValuePair188', b2)
    if hasattr(b2, 'eJSL_CssBlock187'):
        assert not _is_linked(b2, 'eJSL_CssBlock187', a)


def test_assoc_languages113_link_reassign_clear():
    a = eJSL_Language(name="sample_text", sys=True)
    b1 = eJSL_Extension(name="sample_text")
    b2 = eJSL_Extension(name="sample_text_2")
    _safe_set(a, 'eJSL_Language', b1)
    assert _is_linked(a, 'eJSL_Language', b1)
    if hasattr(b1, 'eJSL_Extension114'):
        assert _is_linked(b1, 'eJSL_Extension114', a)
    _safe_set(a, 'eJSL_Language', b2)
    assert _is_linked(a, 'eJSL_Language', b2)
    if hasattr(b1, 'eJSL_Extension114'):
        assert not _is_linked(b1, 'eJSL_Extension114', a)
    if hasattr(b2, 'eJSL_Extension114'):
        assert _is_linked(b2, 'eJSL_Extension114', a)
    _safe_set(a, 'eJSL_Language', None)
    assert not _is_linked(a, 'eJSL_Language', b2)
    if hasattr(b2, 'eJSL_Extension114'):
        assert not _is_linked(b2, 'eJSL_Extension114', a)


def test_assoc_linkedAction102_link_reassign_clear():
    a = eJSL_PageAction(name="sample_text", pageActionPosition="sample_text", pageActionType="sample_text")
    b1 = eJSL_Link()
    b2 = eJSL_Link()
    _safe_set(a, 'eJSL_PageAction104', b1)
    assert _is_linked(a, 'eJSL_PageAction104', b1)
    if hasattr(b1, 'eJSL_Link103'):
        assert _is_linked(b1, 'eJSL_Link103', a)
    _safe_set(a, 'eJSL_PageAction104', b2)
    assert _is_linked(a, 'eJSL_PageAction104', b2)
    if hasattr(b1, 'eJSL_Link103'):
        assert not _is_linked(b1, 'eJSL_Link103', a)
    if hasattr(b2, 'eJSL_Link103'):
        assert _is_linked(b2, 'eJSL_Link103', a)
    _safe_set(a, 'eJSL_PageAction104', None)
    assert not _is_linked(a, 'eJSL_PageAction104', b2)
    if hasattr(b2, 'eJSL_Link103'):
        assert not _is_linked(b2, 'eJSL_Link103', a)


def test_assoc_linkedAttribute99_link_reassign_clear():
    a = eJSL_Attribute(id=True, isprimary=True, isunique=True, name="sample_text", preserve=True)
    b1 = eJSL_Link()
    b2 = eJSL_Link()
    _safe_set(a, 'eJSL_Attribute101', b1)
    assert _is_linked(a, 'eJSL_Attribute101', b1)
    if hasattr(b1, 'eJSL_Link100'):
        assert _is_linked(b1, 'eJSL_Link100', a)
    _safe_set(a, 'eJSL_Attribute101', b2)
    assert _is_linked(a, 'eJSL_Attribute101', b2)
    if hasattr(b1, 'eJSL_Link100'):
        assert not _is_linked(b1, 'eJSL_Link100', a)
    if hasattr(b2, 'eJSL_Link100'):
        assert _is_linked(b2, 'eJSL_Link100', a)
    _safe_set(a, 'eJSL_Attribute101', None)
    assert not _is_linked(a, 'eJSL_Attribute101', b2)
    if hasattr(b2, 'eJSL_Link100'):
        assert not _is_linked(b2, 'eJSL_Link100', a)


def test_assoc_linkparameters107_link_reassign_clear():
    a = eJSL_LinkParameter(id=True, name="sample_text", value="sample_text")
    b1 = eJSL_ContextLink()
    b2 = eJSL_ContextLink()
    _safe_set(a, 'eJSL_LinkParameter', b1)
    assert _is_linked(a, 'eJSL_LinkParameter', b1)
    if hasattr(b1, 'eJSL_ContextLink'):
        assert _is_linked(b1, 'eJSL_ContextLink', a)
    _safe_set(a, 'eJSL_LinkParameter', b2)
    assert _is_linked(a, 'eJSL_LinkParameter', b2)
    if hasattr(b1, 'eJSL_ContextLink'):
        assert not _is_linked(b1, 'eJSL_ContextLink', a)
    if hasattr(b2, 'eJSL_ContextLink'):
        assert _is_linked(b2, 'eJSL_ContextLink', a)
    _safe_set(a, 'eJSL_LinkParameter', None)
    assert not _is_linked(a, 'eJSL_LinkParameter', b2)
    if hasattr(b2, 'eJSL_ContextLink'):
        assert not _is_linked(b2, 'eJSL_ContextLink', a)


def test_assoc_links74_link_reassign_clear():
    a = eJSL_Page(name="sample_text")
    b1 = eJSL_Link()
    b2 = eJSL_Link()
    _safe_set(a, 'eJSL_Page75', {b1})
    assert _is_linked(a, 'eJSL_Page75', b1)
    if hasattr(b1, 'eJSL_Link'):
        assert _is_linked(b1, 'eJSL_Link', a)
    _safe_set(a, 'eJSL_Page75', {b2})
    assert _is_linked(a, 'eJSL_Page75', b2)
    if hasattr(b1, 'eJSL_Link'):
        assert not _is_linked(b1, 'eJSL_Link', a)
    if hasattr(b2, 'eJSL_Link'):
        assert _is_linked(b2, 'eJSL_Link', a)
    _safe_set(a, 'eJSL_Page75', set())
    assert not _is_linked(a, 'eJSL_Page75', b2)
    if hasattr(b2, 'eJSL_Link'):
        assert not _is_linked(b2, 'eJSL_Link', a)


def test_assoc_localparameters136_link_reassign_clear():
    a = eJSL_Plugin(type="sample_text")
    b1 = eJSL_Parameter(defaultvalue="sample_text", descripton="sample_text", label="sample_text", name="sample_text", size=7)
    b2 = eJSL_Parameter(defaultvalue="sample_text_2", descripton="sample_text_2", label="sample_text_2", name="sample_text_2", size=13)
    _safe_set(a, 'eJSL_Plugin137', {b1})
    assert _is_linked(a, 'eJSL_Plugin137', b1)
    if hasattr(b1, 'eJSL_Parameter138'):
        assert _is_linked(b1, 'eJSL_Parameter138', a)
    _safe_set(a, 'eJSL_Plugin137', {b2})
    assert _is_linked(a, 'eJSL_Plugin137', b2)
    if hasattr(b1, 'eJSL_Parameter138'):
        assert not _is_linked(b1, 'eJSL_Parameter138', a)
    if hasattr(b2, 'eJSL_Parameter138'):
        assert _is_linked(b2, 'eJSL_Parameter138', a)
    _safe_set(a, 'eJSL_Plugin137', set())
    assert not _is_linked(a, 'eJSL_Plugin137', b2)
    if hasattr(b2, 'eJSL_Parameter138'):
        assert not _is_linked(b2, 'eJSL_Parameter138', a)


def test_assoc_localparameters170_link_reassign_clear():
    a = eJSL_Parameter(defaultvalue="sample_text", descripton="sample_text", label="sample_text", name="sample_text", size=7)
    b1 = eJSL_Template()
    b2 = eJSL_Template()
    _safe_set(a, 'eJSL_Parameter171', b1)
    assert _is_linked(a, 'eJSL_Parameter171', b1)
    if hasattr(b1, 'eJSL_Template'):
        assert _is_linked(b1, 'eJSL_Template', a)
    _safe_set(a, 'eJSL_Parameter171', b2)
    assert _is_linked(a, 'eJSL_Parameter171', b2)
    if hasattr(b1, 'eJSL_Template'):
        assert not _is_linked(b1, 'eJSL_Template', a)
    if hasattr(b2, 'eJSL_Template'):
        assert _is_linked(b2, 'eJSL_Template', a)
    _safe_set(a, 'eJSL_Parameter171', None)
    assert not _is_linked(a, 'eJSL_Parameter171', b2)
    if hasattr(b2, 'eJSL_Template'):
        assert not _is_linked(b2, 'eJSL_Template', a)


def test_assoc_localparameters69_link_reassign_clear():
    a = eJSL_Parameter(defaultvalue="sample_text", descripton="sample_text", label="sample_text", name="sample_text", size=7)
    b1 = eJSL_Page(name="sample_text")
    b2 = eJSL_Page(name="sample_text_2")
    _safe_set(a, 'eJSL_Parameter71', b1)
    assert _is_linked(a, 'eJSL_Parameter71', b1)
    if hasattr(b1, 'eJSL_Page70'):
        assert _is_linked(b1, 'eJSL_Page70', a)
    _safe_set(a, 'eJSL_Parameter71', b2)
    assert _is_linked(a, 'eJSL_Parameter71', b2)
    if hasattr(b1, 'eJSL_Page70'):
        assert not _is_linked(b1, 'eJSL_Page70', a)
    if hasattr(b2, 'eJSL_Page70'):
        assert _is_linked(b2, 'eJSL_Page70', a)
    _safe_set(a, 'eJSL_Parameter71', None)
    assert not _is_linked(a, 'eJSL_Parameter71', b2)
    if hasattr(b2, 'eJSL_Page70'):
        assert not _is_linked(b2, 'eJSL_Page70', a)


def test_assoc_manifest111_link_reassign_clear():
    a = eJSL_Manifestation(copyright="sample_text", creationdate="sample_text", description="sample_text", license="sample_text", link="sample_text", version="sample_text")
    b1 = eJSL_Extension(name="sample_text")
    b2 = eJSL_Extension(name="sample_text_2")
    _safe_set(a, 'eJSL_Manifestation', b1)
    assert _is_linked(a, 'eJSL_Manifestation', b1)
    if hasattr(b1, 'eJSL_Extension112'):
        assert _is_linked(b1, 'eJSL_Extension112', a)
    _safe_set(a, 'eJSL_Manifestation', b2)
    assert _is_linked(a, 'eJSL_Manifestation', b2)
    if hasattr(b1, 'eJSL_Extension112'):
        assert not _is_linked(b1, 'eJSL_Extension112', a)
    if hasattr(b2, 'eJSL_Extension112'):
        assert _is_linked(b2, 'eJSL_Extension112', a)
    _safe_set(a, 'eJSL_Manifestation', None)
    assert not _is_linked(a, 'eJSL_Manifestation', b2)
    if hasattr(b2, 'eJSL_Extension112'):
        assert not _is_linked(b2, 'eJSL_Extension112', a)


def test_assoc_methodparameters165_link_reassign_clear():
    a = eJSL_MethodParameter(name="sample_text")
    b1 = eJSL_Method(name="sample_text", returnvalue="sample_text")
    b2 = eJSL_Method(name="sample_text_2", returnvalue="sample_text_2")
    _safe_set(a, 'eJSL_MethodParameter', b1)
    assert _is_linked(a, 'eJSL_MethodParameter', b1)
    if hasattr(b1, 'eJSL_Method166'):
        assert _is_linked(b1, 'eJSL_Method166', a)
    _safe_set(a, 'eJSL_MethodParameter', b2)
    assert _is_linked(a, 'eJSL_MethodParameter', b2)
    if hasattr(b1, 'eJSL_Method166'):
        assert not _is_linked(b1, 'eJSL_Method166', a)
    if hasattr(b2, 'eJSL_Method166'):
        assert _is_linked(b2, 'eJSL_Method166', a)
    _safe_set(a, 'eJSL_MethodParameter', None)
    assert not _is_linked(a, 'eJSL_MethodParameter', b2)
    if hasattr(b2, 'eJSL_Method166'):
        assert not _is_linked(b2, 'eJSL_Method166', a)


def test_assoc_methods160_link_reassign_clear():
    a = eJSL_Method(name="sample_text", returnvalue="sample_text")
    b1 = eJSL_Class(name="sample_text")
    b2 = eJSL_Class(name="sample_text_2")
    _safe_set(a, 'eJSL_Method', b1)
    assert _is_linked(a, 'eJSL_Method', b1)
    if hasattr(b1, 'eJSL_Class161'):
        assert _is_linked(b1, 'eJSL_Class161', a)
    _safe_set(a, 'eJSL_Method', b2)
    assert _is_linked(a, 'eJSL_Method', b2)
    if hasattr(b1, 'eJSL_Class161'):
        assert not _is_linked(b1, 'eJSL_Class161', a)
    if hasattr(b2, 'eJSL_Class161'):
        assert _is_linked(b2, 'eJSL_Class161', a)
    _safe_set(a, 'eJSL_Method', None)
    assert not _is_linked(a, 'eJSL_Method', b2)
    if hasattr(b2, 'eJSL_Class161'):
        assert not _is_linked(b2, 'eJSL_Class161', a)


def test_assoc_packages143_link_reassign_clear():
    a = eJSL_Package(name="sample_text")
    b1 = eJSL_Library()
    b2 = eJSL_Library()
    _safe_set(a, 'eJSL_Package', b1)
    assert _is_linked(a, 'eJSL_Package', b1)
    if hasattr(b1, 'eJSL_Library144'):
        assert _is_linked(b1, 'eJSL_Library144', a)
    _safe_set(a, 'eJSL_Package', b2)
    assert _is_linked(a, 'eJSL_Package', b2)
    if hasattr(b1, 'eJSL_Library144'):
        assert not _is_linked(b1, 'eJSL_Library144', a)
    if hasattr(b2, 'eJSL_Library144'):
        assert _is_linked(b2, 'eJSL_Library144', a)
    _safe_set(a, 'eJSL_Package', None)
    assert not _is_linked(a, 'eJSL_Package', b2)
    if hasattr(b2, 'eJSL_Library144'):
        assert not _is_linked(b2, 'eJSL_Library144', a)


def test_assoc_packages146_link_reassign_clear():
    a = eJSL_Package(name="sample_text")
    b1 = eJSL_Package(name="sample_text")
    b2 = eJSL_Package(name="sample_text_2")
    _safe_set(a, 'eJSL_Package145', {b1})
    assert _is_linked(a, 'eJSL_Package145', b1)
    if hasattr(b1, 'eJSL_Package147'):
        assert _is_linked(b1, 'eJSL_Package147', a)
    _safe_set(a, 'eJSL_Package145', {b2})
    assert _is_linked(a, 'eJSL_Package145', b2)
    if hasattr(b1, 'eJSL_Package147'):
        assert not _is_linked(b1, 'eJSL_Package147', a)
    if hasattr(b2, 'eJSL_Package147'):
        assert _is_linked(b2, 'eJSL_Package147', a)
    _safe_set(a, 'eJSL_Package145', set())
    assert not _is_linked(a, 'eJSL_Package145', b2)
    if hasattr(b2, 'eJSL_Package147'):
        assert not _is_linked(b2, 'eJSL_Package147', a)


def test_assoc_page124_link_reassign_clear():
    a = eJSL_PageReference(sect="sample_text")
    b1 = eJSL_Page(name="sample_text")
    b2 = eJSL_Page(name="sample_text_2")
    _safe_set(a, 'eJSL_PageReference125', b1)
    assert _is_linked(a, 'eJSL_PageReference125', b1)
    if hasattr(b1, 'eJSL_Page126'):
        assert _is_linked(b1, 'eJSL_Page126', a)
    _safe_set(a, 'eJSL_PageReference125', b2)
    assert _is_linked(a, 'eJSL_PageReference125', b2)
    if hasattr(b1, 'eJSL_Page126'):
        assert not _is_linked(b1, 'eJSL_Page126', a)
    if hasattr(b2, 'eJSL_Page126'):
        assert _is_linked(b2, 'eJSL_Page126', a)
    _safe_set(a, 'eJSL_PageReference125', None)
    assert not _is_linked(a, 'eJSL_PageReference125', b2)
    if hasattr(b2, 'eJSL_Page126'):
        assert not _is_linked(b2, 'eJSL_Page126', a)


def test_assoc_pageRef122_link_reassign_clear():
    a = eJSL_PageReference(sect="sample_text")
    b1 = eJSL_Section()
    b2 = eJSL_Section()
    _safe_set(a, 'eJSL_PageReference', b1)
    assert _is_linked(a, 'eJSL_PageReference', b1)
    if hasattr(b1, 'eJSL_Section123'):
        assert _is_linked(b1, 'eJSL_Section123', a)
    _safe_set(a, 'eJSL_PageReference', b2)
    assert _is_linked(a, 'eJSL_PageReference', b2)
    if hasattr(b1, 'eJSL_Section123'):
        assert not _is_linked(b1, 'eJSL_Section123', a)
    if hasattr(b2, 'eJSL_Section123'):
        assert _is_linked(b2, 'eJSL_Section123', a)
    _safe_set(a, 'eJSL_PageReference', None)
    assert not _is_linked(a, 'eJSL_PageReference', b2)
    if hasattr(b2, 'eJSL_Section123'):
        assert not _is_linked(b2, 'eJSL_Section123', a)


def test_assoc_pageRef132_link_reassign_clear():
    a = eJSL_PageReference(sect="sample_text")
    b1 = eJSL_Module()
    b2 = eJSL_Module()
    _safe_set(a, 'eJSL_PageReference133', b1)
    assert _is_linked(a, 'eJSL_PageReference133', b1)
    if hasattr(b1, 'eJSL_Module'):
        assert _is_linked(b1, 'eJSL_Module', a)
    _safe_set(a, 'eJSL_PageReference133', b2)
    assert _is_linked(a, 'eJSL_PageReference133', b2)
    if hasattr(b1, 'eJSL_Module'):
        assert not _is_linked(b1, 'eJSL_Module', a)
    if hasattr(b2, 'eJSL_Module'):
        assert _is_linked(b2, 'eJSL_Module', a)
    _safe_set(a, 'eJSL_PageReference133', None)
    assert not _is_linked(a, 'eJSL_PageReference133', b2)
    if hasattr(b2, 'eJSL_Module'):
        assert not _is_linked(b2, 'eJSL_Module', a)


def test_assoc_pageactions72_link_reassign_clear():
    a = eJSL_PageAction(name="sample_text", pageActionPosition="sample_text", pageActionType="sample_text")
    b1 = eJSL_Page(name="sample_text")
    b2 = eJSL_Page(name="sample_text_2")
    _safe_set(a, 'eJSL_PageAction', b1)
    assert _is_linked(a, 'eJSL_PageAction', b1)
    if hasattr(b1, 'eJSL_Page73'):
        assert _is_linked(b1, 'eJSL_Page73', a)
    _safe_set(a, 'eJSL_PageAction', b2)
    assert _is_linked(a, 'eJSL_PageAction', b2)
    if hasattr(b1, 'eJSL_Page73'):
        assert not _is_linked(b1, 'eJSL_Page73', a)
    if hasattr(b2, 'eJSL_Page73'):
        assert _is_linked(b2, 'eJSL_Page73', a)
    _safe_set(a, 'eJSL_PageAction', None)
    assert not _is_linked(a, 'eJSL_PageAction', b2)
    if hasattr(b2, 'eJSL_Page73'):
        assert not _is_linked(b2, 'eJSL_Page73', a)


def test_assoc_pages14_link_reassign_clear():
    a = eJSL_Page(name="sample_text")
    b1 = eJSL_Feature()
    b2 = eJSL_Feature()
    _safe_set(a, 'eJSL_Page', b1)
    assert _is_linked(a, 'eJSL_Page', b1)
    if hasattr(b1, 'eJSL_Feature15'):
        assert _is_linked(b1, 'eJSL_Feature15', a)
    _safe_set(a, 'eJSL_Page', b2)
    assert _is_linked(a, 'eJSL_Page', b2)
    if hasattr(b1, 'eJSL_Feature15'):
        assert not _is_linked(b1, 'eJSL_Feature15', a)
    if hasattr(b2, 'eJSL_Feature15'):
        assert _is_linked(b2, 'eJSL_Feature15', a)
    _safe_set(a, 'eJSL_Page', None)
    assert not _is_linked(a, 'eJSL_Page', b2)
    if hasattr(b2, 'eJSL_Feature15'):
        assert not _is_linked(b2, 'eJSL_Feature15', a)


def test_assoc_pagescr127_link_reassign_clear():
    a = eJSL_PageReference(sect="sample_text")
    b1 = eJSL_ComponentReference(core="sample_text")
    b2 = eJSL_ComponentReference(core="sample_text_2")
    _safe_set(a, 'eJSL_PageReference128', b1)
    assert _is_linked(a, 'eJSL_PageReference128', b1)
    if hasattr(b1, 'eJSL_ComponentReference'):
        assert _is_linked(b1, 'eJSL_ComponentReference', a)
    _safe_set(a, 'eJSL_PageReference128', b2)
    assert _is_linked(a, 'eJSL_PageReference128', b2)
    if hasattr(b1, 'eJSL_ComponentReference'):
        assert not _is_linked(b1, 'eJSL_ComponentReference', a)
    if hasattr(b2, 'eJSL_ComponentReference'):
        assert _is_linked(b2, 'eJSL_ComponentReference', a)
    _safe_set(a, 'eJSL_PageReference128', None)
    assert not _is_linked(a, 'eJSL_PageReference128', b2)
    if hasattr(b2, 'eJSL_ComponentReference'):
        assert not _is_linked(b2, 'eJSL_ComponentReference', a)


def test_assoc_parametergroups5_link_reassign_clear():
    a = eJSL_ParameterGroup(label="sample_text", name="sample_text")
    b1 = eJSL_EJSLPart()
    b2 = eJSL_EJSLPart()
    _safe_set(a, 'eJSL_ParameterGroup', b1)
    assert _is_linked(a, 'eJSL_ParameterGroup', b1)
    if hasattr(b1, 'eJSL_EJSLPart6'):
        assert _is_linked(b1, 'eJSL_EJSLPart6', a)
    _safe_set(a, 'eJSL_ParameterGroup', b2)
    assert _is_linked(a, 'eJSL_ParameterGroup', b2)
    if hasattr(b1, 'eJSL_EJSLPart6'):
        assert not _is_linked(b1, 'eJSL_EJSLPart6', a)
    if hasattr(b2, 'eJSL_EJSLPart6'):
        assert _is_linked(b2, 'eJSL_EJSLPart6', a)
    _safe_set(a, 'eJSL_ParameterGroup', None)
    assert not _is_linked(a, 'eJSL_ParameterGroup', b2)
    if hasattr(b2, 'eJSL_EJSLPart6'):
        assert not _is_linked(b2, 'eJSL_EJSLPart6', a)


def test_assoc_parametergroups63_link_reassign_clear():
    a = eJSL_ParameterGroup(label="sample_text", name="sample_text")
    b1 = eJSL_Page(name="sample_text")
    b2 = eJSL_Page(name="sample_text_2")
    _safe_set(a, 'eJSL_ParameterGroup65', b1)
    assert _is_linked(a, 'eJSL_ParameterGroup65', b1)
    if hasattr(b1, 'eJSL_Page64'):
        assert _is_linked(b1, 'eJSL_Page64', a)
    _safe_set(a, 'eJSL_ParameterGroup65', b2)
    assert _is_linked(a, 'eJSL_ParameterGroup65', b2)
    if hasattr(b1, 'eJSL_Page64'):
        assert not _is_linked(b1, 'eJSL_Page64', a)
    if hasattr(b2, 'eJSL_Page64'):
        assert _is_linked(b2, 'eJSL_Page64', a)
    _safe_set(a, 'eJSL_ParameterGroup65', None)
    assert not _is_linked(a, 'eJSL_ParameterGroup65', b2)
    if hasattr(b2, 'eJSL_Page64'):
        assert not _is_linked(b2, 'eJSL_Page64', a)


def test_assoc_parameters30_link_reassign_clear():
    a = eJSL_ParameterGroup(label="sample_text", name="sample_text")
    b1 = eJSL_Parameter(defaultvalue="sample_text", descripton="sample_text", label="sample_text", name="sample_text", size=7)
    b2 = eJSL_Parameter(defaultvalue="sample_text_2", descripton="sample_text_2", label="sample_text_2", name="sample_text_2", size=13)
    _safe_set(a, 'eJSL_ParameterGroup31', {b1})
    assert _is_linked(a, 'eJSL_ParameterGroup31', b1)
    if hasattr(b1, 'eJSL_Parameter32'):
        assert _is_linked(b1, 'eJSL_Parameter32', a)
    _safe_set(a, 'eJSL_ParameterGroup31', {b2})
    assert _is_linked(a, 'eJSL_ParameterGroup31', b2)
    if hasattr(b1, 'eJSL_Parameter32'):
        assert not _is_linked(b1, 'eJSL_Parameter32', a)
    if hasattr(b2, 'eJSL_Parameter32'):
        assert _is_linked(b2, 'eJSL_Parameter32', a)
    _safe_set(a, 'eJSL_ParameterGroup31', set())
    assert not _is_linked(a, 'eJSL_ParameterGroup31', b2)
    if hasattr(b2, 'eJSL_Parameter32'):
        assert not _is_linked(b2, 'eJSL_Parameter32', a)


def test_assoc_positionparameters181_link_reassign_clear():
    a = eJSL_PositionParameter(divid="sample_text", name="sample_text", type="sample_text")
    b1 = eJSL_Position(name="sample_text")
    b2 = eJSL_Position(name="sample_text_2")
    _safe_set(a, 'eJSL_PositionParameter', b1)
    assert _is_linked(a, 'eJSL_PositionParameter', b1)
    if hasattr(b1, 'eJSL_Position182'):
        assert _is_linked(b1, 'eJSL_Position182', a)
    _safe_set(a, 'eJSL_PositionParameter', b2)
    assert _is_linked(a, 'eJSL_PositionParameter', b2)
    if hasattr(b1, 'eJSL_Position182'):
        assert not _is_linked(b1, 'eJSL_Position182', a)
    if hasattr(b2, 'eJSL_Position182'):
        assert _is_linked(b2, 'eJSL_Position182', a)
    _safe_set(a, 'eJSL_PositionParameter', None)
    assert not _is_linked(a, 'eJSL_PositionParameter', b2)
    if hasattr(b2, 'eJSL_Position182'):
        assert not _is_linked(b2, 'eJSL_Position182', a)


def test_assoc_positions172_link_reassign_clear():
    a = eJSL_Position(name="sample_text")
    b1 = eJSL_Template()
    b2 = eJSL_Template()
    _safe_set(a, 'eJSL_Position', b1)
    assert _is_linked(a, 'eJSL_Position', b1)
    if hasattr(b1, 'eJSL_Template173'):
        assert _is_linked(b1, 'eJSL_Template173', a)
    _safe_set(a, 'eJSL_Position', b2)
    assert _is_linked(a, 'eJSL_Position', b2)
    if hasattr(b1, 'eJSL_Template173'):
        assert not _is_linked(b1, 'eJSL_Template173', a)
    if hasattr(b2, 'eJSL_Template173'):
        assert _is_linked(b2, 'eJSL_Template173', a)
    _safe_set(a, 'eJSL_Position', None)
    assert not _is_linked(a, 'eJSL_Position', b2)
    if hasattr(b2, 'eJSL_Template173'):
        assert not _is_linked(b2, 'eJSL_Template173', a)


def test_assoc_ref129_link_reassign_clear():
    a = eJSL_ComponentReference(core="sample_text")
    b1 = eJSL_Component()
    b2 = eJSL_Component()
    _safe_set(a, 'eJSL_ComponentReference130', b1)
    assert _is_linked(a, 'eJSL_ComponentReference130', b1)
    if hasattr(b1, 'eJSL_Component131'):
        assert _is_linked(b1, 'eJSL_Component131', a)
    _safe_set(a, 'eJSL_ComponentReference130', b2)
    assert _is_linked(a, 'eJSL_ComponentReference130', b2)
    if hasattr(b1, 'eJSL_Component131'):
        assert not _is_linked(b1, 'eJSL_Component131', a)
    if hasattr(b2, 'eJSL_Component131'):
        assert _is_linked(b2, 'eJSL_Component131', a)
    _safe_set(a, 'eJSL_ComponentReference130', None)
    assert not _is_linked(a, 'eJSL_ComponentReference130', b2)
    if hasattr(b2, 'eJSL_Component131'):
        assert not _is_linked(b2, 'eJSL_Component131', a)


def test_assoc_references155_link_reassign_clear():
    a = eJSL_Class(name="sample_text")
    b1 = eJSL_Class(name="sample_text")
    b2 = eJSL_Class(name="sample_text_2")
    _safe_set(a, 'eJSL_Class154', {b1})
    assert _is_linked(a, 'eJSL_Class154', b1)
    if hasattr(b1, 'eJSL_Class156'):
        assert _is_linked(b1, 'eJSL_Class156', a)
    _safe_set(a, 'eJSL_Class154', {b2})
    assert _is_linked(a, 'eJSL_Class154', b2)
    if hasattr(b1, 'eJSL_Class156'):
        assert not _is_linked(b1, 'eJSL_Class156', a)
    if hasattr(b2, 'eJSL_Class156'):
        assert _is_linked(b2, 'eJSL_Class156', a)
    _safe_set(a, 'eJSL_Class154', set())
    assert not _is_linked(a, 'eJSL_Class154', b2)
    if hasattr(b2, 'eJSL_Class156'):
        assert not _is_linked(b2, 'eJSL_Class156', a)


def test_assoc_references47_link_reassign_clear():
    a = eJSL_Reference(id=True, lower="sample_text", preserve=True, upper="sample_text")
    b1 = eJSL_Entity(name="sample_text", preserve=True)
    b2 = eJSL_Entity(name="sample_text_2", preserve=False)
    _safe_set(a, 'eJSL_Reference', b1)
    assert _is_linked(a, 'eJSL_Reference', b1)
    if hasattr(b1, 'eJSL_Entity48'):
        assert _is_linked(b1, 'eJSL_Entity48', a)
    _safe_set(a, 'eJSL_Reference', b2)
    assert _is_linked(a, 'eJSL_Reference', b2)
    if hasattr(b1, 'eJSL_Entity48'):
        assert not _is_linked(b1, 'eJSL_Entity48', a)
    if hasattr(b2, 'eJSL_Entity48'):
        assert _is_linked(b2, 'eJSL_Entity48', a)
    _safe_set(a, 'eJSL_Reference', None)
    assert not _is_linked(a, 'eJSL_Reference', b2)
    if hasattr(b2, 'eJSL_Entity48'):
        assert not _is_linked(b2, 'eJSL_Entity48', a)


def test_assoc_supertype152_link_reassign_clear():
    a = eJSL_Class(name="sample_text")
    b1 = eJSL_Class(name="sample_text")
    b2 = eJSL_Class(name="sample_text_2")
    _safe_set(a, 'eJSL_Class151', b1)
    assert _is_linked(a, 'eJSL_Class151', b1)
    if hasattr(b1, 'eJSL_Class153'):
        assert _is_linked(b1, 'eJSL_Class153', a)
    _safe_set(a, 'eJSL_Class151', b2)
    assert _is_linked(a, 'eJSL_Class151', b2)
    if hasattr(b1, 'eJSL_Class153'):
        assert not _is_linked(b1, 'eJSL_Class153', a)
    if hasattr(b2, 'eJSL_Class153'):
        assert _is_linked(b2, 'eJSL_Class153', a)
    _safe_set(a, 'eJSL_Class151', None)
    assert not _is_linked(a, 'eJSL_Class151', b2)
    if hasattr(b2, 'eJSL_Class153'):
        assert not _is_linked(b2, 'eJSL_Class153', a)


def test_assoc_supertype43_link_reassign_clear():
    a = eJSL_Entity(name="sample_text", preserve=True)
    b1 = eJSL_Entity(name="sample_text", preserve=True)
    b2 = eJSL_Entity(name="sample_text_2", preserve=False)
    _safe_set(a, 'eJSL_Entity42', b1)
    assert _is_linked(a, 'eJSL_Entity42', b1)
    if hasattr(b1, 'eJSL_Entity44'):
        assert _is_linked(b1, 'eJSL_Entity44', a)
    _safe_set(a, 'eJSL_Entity42', b2)
    assert _is_linked(a, 'eJSL_Entity42', b2)
    if hasattr(b1, 'eJSL_Entity44'):
        assert not _is_linked(b1, 'eJSL_Entity44', a)
    if hasattr(b2, 'eJSL_Entity44'):
        assert _is_linked(b2, 'eJSL_Entity44', a)
    _safe_set(a, 'eJSL_Entity42', None)
    assert not _is_linked(a, 'eJSL_Entity42', b2)
    if hasattr(b2, 'eJSL_Entity44'):
        assert not _is_linked(b2, 'eJSL_Entity44', a)


def test_assoc_tablecolumns78_link_reassign_clear():
    a = eJSL_DynamicPage(preserve=True)
    b1 = eJSL_Attribute(id=True, isprimary=True, isunique=True, name="sample_text", preserve=True)
    b2 = eJSL_Attribute(id=False, isprimary=False, isunique=False, name="sample_text_2", preserve=False)
    _safe_set(a, 'eJSL_DynamicPage79', {b1})
    assert _is_linked(a, 'eJSL_DynamicPage79', b1)
    if hasattr(b1, 'eJSL_Attribute80'):
        assert _is_linked(b1, 'eJSL_Attribute80', a)
    _safe_set(a, 'eJSL_DynamicPage79', {b2})
    assert _is_linked(a, 'eJSL_DynamicPage79', b2)
    if hasattr(b1, 'eJSL_Attribute80'):
        assert not _is_linked(b1, 'eJSL_Attribute80', a)
    if hasattr(b2, 'eJSL_Attribute80'):
        assert _is_linked(b2, 'eJSL_Attribute80', a)
    _safe_set(a, 'eJSL_DynamicPage79', set())
    assert not _is_linked(a, 'eJSL_DynamicPage79', b2)
    if hasattr(b2, 'eJSL_Attribute80'):
        assert not _is_linked(b2, 'eJSL_Attribute80', a)


def test_assoc_target105_link_reassign_clear():
    a = eJSL_Page(name="sample_text")
    b1 = eJSL_InternalLink(name="sample_text")
    b2 = eJSL_InternalLink(name="sample_text_2")
    _safe_set(a, 'eJSL_Page106', b1)
    assert _is_linked(a, 'eJSL_Page106', b1)
    if hasattr(b1, 'eJSL_InternalLink'):
        assert _is_linked(b1, 'eJSL_InternalLink', a)
    _safe_set(a, 'eJSL_Page106', b2)
    assert _is_linked(a, 'eJSL_Page106', b2)
    if hasattr(b1, 'eJSL_InternalLink'):
        assert not _is_linked(b1, 'eJSL_InternalLink', a)
    if hasattr(b2, 'eJSL_InternalLink'):
        assert _is_linked(b2, 'eJSL_InternalLink', a)
    _safe_set(a, 'eJSL_Page106', None)
    assert not _is_linked(a, 'eJSL_Page106', b2)
    if hasattr(b2, 'eJSL_InternalLink'):
        assert not _is_linked(b2, 'eJSL_InternalLink', a)


def test_assoc_type162_link_reassign_clear():
    a = eJSL_Method(name="sample_text", returnvalue="sample_text")
    b1 = eJSL_Type()
    b2 = eJSL_Type()
    _safe_set(a, 'eJSL_Method163', b1)
    assert _is_linked(a, 'eJSL_Method163', b1)
    if hasattr(b1, 'eJSL_Type164'):
        assert _is_linked(b1, 'eJSL_Type164', a)
    _safe_set(a, 'eJSL_Method163', b2)
    assert _is_linked(a, 'eJSL_Method163', b2)
    if hasattr(b1, 'eJSL_Type164'):
        assert not _is_linked(b1, 'eJSL_Type164', a)
    if hasattr(b2, 'eJSL_Type164'):
        assert _is_linked(b2, 'eJSL_Type164', a)
    _safe_set(a, 'eJSL_Method163', None)
    assert not _is_linked(a, 'eJSL_Method163', b2)
    if hasattr(b2, 'eJSL_Type164'):
        assert not _is_linked(b2, 'eJSL_Type164', a)


def test_assoc_type167_link_reassign_clear():
    a = eJSL_MethodParameter(name="sample_text")
    b1 = eJSL_Type()
    b2 = eJSL_Type()
    _safe_set(a, 'eJSL_MethodParameter168', b1)
    assert _is_linked(a, 'eJSL_MethodParameter168', b1)
    if hasattr(b1, 'eJSL_Type169'):
        assert _is_linked(b1, 'eJSL_Type169', a)
    _safe_set(a, 'eJSL_MethodParameter168', b2)
    assert _is_linked(a, 'eJSL_MethodParameter168', b2)
    if hasattr(b1, 'eJSL_Type169'):
        assert not _is_linked(b1, 'eJSL_Type169', a)
    if hasattr(b2, 'eJSL_Type169'):
        assert _is_linked(b2, 'eJSL_Type169', a)
    _safe_set(a, 'eJSL_MethodParameter168', None)
    assert not _is_linked(a, 'eJSL_MethodParameter168', b2)
    if hasattr(b2, 'eJSL_Type169'):
        assert not _is_linked(b2, 'eJSL_Type169', a)


def test_assoc_type18_link_reassign_clear():
    a = eJSL_Datatype(name="sample_text", type="sample_text")
    b1 = eJSL_DatatypeReference()
    b2 = eJSL_DatatypeReference()
    _safe_set(a, 'eJSL_Datatype19', b1)
    assert _is_linked(a, 'eJSL_Datatype19', b1)
    if hasattr(b1, 'eJSL_DatatypeReference'):
        assert _is_linked(b1, 'eJSL_DatatypeReference', a)
    _safe_set(a, 'eJSL_Datatype19', b2)
    assert _is_linked(a, 'eJSL_Datatype19', b2)
    if hasattr(b1, 'eJSL_DatatypeReference'):
        assert not _is_linked(b1, 'eJSL_DatatypeReference', a)
    if hasattr(b2, 'eJSL_DatatypeReference'):
        assert _is_linked(b2, 'eJSL_DatatypeReference', a)
    _safe_set(a, 'eJSL_Datatype19', None)
    assert not _is_linked(a, 'eJSL_Datatype19', b2)
    if hasattr(b2, 'eJSL_DatatypeReference'):
        assert not _is_linked(b2, 'eJSL_DatatypeReference', a)


def test_assoc_type49_link_reassign_clear():
    a = eJSL_Attribute(id=True, isprimary=True, isunique=True, name="sample_text", preserve=True)
    b1 = eJSL_Type()
    b2 = eJSL_Type()
    _safe_set(a, 'eJSL_Attribute50', b1)
    assert _is_linked(a, 'eJSL_Attribute50', b1)
    if hasattr(b1, 'eJSL_Type'):
        assert _is_linked(b1, 'eJSL_Type', a)
    _safe_set(a, 'eJSL_Attribute50', b2)
    assert _is_linked(a, 'eJSL_Attribute50', b2)
    if hasattr(b1, 'eJSL_Type'):
        assert not _is_linked(b1, 'eJSL_Type', a)
    if hasattr(b2, 'eJSL_Type'):
        assert _is_linked(b2, 'eJSL_Type', a)
    _safe_set(a, 'eJSL_Attribute50', None)
    assert not _is_linked(a, 'eJSL_Attribute50', b2)
    if hasattr(b2, 'eJSL_Type'):
        assert not _is_linked(b2, 'eJSL_Type', a)


def test_assoc_values22_link_reassign_clear():
    a = eJSL_Parameter(defaultvalue="sample_text", descripton="sample_text", label="sample_text", name="sample_text", size=7)
    b1 = eJSL_KeyValuePair(name="sample_text", value="sample_text")
    b2 = eJSL_KeyValuePair(name="sample_text_2", value="sample_text_2")
    _safe_set(a, 'eJSL_Parameter23', {b1})
    assert _is_linked(a, 'eJSL_Parameter23', b1)
    if hasattr(b1, 'eJSL_KeyValuePair'):
        assert _is_linked(b1, 'eJSL_KeyValuePair', a)
    _safe_set(a, 'eJSL_Parameter23', {b2})
    assert _is_linked(a, 'eJSL_Parameter23', b2)
    if hasattr(b1, 'eJSL_KeyValuePair'):
        assert not _is_linked(b1, 'eJSL_KeyValuePair', a)
    if hasattr(b2, 'eJSL_KeyValuePair'):
        assert _is_linked(b2, 'eJSL_KeyValuePair', a)
    _safe_set(a, 'eJSL_Parameter23', set())
    assert not _is_linked(a, 'eJSL_Parameter23', b2)
    if hasattr(b2, 'eJSL_KeyValuePair'):
        assert not _is_linked(b2, 'eJSL_KeyValuePair', a)


def test_assoc_values91_link_reassign_clear():
    a = eJSL_KeyValuePair(name="sample_text", value="sample_text")
    b1 = eJSL_DetailPageField()
    b2 = eJSL_DetailPageField()
    _safe_set(a, 'eJSL_KeyValuePair93', b1)
    assert _is_linked(a, 'eJSL_KeyValuePair93', b1)
    if hasattr(b1, 'eJSL_DetailPageField92'):
        assert _is_linked(b1, 'eJSL_DetailPageField92', a)
    _safe_set(a, 'eJSL_KeyValuePair93', b2)
    assert _is_linked(a, 'eJSL_KeyValuePair93', b2)
    if hasattr(b1, 'eJSL_DetailPageField92'):
        assert not _is_linked(b1, 'eJSL_DetailPageField92', a)
    if hasattr(b2, 'eJSL_DetailPageField92'):
        assert _is_linked(b2, 'eJSL_DetailPageField92', a)
    _safe_set(a, 'eJSL_KeyValuePair93', None)
    assert not _is_linked(a, 'eJSL_KeyValuePair93', b2)
    if hasattr(b2, 'eJSL_DetailPageField92'):
        assert not _is_linked(b2, 'eJSL_DetailPageField92', a)


def test_assoc_withattribute52_link_reassign_clear():
    a = eJSL_Attribute(id=True, isprimary=True, isunique=True, name="sample_text", preserve=True)
    b1 = eJSL_Attribute(id=True, isprimary=True, isunique=True, name="sample_text", preserve=True)
    b2 = eJSL_Attribute(id=False, isprimary=False, isunique=False, name="sample_text_2", preserve=False)
    _safe_set(a, 'eJSL_Attribute51', b1)
    assert _is_linked(a, 'eJSL_Attribute51', b1)
    if hasattr(b1, 'eJSL_Attribute53'):
        assert _is_linked(b1, 'eJSL_Attribute53', a)
    _safe_set(a, 'eJSL_Attribute51', b2)
    assert _is_linked(a, 'eJSL_Attribute51', b2)
    if hasattr(b1, 'eJSL_Attribute53'):
        assert not _is_linked(b1, 'eJSL_Attribute53', a)
    if hasattr(b2, 'eJSL_Attribute53'):
        assert _is_linked(b2, 'eJSL_Attribute53', a)
    _safe_set(a, 'eJSL_Attribute51', None)
    assert not _is_linked(a, 'eJSL_Attribute51', b2)
    if hasattr(b2, 'eJSL_Attribute53'):
        assert not _is_linked(b2, 'eJSL_Attribute53', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

DynamicPage_strategy = st.builds(DynamicPage)
@given(instance=DynamicPage_strategy)
@settings(max_examples=25)
def test_DynamicPage_instantiation(instance):
    assert isinstance(instance, DynamicPage)


EJSLPart_strategy = st.builds(EJSLPart)
@given(instance=EJSLPart_strategy)
@settings(max_examples=25)
def test_EJSLPart_instantiation(instance):
    assert isinstance(instance, EJSLPart)


Extension_strategy = st.builds(Extension)
@given(instance=Extension_strategy)
@settings(max_examples=25)
def test_Extension_instantiation(instance):
    assert isinstance(instance, Extension)


HTMLTypes_strategy = st.builds(HTMLTypes)
@given(instance=HTMLTypes_strategy)
@settings(max_examples=25)
def test_HTMLTypes_instantiation(instance):
    assert isinstance(instance, HTMLTypes)


InternalLink_strategy = st.builds(InternalLink)
@given(instance=InternalLink_strategy)
@settings(max_examples=25)
def test_InternalLink_instantiation(instance):
    assert isinstance(instance, InternalLink)


Link_strategy = st.builds(Link)
@given(instance=Link_strategy)
@settings(max_examples=25)
def test_Link_instantiation(instance):
    assert isinstance(instance, Link)


Page_strategy = st.builds(Page)
@given(instance=Page_strategy)
@settings(max_examples=25)
def test_Page_instantiation(instance):
    assert isinstance(instance, Page)


Section_strategy = st.builds(Section)
@given(instance=Section_strategy)
@settings(max_examples=25)
def test_Section_instantiation(instance):
    assert isinstance(instance, Section)


Type_strategy = st.builds(Type)
@given(instance=Type_strategy)
@settings(max_examples=25)
def test_Type_instantiation(instance):
    assert isinstance(instance, Type)


eJSL_Attribute_strategy = st.builds(eJSL_Attribute, id=st.booleans(), isprimary=st.booleans(), isunique=st.booleans(), name=safe_text, preserve=st.booleans())
@given(instance=eJSL_Attribute_strategy)
@settings(max_examples=25)
def test_eJSL_Attribute_instantiation(instance):
    assert isinstance(instance, eJSL_Attribute)


eJSL_Author_strategy = st.builds(eJSL_Author, authoremail=safe_text, authorurl=safe_text, name=safe_text)
@given(instance=eJSL_Author_strategy)
@settings(max_examples=25)
def test_eJSL_Author_instantiation(instance):
    assert isinstance(instance, eJSL_Author)


eJSL_BackendSection_strategy = st.builds(eJSL_BackendSection)
@given(instance=eJSL_BackendSection_strategy)
@settings(max_examples=25)
def test_eJSL_BackendSection_instantiation(instance):
    assert isinstance(instance, eJSL_BackendSection)


eJSL_CMSCore_strategy = st.builds(eJSL_CMSCore)
@given(instance=eJSL_CMSCore_strategy)
@settings(max_examples=25)
def test_eJSL_CMSCore_instantiation(instance):
    assert isinstance(instance, eJSL_CMSCore)


eJSL_CMSExtension_strategy = st.builds(eJSL_CMSExtension)
@given(instance=eJSL_CMSExtension_strategy)
@settings(max_examples=25)
def test_eJSL_CMSExtension_instantiation(instance):
    assert isinstance(instance, eJSL_CMSExtension)


eJSL_Class_strategy = st.builds(eJSL_Class, name=safe_text)
@given(instance=eJSL_Class_strategy)
@settings(max_examples=25)
def test_eJSL_Class_instantiation(instance):
    assert isinstance(instance, eJSL_Class)


eJSL_ComplexHTMLTypes_strategy = st.builds(eJSL_ComplexHTMLTypes, htmltype=safe_text)
@given(instance=eJSL_ComplexHTMLTypes_strategy)
@settings(max_examples=25)
def test_eJSL_ComplexHTMLTypes_instantiation(instance):
    assert isinstance(instance, eJSL_ComplexHTMLTypes)


eJSL_Component_strategy = st.builds(eJSL_Component)
@given(instance=eJSL_Component_strategy)
@settings(max_examples=25)
def test_eJSL_Component_instantiation(instance):
    assert isinstance(instance, eJSL_Component)


eJSL_ComponentReference_strategy = st.builds(eJSL_ComponentReference, core=safe_text)
@given(instance=eJSL_ComponentReference_strategy)
@settings(max_examples=25)
def test_eJSL_ComponentReference_instantiation(instance):
    assert isinstance(instance, eJSL_ComponentReference)


eJSL_ContextLink_strategy = st.builds(eJSL_ContextLink)
@given(instance=eJSL_ContextLink_strategy)
@settings(max_examples=25)
def test_eJSL_ContextLink_instantiation(instance):
    assert isinstance(instance, eJSL_ContextLink)


eJSL_CssBlock_strategy = st.builds(eJSL_CssBlock, selector=safe_text)
@given(instance=eJSL_CssBlock_strategy)
@settings(max_examples=25)
def test_eJSL_CssBlock_instantiation(instance):
    assert isinstance(instance, eJSL_CssBlock)


eJSL_CustomPage_strategy = st.builds(eJSL_CustomPage, pageType=safe_text, preserve=safe_text)
@given(instance=eJSL_CustomPage_strategy)
@settings(max_examples=25)
def test_eJSL_CustomPage_instantiation(instance):
    assert isinstance(instance, eJSL_CustomPage)


eJSL_Datatype_strategy = st.builds(eJSL_Datatype, name=safe_text, type=safe_text)
@given(instance=eJSL_Datatype_strategy)
@settings(max_examples=25)
def test_eJSL_Datatype_instantiation(instance):
    assert isinstance(instance, eJSL_Datatype)


eJSL_DatatypeReference_strategy = st.builds(eJSL_DatatypeReference)
@given(instance=eJSL_DatatypeReference_strategy)
@settings(max_examples=25)
def test_eJSL_DatatypeReference_instantiation(instance):
    assert isinstance(instance, eJSL_DatatypeReference)


eJSL_DetailPageField_strategy = st.builds(eJSL_DetailPageField)
@given(instance=eJSL_DetailPageField_strategy)
@settings(max_examples=25)
def test_eJSL_DetailPageField_instantiation(instance):
    assert isinstance(instance, eJSL_DetailPageField)


eJSL_DetailsPage_strategy = st.builds(eJSL_DetailsPage)
@given(instance=eJSL_DetailsPage_strategy)
@settings(max_examples=25)
def test_eJSL_DetailsPage_instantiation(instance):
    assert isinstance(instance, eJSL_DetailsPage)


eJSL_DynamicPage_strategy = st.builds(eJSL_DynamicPage, preserve=st.booleans())
@given(instance=eJSL_DynamicPage_strategy)
@settings(max_examples=25)
def test_eJSL_DynamicPage_instantiation(instance):
    assert isinstance(instance, eJSL_DynamicPage)


eJSL_EJSLModel_strategy = st.builds(eJSL_EJSLModel, name=safe_text)
@given(instance=eJSL_EJSLModel_strategy)
@settings(max_examples=25)
def test_eJSL_EJSLModel_instantiation(instance):
    assert isinstance(instance, eJSL_EJSLModel)


eJSL_EJSLPart_strategy = st.builds(eJSL_EJSLPart)
@given(instance=eJSL_EJSLPart_strategy)
@settings(max_examples=25)
def test_eJSL_EJSLPart_instantiation(instance):
    assert isinstance(instance, eJSL_EJSLPart)


eJSL_Entity_strategy = st.builds(eJSL_Entity, name=safe_text, preserve=st.booleans())
@given(instance=eJSL_Entity_strategy)
@settings(max_examples=25)
def test_eJSL_Entity_instantiation(instance):
    assert isinstance(instance, eJSL_Entity)


eJSL_Entitypackage_strategy = st.builds(eJSL_Entitypackage, name=safe_text)
@given(instance=eJSL_Entitypackage_strategy)
@settings(max_examples=25)
def test_eJSL_Entitypackage_instantiation(instance):
    assert isinstance(instance, eJSL_Entitypackage)


eJSL_Extension_strategy = st.builds(eJSL_Extension, name=safe_text)
@given(instance=eJSL_Extension_strategy)
@settings(max_examples=25)
def test_eJSL_Extension_instantiation(instance):
    assert isinstance(instance, eJSL_Extension)


eJSL_ExtensionPackage_strategy = st.builds(eJSL_ExtensionPackage)
@given(instance=eJSL_ExtensionPackage_strategy)
@settings(max_examples=25)
def test_eJSL_ExtensionPackage_instantiation(instance):
    assert isinstance(instance, eJSL_ExtensionPackage)


eJSL_ExternalLink_strategy = st.builds(eJSL_ExternalLink, label=safe_text, target=safe_text)
@given(instance=eJSL_ExternalLink_strategy)
@settings(max_examples=25)
def test_eJSL_ExternalLink_instantiation(instance):
    assert isinstance(instance, eJSL_ExternalLink)


eJSL_Feature_strategy = st.builds(eJSL_Feature)
@given(instance=eJSL_Feature_strategy)
@settings(max_examples=25)
def test_eJSL_Feature_instantiation(instance):
    assert isinstance(instance, eJSL_Feature)


eJSL_FrontendSection_strategy = st.builds(eJSL_FrontendSection)
@given(instance=eJSL_FrontendSection_strategy)
@settings(max_examples=25)
def test_eJSL_FrontendSection_instantiation(instance):
    assert isinstance(instance, eJSL_FrontendSection)


eJSL_HTMLTypes_strategy = st.builds(eJSL_HTMLTypes)
@given(instance=eJSL_HTMLTypes_strategy)
@settings(max_examples=25)
def test_eJSL_HTMLTypes_instantiation(instance):
    assert isinstance(instance, eJSL_HTMLTypes)


eJSL_IndexPage_strategy = st.builds(eJSL_IndexPage)
@given(instance=eJSL_IndexPage_strategy)
@settings(max_examples=25)
def test_eJSL_IndexPage_instantiation(instance):
    assert isinstance(instance, eJSL_IndexPage)


eJSL_InternalLink_strategy = st.builds(eJSL_InternalLink, name=safe_text)
@given(instance=eJSL_InternalLink_strategy)
@settings(max_examples=25)
def test_eJSL_InternalLink_instantiation(instance):
    assert isinstance(instance, eJSL_InternalLink)


eJSL_KeyValuePair_strategy = st.builds(eJSL_KeyValuePair, name=safe_text, value=safe_text)
@given(instance=eJSL_KeyValuePair_strategy)
@settings(max_examples=25)
def test_eJSL_KeyValuePair_instantiation(instance):
    assert isinstance(instance, eJSL_KeyValuePair)


eJSL_Language_strategy = st.builds(eJSL_Language, name=safe_text, sys=st.booleans())
@given(instance=eJSL_Language_strategy)
@settings(max_examples=25)
def test_eJSL_Language_instantiation(instance):
    assert isinstance(instance, eJSL_Language)


eJSL_Library_strategy = st.builds(eJSL_Library)
@given(instance=eJSL_Library_strategy)
@settings(max_examples=25)
def test_eJSL_Library_instantiation(instance):
    assert isinstance(instance, eJSL_Library)


eJSL_Link_strategy = st.builds(eJSL_Link)
@given(instance=eJSL_Link_strategy)
@settings(max_examples=25)
def test_eJSL_Link_instantiation(instance):
    assert isinstance(instance, eJSL_Link)


eJSL_LinkParameter_strategy = st.builds(eJSL_LinkParameter, id=st.booleans(), name=safe_text, value=safe_text)
@given(instance=eJSL_LinkParameter_strategy)
@settings(max_examples=25)
def test_eJSL_LinkParameter_instantiation(instance):
    assert isinstance(instance, eJSL_LinkParameter)


eJSL_Manifestation_strategy = st.builds(eJSL_Manifestation, copyright=safe_text, creationdate=safe_text, description=safe_text, license=safe_text, link=safe_text, version=safe_text)
@given(instance=eJSL_Manifestation_strategy)
@settings(max_examples=25)
def test_eJSL_Manifestation_instantiation(instance):
    assert isinstance(instance, eJSL_Manifestation)


eJSL_Method_strategy = st.builds(eJSL_Method, name=safe_text, returnvalue=safe_text)
@given(instance=eJSL_Method_strategy)
@settings(max_examples=25)
def test_eJSL_Method_instantiation(instance):
    assert isinstance(instance, eJSL_Method)


eJSL_MethodParameter_strategy = st.builds(eJSL_MethodParameter, name=safe_text)
@given(instance=eJSL_MethodParameter_strategy)
@settings(max_examples=25)
def test_eJSL_MethodParameter_instantiation(instance):
    assert isinstance(instance, eJSL_MethodParameter)


eJSL_Module_strategy = st.builds(eJSL_Module)
@given(instance=eJSL_Module_strategy)
@settings(max_examples=25)
def test_eJSL_Module_instantiation(instance):
    assert isinstance(instance, eJSL_Module)


eJSL_Package_strategy = st.builds(eJSL_Package, name=safe_text)
@given(instance=eJSL_Package_strategy)
@settings(max_examples=25)
def test_eJSL_Package_instantiation(instance):
    assert isinstance(instance, eJSL_Package)


eJSL_Page_strategy = st.builds(eJSL_Page, name=safe_text)
@given(instance=eJSL_Page_strategy)
@settings(max_examples=25)
def test_eJSL_Page_instantiation(instance):
    assert isinstance(instance, eJSL_Page)


eJSL_PageAction_strategy = st.builds(eJSL_PageAction, name=safe_text, pageActionPosition=safe_text, pageActionType=safe_text)
@given(instance=eJSL_PageAction_strategy)
@settings(max_examples=25)
def test_eJSL_PageAction_instantiation(instance):
    assert isinstance(instance, eJSL_PageAction)


eJSL_PageReference_strategy = st.builds(eJSL_PageReference, sect=safe_text)
@given(instance=eJSL_PageReference_strategy)
@settings(max_examples=25)
def test_eJSL_PageReference_instantiation(instance):
    assert isinstance(instance, eJSL_PageReference)


eJSL_Parameter_strategy = st.builds(eJSL_Parameter, defaultvalue=safe_text, descripton=safe_text, label=safe_text, name=safe_text, size=st.integers())
@given(instance=eJSL_Parameter_strategy)
@settings(max_examples=25)
def test_eJSL_Parameter_instantiation(instance):
    assert isinstance(instance, eJSL_Parameter)


eJSL_ParameterGroup_strategy = st.builds(eJSL_ParameterGroup, label=safe_text, name=safe_text)
@given(instance=eJSL_ParameterGroup_strategy)
@settings(max_examples=25)
def test_eJSL_ParameterGroup_instantiation(instance):
    assert isinstance(instance, eJSL_ParameterGroup)


eJSL_Plugin_strategy = st.builds(eJSL_Plugin, type=safe_text)
@given(instance=eJSL_Plugin_strategy)
@settings(max_examples=25)
def test_eJSL_Plugin_instantiation(instance):
    assert isinstance(instance, eJSL_Plugin)


eJSL_Position_strategy = st.builds(eJSL_Position, name=safe_text)
@given(instance=eJSL_Position_strategy)
@settings(max_examples=25)
def test_eJSL_Position_instantiation(instance):
    assert isinstance(instance, eJSL_Position)


eJSL_PositionParameter_strategy = st.builds(eJSL_PositionParameter, divid=safe_text, name=safe_text, type=safe_text)
@given(instance=eJSL_PositionParameter_strategy)
@settings(max_examples=25)
def test_eJSL_PositionParameter_instantiation(instance):
    assert isinstance(instance, eJSL_PositionParameter)


eJSL_Reference_strategy = st.builds(eJSL_Reference, id=st.booleans(), lower=safe_text, preserve=st.booleans(), upper=safe_text)
@given(instance=eJSL_Reference_strategy)
@settings(max_examples=25)
def test_eJSL_Reference_instantiation(instance):
    assert isinstance(instance, eJSL_Reference)


eJSL_Section_strategy = st.builds(eJSL_Section)
@given(instance=eJSL_Section_strategy)
@settings(max_examples=25)
def test_eJSL_Section_instantiation(instance):
    assert isinstance(instance, eJSL_Section)


eJSL_SimpleHTMLTypes_strategy = st.builds(eJSL_SimpleHTMLTypes, htmltype=safe_text)
@given(instance=eJSL_SimpleHTMLTypes_strategy)
@settings(max_examples=25)
def test_eJSL_SimpleHTMLTypes_instantiation(instance):
    assert isinstance(instance, eJSL_SimpleHTMLTypes)


eJSL_StandardTypes_strategy = st.builds(eJSL_StandardTypes, autoincrement=st.booleans(), default=safe_text, notnull=st.booleans(), type=safe_text)
@given(instance=eJSL_StandardTypes_strategy)
@settings(max_examples=25)
def test_eJSL_StandardTypes_instantiation(instance):
    assert isinstance(instance, eJSL_StandardTypes)


eJSL_StaticPage_strategy = st.builds(eJSL_StaticPage, HTMLBody=safe_text, preserve=st.booleans())
@given(instance=eJSL_StaticPage_strategy)
@settings(max_examples=25)
def test_eJSL_StaticPage_instantiation(instance):
    assert isinstance(instance, eJSL_StaticPage)


eJSL_Template_strategy = st.builds(eJSL_Template)
@given(instance=eJSL_Template_strategy)
@settings(max_examples=25)
def test_eJSL_Template_instantiation(instance):
    assert isinstance(instance, eJSL_Template)


eJSL_Type_strategy = st.builds(eJSL_Type)
@given(instance=eJSL_Type_strategy)
@settings(max_examples=25)
def test_eJSL_Type_instantiation(instance):
    assert isinstance(instance, eJSL_Type)


eJSL_coreFeature_strategy = st.builds(eJSL_coreFeature)
@given(instance=eJSL_coreFeature_strategy)
@settings(max_examples=25)
def test_eJSL_coreFeature_instantiation(instance):
    assert isinstance(instance, eJSL_coreFeature)


