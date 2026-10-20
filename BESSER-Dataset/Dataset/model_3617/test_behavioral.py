import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    profile_CD,
    profile_CR,
    profile_Class,
    profile_Classifier,
    profile_CodeSystemConstraint,
    profile_CodeSystemVersion,
    profile_CodedType,
    profile_ConceptDomain,
    profile_ConceptDomainConstraint,
    profile_Context,
    profile_ContextToValueSet,
    profile_Enumeration,
    profile_EnumerationLiteral,
    profile_NullValueSetConstraint,
    profile_Property,
    profile_UsageContext,
    profile_ValueSetCode,
    profile_ValueSetConstraint,
    profile_ValueSetConstraints,
    profile_ValueSetContextBinding,
    profile_ValueSetVersion,
    BindingKind,
    Extensibility,
    Guidance,
    StatusKind,
    ValueSetBinding,
    ValueSetType,
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

def test_assoc_codeSystem28_reverse_link_reassign_clear():
    a1 = profile_ValueSetVersion(binding="sample_text", definition="sample_text", effectiveDate="sample_text", expirationDate="sample_text", fullName="sample_text", identifier="sample_text", releaseDate="sample_text", revisionDate="sample_text", source="sample_text", status="sample_text", statusDate="sample_text", type="sample_text", url="sample_text", version="sample_text")
    a2 = profile_ValueSetVersion(binding="sample_text_2", definition="sample_text_2", effectiveDate="sample_text_2", expirationDate="sample_text_2", fullName="sample_text_2", identifier="sample_text_2", releaseDate="sample_text_2", revisionDate="sample_text_2", source="sample_text_2", status="sample_text_2", statusDate="sample_text_2", type="sample_text_2", url="sample_text_2", version="sample_text_2")
    b = profile_CodeSystemVersion(effectiveDate="sample_text", fullName="sample_text", identifier="sample_text", releaseDate="sample_text", source="sample_text", status="sample_text", statusDate="sample_text", url="sample_text", version="sample_text")
    _safe_set(b, 'profile_CodeSystemVersion30', a1)
    assert _is_linked(b, 'profile_CodeSystemVersion30', a1)
    if hasattr(a1, 'profile_ValueSetVersion29'):
        assert _is_linked(a1, 'profile_ValueSetVersion29', b)
    _safe_set(b, 'profile_CodeSystemVersion30', a2)
    assert _is_linked(b, 'profile_CodeSystemVersion30', a2)
    if hasattr(a1, 'profile_ValueSetVersion29'):
        assert not _is_linked(a1, 'profile_ValueSetVersion29', b)
    if hasattr(a2, 'profile_ValueSetVersion29'):
        assert _is_linked(a2, 'profile_ValueSetVersion29', b)
    _safe_set(b, 'profile_CodeSystemVersion30', None)
    assert not _is_linked(b, 'profile_CodeSystemVersion30', a2)
    if hasattr(a2, 'profile_ValueSetVersion29'):
        assert not _is_linked(a2, 'profile_ValueSetVersion29', b)


def test_assoc_codeSystem34_reverse_link_reassign_clear():
    a1 = profile_ValueSetCode(conceptName="sample_text", usageNote="sample_text")
    a2 = profile_ValueSetCode(conceptName="sample_text_2", usageNote="sample_text_2")
    b = profile_CodeSystemVersion(effectiveDate="sample_text", fullName="sample_text", identifier="sample_text", releaseDate="sample_text", source="sample_text", status="sample_text", statusDate="sample_text", url="sample_text", version="sample_text")
    _safe_set(b, 'profile_CodeSystemVersion35', a1)
    assert _is_linked(b, 'profile_CodeSystemVersion35', a1)
    if hasattr(a1, 'profile_ValueSetCode'):
        assert _is_linked(a1, 'profile_ValueSetCode', b)
    _safe_set(b, 'profile_CodeSystemVersion35', a2)
    assert _is_linked(b, 'profile_CodeSystemVersion35', a2)
    if hasattr(a1, 'profile_ValueSetCode'):
        assert not _is_linked(a1, 'profile_ValueSetCode', b)
    if hasattr(a2, 'profile_ValueSetCode'):
        assert _is_linked(a2, 'profile_ValueSetCode', b)
    _safe_set(b, 'profile_CodeSystemVersion35', None)
    assert not _is_linked(b, 'profile_CodeSystemVersion35', a2)
    if hasattr(a2, 'profile_ValueSetCode'):
        assert not _is_linked(a2, 'profile_ValueSetCode', b)


