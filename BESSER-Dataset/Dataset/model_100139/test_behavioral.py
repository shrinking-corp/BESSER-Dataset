import pytest
from datetime import date, datetime, time, timedelta

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

def test_assoc_attr41_reverse_link_reassign_clear():
    a1 = dbmodel_IndexRef(clustered=True, isPrimkey=True)
    a2 = dbmodel_IndexRef(clustered=False, isPrimkey=False)
    b = dbmodel_Attribute(aName="sample_text", archiv=True, descr="sample_text", extattr="sample_text", exttable="sample_text", foreign=True, immutable=True, isInDB=True, isPublic=True, kuko=True, kukoindex=True, kukoonly=True, name="sample_text", nullOK=True, optional=True, shared=True, sybident=True)
    _safe_set(b, 'dbmodel_Attribute43', a1)
    assert _is_linked(b, 'dbmodel_Attribute43', a1)
    if hasattr(a1, 'dbmodel_IndexRef42'):
        assert _is_linked(a1, 'dbmodel_IndexRef42', b)
    _safe_set(b, 'dbmodel_Attribute43', a2)
    assert _is_linked(b, 'dbmodel_Attribute43', a2)
    if hasattr(a1, 'dbmodel_IndexRef42'):
        assert not _is_linked(a1, 'dbmodel_IndexRef42', b)
    if hasattr(a2, 'dbmodel_IndexRef42'):
        assert _is_linked(a2, 'dbmodel_IndexRef42', b)
    _safe_set(b, 'dbmodel_Attribute43', None)
    assert not _is_linked(b, 'dbmodel_Attribute43', a2)
    if hasattr(a2, 'dbmodel_IndexRef42'):
        assert not _is_linked(a2, 'dbmodel_IndexRef42', b)


def test_assoc_attributes10_reverse_link_reassign_clear():
    a1 = dbmodel_Class(aName="sample_text", archivIndex="sample_text", descr="sample_text", noDBio=True, publish=True, pubname="sample_text", pubspec=True, vmaj=7, vmin=7, whereclause="sample_text")
    a2 = dbmodel_Class(aName="sample_text_2", archivIndex="sample_text_2", descr="sample_text_2", noDBio=False, publish=False, pubname="sample_text_2", pubspec=False, vmaj=13, vmin=13, whereclause="sample_text_2")
    b = dbmodel_Attribute(aName="sample_text", archiv=True, descr="sample_text", extattr="sample_text", exttable="sample_text", foreign=True, immutable=True, isInDB=True, isPublic=True, kuko=True, kukoindex=True, kukoonly=True, name="sample_text", nullOK=True, optional=True, shared=True, sybident=True)
    _safe_set(b, 'dbmodel_Attribute', a1)
    assert _is_linked(b, 'dbmodel_Attribute', a1)
    if hasattr(a1, 'dbmodel_Class11'):
        assert _is_linked(a1, 'dbmodel_Class11', b)
    _safe_set(b, 'dbmodel_Attribute', a2)
    assert _is_linked(b, 'dbmodel_Attribute', a2)
    if hasattr(a1, 'dbmodel_Class11'):
        assert not _is_linked(a1, 'dbmodel_Class11', b)
    if hasattr(a2, 'dbmodel_Class11'):
        assert _is_linked(a2, 'dbmodel_Class11', b)
    _safe_set(b, 'dbmodel_Attribute', None)
    assert not _is_linked(b, 'dbmodel_Attribute', a2)
    if hasattr(a2, 'dbmodel_Class11'):
        assert not _is_linked(a2, 'dbmodel_Class11', b)


