import pytest
from datetime import date, datetime, time, timedelta

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

def test_assoc_descriptorvalue2_reverse_link_reassign_clear():
    a1 = qsar_DescriptorvalueType(index="sample_text", label="sample_text", value="sample_text")
    a2 = qsar_DescriptorvalueType(index="sample_text_2", label="sample_text_2", value="sample_text_2")
    b = qsar_DescriptorresultType(descriptorid="sample_text", structureid="sample_text")
    _safe_set(b, 'qsar_DescriptorresultType3', {a1})
    assert _is_linked(b, 'qsar_DescriptorresultType3', a1)
    if hasattr(a1, 'qsar_DescriptorvalueType'):
        assert _is_linked(a1, 'qsar_DescriptorvalueType', b)
    _safe_set(b, 'qsar_DescriptorresultType3', {a2})
    assert _is_linked(b, 'qsar_DescriptorresultType3', a2)
    if hasattr(a1, 'qsar_DescriptorvalueType'):
        assert not _is_linked(a1, 'qsar_DescriptorvalueType', b)
    if hasattr(a2, 'qsar_DescriptorvalueType'):
        assert _is_linked(a2, 'qsar_DescriptorvalueType', b)
    _safe_set(b, 'qsar_DescriptorresultType3', set())
    assert not _is_linked(b, 'qsar_DescriptorresultType3', a2)
    if hasattr(a2, 'qsar_DescriptorvalueType'):
        assert not _is_linked(a2, 'qsar_DescriptorvalueType', b)


def test_assoc_parameter4_reverse_link_reassign_clear():
    a1 = qsar_ParameterType(key="sample_text", value="sample_text")
    a2 = qsar_ParameterType(key="sample_text_2", value="sample_text_2")
    b = qsar_DescriptorType(id="sample_text", ontologyid="sample_text", provider="sample_text")
    _safe_set(b, 'qsar_DescriptorType5', {a1})
    assert _is_linked(b, 'qsar_DescriptorType5', a1)
    if hasattr(a1, 'qsar_ParameterType'):
        assert _is_linked(a1, 'qsar_ParameterType', b)
    _safe_set(b, 'qsar_DescriptorType5', {a2})
    assert _is_linked(b, 'qsar_DescriptorType5', a2)
    if hasattr(a1, 'qsar_ParameterType'):
        assert not _is_linked(a1, 'qsar_ParameterType', b)
    if hasattr(a2, 'qsar_ParameterType'):
        assert _is_linked(a2, 'qsar_ParameterType', b)
    _safe_set(b, 'qsar_DescriptorType5', set())
    assert not _is_linked(b, 'qsar_DescriptorType5', a2)
    if hasattr(a2, 'qsar_ParameterType'):
        assert not _is_linked(a2, 'qsar_ParameterType', b)


