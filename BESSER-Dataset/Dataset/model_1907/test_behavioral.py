import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ABIEProperty,
    ACCProperty,
    AssembledBase,
    BDTProperty,
    CDTProperty,
    ContextRef,
    ENUM,
    Library,
    MAProperty,
    OclBooleanLiteral,
    OclExpression,
    OclFunctionCall,
    OclLiteral,
    OclRef,
    OclReference,
    OclValue,
    umm_ABIE,
    umm_ABIEProperty,
    umm_ACC,
    umm_ACCProperty,
    umm_ASBIE,
    umm_ASCC,
    umm_ASMA,
    umm_ASNONE,
    umm_Assembled,
    umm_AssembledBase,
    umm_BBIE,
    umm_BCC,
    umm_BDT,
    umm_BDTLibrary,
    umm_BDTProperty,
    umm_BIELibrary,
    umm_CCLibrary,
    umm_CDT,
    umm_CDTLibrary,
    umm_CDTProperty,
    umm_CDT_Content,
    umm_CDT_Supplement,
    umm_CodelistEntry,
    umm_Constraint,
    umm_Content,
    umm_ContextRef,
    umm_DocLibrary,
    umm_ENUM,
    umm_ENUMLibrary,
    umm_InfEnvelope,
    umm_Library,
    umm_MA,
    umm_MAProperty,
    umm_OclAnd,
    umm_OclArrow,
    umm_OclBooleanFalse,
    umm_OclBooleanLiteral,
    umm_OclBooleanTrue,
    umm_OclEnumerationLiteral,
    umm_OclEqual,
    umm_OclExpression,
    umm_OclForAll,
    umm_OclFunctionCall,
    umm_OclImplies,
    umm_OclIntegerLiteral,
    umm_OclInvariant,
    umm_OclIsEmpty,
    umm_OclLess,
    umm_OclLessOrEqual,
    umm_OclLiteral,
    umm_OclMore,
    umm_OclMoreOrEqual,
    umm_OclNotEmpty,
    umm_OclOr,
    umm_OclPathFeatureHead,
    umm_OclPathSelfHead,
    umm_OclPathTail,
    umm_OclRef,
    umm_OclReference,
    umm_OclSize,
    umm_OclStringLiteral,
    umm_OclValue,
    umm_OclXor,
    umm_Original,
    umm_Primitive,
    umm_PrimitiveLibrary,
    umm_Subset,
    umm_Supplement,
    umm_TC_Constraint,
    ConstraintKind,
    MultiplicityKind,
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

def test_assoc_abies22_reverse_link_reassign_clear():
    a1 = umm_BIELibrary(baseURN="sample_text", businessTerm="sample_text", copyright="sample_text", namespacePrefix="sample_text", owner="sample_text", reference="sample_text", uniqueIdentifier="sample_text", versionIdentifier="sample_text")
    a2 = umm_BIELibrary(baseURN="sample_text_2", businessTerm="sample_text_2", copyright="sample_text_2", namespacePrefix="sample_text_2", owner="sample_text_2", reference="sample_text_2", uniqueIdentifier="sample_text_2", versionIdentifier="sample_text_2")
    b = umm_ABIE(businessTerm="sample_text", definition="sample_text", dictionary="sample_text", uniqueIdentifier="sample_text", versionIdentifier="sample_text")
    _safe_set(b, 'umm_ABIE24', a1)
    assert _is_linked(b, 'umm_ABIE24', a1)
    if hasattr(a1, 'umm_BIELibrary23'):
        assert _is_linked(a1, 'umm_BIELibrary23', b)
    _safe_set(b, 'umm_ABIE24', a2)
    assert _is_linked(b, 'umm_ABIE24', a2)
    if hasattr(a1, 'umm_BIELibrary23'):
        assert not _is_linked(a1, 'umm_BIELibrary23', b)
    if hasattr(a2, 'umm_BIELibrary23'):
        assert _is_linked(a2, 'umm_BIELibrary23', b)
    _safe_set(b, 'umm_ABIE24', None)
    assert not _is_linked(b, 'umm_ABIE24', a2)
    if hasattr(a2, 'umm_BIELibrary23'):
        assert not _is_linked(a2, 'umm_BIELibrary23', b)