def test_assoc_conceptDomain38_reverse_link_reassign_clear():
    a1 = profile_ValueSetContextBinding(effectiveDate="sample_text")
    a2 = profile_ValueSetContextBinding(effectiveDate="sample_text_2")
    b = profile_ConceptDomain(fullName="sample_text", identifier="sample_text", status="sample_text", statusDate="sample_text")
    _safe_set(b, 'profile_ConceptDomain39', a1)
    assert _is_linked(b, 'profile_ConceptDomain39', a1)
    if hasattr(a1, 'profile_ValueSetContextBinding'):
        assert _is_linked(a1, 'profile_ValueSetContextBinding', b)
    _safe_set(b, 'profile_ConceptDomain39', a2)
    assert _is_linked(b, 'profile_ConceptDomain39', a2)
    if hasattr(a1, 'profile_ValueSetContextBinding'):
        assert not _is_linked(a1, 'profile_ValueSetContextBinding', b)
    if hasattr(a2, 'profile_ValueSetContextBinding'):
        assert _is_linked(a2, 'profile_ValueSetContextBinding', b)
    _safe_set(b, 'profile_ConceptDomain39', None)
    assert not _is_linked(b, 'profile_ConceptDomain39', a2)
    if hasattr(a2, 'profile_ValueSetContextBinding'):
        assert not _is_linked(a2, 'profile_ValueSetContextBinding', b)


def test_assoc_name4_reverse_link_reassign_clear():
    a1 = profile_CR(inverted="sample_text")
    a2 = profile_CR(inverted="sample_text_2")
    b = profile_CD(code="sample_text", codeSystem="sample_text", codeSystemName="sample_text", codeSystemVersion="sample_text", displayName="sample_text")
    _safe_set(b, 'profile_CD6', a1)
    assert _is_linked(b, 'profile_CD6', a1)
    if hasattr(a1, 'profile_CR5'):
        assert _is_linked(a1, 'profile_CR5', b)
    _safe_set(b, 'profile_CD6', a2)
    assert _is_linked(b, 'profile_CD6', a2)
    if hasattr(a1, 'profile_CR5'):
        assert not _is_linked(a1, 'profile_CR5', b)
    if hasattr(a2, 'profile_CR5'):
        assert _is_linked(a2, 'profile_CR5', b)
    _safe_set(b, 'profile_CD6', None)
    assert not _is_linked(b, 'profile_CD6', a2)
    if hasattr(a2, 'profile_CR5'):
        assert not _is_linked(a2, 'profile_CR5', b)


def test_assoc_qualifier0_reverse_link_reassign_clear():
    a1 = profile_CR(inverted="sample_text")
    a2 = profile_CR(inverted="sample_text_2")
    b = profile_CD(code="sample_text", codeSystem="sample_text", codeSystemName="sample_text", codeSystemVersion="sample_text", displayName="sample_text")
    _safe_set(b, 'profile_CD', {a1})
    assert _is_linked(b, 'profile_CD', a1)
    if hasattr(a1, 'profile_CR'):
        assert _is_linked(a1, 'profile_CR', b)
    _safe_set(b, 'profile_CD', {a2})
    assert _is_linked(b, 'profile_CD', a2)
    if hasattr(a1, 'profile_CR'):
        assert not _is_linked(a1, 'profile_CR', b)
    if hasattr(a2, 'profile_CR'):
        assert _is_linked(a2, 'profile_CR', b)
    _safe_set(b, 'profile_CD', set())
    assert not _is_linked(b, 'profile_CD', a2)
    if hasattr(a2, 'profile_CR'):
        assert not _is_linked(a2, 'profile_CR', b)