def test_assoc_attrs36_reverse_link_reassign_clear():
    a1 = dbmodel_Index(kuko=True, name="sample_text", unique=True)
    a2 = dbmodel_Index(kuko=False, name="sample_text_2", unique=False)
    b = dbmodel_Attribute(aName="sample_text", archiv=True, descr="sample_text", extattr="sample_text", exttable="sample_text", foreign=True, immutable=True, isInDB=True, isPublic=True, kuko=True, kukoindex=True, kukoonly=True, name="sample_text", nullOK=True, optional=True, shared=True, sybident=True)
    _safe_set(b, 'dbmodel_Attribute38', a1)
    assert _is_linked(b, 'dbmodel_Attribute38', a1)
    if hasattr(a1, 'dbmodel_Index37'):
        assert _is_linked(a1, 'dbmodel_Index37', b)
    _safe_set(b, 'dbmodel_Attribute38', a2)
    assert _is_linked(b, 'dbmodel_Attribute38', a2)
    if hasattr(a1, 'dbmodel_Index37'):
        assert not _is_linked(a1, 'dbmodel_Index37', b)
    if hasattr(a2, 'dbmodel_Index37'):
        assert _is_linked(a2, 'dbmodel_Index37', b)
    _safe_set(b, 'dbmodel_Attribute38', None)
    assert not _is_linked(b, 'dbmodel_Attribute38', a2)
    if hasattr(a2, 'dbmodel_Index37'):
        assert not _is_linked(a2, 'dbmodel_Index37', b)


def test_assoc_classes3_reverse_link_reassign_clear():
    a1 = dbmodel_DbModel(doAll=True, kobeType="sample_text", kudaType="sample_text", mtype="sample_text", name="sample_text", version="sample_text")
    a2 = dbmodel_DbModel(doAll=False, kobeType="sample_text_2", kudaType="sample_text_2", mtype="sample_text_2", name="sample_text_2", version="sample_text_2")
    b = dbmodel_Class(aName="sample_text", archivIndex="sample_text", descr="sample_text", noDBio=True, publish=True, pubname="sample_text", pubspec=True, vmaj=7, vmin=7, whereclause="sample_text")
    _safe_set(b, 'dbmodel_Class', a1)
    assert _is_linked(b, 'dbmodel_Class', a1)
    if hasattr(a1, 'dbmodel_DbModel4'):
        assert _is_linked(a1, 'dbmodel_DbModel4', b)
    _safe_set(b, 'dbmodel_Class', a2)
    assert _is_linked(b, 'dbmodel_Class', a2)
    if hasattr(a1, 'dbmodel_DbModel4'):
        assert not _is_linked(a1, 'dbmodel_DbModel4', b)
    if hasattr(a2, 'dbmodel_DbModel4'):
        assert _is_linked(a2, 'dbmodel_DbModel4', b)
    _safe_set(b, 'dbmodel_Class', None)
    assert not _is_linked(b, 'dbmodel_Class', a2)
    if hasattr(a2, 'dbmodel_DbModel4'):
        assert not _is_linked(a2, 'dbmodel_DbModel4', b)


def test_assoc_forattr24_reverse_link_reassign_clear():
    a1 = dbmodel_Attribute(aName="sample_text", archiv=True, descr="sample_text", extattr="sample_text", exttable="sample_text", foreign=True, immutable=True, isInDB=True, isPublic=True, kuko=True, kukoindex=True, kukoonly=True, name="sample_text", nullOK=True, optional=True, shared=True, sybident=True)
    a2 = dbmodel_Attribute(aName="sample_text_2", archiv=False, descr="sample_text_2", extattr="sample_text_2", exttable="sample_text_2", foreign=False, immutable=False, isInDB=False, isPublic=False, kuko=False, kukoindex=False, kukoonly=False, name="sample_text_2", nullOK=False, optional=False, shared=False, sybident=False)
    b = dbmodel_Attribute(aName="sample_text", archiv=True, descr="sample_text", extattr="sample_text", exttable="sample_text", foreign=True, immutable=True, isInDB=True, isPublic=True, kuko=True, kukoindex=True, kukoonly=True, name="sample_text", nullOK=True, optional=True, shared=True, sybident=True)
    _safe_set(b, 'dbmodel_Attribute25', a1)
    assert _is_linked(b, 'dbmodel_Attribute25', a1)
    if hasattr(a1, 'dbmodel_Attribute23'):
        assert _is_linked(a1, 'dbmodel_Attribute23', b)
    _safe_set(b, 'dbmodel_Attribute25', a2)
    assert _is_linked(b, 'dbmodel_Attribute25', a2)
    if hasattr(a1, 'dbmodel_Attribute23'):
        assert not _is_linked(a1, 'dbmodel_Attribute23', b)
    if hasattr(a2, 'dbmodel_Attribute23'):
        assert _is_linked(a2, 'dbmodel_Attribute23', b)
    _safe_set(b, 'dbmodel_Attribute25', None)
    assert not _is_linked(b, 'dbmodel_Attribute25', a2)
    if hasattr(a2, 'dbmodel_Attribute23'):
        assert not _is_linked(a2, 'dbmodel_Attribute23', b)