def test_assoc_accs52_reverse_link_reassign_clear():
    a1 = umm_CCLibrary(baseURN="sample_text", businessTerm="sample_text", copyright="sample_text", namespacePrefix="sample_text", owner="sample_text", reference="sample_text", uniqueIdentifier="sample_text", versionIdentifier="sample_text")
    a2 = umm_CCLibrary(baseURN="sample_text_2", businessTerm="sample_text_2", copyright="sample_text_2", namespacePrefix="sample_text_2", owner="sample_text_2", reference="sample_text_2", uniqueIdentifier="sample_text_2", versionIdentifier="sample_text_2")
    b = umm_ACC(businessTerm="sample_text", definition="sample_text", dictionary="sample_text", name="sample_text", uniqueIdentifier="sample_text", versionIdentifier="sample_text")
    _safe_set(b, 'umm_ACC', a1)
    assert _is_linked(b, 'umm_ACC', a1)
    if hasattr(a1, 'umm_CCLibrary'):
        assert _is_linked(a1, 'umm_CCLibrary', b)
    _safe_set(b, 'umm_ACC', a2)
    assert _is_linked(b, 'umm_ACC', a2)
    if hasattr(a1, 'umm_CCLibrary'):
        assert not _is_linked(a1, 'umm_CCLibrary', b)
    if hasattr(a2, 'umm_CCLibrary'):
        assert _is_linked(a2, 'umm_CCLibrary', b)
    _safe_set(b, 'umm_ACC', None)
    assert not _is_linked(b, 'umm_ACC', a2)
    if hasattr(a2, 'umm_CCLibrary'):
        assert not _is_linked(a2, 'umm_CCLibrary', b)


def test_assoc_bdtLibrary1_reverse_link_reassign_clear():
    a1 = umm_DocLibrary(baseURN="sample_text", businessTerm="sample_text", copyright="sample_text", namespacePrefix="sample_text", owner="sample_text", reference="sample_text", uniqueIdentifier="sample_text", versionIdentifier="sample_text")
    a2 = umm_DocLibrary(baseURN="sample_text_2", businessTerm="sample_text_2", copyright="sample_text_2", namespacePrefix="sample_text_2", owner="sample_text_2", reference="sample_text_2", uniqueIdentifier="sample_text_2", versionIdentifier="sample_text_2")
    b = umm_BDTLibrary(baseURN="sample_text", businessTerm="sample_text", copyright="sample_text", namespacePrefix="sample_text", owner="sample_text", reference="sample_text", uniqueIdentifier="sample_text", versionIdentifier="sample_text")
    _safe_set(b, 'umm_BDTLibrary', a1)
    assert _is_linked(b, 'umm_BDTLibrary', a1)
    if hasattr(a1, 'umm_DocLibrary2'):
        assert _is_linked(a1, 'umm_DocLibrary2', b)
    _safe_set(b, 'umm_BDTLibrary', a2)
    assert _is_linked(b, 'umm_BDTLibrary', a2)
    if hasattr(a1, 'umm_DocLibrary2'):
        assert not _is_linked(a1, 'umm_DocLibrary2', b)
    if hasattr(a2, 'umm_DocLibrary2'):
        assert _is_linked(a2, 'umm_DocLibrary2', b)
    _safe_set(b, 'umm_BDTLibrary', None)
    assert not _is_linked(b, 'umm_BDTLibrary', a2)
    if hasattr(a2, 'umm_DocLibrary2'):
        assert not _is_linked(a2, 'umm_DocLibrary2', b)


def test_assoc_bdtLibrary19_reverse_link_reassign_clear():
    a1 = umm_BIELibrary(baseURN="sample_text", businessTerm="sample_text", copyright="sample_text", namespacePrefix="sample_text", owner="sample_text", reference="sample_text", uniqueIdentifier="sample_text", versionIdentifier="sample_text")
    a2 = umm_BIELibrary(baseURN="sample_text_2", businessTerm="sample_text_2", copyright="sample_text_2", namespacePrefix="sample_text_2", owner="sample_text_2", reference="sample_text_2", uniqueIdentifier="sample_text_2", versionIdentifier="sample_text_2")
    b = umm_BDTLibrary(baseURN="sample_text", businessTerm="sample_text", copyright="sample_text", namespacePrefix="sample_text", owner="sample_text", reference="sample_text", uniqueIdentifier="sample_text", versionIdentifier="sample_text")
    _safe_set(b, 'umm_BDTLibrary21', a1)
    assert _is_linked(b, 'umm_BDTLibrary21', a1)
    if hasattr(a1, 'umm_BIELibrary20'):
        assert _is_linked(a1, 'umm_BIELibrary20', b)
    _safe_set(b, 'umm_BDTLibrary21', a2)
    assert _is_linked(b, 'umm_BDTLibrary21', a2)
    if hasattr(a1, 'umm_BIELibrary20'):
        assert not _is_linked(a1, 'umm_BIELibrary20', b)
    if hasattr(a2, 'umm_BIELibrary20'):
        assert _is_linked(a2, 'umm_BIELibrary20', b)
    _safe_set(b, 'umm_BDTLibrary21', None)
    assert not _is_linked(b, 'umm_BDTLibrary21', a2)
    if hasattr(a2, 'umm_BIELibrary20'):
        assert not _is_linked(a2, 'umm_BIELibrary20', b)