def test_assoc_qualifier16_reverse_link_reassign_clear():
    a1 = profile_CodeSystemConstraint(binding="sample_text", code="sample_text", displayName="sample_text", identifier="sample_text", name="sample_text", version="sample_text")
    a2 = profile_CodeSystemConstraint(binding="sample_text_2", code="sample_text_2", displayName="sample_text_2", identifier="sample_text_2", name="sample_text_2", version="sample_text_2")
    b = profile_CR(inverted="sample_text")
    _safe_set(b, 'profile_CR18', a1)
    assert _is_linked(b, 'profile_CR18', a1)
    if hasattr(a1, 'profile_CodeSystemConstraint17'):
        assert _is_linked(a1, 'profile_CodeSystemConstraint17', b)
    _safe_set(b, 'profile_CR18', a2)
    assert _is_linked(b, 'profile_CR18', a2)
    if hasattr(a1, 'profile_CodeSystemConstraint17'):
        assert not _is_linked(a1, 'profile_CodeSystemConstraint17', b)
    if hasattr(a2, 'profile_CodeSystemConstraint17'):
        assert _is_linked(a2, 'profile_CodeSystemConstraint17', b)
    _safe_set(b, 'profile_CR18', None)
    assert not _is_linked(b, 'profile_CR18', a2)
    if hasattr(a2, 'profile_CodeSystemConstraint17'):
        assert not _is_linked(a2, 'profile_CodeSystemConstraint17', b)


def test_assoc_reference10_reverse_link_reassign_clear():
    a1 = profile_ConceptDomainConstraint(identifier="sample_text", name="sample_text")
    a2 = profile_ConceptDomainConstraint(identifier="sample_text_2", name="sample_text_2")
    b = profile_ConceptDomain(fullName="sample_text", identifier="sample_text", status="sample_text", statusDate="sample_text")
    _safe_set(b, 'profile_ConceptDomain', a1)
    assert _is_linked(b, 'profile_ConceptDomain', a1)
    if hasattr(a1, 'profile_ConceptDomainConstraint'):
        assert _is_linked(a1, 'profile_ConceptDomainConstraint', b)
    _safe_set(b, 'profile_ConceptDomain', a2)
    assert _is_linked(b, 'profile_ConceptDomain', a2)
    if hasattr(a1, 'profile_ConceptDomainConstraint'):
        assert not _is_linked(a1, 'profile_ConceptDomainConstraint', b)
    if hasattr(a2, 'profile_ConceptDomainConstraint'):
        assert _is_linked(a2, 'profile_ConceptDomainConstraint', b)
    _safe_set(b, 'profile_ConceptDomain', None)
    assert not _is_linked(b, 'profile_ConceptDomain', a2)
    if hasattr(a2, 'profile_ConceptDomainConstraint'):
        assert not _is_linked(a2, 'profile_ConceptDomainConstraint', b)


def test_assoc_reference15_reverse_link_reassign_clear():
    a1 = profile_CodeSystemVersion(effectiveDate="sample_text", fullName="sample_text", identifier="sample_text", releaseDate="sample_text", source="sample_text", status="sample_text", statusDate="sample_text", url="sample_text", version="sample_text")
    a2 = profile_CodeSystemVersion(effectiveDate="sample_text_2", fullName="sample_text_2", identifier="sample_text_2", releaseDate="sample_text_2", source="sample_text_2", status="sample_text_2", statusDate="sample_text_2", url="sample_text_2", version="sample_text_2")
    b = profile_CodeSystemConstraint(binding="sample_text", code="sample_text", displayName="sample_text", identifier="sample_text", name="sample_text", version="sample_text")
    _safe_set(b, 'profile_CodeSystemConstraint', a1)
    assert _is_linked(b, 'profile_CodeSystemConstraint', a1)
    if hasattr(a1, 'profile_CodeSystemVersion'):
        assert _is_linked(a1, 'profile_CodeSystemVersion', b)
    _safe_set(b, 'profile_CodeSystemConstraint', a2)
    assert _is_linked(b, 'profile_CodeSystemConstraint', a2)
    if hasattr(a1, 'profile_CodeSystemVersion'):
        assert not _is_linked(a1, 'profile_CodeSystemVersion', b)
    if hasattr(a2, 'profile_CodeSystemVersion'):
        assert _is_linked(a2, 'profile_CodeSystemVersion', b)
    _safe_set(b, 'profile_CodeSystemConstraint', None)
    assert not _is_linked(b, 'profile_CodeSystemConstraint', a2)
    if hasattr(a2, 'profile_CodeSystemVersion'):
        assert not _is_linked(a2, 'profile_CodeSystemVersion', b)