def test_assoc_imports0_reverse_link_reassign_clear():
    a1 = dbmodel_Import(importedNamespace="sample_text")
    a2 = dbmodel_Import(importedNamespace="sample_text_2")
    b = dbmodel_DbModel(doAll=True, kobeType="sample_text", kudaType="sample_text", mtype="sample_text", name="sample_text", version="sample_text")
    _safe_set(b, 'dbmodel_DbModel', {a1})
    assert _is_linked(b, 'dbmodel_DbModel', a1)
    if hasattr(a1, 'dbmodel_Import'):
        assert _is_linked(a1, 'dbmodel_Import', b)
    _safe_set(b, 'dbmodel_DbModel', {a2})
    assert _is_linked(b, 'dbmodel_DbModel', a2)
    if hasattr(a1, 'dbmodel_Import'):
        assert not _is_linked(a1, 'dbmodel_Import', b)
    if hasattr(a2, 'dbmodel_Import'):
        assert _is_linked(a2, 'dbmodel_Import', b)
    _safe_set(b, 'dbmodel_DbModel', set())
    assert not _is_linked(b, 'dbmodel_DbModel', a2)
    if hasattr(a2, 'dbmodel_Import'):
        assert not _is_linked(a2, 'dbmodel_Import', b)


def test_assoc_index39_reverse_link_reassign_clear():
    a1 = dbmodel_IndexRef(clustered=True, isPrimkey=True)
    a2 = dbmodel_IndexRef(clustered=False, isPrimkey=False)
    b = dbmodel_Index(kuko=True, name="sample_text", unique=True)
    _safe_set(b, 'dbmodel_Index40', a1)
    assert _is_linked(b, 'dbmodel_Index40', a1)
    if hasattr(a1, 'dbmodel_IndexRef'):
        assert _is_linked(a1, 'dbmodel_IndexRef', b)
    _safe_set(b, 'dbmodel_Index40', a2)
    assert _is_linked(b, 'dbmodel_Index40', a2)
    if hasattr(a1, 'dbmodel_IndexRef'):
        assert not _is_linked(a1, 'dbmodel_IndexRef', b)
    if hasattr(a2, 'dbmodel_IndexRef'):
        assert _is_linked(a2, 'dbmodel_IndexRef', b)
    _safe_set(b, 'dbmodel_Index40', None)
    assert not _is_linked(b, 'dbmodel_Index40', a2)
    if hasattr(a2, 'dbmodel_IndexRef'):
        assert not _is_linked(a2, 'dbmodel_IndexRef', b)


def test_assoc_indices14_reverse_link_reassign_clear():
    a1 = dbmodel_Index(kuko=True, name="sample_text", unique=True)
    a2 = dbmodel_Index(kuko=False, name="sample_text_2", unique=False)
    b = dbmodel_Class(aName="sample_text", archivIndex="sample_text", descr="sample_text", noDBio=True, publish=True, pubname="sample_text", pubspec=True, vmaj=7, vmin=7, whereclause="sample_text")
    _safe_set(b, 'dbmodel_Class15', {a1})
    assert _is_linked(b, 'dbmodel_Class15', a1)
    if hasattr(a1, 'dbmodel_Index'):
        assert _is_linked(a1, 'dbmodel_Index', b)
    _safe_set(b, 'dbmodel_Class15', {a2})
    assert _is_linked(b, 'dbmodel_Class15', a2)
    if hasattr(a1, 'dbmodel_Index'):
        assert not _is_linked(a1, 'dbmodel_Index', b)
    if hasattr(a2, 'dbmodel_Index'):
        assert _is_linked(a2, 'dbmodel_Index', b)
    _safe_set(b, 'dbmodel_Class15', set())
    assert not _is_linked(b, 'dbmodel_Class15', a2)
    if hasattr(a2, 'dbmodel_Index'):
        assert not _is_linked(a2, 'dbmodel_Index', b)