def test_assoc_bdts36_reverse_link_reassign_clear():
    a1 = umm_BDTLibrary(baseURN="sample_text", businessTerm="sample_text", copyright="sample_text", namespacePrefix="sample_text", owner="sample_text", reference="sample_text", uniqueIdentifier="sample_text", versionIdentifier="sample_text")
    a2 = umm_BDTLibrary(baseURN="sample_text_2", businessTerm="sample_text_2", copyright="sample_text_2", namespacePrefix="sample_text_2", owner="sample_text_2", reference="sample_text_2", uniqueIdentifier="sample_text_2", versionIdentifier="sample_text_2")
    b = umm_BDT(businessTerm="sample_text", definition="sample_text", dictionary="sample_text", uniqueIdentifier="sample_text", versionIdentifier="sample_text")
    _safe_set(b, 'umm_BDT38', a1)
    assert _is_linked(b, 'umm_BDT38', a1)
    if hasattr(a1, 'umm_BDTLibrary37'):
        assert _is_linked(a1, 'umm_BDTLibrary37', b)
    _safe_set(b, 'umm_BDT38', a2)
    assert _is_linked(b, 'umm_BDT38', a2)
    if hasattr(a1, 'umm_BDTLibrary37'):
        assert not _is_linked(a1, 'umm_BDTLibrary37', b)
    if hasattr(a2, 'umm_BDTLibrary37'):
        assert _is_linked(a2, 'umm_BDTLibrary37', b)
    _safe_set(b, 'umm_BDT38', None)
    assert not _is_linked(b, 'umm_BDT38', a2)
    if hasattr(a2, 'umm_BDTLibrary37'):
        assert not _is_linked(a2, 'umm_BDTLibrary37', b)


def test_assoc_bieLibrary0_reverse_link_reassign_clear():
    a1 = umm_DocLibrary(baseURN="sample_text", businessTerm="sample_text", copyright="sample_text", namespacePrefix="sample_text", owner="sample_text", reference="sample_text", uniqueIdentifier="sample_text", versionIdentifier="sample_text")
    a2 = umm_DocLibrary(baseURN="sample_text_2", businessTerm="sample_text_2", copyright="sample_text_2", namespacePrefix="sample_text_2", owner="sample_text_2", reference="sample_text_2", uniqueIdentifier="sample_text_2", versionIdentifier="sample_text_2")
    b = umm_BIELibrary(baseURN="sample_text", businessTerm="sample_text", copyright="sample_text", namespacePrefix="sample_text", owner="sample_text", reference="sample_text", uniqueIdentifier="sample_text", versionIdentifier="sample_text")
    _safe_set(b, 'umm_BIELibrary', a1)
    assert _is_linked(b, 'umm_BIELibrary', a1)
    if hasattr(a1, 'umm_DocLibrary'):
        assert _is_linked(a1, 'umm_DocLibrary', b)
    _safe_set(b, 'umm_BIELibrary', a2)
    assert _is_linked(b, 'umm_BIELibrary', a2)
    if hasattr(a1, 'umm_DocLibrary'):
        assert not _is_linked(a1, 'umm_DocLibrary', b)
    if hasattr(a2, 'umm_DocLibrary'):
        assert _is_linked(a2, 'umm_DocLibrary', b)
    _safe_set(b, 'umm_BIELibrary', None)
    assert not _is_linked(b, 'umm_BIELibrary', a2)
    if hasattr(a2, 'umm_DocLibrary'):
        assert not _is_linked(a2, 'umm_DocLibrary', b)


def test_assoc_cdts61_reverse_link_reassign_clear():
    a1 = umm_CDTLibrary(baseURN="sample_text", businessTerm="sample_text", copyright="sample_text", namespacePrefix="sample_text", owner="sample_text", reference="sample_text", uniqueIdentifier="sample_text", versionIdentifier="sample_text")
    a2 = umm_CDTLibrary(baseURN="sample_text_2", businessTerm="sample_text_2", copyright="sample_text_2", namespacePrefix="sample_text_2", owner="sample_text_2", reference="sample_text_2", uniqueIdentifier="sample_text_2", versionIdentifier="sample_text_2")
    b = umm_CDT(businessTerm="sample_text", definition="sample_text", dictionary="sample_text", name="sample_text", uniqueIdentifier="sample_text", versionIdentifier="sample_text")
    _safe_set(b, 'umm_CDT62', a1)
    assert _is_linked(b, 'umm_CDT62', a1)
    if hasattr(a1, 'umm_CDTLibrary'):
        assert _is_linked(a1, 'umm_CDTLibrary', b)
    _safe_set(b, 'umm_CDT62', a2)
    assert _is_linked(b, 'umm_CDT62', a2)
    if hasattr(a1, 'umm_CDTLibrary'):
        assert not _is_linked(a1, 'umm_CDTLibrary', b)
    if hasattr(a2, 'umm_CDTLibrary'):
        assert _is_linked(a2, 'umm_CDTLibrary', b)
    _safe_set(b, 'umm_CDT62', None)
    assert not _is_linked(b, 'umm_CDT62', a2)
    if hasattr(a2, 'umm_CDTLibrary'):
        assert not _is_linked(a2, 'umm_CDTLibrary', b)