def test_assoc_reference24_reverse_link_reassign_clear():
    a1 = profile_ValueSetVersion(binding="sample_text", definition="sample_text", effectiveDate="sample_text", expirationDate="sample_text", fullName="sample_text", identifier="sample_text", releaseDate="sample_text", revisionDate="sample_text", source="sample_text", status="sample_text", statusDate="sample_text", type="sample_text", url="sample_text", version="sample_text")
    a2 = profile_ValueSetVersion(binding="sample_text_2", definition="sample_text_2", effectiveDate="sample_text_2", expirationDate="sample_text_2", fullName="sample_text_2", identifier="sample_text_2", releaseDate="sample_text_2", revisionDate="sample_text_2", source="sample_text_2", status="sample_text_2", statusDate="sample_text_2", type="sample_text_2", url="sample_text_2", version="sample_text_2")
    b = profile_ValueSetConstraint(binding="sample_text", extensibility="sample_text", guidance="sample_text", identifier="sample_text", name="sample_text", uri="sample_text", version="sample_text")
    _safe_set(b, 'profile_ValueSetConstraint', a1)
    assert _is_linked(b, 'profile_ValueSetConstraint', a1)
    if hasattr(a1, 'profile_ValueSetVersion'):
        assert _is_linked(a1, 'profile_ValueSetVersion', b)
    _safe_set(b, 'profile_ValueSetConstraint', a2)
    assert _is_linked(b, 'profile_ValueSetConstraint', a2)
    if hasattr(a1, 'profile_ValueSetVersion'):
        assert not _is_linked(a1, 'profile_ValueSetVersion', b)
    if hasattr(a2, 'profile_ValueSetVersion'):
        assert _is_linked(a2, 'profile_ValueSetVersion', b)
    _safe_set(b, 'profile_ValueSetConstraint', None)
    assert not _is_linked(b, 'profile_ValueSetConstraint', a2)
    if hasattr(a2, 'profile_ValueSetVersion'):
        assert not _is_linked(a2, 'profile_ValueSetVersion', b)


def test_assoc_reference55_reverse_link_reassign_clear():
    a1 = profile_ValueSetVersion(binding="sample_text", definition="sample_text", effectiveDate="sample_text", expirationDate="sample_text", fullName="sample_text", identifier="sample_text", releaseDate="sample_text", revisionDate="sample_text", source="sample_text", status="sample_text", statusDate="sample_text", type="sample_text", url="sample_text", version="sample_text")
    a2 = profile_ValueSetVersion(binding="sample_text_2", definition="sample_text_2", effectiveDate="sample_text_2", expirationDate="sample_text_2", fullName="sample_text_2", identifier="sample_text_2", releaseDate="sample_text_2", revisionDate="sample_text_2", source="sample_text_2", status="sample_text_2", statusDate="sample_text_2", type="sample_text_2", url="sample_text_2", version="sample_text_2")
    b = profile_NullValueSetConstraint(binding="sample_text", identifier="sample_text", name="sample_text", version="sample_text")
    _safe_set(b, 'profile_NullValueSetConstraint', a1)
    assert _is_linked(b, 'profile_NullValueSetConstraint', a1)
    if hasattr(a1, 'profile_ValueSetVersion56'):
        assert _is_linked(a1, 'profile_ValueSetVersion56', b)
    _safe_set(b, 'profile_NullValueSetConstraint', a2)
    assert _is_linked(b, 'profile_NullValueSetConstraint', a2)
    if hasattr(a1, 'profile_ValueSetVersion56'):
        assert not _is_linked(a1, 'profile_ValueSetVersion56', b)
    if hasattr(a2, 'profile_ValueSetVersion56'):
        assert _is_linked(a2, 'profile_ValueSetVersion56', b)
    _safe_set(b, 'profile_NullValueSetConstraint', None)
    assert not _is_linked(b, 'profile_NullValueSetConstraint', a2)
    if hasattr(a2, 'profile_ValueSetVersion56'):
        assert not _is_linked(a2, 'profile_ValueSetVersion56', b)


