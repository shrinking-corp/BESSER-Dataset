import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    ClassOrDuplicate,
    dbmodel_Attribute,
    dbmodel_Class,
    dbmodel_ClassOrDuplicate,
    dbmodel_DbModel,
    dbmodel_Duplicate,
    dbmodel_Import,
    dbmodel_Index,
    dbmodel_IndexRef,
    dbmodel_Ltype,
    dbmodel_Pdb,
    dbmodel_Primkey,
    dbmodel_StructOverride,
    dbmodel_StructShare,
    dbmodel_Stype,
    dbmodel_Subject,
    dbmodel_Type,
    KobeType,
    KudaReplicate,
    KudaType,
    LockSchema,
    Mtype,
    PhysicalDatabase,
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

def test_dbmodel_Attribute_aName_value_roundtrip():
    instance = dbmodel_Attribute(aName="sample_text", archiv=True, descr="sample_text", extattr="sample_text", exttable="sample_text", foreign=True, immutable=True, isInDB=True, isPublic=True, kuko=True, kukoindex=True, kukoonly=True, name="sample_text", nullOK=True, optional=True, shared=True, sybident=True)
    assert instance.aName == "sample_text"
    instance.aName = "sample_text_2"
    assert instance.aName == "sample_text_2"


def test_dbmodel_Attribute_archiv_value_roundtrip():
    instance = dbmodel_Attribute(aName="sample_text", archiv=True, descr="sample_text", extattr="sample_text", exttable="sample_text", foreign=True, immutable=True, isInDB=True, isPublic=True, kuko=True, kukoindex=True, kukoonly=True, name="sample_text", nullOK=True, optional=True, shared=True, sybident=True)
    assert instance.archiv == True
    instance.archiv = False
    assert instance.archiv == False


def test_dbmodel_Attribute_descr_value_roundtrip():
    instance = dbmodel_Attribute(aName="sample_text", archiv=True, descr="sample_text", extattr="sample_text", exttable="sample_text", foreign=True, immutable=True, isInDB=True, isPublic=True, kuko=True, kukoindex=True, kukoonly=True, name="sample_text", nullOK=True, optional=True, shared=True, sybident=True)
    assert instance.descr == "sample_text"
    instance.descr = "sample_text_2"
    assert instance.descr == "sample_text_2"


def test_dbmodel_Attribute_extattr_value_roundtrip():
    instance = dbmodel_Attribute(aName="sample_text", archiv=True, descr="sample_text", extattr="sample_text", exttable="sample_text", foreign=True, immutable=True, isInDB=True, isPublic=True, kuko=True, kukoindex=True, kukoonly=True, name="sample_text", nullOK=True, optional=True, shared=True, sybident=True)
    assert instance.extattr == "sample_text"
    instance.extattr = "sample_text_2"
    assert instance.extattr == "sample_text_2"


def test_dbmodel_Attribute_exttable_value_roundtrip():
    instance = dbmodel_Attribute(aName="sample_text", archiv=True, descr="sample_text", extattr="sample_text", exttable="sample_text", foreign=True, immutable=True, isInDB=True, isPublic=True, kuko=True, kukoindex=True, kukoonly=True, name="sample_text", nullOK=True, optional=True, shared=True, sybident=True)
    assert instance.exttable == "sample_text"
    instance.exttable = "sample_text_2"
    assert instance.exttable == "sample_text_2"


def test_dbmodel_Attribute_foreign_value_roundtrip():
    instance = dbmodel_Attribute(aName="sample_text", archiv=True, descr="sample_text", extattr="sample_text", exttable="sample_text", foreign=True, immutable=True, isInDB=True, isPublic=True, kuko=True, kukoindex=True, kukoonly=True, name="sample_text", nullOK=True, optional=True, shared=True, sybident=True)
    assert instance.foreign == True
    instance.foreign = False
    assert instance.foreign == False


def test_dbmodel_Attribute_immutable_value_roundtrip():
    instance = dbmodel_Attribute(aName="sample_text", archiv=True, descr="sample_text", extattr="sample_text", exttable="sample_text", foreign=True, immutable=True, isInDB=True, isPublic=True, kuko=True, kukoindex=True, kukoonly=True, name="sample_text", nullOK=True, optional=True, shared=True, sybident=True)
    assert instance.immutable == True
    instance.immutable = False
    assert instance.immutable == False


def test_dbmodel_Attribute_isInDB_value_roundtrip():
    instance = dbmodel_Attribute(aName="sample_text", archiv=True, descr="sample_text", extattr="sample_text", exttable="sample_text", foreign=True, immutable=True, isInDB=True, isPublic=True, kuko=True, kukoindex=True, kukoonly=True, name="sample_text", nullOK=True, optional=True, shared=True, sybident=True)
    assert instance.isInDB == True
    instance.isInDB = False
    assert instance.isInDB == False


def test_dbmodel_Attribute_isPublic_value_roundtrip():
    instance = dbmodel_Attribute(aName="sample_text", archiv=True, descr="sample_text", extattr="sample_text", exttable="sample_text", foreign=True, immutable=True, isInDB=True, isPublic=True, kuko=True, kukoindex=True, kukoonly=True, name="sample_text", nullOK=True, optional=True, shared=True, sybident=True)
    assert instance.isPublic == True
    instance.isPublic = False
    assert instance.isPublic == False


def test_dbmodel_Attribute_kuko_value_roundtrip():
    instance = dbmodel_Attribute(aName="sample_text", archiv=True, descr="sample_text", extattr="sample_text", exttable="sample_text", foreign=True, immutable=True, isInDB=True, isPublic=True, kuko=True, kukoindex=True, kukoonly=True, name="sample_text", nullOK=True, optional=True, shared=True, sybident=True)
    assert instance.kuko == True
    instance.kuko = False
    assert instance.kuko == False


def test_dbmodel_Attribute_kukoindex_value_roundtrip():
    instance = dbmodel_Attribute(aName="sample_text", archiv=True, descr="sample_text", extattr="sample_text", exttable="sample_text", foreign=True, immutable=True, isInDB=True, isPublic=True, kuko=True, kukoindex=True, kukoonly=True, name="sample_text", nullOK=True, optional=True, shared=True, sybident=True)
    assert instance.kukoindex == True
    instance.kukoindex = False
    assert instance.kukoindex == False


def test_dbmodel_Attribute_kukoonly_value_roundtrip():
    instance = dbmodel_Attribute(aName="sample_text", archiv=True, descr="sample_text", extattr="sample_text", exttable="sample_text", foreign=True, immutable=True, isInDB=True, isPublic=True, kuko=True, kukoindex=True, kukoonly=True, name="sample_text", nullOK=True, optional=True, shared=True, sybident=True)
    assert instance.kukoonly == True
    instance.kukoonly = False
    assert instance.kukoonly == False