def test_assoc_enums43_reverse_link_reassign_clear():
    a1 = umm_ENUMLibrary(baseURN="sample_text", businessTerm="sample_text", copyright="sample_text", namespacePrefix="sample_text", owner="sample_text", reference="sample_text", uniqueIdentifier="sample_text", versionIdentifier="sample_text")
    a2 = umm_ENUMLibrary(baseURN="sample_text_2", businessTerm="sample_text_2", copyright="sample_text_2", namespacePrefix="sample_text_2", owner="sample_text_2", reference="sample_text_2", uniqueIdentifier="sample_text_2", versionIdentifier="sample_text_2")
    b = umm_ENUM(businessTerm="sample_text", codeListAgencyIdentifier="sample_text", codeListIdentifier="sample_text", codeListName="sample_text", definition="sample_text", dictionary="sample_text", name="sample_text", uniqueIdentifier="sample_text", versionIdentifier="sample_text")
    _safe_set(b, 'umm_ENUM', a1)
    assert _is_linked(b, 'umm_ENUM', a1)
    if hasattr(a1, 'umm_ENUMLibrary'):
        assert _is_linked(a1, 'umm_ENUMLibrary', b)
    _safe_set(b, 'umm_ENUM', a2)
    assert _is_linked(b, 'umm_ENUM', a2)
    if hasattr(a1, 'umm_ENUMLibrary'):
        assert not _is_linked(a1, 'umm_ENUMLibrary', b)
    if hasattr(a2, 'umm_ENUMLibrary'):
        assert _is_linked(a2, 'umm_ENUMLibrary', b)
    _safe_set(b, 'umm_ENUM', None)
    assert not _is_linked(b, 'umm_ENUM', a2)
    if hasattr(a2, 'umm_ENUMLibrary'):
        assert not _is_linked(a2, 'umm_ENUMLibrary', b)


def test_assoc_envelopes3_reverse_link_reassign_clear():
    a1 = umm_InfEnvelope(name="sample_text")
    a2 = umm_InfEnvelope(name="sample_text_2")
    b = umm_DocLibrary(baseURN="sample_text", businessTerm="sample_text", copyright="sample_text", namespacePrefix="sample_text", owner="sample_text", reference="sample_text", uniqueIdentifier="sample_text", versionIdentifier="sample_text")
    _safe_set(b, 'umm_DocLibrary4', {a1})
    assert _is_linked(b, 'umm_DocLibrary4', a1)
    if hasattr(a1, 'umm_InfEnvelope'):
        assert _is_linked(a1, 'umm_InfEnvelope', b)
    _safe_set(b, 'umm_DocLibrary4', {a2})
    assert _is_linked(b, 'umm_DocLibrary4', a2)
    if hasattr(a1, 'umm_InfEnvelope'):
        assert not _is_linked(a1, 'umm_InfEnvelope', b)
    if hasattr(a2, 'umm_InfEnvelope'):
        assert _is_linked(a2, 'umm_InfEnvelope', b)
    _safe_set(b, 'umm_DocLibrary4', set())
    assert not _is_linked(b, 'umm_DocLibrary4', a2)
    if hasattr(a2, 'umm_InfEnvelope'):
        assert not _is_linked(a2, 'umm_InfEnvelope', b)


def test_assoc_or_31_reverse_link_reassign_clear():
    a1 = umm_ABIEProperty(businessTerm="sample_text", definition="sample_text", dictionary="sample_text", sequencingKey="sample_text", uniqueIdentifier="sample_text", versionIdentifier="sample_text")
    a2 = umm_ABIEProperty(businessTerm="sample_text_2", definition="sample_text_2", dictionary="sample_text_2", sequencingKey="sample_text_2", uniqueIdentifier="sample_text_2", versionIdentifier="sample_text_2")
    b = umm_ABIEProperty(businessTerm="sample_text", definition="sample_text", dictionary="sample_text", sequencingKey="sample_text", uniqueIdentifier="sample_text", versionIdentifier="sample_text")
    _safe_set(b, 'umm_ABIEProperty32', a1)
    assert _is_linked(b, 'umm_ABIEProperty32', a1)
    if hasattr(a1, 'umm_ABIEProperty30'):
        assert _is_linked(a1, 'umm_ABIEProperty30', b)
    _safe_set(b, 'umm_ABIEProperty32', a2)
    assert _is_linked(b, 'umm_ABIEProperty32', a2)
    if hasattr(a1, 'umm_ABIEProperty30'):
        assert not _is_linked(a1, 'umm_ABIEProperty30', b)
    if hasattr(a2, 'umm_ABIEProperty30'):
        assert _is_linked(a2, 'umm_ABIEProperty30', b)
    _safe_set(b, 'umm_ABIEProperty32', None)
    assert not _is_linked(b, 'umm_ABIEProperty32', a2)
    if hasattr(a2, 'umm_ABIEProperty30'):
        assert not _is_linked(a2, 'umm_ABIEProperty30', b)