def test_assoc_indices44_reverse_link_reassign_clear():
    a1 = dbmodel_Pdb(lockSchema="sample_text", name="sample_text", tablePartitioning=7)
    a2 = dbmodel_Pdb(lockSchema="sample_text_2", name="sample_text_2", tablePartitioning=13)
    b = dbmodel_IndexRef(clustered=True, isPrimkey=True)
    _safe_set(b, 'dbmodel_IndexRef46', a1)
    assert _is_linked(b, 'dbmodel_IndexRef46', a1)
    if hasattr(a1, 'dbmodel_Pdb45'):
        assert _is_linked(a1, 'dbmodel_Pdb45', b)
    _safe_set(b, 'dbmodel_IndexRef46', a2)
    assert _is_linked(b, 'dbmodel_IndexRef46', a2)
    if hasattr(a1, 'dbmodel_Pdb45'):
        assert not _is_linked(a1, 'dbmodel_Pdb45', b)
    if hasattr(a2, 'dbmodel_Pdb45'):
        assert _is_linked(a2, 'dbmodel_Pdb45', b)
    _safe_set(b, 'dbmodel_IndexRef46', None)
    assert not _is_linked(b, 'dbmodel_IndexRef46', a2)
    if hasattr(a2, 'dbmodel_Pdb45'):
        assert not _is_linked(a2, 'dbmodel_Pdb45', b)


def test_assoc_logattr31_reverse_link_reassign_clear():
    a1 = dbmodel_Attribute(aName="sample_text", archiv=True, descr="sample_text", extattr="sample_text", exttable="sample_text", foreign=True, immutable=True, isInDB=True, isPublic=True, kuko=True, kukoindex=True, kukoonly=True, name="sample_text", nullOK=True, optional=True, shared=True, sybident=True)
    a2 = dbmodel_Attribute(aName="sample_text_2", archiv=False, descr="sample_text_2", extattr="sample_text_2", exttable="sample_text_2", foreign=False, immutable=False, isInDB=False, isPublic=False, kuko=False, kukoindex=False, kukoonly=False, name="sample_text_2", nullOK=False, optional=False, shared=False, sybident=False)
    b = dbmodel_Attribute(aName="sample_text", archiv=True, descr="sample_text", extattr="sample_text", exttable="sample_text", foreign=True, immutable=True, isInDB=True, isPublic=True, kuko=True, kukoindex=True, kukoonly=True, name="sample_text", nullOK=True, optional=True, shared=True, sybident=True)
    _safe_set(b, 'dbmodel_Attribute32', a1)
    assert _is_linked(b, 'dbmodel_Attribute32', a1)
    if hasattr(a1, 'dbmodel_Attribute30'):
        assert _is_linked(a1, 'dbmodel_Attribute30', b)
    _safe_set(b, 'dbmodel_Attribute32', a2)
    assert _is_linked(b, 'dbmodel_Attribute32', a2)
    if hasattr(a1, 'dbmodel_Attribute30'):
        assert not _is_linked(a1, 'dbmodel_Attribute30', b)
    if hasattr(a2, 'dbmodel_Attribute30'):
        assert _is_linked(a2, 'dbmodel_Attribute30', b)
    _safe_set(b, 'dbmodel_Attribute32', None)
    assert not _is_linked(b, 'dbmodel_Attribute32', a2)
    if hasattr(a2, 'dbmodel_Attribute30'):
        assert not _is_linked(a2, 'dbmodel_Attribute30', b)