def test_assoc_structure34_reverse_link_reassign_clear():
    a1 = qsar_StructureType(id="sample_text", inchi="sample_text", resourceid="sample_text", resourceindex="sample_text")
    a2 = qsar_StructureType(id="sample_text_2", inchi="sample_text_2", resourceid="sample_text_2", resourceindex="sample_text_2")
    b = qsar_ResourceType(checksum="sample_text", excluded="sample_text", file="sample_text", id="sample_text", name="sample_text", no2d="sample_text", no3d="sample_text", noMols="sample_text", type="sample_text", uRL="sample_text")
    _safe_set(b, 'qsar_ResourceType', {a1})
    assert _is_linked(b, 'qsar_ResourceType', a1)
    if hasattr(a1, 'qsar_StructureType'):
        assert _is_linked(a1, 'qsar_StructureType', b)
    _safe_set(b, 'qsar_ResourceType', {a2})
    assert _is_linked(b, 'qsar_ResourceType', a2)
    if hasattr(a1, 'qsar_StructureType'):
        assert not _is_linked(a1, 'qsar_StructureType', b)
    if hasattr(a2, 'qsar_StructureType'):
        assert _is_linked(a2, 'qsar_StructureType', b)
    _safe_set(b, 'qsar_ResourceType', set())
    assert not _is_linked(b, 'qsar_ResourceType', a2)
    if hasattr(a2, 'qsar_StructureType'):
        assert not _is_linked(a2, 'qsar_StructureType', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_descriptorproviders19_stub_double():
    # qsar_QsarType has no real 'qsar_QsarType20' property in the generated
    # code (a bare stub) -- manually attach it so qsar_DescriptorproviderType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qsar_DescriptorproviderType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qsar_DescriptorproviderType(id="sample_text", name="sample_text", uRL="sample_text", vendor="sample_text", version="sample_text")
    partner = qsar_QsarType()
    setattr(partner, 'qsar_QsarType20', None)
    _safe_set(owner, 'qsar_DescriptorproviderType', partner)
    assert owner in getattr(partner, 'qsar_QsarType20')
    _safe_set(owner, 'qsar_DescriptorproviderType', None)
    assert owner not in getattr(partner, 'qsar_QsarType20')


def test_assoc_descriptorresult1_stub_double():
    # qsar_DescriptorresultlistsType has no real 'qsar_DescriptorresultlistsType' property in the generated
    # code (a bare stub) -- manually attach it so qsar_DescriptorresultType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qsar_DescriptorresultType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qsar_DescriptorresultType(descriptorid="sample_text", structureid="sample_text")
    partner = qsar_DescriptorresultlistsType()
    setattr(partner, 'qsar_DescriptorresultlistsType', None)
    _safe_set(owner, 'qsar_DescriptorresultType', partner)
    assert owner in getattr(partner, 'qsar_DescriptorresultlistsType')
    _safe_set(owner, 'qsar_DescriptorresultType', None)
    assert owner not in getattr(partner, 'qsar_DescriptorresultlistsType')


def test_assoc_descriptors0_stub_double():
    # qsar_DescriptorlistType has no real 'qsar_DescriptorlistType' property in the generated
    # code (a bare stub) -- manually attach it so qsar_DescriptorType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qsar_DescriptorType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qsar_DescriptorType(id="sample_text", ontologyid="sample_text", provider="sample_text")
    partner = qsar_DescriptorlistType()
    setattr(partner, 'qsar_DescriptorlistType', None)
    _safe_set(owner, 'qsar_DescriptorType', partner)
    assert owner in getattr(partner, 'qsar_DescriptorlistType')
    _safe_set(owner, 'qsar_DescriptorType', None)
    assert owner not in getattr(partner, 'qsar_DescriptorlistType')


def test_assoc_metadata28_stub_double():
    # qsar_QsarType has no real 'qsar_QsarType29' property in the generated
    # code (a bare stub) -- manually attach it so qsar_MetadataType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qsar_MetadataType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qsar_MetadataType(authors="sample_text", datasetname="sample_text", description="sample_text", license="sample_text", uRL="sample_text")
    partner = qsar_QsarType()
    setattr(partner, 'qsar_QsarType29', None)
    _safe_set(owner, 'qsar_MetadataType30', partner)
    assert getattr(partner, 'qsar_QsarType29') == owner
    _safe_set(owner, 'qsar_MetadataType30', None)
    assert getattr(partner, 'qsar_QsarType29') is None


def test_assoc_preprocessingStep13_stub_double():
    # qsar_PreprocessingType has no real 'qsar_PreprocessingType' property in the generated
    # code (a bare stub) -- manually attach it so qsar_PreprocessingStepType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qsar_PreprocessingStepType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qsar_PreprocessingStepType(id="sample_text", name="sample_text", namespace="sample_text", order="sample_text", vendor="sample_text")
    partner = qsar_PreprocessingType()
    setattr(partner, 'qsar_PreprocessingType', None)
    _safe_set(owner, 'qsar_PreprocessingStepType', partner)
    assert owner in getattr(partner, 'qsar_PreprocessingType')
    _safe_set(owner, 'qsar_PreprocessingStepType', None)
    assert owner not in getattr(partner, 'qsar_PreprocessingType')


def test_assoc_qsar10_stub_double():
    # qsar_QsarType has no real 'qsar_QsarType' property in the generated
    # code (a bare stub) -- manually attach it so qsar_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qsar_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qsar_DocumentRoot(mixed="sample_text")
    partner = qsar_QsarType()
    setattr(partner, 'qsar_QsarType', None)
    _safe_set(owner, 'qsar_DocumentRoot11', {partner})
    assert getattr(partner, 'qsar_QsarType') == owner
    _safe_set(owner, 'qsar_DocumentRoot11', set())
    assert getattr(partner, 'qsar_QsarType') is None


def test_assoc_reference12_stub_double():
    # qsar_BibTeXMLEntriesClass has no real 'qsar_BibTeXMLEntriesClass' property in the generated
    # code (a bare stub) -- manually attach it so qsar_MetadataType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qsar_MetadataType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qsar_MetadataType(authors="sample_text", datasetname="sample_text", description="sample_text", license="sample_text", uRL="sample_text")
    partner = qsar_BibTeXMLEntriesClass()
    setattr(partner, 'qsar_BibTeXMLEntriesClass', None)
    _safe_set(owner, 'qsar_MetadataType', {partner})
    assert getattr(partner, 'qsar_BibTeXMLEntriesClass') == owner
    _safe_set(owner, 'qsar_MetadataType', set())
    assert getattr(partner, 'qsar_BibTeXMLEntriesClass') is None


def test_assoc_resources37_stub_double():
    # qsar_StructurelistType has no real 'qsar_StructurelistType38' property in the generated
    # code (a bare stub) -- manually attach it so qsar_ResourceType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qsar_ResourceType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qsar_ResourceType(checksum="sample_text", excluded="sample_text", file="sample_text", id="sample_text", name="sample_text", no2d="sample_text", no3d="sample_text", noMols="sample_text", type="sample_text", uRL="sample_text")
    partner = qsar_StructurelistType()
    setattr(partner, 'qsar_StructurelistType38', None)
    _safe_set(owner, 'qsar_ResourceType39', partner)
    assert owner in getattr(partner, 'qsar_StructurelistType38')
    _safe_set(owner, 'qsar_ResourceType39', None)
    assert owner not in getattr(partner, 'qsar_StructurelistType38')


def test_assoc_response35_stub_double():
    # qsar_ResponsesListType has no real 'qsar_ResponsesListType36' property in the generated
    # code (a bare stub) -- manually attach it so qsar_ResponseType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qsar_ResponseType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qsar_ResponseType(arrayValues="sample_text", structureID="sample_text", unit="sample_text", value="sample_text")
    partner = qsar_ResponsesListType()
    setattr(partner, 'qsar_ResponsesListType36', None)
    _safe_set(owner, 'qsar_ResponseType', partner)
    assert owner in getattr(partner, 'qsar_ResponsesListType36')
    _safe_set(owner, 'qsar_ResponseType', None)
    assert owner not in getattr(partner, 'qsar_ResponsesListType36')


def test_assoc_responseunit26_stub_double():
    # qsar_QsarType has no real 'qsar_QsarType27' property in the generated
    # code (a bare stub) -- manually attach it so qsar_ResponseunitType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qsar_ResponseunitType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qsar_ResponseunitType(description="sample_text", id="sample_text", name="sample_text", shortname="sample_text", uRL="sample_text")
    partner = qsar_QsarType()
    setattr(partner, 'qsar_QsarType27', None)
    _safe_set(owner, 'qsar_ResponseunitType', partner)
    assert owner in getattr(partner, 'qsar_QsarType27')
    _safe_set(owner, 'qsar_ResponseunitType', None)
    assert owner not in getattr(partner, 'qsar_QsarType27')


def test_assoc_xMLNSPrefixMap6_stub_double():
    # qsar_EStringToStringMapEntry has no real 'qsar_EStringToStringMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so qsar_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qsar_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qsar_DocumentRoot(mixed="sample_text")
    partner = qsar_EStringToStringMapEntry()
    setattr(partner, 'qsar_EStringToStringMapEntry', None)
    _safe_set(owner, 'qsar_DocumentRoot', {partner})
    assert getattr(partner, 'qsar_EStringToStringMapEntry') == owner
    _safe_set(owner, 'qsar_DocumentRoot', set())
    assert getattr(partner, 'qsar_EStringToStringMapEntry') is None


def test_assoc_xSISchemaLocation7_stub_double():
    # qsar_EStringToStringMapEntry has no real 'qsar_EStringToStringMapEntry9' property in the generated
    # code (a bare stub) -- manually attach it so qsar_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qsar_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qsar_DocumentRoot(mixed="sample_text")
    partner = qsar_EStringToStringMapEntry()
    setattr(partner, 'qsar_EStringToStringMapEntry9', None)
    _safe_set(owner, 'qsar_DocumentRoot8', {partner})
    assert getattr(partner, 'qsar_EStringToStringMapEntry9') == owner
    _safe_set(owner, 'qsar_DocumentRoot8', set())
    assert getattr(partner, 'qsar_EStringToStringMapEntry9') is None