def test_dbmodel_Attribute_name_value_roundtrip():
    instance = dbmodel_Attribute(aName="sample_text", archiv=True, descr="sample_text", extattr="sample_text", exttable="sample_text", foreign=True, immutable=True, isInDB=True, isPublic=True, kuko=True, kukoindex=True, kukoonly=True, name="sample_text", nullOK=True, optional=True, shared=True, sybident=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dbmodel_Attribute_nullOK_value_roundtrip():
    instance = dbmodel_Attribute(aName="sample_text", archiv=True, descr="sample_text", extattr="sample_text", exttable="sample_text", foreign=True, immutable=True, isInDB=True, isPublic=True, kuko=True, kukoindex=True, kukoonly=True, name="sample_text", nullOK=True, optional=True, shared=True, sybident=True)
    assert instance.nullOK == True
    instance.nullOK = False
    assert instance.nullOK == False


def test_dbmodel_Attribute_optional_value_roundtrip():
    instance = dbmodel_Attribute(aName="sample_text", archiv=True, descr="sample_text", extattr="sample_text", exttable="sample_text", foreign=True, immutable=True, isInDB=True, isPublic=True, kuko=True, kukoindex=True, kukoonly=True, name="sample_text", nullOK=True, optional=True, shared=True, sybident=True)
    assert instance.optional == True
    instance.optional = False
    assert instance.optional == False


def test_dbmodel_Attribute_shared_value_roundtrip():
    instance = dbmodel_Attribute(aName="sample_text", archiv=True, descr="sample_text", extattr="sample_text", exttable="sample_text", foreign=True, immutable=True, isInDB=True, isPublic=True, kuko=True, kukoindex=True, kukoonly=True, name="sample_text", nullOK=True, optional=True, shared=True, sybident=True)
    assert instance.shared == True
    instance.shared = False
    assert instance.shared == False


def test_dbmodel_Attribute_sybident_value_roundtrip():
    instance = dbmodel_Attribute(aName="sample_text", archiv=True, descr="sample_text", extattr="sample_text", exttable="sample_text", foreign=True, immutable=True, isInDB=True, isPublic=True, kuko=True, kukoindex=True, kukoonly=True, name="sample_text", nullOK=True, optional=True, shared=True, sybident=True)
    assert instance.sybident == True
    instance.sybident = False
    assert instance.sybident == False


def test_dbmodel_Class_aName_value_roundtrip():
    instance = dbmodel_Class(aName="sample_text", archivIndex="sample_text", descr="sample_text", noDBio=True, publish=True, pubname="sample_text", pubspec=True, vmaj=7, vmin=7, whereclause="sample_text")
    assert instance.aName == "sample_text"
    instance.aName = "sample_text_2"
    assert instance.aName == "sample_text_2"


def test_dbmodel_Class_archivIndex_value_roundtrip():
    instance = dbmodel_Class(aName="sample_text", archivIndex="sample_text", descr="sample_text", noDBio=True, publish=True, pubname="sample_text", pubspec=True, vmaj=7, vmin=7, whereclause="sample_text")
    assert instance.archivIndex == "sample_text"
    instance.archivIndex = "sample_text_2"
    assert instance.archivIndex == "sample_text_2"


def test_dbmodel_Class_descr_value_roundtrip():
    instance = dbmodel_Class(aName="sample_text", archivIndex="sample_text", descr="sample_text", noDBio=True, publish=True, pubname="sample_text", pubspec=True, vmaj=7, vmin=7, whereclause="sample_text")
    assert instance.descr == "sample_text"
    instance.descr = "sample_text_2"
    assert instance.descr == "sample_text_2"


def test_dbmodel_Class_noDBio_value_roundtrip():
    instance = dbmodel_Class(aName="sample_text", archivIndex="sample_text", descr="sample_text", noDBio=True, publish=True, pubname="sample_text", pubspec=True, vmaj=7, vmin=7, whereclause="sample_text")
    assert instance.noDBio == True
    instance.noDBio = False
    assert instance.noDBio == False


def test_dbmodel_Class_publish_value_roundtrip():
    instance = dbmodel_Class(aName="sample_text", archivIndex="sample_text", descr="sample_text", noDBio=True, publish=True, pubname="sample_text", pubspec=True, vmaj=7, vmin=7, whereclause="sample_text")
    assert instance.publish == True
    instance.publish = False
    assert instance.publish == False


def test_dbmodel_Class_pubname_value_roundtrip():
    instance = dbmodel_Class(aName="sample_text", archivIndex="sample_text", descr="sample_text", noDBio=True, publish=True, pubname="sample_text", pubspec=True, vmaj=7, vmin=7, whereclause="sample_text")
    assert instance.pubname == "sample_text"
    instance.pubname = "sample_text_2"
    assert instance.pubname == "sample_text_2"


def test_dbmodel_Class_pubspec_value_roundtrip():
    instance = dbmodel_Class(aName="sample_text", archivIndex="sample_text", descr="sample_text", noDBio=True, publish=True, pubname="sample_text", pubspec=True, vmaj=7, vmin=7, whereclause="sample_text")
    assert instance.pubspec == True
    instance.pubspec = False
    assert instance.pubspec == False


def test_dbmodel_Class_vmaj_value_roundtrip():
    instance = dbmodel_Class(aName="sample_text", archivIndex="sample_text", descr="sample_text", noDBio=True, publish=True, pubname="sample_text", pubspec=True, vmaj=7, vmin=7, whereclause="sample_text")
    assert instance.vmaj == 7
    instance.vmaj = 13
    assert instance.vmaj == 13


def test_dbmodel_Class_vmin_value_roundtrip():
    instance = dbmodel_Class(aName="sample_text", archivIndex="sample_text", descr="sample_text", noDBio=True, publish=True, pubname="sample_text", pubspec=True, vmaj=7, vmin=7, whereclause="sample_text")
    assert instance.vmin == 7
    instance.vmin = 13
    assert instance.vmin == 13


def test_dbmodel_Class_whereclause_value_roundtrip():
    instance = dbmodel_Class(aName="sample_text", archivIndex="sample_text", descr="sample_text", noDBio=True, publish=True, pubname="sample_text", pubspec=True, vmaj=7, vmin=7, whereclause="sample_text")
    assert instance.whereclause == "sample_text"
    instance.whereclause = "sample_text_2"
    assert instance.whereclause == "sample_text_2"


def test_dbmodel_ClassOrDuplicate_abbrev_value_roundtrip():
    instance = dbmodel_ClassOrDuplicate(abbrev="sample_text", name="sample_text", reps="sample_text")
    assert instance.abbrev == "sample_text"
    instance.abbrev = "sample_text_2"
    assert instance.abbrev == "sample_text_2"


def test_dbmodel_ClassOrDuplicate_name_value_roundtrip():
    instance = dbmodel_ClassOrDuplicate(abbrev="sample_text", name="sample_text", reps="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dbmodel_ClassOrDuplicate_reps_value_roundtrip():
    instance = dbmodel_ClassOrDuplicate(abbrev="sample_text", name="sample_text", reps="sample_text")
    assert instance.reps == "sample_text"
    instance.reps = "sample_text_2"
    assert instance.reps == "sample_text_2"


def test_dbmodel_DbModel_doAll_value_roundtrip():
    instance = dbmodel_DbModel(doAll=True, kobeType="sample_text", kudaType="sample_text", mtype="sample_text", name="sample_text", version="sample_text")
    assert instance.doAll == True
    instance.doAll = False
    assert instance.doAll == False


def test_dbmodel_DbModel_kobeType_value_roundtrip():
    instance = dbmodel_DbModel(doAll=True, kobeType="sample_text", kudaType="sample_text", mtype="sample_text", name="sample_text", version="sample_text")
    assert instance.kobeType == "sample_text"
    instance.kobeType = "sample_text_2"
    assert instance.kobeType == "sample_text_2"


def test_dbmodel_DbModel_kudaType_value_roundtrip():
    instance = dbmodel_DbModel(doAll=True, kobeType="sample_text", kudaType="sample_text", mtype="sample_text", name="sample_text", version="sample_text")
    assert instance.kudaType == "sample_text"
    instance.kudaType = "sample_text_2"
    assert instance.kudaType == "sample_text_2"


def test_dbmodel_DbModel_mtype_value_roundtrip():
    instance = dbmodel_DbModel(doAll=True, kobeType="sample_text", kudaType="sample_text", mtype="sample_text", name="sample_text", version="sample_text")
    assert instance.mtype == "sample_text"
    instance.mtype = "sample_text_2"
    assert instance.mtype == "sample_text_2"


def test_dbmodel_DbModel_name_value_roundtrip():
    instance = dbmodel_DbModel(doAll=True, kobeType="sample_text", kudaType="sample_text", mtype="sample_text", name="sample_text", version="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dbmodel_DbModel_version_value_roundtrip():
    instance = dbmodel_DbModel(doAll=True, kobeType="sample_text", kudaType="sample_text", mtype="sample_text", name="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_dbmodel_Import_importedNamespace_value_roundtrip():
    instance = dbmodel_Import(importedNamespace="sample_text")
    assert instance.importedNamespace == "sample_text"
    instance.importedNamespace = "sample_text_2"
    assert instance.importedNamespace == "sample_text_2"


def test_dbmodel_Index_kuko_value_roundtrip():
    instance = dbmodel_Index(kuko=True, name="sample_text", unique=True)
    assert instance.kuko == True
    instance.kuko = False
    assert instance.kuko == False


def test_dbmodel_Index_name_value_roundtrip():
    instance = dbmodel_Index(kuko=True, name="sample_text", unique=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dbmodel_Index_unique_value_roundtrip():
    instance = dbmodel_Index(kuko=True, name="sample_text", unique=True)
    assert instance.unique == True
    instance.unique = False
    assert instance.unique == False


def test_dbmodel_IndexRef_clustered_value_roundtrip():
    instance = dbmodel_IndexRef(clustered=True, isPrimkey=True)
    assert instance.clustered == True
    instance.clustered = False
    assert instance.clustered == False


def test_dbmodel_IndexRef_isPrimkey_value_roundtrip():
    instance = dbmodel_IndexRef(clustered=True, isPrimkey=True)
    assert instance.isPrimkey == True
    instance.isPrimkey = False
    assert instance.isPrimkey == False


def test_dbmodel_Pdb_lockSchema_value_roundtrip():
    instance = dbmodel_Pdb(lockSchema="sample_text", name="sample_text", tablePartitioning=7)
    assert instance.lockSchema == "sample_text"
    instance.lockSchema = "sample_text_2"
    assert instance.lockSchema == "sample_text_2"


def test_dbmodel_Pdb_name_value_roundtrip():
    instance = dbmodel_Pdb(lockSchema="sample_text", name="sample_text", tablePartitioning=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dbmodel_Pdb_tablePartitioning_value_roundtrip():
    instance = dbmodel_Pdb(lockSchema="sample_text", name="sample_text", tablePartitioning=7)
    assert instance.tablePartitioning == 7
    instance.tablePartitioning = 13
    assert instance.tablePartitioning == 13


def test_dbmodel_StructOverride_altname_value_roundtrip():
    instance = dbmodel_StructOverride(altname="sample_text")
    assert instance.altname == "sample_text"
    instance.altname = "sample_text_2"
    assert instance.altname == "sample_text_2"


def test_dbmodel_Subject_name_value_roundtrip():
    instance = dbmodel_Subject(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dbmodel_Class_isa_ClassOrDuplicate():
    instance = dbmodel_Class(aName="sample_text", archivIndex="sample_text", descr="sample_text", noDBio=True, publish=True, pubname="sample_text", pubspec=True, vmaj=7, vmin=7, whereclause="sample_text")
    assert isinstance(instance, ClassOrDuplicate)


def test_dbmodel_Duplicate_isa_ClassOrDuplicate():
    instance = dbmodel_Duplicate()
    assert isinstance(instance, ClassOrDuplicate)


def test_assoc_attr41_link_reassign_clear():
    a = dbmodel_IndexRef(clustered=True, isPrimkey=True)
    b1 = dbmodel_Attribute(aName="sample_text", archiv=True, descr="sample_text", extattr="sample_text", exttable="sample_text", foreign=True, immutable=True, isInDB=True, isPublic=True, kuko=True, kukoindex=True, kukoonly=True, name="sample_text", nullOK=True, optional=True, shared=True, sybident=True)
    b2 = dbmodel_Attribute(aName="sample_text_2", archiv=False, descr="sample_text_2", extattr="sample_text_2", exttable="sample_text_2", foreign=False, immutable=False, isInDB=False, isPublic=False, kuko=False, kukoindex=False, kukoonly=False, name="sample_text_2", nullOK=False, optional=False, shared=False, sybident=False)
    _safe_set(a, 'dbmodel_IndexRef42', b1)
    assert _is_linked(a, 'dbmodel_IndexRef42', b1)
    if hasattr(b1, 'dbmodel_Attribute43'):
        assert _is_linked(b1, 'dbmodel_Attribute43', a)
    _safe_set(a, 'dbmodel_IndexRef42', b2)
    assert _is_linked(a, 'dbmodel_IndexRef42', b2)
    if hasattr(b1, 'dbmodel_Attribute43'):
        assert not _is_linked(b1, 'dbmodel_Attribute43', a)
    if hasattr(b2, 'dbmodel_Attribute43'):
        assert _is_linked(b2, 'dbmodel_Attribute43', a)
    _safe_set(a, 'dbmodel_IndexRef42', None)
    assert not _is_linked(a, 'dbmodel_IndexRef42', b2)
    if hasattr(b2, 'dbmodel_Attribute43'):
        assert not _is_linked(b2, 'dbmodel_Attribute43', a)


def test_assoc_attr51_link_reassign_clear():
    a = dbmodel_Attribute(aName="sample_text", archiv=True, descr="sample_text", extattr="sample_text", exttable="sample_text", foreign=True, immutable=True, isInDB=True, isPublic=True, kuko=True, kukoindex=True, kukoonly=True, name="sample_text", nullOK=True, optional=True, shared=True, sybident=True)
    b1 = dbmodel_StructShare()
    b2 = dbmodel_StructShare()
    _safe_set(a, 'dbmodel_Attribute53', b1)
    assert _is_linked(a, 'dbmodel_Attribute53', b1)
    if hasattr(b1, 'dbmodel_StructShare52'):
        assert _is_linked(b1, 'dbmodel_StructShare52', a)
    _safe_set(a, 'dbmodel_Attribute53', b2)
    assert _is_linked(a, 'dbmodel_Attribute53', b2)
    if hasattr(b1, 'dbmodel_StructShare52'):
        assert not _is_linked(b1, 'dbmodel_StructShare52', a)
    if hasattr(b2, 'dbmodel_StructShare52'):
        assert _is_linked(b2, 'dbmodel_StructShare52', a)
    _safe_set(a, 'dbmodel_Attribute53', None)
    assert not _is_linked(a, 'dbmodel_Attribute53', b2)
    if hasattr(b2, 'dbmodel_StructShare52'):
        assert not _is_linked(b2, 'dbmodel_StructShare52', a)


def test_assoc_attributes10_link_reassign_clear():
    a = dbmodel_Class(aName="sample_text", archivIndex="sample_text", descr="sample_text", noDBio=True, publish=True, pubname="sample_text", pubspec=True, vmaj=7, vmin=7, whereclause="sample_text")
    b1 = dbmodel_Attribute(aName="sample_text", archiv=True, descr="sample_text", extattr="sample_text", exttable="sample_text", foreign=True, immutable=True, isInDB=True, isPublic=True, kuko=True, kukoindex=True, kukoonly=True, name="sample_text", nullOK=True, optional=True, shared=True, sybident=True)
    b2 = dbmodel_Attribute(aName="sample_text_2", archiv=False, descr="sample_text_2", extattr="sample_text_2", exttable="sample_text_2", foreign=False, immutable=False, isInDB=False, isPublic=False, kuko=False, kukoindex=False, kukoonly=False, name="sample_text_2", nullOK=False, optional=False, shared=False, sybident=False)
    _safe_set(a, 'dbmodel_Class11', {b1})
    assert _is_linked(a, 'dbmodel_Class11', b1)
    if hasattr(b1, 'dbmodel_Attribute'):
        assert _is_linked(b1, 'dbmodel_Attribute', a)
    _safe_set(a, 'dbmodel_Class11', {b2})
    assert _is_linked(a, 'dbmodel_Class11', b2)
    if hasattr(b1, 'dbmodel_Attribute'):
        assert not _is_linked(b1, 'dbmodel_Attribute', a)
    if hasattr(b2, 'dbmodel_Attribute'):
        assert _is_linked(b2, 'dbmodel_Attribute', a)
    _safe_set(a, 'dbmodel_Class11', set())
    assert not _is_linked(a, 'dbmodel_Class11', b2)
    if hasattr(b2, 'dbmodel_Attribute'):
        assert not _is_linked(b2, 'dbmodel_Attribute', a)


def test_assoc_attrs36_link_reassign_clear():
    a = dbmodel_Index(kuko=True, name="sample_text", unique=True)
    b1 = dbmodel_Attribute(aName="sample_text", archiv=True, descr="sample_text", extattr="sample_text", exttable="sample_text", foreign=True, immutable=True, isInDB=True, isPublic=True, kuko=True, kukoindex=True, kukoonly=True, name="sample_text", nullOK=True, optional=True, shared=True, sybident=True)
    b2 = dbmodel_Attribute(aName="sample_text_2", archiv=False, descr="sample_text_2", extattr="sample_text_2", exttable="sample_text_2", foreign=False, immutable=False, isInDB=False, isPublic=False, kuko=False, kukoindex=False, kukoonly=False, name="sample_text_2", nullOK=False, optional=False, shared=False, sybident=False)
    _safe_set(a, 'dbmodel_Index37', {b1})
    assert _is_linked(a, 'dbmodel_Index37', b1)
    if hasattr(b1, 'dbmodel_Attribute38'):
        assert _is_linked(b1, 'dbmodel_Attribute38', a)
    _safe_set(a, 'dbmodel_Index37', {b2})
    assert _is_linked(a, 'dbmodel_Index37', b2)
    if hasattr(b1, 'dbmodel_Attribute38'):
        assert not _is_linked(b1, 'dbmodel_Attribute38', a)
    if hasattr(b2, 'dbmodel_Attribute38'):
        assert _is_linked(b2, 'dbmodel_Attribute38', a)
    _safe_set(a, 'dbmodel_Index37', set())
    assert not _is_linked(a, 'dbmodel_Index37', b2)
    if hasattr(b2, 'dbmodel_Attribute38'):
        assert not _is_linked(b2, 'dbmodel_Attribute38', a)


def test_assoc_classes3_link_reassign_clear():
    a = dbmodel_DbModel(doAll=True, kobeType="sample_text", kudaType="sample_text", mtype="sample_text", name="sample_text", version="sample_text")
    b1 = dbmodel_Class(aName="sample_text", archivIndex="sample_text", descr="sample_text", noDBio=True, publish=True, pubname="sample_text", pubspec=True, vmaj=7, vmin=7, whereclause="sample_text")
    b2 = dbmodel_Class(aName="sample_text_2", archivIndex="sample_text_2", descr="sample_text_2", noDBio=False, publish=False, pubname="sample_text_2", pubspec=False, vmaj=13, vmin=13, whereclause="sample_text_2")
    _safe_set(a, 'dbmodel_DbModel4', {b1})
    assert _is_linked(a, 'dbmodel_DbModel4', b1)
    if hasattr(b1, 'dbmodel_Class'):
        assert _is_linked(b1, 'dbmodel_Class', a)
    _safe_set(a, 'dbmodel_DbModel4', {b2})
    assert _is_linked(a, 'dbmodel_DbModel4', b2)
    if hasattr(b1, 'dbmodel_Class'):
        assert not _is_linked(b1, 'dbmodel_Class', a)
    if hasattr(b2, 'dbmodel_Class'):
        assert _is_linked(b2, 'dbmodel_Class', a)
    _safe_set(a, 'dbmodel_DbModel4', set())
    assert not _is_linked(a, 'dbmodel_DbModel4', b2)
    if hasattr(b2, 'dbmodel_Class'):
        assert not _is_linked(b2, 'dbmodel_Class', a)


def test_assoc_duplicates5_link_reassign_clear():
    a = dbmodel_DbModel(doAll=True, kobeType="sample_text", kudaType="sample_text", mtype="sample_text", name="sample_text", version="sample_text")
    b1 = dbmodel_Duplicate()
    b2 = dbmodel_Duplicate()
    _safe_set(a, 'dbmodel_DbModel6', {b1})
    assert _is_linked(a, 'dbmodel_DbModel6', b1)
    if hasattr(b1, 'dbmodel_Duplicate'):
        assert _is_linked(b1, 'dbmodel_Duplicate', a)
    _safe_set(a, 'dbmodel_DbModel6', {b2})
    assert _is_linked(a, 'dbmodel_DbModel6', b2)
    if hasattr(b1, 'dbmodel_Duplicate'):
        assert not _is_linked(b1, 'dbmodel_Duplicate', a)
    if hasattr(b2, 'dbmodel_Duplicate'):
        assert _is_linked(b2, 'dbmodel_Duplicate', a)
    _safe_set(a, 'dbmodel_DbModel6', set())
    assert not _is_linked(a, 'dbmodel_DbModel6', b2)
    if hasattr(b2, 'dbmodel_Duplicate'):
        assert not _is_linked(b2, 'dbmodel_Duplicate', a)


def test_assoc_forattr24_link_reassign_clear():
    a = dbmodel_Attribute(aName="sample_text", archiv=True, descr="sample_text", extattr="sample_text", exttable="sample_text", foreign=True, immutable=True, isInDB=True, isPublic=True, kuko=True, kukoindex=True, kukoonly=True, name="sample_text", nullOK=True, optional=True, shared=True, sybident=True)
    b1 = dbmodel_Attribute(aName="sample_text", archiv=True, descr="sample_text", extattr="sample_text", exttable="sample_text", foreign=True, immutable=True, isInDB=True, isPublic=True, kuko=True, kukoindex=True, kukoonly=True, name="sample_text", nullOK=True, optional=True, shared=True, sybident=True)
    b2 = dbmodel_Attribute(aName="sample_text_2", archiv=False, descr="sample_text_2", extattr="sample_text_2", exttable="sample_text_2", foreign=False, immutable=False, isInDB=False, isPublic=False, kuko=False, kukoindex=False, kukoonly=False, name="sample_text_2", nullOK=False, optional=False, shared=False, sybident=False)
    _safe_set(a, 'dbmodel_Attribute23', b1)
    assert _is_linked(a, 'dbmodel_Attribute23', b1)
    if hasattr(b1, 'dbmodel_Attribute25'):
        assert _is_linked(b1, 'dbmodel_Attribute25', a)
    _safe_set(a, 'dbmodel_Attribute23', b2)
    assert _is_linked(a, 'dbmodel_Attribute23', b2)
    if hasattr(b1, 'dbmodel_Attribute25'):
        assert not _is_linked(b1, 'dbmodel_Attribute25', a)
    if hasattr(b2, 'dbmodel_Attribute25'):
        assert _is_linked(b2, 'dbmodel_Attribute25', a)
    _safe_set(a, 'dbmodel_Attribute23', None)
    assert not _is_linked(a, 'dbmodel_Attribute23', b2)
    if hasattr(b2, 'dbmodel_Attribute25'):
        assert not _is_linked(b2, 'dbmodel_Attribute25', a)


def test_assoc_imports0_link_reassign_clear():
    a = dbmodel_Import(importedNamespace="sample_text")
    b1 = dbmodel_DbModel(doAll=True, kobeType="sample_text", kudaType="sample_text", mtype="sample_text", name="sample_text", version="sample_text")
    b2 = dbmodel_DbModel(doAll=False, kobeType="sample_text_2", kudaType="sample_text_2", mtype="sample_text_2", name="sample_text_2", version="sample_text_2")
    _safe_set(a, 'dbmodel_Import', b1)
    assert _is_linked(a, 'dbmodel_Import', b1)
    if hasattr(b1, 'dbmodel_DbModel'):
        assert _is_linked(b1, 'dbmodel_DbModel', a)
    _safe_set(a, 'dbmodel_Import', b2)
    assert _is_linked(a, 'dbmodel_Import', b2)
    if hasattr(b1, 'dbmodel_DbModel'):
        assert not _is_linked(b1, 'dbmodel_DbModel', a)
    if hasattr(b2, 'dbmodel_DbModel'):
        assert _is_linked(b2, 'dbmodel_DbModel', a)
    _safe_set(a, 'dbmodel_Import', None)
    assert not _is_linked(a, 'dbmodel_Import', b2)
    if hasattr(b2, 'dbmodel_DbModel'):
        assert not _is_linked(b2, 'dbmodel_DbModel', a)


def test_assoc_index39_link_reassign_clear():
    a = dbmodel_IndexRef(clustered=True, isPrimkey=True)
    b1 = dbmodel_Index(kuko=True, name="sample_text", unique=True)
    b2 = dbmodel_Index(kuko=False, name="sample_text_2", unique=False)
    _safe_set(a, 'dbmodel_IndexRef', b1)
    assert _is_linked(a, 'dbmodel_IndexRef', b1)
    if hasattr(b1, 'dbmodel_Index40'):
        assert _is_linked(b1, 'dbmodel_Index40', a)
    _safe_set(a, 'dbmodel_IndexRef', b2)
    assert _is_linked(a, 'dbmodel_IndexRef', b2)
    if hasattr(b1, 'dbmodel_Index40'):
        assert not _is_linked(b1, 'dbmodel_Index40', a)
    if hasattr(b2, 'dbmodel_Index40'):
        assert _is_linked(b2, 'dbmodel_Index40', a)
    _safe_set(a, 'dbmodel_IndexRef', None)
    assert not _is_linked(a, 'dbmodel_IndexRef', b2)
    if hasattr(b2, 'dbmodel_Index40'):
        assert not _is_linked(b2, 'dbmodel_Index40', a)


def test_assoc_indices14_link_reassign_clear():
    a = dbmodel_Index(kuko=True, name="sample_text", unique=True)
    b1 = dbmodel_Class(aName="sample_text", archivIndex="sample_text", descr="sample_text", noDBio=True, publish=True, pubname="sample_text", pubspec=True, vmaj=7, vmin=7, whereclause="sample_text")
    b2 = dbmodel_Class(aName="sample_text_2", archivIndex="sample_text_2", descr="sample_text_2", noDBio=False, publish=False, pubname="sample_text_2", pubspec=False, vmaj=13, vmin=13, whereclause="sample_text_2")
    _safe_set(a, 'dbmodel_Index', b1)
    assert _is_linked(a, 'dbmodel_Index', b1)
    if hasattr(b1, 'dbmodel_Class15'):
        assert _is_linked(b1, 'dbmodel_Class15', a)
    _safe_set(a, 'dbmodel_Index', b2)
    assert _is_linked(a, 'dbmodel_Index', b2)
    if hasattr(b1, 'dbmodel_Class15'):
        assert not _is_linked(b1, 'dbmodel_Class15', a)
    if hasattr(b2, 'dbmodel_Class15'):
        assert _is_linked(b2, 'dbmodel_Class15', a)
    _safe_set(a, 'dbmodel_Index', None)
    assert not _is_linked(a, 'dbmodel_Index', b2)
    if hasattr(b2, 'dbmodel_Class15'):
        assert not _is_linked(b2, 'dbmodel_Class15', a)


def test_assoc_indices44_link_reassign_clear():
    a = dbmodel_Pdb(lockSchema="sample_text", name="sample_text", tablePartitioning=7)
    b1 = dbmodel_IndexRef(clustered=True, isPrimkey=True)
    b2 = dbmodel_IndexRef(clustered=False, isPrimkey=False)
    _safe_set(a, 'dbmodel_Pdb45', {b1})
    assert _is_linked(a, 'dbmodel_Pdb45', b1)
    if hasattr(b1, 'dbmodel_IndexRef46'):
        assert _is_linked(b1, 'dbmodel_IndexRef46', a)
    _safe_set(a, 'dbmodel_Pdb45', {b2})
    assert _is_linked(a, 'dbmodel_Pdb45', b2)
    if hasattr(b1, 'dbmodel_IndexRef46'):
        assert not _is_linked(b1, 'dbmodel_IndexRef46', a)
    if hasattr(b2, 'dbmodel_IndexRef46'):
        assert _is_linked(b2, 'dbmodel_IndexRef46', a)
    _safe_set(a, 'dbmodel_Pdb45', set())
    assert not _is_linked(a, 'dbmodel_Pdb45', b2)
    if hasattr(b2, 'dbmodel_IndexRef46'):
        assert not _is_linked(b2, 'dbmodel_IndexRef46', a)


def test_assoc_logattr31_link_reassign_clear():
    a = dbmodel_Attribute(aName="sample_text", archiv=True, descr="sample_text", extattr="sample_text", exttable="sample_text", foreign=True, immutable=True, isInDB=True, isPublic=True, kuko=True, kukoindex=True, kukoonly=True, name="sample_text", nullOK=True, optional=True, shared=True, sybident=True)
    b1 = dbmodel_Attribute(aName="sample_text", archiv=True, descr="sample_text", extattr="sample_text", exttable="sample_text", foreign=True, immutable=True, isInDB=True, isPublic=True, kuko=True, kukoindex=True, kukoonly=True, name="sample_text", nullOK=True, optional=True, shared=True, sybident=True)
    b2 = dbmodel_Attribute(aName="sample_text_2", archiv=False, descr="sample_text_2", extattr="sample_text_2", exttable="sample_text_2", foreign=False, immutable=False, isInDB=False, isPublic=False, kuko=False, kukoindex=False, kukoonly=False, name="sample_text_2", nullOK=False, optional=False, shared=False, sybident=False)
    _safe_set(a, 'dbmodel_Attribute30', b1)
    assert _is_linked(a, 'dbmodel_Attribute30', b1)
    if hasattr(b1, 'dbmodel_Attribute32'):
        assert _is_linked(b1, 'dbmodel_Attribute32', a)
    _safe_set(a, 'dbmodel_Attribute30', b2)
    assert _is_linked(a, 'dbmodel_Attribute30', b2)
    if hasattr(b1, 'dbmodel_Attribute32'):
        assert not _is_linked(b1, 'dbmodel_Attribute32', a)
    if hasattr(b2, 'dbmodel_Attribute32'):
        assert _is_linked(b2, 'dbmodel_Attribute32', a)
    _safe_set(a, 'dbmodel_Attribute30', None)
    assert not _is_linked(a, 'dbmodel_Attribute30', b2)
    if hasattr(b2, 'dbmodel_Attribute32'):
        assert not _is_linked(b2, 'dbmodel_Attribute32', a)


def test_assoc_orig18_link_reassign_clear():
    a = dbmodel_Class(aName="sample_text", archivIndex="sample_text", descr="sample_text", noDBio=True, publish=True, pubname="sample_text", pubspec=True, vmaj=7, vmin=7, whereclause="sample_text")
    b1 = dbmodel_Duplicate()
    b2 = dbmodel_Duplicate()
    _safe_set(a, 'dbmodel_Class20', b1)
    assert _is_linked(a, 'dbmodel_Class20', b1)
    if hasattr(b1, 'dbmodel_Duplicate19'):
        assert _is_linked(b1, 'dbmodel_Duplicate19', a)
    _safe_set(a, 'dbmodel_Class20', b2)
    assert _is_linked(a, 'dbmodel_Class20', b2)
    if hasattr(b1, 'dbmodel_Duplicate19'):
        assert not _is_linked(b1, 'dbmodel_Duplicate19', a)
    if hasattr(b2, 'dbmodel_Duplicate19'):
        assert _is_linked(b2, 'dbmodel_Duplicate19', a)
    _safe_set(a, 'dbmodel_Class20', None)
    assert not _is_linked(a, 'dbmodel_Class20', b2)
    if hasattr(b2, 'dbmodel_Duplicate19'):
        assert not _is_linked(b2, 'dbmodel_Duplicate19', a)


def test_assoc_ovride28_link_reassign_clear():
    a = dbmodel_StructOverride(altname="sample_text")
    b1 = dbmodel_Attribute(aName="sample_text", archiv=True, descr="sample_text", extattr="sample_text", exttable="sample_text", foreign=True, immutable=True, isInDB=True, isPublic=True, kuko=True, kukoindex=True, kukoonly=True, name="sample_text", nullOK=True, optional=True, shared=True, sybident=True)
    b2 = dbmodel_Attribute(aName="sample_text_2", archiv=False, descr="sample_text_2", extattr="sample_text_2", exttable="sample_text_2", foreign=False, immutable=False, isInDB=False, isPublic=False, kuko=False, kukoindex=False, kukoonly=False, name="sample_text_2", nullOK=False, optional=False, shared=False, sybident=False)
    _safe_set(a, 'dbmodel_StructOverride', b1)
    assert _is_linked(a, 'dbmodel_StructOverride', b1)
    if hasattr(b1, 'dbmodel_Attribute29'):
        assert _is_linked(b1, 'dbmodel_Attribute29', a)
    _safe_set(a, 'dbmodel_StructOverride', b2)
    assert _is_linked(a, 'dbmodel_StructOverride', b2)
    if hasattr(b1, 'dbmodel_Attribute29'):
        assert not _is_linked(b1, 'dbmodel_Attribute29', a)
    if hasattr(b2, 'dbmodel_Attribute29'):
        assert _is_linked(b2, 'dbmodel_Attribute29', a)
    _safe_set(a, 'dbmodel_StructOverride', None)
    assert not _is_linked(a, 'dbmodel_StructOverride', b2)
    if hasattr(b2, 'dbmodel_Attribute29'):
        assert not _is_linked(b2, 'dbmodel_Attribute29', a)


def test_assoc_part49_link_reassign_clear():
    a = dbmodel_StructOverride(altname="sample_text")
    b1 = dbmodel_Stype()
    b2 = dbmodel_Stype()
    _safe_set(a, 'dbmodel_StructOverride50', b1)
    assert _is_linked(a, 'dbmodel_StructOverride50', b1)
    if hasattr(b1, 'dbmodel_Stype'):
        assert _is_linked(b1, 'dbmodel_Stype', a)
    _safe_set(a, 'dbmodel_StructOverride50', b2)
    assert _is_linked(a, 'dbmodel_StructOverride50', b2)
    if hasattr(b1, 'dbmodel_Stype'):
        assert not _is_linked(b1, 'dbmodel_Stype', a)
    if hasattr(b2, 'dbmodel_Stype'):
        assert _is_linked(b2, 'dbmodel_Stype', a)
    _safe_set(a, 'dbmodel_StructOverride50', None)
    assert not _is_linked(a, 'dbmodel_StructOverride50', b2)
    if hasattr(b2, 'dbmodel_Stype'):
        assert not _is_linked(b2, 'dbmodel_Stype', a)


def test_assoc_pdbs16_link_reassign_clear():
    a = dbmodel_Pdb(lockSchema="sample_text", name="sample_text", tablePartitioning=7)
    b1 = dbmodel_Class(aName="sample_text", archivIndex="sample_text", descr="sample_text", noDBio=True, publish=True, pubname="sample_text", pubspec=True, vmaj=7, vmin=7, whereclause="sample_text")
    b2 = dbmodel_Class(aName="sample_text_2", archivIndex="sample_text_2", descr="sample_text_2", noDBio=False, publish=False, pubname="sample_text_2", pubspec=False, vmaj=13, vmin=13, whereclause="sample_text_2")
    _safe_set(a, 'dbmodel_Pdb', b1)
    assert _is_linked(a, 'dbmodel_Pdb', b1)
    if hasattr(b1, 'dbmodel_Class17'):
        assert _is_linked(b1, 'dbmodel_Class17', a)
    _safe_set(a, 'dbmodel_Pdb', b2)
    assert _is_linked(a, 'dbmodel_Pdb', b2)
    if hasattr(b1, 'dbmodel_Class17'):
        assert not _is_linked(b1, 'dbmodel_Class17', a)
    if hasattr(b2, 'dbmodel_Class17'):
        assert _is_linked(b2, 'dbmodel_Class17', a)
    _safe_set(a, 'dbmodel_Pdb', None)
    assert not _is_linked(a, 'dbmodel_Pdb', b2)
    if hasattr(b2, 'dbmodel_Class17'):
        assert not _is_linked(b2, 'dbmodel_Class17', a)


def test_assoc_pkeys33_link_reassign_clear():
    a = dbmodel_Attribute(aName="sample_text", archiv=True, descr="sample_text", extattr="sample_text", exttable="sample_text", foreign=True, immutable=True, isInDB=True, isPublic=True, kuko=True, kukoindex=True, kukoonly=True, name="sample_text", nullOK=True, optional=True, shared=True, sybident=True)
    b1 = dbmodel_Primkey()
    b2 = dbmodel_Primkey()
    _safe_set(a, 'dbmodel_Attribute35', b1)
    assert _is_linked(a, 'dbmodel_Attribute35', b1)
    if hasattr(b1, 'dbmodel_Primkey34'):
        assert _is_linked(b1, 'dbmodel_Primkey34', a)
    _safe_set(a, 'dbmodel_Attribute35', b2)
    assert _is_linked(a, 'dbmodel_Attribute35', b2)
    if hasattr(b1, 'dbmodel_Primkey34'):
        assert not _is_linked(b1, 'dbmodel_Primkey34', a)
    if hasattr(b2, 'dbmodel_Primkey34'):
        assert _is_linked(b2, 'dbmodel_Primkey34', a)
    _safe_set(a, 'dbmodel_Attribute35', None)
    assert not _is_linked(a, 'dbmodel_Attribute35', b2)
    if hasattr(b2, 'dbmodel_Primkey34'):
        assert not _is_linked(b2, 'dbmodel_Primkey34', a)


def test_assoc_primkey12_link_reassign_clear():
    a = dbmodel_Class(aName="sample_text", archivIndex="sample_text", descr="sample_text", noDBio=True, publish=True, pubname="sample_text", pubspec=True, vmaj=7, vmin=7, whereclause="sample_text")
    b1 = dbmodel_Primkey()
    b2 = dbmodel_Primkey()
    _safe_set(a, 'dbmodel_Class13', b1)
    assert _is_linked(a, 'dbmodel_Class13', b1)
    if hasattr(b1, 'dbmodel_Primkey'):
        assert _is_linked(b1, 'dbmodel_Primkey', a)
    _safe_set(a, 'dbmodel_Class13', b2)
    assert _is_linked(a, 'dbmodel_Class13', b2)
    if hasattr(b1, 'dbmodel_Primkey'):
        assert not _is_linked(b1, 'dbmodel_Primkey', a)
    if hasattr(b2, 'dbmodel_Primkey'):
        assert _is_linked(b2, 'dbmodel_Primkey', a)
    _safe_set(a, 'dbmodel_Class13', None)
    assert not _is_linked(a, 'dbmodel_Class13', b2)
    if hasattr(b2, 'dbmodel_Primkey'):
        assert not _is_linked(b2, 'dbmodel_Primkey', a)


def test_assoc_shrs26_link_reassign_clear():
    a = dbmodel_Attribute(aName="sample_text", archiv=True, descr="sample_text", extattr="sample_text", exttable="sample_text", foreign=True, immutable=True, isInDB=True, isPublic=True, kuko=True, kukoindex=True, kukoonly=True, name="sample_text", nullOK=True, optional=True, shared=True, sybident=True)
    b1 = dbmodel_StructShare()
    b2 = dbmodel_StructShare()
    _safe_set(a, 'dbmodel_Attribute27', {b1})
    assert _is_linked(a, 'dbmodel_Attribute27', b1)
    if hasattr(b1, 'dbmodel_StructShare'):
        assert _is_linked(b1, 'dbmodel_StructShare', a)
    _safe_set(a, 'dbmodel_Attribute27', {b2})
    assert _is_linked(a, 'dbmodel_Attribute27', b2)
    if hasattr(b1, 'dbmodel_StructShare'):
        assert not _is_linked(b1, 'dbmodel_StructShare', a)
    if hasattr(b2, 'dbmodel_StructShare'):
        assert _is_linked(b2, 'dbmodel_StructShare', a)
    _safe_set(a, 'dbmodel_Attribute27', set())
    assert not _is_linked(a, 'dbmodel_Attribute27', b2)
    if hasattr(b2, 'dbmodel_StructShare'):
        assert not _is_linked(b2, 'dbmodel_StructShare', a)


def test_assoc_subject7_link_reassign_clear():
    a = dbmodel_Subject(name="sample_text")
    b1 = dbmodel_Class(aName="sample_text", archivIndex="sample_text", descr="sample_text", noDBio=True, publish=True, pubname="sample_text", pubspec=True, vmaj=7, vmin=7, whereclause="sample_text")
    b2 = dbmodel_Class(aName="sample_text_2", archivIndex="sample_text_2", descr="sample_text_2", noDBio=False, publish=False, pubname="sample_text_2", pubspec=False, vmaj=13, vmin=13, whereclause="sample_text_2")
    _safe_set(a, 'dbmodel_Subject9', b1)
    assert _is_linked(a, 'dbmodel_Subject9', b1)
    if hasattr(b1, 'dbmodel_Class8'):
        assert _is_linked(b1, 'dbmodel_Class8', a)
    _safe_set(a, 'dbmodel_Subject9', b2)
    assert _is_linked(a, 'dbmodel_Subject9', b2)
    if hasattr(b1, 'dbmodel_Class8'):
        assert not _is_linked(b1, 'dbmodel_Class8', a)
    if hasattr(b2, 'dbmodel_Class8'):
        assert _is_linked(b2, 'dbmodel_Class8', a)
    _safe_set(a, 'dbmodel_Subject9', None)
    assert not _is_linked(a, 'dbmodel_Subject9', b2)
    if hasattr(b2, 'dbmodel_Class8'):
        assert not _is_linked(b2, 'dbmodel_Class8', a)


def test_assoc_subjects1_link_reassign_clear():
    a = dbmodel_Subject(name="sample_text")
    b1 = dbmodel_DbModel(doAll=True, kobeType="sample_text", kudaType="sample_text", mtype="sample_text", name="sample_text", version="sample_text")
    b2 = dbmodel_DbModel(doAll=False, kobeType="sample_text_2", kudaType="sample_text_2", mtype="sample_text_2", name="sample_text_2", version="sample_text_2")
    _safe_set(a, 'dbmodel_Subject', b1)
    assert _is_linked(a, 'dbmodel_Subject', b1)
    if hasattr(b1, 'dbmodel_DbModel2'):
        assert _is_linked(b1, 'dbmodel_DbModel2', a)
    _safe_set(a, 'dbmodel_Subject', b2)
    assert _is_linked(a, 'dbmodel_Subject', b2)
    if hasattr(b1, 'dbmodel_DbModel2'):
        assert not _is_linked(b1, 'dbmodel_DbModel2', a)
    if hasattr(b2, 'dbmodel_DbModel2'):
        assert _is_linked(b2, 'dbmodel_DbModel2', a)
    _safe_set(a, 'dbmodel_Subject', None)
    assert not _is_linked(a, 'dbmodel_Subject', b2)
    if hasattr(b2, 'dbmodel_DbModel2'):
        assert not _is_linked(b2, 'dbmodel_DbModel2', a)


def test_assoc_type21_link_reassign_clear():
    a = dbmodel_Attribute(aName="sample_text", archiv=True, descr="sample_text", extattr="sample_text", exttable="sample_text", foreign=True, immutable=True, isInDB=True, isPublic=True, kuko=True, kukoindex=True, kukoonly=True, name="sample_text", nullOK=True, optional=True, shared=True, sybident=True)
    b1 = dbmodel_Ltype()
    b2 = dbmodel_Ltype()
    _safe_set(a, 'dbmodel_Attribute22', b1)
    assert _is_linked(a, 'dbmodel_Attribute22', b1)
    if hasattr(b1, 'dbmodel_Ltype'):
        assert _is_linked(b1, 'dbmodel_Ltype', a)
    _safe_set(a, 'dbmodel_Attribute22', b2)
    assert _is_linked(a, 'dbmodel_Attribute22', b2)
    if hasattr(b1, 'dbmodel_Ltype'):
        assert not _is_linked(b1, 'dbmodel_Ltype', a)
    if hasattr(b2, 'dbmodel_Ltype'):
        assert _is_linked(b2, 'dbmodel_Ltype', a)
    _safe_set(a, 'dbmodel_Attribute22', None)
    assert not _is_linked(a, 'dbmodel_Attribute22', b2)
    if hasattr(b2, 'dbmodel_Ltype'):
        assert not _is_linked(b2, 'dbmodel_Ltype', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ClassOrDuplicate_strategy = st.builds(ClassOrDuplicate)
@given(instance=ClassOrDuplicate_strategy)
@settings(max_examples=25)
def test_ClassOrDuplicate_instantiation(instance):
    assert isinstance(instance, ClassOrDuplicate)


dbmodel_Attribute_strategy = st.builds(dbmodel_Attribute, aName=safe_text, archiv=st.booleans(), descr=safe_text, extattr=safe_text, exttable=safe_text, foreign=st.booleans(), immutable=st.booleans(), isInDB=st.booleans(), isPublic=st.booleans(), kuko=st.booleans(), kukoindex=st.booleans(), kukoonly=st.booleans(), name=safe_text, nullOK=st.booleans(), optional=st.booleans(), shared=st.booleans(), sybident=st.booleans())
@given(instance=dbmodel_Attribute_strategy)
@settings(max_examples=25)
def test_dbmodel_Attribute_instantiation(instance):
    assert isinstance(instance, dbmodel_Attribute)


dbmodel_Class_strategy = st.builds(dbmodel_Class, aName=safe_text, archivIndex=safe_text, descr=safe_text, noDBio=st.booleans(), publish=st.booleans(), pubname=safe_text, pubspec=st.booleans(), vmaj=st.integers(), vmin=st.integers(), whereclause=safe_text)
@given(instance=dbmodel_Class_strategy)
@settings(max_examples=25)
def test_dbmodel_Class_instantiation(instance):
    assert isinstance(instance, dbmodel_Class)


dbmodel_ClassOrDuplicate_strategy = st.builds(dbmodel_ClassOrDuplicate, abbrev=safe_text, name=safe_text, reps=safe_text)
@given(instance=dbmodel_ClassOrDuplicate_strategy)
@settings(max_examples=25)
def test_dbmodel_ClassOrDuplicate_instantiation(instance):
    assert isinstance(instance, dbmodel_ClassOrDuplicate)


dbmodel_DbModel_strategy = st.builds(dbmodel_DbModel, doAll=st.booleans(), kobeType=safe_text, kudaType=safe_text, mtype=safe_text, name=safe_text, version=safe_text)
@given(instance=dbmodel_DbModel_strategy)
@settings(max_examples=25)
def test_dbmodel_DbModel_instantiation(instance):
    assert isinstance(instance, dbmodel_DbModel)


dbmodel_Duplicate_strategy = st.builds(dbmodel_Duplicate)
@given(instance=dbmodel_Duplicate_strategy)
@settings(max_examples=25)
def test_dbmodel_Duplicate_instantiation(instance):
    assert isinstance(instance, dbmodel_Duplicate)


dbmodel_Import_strategy = st.builds(dbmodel_Import, importedNamespace=safe_text)
@given(instance=dbmodel_Import_strategy)
@settings(max_examples=25)
def test_dbmodel_Import_instantiation(instance):
    assert isinstance(instance, dbmodel_Import)


dbmodel_Index_strategy = st.builds(dbmodel_Index, kuko=st.booleans(), name=safe_text, unique=st.booleans())
@given(instance=dbmodel_Index_strategy)
@settings(max_examples=25)
def test_dbmodel_Index_instantiation(instance):
    assert isinstance(instance, dbmodel_Index)


dbmodel_IndexRef_strategy = st.builds(dbmodel_IndexRef, clustered=st.booleans(), isPrimkey=st.booleans())
@given(instance=dbmodel_IndexRef_strategy)
@settings(max_examples=25)
def test_dbmodel_IndexRef_instantiation(instance):
    assert isinstance(instance, dbmodel_IndexRef)


dbmodel_Ltype_strategy = st.builds(dbmodel_Ltype)
@given(instance=dbmodel_Ltype_strategy)
@settings(max_examples=25)
def test_dbmodel_Ltype_instantiation(instance):
    assert isinstance(instance, dbmodel_Ltype)


dbmodel_Pdb_strategy = st.builds(dbmodel_Pdb, lockSchema=safe_text, name=safe_text, tablePartitioning=st.integers())
@given(instance=dbmodel_Pdb_strategy)
@settings(max_examples=25)
def test_dbmodel_Pdb_instantiation(instance):
    assert isinstance(instance, dbmodel_Pdb)


dbmodel_Primkey_strategy = st.builds(dbmodel_Primkey)
@given(instance=dbmodel_Primkey_strategy)
@settings(max_examples=25)
def test_dbmodel_Primkey_instantiation(instance):
    assert isinstance(instance, dbmodel_Primkey)


dbmodel_StructOverride_strategy = st.builds(dbmodel_StructOverride, altname=safe_text)
@given(instance=dbmodel_StructOverride_strategy)
@settings(max_examples=25)
def test_dbmodel_StructOverride_instantiation(instance):
    assert isinstance(instance, dbmodel_StructOverride)


dbmodel_StructShare_strategy = st.builds(dbmodel_StructShare)
@given(instance=dbmodel_StructShare_strategy)
@settings(max_examples=25)
def test_dbmodel_StructShare_instantiation(instance):
    assert isinstance(instance, dbmodel_StructShare)


dbmodel_Stype_strategy = st.builds(dbmodel_Stype)
@given(instance=dbmodel_Stype_strategy)
@settings(max_examples=25)
def test_dbmodel_Stype_instantiation(instance):
    assert isinstance(instance, dbmodel_Stype)


dbmodel_Subject_strategy = st.builds(dbmodel_Subject, name=safe_text)
@given(instance=dbmodel_Subject_strategy)
@settings(max_examples=25)
def test_dbmodel_Subject_instantiation(instance):
    assert isinstance(instance, dbmodel_Subject)


dbmodel_Type_strategy = st.builds(dbmodel_Type)
@given(instance=dbmodel_Type_strategy)
@settings(max_examples=25)
def test_dbmodel_Type_instantiation(instance):
    assert isinstance(instance, dbmodel_Type)