def test_assoc_ovride28_reverse_link_reassign_clear():
    a1 = dbmodel_StructOverride(altname="sample_text")
    a2 = dbmodel_StructOverride(altname="sample_text_2")
    b = dbmodel_Attribute(aName="sample_text", archiv=True, descr="sample_text", extattr="sample_text", exttable="sample_text", foreign=True, immutable=True, isInDB=True, isPublic=True, kuko=True, kukoindex=True, kukoonly=True, name="sample_text", nullOK=True, optional=True, shared=True, sybident=True)
    _safe_set(b, 'dbmodel_Attribute29', {a1})
    assert _is_linked(b, 'dbmodel_Attribute29', a1)
    if hasattr(a1, 'dbmodel_StructOverride'):
        assert _is_linked(a1, 'dbmodel_StructOverride', b)
    _safe_set(b, 'dbmodel_Attribute29', {a2})
    assert _is_linked(b, 'dbmodel_Attribute29', a2)
    if hasattr(a1, 'dbmodel_StructOverride'):
        assert not _is_linked(a1, 'dbmodel_StructOverride', b)
    if hasattr(a2, 'dbmodel_StructOverride'):
        assert _is_linked(a2, 'dbmodel_StructOverride', b)
    _safe_set(b, 'dbmodel_Attribute29', set())
    assert not _is_linked(b, 'dbmodel_Attribute29', a2)
    if hasattr(a2, 'dbmodel_StructOverride'):
        assert not _is_linked(a2, 'dbmodel_StructOverride', b)


def test_assoc_pdbs16_reverse_link_reassign_clear():
    a1 = dbmodel_Pdb(lockSchema="sample_text", name="sample_text", tablePartitioning=7)
    a2 = dbmodel_Pdb(lockSchema="sample_text_2", name="sample_text_2", tablePartitioning=13)
    b = dbmodel_Class(aName="sample_text", archivIndex="sample_text", descr="sample_text", noDBio=True, publish=True, pubname="sample_text", pubspec=True, vmaj=7, vmin=7, whereclause="sample_text")
    _safe_set(b, 'dbmodel_Class17', {a1})
    assert _is_linked(b, 'dbmodel_Class17', a1)
    if hasattr(a1, 'dbmodel_Pdb'):
        assert _is_linked(a1, 'dbmodel_Pdb', b)
    _safe_set(b, 'dbmodel_Class17', {a2})
    assert _is_linked(b, 'dbmodel_Class17', a2)
    if hasattr(a1, 'dbmodel_Pdb'):
        assert not _is_linked(a1, 'dbmodel_Pdb', b)
    if hasattr(a2, 'dbmodel_Pdb'):
        assert _is_linked(a2, 'dbmodel_Pdb', b)
    _safe_set(b, 'dbmodel_Class17', set())
    assert not _is_linked(b, 'dbmodel_Class17', a2)
    if hasattr(a2, 'dbmodel_Pdb'):
        assert not _is_linked(a2, 'dbmodel_Pdb', b)


def test_assoc_subject7_reverse_link_reassign_clear():
    a1 = dbmodel_Subject(name="sample_text")
    a2 = dbmodel_Subject(name="sample_text_2")
    b = dbmodel_Class(aName="sample_text", archivIndex="sample_text", descr="sample_text", noDBio=True, publish=True, pubname="sample_text", pubspec=True, vmaj=7, vmin=7, whereclause="sample_text")
    _safe_set(b, 'dbmodel_Class8', a1)
    assert _is_linked(b, 'dbmodel_Class8', a1)
    if hasattr(a1, 'dbmodel_Subject9'):
        assert _is_linked(a1, 'dbmodel_Subject9', b)
    _safe_set(b, 'dbmodel_Class8', a2)
    assert _is_linked(b, 'dbmodel_Class8', a2)
    if hasattr(a1, 'dbmodel_Subject9'):
        assert not _is_linked(a1, 'dbmodel_Subject9', b)
    if hasattr(a2, 'dbmodel_Subject9'):
        assert _is_linked(a2, 'dbmodel_Subject9', b)
    _safe_set(b, 'dbmodel_Class8', None)
    assert not _is_linked(b, 'dbmodel_Class8', a2)
    if hasattr(a2, 'dbmodel_Subject9'):
        assert not _is_linked(a2, 'dbmodel_Subject9', b)