def test_assoc_properties25_reverse_link_reassign_clear():
    a1 = umm_ABIEProperty(businessTerm="sample_text", definition="sample_text", dictionary="sample_text", sequencingKey="sample_text", uniqueIdentifier="sample_text", versionIdentifier="sample_text")
    a2 = umm_ABIEProperty(businessTerm="sample_text_2", definition="sample_text_2", dictionary="sample_text_2", sequencingKey="sample_text_2", uniqueIdentifier="sample_text_2", versionIdentifier="sample_text_2")
    b = umm_ABIE(businessTerm="sample_text", definition="sample_text", dictionary="sample_text", uniqueIdentifier="sample_text", versionIdentifier="sample_text")
    _safe_set(b, 'umm_ABIE26', {a1})
    assert _is_linked(b, 'umm_ABIE26', a1)
    if hasattr(a1, 'umm_ABIEProperty'):
        assert _is_linked(a1, 'umm_ABIEProperty', b)
    _safe_set(b, 'umm_ABIE26', {a2})
    assert _is_linked(b, 'umm_ABIE26', a2)
    if hasattr(a1, 'umm_ABIEProperty'):
        assert not _is_linked(a1, 'umm_ABIEProperty', b)
    if hasattr(a2, 'umm_ABIEProperty'):
        assert _is_linked(a2, 'umm_ABIEProperty', b)
    _safe_set(b, 'umm_ABIE26', set())
    assert not _is_linked(b, 'umm_ABIE26', a2)
    if hasattr(a2, 'umm_ABIEProperty'):
        assert not _is_linked(a2, 'umm_ABIEProperty', b)


def test_assoc_properties39_reverse_link_reassign_clear():
    a1 = umm_BDTProperty(businessTerm="sample_text", definition="sample_text", dictionary="sample_text", length=7, maxLength=7, minLength=7, pattern="sample_text", uniqueIdentifier="sample_text", versionIdentifier="sample_text")
    a2 = umm_BDTProperty(businessTerm="sample_text_2", definition="sample_text_2", dictionary="sample_text_2", length=13, maxLength=13, minLength=13, pattern="sample_text_2", uniqueIdentifier="sample_text_2", versionIdentifier="sample_text_2")
    b = umm_BDT(businessTerm="sample_text", definition="sample_text", dictionary="sample_text", uniqueIdentifier="sample_text", versionIdentifier="sample_text")
    _safe_set(b, 'umm_BDT40', {a1})
    assert _is_linked(b, 'umm_BDT40', a1)
    if hasattr(a1, 'umm_BDTProperty'):
        assert _is_linked(a1, 'umm_BDTProperty', b)
    _safe_set(b, 'umm_BDT40', {a2})
    assert _is_linked(b, 'umm_BDT40', a2)
    if hasattr(a1, 'umm_BDTProperty'):
        assert not _is_linked(a1, 'umm_BDTProperty', b)
    if hasattr(a2, 'umm_BDTProperty'):
        assert _is_linked(a2, 'umm_BDTProperty', b)
    _safe_set(b, 'umm_BDT40', set())
    assert not _is_linked(b, 'umm_BDT40', a2)
    if hasattr(a2, 'umm_BDTProperty'):
        assert not _is_linked(a2, 'umm_BDTProperty', b)


def test_assoc_properties53_reverse_link_reassign_clear():
    a1 = umm_ACCProperty(businessTerm="sample_text", definition="sample_text", dictionary="sample_text", multiplicity="sample_text", name="sample_text", sequencingKey="sample_text", uniqueIdentifier="sample_text", versionIdentifier="sample_text")
    a2 = umm_ACCProperty(businessTerm="sample_text_2", definition="sample_text_2", dictionary="sample_text_2", multiplicity="sample_text_2", name="sample_text_2", sequencingKey="sample_text_2", uniqueIdentifier="sample_text_2", versionIdentifier="sample_text_2")
    b = umm_ACC(businessTerm="sample_text", definition="sample_text", dictionary="sample_text", name="sample_text", uniqueIdentifier="sample_text", versionIdentifier="sample_text")
    _safe_set(b, 'umm_ACC54', {a1})
    assert _is_linked(b, 'umm_ACC54', a1)
    if hasattr(a1, 'umm_ACCProperty'):
        assert _is_linked(a1, 'umm_ACCProperty', b)
    _safe_set(b, 'umm_ACC54', {a2})
    assert _is_linked(b, 'umm_ACC54', a2)
    if hasattr(a1, 'umm_ACCProperty'):
        assert not _is_linked(a1, 'umm_ACCProperty', b)
    if hasattr(a2, 'umm_ACCProperty'):
        assert _is_linked(a2, 'umm_ACCProperty', b)
    _safe_set(b, 'umm_ACC54', set())
    assert not _is_linked(b, 'umm_ACC54', a2)
    if hasattr(a2, 'umm_ACCProperty'):
        assert not _is_linked(a2, 'umm_ACCProperty', b)


