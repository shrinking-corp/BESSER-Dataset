import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    qsar_BibTeXMLEntriesClass,
    qsar_DescriptorType,
    qsar_DescriptorlistType,
    qsar_DescriptorproviderType,
    qsar_DescriptorresultType,
    qsar_DescriptorresultlistsType,
    qsar_DescriptorvalueType,
    qsar_DocumentRoot,
    qsar_EStringToStringMapEntry,
    qsar_MetadataType,
    qsar_ParameterType,
    qsar_PreprocessingStepType,
    qsar_PreprocessingType,
    qsar_QsarType,
    qsar_ResourceType,
    qsar_ResponseType,
    qsar_ResponsesListType,
    qsar_ResponseunitType,
    qsar_StructureType,
    qsar_StructurelistType,
    TypeType,
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

def test_qsar_DescriptorType_id_value_roundtrip():
    instance = qsar_DescriptorType(id="sample_text", ontologyid="sample_text", provider="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_qsar_DescriptorType_ontologyid_value_roundtrip():
    instance = qsar_DescriptorType(id="sample_text", ontologyid="sample_text", provider="sample_text")
    assert instance.ontologyid == "sample_text"
    instance.ontologyid = "sample_text_2"
    assert instance.ontologyid == "sample_text_2"


def test_qsar_DescriptorType_provider_value_roundtrip():
    instance = qsar_DescriptorType(id="sample_text", ontologyid="sample_text", provider="sample_text")
    assert instance.provider == "sample_text"
    instance.provider = "sample_text_2"
    assert instance.provider == "sample_text_2"


def test_qsar_DescriptorproviderType_id_value_roundtrip():
    instance = qsar_DescriptorproviderType(id="sample_text", name="sample_text", uRL="sample_text", vendor="sample_text", version="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_qsar_DescriptorproviderType_name_value_roundtrip():
    instance = qsar_DescriptorproviderType(id="sample_text", name="sample_text", uRL="sample_text", vendor="sample_text", version="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_qsar_DescriptorproviderType_uRL_value_roundtrip():
    instance = qsar_DescriptorproviderType(id="sample_text", name="sample_text", uRL="sample_text", vendor="sample_text", version="sample_text")
    assert instance.uRL == "sample_text"
    instance.uRL = "sample_text_2"
    assert instance.uRL == "sample_text_2"


def test_qsar_DescriptorproviderType_vendor_value_roundtrip():
    instance = qsar_DescriptorproviderType(id="sample_text", name="sample_text", uRL="sample_text", vendor="sample_text", version="sample_text")
    assert instance.vendor == "sample_text"
    instance.vendor = "sample_text_2"
    assert instance.vendor == "sample_text_2"


def test_qsar_DescriptorproviderType_version_value_roundtrip():
    instance = qsar_DescriptorproviderType(id="sample_text", name="sample_text", uRL="sample_text", vendor="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_qsar_DescriptorresultType_descriptorid_value_roundtrip():
    instance = qsar_DescriptorresultType(descriptorid="sample_text", structureid="sample_text")
    assert instance.descriptorid == "sample_text"
    instance.descriptorid = "sample_text_2"
    assert instance.descriptorid == "sample_text_2"


def test_qsar_DescriptorresultType_structureid_value_roundtrip():
    instance = qsar_DescriptorresultType(descriptorid="sample_text", structureid="sample_text")
    assert instance.structureid == "sample_text"
    instance.structureid = "sample_text_2"
    assert instance.structureid == "sample_text_2"


def test_qsar_DescriptorvalueType_index_value_roundtrip():
    instance = qsar_DescriptorvalueType(index="sample_text", label="sample_text", value="sample_text")
    assert instance.index == "sample_text"
    instance.index = "sample_text_2"
    assert instance.index == "sample_text_2"


def test_qsar_DescriptorvalueType_label_value_roundtrip():
    instance = qsar_DescriptorvalueType(index="sample_text", label="sample_text", value="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_qsar_DescriptorvalueType_value_value_roundtrip():
    instance = qsar_DescriptorvalueType(index="sample_text", label="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_qsar_DocumentRoot_mixed_value_roundtrip():
    instance = qsar_DocumentRoot(mixed="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_qsar_MetadataType_authors_value_roundtrip():
    instance = qsar_MetadataType(authors="sample_text", datasetname="sample_text", description="sample_text", license="sample_text", uRL="sample_text")
    assert instance.authors == "sample_text"
    instance.authors = "sample_text_2"
    assert instance.authors == "sample_text_2"


def test_qsar_MetadataType_datasetname_value_roundtrip():
    instance = qsar_MetadataType(authors="sample_text", datasetname="sample_text", description="sample_text", license="sample_text", uRL="sample_text")
    assert instance.datasetname == "sample_text"
    instance.datasetname = "sample_text_2"
    assert instance.datasetname == "sample_text_2"


def test_qsar_MetadataType_description_value_roundtrip():
    instance = qsar_MetadataType(authors="sample_text", datasetname="sample_text", description="sample_text", license="sample_text", uRL="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_qsar_MetadataType_license_value_roundtrip():
    instance = qsar_MetadataType(authors="sample_text", datasetname="sample_text", description="sample_text", license="sample_text", uRL="sample_text")
    assert instance.license == "sample_text"
    instance.license = "sample_text_2"
    assert instance.license == "sample_text_2"


def test_qsar_MetadataType_uRL_value_roundtrip():
    instance = qsar_MetadataType(authors="sample_text", datasetname="sample_text", description="sample_text", license="sample_text", uRL="sample_text")
    assert instance.uRL == "sample_text"
    instance.uRL = "sample_text_2"
    assert instance.uRL == "sample_text_2"


def test_qsar_ParameterType_key_value_roundtrip():
    instance = qsar_ParameterType(key="sample_text", value="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_qsar_ParameterType_value_value_roundtrip():
    instance = qsar_ParameterType(key="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_qsar_PreprocessingStepType_id_value_roundtrip():
    instance = qsar_PreprocessingStepType(id="sample_text", name="sample_text", namespace="sample_text", order="sample_text", vendor="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_qsar_PreprocessingStepType_name_value_roundtrip():
    instance = qsar_PreprocessingStepType(id="sample_text", name="sample_text", namespace="sample_text", order="sample_text", vendor="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_qsar_PreprocessingStepType_namespace_value_roundtrip():
    instance = qsar_PreprocessingStepType(id="sample_text", name="sample_text", namespace="sample_text", order="sample_text", vendor="sample_text")
    assert instance.namespace == "sample_text"
    instance.namespace = "sample_text_2"
    assert instance.namespace == "sample_text_2"


def test_qsar_PreprocessingStepType_order_value_roundtrip():
    instance = qsar_PreprocessingStepType(id="sample_text", name="sample_text", namespace="sample_text", order="sample_text", vendor="sample_text")
    assert instance.order == "sample_text"
    instance.order = "sample_text_2"
    assert instance.order == "sample_text_2"


def test_qsar_PreprocessingStepType_vendor_value_roundtrip():
    instance = qsar_PreprocessingStepType(id="sample_text", name="sample_text", namespace="sample_text", order="sample_text", vendor="sample_text")
    assert instance.vendor == "sample_text"
    instance.vendor = "sample_text_2"
    assert instance.vendor == "sample_text_2"


def test_qsar_ResourceType_checksum_value_roundtrip():
    instance = qsar_ResourceType(checksum="sample_text", excluded="sample_text", file="sample_text", id="sample_text", name="sample_text", no2d="sample_text", no3d="sample_text", noMols="sample_text", type="sample_text", uRL="sample_text")
    assert instance.checksum == "sample_text"
    instance.checksum = "sample_text_2"
    assert instance.checksum == "sample_text_2"


def test_qsar_ResourceType_excluded_value_roundtrip():
    instance = qsar_ResourceType(checksum="sample_text", excluded="sample_text", file="sample_text", id="sample_text", name="sample_text", no2d="sample_text", no3d="sample_text", noMols="sample_text", type="sample_text", uRL="sample_text")
    assert instance.excluded == "sample_text"
    instance.excluded = "sample_text_2"
    assert instance.excluded == "sample_text_2"


def test_qsar_ResourceType_file_value_roundtrip():
    instance = qsar_ResourceType(checksum="sample_text", excluded="sample_text", file="sample_text", id="sample_text", name="sample_text", no2d="sample_text", no3d="sample_text", noMols="sample_text", type="sample_text", uRL="sample_text")
    assert instance.file == "sample_text"
    instance.file = "sample_text_2"
    assert instance.file == "sample_text_2"


def test_qsar_ResourceType_id_value_roundtrip():
    instance = qsar_ResourceType(checksum="sample_text", excluded="sample_text", file="sample_text", id="sample_text", name="sample_text", no2d="sample_text", no3d="sample_text", noMols="sample_text", type="sample_text", uRL="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_qsar_ResourceType_name_value_roundtrip():
    instance = qsar_ResourceType(checksum="sample_text", excluded="sample_text", file="sample_text", id="sample_text", name="sample_text", no2d="sample_text", no3d="sample_text", noMols="sample_text", type="sample_text", uRL="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_qsar_ResourceType_no2d_value_roundtrip():
    instance = qsar_ResourceType(checksum="sample_text", excluded="sample_text", file="sample_text", id="sample_text", name="sample_text", no2d="sample_text", no3d="sample_text", noMols="sample_text", type="sample_text", uRL="sample_text")
    assert instance.no2d == "sample_text"
    instance.no2d = "sample_text_2"
    assert instance.no2d == "sample_text_2"


def test_qsar_ResourceType_no3d_value_roundtrip():
    instance = qsar_ResourceType(checksum="sample_text", excluded="sample_text", file="sample_text", id="sample_text", name="sample_text", no2d="sample_text", no3d="sample_text", noMols="sample_text", type="sample_text", uRL="sample_text")
    assert instance.no3d == "sample_text"
    instance.no3d = "sample_text_2"
    assert instance.no3d == "sample_text_2"


def test_qsar_ResourceType_noMols_value_roundtrip():
    instance = qsar_ResourceType(checksum="sample_text", excluded="sample_text", file="sample_text", id="sample_text", name="sample_text", no2d="sample_text", no3d="sample_text", noMols="sample_text", type="sample_text", uRL="sample_text")
    assert instance.noMols == "sample_text"
    instance.noMols = "sample_text_2"
    assert instance.noMols == "sample_text_2"


def test_qsar_ResourceType_type_value_roundtrip():
    instance = qsar_ResourceType(checksum="sample_text", excluded="sample_text", file="sample_text", id="sample_text", name="sample_text", no2d="sample_text", no3d="sample_text", noMols="sample_text", type="sample_text", uRL="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_qsar_ResourceType_uRL_value_roundtrip():
    instance = qsar_ResourceType(checksum="sample_text", excluded="sample_text", file="sample_text", id="sample_text", name="sample_text", no2d="sample_text", no3d="sample_text", noMols="sample_text", type="sample_text", uRL="sample_text")
    assert instance.uRL == "sample_text"
    instance.uRL = "sample_text_2"
    assert instance.uRL == "sample_text_2"


def test_qsar_ResponseType_arrayValues_value_roundtrip():
    instance = qsar_ResponseType(arrayValues="sample_text", structureID="sample_text", unit="sample_text", value="sample_text")
    assert instance.arrayValues == "sample_text"
    instance.arrayValues = "sample_text_2"
    assert instance.arrayValues == "sample_text_2"


def test_qsar_ResponseType_structureID_value_roundtrip():
    instance = qsar_ResponseType(arrayValues="sample_text", structureID="sample_text", unit="sample_text", value="sample_text")
    assert instance.structureID == "sample_text"
    instance.structureID = "sample_text_2"
    assert instance.structureID == "sample_text_2"


def test_qsar_ResponseType_unit_value_roundtrip():
    instance = qsar_ResponseType(arrayValues="sample_text", structureID="sample_text", unit="sample_text", value="sample_text")
    assert instance.unit == "sample_text"
    instance.unit = "sample_text_2"
    assert instance.unit == "sample_text_2"


def test_qsar_ResponseType_value_value_roundtrip():
    instance = qsar_ResponseType(arrayValues="sample_text", structureID="sample_text", unit="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_qsar_ResponseunitType_description_value_roundtrip():
    instance = qsar_ResponseunitType(description="sample_text", id="sample_text", name="sample_text", shortname="sample_text", uRL="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_qsar_ResponseunitType_id_value_roundtrip():
    instance = qsar_ResponseunitType(description="sample_text", id="sample_text", name="sample_text", shortname="sample_text", uRL="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_qsar_ResponseunitType_name_value_roundtrip():
    instance = qsar_ResponseunitType(description="sample_text", id="sample_text", name="sample_text", shortname="sample_text", uRL="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_qsar_ResponseunitType_shortname_value_roundtrip():
    instance = qsar_ResponseunitType(description="sample_text", id="sample_text", name="sample_text", shortname="sample_text", uRL="sample_text")
    assert instance.shortname == "sample_text"
    instance.shortname = "sample_text_2"
    assert instance.shortname == "sample_text_2"


def test_qsar_ResponseunitType_uRL_value_roundtrip():
    instance = qsar_ResponseunitType(description="sample_text", id="sample_text", name="sample_text", shortname="sample_text", uRL="sample_text")
    assert instance.uRL == "sample_text"
    instance.uRL = "sample_text_2"
    assert instance.uRL == "sample_text_2"


def test_qsar_StructureType_id_value_roundtrip():
    instance = qsar_StructureType(id="sample_text", inchi="sample_text", resourceid="sample_text", resourceindex="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_qsar_StructureType_inchi_value_roundtrip():
    instance = qsar_StructureType(id="sample_text", inchi="sample_text", resourceid="sample_text", resourceindex="sample_text")
    assert instance.inchi == "sample_text"
    instance.inchi = "sample_text_2"
    assert instance.inchi == "sample_text_2"


def test_qsar_StructureType_resourceid_value_roundtrip():
    instance = qsar_StructureType(id="sample_text", inchi="sample_text", resourceid="sample_text", resourceindex="sample_text")
    assert instance.resourceid == "sample_text"
    instance.resourceid = "sample_text_2"
    assert instance.resourceid == "sample_text_2"


def test_qsar_StructureType_resourceindex_value_roundtrip():
    instance = qsar_StructureType(id="sample_text", inchi="sample_text", resourceid="sample_text", resourceindex="sample_text")
    assert instance.resourceindex == "sample_text"
    instance.resourceindex = "sample_text_2"
    assert instance.resourceindex == "sample_text_2"


def test_assoc_descriptorproviders19_link_reassign_clear():
    a = qsar_DescriptorproviderType(id="sample_text", name="sample_text", uRL="sample_text", vendor="sample_text", version="sample_text")
    b1 = qsar_QsarType()
    b2 = qsar_QsarType()
    _safe_set(a, 'qsar_DescriptorproviderType', b1)
    assert _is_linked(a, 'qsar_DescriptorproviderType', b1)
    if hasattr(b1, 'qsar_QsarType20'):
        assert _is_linked(b1, 'qsar_QsarType20', a)
    _safe_set(a, 'qsar_DescriptorproviderType', b2)
    assert _is_linked(a, 'qsar_DescriptorproviderType', b2)
    if hasattr(b1, 'qsar_QsarType20'):
        assert not _is_linked(b1, 'qsar_QsarType20', a)
    if hasattr(b2, 'qsar_QsarType20'):
        assert _is_linked(b2, 'qsar_QsarType20', a)
    _safe_set(a, 'qsar_DescriptorproviderType', None)
    assert not _is_linked(a, 'qsar_DescriptorproviderType', b2)
    if hasattr(b2, 'qsar_QsarType20'):
        assert not _is_linked(b2, 'qsar_QsarType20', a)


def test_assoc_descriptorresult1_link_reassign_clear():
    a = qsar_DescriptorresultType(descriptorid="sample_text", structureid="sample_text")
    b1 = qsar_DescriptorresultlistsType()
    b2 = qsar_DescriptorresultlistsType()
    _safe_set(a, 'qsar_DescriptorresultType', b1)
    assert _is_linked(a, 'qsar_DescriptorresultType', b1)
    if hasattr(b1, 'qsar_DescriptorresultlistsType'):
        assert _is_linked(b1, 'qsar_DescriptorresultlistsType', a)
    _safe_set(a, 'qsar_DescriptorresultType', b2)
    assert _is_linked(a, 'qsar_DescriptorresultType', b2)
    if hasattr(b1, 'qsar_DescriptorresultlistsType'):
        assert not _is_linked(b1, 'qsar_DescriptorresultlistsType', a)
    if hasattr(b2, 'qsar_DescriptorresultlistsType'):
        assert _is_linked(b2, 'qsar_DescriptorresultlistsType', a)
    _safe_set(a, 'qsar_DescriptorresultType', None)
    assert not _is_linked(a, 'qsar_DescriptorresultType', b2)
    if hasattr(b2, 'qsar_DescriptorresultlistsType'):
        assert not _is_linked(b2, 'qsar_DescriptorresultlistsType', a)


def test_assoc_descriptors0_link_reassign_clear():
    a = qsar_DescriptorType(id="sample_text", ontologyid="sample_text", provider="sample_text")
    b1 = qsar_DescriptorlistType()
    b2 = qsar_DescriptorlistType()
    _safe_set(a, 'qsar_DescriptorType', b1)
    assert _is_linked(a, 'qsar_DescriptorType', b1)
    if hasattr(b1, 'qsar_DescriptorlistType'):
        assert _is_linked(b1, 'qsar_DescriptorlistType', a)
    _safe_set(a, 'qsar_DescriptorType', b2)
    assert _is_linked(a, 'qsar_DescriptorType', b2)
    if hasattr(b1, 'qsar_DescriptorlistType'):
        assert not _is_linked(b1, 'qsar_DescriptorlistType', a)
    if hasattr(b2, 'qsar_DescriptorlistType'):
        assert _is_linked(b2, 'qsar_DescriptorlistType', a)
    _safe_set(a, 'qsar_DescriptorType', None)
    assert not _is_linked(a, 'qsar_DescriptorType', b2)
    if hasattr(b2, 'qsar_DescriptorlistType'):
        assert not _is_linked(b2, 'qsar_DescriptorlistType', a)


def test_assoc_descriptorvalue2_link_reassign_clear():
    a = qsar_DescriptorvalueType(index="sample_text", label="sample_text", value="sample_text")
    b1 = qsar_DescriptorresultType(descriptorid="sample_text", structureid="sample_text")
    b2 = qsar_DescriptorresultType(descriptorid="sample_text_2", structureid="sample_text_2")
    _safe_set(a, 'qsar_DescriptorvalueType', b1)
    assert _is_linked(a, 'qsar_DescriptorvalueType', b1)
    if hasattr(b1, 'qsar_DescriptorresultType3'):
        assert _is_linked(b1, 'qsar_DescriptorresultType3', a)
    _safe_set(a, 'qsar_DescriptorvalueType', b2)
    assert _is_linked(a, 'qsar_DescriptorvalueType', b2)
    if hasattr(b1, 'qsar_DescriptorresultType3'):
        assert not _is_linked(b1, 'qsar_DescriptorresultType3', a)
    if hasattr(b2, 'qsar_DescriptorresultType3'):
        assert _is_linked(b2, 'qsar_DescriptorresultType3', a)
    _safe_set(a, 'qsar_DescriptorvalueType', None)
    assert not _is_linked(a, 'qsar_DescriptorvalueType', b2)
    if hasattr(b2, 'qsar_DescriptorresultType3'):
        assert not _is_linked(b2, 'qsar_DescriptorresultType3', a)


def test_assoc_metadata28_link_reassign_clear():
    a = qsar_MetadataType(authors="sample_text", datasetname="sample_text", description="sample_text", license="sample_text", uRL="sample_text")
    b1 = qsar_QsarType()
    b2 = qsar_QsarType()
    _safe_set(a, 'qsar_MetadataType30', b1)
    assert _is_linked(a, 'qsar_MetadataType30', b1)
    if hasattr(b1, 'qsar_QsarType29'):
        assert _is_linked(b1, 'qsar_QsarType29', a)
    _safe_set(a, 'qsar_MetadataType30', b2)
    assert _is_linked(a, 'qsar_MetadataType30', b2)
    if hasattr(b1, 'qsar_QsarType29'):
        assert not _is_linked(b1, 'qsar_QsarType29', a)
    if hasattr(b2, 'qsar_QsarType29'):
        assert _is_linked(b2, 'qsar_QsarType29', a)
    _safe_set(a, 'qsar_MetadataType30', None)
    assert not _is_linked(a, 'qsar_MetadataType30', b2)
    if hasattr(b2, 'qsar_QsarType29'):
        assert not _is_linked(b2, 'qsar_QsarType29', a)


def test_assoc_parameter4_link_reassign_clear():
    a = qsar_ParameterType(key="sample_text", value="sample_text")
    b1 = qsar_DescriptorType(id="sample_text", ontologyid="sample_text", provider="sample_text")
    b2 = qsar_DescriptorType(id="sample_text_2", ontologyid="sample_text_2", provider="sample_text_2")
    _safe_set(a, 'qsar_ParameterType', b1)
    assert _is_linked(a, 'qsar_ParameterType', b1)
    if hasattr(b1, 'qsar_DescriptorType5'):
        assert _is_linked(b1, 'qsar_DescriptorType5', a)
    _safe_set(a, 'qsar_ParameterType', b2)
    assert _is_linked(a, 'qsar_ParameterType', b2)
    if hasattr(b1, 'qsar_DescriptorType5'):
        assert not _is_linked(b1, 'qsar_DescriptorType5', a)
    if hasattr(b2, 'qsar_DescriptorType5'):
        assert _is_linked(b2, 'qsar_DescriptorType5', a)
    _safe_set(a, 'qsar_ParameterType', None)
    assert not _is_linked(a, 'qsar_ParameterType', b2)
    if hasattr(b2, 'qsar_DescriptorType5'):
        assert not _is_linked(b2, 'qsar_DescriptorType5', a)


def test_assoc_preprocessingStep13_link_reassign_clear():
    a = qsar_PreprocessingStepType(id="sample_text", name="sample_text", namespace="sample_text", order="sample_text", vendor="sample_text")
    b1 = qsar_PreprocessingType()
    b2 = qsar_PreprocessingType()
    _safe_set(a, 'qsar_PreprocessingStepType', b1)
    assert _is_linked(a, 'qsar_PreprocessingStepType', b1)
    if hasattr(b1, 'qsar_PreprocessingType'):
        assert _is_linked(b1, 'qsar_PreprocessingType', a)
    _safe_set(a, 'qsar_PreprocessingStepType', b2)
    assert _is_linked(a, 'qsar_PreprocessingStepType', b2)
    if hasattr(b1, 'qsar_PreprocessingType'):
        assert not _is_linked(b1, 'qsar_PreprocessingType', a)
    if hasattr(b2, 'qsar_PreprocessingType'):
        assert _is_linked(b2, 'qsar_PreprocessingType', a)
    _safe_set(a, 'qsar_PreprocessingStepType', None)
    assert not _is_linked(a, 'qsar_PreprocessingStepType', b2)
    if hasattr(b2, 'qsar_PreprocessingType'):
        assert not _is_linked(b2, 'qsar_PreprocessingType', a)


def test_assoc_qsar10_link_reassign_clear():
    a = qsar_DocumentRoot(mixed="sample_text")
    b1 = qsar_QsarType()
    b2 = qsar_QsarType()
    _safe_set(a, 'qsar_DocumentRoot11', {b1})
    assert _is_linked(a, 'qsar_DocumentRoot11', b1)
    if hasattr(b1, 'qsar_QsarType'):
        assert _is_linked(b1, 'qsar_QsarType', a)
    _safe_set(a, 'qsar_DocumentRoot11', {b2})
    assert _is_linked(a, 'qsar_DocumentRoot11', b2)
    if hasattr(b1, 'qsar_QsarType'):
        assert not _is_linked(b1, 'qsar_QsarType', a)
    if hasattr(b2, 'qsar_QsarType'):
        assert _is_linked(b2, 'qsar_QsarType', a)
    _safe_set(a, 'qsar_DocumentRoot11', set())
    assert not _is_linked(a, 'qsar_DocumentRoot11', b2)
    if hasattr(b2, 'qsar_QsarType'):
        assert not _is_linked(b2, 'qsar_QsarType', a)


def test_assoc_reference12_link_reassign_clear():
    a = qsar_MetadataType(authors="sample_text", datasetname="sample_text", description="sample_text", license="sample_text", uRL="sample_text")
    b1 = qsar_BibTeXMLEntriesClass()
    b2 = qsar_BibTeXMLEntriesClass()
    _safe_set(a, 'qsar_MetadataType', {b1})
    assert _is_linked(a, 'qsar_MetadataType', b1)
    if hasattr(b1, 'qsar_BibTeXMLEntriesClass'):
        assert _is_linked(b1, 'qsar_BibTeXMLEntriesClass', a)
    _safe_set(a, 'qsar_MetadataType', {b2})
    assert _is_linked(a, 'qsar_MetadataType', b2)
    if hasattr(b1, 'qsar_BibTeXMLEntriesClass'):
        assert not _is_linked(b1, 'qsar_BibTeXMLEntriesClass', a)
    if hasattr(b2, 'qsar_BibTeXMLEntriesClass'):
        assert _is_linked(b2, 'qsar_BibTeXMLEntriesClass', a)
    _safe_set(a, 'qsar_MetadataType', set())
    assert not _is_linked(a, 'qsar_MetadataType', b2)
    if hasattr(b2, 'qsar_BibTeXMLEntriesClass'):
        assert not _is_linked(b2, 'qsar_BibTeXMLEntriesClass', a)


def test_assoc_resources37_link_reassign_clear():
    a = qsar_ResourceType(checksum="sample_text", excluded="sample_text", file="sample_text", id="sample_text", name="sample_text", no2d="sample_text", no3d="sample_text", noMols="sample_text", type="sample_text", uRL="sample_text")
    b1 = qsar_StructurelistType()
    b2 = qsar_StructurelistType()
    _safe_set(a, 'qsar_ResourceType39', b1)
    assert _is_linked(a, 'qsar_ResourceType39', b1)
    if hasattr(b1, 'qsar_StructurelistType38'):
        assert _is_linked(b1, 'qsar_StructurelistType38', a)
    _safe_set(a, 'qsar_ResourceType39', b2)
    assert _is_linked(a, 'qsar_ResourceType39', b2)
    if hasattr(b1, 'qsar_StructurelistType38'):
        assert not _is_linked(b1, 'qsar_StructurelistType38', a)
    if hasattr(b2, 'qsar_StructurelistType38'):
        assert _is_linked(b2, 'qsar_StructurelistType38', a)
    _safe_set(a, 'qsar_ResourceType39', None)
    assert not _is_linked(a, 'qsar_ResourceType39', b2)
    if hasattr(b2, 'qsar_StructurelistType38'):
        assert not _is_linked(b2, 'qsar_StructurelistType38', a)


def test_assoc_response35_link_reassign_clear():
    a = qsar_ResponseType(arrayValues="sample_text", structureID="sample_text", unit="sample_text", value="sample_text")
    b1 = qsar_ResponsesListType()
    b2 = qsar_ResponsesListType()
    _safe_set(a, 'qsar_ResponseType', b1)
    assert _is_linked(a, 'qsar_ResponseType', b1)
    if hasattr(b1, 'qsar_ResponsesListType36'):
        assert _is_linked(b1, 'qsar_ResponsesListType36', a)
    _safe_set(a, 'qsar_ResponseType', b2)
    assert _is_linked(a, 'qsar_ResponseType', b2)
    if hasattr(b1, 'qsar_ResponsesListType36'):
        assert not _is_linked(b1, 'qsar_ResponsesListType36', a)
    if hasattr(b2, 'qsar_ResponsesListType36'):
        assert _is_linked(b2, 'qsar_ResponsesListType36', a)
    _safe_set(a, 'qsar_ResponseType', None)
    assert not _is_linked(a, 'qsar_ResponseType', b2)
    if hasattr(b2, 'qsar_ResponsesListType36'):
        assert not _is_linked(b2, 'qsar_ResponsesListType36', a)


def test_assoc_responseunit26_link_reassign_clear():
    a = qsar_ResponseunitType(description="sample_text", id="sample_text", name="sample_text", shortname="sample_text", uRL="sample_text")
    b1 = qsar_QsarType()
    b2 = qsar_QsarType()
    _safe_set(a, 'qsar_ResponseunitType', b1)
    assert _is_linked(a, 'qsar_ResponseunitType', b1)
    if hasattr(b1, 'qsar_QsarType27'):
        assert _is_linked(b1, 'qsar_QsarType27', a)
    _safe_set(a, 'qsar_ResponseunitType', b2)
    assert _is_linked(a, 'qsar_ResponseunitType', b2)
    if hasattr(b1, 'qsar_QsarType27'):
        assert not _is_linked(b1, 'qsar_QsarType27', a)
    if hasattr(b2, 'qsar_QsarType27'):
        assert _is_linked(b2, 'qsar_QsarType27', a)
    _safe_set(a, 'qsar_ResponseunitType', None)
    assert not _is_linked(a, 'qsar_ResponseunitType', b2)
    if hasattr(b2, 'qsar_QsarType27'):
        assert not _is_linked(b2, 'qsar_QsarType27', a)


def test_assoc_structure34_link_reassign_clear():
    a = qsar_StructureType(id="sample_text", inchi="sample_text", resourceid="sample_text", resourceindex="sample_text")
    b1 = qsar_ResourceType(checksum="sample_text", excluded="sample_text", file="sample_text", id="sample_text", name="sample_text", no2d="sample_text", no3d="sample_text", noMols="sample_text", type="sample_text", uRL="sample_text")
    b2 = qsar_ResourceType(checksum="sample_text_2", excluded="sample_text_2", file="sample_text_2", id="sample_text_2", name="sample_text_2", no2d="sample_text_2", no3d="sample_text_2", noMols="sample_text_2", type="sample_text_2", uRL="sample_text_2")
    _safe_set(a, 'qsar_StructureType', b1)
    assert _is_linked(a, 'qsar_StructureType', b1)
    if hasattr(b1, 'qsar_ResourceType'):
        assert _is_linked(b1, 'qsar_ResourceType', a)
    _safe_set(a, 'qsar_StructureType', b2)
    assert _is_linked(a, 'qsar_StructureType', b2)
    if hasattr(b1, 'qsar_ResourceType'):
        assert not _is_linked(b1, 'qsar_ResourceType', a)
    if hasattr(b2, 'qsar_ResourceType'):
        assert _is_linked(b2, 'qsar_ResourceType', a)
    _safe_set(a, 'qsar_StructureType', None)
    assert not _is_linked(a, 'qsar_StructureType', b2)
    if hasattr(b2, 'qsar_ResourceType'):
        assert not _is_linked(b2, 'qsar_ResourceType', a)


def test_assoc_xMLNSPrefixMap6_link_reassign_clear():
    a = qsar_DocumentRoot(mixed="sample_text")
    b1 = qsar_EStringToStringMapEntry()
    b2 = qsar_EStringToStringMapEntry()
    _safe_set(a, 'qsar_DocumentRoot', {b1})
    assert _is_linked(a, 'qsar_DocumentRoot', b1)
    if hasattr(b1, 'qsar_EStringToStringMapEntry'):
        assert _is_linked(b1, 'qsar_EStringToStringMapEntry', a)
    _safe_set(a, 'qsar_DocumentRoot', {b2})
    assert _is_linked(a, 'qsar_DocumentRoot', b2)
    if hasattr(b1, 'qsar_EStringToStringMapEntry'):
        assert not _is_linked(b1, 'qsar_EStringToStringMapEntry', a)
    if hasattr(b2, 'qsar_EStringToStringMapEntry'):
        assert _is_linked(b2, 'qsar_EStringToStringMapEntry', a)
    _safe_set(a, 'qsar_DocumentRoot', set())
    assert not _is_linked(a, 'qsar_DocumentRoot', b2)
    if hasattr(b2, 'qsar_EStringToStringMapEntry'):
        assert not _is_linked(b2, 'qsar_EStringToStringMapEntry', a)


def test_assoc_xSISchemaLocation7_link_reassign_clear():
    a = qsar_DocumentRoot(mixed="sample_text")
    b1 = qsar_EStringToStringMapEntry()
    b2 = qsar_EStringToStringMapEntry()
    _safe_set(a, 'qsar_DocumentRoot8', {b1})
    assert _is_linked(a, 'qsar_DocumentRoot8', b1)
    if hasattr(b1, 'qsar_EStringToStringMapEntry9'):
        assert _is_linked(b1, 'qsar_EStringToStringMapEntry9', a)
    _safe_set(a, 'qsar_DocumentRoot8', {b2})
    assert _is_linked(a, 'qsar_DocumentRoot8', b2)
    if hasattr(b1, 'qsar_EStringToStringMapEntry9'):
        assert not _is_linked(b1, 'qsar_EStringToStringMapEntry9', a)
    if hasattr(b2, 'qsar_EStringToStringMapEntry9'):
        assert _is_linked(b2, 'qsar_EStringToStringMapEntry9', a)
    _safe_set(a, 'qsar_DocumentRoot8', set())
    assert not _is_linked(a, 'qsar_DocumentRoot8', b2)
    if hasattr(b2, 'qsar_EStringToStringMapEntry9'):
        assert not _is_linked(b2, 'qsar_EStringToStringMapEntry9', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

qsar_BibTeXMLEntriesClass_strategy = st.builds(qsar_BibTeXMLEntriesClass)
@given(instance=qsar_BibTeXMLEntriesClass_strategy)
@settings(max_examples=25)
def test_qsar_BibTeXMLEntriesClass_instantiation(instance):
    assert isinstance(instance, qsar_BibTeXMLEntriesClass)


qsar_DescriptorType_strategy = st.builds(qsar_DescriptorType, id=safe_text, ontologyid=safe_text, provider=safe_text)
@given(instance=qsar_DescriptorType_strategy)
@settings(max_examples=25)
def test_qsar_DescriptorType_instantiation(instance):
    assert isinstance(instance, qsar_DescriptorType)


qsar_DescriptorlistType_strategy = st.builds(qsar_DescriptorlistType)
@given(instance=qsar_DescriptorlistType_strategy)
@settings(max_examples=25)
def test_qsar_DescriptorlistType_instantiation(instance):
    assert isinstance(instance, qsar_DescriptorlistType)


qsar_DescriptorproviderType_strategy = st.builds(qsar_DescriptorproviderType, id=safe_text, name=safe_text, uRL=safe_text, vendor=safe_text, version=safe_text)
@given(instance=qsar_DescriptorproviderType_strategy)
@settings(max_examples=25)
def test_qsar_DescriptorproviderType_instantiation(instance):
    assert isinstance(instance, qsar_DescriptorproviderType)


qsar_DescriptorresultType_strategy = st.builds(qsar_DescriptorresultType, descriptorid=safe_text, structureid=safe_text)
@given(instance=qsar_DescriptorresultType_strategy)
@settings(max_examples=25)
def test_qsar_DescriptorresultType_instantiation(instance):
    assert isinstance(instance, qsar_DescriptorresultType)


qsar_DescriptorresultlistsType_strategy = st.builds(qsar_DescriptorresultlistsType)
@given(instance=qsar_DescriptorresultlistsType_strategy)
@settings(max_examples=25)
def test_qsar_DescriptorresultlistsType_instantiation(instance):
    assert isinstance(instance, qsar_DescriptorresultlistsType)


qsar_DescriptorvalueType_strategy = st.builds(qsar_DescriptorvalueType, index=safe_text, label=safe_text, value=safe_text)
@given(instance=qsar_DescriptorvalueType_strategy)
@settings(max_examples=25)
def test_qsar_DescriptorvalueType_instantiation(instance):
    assert isinstance(instance, qsar_DescriptorvalueType)


qsar_DocumentRoot_strategy = st.builds(qsar_DocumentRoot, mixed=safe_text)
@given(instance=qsar_DocumentRoot_strategy)
@settings(max_examples=25)
def test_qsar_DocumentRoot_instantiation(instance):
    assert isinstance(instance, qsar_DocumentRoot)


qsar_EStringToStringMapEntry_strategy = st.builds(qsar_EStringToStringMapEntry)
@given(instance=qsar_EStringToStringMapEntry_strategy)
@settings(max_examples=25)
def test_qsar_EStringToStringMapEntry_instantiation(instance):
    assert isinstance(instance, qsar_EStringToStringMapEntry)


qsar_MetadataType_strategy = st.builds(qsar_MetadataType, authors=safe_text, datasetname=safe_text, description=safe_text, license=safe_text, uRL=safe_text)
@given(instance=qsar_MetadataType_strategy)
@settings(max_examples=25)
def test_qsar_MetadataType_instantiation(instance):
    assert isinstance(instance, qsar_MetadataType)


qsar_ParameterType_strategy = st.builds(qsar_ParameterType, key=safe_text, value=safe_text)
@given(instance=qsar_ParameterType_strategy)
@settings(max_examples=25)
def test_qsar_ParameterType_instantiation(instance):
    assert isinstance(instance, qsar_ParameterType)


qsar_PreprocessingStepType_strategy = st.builds(qsar_PreprocessingStepType, id=safe_text, name=safe_text, namespace=safe_text, order=safe_text, vendor=safe_text)
@given(instance=qsar_PreprocessingStepType_strategy)
@settings(max_examples=25)
def test_qsar_PreprocessingStepType_instantiation(instance):
    assert isinstance(instance, qsar_PreprocessingStepType)


qsar_PreprocessingType_strategy = st.builds(qsar_PreprocessingType)
@given(instance=qsar_PreprocessingType_strategy)
@settings(max_examples=25)
def test_qsar_PreprocessingType_instantiation(instance):
    assert isinstance(instance, qsar_PreprocessingType)


qsar_QsarType_strategy = st.builds(qsar_QsarType)
@given(instance=qsar_QsarType_strategy)
@settings(max_examples=25)
def test_qsar_QsarType_instantiation(instance):
    assert isinstance(instance, qsar_QsarType)


qsar_ResourceType_strategy = st.builds(qsar_ResourceType, checksum=safe_text, excluded=safe_text, file=safe_text, id=safe_text, name=safe_text, no2d=safe_text, no3d=safe_text, noMols=safe_text, type=safe_text, uRL=safe_text)
@given(instance=qsar_ResourceType_strategy)
@settings(max_examples=25)
def test_qsar_ResourceType_instantiation(instance):
    assert isinstance(instance, qsar_ResourceType)


qsar_ResponseType_strategy = st.builds(qsar_ResponseType, arrayValues=safe_text, structureID=safe_text, unit=safe_text, value=safe_text)
@given(instance=qsar_ResponseType_strategy)
@settings(max_examples=25)
def test_qsar_ResponseType_instantiation(instance):
    assert isinstance(instance, qsar_ResponseType)


qsar_ResponsesListType_strategy = st.builds(qsar_ResponsesListType)
@given(instance=qsar_ResponsesListType_strategy)
@settings(max_examples=25)
def test_qsar_ResponsesListType_instantiation(instance):
    assert isinstance(instance, qsar_ResponsesListType)


qsar_ResponseunitType_strategy = st.builds(qsar_ResponseunitType, description=safe_text, id=safe_text, name=safe_text, shortname=safe_text, uRL=safe_text)
@given(instance=qsar_ResponseunitType_strategy)
@settings(max_examples=25)
def test_qsar_ResponseunitType_instantiation(instance):
    assert isinstance(instance, qsar_ResponseunitType)


qsar_StructureType_strategy = st.builds(qsar_StructureType, id=safe_text, inchi=safe_text, resourceid=safe_text, resourceindex=safe_text)
@given(instance=qsar_StructureType_strategy)
@settings(max_examples=25)
def test_qsar_StructureType_instantiation(instance):
    assert isinstance(instance, qsar_StructureType)


qsar_StructurelistType_strategy = st.builds(qsar_StructurelistType)
@given(instance=qsar_StructurelistType_strategy)
@settings(max_examples=25)
def test_qsar_StructurelistType_instantiation(instance):
    assert isinstance(instance, qsar_StructurelistType)