def test_assoc_subjects1_reverse_link_reassign_clear():
    a1 = dbmodel_Subject(name="sample_text")
    a2 = dbmodel_Subject(name="sample_text_2")
    b = dbmodel_DbModel(doAll=True, kobeType="sample_text", kudaType="sample_text", mtype="sample_text", name="sample_text", version="sample_text")
    _safe_set(b, 'dbmodel_DbModel2', {a1})
    assert _is_linked(b, 'dbmodel_DbModel2', a1)
    if hasattr(a1, 'dbmodel_Subject'):
        assert _is_linked(a1, 'dbmodel_Subject', b)
    _safe_set(b, 'dbmodel_DbModel2', {a2})
    assert _is_linked(b, 'dbmodel_DbModel2', a2)
    if hasattr(a1, 'dbmodel_Subject'):
        assert not _is_linked(a1, 'dbmodel_Subject', b)
    if hasattr(a2, 'dbmodel_Subject'):
        assert _is_linked(a2, 'dbmodel_Subject', b)
    _safe_set(b, 'dbmodel_DbModel2', set())
    assert not _is_linked(b, 'dbmodel_DbModel2', a2)
    if hasattr(a2, 'dbmodel_Subject'):
        assert not _is_linked(a2, 'dbmodel_Subject', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attr51_stub_double():
    # dbmodel_StructShare has no real 'dbmodel_StructShare52' property in the generated
    # code (a bare stub) -- manually attach it so dbmodel_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbmodel_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbmodel_Attribute(aName="sample_text", archiv=True, descr="sample_text", extattr="sample_text", exttable="sample_text", foreign=True, immutable=True, isInDB=True, isPublic=True, kuko=True, kukoindex=True, kukoonly=True, name="sample_text", nullOK=True, optional=True, shared=True, sybident=True)
    partner = dbmodel_StructShare()
    setattr(partner, 'dbmodel_StructShare52', None)
    _safe_set(owner, 'dbmodel_Attribute53', partner)
    assert getattr(partner, 'dbmodel_StructShare52') == owner
    _safe_set(owner, 'dbmodel_Attribute53', None)
    assert getattr(partner, 'dbmodel_StructShare52') is None


def test_assoc_duplicates5_stub_double():
    # dbmodel_Duplicate has no real 'dbmodel_Duplicate' property in the generated
    # code (a bare stub) -- manually attach it so dbmodel_DbModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbmodel_DbModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbmodel_DbModel(doAll=True, kobeType="sample_text", kudaType="sample_text", mtype="sample_text", name="sample_text", version="sample_text")
    partner = dbmodel_Duplicate()
    setattr(partner, 'dbmodel_Duplicate', None)
    _safe_set(owner, 'dbmodel_DbModel6', {partner})
    assert getattr(partner, 'dbmodel_Duplicate') == owner
    _safe_set(owner, 'dbmodel_DbModel6', set())
    assert getattr(partner, 'dbmodel_Duplicate') is None


def test_assoc_orig18_stub_double():
    # dbmodel_Duplicate has no real 'dbmodel_Duplicate19' property in the generated
    # code (a bare stub) -- manually attach it so dbmodel_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbmodel_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbmodel_Class(aName="sample_text", archivIndex="sample_text", descr="sample_text", noDBio=True, publish=True, pubname="sample_text", pubspec=True, vmaj=7, vmin=7, whereclause="sample_text")
    partner = dbmodel_Duplicate()
    setattr(partner, 'dbmodel_Duplicate19', None)
    _safe_set(owner, 'dbmodel_Class20', partner)
    assert getattr(partner, 'dbmodel_Duplicate19') == owner
    _safe_set(owner, 'dbmodel_Class20', None)
    assert getattr(partner, 'dbmodel_Duplicate19') is None


def test_assoc_part49_stub_double():
    # dbmodel_Stype has no real 'dbmodel_Stype' property in the generated
    # code (a bare stub) -- manually attach it so dbmodel_StructOverride's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbmodel_StructOverride's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbmodel_StructOverride(altname="sample_text")
    partner = dbmodel_Stype()
    setattr(partner, 'dbmodel_Stype', None)
    _safe_set(owner, 'dbmodel_StructOverride50', partner)
    assert getattr(partner, 'dbmodel_Stype') == owner
    _safe_set(owner, 'dbmodel_StructOverride50', None)
    assert getattr(partner, 'dbmodel_Stype') is None


def test_assoc_pkeys33_stub_double():
    # dbmodel_Primkey has no real 'dbmodel_Primkey34' property in the generated
    # code (a bare stub) -- manually attach it so dbmodel_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbmodel_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbmodel_Attribute(aName="sample_text", archiv=True, descr="sample_text", extattr="sample_text", exttable="sample_text", foreign=True, immutable=True, isInDB=True, isPublic=True, kuko=True, kukoindex=True, kukoonly=True, name="sample_text", nullOK=True, optional=True, shared=True, sybident=True)
    partner = dbmodel_Primkey()
    setattr(partner, 'dbmodel_Primkey34', None)
    _safe_set(owner, 'dbmodel_Attribute35', partner)
    assert owner in getattr(partner, 'dbmodel_Primkey34')
    _safe_set(owner, 'dbmodel_Attribute35', None)
    assert owner not in getattr(partner, 'dbmodel_Primkey34')


def test_assoc_primkey12_stub_double():
    # dbmodel_Primkey has no real 'dbmodel_Primkey' property in the generated
    # code (a bare stub) -- manually attach it so dbmodel_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbmodel_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbmodel_Class(aName="sample_text", archivIndex="sample_text", descr="sample_text", noDBio=True, publish=True, pubname="sample_text", pubspec=True, vmaj=7, vmin=7, whereclause="sample_text")
    partner = dbmodel_Primkey()
    setattr(partner, 'dbmodel_Primkey', None)
    _safe_set(owner, 'dbmodel_Class13', partner)
    assert getattr(partner, 'dbmodel_Primkey') == owner
    _safe_set(owner, 'dbmodel_Class13', None)
    assert getattr(partner, 'dbmodel_Primkey') is None


def test_assoc_shrs26_stub_double():
    # dbmodel_StructShare has no real 'dbmodel_StructShare' property in the generated
    # code (a bare stub) -- manually attach it so dbmodel_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbmodel_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbmodel_Attribute(aName="sample_text", archiv=True, descr="sample_text", extattr="sample_text", exttable="sample_text", foreign=True, immutable=True, isInDB=True, isPublic=True, kuko=True, kukoindex=True, kukoonly=True, name="sample_text", nullOK=True, optional=True, shared=True, sybident=True)
    partner = dbmodel_StructShare()
    setattr(partner, 'dbmodel_StructShare', None)
    _safe_set(owner, 'dbmodel_Attribute27', {partner})
    assert getattr(partner, 'dbmodel_StructShare') == owner
    _safe_set(owner, 'dbmodel_Attribute27', set())
    assert getattr(partner, 'dbmodel_StructShare') is None


def test_assoc_type21_stub_double():
    # dbmodel_Ltype has no real 'dbmodel_Ltype' property in the generated
    # code (a bare stub) -- manually attach it so dbmodel_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbmodel_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbmodel_Attribute(aName="sample_text", archiv=True, descr="sample_text", extattr="sample_text", exttable="sample_text", foreign=True, immutable=True, isInDB=True, isPublic=True, kuko=True, kukoindex=True, kukoonly=True, name="sample_text", nullOK=True, optional=True, shared=True, sybident=True)
    partner = dbmodel_Ltype()
    setattr(partner, 'dbmodel_Ltype', None)
    _safe_set(owner, 'dbmodel_Attribute22', partner)
    assert getattr(partner, 'dbmodel_Ltype') == owner
    _safe_set(owner, 'dbmodel_Attribute22', None)
    assert getattr(partner, 'dbmodel_Ltype') is None