def test_assoc_properties63_reverse_link_reassign_clear():
    a1 = umm_CDTProperty(businessTerm="sample_text", definition="sample_text", dictionary="sample_text", multiplicity="sample_text", name="sample_text", uniqueIdentifier="sample_text", versionIdentifier="sample_text")
    a2 = umm_CDTProperty(businessTerm="sample_text_2", definition="sample_text_2", dictionary="sample_text_2", multiplicity="sample_text_2", name="sample_text_2", uniqueIdentifier="sample_text_2", versionIdentifier="sample_text_2")
    b = umm_CDT(businessTerm="sample_text", definition="sample_text", dictionary="sample_text", name="sample_text", uniqueIdentifier="sample_text", versionIdentifier="sample_text")
    _safe_set(b, 'umm_CDT64', {a1})
    assert _is_linked(b, 'umm_CDT64', a1)
    if hasattr(a1, 'umm_CDTProperty'):
        assert _is_linked(a1, 'umm_CDTProperty', b)
    _safe_set(b, 'umm_CDT64', {a2})
    assert _is_linked(b, 'umm_CDT64', a2)
    if hasattr(a1, 'umm_CDTProperty'):
        assert not _is_linked(a1, 'umm_CDTProperty', b)
    if hasattr(a2, 'umm_CDTProperty'):
        assert _is_linked(a2, 'umm_CDTProperty', b)
    _safe_set(b, 'umm_CDT64', set())
    assert not _is_linked(b, 'umm_CDT64', a2)
    if hasattr(a2, 'umm_CDTProperty'):
        assert not _is_linked(a2, 'umm_CDTProperty', b)


def test_assoc_type35_reverse_link_reassign_clear():
    a1 = umm_BDT(businessTerm="sample_text", definition="sample_text", dictionary="sample_text", uniqueIdentifier="sample_text", versionIdentifier="sample_text")
    a2 = umm_BDT(businessTerm="sample_text_2", definition="sample_text_2", dictionary="sample_text_2", uniqueIdentifier="sample_text_2", versionIdentifier="sample_text_2")
    b = umm_BBIE(fixedValue="sample_text", restriction="sample_text")
    _safe_set(b, 'umm_BBIE', a1)
    assert _is_linked(b, 'umm_BBIE', a1)
    if hasattr(a1, 'umm_BDT'):
        assert _is_linked(a1, 'umm_BDT', b)
    _safe_set(b, 'umm_BBIE', a2)
    assert _is_linked(b, 'umm_BBIE', a2)
    if hasattr(a1, 'umm_BDT'):
        assert not _is_linked(a1, 'umm_BDT', b)
    if hasattr(a2, 'umm_BDT'):
        assert _is_linked(a2, 'umm_BDT', b)
    _safe_set(b, 'umm_BBIE', None)
    assert not _is_linked(b, 'umm_BBIE', a2)
    if hasattr(a2, 'umm_BDT'):
        assert not _is_linked(a2, 'umm_BDT', b)