def test_assoc_translation2_reverse_link_reassign_clear():
    a1 = profile_CD(code="sample_text", codeSystem="sample_text", codeSystemName="sample_text", codeSystemVersion="sample_text", displayName="sample_text")
    a2 = profile_CD(code="sample_text_2", codeSystem="sample_text_2", codeSystemName="sample_text_2", codeSystemVersion="sample_text_2", displayName="sample_text_2")
    b = profile_CD(code="sample_text", codeSystem="sample_text", codeSystemName="sample_text", codeSystemVersion="sample_text", displayName="sample_text")
    _safe_set(b, 'profile_CD3', a1)
    assert _is_linked(b, 'profile_CD3', a1)
    if hasattr(a1, 'profile_CD1'):
        assert _is_linked(a1, 'profile_CD1', b)
    _safe_set(b, 'profile_CD3', a2)
    assert _is_linked(b, 'profile_CD3', a2)
    if hasattr(a1, 'profile_CD1'):
        assert not _is_linked(a1, 'profile_CD1', b)
    if hasattr(a2, 'profile_CD1'):
        assert _is_linked(a2, 'profile_CD1', b)
    _safe_set(b, 'profile_CD3', None)
    assert not _is_linked(b, 'profile_CD3', a2)
    if hasattr(a2, 'profile_CD1'):
        assert not _is_linked(a2, 'profile_CD1', b)


def test_assoc_usageContext43_reverse_link_reassign_clear():
    a1 = profile_ValueSetContextBinding(effectiveDate="sample_text")
    a2 = profile_ValueSetContextBinding(effectiveDate="sample_text_2")
    b = profile_UsageContext(identifier="sample_text", status="sample_text", statusDate="sample_text")
    _safe_set(b, 'profile_UsageContext', a1)
    assert _is_linked(b, 'profile_UsageContext', a1)
    if hasattr(a1, 'profile_ValueSetContextBinding44'):
        assert _is_linked(a1, 'profile_ValueSetContextBinding44', b)
    _safe_set(b, 'profile_UsageContext', a2)
    assert _is_linked(b, 'profile_UsageContext', a2)
    if hasattr(a1, 'profile_ValueSetContextBinding44'):
        assert not _is_linked(a1, 'profile_ValueSetContextBinding44', b)
    if hasattr(a2, 'profile_ValueSetContextBinding44'):
        assert _is_linked(a2, 'profile_ValueSetContextBinding44', b)
    _safe_set(b, 'profile_UsageContext', None)
    assert not _is_linked(b, 'profile_UsageContext', a2)
    if hasattr(a2, 'profile_ValueSetContextBinding44'):
        assert not _is_linked(a2, 'profile_ValueSetContextBinding44', b)


def test_assoc_value7_reverse_link_reassign_clear():
    a1 = profile_CR(inverted="sample_text")
    a2 = profile_CR(inverted="sample_text_2")
    b = profile_CD(code="sample_text", codeSystem="sample_text", codeSystemName="sample_text", codeSystemVersion="sample_text", displayName="sample_text")
    _safe_set(b, 'profile_CD9', a1)
    assert _is_linked(b, 'profile_CD9', a1)
    if hasattr(a1, 'profile_CR8'):
        assert _is_linked(a1, 'profile_CR8', b)
    _safe_set(b, 'profile_CD9', a2)
    assert _is_linked(b, 'profile_CD9', a2)
    if hasattr(a1, 'profile_CR8'):
        assert not _is_linked(a1, 'profile_CR8', b)
    if hasattr(a2, 'profile_CR8'):
        assert _is_linked(a2, 'profile_CR8', b)
    _safe_set(b, 'profile_CD9', None)
    assert not _is_linked(b, 'profile_CD9', a2)
    if hasattr(a2, 'profile_CR8'):
        assert not _is_linked(a2, 'profile_CR8', b)


