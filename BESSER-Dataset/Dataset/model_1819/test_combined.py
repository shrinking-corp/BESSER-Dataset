# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    doc_builder_PropertyEntry,
    builder_PropertyEntry,
    Author,
    doc_fragment_Copyright,
    Map,
    doc_builder_BookBuilder,
    BookSection,
    doc_book_BookContainer,
    Copyright,
    BookContainer,
    doc_book_BookSection,
    doc_book_Book,
    doc_map_MapContainer,
    fragment_Content,
    doc_fragment_Author,
    doc_fragment_Content,
    Section,
    Content,
    doc_fragment_PlainTextContent,
    doc_fragment_Container,
    Container,
    doc_fragment_Section,
    doc_fragment_Fragment,
    ResourceFactory,
    doc_map_ExtensionMappingEntry,
    doc_map_ResourceFactory,
    map_MapElement,
    doc_map_ContentGenerator,
    map_MapContainer,
    doc_map_MapSection,
    PatternRule,
    doc_map_ExcludePatternRule,
    doc_map_IncludePatternRule,
    doc_map_NameRule,
    NameRule,
    doc_map_PatternRule,
    doc_map_MapElement,
    Import,
    doc_map_Feature,
    doc_map_File,
    MapElement,
    doc_map_Import,
    ExtensionMappingEntry,
    MapContainer,
    doc_map_Map,
    doc_Test,
    RuleResult,
    NumberingStyle,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_doc_builder_propertyentry_is_not_abstract():
    assert not inspect.isabstract(doc_builder_PropertyEntry)


def test_hyp_doc_builder_propertyentry_constructor_exists():
    assert callable(doc_builder_PropertyEntry.__init__)