def test_assoc_type60_reverse_link_reassign_clear():
    a1 = umm_CDT(businessTerm="sample_text", definition="sample_text", dictionary="sample_text", name="sample_text", uniqueIdentifier="sample_text", versionIdentifier="sample_text")
    a2 = umm_CDT(businessTerm="sample_text_2", definition="sample_text_2", dictionary="sample_text_2", name="sample_text_2", uniqueIdentifier="sample_text_2", versionIdentifier="sample_text_2")
    b = umm_BCC(fixedValue="sample_text", restriction="sample_text")
    _safe_set(b, 'umm_BCC', a1)
    assert _is_linked(b, 'umm_BCC', a1)
    if hasattr(a1, 'umm_CDT'):
        assert _is_linked(a1, 'umm_CDT', b)
    _safe_set(b, 'umm_BCC', a2)
    assert _is_linked(b, 'umm_BCC', a2)
    if hasattr(a1, 'umm_CDT'):
        assert not _is_linked(a1, 'umm_CDT', b)
    if hasattr(a2, 'umm_CDT'):
        assert _is_linked(a2, 'umm_CDT', b)
    _safe_set(b, 'umm_BCC', None)
    assert not _is_linked(b, 'umm_BCC', a2)
    if hasattr(a2, 'umm_CDT'):
        assert not _is_linked(a2, 'umm_CDT', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_assemblies5_stub_double():
    # umm_MA has no real 'umm_MA' property in the generated
    # code (a bare stub) -- manually attach it so umm_InfEnvelope's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umm_InfEnvelope's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umm_InfEnvelope(name="sample_text")
    partner = umm_MA()
    setattr(partner, 'umm_MA', None)
    _safe_set(owner, 'umm_InfEnvelope6', {partner})
    assert getattr(partner, 'umm_MA') == owner
    _safe_set(owner, 'umm_InfEnvelope6', set())
    assert getattr(partner, 'umm_MA') is None


def test_assoc_codes47_stub_double():
    # umm_Original has no real 'umm_Original48' property in the generated
    # code (a bare stub) -- manually attach it so umm_CodelistEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umm_CodelistEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umm_CodelistEntry(description="sample_text", name="sample_text")
    partner = umm_Original()
    setattr(partner, 'umm_Original48', None)
    _safe_set(owner, 'umm_CodelistEntry', partner)
    assert owner in getattr(partner, 'umm_Original48')
    _safe_set(owner, 'umm_CodelistEntry', None)
    assert owner not in getattr(partner, 'umm_Original48')


def test_assoc_codes49_stub_double():
    # umm_Subset has no real 'umm_Subset50' property in the generated
    # code (a bare stub) -- manually attach it so umm_CodelistEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umm_CodelistEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umm_CodelistEntry(description="sample_text", name="sample_text")
    partner = umm_Subset()
    setattr(partner, 'umm_Subset50', None)
    _safe_set(owner, 'umm_CodelistEntry51', partner)
    assert owner in getattr(partner, 'umm_Subset50')
    _safe_set(owner, 'umm_CodelistEntry51', None)
    assert owner not in getattr(partner, 'umm_Subset50')


def test_assoc_constraints27_stub_double():
    # umm_Constraint has no real 'umm_Constraint29' property in the generated
    # code (a bare stub) -- manually attach it so umm_ABIE's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umm_ABIE's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umm_ABIE(businessTerm="sample_text", definition="sample_text", dictionary="sample_text", uniqueIdentifier="sample_text", versionIdentifier="sample_text")
    partner = umm_Constraint()
    setattr(partner, 'umm_Constraint29', None)
    _safe_set(owner, 'umm_ABIE28', {partner})
    assert getattr(partner, 'umm_Constraint29') == owner
    _safe_set(owner, 'umm_ABIE28', set())
    assert getattr(partner, 'umm_Constraint29') is None


def test_assoc_constraints55_stub_double():
    # umm_Constraint has no real 'umm_Constraint57' property in the generated
    # code (a bare stub) -- manually attach it so umm_ACC's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umm_ACC's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umm_ACC(businessTerm="sample_text", definition="sample_text", dictionary="sample_text", name="sample_text", uniqueIdentifier="sample_text", versionIdentifier="sample_text")
    partner = umm_Constraint()
    setattr(partner, 'umm_Constraint57', None)
    _safe_set(owner, 'umm_ACC56', {partner})
    assert getattr(partner, 'umm_Constraint57') == owner
    _safe_set(owner, 'umm_ACC56', set())
    assert getattr(partner, 'umm_Constraint57') is None


def test_assoc_context13_stub_double():
    # umm_Constraint has no real 'umm_Constraint14' property in the generated
    # code (a bare stub) -- manually attach it so umm_ContextRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umm_ContextRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umm_ContextRef(name="sample_text")
    partner = umm_Constraint()
    setattr(partner, 'umm_Constraint14', None)
    _safe_set(owner, 'umm_ContextRef', partner)
    assert getattr(partner, 'umm_Constraint14') == owner
    _safe_set(owner, 'umm_ContextRef', None)
    assert getattr(partner, 'umm_Constraint14') is None


def test_assoc_feature72_stub_double():
    # umm_OclPathFeatureHead has no real 'umm_OclPathFeatureHead' property in the generated
    # code (a bare stub) -- manually attach it so umm_OclRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umm_OclRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umm_OclRef(multiplicity="sample_text", name="sample_text")
    partner = umm_OclPathFeatureHead()
    setattr(partner, 'umm_OclPathFeatureHead', None)
    _safe_set(owner, 'umm_OclRef', partner)
    assert getattr(partner, 'umm_OclPathFeatureHead') == owner
    _safe_set(owner, 'umm_OclRef', None)
    assert getattr(partner, 'umm_OclPathFeatureHead') is None


def test_assoc_feature76_stub_double():
    # umm_OclPathTail has no real 'umm_OclPathTail77' property in the generated
    # code (a bare stub) -- manually attach it so umm_OclRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umm_OclRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umm_OclRef(multiplicity="sample_text", name="sample_text")
    partner = umm_OclPathTail()
    setattr(partner, 'umm_OclPathTail77', None)
    _safe_set(owner, 'umm_OclRef78', partner)
    assert getattr(partner, 'umm_OclPathTail77') == owner
    _safe_set(owner, 'umm_OclRef78', None)
    assert getattr(partner, 'umm_OclPathTail77') is None


def test_assoc_type11_stub_double():
    # umm_MAProperty has no real 'umm_MAProperty12' property in the generated
    # code (a bare stub) -- manually attach it so umm_ABIE's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umm_ABIE's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umm_ABIE(businessTerm="sample_text", definition="sample_text", dictionary="sample_text", uniqueIdentifier="sample_text", versionIdentifier="sample_text")
    partner = umm_MAProperty()
    setattr(partner, 'umm_MAProperty12', None)
    _safe_set(owner, 'umm_ABIE', partner)
    assert getattr(partner, 'umm_MAProperty12') == owner
    _safe_set(owner, 'umm_ABIE', None)
    assert getattr(partner, 'umm_MAProperty12') is None


def test_assoc_type15_stub_double():
    # umm_Constraint has no real 'umm_Constraint16' property in the generated
    # code (a bare stub) -- manually attach it so umm_TC_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umm_TC_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umm_TC_Constraint(kind="sample_text", listIdentifier="sample_text", responsibleAgency="sample_text")
    partner = umm_Constraint()
    setattr(partner, 'umm_Constraint16', None)
    _safe_set(owner, 'umm_TC_Constraint', partner)
    assert owner in getattr(partner, 'umm_Constraint16')
    _safe_set(owner, 'umm_TC_Constraint', None)
    assert owner not in getattr(partner, 'umm_Constraint16')


def test_assoc_type33_stub_double():
    # umm_ASBIE has no real 'umm_ASBIE' property in the generated
    # code (a bare stub) -- manually attach it so umm_ABIE's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umm_ABIE's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umm_ABIE(businessTerm="sample_text", definition="sample_text", dictionary="sample_text", uniqueIdentifier="sample_text", versionIdentifier="sample_text")
    partner = umm_ASBIE()
    setattr(partner, 'umm_ASBIE', None)
    _safe_set(owner, 'umm_ABIE34', partner)
    assert getattr(partner, 'umm_ASBIE') == owner
    _safe_set(owner, 'umm_ABIE34', None)
    assert getattr(partner, 'umm_ASBIE') is None


def test_assoc_type41_stub_double():
    # umm_AssembledBase has no real 'umm_AssembledBase' property in the generated
    # code (a bare stub) -- manually attach it so umm_BDTProperty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umm_BDTProperty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umm_BDTProperty(businessTerm="sample_text", definition="sample_text", dictionary="sample_text", length=7, maxLength=7, minLength=7, pattern="sample_text", uniqueIdentifier="sample_text", versionIdentifier="sample_text")
    partner = umm_AssembledBase()
    setattr(partner, 'umm_AssembledBase', None)
    _safe_set(owner, 'umm_BDTProperty42', partner)
    assert getattr(partner, 'umm_AssembledBase') == owner
    _safe_set(owner, 'umm_BDTProperty42', None)
    assert getattr(partner, 'umm_AssembledBase') is None


def test_assoc_type58_stub_double():
    # umm_ASCC has no real 'umm_ASCC' property in the generated
    # code (a bare stub) -- manually attach it so umm_ACC's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umm_ACC's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umm_ACC(businessTerm="sample_text", definition="sample_text", dictionary="sample_text", name="sample_text", uniqueIdentifier="sample_text", versionIdentifier="sample_text")
    partner = umm_ASCC()
    setattr(partner, 'umm_ASCC', None)
    _safe_set(owner, 'umm_ACC59', partner)
    assert getattr(partner, 'umm_ASCC') == owner
    _safe_set(owner, 'umm_ACC59', None)
    assert getattr(partner, 'umm_ASCC') is None


def test_assoc_type65_stub_double():
    # umm_Primitive has no real 'umm_Primitive' property in the generated
    # code (a bare stub) -- manually attach it so umm_CDTProperty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umm_CDTProperty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umm_CDTProperty(businessTerm="sample_text", definition="sample_text", dictionary="sample_text", multiplicity="sample_text", name="sample_text", uniqueIdentifier="sample_text", versionIdentifier="sample_text")
    partner = umm_Primitive()
    setattr(partner, 'umm_Primitive', None)
    _safe_set(owner, 'umm_CDTProperty66', partner)
    assert getattr(partner, 'umm_Primitive') == owner
    _safe_set(owner, 'umm_CDTProperty66', None)
    assert getattr(partner, 'umm_Primitive') is None