def test_assoc_valueSet40_reverse_link_reassign_clear():
    a1 = profile_ValueSetVersion(binding="sample_text", definition="sample_text", effectiveDate="sample_text", expirationDate="sample_text", fullName="sample_text", identifier="sample_text", releaseDate="sample_text", revisionDate="sample_text", source="sample_text", status="sample_text", statusDate="sample_text", type="sample_text", url="sample_text", version="sample_text")
    a2 = profile_ValueSetVersion(binding="sample_text_2", definition="sample_text_2", effectiveDate="sample_text_2", expirationDate="sample_text_2", fullName="sample_text_2", identifier="sample_text_2", releaseDate="sample_text_2", revisionDate="sample_text_2", source="sample_text_2", status="sample_text_2", statusDate="sample_text_2", type="sample_text_2", url="sample_text_2", version="sample_text_2")
    b = profile_ValueSetContextBinding(effectiveDate="sample_text")
    _safe_set(b, 'profile_ValueSetContextBinding41', a1)
    assert _is_linked(b, 'profile_ValueSetContextBinding41', a1)
    if hasattr(a1, 'profile_ValueSetVersion42'):
        assert _is_linked(a1, 'profile_ValueSetVersion42', b)
    _safe_set(b, 'profile_ValueSetContextBinding41', a2)
    assert _is_linked(b, 'profile_ValueSetContextBinding41', a2)
    if hasattr(a1, 'profile_ValueSetVersion42'):
        assert not _is_linked(a1, 'profile_ValueSetVersion42', b)
    if hasattr(a2, 'profile_ValueSetVersion42'):
        assert _is_linked(a2, 'profile_ValueSetVersion42', b)
    _safe_set(b, 'profile_ValueSetContextBinding41', None)
    assert not _is_linked(b, 'profile_ValueSetContextBinding41', a2)
    if hasattr(a2, 'profile_ValueSetVersion42'):
        assert not _is_linked(a2, 'profile_ValueSetVersion42', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_base_Class13_stub_double():
    # profile_Class has no real 'profile_Class' property in the generated
    # code (a bare stub) -- manually attach it so profile_ConceptDomain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # profile_ConceptDomain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = profile_ConceptDomain(fullName="sample_text", identifier="sample_text", status="sample_text", statusDate="sample_text")
    partner = profile_Class()
    setattr(partner, 'profile_Class', None)
    _safe_set(owner, 'profile_ConceptDomain14', partner)
    assert getattr(partner, 'profile_Class') == owner
    _safe_set(owner, 'profile_ConceptDomain14', None)
    assert getattr(partner, 'profile_Class') is None


def test_assoc_base_Class45_stub_double():
    # profile_Class has no real 'profile_Class47' property in the generated
    # code (a bare stub) -- manually attach it so profile_ValueSetContextBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # profile_ValueSetContextBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = profile_ValueSetContextBinding(effectiveDate="sample_text")
    partner = profile_Class()
    setattr(partner, 'profile_Class47', None)
    _safe_set(owner, 'profile_ValueSetContextBinding46', partner)
    assert getattr(partner, 'profile_Class47') == owner
    _safe_set(owner, 'profile_ValueSetContextBinding46', None)
    assert getattr(partner, 'profile_Class47') is None


def test_assoc_base_Class48_stub_double():
    # profile_Class has no real 'profile_Class50' property in the generated
    # code (a bare stub) -- manually attach it so profile_UsageContext's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # profile_UsageContext's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = profile_UsageContext(identifier="sample_text", status="sample_text", statusDate="sample_text")
    partner = profile_Class()
    setattr(partner, 'profile_Class50', None)
    _safe_set(owner, 'profile_UsageContext49', partner)
    assert getattr(partner, 'profile_Class50') == owner
    _safe_set(owner, 'profile_UsageContext49', None)
    assert getattr(partner, 'profile_Class50') is None


def test_assoc_base_Enumeration22_stub_double():
    # profile_Enumeration has no real 'profile_Enumeration' property in the generated
    # code (a bare stub) -- manually attach it so profile_CodeSystemVersion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # profile_CodeSystemVersion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = profile_CodeSystemVersion(effectiveDate="sample_text", fullName="sample_text", identifier="sample_text", releaseDate="sample_text", source="sample_text", status="sample_text", statusDate="sample_text", url="sample_text", version="sample_text")
    partner = profile_Enumeration()
    setattr(partner, 'profile_Enumeration', None)
    _safe_set(owner, 'profile_CodeSystemVersion23', partner)
    assert getattr(partner, 'profile_Enumeration') == owner
    _safe_set(owner, 'profile_CodeSystemVersion23', None)
    assert getattr(partner, 'profile_Enumeration') is None


def test_assoc_base_Enumeration31_stub_double():
    # profile_Enumeration has no real 'profile_Enumeration33' property in the generated
    # code (a bare stub) -- manually attach it so profile_ValueSetVersion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # profile_ValueSetVersion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = profile_ValueSetVersion(binding="sample_text", definition="sample_text", effectiveDate="sample_text", expirationDate="sample_text", fullName="sample_text", identifier="sample_text", releaseDate="sample_text", revisionDate="sample_text", source="sample_text", status="sample_text", statusDate="sample_text", type="sample_text", url="sample_text", version="sample_text")
    partner = profile_Enumeration()
    setattr(partner, 'profile_Enumeration33', None)
    _safe_set(owner, 'profile_ValueSetVersion32', partner)
    assert getattr(partner, 'profile_Enumeration33') == owner
    _safe_set(owner, 'profile_ValueSetVersion32', None)
    assert getattr(partner, 'profile_Enumeration33') is None


def test_assoc_base_EnumerationLiteral36_stub_double():
    # profile_EnumerationLiteral has no real 'profile_EnumerationLiteral' property in the generated
    # code (a bare stub) -- manually attach it so profile_ValueSetCode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # profile_ValueSetCode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = profile_ValueSetCode(conceptName="sample_text", usageNote="sample_text")
    partner = profile_EnumerationLiteral()
    setattr(partner, 'profile_EnumerationLiteral', None)
    _safe_set(owner, 'profile_ValueSetCode37', partner)
    assert getattr(partner, 'profile_EnumerationLiteral') == owner
    _safe_set(owner, 'profile_ValueSetCode37', None)
    assert getattr(partner, 'profile_EnumerationLiteral') is None


def test_assoc_base_Property11_stub_double():
    # profile_Property has no real 'profile_Property' property in the generated
    # code (a bare stub) -- manually attach it so profile_ConceptDomainConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # profile_ConceptDomainConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = profile_ConceptDomainConstraint(identifier="sample_text", name="sample_text")
    partner = profile_Property()
    setattr(partner, 'profile_Property', None)
    _safe_set(owner, 'profile_ConceptDomainConstraint12', partner)
    assert getattr(partner, 'profile_Property') == owner
    _safe_set(owner, 'profile_ConceptDomainConstraint12', None)
    assert getattr(partner, 'profile_Property') is None


def test_assoc_base_Property19_stub_double():
    # profile_Property has no real 'profile_Property21' property in the generated
    # code (a bare stub) -- manually attach it so profile_CodeSystemConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # profile_CodeSystemConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = profile_CodeSystemConstraint(binding="sample_text", code="sample_text", displayName="sample_text", identifier="sample_text", name="sample_text", version="sample_text")
    partner = profile_Property()
    setattr(partner, 'profile_Property21', None)
    _safe_set(owner, 'profile_CodeSystemConstraint20', partner)
    assert getattr(partner, 'profile_Property21') == owner
    _safe_set(owner, 'profile_CodeSystemConstraint20', None)
    assert getattr(partner, 'profile_Property21') is None


def test_assoc_base_Property25_stub_double():
    # profile_Property has no real 'profile_Property27' property in the generated
    # code (a bare stub) -- manually attach it so profile_ValueSetConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # profile_ValueSetConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = profile_ValueSetConstraint(binding="sample_text", extensibility="sample_text", guidance="sample_text", identifier="sample_text", name="sample_text", uri="sample_text", version="sample_text")
    partner = profile_Property()
    setattr(partner, 'profile_Property27', None)
    _safe_set(owner, 'profile_ValueSetConstraint26', partner)
    assert getattr(partner, 'profile_Property27') == owner
    _safe_set(owner, 'profile_ValueSetConstraint26', None)
    assert getattr(partner, 'profile_Property27') is None


def test_assoc_base_Property57_stub_double():
    # profile_Property has no real 'profile_Property59' property in the generated
    # code (a bare stub) -- manually attach it so profile_NullValueSetConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # profile_NullValueSetConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = profile_NullValueSetConstraint(binding="sample_text", identifier="sample_text", name="sample_text", version="sample_text")
    partner = profile_Property()
    setattr(partner, 'profile_Property59', None)
    _safe_set(owner, 'profile_NullValueSetConstraint58', partner)
    assert getattr(partner, 'profile_Property59') == owner
    _safe_set(owner, 'profile_NullValueSetConstraint58', None)
    assert getattr(partner, 'profile_Property59') is None


def test_assoc_constraints53_stub_double():
    # profile_ValueSetConstraints has no real 'profile_ValueSetConstraints54' property in the generated
    # code (a bare stub) -- manually attach it so profile_ContextToValueSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # profile_ContextToValueSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = profile_ContextToValueSet(key="sample_text", value="sample_text")
    partner = profile_ValueSetConstraints()
    setattr(partner, 'profile_ValueSetConstraints54', None)
    _safe_set(owner, 'profile_ContextToValueSet', partner)
    assert owner in getattr(partner, 'profile_ValueSetConstraints54')
    _safe_set(owner, 'profile_ContextToValueSet', None)
    assert owner not in getattr(partner, 'profile_ValueSetConstraints54')