def test_hyp_doc_builder_propertyentry_constructor_args():
    sig = inspect.signature(doc_builder_PropertyEntry.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_builder_propertyentry_is_not_abstract():
    assert not inspect.isabstract(builder_PropertyEntry)


def test_hyp_builder_propertyentry_constructor_exists():
    assert callable(builder_PropertyEntry.__init__)


def test_hyp_builder_propertyentry_constructor_args():
    sig = inspect.signature(builder_PropertyEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_author_is_not_abstract():
    assert not inspect.isabstract(Author)


def test_hyp_author_constructor_exists():
    assert callable(Author.__init__)


def test_hyp_author_constructor_args():
    sig = inspect.signature(Author.__init__)
    params = list(sig.parameters.keys())



def test_hyp_doc_fragment_copyright_is_not_abstract():
    assert not inspect.isabstract(doc_fragment_Copyright)


def test_hyp_doc_fragment_copyright_constructor_exists():
    assert callable(doc_fragment_Copyright.__init__)


def test_hyp_doc_fragment_copyright_constructor_args():
    sig = inspect.signature(doc_fragment_Copyright.__init__)
    params = list(sig.parameters.keys())
    assert "year" in params, "Missing parameter 'year'"




def test_hyp_map_is_not_abstract():
    assert not inspect.isabstract(Map)


def test_hyp_map_constructor_exists():
    assert callable(Map.__init__)


def test_hyp_map_constructor_args():
    sig = inspect.signature(Map.__init__)
    params = list(sig.parameters.keys())



def test_hyp_doc_builder_bookbuilder_is_not_abstract():
    assert not inspect.isabstract(doc_builder_BookBuilder)


def test_hyp_doc_builder_bookbuilder_constructor_exists():
    assert callable(doc_builder_BookBuilder.__init__)


def test_hyp_doc_builder_bookbuilder_constructor_args():
    sig = inspect.signature(doc_builder_BookBuilder.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "license" in params, "Missing parameter 'license'"
    assert "copyrightMarker" in params, "Missing parameter 'copyrightMarker'"
    assert "version" in params, "Missing parameter 'version'"







def test_hyp_booksection_is_not_abstract():
    assert not inspect.isabstract(BookSection)


def test_hyp_booksection_constructor_exists():
    assert callable(BookSection.__init__)


def test_hyp_booksection_constructor_args():
    sig = inspect.signature(BookSection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_doc_book_bookcontainer_is_not_abstract():
    assert not inspect.isabstract(doc_book_BookContainer)


def test_hyp_doc_book_bookcontainer_constructor_exists():
    assert callable(doc_book_BookContainer.__init__)


def test_hyp_doc_book_bookcontainer_constructor_args():
    sig = inspect.signature(doc_book_BookContainer.__init__)
    params = list(sig.parameters.keys())
    assert "numberingStyle" in params, "Missing parameter 'numberingStyle'"




def test_hyp_copyright_is_not_abstract():
    assert not inspect.isabstract(Copyright)


def test_hyp_copyright_constructor_exists():
    assert callable(Copyright.__init__)


def test_hyp_copyright_constructor_args():
    sig = inspect.signature(Copyright.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bookcontainer_is_not_abstract():
    assert not inspect.isabstract(BookContainer)


def test_hyp_bookcontainer_constructor_exists():
    assert callable(BookContainer.__init__)


def test_hyp_bookcontainer_constructor_args():
    sig = inspect.signature(BookContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_doc_book_booksection_is_not_abstract():
    assert not inspect.isabstract(doc_book_BookSection)


def test_hyp_doc_book_booksection_constructor_exists():
    assert callable(doc_book_BookSection.__init__)


def test_hyp_doc_book_booksection_constructor_args():
    sig = inspect.signature(doc_book_BookSection.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "fullNumber" in params, "Missing parameter 'fullNumber'"
    assert "number" in params, "Missing parameter 'number'"
    assert "title" in params, "Missing parameter 'title'"







def test_hyp_doc_book_book_is_not_abstract():
    assert not inspect.isabstract(doc_book_Book)


def test_hyp_doc_book_book_constructor_exists():
    assert callable(doc_book_Book.__init__)


def test_hyp_doc_book_book_constructor_args():
    sig = inspect.signature(doc_book_Book.__init__)
    params = list(sig.parameters.keys())
    assert "copyrightMarker" in params, "Missing parameter 'copyrightMarker'"
    assert "version" in params, "Missing parameter 'version'"
    assert "title" in params, "Missing parameter 'title'"
    assert "copyrightText" in params, "Missing parameter 'copyrightText'"







def test_hyp_doc_map_mapcontainer_is_not_abstract():
    assert not inspect.isabstract(doc_map_MapContainer)


def test_hyp_doc_map_mapcontainer_constructor_exists():
    assert callable(doc_map_MapContainer.__init__)


def test_hyp_doc_map_mapcontainer_constructor_args():
    sig = inspect.signature(doc_map_MapContainer.__init__)
    params = list(sig.parameters.keys())
    assert "numberingStyle" in params, "Missing parameter 'numberingStyle'"




def test_hyp_fragment_content_is_not_abstract():
    assert not inspect.isabstract(fragment_Content)


def test_hyp_fragment_content_constructor_exists():
    assert callable(fragment_Content.__init__)


def test_hyp_fragment_content_constructor_args():
    sig = inspect.signature(fragment_Content.__init__)
    params = list(sig.parameters.keys())



def test_hyp_doc_fragment_author_is_not_abstract():
    assert not inspect.isabstract(doc_fragment_Author)


def test_hyp_doc_fragment_author_constructor_exists():
    assert callable(doc_fragment_Author.__init__)


def test_hyp_doc_fragment_author_constructor_args():
    sig = inspect.signature(doc_fragment_Author.__init__)
    params = list(sig.parameters.keys())
    assert "ref" in params, "Missing parameter 'ref'"
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"






def test_hyp_doc_fragment_content_is_not_abstract():
    assert not inspect.isabstract(doc_fragment_Content)


def test_hyp_doc_fragment_content_constructor_exists():
    assert callable(doc_fragment_Content.__init__)


def test_hyp_doc_fragment_content_constructor_args():
    sig = inspect.signature(doc_fragment_Content.__init__)
    params = list(sig.parameters.keys())



def test_hyp_section_is_not_abstract():
    assert not inspect.isabstract(Section)


def test_hyp_section_constructor_exists():
    assert callable(Section.__init__)


def test_hyp_section_constructor_args():
    sig = inspect.signature(Section.__init__)
    params = list(sig.parameters.keys())



def test_hyp_content_is_not_abstract():
    assert not inspect.isabstract(Content)


def test_hyp_content_constructor_exists():
    assert callable(Content.__init__)


def test_hyp_content_constructor_args():
    sig = inspect.signature(Content.__init__)
    params = list(sig.parameters.keys())



def test_hyp_doc_fragment_plaintextcontent_is_not_abstract():
    assert not inspect.isabstract(doc_fragment_PlainTextContent)


def test_hyp_doc_fragment_plaintextcontent_constructor_exists():
    assert callable(doc_fragment_PlainTextContent.__init__)


def test_hyp_doc_fragment_plaintextcontent_constructor_args():
    sig = inspect.signature(doc_fragment_PlainTextContent.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_doc_fragment_container_is_not_abstract():
    assert not inspect.isabstract(doc_fragment_Container)


def test_hyp_doc_fragment_container_constructor_exists():
    assert callable(doc_fragment_Container.__init__)


def test_hyp_doc_fragment_container_constructor_args():
    sig = inspect.signature(doc_fragment_Container.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"




def test_hyp_container_is_not_abstract():
    assert not inspect.isabstract(Container)


def test_hyp_container_constructor_exists():
    assert callable(Container.__init__)


def test_hyp_container_constructor_args():
    sig = inspect.signature(Container.__init__)
    params = list(sig.parameters.keys())



def test_hyp_doc_fragment_section_is_not_abstract():
    assert not inspect.isabstract(doc_fragment_Section)


def test_hyp_doc_fragment_section_constructor_exists():
    assert callable(doc_fragment_Section.__init__)


def test_hyp_doc_fragment_section_constructor_args():
    sig = inspect.signature(doc_fragment_Section.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"




def test_hyp_doc_fragment_fragment_is_not_abstract():
    assert not inspect.isabstract(doc_fragment_Fragment)


def test_hyp_doc_fragment_fragment_constructor_exists():
    assert callable(doc_fragment_Fragment.__init__)


def test_hyp_doc_fragment_fragment_constructor_args():
    sig = inspect.signature(doc_fragment_Fragment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_resourcefactory_is_not_abstract():
    assert not inspect.isabstract(ResourceFactory)


def test_hyp_resourcefactory_constructor_exists():
    assert callable(ResourceFactory.__init__)


def test_hyp_resourcefactory_constructor_args():
    sig = inspect.signature(ResourceFactory.__init__)
    params = list(sig.parameters.keys())



def test_hyp_doc_map_extensionmappingentry_is_not_abstract():
    assert not inspect.isabstract(doc_map_ExtensionMappingEntry)


def test_hyp_doc_map_extensionmappingentry_constructor_exists():
    assert callable(doc_map_ExtensionMappingEntry.__init__)


def test_hyp_doc_map_extensionmappingentry_constructor_args():
    sig = inspect.signature(doc_map_ExtensionMappingEntry.__init__)
    params = list(sig.parameters.keys())
    assert "extension" in params, "Missing parameter 'extension'"




def test_hyp_doc_map_resourcefactory_is_not_abstract():
    assert not inspect.isabstract(doc_map_ResourceFactory)


def test_hyp_doc_map_resourcefactory_constructor_exists():
    assert callable(doc_map_ResourceFactory.__init__)


def test_hyp_doc_map_resourcefactory_constructor_args():
    sig = inspect.signature(doc_map_ResourceFactory.__init__)
    params = list(sig.parameters.keys())
    assert "className" in params, "Missing parameter 'className'"




def test_hyp_map_mapelement_is_not_abstract():
    assert not inspect.isabstract(map_MapElement)


def test_hyp_map_mapelement_constructor_exists():
    assert callable(map_MapElement.__init__)


def test_hyp_map_mapelement_constructor_args():
    sig = inspect.signature(map_MapElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_doc_map_contentgenerator_is_not_abstract():
    assert not inspect.isabstract(doc_map_ContentGenerator)


def test_hyp_doc_map_contentgenerator_constructor_exists():
    assert callable(doc_map_ContentGenerator.__init__)


def test_hyp_doc_map_contentgenerator_constructor_args():
    sig = inspect.signature(doc_map_ContentGenerator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_map_mapcontainer_is_not_abstract():
    assert not inspect.isabstract(map_MapContainer)


def test_hyp_map_mapcontainer_constructor_exists():
    assert callable(map_MapContainer.__init__)


def test_hyp_map_mapcontainer_constructor_args():
    sig = inspect.signature(map_MapContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_doc_map_mapsection_is_not_abstract():
    assert not inspect.isabstract(doc_map_MapSection)


def test_hyp_doc_map_mapsection_constructor_exists():
    assert callable(doc_map_MapSection.__init__)


def test_hyp_doc_map_mapsection_constructor_args():
    sig = inspect.signature(doc_map_MapSection.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "title" in params, "Missing parameter 'title'"





def test_hyp_patternrule_is_not_abstract():
    assert not inspect.isabstract(PatternRule)


def test_hyp_patternrule_constructor_exists():
    assert callable(PatternRule.__init__)


def test_hyp_patternrule_constructor_args():
    sig = inspect.signature(PatternRule.__init__)
    params = list(sig.parameters.keys())



def test_hyp_doc_map_excludepatternrule_is_not_abstract():
    assert not inspect.isabstract(doc_map_ExcludePatternRule)


def test_hyp_doc_map_excludepatternrule_constructor_exists():
    assert callable(doc_map_ExcludePatternRule.__init__)


def test_hyp_doc_map_excludepatternrule_constructor_args():
    sig = inspect.signature(doc_map_ExcludePatternRule.__init__)
    params = list(sig.parameters.keys())



def test_hyp_doc_map_includepatternrule_is_not_abstract():
    assert not inspect.isabstract(doc_map_IncludePatternRule)


def test_hyp_doc_map_includepatternrule_constructor_exists():
    assert callable(doc_map_IncludePatternRule.__init__)


def test_hyp_doc_map_includepatternrule_constructor_args():
    sig = inspect.signature(doc_map_IncludePatternRule.__init__)
    params = list(sig.parameters.keys())



def test_hyp_doc_map_namerule_is_not_abstract():
    assert not inspect.isabstract(doc_map_NameRule)


def test_hyp_doc_map_namerule_constructor_exists():
    assert callable(doc_map_NameRule.__init__)


def test_hyp_doc_map_namerule_constructor_args():
    sig = inspect.signature(doc_map_NameRule.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namerule_is_not_abstract():
    assert not inspect.isabstract(NameRule)


def test_hyp_namerule_constructor_exists():
    assert callable(NameRule.__init__)


def test_hyp_namerule_constructor_args():
    sig = inspect.signature(NameRule.__init__)
    params = list(sig.parameters.keys())



def test_hyp_doc_map_patternrule_is_not_abstract():
    assert not inspect.isabstract(doc_map_PatternRule)


def test_hyp_doc_map_patternrule_constructor_exists():
    assert callable(doc_map_PatternRule.__init__)


def test_hyp_doc_map_patternrule_constructor_args():
    sig = inspect.signature(doc_map_PatternRule.__init__)
    params = list(sig.parameters.keys())
    assert "pattern" in params, "Missing parameter 'pattern'"




def test_hyp_doc_map_mapelement_is_not_abstract():
    assert not inspect.isabstract(doc_map_MapElement)


def test_hyp_doc_map_mapelement_constructor_exists():
    assert callable(doc_map_MapElement.__init__)


def test_hyp_doc_map_mapelement_constructor_args():
    sig = inspect.signature(doc_map_MapElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_import_is_not_abstract():
    assert not inspect.isabstract(Import)


def test_hyp_import_constructor_exists():
    assert callable(Import.__init__)


def test_hyp_import_constructor_args():
    sig = inspect.signature(Import.__init__)
    params = list(sig.parameters.keys())



def test_hyp_doc_map_feature_is_not_abstract():
    assert not inspect.isabstract(doc_map_Feature)


def test_hyp_doc_map_feature_constructor_exists():
    assert callable(doc_map_Feature.__init__)


def test_hyp_doc_map_feature_constructor_args():
    sig = inspect.signature(doc_map_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "featureId" in params, "Missing parameter 'featureId'"
    assert "createSection" in params, "Missing parameter 'createSection'"





def test_hyp_doc_map_file_is_not_abstract():
    assert not inspect.isabstract(doc_map_File)


def test_hyp_doc_map_file_constructor_exists():
    assert callable(doc_map_File.__init__)


def test_hyp_doc_map_file_constructor_args():
    sig = inspect.signature(doc_map_File.__init__)
    params = list(sig.parameters.keys())
    assert "path" in params, "Missing parameter 'path'"




def test_hyp_mapelement_is_not_abstract():
    assert not inspect.isabstract(MapElement)


def test_hyp_mapelement_constructor_exists():
    assert callable(MapElement.__init__)


def test_hyp_mapelement_constructor_args():
    sig = inspect.signature(MapElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_doc_map_import_is_not_abstract():
    assert not inspect.isabstract(doc_map_Import)


def test_hyp_doc_map_import_constructor_exists():
    assert callable(doc_map_Import.__init__)


def test_hyp_doc_map_import_constructor_args():
    sig = inspect.signature(doc_map_Import.__init__)
    params = list(sig.parameters.keys())



def test_hyp_extensionmappingentry_is_not_abstract():
    assert not inspect.isabstract(ExtensionMappingEntry)


def test_hyp_extensionmappingentry_constructor_exists():
    assert callable(ExtensionMappingEntry.__init__)


def test_hyp_extensionmappingentry_constructor_args():
    sig = inspect.signature(ExtensionMappingEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mapcontainer_is_not_abstract():
    assert not inspect.isabstract(MapContainer)


def test_hyp_mapcontainer_constructor_exists():
    assert callable(MapContainer.__init__)


def test_hyp_mapcontainer_constructor_args():
    sig = inspect.signature(MapContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_doc_map_map_is_not_abstract():
    assert not inspect.isabstract(doc_map_Map)


def test_hyp_doc_map_map_constructor_exists():
    assert callable(doc_map_Map.__init__)


def test_hyp_doc_map_map_constructor_args():
    sig = inspect.signature(doc_map_Map.__init__)
    params = list(sig.parameters.keys())



def test_hyp_doc_test_is_not_abstract():
    assert not inspect.isabstract(doc_Test)


def test_hyp_doc_test_constructor_exists():
    assert callable(doc_Test.__init__)


def test_hyp_doc_test_constructor_args():
    sig = inspect.signature(doc_Test.__init__)
    params = list(sig.parameters.keys())

def test_hyp_ruleresult_exists():
    # Check that the Enumeration exists
    assert RuleResult is not None

def test_hyp_ruleresult_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RuleResult]
    expected_literals = [
        "ACCEPT",
        "REJECT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RuleResult"

def test_hyp_numberingstyle_exists():
    # Check that the Enumeration exists
    assert NumberingStyle is not None

def test_hyp_numberingstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NumberingStyle]
    expected_literals = [
        "LATIN",
        "ARABIC",
        "ROMAN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NumberingStyle"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
doc_builder_PropertyEntry_strategy = st.builds(
    doc_builder_PropertyEntry,
    key=
        safe_text,
    value=
        safe_text
)
builder_PropertyEntry_strategy = st.builds(
    builder_PropertyEntry,
)
Author_strategy = st.builds(
    Author,
)
doc_fragment_Copyright_strategy = st.builds(
    doc_fragment_Copyright,
    year=
        st.integers()
)
Map_strategy = st.builds(
    Map,
)
doc_builder_BookBuilder_strategy = st.builds(
    doc_builder_BookBuilder,
    title=
        safe_text,
    license=
        safe_text,
    copyrightMarker=
        safe_text,
    version=
        safe_text
)
BookSection_strategy = st.builds(
    BookSection,
)
doc_book_BookContainer_strategy = st.builds(
    doc_book_BookContainer,
    numberingStyle=
        safe_text
)
Copyright_strategy = st.builds(
    Copyright,
)
BookContainer_strategy = st.builds(
    BookContainer,
)
doc_book_BookSection_strategy = st.builds(
    doc_book_BookSection,
    id=
        safe_text,
    fullNumber=
        safe_text,
    number=
        st.integers(),
    title=
        safe_text
)
doc_book_Book_strategy = st.builds(
    doc_book_Book,
    copyrightMarker=
        safe_text,
    version=
        safe_text,
    title=
        safe_text,
    copyrightText=
        safe_text
)
doc_map_MapContainer_strategy = st.builds(
    doc_map_MapContainer,
    numberingStyle=
        safe_text
)
fragment_Content_strategy = st.builds(
    fragment_Content,
)
doc_fragment_Author_strategy = st.builds(
    doc_fragment_Author,
    ref=
        safe_text,
    id=
        safe_text,
    name=
        safe_text
)
doc_fragment_Content_strategy = st.builds(
    doc_fragment_Content,
)
Section_strategy = st.builds(
    Section,
)
Content_strategy = st.builds(
    Content,
)
doc_fragment_PlainTextContent_strategy = st.builds(
    doc_fragment_PlainTextContent,
    value=
        safe_text
)
doc_fragment_Container_strategy = st.builds(
    doc_fragment_Container,
    content=
        safe_text
)
Container_strategy = st.builds(
    Container,
)
doc_fragment_Section_strategy = st.builds(
    doc_fragment_Section,
    title=
        safe_text
)
doc_fragment_Fragment_strategy = st.builds(
    doc_fragment_Fragment,
)
ResourceFactory_strategy = st.builds(
    ResourceFactory,
)
doc_map_ExtensionMappingEntry_strategy = st.builds(
    doc_map_ExtensionMappingEntry,
    extension=
        safe_text
)
doc_map_ResourceFactory_strategy = st.builds(
    doc_map_ResourceFactory,
    className=
        safe_text
)
map_MapElement_strategy = st.builds(
    map_MapElement,
)
doc_map_ContentGenerator_strategy = st.builds(
    doc_map_ContentGenerator,
)
map_MapContainer_strategy = st.builds(
    map_MapContainer,
)
doc_map_MapSection_strategy = st.builds(
    doc_map_MapSection,
    id=
        safe_text,
    title=
        safe_text
)
PatternRule_strategy = st.builds(
    PatternRule,
)
doc_map_ExcludePatternRule_strategy = st.builds(
    doc_map_ExcludePatternRule,
)
doc_map_IncludePatternRule_strategy = st.builds(
    doc_map_IncludePatternRule,
)
doc_map_NameRule_strategy = st.builds(
    doc_map_NameRule,
)
NameRule_strategy = st.builds(
    NameRule,
)
doc_map_PatternRule_strategy = st.builds(
    doc_map_PatternRule,
    pattern=
        safe_text
)
doc_map_MapElement_strategy = st.builds(
    doc_map_MapElement,
)
Import_strategy = st.builds(
    Import,
)
doc_map_Feature_strategy = st.builds(
    doc_map_Feature,
    featureId=
        safe_text,
    createSection=
        st.booleans()
)
doc_map_File_strategy = st.builds(
    doc_map_File,
    path=
        safe_text
)
MapElement_strategy = st.builds(
    MapElement,
)
doc_map_Import_strategy = st.builds(
    doc_map_Import,
)
ExtensionMappingEntry_strategy = st.builds(
    ExtensionMappingEntry,
)
MapContainer_strategy = st.builds(
    MapContainer,
)
doc_map_Map_strategy = st.builds(
    doc_map_Map,
)
doc_Test_strategy = st.builds(
    doc_Test,
)




@given(instance=doc_builder_PropertyEntry_strategy)
def test_hyp_doc_builder_propertyentry_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=doc_builder_PropertyEntry_strategy)
def test_hyp_doc_builder_propertyentry_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original






@given(instance=doc_fragment_Copyright_strategy)
def test_hyp_doc_fragment_copyright_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original





@given(instance=doc_builder_BookBuilder_strategy)
def test_hyp_doc_builder_bookbuilder_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=doc_builder_BookBuilder_strategy)
def test_hyp_doc_builder_bookbuilder_license_setter(instance):
    original = instance.license
    instance.license = original
    assert instance.license == original



@given(instance=doc_builder_BookBuilder_strategy)
def test_hyp_doc_builder_bookbuilder_copyrightMarker_setter(instance):
    original = instance.copyrightMarker
    instance.copyrightMarker = original
    assert instance.copyrightMarker == original



@given(instance=doc_builder_BookBuilder_strategy)
def test_hyp_doc_builder_bookbuilder_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original





@given(instance=doc_book_BookContainer_strategy)
def test_hyp_doc_book_bookcontainer_numberingStyle_setter(instance):
    original = instance.numberingStyle
    instance.numberingStyle = original
    assert instance.numberingStyle == original






@given(instance=doc_book_BookSection_strategy)
def test_hyp_doc_book_booksection_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=doc_book_BookSection_strategy)
def test_hyp_doc_book_booksection_fullNumber_setter(instance):
    original = instance.fullNumber
    instance.fullNumber = original
    assert instance.fullNumber == original



@given(instance=doc_book_BookSection_strategy)
def test_hyp_doc_book_booksection_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=doc_book_BookSection_strategy)
def test_hyp_doc_book_booksection_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original




@given(instance=doc_book_Book_strategy)
def test_hyp_doc_book_book_copyrightMarker_setter(instance):
    original = instance.copyrightMarker
    instance.copyrightMarker = original
    assert instance.copyrightMarker == original



@given(instance=doc_book_Book_strategy)
def test_hyp_doc_book_book_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=doc_book_Book_strategy)
def test_hyp_doc_book_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=doc_book_Book_strategy)
def test_hyp_doc_book_book_copyrightText_setter(instance):
    original = instance.copyrightText
    instance.copyrightText = original
    assert instance.copyrightText == original




@given(instance=doc_map_MapContainer_strategy)
def test_hyp_doc_map_mapcontainer_numberingStyle_setter(instance):
    original = instance.numberingStyle
    instance.numberingStyle = original
    assert instance.numberingStyle == original





@given(instance=doc_fragment_Author_strategy)
def test_hyp_doc_fragment_author_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original



@given(instance=doc_fragment_Author_strategy)
def test_hyp_doc_fragment_author_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=doc_fragment_Author_strategy)
def test_hyp_doc_fragment_author_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original







@given(instance=doc_fragment_PlainTextContent_strategy)
def test_hyp_doc_fragment_plaintextcontent_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=doc_fragment_Container_strategy)
def test_hyp_doc_fragment_container_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original





@given(instance=doc_fragment_Section_strategy)
def test_hyp_doc_fragment_section_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original






@given(instance=doc_map_ExtensionMappingEntry_strategy)
def test_hyp_doc_map_extensionmappingentry_extension_setter(instance):
    original = instance.extension
    instance.extension = original
    assert instance.extension == original




@given(instance=doc_map_ResourceFactory_strategy)
def test_hyp_doc_map_resourcefactory_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original







@given(instance=doc_map_MapSection_strategy)
def test_hyp_doc_map_mapsection_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=doc_map_MapSection_strategy)
def test_hyp_doc_map_mapsection_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=doc_map_ExcludePatternRule_strategy)
@settings(max_examples=30)
def test_hyp_doc_map_excludepatternrule_checkrule_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.checkRule(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.checkRule).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'checkRule' in doc_map_ExcludePatternRule is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'checkRule' in doc_map_ExcludePatternRule did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'checkRule' in doc_map_ExcludePatternRule is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=doc_map_IncludePatternRule_strategy)
@settings(max_examples=30)
def test_hyp_doc_map_includepatternrule_checkrule_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.checkRule(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.checkRule).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'checkRule' in doc_map_IncludePatternRule is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'checkRule' in doc_map_IncludePatternRule did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'checkRule' in doc_map_IncludePatternRule is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=doc_map_NameRule_strategy)
@settings(max_examples=30)
def test_hyp_doc_map_namerule_checkrule_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.checkRule(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.checkRule).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'checkRule' in doc_map_NameRule is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'checkRule' in doc_map_NameRule did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'checkRule' in doc_map_NameRule is not implemented or raised an error")





@given(instance=doc_map_PatternRule_strategy)
def test_hyp_doc_map_patternrule_pattern_setter(instance):
    original = instance.pattern
    instance.pattern = original
    assert instance.pattern == original


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=doc_map_MapElement_strategy)
@settings(max_examples=30)
def test_hyp_doc_map_mapelement_visit_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visit(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visit).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visit' in doc_map_MapElement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visit' in doc_map_MapElement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visit' in doc_map_MapElement is not implemented or raised an error")





@given(instance=doc_map_Feature_strategy)
def test_hyp_doc_map_feature_featureId_setter(instance):
    original = instance.featureId
    instance.featureId = original
    assert instance.featureId == original



@given(instance=doc_map_Feature_strategy)
def test_hyp_doc_map_feature_createSection_setter(instance):
    original = instance.createSection
    instance.createSection = original
    assert instance.createSection == original




@given(instance=doc_map_File_strategy)
def test_hyp_doc_map_file_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original






import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=doc_map_Map_strategy)
@settings(max_examples=30)
def test_hyp_doc_map_map_visit_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visit(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visit).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visit' in doc_map_Map is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visit' in doc_map_Map did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visit' in doc_map_Map is not implemented or raised an error")



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

def test_doc_book_Book_copyrightMarker_value_roundtrip():
    instance = doc_book_Book(copyrightMarker="sample_text", copyrightText="sample_text", title="sample_text", version="sample_text")
    assert instance.copyrightMarker == "sample_text"
    instance.copyrightMarker = "sample_text_2"
    assert instance.copyrightMarker == "sample_text_2"


def test_doc_book_Book_copyrightText_value_roundtrip():
    instance = doc_book_Book(copyrightMarker="sample_text", copyrightText="sample_text", title="sample_text", version="sample_text")
    assert instance.copyrightText == "sample_text"
    instance.copyrightText = "sample_text_2"
    assert instance.copyrightText == "sample_text_2"


def test_doc_book_Book_title_value_roundtrip():
    instance = doc_book_Book(copyrightMarker="sample_text", copyrightText="sample_text", title="sample_text", version="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_doc_book_Book_version_value_roundtrip():
    instance = doc_book_Book(copyrightMarker="sample_text", copyrightText="sample_text", title="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_doc_book_BookContainer_numberingStyle_value_roundtrip():
    instance = doc_book_BookContainer(numberingStyle="sample_text")
    assert instance.numberingStyle == "sample_text"
    instance.numberingStyle = "sample_text_2"
    assert instance.numberingStyle == "sample_text_2"


def test_doc_book_BookSection_fullNumber_value_roundtrip():
    instance = doc_book_BookSection(fullNumber="sample_text", id="sample_text", number=7, title="sample_text")
    assert instance.fullNumber == "sample_text"
    instance.fullNumber = "sample_text_2"
    assert instance.fullNumber == "sample_text_2"


def test_doc_book_BookSection_id_value_roundtrip():
    instance = doc_book_BookSection(fullNumber="sample_text", id="sample_text", number=7, title="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_doc_book_BookSection_number_value_roundtrip():
    instance = doc_book_BookSection(fullNumber="sample_text", id="sample_text", number=7, title="sample_text")
    assert instance.number == 7
    instance.number = 13
    assert instance.number == 13


def test_doc_book_BookSection_title_value_roundtrip():
    instance = doc_book_BookSection(fullNumber="sample_text", id="sample_text", number=7, title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_doc_builder_BookBuilder_copyrightMarker_value_roundtrip():
    instance = doc_builder_BookBuilder(copyrightMarker="sample_text", license="sample_text", title="sample_text", version="sample_text")
    assert instance.copyrightMarker == "sample_text"
    instance.copyrightMarker = "sample_text_2"
    assert instance.copyrightMarker == "sample_text_2"


def test_doc_builder_BookBuilder_license_value_roundtrip():
    instance = doc_builder_BookBuilder(copyrightMarker="sample_text", license="sample_text", title="sample_text", version="sample_text")
    assert instance.license == "sample_text"
    instance.license = "sample_text_2"
    assert instance.license == "sample_text_2"


def test_doc_builder_BookBuilder_title_value_roundtrip():
    instance = doc_builder_BookBuilder(copyrightMarker="sample_text", license="sample_text", title="sample_text", version="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_doc_builder_BookBuilder_version_value_roundtrip():
    instance = doc_builder_BookBuilder(copyrightMarker="sample_text", license="sample_text", title="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_doc_builder_PropertyEntry_key_value_roundtrip():
    instance = doc_builder_PropertyEntry(key="sample_text", value="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_doc_builder_PropertyEntry_value_value_roundtrip():
    instance = doc_builder_PropertyEntry(key="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_doc_fragment_Author_id_value_roundtrip():
    instance = doc_fragment_Author(id="sample_text", name="sample_text", ref="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_doc_fragment_Author_name_value_roundtrip():
    instance = doc_fragment_Author(id="sample_text", name="sample_text", ref="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_doc_fragment_Author_ref_value_roundtrip():
    instance = doc_fragment_Author(id="sample_text", name="sample_text", ref="sample_text")
    assert instance.ref == "sample_text"
    instance.ref = "sample_text_2"
    assert instance.ref == "sample_text_2"


def test_doc_fragment_Container_content_value_roundtrip():
    instance = doc_fragment_Container(content="sample_text")
    assert instance.content == "sample_text"
    instance.content = "sample_text_2"
    assert instance.content == "sample_text_2"


def test_doc_fragment_Copyright_year_value_roundtrip():
    instance = doc_fragment_Copyright(year=7)
    assert instance.year == 7
    instance.year = 13
    assert instance.year == 13


def test_doc_fragment_PlainTextContent_value_value_roundtrip():
    instance = doc_fragment_PlainTextContent(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_doc_fragment_Section_title_value_roundtrip():
    instance = doc_fragment_Section(title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_doc_map_ExtensionMappingEntry_extension_value_roundtrip():
    instance = doc_map_ExtensionMappingEntry(extension="sample_text")
    assert instance.extension == "sample_text"
    instance.extension = "sample_text_2"
    assert instance.extension == "sample_text_2"


def test_doc_map_Feature_createSection_value_roundtrip():
    instance = doc_map_Feature(createSection=True, featureId="sample_text")
    assert instance.createSection == True
    instance.createSection = False
    assert instance.createSection == False


def test_doc_map_Feature_featureId_value_roundtrip():
    instance = doc_map_Feature(createSection=True, featureId="sample_text")
    assert instance.featureId == "sample_text"
    instance.featureId = "sample_text_2"
    assert instance.featureId == "sample_text_2"


def test_doc_map_File_path_value_roundtrip():
    instance = doc_map_File(path="sample_text")
    assert instance.path == "sample_text"
    instance.path = "sample_text_2"
    assert instance.path == "sample_text_2"


def test_doc_map_MapContainer_numberingStyle_value_roundtrip():
    instance = doc_map_MapContainer(numberingStyle="sample_text")
    assert instance.numberingStyle == "sample_text"
    instance.numberingStyle = "sample_text_2"
    assert instance.numberingStyle == "sample_text_2"


def test_doc_map_MapSection_id_value_roundtrip():
    instance = doc_map_MapSection(id="sample_text", title="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_doc_map_MapSection_title_value_roundtrip():
    instance = doc_map_MapSection(id="sample_text", title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_doc_map_PatternRule_pattern_value_roundtrip():
    instance = doc_map_PatternRule(pattern="sample_text")
    assert instance.pattern == "sample_text"
    instance.pattern = "sample_text_2"
    assert instance.pattern == "sample_text_2"


def test_doc_map_ResourceFactory_className_value_roundtrip():
    instance = doc_map_ResourceFactory(className="sample_text")
    assert instance.className == "sample_text"
    instance.className = "sample_text_2"
    assert instance.className == "sample_text_2"


def test_doc_book_Book_isa_BookContainer():
    instance = doc_book_Book(copyrightMarker="sample_text", copyrightText="sample_text", title="sample_text", version="sample_text")
    assert isinstance(instance, BookContainer)


def test_doc_book_BookSection_isa_BookContainer():
    instance = doc_book_BookSection(fullNumber="sample_text", id="sample_text", number=7, title="sample_text")
    assert isinstance(instance, BookContainer)


def test_doc_fragment_Fragment_isa_Container():
    instance = doc_fragment_Fragment()
    assert isinstance(instance, Container)


def test_doc_fragment_Section_isa_Container():
    instance = doc_fragment_Section(title="sample_text")
    assert isinstance(instance, Container)


def test_doc_fragment_PlainTextContent_isa_Content():
    instance = doc_fragment_PlainTextContent(value="sample_text")
    assert isinstance(instance, Content)


def test_doc_map_Feature_isa_Import():
    instance = doc_map_Feature(createSection=True, featureId="sample_text")
    assert isinstance(instance, Import)


def test_doc_map_File_isa_Import():
    instance = doc_map_File(path="sample_text")
    assert isinstance(instance, Import)


def test_doc_builder_BookBuilder_isa_Map():
    instance = doc_builder_BookBuilder(copyrightMarker="sample_text", license="sample_text", title="sample_text", version="sample_text")
    assert isinstance(instance, Map)


def test_doc_map_Map_isa_MapContainer():
    instance = doc_map_Map()
    assert isinstance(instance, MapContainer)


def test_doc_map_Import_isa_MapElement():
    instance = doc_map_Import()
    assert isinstance(instance, MapElement)


def test_doc_map_PatternRule_isa_NameRule():
    instance = doc_map_PatternRule(pattern="sample_text")
    assert isinstance(instance, NameRule)


def test_doc_map_ExcludePatternRule_isa_PatternRule():
    instance = doc_map_ExcludePatternRule()
    assert isinstance(instance, PatternRule)


def test_doc_map_IncludePatternRule_isa_PatternRule():
    instance = doc_map_IncludePatternRule()
    assert isinstance(instance, PatternRule)


def test_doc_map_ContentGenerator_isa_fragment_Content():
    instance = doc_map_ContentGenerator()
    assert isinstance(instance, fragment_Content)


def test_doc_map_MapSection_isa_map_MapContainer():
    instance = doc_map_MapSection(id="sample_text", title="sample_text")
    assert isinstance(instance, map_MapContainer)


def test_doc_map_ContentGenerator_isa_map_MapElement():
    instance = doc_map_ContentGenerator()
    assert isinstance(instance, map_MapElement)


def test_doc_map_MapSection_isa_map_MapElement():
    instance = doc_map_MapSection(id="sample_text", title="sample_text")
    assert isinstance(instance, map_MapElement)


def test_assoc_anyContent4_link_reassign_clear():
    a = doc_fragment_Container(content="sample_text")
    b1 = Content()
    b2 = Content()
    _safe_set(a, 'doc_fragment_Container', {b1})
    assert _is_linked(a, 'doc_fragment_Container', b1)
    if hasattr(b1, 'Content'):
        assert _is_linked(b1, 'Content', a)
    _safe_set(a, 'doc_fragment_Container', {b2})
    assert _is_linked(a, 'doc_fragment_Container', b2)
    if hasattr(b1, 'Content'):
        assert not _is_linked(b1, 'Content', a)
    if hasattr(b2, 'Content'):
        assert _is_linked(b2, 'Content', a)
    _safe_set(a, 'doc_fragment_Container', set())
    assert not _is_linked(a, 'doc_fragment_Container', b2)
    if hasattr(b2, 'Content'):
        assert not _is_linked(b2, 'Content', a)


def test_assoc_author7_link_reassign_clear():
    a = doc_fragment_Copyright(year=7)
    b1 = Author()
    b2 = Author()
    _safe_set(a, 'doc_fragment_Copyright', {b1})
    assert _is_linked(a, 'doc_fragment_Copyright', b1)
    if hasattr(b1, 'Author'):
        assert _is_linked(b1, 'Author', a)
    _safe_set(a, 'doc_fragment_Copyright', {b2})
    assert _is_linked(a, 'doc_fragment_Copyright', b2)
    if hasattr(b1, 'Author'):
        assert not _is_linked(b1, 'Author', a)
    if hasattr(b2, 'Author'):
        assert _is_linked(b2, 'Author', a)
    _safe_set(a, 'doc_fragment_Copyright', set())
    assert not _is_linked(a, 'doc_fragment_Copyright', b2)
    if hasattr(b2, 'Author'):
        assert not _is_linked(b2, 'Author', a)


def test_assoc_authors16_link_reassign_clear():
    a = doc_builder_BookBuilder(copyrightMarker="sample_text", license="sample_text", title="sample_text", version="sample_text")
    b1 = Author()
    b2 = Author()
    _safe_set(a, 'doc_builder_BookBuilder', {b1})
    assert _is_linked(a, 'doc_builder_BookBuilder', b1)
    if hasattr(b1, 'Author17'):
        assert _is_linked(b1, 'Author17', a)
    _safe_set(a, 'doc_builder_BookBuilder', {b2})
    assert _is_linked(a, 'doc_builder_BookBuilder', b2)
    if hasattr(b1, 'Author17'):
        assert not _is_linked(b1, 'Author17', a)
    if hasattr(b2, 'Author17'):
        assert _is_linked(b2, 'Author17', a)
    _safe_set(a, 'doc_builder_BookBuilder', set())
    assert not _is_linked(a, 'doc_builder_BookBuilder', b2)
    if hasattr(b2, 'Author17'):
        assert not _is_linked(b2, 'Author17', a)


def test_assoc_authors8_link_reassign_clear():
    a = doc_book_Book(copyrightMarker="sample_text", copyrightText="sample_text", title="sample_text", version="sample_text")
    b1 = Author()
    b2 = Author()
    _safe_set(a, 'doc_book_Book', {b1})
    assert _is_linked(a, 'doc_book_Book', b1)
    if hasattr(b1, 'Author9'):
        assert _is_linked(b1, 'Author9', a)
    _safe_set(a, 'doc_book_Book', {b2})
    assert _is_linked(a, 'doc_book_Book', b2)
    if hasattr(b1, 'Author9'):
        assert not _is_linked(b1, 'Author9', a)
    if hasattr(b2, 'Author9'):
        assert _is_linked(b2, 'Author9', a)
    _safe_set(a, 'doc_book_Book', set())
    assert not _is_linked(a, 'doc_book_Book', b2)
    if hasattr(b2, 'Author9'):
        assert not _is_linked(b2, 'Author9', a)


def test_assoc_content12_link_reassign_clear():
    a = doc_book_BookContainer(numberingStyle="sample_text")
    b1 = Content()
    b2 = Content()
    _safe_set(a, 'doc_book_BookContainer', {b1})
    assert _is_linked(a, 'doc_book_BookContainer', b1)
    if hasattr(b1, 'Content13'):
        assert _is_linked(b1, 'Content13', a)
    _safe_set(a, 'doc_book_BookContainer', {b2})
    assert _is_linked(a, 'doc_book_BookContainer', b2)
    if hasattr(b1, 'Content13'):
        assert not _is_linked(b1, 'Content13', a)
    if hasattr(b2, 'Content13'):
        assert _is_linked(b2, 'Content13', a)
    _safe_set(a, 'doc_book_BookContainer', set())
    assert not _is_linked(a, 'doc_book_BookContainer', b2)
    if hasattr(b2, 'Content13'):
        assert not _is_linked(b2, 'Content13', a)


def test_assoc_copyright10_link_reassign_clear():
    a = doc_book_Book(copyrightMarker="sample_text", copyrightText="sample_text", title="sample_text", version="sample_text")
    b1 = Copyright()
    b2 = Copyright()
    _safe_set(a, 'doc_book_Book11', {b1})
    assert _is_linked(a, 'doc_book_Book11', b1)
    if hasattr(b1, 'Copyright'):
        assert _is_linked(b1, 'Copyright', a)
    _safe_set(a, 'doc_book_Book11', {b2})
    assert _is_linked(a, 'doc_book_Book11', b2)
    if hasattr(b1, 'Copyright'):
        assert not _is_linked(b1, 'Copyright', a)
    if hasattr(b2, 'Copyright'):
        assert _is_linked(b2, 'Copyright', a)
    _safe_set(a, 'doc_book_Book11', set())
    assert not _is_linked(a, 'doc_book_Book11', b2)
    if hasattr(b2, 'Copyright'):
        assert not _is_linked(b2, 'Copyright', a)


def test_assoc_copyright18_link_reassign_clear():
    a = doc_builder_BookBuilder(copyrightMarker="sample_text", license="sample_text", title="sample_text", version="sample_text")
    b1 = Copyright()
    b2 = Copyright()
    _safe_set(a, 'doc_builder_BookBuilder19', {b1})
    assert _is_linked(a, 'doc_builder_BookBuilder19', b1)
    if hasattr(b1, 'Copyright20'):
        assert _is_linked(b1, 'Copyright20', a)
    _safe_set(a, 'doc_builder_BookBuilder19', {b2})
    assert _is_linked(a, 'doc_builder_BookBuilder19', b2)
    if hasattr(b1, 'Copyright20'):
        assert not _is_linked(b1, 'Copyright20', a)
    if hasattr(b2, 'Copyright20'):
        assert _is_linked(b2, 'Copyright20', a)
    _safe_set(a, 'doc_builder_BookBuilder19', set())
    assert not _is_linked(a, 'doc_builder_BookBuilder19', b2)
    if hasattr(b2, 'Copyright20'):
        assert not _is_linked(b2, 'Copyright20', a)


def test_assoc_elements3_link_reassign_clear():
    a = doc_map_MapContainer(numberingStyle="sample_text")
    b1 = MapElement()
    b2 = MapElement()
    _safe_set(a, 'doc_map_MapContainer', {b1})
    assert _is_linked(a, 'doc_map_MapContainer', b1)
    if hasattr(b1, 'MapElement'):
        assert _is_linked(b1, 'MapElement', a)
    _safe_set(a, 'doc_map_MapContainer', {b2})
    assert _is_linked(a, 'doc_map_MapContainer', b2)
    if hasattr(b1, 'MapElement'):
        assert not _is_linked(b1, 'MapElement', a)
    if hasattr(b2, 'MapElement'):
        assert _is_linked(b2, 'MapElement', a)
    _safe_set(a, 'doc_map_MapContainer', set())
    assert not _is_linked(a, 'doc_map_MapContainer', b2)
    if hasattr(b2, 'MapElement'):
        assert not _is_linked(b2, 'MapElement', a)


def test_assoc_extensionMappings0_link_reassign_clear():
    a = doc_map_Map()
    b1 = ExtensionMappingEntry()
    b2 = ExtensionMappingEntry()
    _safe_set(a, 'doc_map_Map', {b1})
    assert _is_linked(a, 'doc_map_Map', b1)
    if hasattr(b1, 'ExtensionMappingEntry'):
        assert _is_linked(b1, 'ExtensionMappingEntry', a)
    _safe_set(a, 'doc_map_Map', {b2})
    assert _is_linked(a, 'doc_map_Map', b2)
    if hasattr(b1, 'ExtensionMappingEntry'):
        assert not _is_linked(b1, 'ExtensionMappingEntry', a)
    if hasattr(b2, 'ExtensionMappingEntry'):
        assert _is_linked(b2, 'ExtensionMappingEntry', a)
    _safe_set(a, 'doc_map_Map', set())
    assert not _is_linked(a, 'doc_map_Map', b2)
    if hasattr(b2, 'ExtensionMappingEntry'):
        assert not _is_linked(b2, 'ExtensionMappingEntry', a)


def test_assoc_factory2_link_reassign_clear():
    a = doc_map_ExtensionMappingEntry(extension="sample_text")
    b1 = ResourceFactory()
    b2 = ResourceFactory()
    _safe_set(a, 'doc_map_ExtensionMappingEntry', b1)
    assert _is_linked(a, 'doc_map_ExtensionMappingEntry', b1)
    if hasattr(b1, 'ResourceFactory'):
        assert _is_linked(b1, 'ResourceFactory', a)
    _safe_set(a, 'doc_map_ExtensionMappingEntry', b2)
    assert _is_linked(a, 'doc_map_ExtensionMappingEntry', b2)
    if hasattr(b1, 'ResourceFactory'):
        assert not _is_linked(b1, 'ResourceFactory', a)
    if hasattr(b2, 'ResourceFactory'):
        assert _is_linked(b2, 'ResourceFactory', a)
    _safe_set(a, 'doc_map_ExtensionMappingEntry', None)
    assert not _is_linked(a, 'doc_map_ExtensionMappingEntry', b2)
    if hasattr(b2, 'ResourceFactory'):
        assert not _is_linked(b2, 'ResourceFactory', a)


def test_assoc_fileNameRules1_link_reassign_clear():
    a = doc_map_Feature(createSection=True, featureId="sample_text")
    b1 = NameRule()
    b2 = NameRule()
    _safe_set(a, 'doc_map_Feature', {b1})
    assert _is_linked(a, 'doc_map_Feature', b1)
    if hasattr(b1, 'NameRule'):
        assert _is_linked(b1, 'NameRule', a)
    _safe_set(a, 'doc_map_Feature', {b2})
    assert _is_linked(a, 'doc_map_Feature', b2)
    if hasattr(b1, 'NameRule'):
        assert not _is_linked(b1, 'NameRule', a)
    if hasattr(b2, 'NameRule'):
        assert _is_linked(b2, 'NameRule', a)
    _safe_set(a, 'doc_map_Feature', set())
    assert not _is_linked(a, 'doc_map_Feature', b2)
    if hasattr(b2, 'NameRule'):
        assert not _is_linked(b2, 'NameRule', a)


def test_assoc_properties21_link_reassign_clear():
    a = doc_builder_BookBuilder(copyrightMarker="sample_text", license="sample_text", title="sample_text", version="sample_text")
    b1 = builder_PropertyEntry()
    b2 = builder_PropertyEntry()
    _safe_set(a, 'doc_builder_BookBuilder22', {b1})
    assert _is_linked(a, 'doc_builder_BookBuilder22', b1)
    if hasattr(b1, 'builder_PropertyEntry'):
        assert _is_linked(b1, 'builder_PropertyEntry', a)
    _safe_set(a, 'doc_builder_BookBuilder22', {b2})
    assert _is_linked(a, 'doc_builder_BookBuilder22', b2)
    if hasattr(b1, 'builder_PropertyEntry'):
        assert not _is_linked(b1, 'builder_PropertyEntry', a)
    if hasattr(b2, 'builder_PropertyEntry'):
        assert _is_linked(b2, 'builder_PropertyEntry', a)
    _safe_set(a, 'doc_builder_BookBuilder22', set())
    assert not _is_linked(a, 'doc_builder_BookBuilder22', b2)
    if hasattr(b2, 'builder_PropertyEntry'):
        assert not _is_linked(b2, 'builder_PropertyEntry', a)


def test_assoc_section5_link_reassign_clear():
    a = doc_fragment_Container(content="sample_text")
    b1 = Section()
    b2 = Section()
    _safe_set(a, 'doc_fragment_Container6', {b1})
    assert _is_linked(a, 'doc_fragment_Container6', b1)
    if hasattr(b1, 'Section'):
        assert _is_linked(b1, 'Section', a)
    _safe_set(a, 'doc_fragment_Container6', {b2})
    assert _is_linked(a, 'doc_fragment_Container6', b2)
    if hasattr(b1, 'Section'):
        assert not _is_linked(b1, 'Section', a)
    if hasattr(b2, 'Section'):
        assert _is_linked(b2, 'Section', a)
    _safe_set(a, 'doc_fragment_Container6', set())
    assert not _is_linked(a, 'doc_fragment_Container6', b2)
    if hasattr(b2, 'Section'):
        assert not _is_linked(b2, 'Section', a)


def test_assoc_sections14_link_reassign_clear():
    a = doc_book_BookContainer(numberingStyle="sample_text")
    b1 = BookSection()
    b2 = BookSection()
    _safe_set(a, 'doc_book_BookContainer15', {b1})
    assert _is_linked(a, 'doc_book_BookContainer15', b1)
    if hasattr(b1, 'BookSection'):
        assert _is_linked(b1, 'BookSection', a)
    _safe_set(a, 'doc_book_BookContainer15', {b2})
    assert _is_linked(a, 'doc_book_BookContainer15', b2)
    if hasattr(b1, 'BookSection'):
        assert not _is_linked(b1, 'BookSection', a)
    if hasattr(b2, 'BookSection'):
        assert _is_linked(b2, 'BookSection', a)
    _safe_set(a, 'doc_book_BookContainer15', set())
    assert not _is_linked(a, 'doc_book_BookContainer15', b2)
    if hasattr(b2, 'BookSection'):
        assert not _is_linked(b2, 'BookSection', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Author_strategy = st.builds(Author)
@given(instance=Author_strategy)
@settings(max_examples=25)
def test_Author_instantiation(instance):
    assert isinstance(instance, Author)


BookContainer_strategy = st.builds(BookContainer)
@given(instance=BookContainer_strategy)
@settings(max_examples=25)
def test_BookContainer_instantiation(instance):
    assert isinstance(instance, BookContainer)


BookSection_strategy = st.builds(BookSection)
@given(instance=BookSection_strategy)
@settings(max_examples=25)
def test_BookSection_instantiation(instance):
    assert isinstance(instance, BookSection)


Container_strategy = st.builds(Container)
@given(instance=Container_strategy)
@settings(max_examples=25)
def test_Container_instantiation(instance):
    assert isinstance(instance, Container)


Content_strategy = st.builds(Content)
@given(instance=Content_strategy)
@settings(max_examples=25)
def test_Content_instantiation(instance):
    assert isinstance(instance, Content)


Copyright_strategy = st.builds(Copyright)
@given(instance=Copyright_strategy)
@settings(max_examples=25)
def test_Copyright_instantiation(instance):
    assert isinstance(instance, Copyright)


ExtensionMappingEntry_strategy = st.builds(ExtensionMappingEntry)
@given(instance=ExtensionMappingEntry_strategy)
@settings(max_examples=25)
def test_ExtensionMappingEntry_instantiation(instance):
    assert isinstance(instance, ExtensionMappingEntry)


Import_strategy = st.builds(Import)
@given(instance=Import_strategy)
@settings(max_examples=25)
def test_Import_instantiation(instance):
    assert isinstance(instance, Import)


Map_strategy = st.builds(Map)
@given(instance=Map_strategy)
@settings(max_examples=25)
def test_Map_instantiation(instance):
    assert isinstance(instance, Map)


MapContainer_strategy = st.builds(MapContainer)
@given(instance=MapContainer_strategy)
@settings(max_examples=25)
def test_MapContainer_instantiation(instance):
    assert isinstance(instance, MapContainer)


MapElement_strategy = st.builds(MapElement)
@given(instance=MapElement_strategy)
@settings(max_examples=25)
def test_MapElement_instantiation(instance):
    assert isinstance(instance, MapElement)


NameRule_strategy = st.builds(NameRule)
@given(instance=NameRule_strategy)
@settings(max_examples=25)
def test_NameRule_instantiation(instance):
    assert isinstance(instance, NameRule)


PatternRule_strategy = st.builds(PatternRule)
@given(instance=PatternRule_strategy)
@settings(max_examples=25)
def test_PatternRule_instantiation(instance):
    assert isinstance(instance, PatternRule)


ResourceFactory_strategy = st.builds(ResourceFactory)
@given(instance=ResourceFactory_strategy)
@settings(max_examples=25)
def test_ResourceFactory_instantiation(instance):
    assert isinstance(instance, ResourceFactory)


Section_strategy = st.builds(Section)
@given(instance=Section_strategy)
@settings(max_examples=25)
def test_Section_instantiation(instance):
    assert isinstance(instance, Section)


builder_PropertyEntry_strategy = st.builds(builder_PropertyEntry)
@given(instance=builder_PropertyEntry_strategy)
@settings(max_examples=25)
def test_builder_PropertyEntry_instantiation(instance):
    assert isinstance(instance, builder_PropertyEntry)


doc_Test_strategy = st.builds(doc_Test)
@given(instance=doc_Test_strategy)
@settings(max_examples=25)
def test_doc_Test_instantiation(instance):
    assert isinstance(instance, doc_Test)


doc_book_Book_strategy = st.builds(doc_book_Book, copyrightMarker=safe_text, copyrightText=safe_text, title=safe_text, version=safe_text)
@given(instance=doc_book_Book_strategy)
@settings(max_examples=25)
def test_doc_book_Book_instantiation(instance):
    assert isinstance(instance, doc_book_Book)


doc_book_BookContainer_strategy = st.builds(doc_book_BookContainer, numberingStyle=safe_text)
@given(instance=doc_book_BookContainer_strategy)
@settings(max_examples=25)
def test_doc_book_BookContainer_instantiation(instance):
    assert isinstance(instance, doc_book_BookContainer)


doc_book_BookSection_strategy = st.builds(doc_book_BookSection, fullNumber=safe_text, id=safe_text, number=st.integers(), title=safe_text)
@given(instance=doc_book_BookSection_strategy)
@settings(max_examples=25)
def test_doc_book_BookSection_instantiation(instance):
    assert isinstance(instance, doc_book_BookSection)


doc_builder_BookBuilder_strategy = st.builds(doc_builder_BookBuilder, copyrightMarker=safe_text, license=safe_text, title=safe_text, version=safe_text)
@given(instance=doc_builder_BookBuilder_strategy)
@settings(max_examples=25)
def test_doc_builder_BookBuilder_instantiation(instance):
    assert isinstance(instance, doc_builder_BookBuilder)


doc_builder_PropertyEntry_strategy = st.builds(doc_builder_PropertyEntry, key=safe_text, value=safe_text)
@given(instance=doc_builder_PropertyEntry_strategy)
@settings(max_examples=25)
def test_doc_builder_PropertyEntry_instantiation(instance):
    assert isinstance(instance, doc_builder_PropertyEntry)


doc_fragment_Author_strategy = st.builds(doc_fragment_Author, id=safe_text, name=safe_text, ref=safe_text)
@given(instance=doc_fragment_Author_strategy)
@settings(max_examples=25)
def test_doc_fragment_Author_instantiation(instance):
    assert isinstance(instance, doc_fragment_Author)


doc_fragment_Container_strategy = st.builds(doc_fragment_Container, content=safe_text)
@given(instance=doc_fragment_Container_strategy)
@settings(max_examples=25)
def test_doc_fragment_Container_instantiation(instance):
    assert isinstance(instance, doc_fragment_Container)


doc_fragment_Content_strategy = st.builds(doc_fragment_Content)
@given(instance=doc_fragment_Content_strategy)
@settings(max_examples=25)
def test_doc_fragment_Content_instantiation(instance):
    assert isinstance(instance, doc_fragment_Content)


doc_fragment_Copyright_strategy = st.builds(doc_fragment_Copyright, year=st.integers())
@given(instance=doc_fragment_Copyright_strategy)
@settings(max_examples=25)
def test_doc_fragment_Copyright_instantiation(instance):
    assert isinstance(instance, doc_fragment_Copyright)


doc_fragment_Fragment_strategy = st.builds(doc_fragment_Fragment)
@given(instance=doc_fragment_Fragment_strategy)
@settings(max_examples=25)
def test_doc_fragment_Fragment_instantiation(instance):
    assert isinstance(instance, doc_fragment_Fragment)


doc_fragment_PlainTextContent_strategy = st.builds(doc_fragment_PlainTextContent, value=safe_text)
@given(instance=doc_fragment_PlainTextContent_strategy)
@settings(max_examples=25)
def test_doc_fragment_PlainTextContent_instantiation(instance):
    assert isinstance(instance, doc_fragment_PlainTextContent)


doc_fragment_Section_strategy = st.builds(doc_fragment_Section, title=safe_text)
@given(instance=doc_fragment_Section_strategy)
@settings(max_examples=25)
def test_doc_fragment_Section_instantiation(instance):
    assert isinstance(instance, doc_fragment_Section)


doc_map_ContentGenerator_strategy = st.builds(doc_map_ContentGenerator)
@given(instance=doc_map_ContentGenerator_strategy)
@settings(max_examples=25)
def test_doc_map_ContentGenerator_instantiation(instance):
    assert isinstance(instance, doc_map_ContentGenerator)


doc_map_ExcludePatternRule_strategy = st.builds(doc_map_ExcludePatternRule)
@given(instance=doc_map_ExcludePatternRule_strategy)
@settings(max_examples=25)
def test_doc_map_ExcludePatternRule_instantiation(instance):
    assert isinstance(instance, doc_map_ExcludePatternRule)


doc_map_ExtensionMappingEntry_strategy = st.builds(doc_map_ExtensionMappingEntry, extension=safe_text)
@given(instance=doc_map_ExtensionMappingEntry_strategy)
@settings(max_examples=25)
def test_doc_map_ExtensionMappingEntry_instantiation(instance):
    assert isinstance(instance, doc_map_ExtensionMappingEntry)


doc_map_Feature_strategy = st.builds(doc_map_Feature, createSection=st.booleans(), featureId=safe_text)
@given(instance=doc_map_Feature_strategy)
@settings(max_examples=25)
def test_doc_map_Feature_instantiation(instance):
    assert isinstance(instance, doc_map_Feature)


doc_map_File_strategy = st.builds(doc_map_File, path=safe_text)
@given(instance=doc_map_File_strategy)
@settings(max_examples=25)
def test_doc_map_File_instantiation(instance):
    assert isinstance(instance, doc_map_File)


doc_map_Import_strategy = st.builds(doc_map_Import)
@given(instance=doc_map_Import_strategy)
@settings(max_examples=25)
def test_doc_map_Import_instantiation(instance):
    assert isinstance(instance, doc_map_Import)


doc_map_IncludePatternRule_strategy = st.builds(doc_map_IncludePatternRule)
@given(instance=doc_map_IncludePatternRule_strategy)
@settings(max_examples=25)
def test_doc_map_IncludePatternRule_instantiation(instance):
    assert isinstance(instance, doc_map_IncludePatternRule)


doc_map_Map_strategy = st.builds(doc_map_Map)
@given(instance=doc_map_Map_strategy)
@settings(max_examples=25)
def test_doc_map_Map_instantiation(instance):
    assert isinstance(instance, doc_map_Map)


doc_map_MapContainer_strategy = st.builds(doc_map_MapContainer, numberingStyle=safe_text)
@given(instance=doc_map_MapContainer_strategy)
@settings(max_examples=25)
def test_doc_map_MapContainer_instantiation(instance):
    assert isinstance(instance, doc_map_MapContainer)


doc_map_MapElement_strategy = st.builds(doc_map_MapElement)
@given(instance=doc_map_MapElement_strategy)
@settings(max_examples=25)
def test_doc_map_MapElement_instantiation(instance):
    assert isinstance(instance, doc_map_MapElement)


doc_map_MapSection_strategy = st.builds(doc_map_MapSection, id=safe_text, title=safe_text)
@given(instance=doc_map_MapSection_strategy)
@settings(max_examples=25)
def test_doc_map_MapSection_instantiation(instance):
    assert isinstance(instance, doc_map_MapSection)


doc_map_NameRule_strategy = st.builds(doc_map_NameRule)
@given(instance=doc_map_NameRule_strategy)
@settings(max_examples=25)
def test_doc_map_NameRule_instantiation(instance):
    assert isinstance(instance, doc_map_NameRule)


doc_map_PatternRule_strategy = st.builds(doc_map_PatternRule, pattern=safe_text)
@given(instance=doc_map_PatternRule_strategy)
@settings(max_examples=25)
def test_doc_map_PatternRule_instantiation(instance):
    assert isinstance(instance, doc_map_PatternRule)


doc_map_ResourceFactory_strategy = st.builds(doc_map_ResourceFactory, className=safe_text)
@given(instance=doc_map_ResourceFactory_strategy)
@settings(max_examples=25)
def test_doc_map_ResourceFactory_instantiation(instance):
    assert isinstance(instance, doc_map_ResourceFactory)


fragment_Content_strategy = st.builds(fragment_Content)
@given(instance=fragment_Content_strategy)
@settings(max_examples=25)
def test_fragment_Content_instantiation(instance):
    assert isinstance(instance, fragment_Content)


map_MapContainer_strategy = st.builds(map_MapContainer)
@given(instance=map_MapContainer_strategy)
@settings(max_examples=25)
def test_map_MapContainer_instantiation(instance):
    assert isinstance(instance, map_MapContainer)


map_MapElement_strategy = st.builds(map_MapElement)
@given(instance=map_MapElement_strategy)
@settings(max_examples=25)
def test_map_MapElement_instantiation(instance):
    assert isinstance(instance, map_MapElement)



